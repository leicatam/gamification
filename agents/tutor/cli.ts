import Anthropic from "@anthropic-ai/sdk";
import { existsSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { createInterface } from "node:readline/promises";
import { fileURLToPath } from "node:url";

const MODEL = "claude-sonnet-4-6";
const MAX_TOKENS = 4096;
const STATE_PATH = ".opc-tutor-state.json";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = join(__dirname, "..", "..");

interface PriorKnowledge {
  corporate_finance: "none" | "basic" | "strong";
  hk_tax: "none" | "basic" | "strong";
  digital_tools: "none" | "basic" | "strong";
  ai_agents: "none" | "basic" | "strong";
}

interface Accessibility {
  type_size: "default" | "large" | "extra-large";
  voice_io: "off" | "on";
  pacing: "brisk" | "measured" | "slow";
  human_escalation_offered: boolean;
}

interface LearnerProfile {
  persona: "mid-career-pivot" | "pre-retirement" | "active-retiree" | "unknown";
  prior_knowledge: PriorKnowledge;
  motivation: string;
  goals: string[];
  accessibility: Accessibility;
  onboarding_complete: boolean;
  arc1_started: boolean;
  notes: string;
}

const initialProfile: LearnerProfile = {
  persona: "unknown",
  prior_knowledge: {
    corporate_finance: "none",
    hk_tax: "none",
    digital_tools: "none",
    ai_agents: "none",
  },
  motivation: "",
  goals: [],
  accessibility: {
    type_size: "default",
    voice_io: "off",
    pacing: "measured",
    human_escalation_offered: false,
  },
  onboarding_complete: false,
  arc1_started: false,
  notes: "",
};

function loadProfile(): LearnerProfile {
  if (!existsSync(STATE_PATH)) return structuredClone(initialProfile);
  return { ...initialProfile, ...JSON.parse(readFileSync(STATE_PATH, "utf8")) };
}

function saveProfile(p: LearnerProfile): void {
  writeFileSync(STATE_PATH, JSON.stringify(p, null, 2));
}

function loadStableSystemContent(): string {
  const tutorPrompt = readFileSync(join(REPO_ROOT, "agents/tutor/system-prompt.md"), "utf8");
  const dialogue = readFileSync(join(REPO_ROOT, "agents/tutor/onboarding-dialogue.md"), "utf8");
  const arc1 = readFileSync(join(REPO_ROOT, "content/arcs/01-why-opc-in-hk.md"), "utf8");

  const personasDir = join(REPO_ROOT, "content/personas");
  const personaFiles = readdirSync(personasDir).filter((f) => f.endsWith(".yaml")).sort();
  const personas = personaFiles
    .map((f) => `## Persona definition: ${f}\n\n${readFileSync(join(personasDir, f), "utf8")}`)
    .join("\n\n");

  return [
    "# Canonical tutor system prompt",
    tutorPrompt,
    "",
    "# Personas",
    personas,
    "",
    "# Onboarding dialogue specification",
    dialogue,
    "",
    "# Arc 1 — Why an OPC in Hong Kong, Why Now",
    arc1,
    "",
    "# CLI environment notes",
    "- The learner is using a text-only CLI. Voice I/O preferences are recorded in the profile, but the CLI cannot deliver voice yet — acknowledge this if the learner asks.",
    "- After every reply, call the `update_learner_profile` tool exactly once with any new information detected this turn (pass an empty object if nothing changed).",
    "- Set `onboarding_complete` to true only after Stage 7 of the onboarding dialogue is complete.",
  ].join("\n");
}

const updateProfileTool: Anthropic.Tool = {
  name: "update_learner_profile",
  description:
    "Record updates to the learner profile from this turn. Call exactly once per reply, after the learner-facing text.",
  input_schema: {
    type: "object",
    properties: {
      persona: {
        type: "string",
        enum: ["mid-career-pivot", "pre-retirement", "active-retiree", "unknown"],
      },
      prior_knowledge: {
        type: "object",
        properties: {
          corporate_finance: { type: "string", enum: ["none", "basic", "strong"] },
          hk_tax: { type: "string", enum: ["none", "basic", "strong"] },
          digital_tools: { type: "string", enum: ["none", "basic", "strong"] },
          ai_agents: { type: "string", enum: ["none", "basic", "strong"] },
        },
      },
      motivation: { type: "string" },
      goals: { type: "array", items: { type: "string" } },
      accessibility: {
        type: "object",
        properties: {
          type_size: { type: "string", enum: ["default", "large", "extra-large"] },
          voice_io: { type: "string", enum: ["off", "on"] },
          pacing: { type: "string", enum: ["brisk", "measured", "slow"] },
          human_escalation_offered: { type: "boolean" },
        },
      },
      onboarding_complete: { type: "boolean" },
      arc1_started: { type: "boolean" },
      notes: { type: "string" },
    },
  },
};

function mergeProfile(base: LearnerProfile, update: Record<string, unknown>): LearnerProfile {
  const next = structuredClone(base);
  if (typeof update.persona === "string") next.persona = update.persona as LearnerProfile["persona"];
  if (update.prior_knowledge && typeof update.prior_knowledge === "object") {
    Object.assign(next.prior_knowledge, update.prior_knowledge);
  }
  if (typeof update.motivation === "string" && update.motivation.length > 0) {
    next.motivation = update.motivation;
  }
  if (Array.isArray(update.goals)) next.goals = update.goals.filter((g): g is string => typeof g === "string");
  if (update.accessibility && typeof update.accessibility === "object") {
    Object.assign(next.accessibility, update.accessibility);
  }
  if (typeof update.onboarding_complete === "boolean") next.onboarding_complete = update.onboarding_complete;
  if (typeof update.arc1_started === "boolean") next.arc1_started = update.arc1_started;
  if (typeof update.notes === "string" && update.notes.length > 0) next.notes = update.notes;
  return next;
}

async function main(): Promise<void> {
  const client = new Anthropic();
  const stableContent = loadStableSystemContent();
  let profile = loadProfile();
  const isResume = existsSync(STATE_PATH);

  console.log(`[OPC Tutor — Hong Kong | model: ${MODEL}]`);
  console.log(`[State: ${isResume ? "resumed from " + STATE_PATH : "new session"}]`);
  console.log("[Type 'exit' or Ctrl-D to quit]\n");

  const rl = createInterface({ input: process.stdin, output: process.stdout });
  const messages: Anthropic.MessageParam[] = [];

  let nextAuto: string | null;
  if (!isResume) {
    nextAuto = "[New session — please begin with Stage 1 of the onboarding dialogue.]";
  } else if (!profile.onboarding_complete) {
    nextAuto =
      "[Resuming an in-progress onboarding session. The current profile is in your context. Pick up where it left off — do not restart Stage 1 if information is already filled in.]";
  } else if (!profile.arc1_started) {
    nextAuto = null;
  } else {
    nextAuto = "[Resuming Arc 1. Continue from where it left off, adapted to the saved persona.]";
  }

  if (profile.onboarding_complete && !profile.arc1_started) {
    console.log("[Onboarding already complete in saved state.]");
    const ans = (await rl.question("Continue to Arc 1 now? [y/n]: ")).trim().toLowerCase();
    if (ans !== "y" && ans !== "yes") {
      rl.close();
      return;
    }
    profile.arc1_started = true;
    saveProfile(profile);
    nextAuto =
      "[Learner has agreed to begin Arc 1. Please start with Section 1, adapted to the saved persona and prior knowledge.]";
  }

  while (true) {
    let userInput: string;
    if (nextAuto !== null) {
      userInput = nextAuto;
      nextAuto = null;
    } else {
      let raw: string;
      try {
        raw = (await rl.question("You: ")).trim();
      } catch {
        break;
      }
      if (raw === "exit" || raw === "quit") break;
      if (!raw) continue;
      userInput = raw;
    }

    const last = messages[messages.length - 1];
    let userContent: Anthropic.MessageParam["content"];
    if (last && last.role === "assistant" && Array.isArray(last.content)) {
      const toolUses = last.content.filter(
        (b): b is Anthropic.ToolUseBlock => b.type === "tool_use",
      );
      if (toolUses.length > 0) {
        userContent = [
          ...toolUses.map(
            (tu): Anthropic.ToolResultBlockParam => ({
              type: "tool_result",
              tool_use_id: tu.id,
              content: "Profile updated.",
            }),
          ),
          { type: "text", text: userInput },
        ];
      } else {
        userContent = userInput;
      }
    } else {
      userContent = userInput;
    }

    messages.push({ role: "user", content: userContent });

    const system: Anthropic.TextBlockParam[] = [
      { type: "text", text: stableContent, cache_control: { type: "ephemeral" } },
      { type: "text", text: "## Current learner profile\n\n" + JSON.stringify(profile, null, 2) },
    ];

    process.stdout.write("Tutor: ");
    const stream = client.messages.stream({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      system,
      tools: [updateProfileTool],
      messages,
    });
    stream.on("text", (delta) => process.stdout.write(delta));

    let message: Anthropic.Message;
    try {
      message = await stream.finalMessage();
    } catch (err) {
      console.error("\n[API error]", err instanceof Error ? err.message : err);
      messages.pop();
      continue;
    }
    process.stdout.write("\n\n");

    messages.push({ role: "assistant", content: message.content });

    for (const block of message.content) {
      if (block.type === "tool_use" && block.name === "update_learner_profile") {
        profile = mergeProfile(profile, block.input as Record<string, unknown>);
      }
    }
    saveProfile(profile);

    if (message.usage.cache_read_input_tokens || message.usage.cache_creation_input_tokens) {
      console.log(
        `[cache: read=${message.usage.cache_read_input_tokens ?? 0} write=${message.usage.cache_creation_input_tokens ?? 0} | input=${message.usage.input_tokens} output=${message.usage.output_tokens}]\n`,
      );
    }

    if (profile.onboarding_complete && !profile.arc1_started) {
      console.log(`[Onboarding complete — profile written to ${STATE_PATH}]`);
      const ans = (await rl.question("Continue to Arc 1 now? [y/n]: ")).trim().toLowerCase();
      if (ans !== "y" && ans !== "yes") break;
      profile.arc1_started = true;
      saveProfile(profile);
      nextAuto =
        "[Learner has agreed to begin Arc 1. Please start with Section 1, adapted to the saved persona and prior knowledge.]";
    }
  }

  rl.close();
  console.log(`\n[Profile saved to ${STATE_PATH}.]`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

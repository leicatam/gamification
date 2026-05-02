# Diagnostic onboarding dialogue

A 5-minute Socratic dialogue, run on first launch, that builds the initial learner profile and
classifies the persona. Used by the tutor agent before any Arc 1 content is shown.

The dialogue is open-ended; the tutor decides which probes to skip based on what the learner
volunteers. The flow below is a guideline, not a script.

Goals of the dialogue, in priority order:

1. Detect persona (mid-career-pivot / pre-retirement / active-retiree).
2. Set accessibility defaults (type size, voice I/O, pacing).
3. Establish prior knowledge across four axes (corporate finance, HK tax, digital tools, AI agents).
4. Capture motivation in the learner's own words.
5. Surface any human-escalation needs.

Hard ceiling: 5 minutes (~ 6-8 exchanges). If the dialogue runs long, the tutor closes it and
proceeds with what it has.

---

## Stage 1 — Welcome and accessibility (1 turn)

Tutor opens warmly and offers an accessibility choice up-front. This protects the active-retiree
persona, who otherwise may abandon if they hit small text in turn 2.

> "Welcome. Before we start, a quick question: would you like larger text, voice replies, or both?
> You can change this any time."

Branch:
- "Larger text" / "voice" / "both" → set accessibility profile, lean toward `active-retiree`.
- "Default is fine" / silent dismiss → leave defaults, no signal yet.

## Stage 2 — Open motivation probe (1 turn)

> "In a sentence or two, what brings you here? What would you like to be different a year from
> now?"

Capture the answer verbatim into `motivation`. This single question yields a strong persona
signal:

- "I want to formalize my consulting" / "tax efficiency on my freelance income" → mid-career.
- "I'm retiring in two years and want a vehicle" / "monetize my expertise" → pre-retirement.
- "Something to keep me busy" / "small income from my hobby" / "my daughter suggested this" →
  active-retiree.

## Stage 3 — Prior-knowledge probes (2-3 turns)

Each probe is one short question that returns a none/basic/strong reading. Tutor skips probes
where the answer is obvious from earlier turns.

Corporate finance:
> "If I said 'two-tier profits tax with a HK$2 million threshold', would that be familiar, vaguely
> familiar, or new to you?"

HK-specific tax:
> "Have you filed an IRD return as a sole proprietor or as a company before, or only as an
> individual?"

Digital tools:
> "How do you usually handle invoices and bookkeeping today — spreadsheet, accounting software,
> or someone else does it for you?"

AI agents:
> "Have you ever used an AI assistant for work tasks like drafting an email or summarizing a
> document?"

The tutor combines responses into the `prior_knowledge` block.

## Stage 4 — Persona classification (internal, no turn)

After Stages 1-3 the tutor classifies persona. If signals conflict, ask one disambiguating
question. Examples:

- Strong corporate-finance + mention of "retirement" → ask "Are you currently working, transitioning
  out, or already retired?"
- Strong digital tools + "small income from hobby" → ask "Are you doing this full-time or as a
  side activity?"

If still unclear, default to `pre-retirement` (the persona with the broadest content fit) and
revisit on subsequent turns.

## Stage 5 — Goal capture (1 turn)

> "If you finish this course and only one thing changes for you, what should it be?"

This reply seeds the readiness score's weighting. A learner whose goal is "incorporate within 90
days" weights Arc 2 heavily; one whose goal is "decide whether this is for me" weights Arc 1.

## Stage 6 — Human escalation offer (1 turn, only for active-retiree signal)

If the persona signal is `active-retiree`, the tutor offers the human-escalation path explicitly
before any content begins:

> "If at any point this feels like too much, you can ask me to slow down or to connect you with
> a human guide. Just say so. Should I keep that option visible at the top of every page?"

## Stage 7 — Handoff to Arc 1

The tutor summarizes briefly what it heard — to confirm and to demonstrate listening — and
transitions:

> "Here's what I picked up: [persona-appropriate summary in 2 sentences]. With that in mind,
> let's start with why a one-person HK Ltd is a thing people are even considering right now.
> Ready when you are."

The active-retiree summary uses simpler language and waits for an explicit "yes" before
advancing. The mid-career-pivot summary may skip the readiness check.

---

## Output of the dialogue

After Stage 7, the tutor writes the initial profile to the persistence layer:

```json
{
  "persona": "pre-retirement",
  "prior_knowledge": {
    "corporate_finance": "strong",
    "hk_tax": "basic",
    "digital_tools": "basic",
    "ai_agents": "none"
  },
  "motivation": "Monetize 30 years of pharma QA expertise without rebuilding a firm.",
  "goals": ["decide if HK Ltd fits", "draft NNC1 within 90 days"],
  "accessibility": {
    "type_size": "default",
    "voice_io": "off",
    "pacing": "measured",
    "human_escalation_offered": false
  }
}
```

This profile is the input to every subsequent tutor turn.

---

## Failure modes the tutor must handle

- **Learner won't engage with questions.** After two non-answers, tutor switches to a
  capability tour ("Here's what's inside; tell me which part interests you") and infers persona
  from clicks.
- **Learner answers inconsistently.** Tutor flags low-confidence persona and re-checks at the
  end of Arc 1 Section 1.
- **Learner volunteers sensitive info** (HKID number, bank details). Tutor declines to retain
  it, names why, and continues.
- **Learner is in distress or confused.** Tutor stops, acknowledges, and offers the human
  escalation path regardless of persona.

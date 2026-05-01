# Evaluation harness

Three eval suites validate the product before each release.

## 1. Golden Q&A per persona (`eval/golden-qa/`)

Hand-curated question-answer pairs, ~30 per persona, anchored in HK content. The tutor's reply
is graded by a separate judge model on:

- Factual correctness
- Persona-appropriate vocabulary and length
- Hard-rule compliance (no advice; no auto-file claims; first-use acronym definitions)

## 2. Persona classifier (`eval/persona-classifier/`)

Replays recorded onboarding dialogues and checks the tutor's persona classification against the
learner's self-reported persona at end of course. Target: >85% agreement.

## 3. Accessibility checks (`eval/accessibility/`)

- WCAG 2.2 AA scan on all rendered pages
- Voice I/O latency (target <2s round-trip)
- Large-type and extra-large-type rendering parity
- Keyboard-only navigation coverage

## Running

(Tooling lands when stack is selected. Until then this directory holds the test specs and
golden data only.)

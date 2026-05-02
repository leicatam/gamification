# Operational toolkit (Phase 2)

Phase 2 agents that operate on the learner's real OPC data once they graduate from the
education layer. Each agent is described here as a contract — inputs, outputs, and the
human-in-the-loop guardrail. Implementation lands when Phase 1 is validated with testers.

| Agent | Purpose | Auto-action allowed |
|---|---|---|
| Incorporation drafter | Generates NNC1, articles, first-board resolutions from learner inputs | No — human reviews and submits |
| Compliance calendar | Tracks NAR1, BR renewal, BIR51, audit, SCR updates; drafts filings | No — drafts only |
| Bookkeeping agent | Categorizes transactions, produces P&L and balance sheet, prepares audit working papers | No — categorizations confirmed by learner |
| Profits-tax assistant | Provisional tax estimates, BIR51 draft, surfaces offshore-source considerations | No — never files autonomously |
| Document vault | Versioned articles, contracts, board minutes, filings; tamper-evident timestamps | N/A (storage only) |
| Decision log | Records every agent action with human approval state | N/A (logging only) |

## Hard guardrails (apply to every agent)

1. No agent submits to Companies Registry, IRD, MPFA, or any bank portal autonomously.
2. Every output is draft-only until a human approves.
3. The product does not give legal or tax advice; agents flag advice-territory questions and
   defer.
4. Every agent action is logged in the decision log with input, output, approver, and timestamp.

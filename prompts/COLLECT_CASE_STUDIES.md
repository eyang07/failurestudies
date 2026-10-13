# Reusable Prompt: Collect Autoformalization Failure Cases

Set up and execute a bounded, multi-agent archival diagnostic study in this repository. Read `AGENTS.md`, `STUDY_PLAN.md`, and `protocols/archival-v1/PROTOCOL.md` first.

Assign independent collectors to FaithformBench, ProofFlow, Pistis, and Navier-Stokes lost in translation. Have each inspect the primary paper and relevant released artifacts, retrieve a small set of concrete case studies, and explain what the observed evidence does and does not establish. Focus on changed assumptions, weakened/trivialized conclusions, and bypassed argument structure, while retaining other well-supported mechanisms.

Give each collector the role instructions in `instructions/COLLECTOR.md` and an unused ID range from the protocol. Collectors write only their own versioned import bundles. They must preserve source inputs and published outputs separately from interpretations, identify exact versions and locators, record unavailable prompts/settings as unknown, and distinguish reported failures from source defects and successful comparisons.

Do not conduct new formalization runs, train models, repair proofs, or claim that published Lean code has been independently verified. Do not manufacture examples or source details to fill a quota. A new run requires a separately approved, frozen experimental protocol.

As coordinator, validate and review all submissions before importing them into the shared registry. Check ownership, IDs, primary-source attribution, transcription status, label evidence, and family grouping. An independent reviewer should examine representative high-impact findings and possible overclaims. Keep unresolved judgments provisional. Do not mark findings confirmed merely because a collector or reviewer agrees with a paper.

Deliver: populated case packets; provenance-linked findings; a case index; missing-artifact and reproduction-readiness notes; a record of review decisions; and a short summary separating observed published evidence, our tentative interpretation, and unanswered causal questions. Do not infer population frequencies from this curated collection. Commit and push the reviewed changes to the existing private repository after excluding restricted raw sources and secrets.

This prompt authorizes collector and reviewer subagents for archival work only. On a subsequent invocation, allocate new IDs and preserve prior artifacts rather than overwriting them.

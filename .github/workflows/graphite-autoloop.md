---
description: |
  Run one measurable Graphite Mountain improvement experiment for an open
  issue labelled `graphite-program`, keeping only candidates that improve the
  declared metric while all regression checks pass.
on:
  schedule: every 12h
  workflow_dispatch:
    inputs:
      issue:
        description: "Optional Graphite Program issue number to run"
        required: false
        type: string
  slash_command:
    name: graphite-autoloop
permissions: read-all
timeout-minutes: 45
max-daily-ai-credits: 100K
network:
  allowed:
    - defaults
safe-outputs:
  max-patch-size: 10240
  add-comment:
    max: 8
    target: "*"
    hide-older-comments: false
  create-pull-request:
    draft: true
    labels: [automation, graphite-program]
    preserve-branch-name: true
    max: 1
  push-to-pull-request-branch:
    target: "*"
    required-labels: [graphite-program]
  add-labels:
    target: "*"
    max: 2
  remove-labels:
    target: "*"
    max: 2
tools:
  github:
    allowed-repos: ["wilfgrainger/graphite-mountain"]
    min-integrity: approved
    approval-labels: ["graphite-approved"]
    toolsets: [issues, pull_requests, repos]
  bash: true
  edit: true
  repo-memory:
    branch-name: memory/graphite-autoloop
    file-glob: [".graphite/programs/*.md"]
    max-file-size: 40960
engine: copilot
---

# Graphite Autoloop

Run exactly one bounded experiment for one open issue labelled `graphite-program`. The issue is the program contract; the memory file is the run ledger; the draft PR is the review surface.

## Quality gate

Before editing, require a goal, bounded target files, a numeric evaluator, metric
direction, a reproducible baseline, regression checks, constraints, a model profile and
per-run/total budget, and a plateau or blocked stop condition. If any are missing,
comment with the missing fields and stop.

## Select one program

Use the issue from the workflow event or optional `issue` input when one is present. Otherwise list open issues with the exact `graphite-program` label and choose the oldest active issue; choose only one. Skip issues labelled `graphite-program-completed` or `graphite-program-blocked`. If no eligible issue exists, stop without changing files or creating a PR. Derive the canonical implementation branch as `graphite/autoloop-<issue-number>` and reuse it on every run; find an existing draft PR for that branch before creating one.

## One-experiment loop

1. Read repository instructions, the issue, new human comments, prior memory, and the current branch/PR.
2. Run the evaluator against the current baseline and record the exact numeric output, selected model profile, actual provider/model/effort when exposed, and budget remaining.
3. Choose one falsifiable hypothesis and one smallest candidate change.
4. Change only the declared target files.
5. Run the evaluator and every required regression check.
6. Retain the candidate only if the metric improves in the declared direction and regressions pass; otherwise discard it and explain why.
7. Update memory and post a comment with the baseline, model and budget record, hypothesis, candidate, metric, regressions, and decision.
8. Mark the program complete only when its target metric and contract are satisfied. Otherwise select a different hypothesis on the next run; do not repeat a rejected path without new evidence.

## Decisions

```text
retain: metric improved and regressions passed
reject: metric did not improve or regressions failed; candidate discarded
blocked: evidence, authority, dependency, or budget is missing
complete: target metric and completion contract are satisfied
```

Never keep a change because it is interesting or larger. Never merge or deploy the draft PR automatically.

## Model strategy

Use a strong reasoning profile for ambiguous hypothesis selection or independent review,
and a cheaper coding profile for a bounded candidate when it is demonstrably adequate.
The evaluator must remain deterministic and independent of the model's preference. If
the runtime cannot expose the chosen model or effort, record `runtime default
unavailable`; do not invent a model name. Model selection never overrides the issue
contract, approval label, budget, regression checks, or human release authority.

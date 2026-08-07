<div align="center">

# Graphite Mountain

### Evidence-led software delivery. Human judgment at every gate.

An open-source, evidence-led multi-agent development team for substantial software work.

[![Validate](https://github.com/wilfgrainger/graphite-mountain/actions/workflows/validate.yml/badge.svg)](https://github.com/wilfgrainger/graphite-mountain/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/wilfgrainger/graphite-mountain?display_name=tag&sort=semver)](https://github.com/wilfgrainger/graphite-mountain/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-111827.svg)](LICENSE)
[![Lifecycle](https://img.shields.io/badge/lifecycle-4%20gated%20stages-2dd4bf.svg)](skills/graphite-mountain/WORKFLOW.md)

[Explore the workflow](skills/graphite-mountain/WORKFLOW.md) · [Guided intake](#start-with-guided-questions) · [Choose a mode](#choose-a-mode) · [Meet the team](#the-team) · [Open the visual guide](docs/index.html) · [Install](#install)

</div>

---

## What it is

Graphite Mountain is one master skill, six specialist playbooks, and one coherent delivery lifecycle. It turns a broad software request into a requirements pack, an architecture decision, a verified release candidate, and an operable handover.

It can run with true subagents or sequentially in one capable agent. It never claims parallel work occurred when it did not.

> **Design principle:** quality before performance. Specialist lenses sharpen judgement; evidence, ownership, and delivery remain the point.

## At a glance

| | |
|---|---|
| **Lifecycle** | Requirements → Architecture → Construction & Verification → Deployment & Operations |
| **Team** | Jared, Richard Hendricks, Dinesh, Gilfoyle, Jian-Yang, and Erlich Bachman |
| **Default** | Comprehensive Requirements and Architecture for substantial work |
| **Evidence** | Facts, results, assumptions, decisions, risks, and unknowns stay explicitly separated |
| **Authority** | The user remains principal; consequential actions require real authority |
| **Delivery** | One reconciled result, one accountable owner per decision, independent review of the actual change |

## The lifecycle

```text
┌──────────────────────┐
│ 1. Requirements      │  Mission, users, journeys, constraints,
│                      │  acceptance, risk, proof, work units
└──────────┬───────────┘
           ↓ Gate 1
┌──────────────────────┐
│ 2. Architecture      │  Options, boundaries, data, security,
│                      │  reliability, verification, release design
└──────────┬───────────┘
           ↓ Gate 2
┌──────────────────────┐
│ 3. Construct & Verify│  Complete slices, tests, actual-diff review,
│                      │  correction, reproducible release candidate
└──────────┬───────────┘
           ↓ Gate 3
┌──────────────────────┐
│ 4. Deploy & Operate  │  Authority, rollout, real-environment proof,
│                      │  observability, rollback, recovery, handover
└──────────────────────┘
```

The stages are gates, not theatre. New evidence can reopen an earlier stage.

## Choose a mode

Start with the smallest mode that can materially change the outcome.

| Mode | Use it for |
|---|---|
| `full-team` | Substantial work that needs requirements, architecture, construction, verification, and release thinking |
| `review` | Inspecting the actual state of an existing repository and ranking evidence-led improvements |
| `rescue` | Stabilising stalled, broken, contradictory, or poorly handed-over work |
| `requirements` | Establishing the mission, journeys, constraints, acceptance criteria, risk, and proof |
| `architecture` | Comparing options and selecting coherent boundaries, contracts, controls, and recovery |
| `construct` | Building approved vertical slices with tests and independent actual-diff review |
| `release` | Assessing readiness or performing an authorised deployment and operational verification |
| `intake` | Running the bounded question sequence and recording answer cards before planning |
| `goal` | Working one evidence-backed GitHub objective, one checkpoint per run |
| `autoloop` | Running one measurable improvement experiment and retaining only evaluated gains |
| `issue-forge` | Scanning trusted repository state and creating deduplicated issues for human triage |
| `review-loop` | Independently reviewing a goal, pull request, or release candidate |
| named member | Applying one specialist lens while Jared remains lifecycle chair for substantial work |

## Start with guided questions

If the brief is incomplete, Graphite Mountain guides the conversation instead of guessing. It asks up to three related questions at a time, reflects each answer with its evidence and impact, then pauses for confirmation before crossing a lifecycle gate.

The intake sequence is:

1. **Outcome** — who needs what observable change, and why now?
2. **Target and truth** — what is in scope, and what is verified today?
3. **Journeys** — who must succeed, including operator, support, abuse, and recovery paths?
4. **Boundaries** — what must remain true, and what is explicitly out of scope?
5. **Proof** — what counts as success, and what would falsify the approach early?
6. **Authority and depth** — what actions are authorised, and how comprehensive should the work be?

Start a guided session with:

```text
Use Graphite Mountain in full-team mode. Start with the guided intake, ask no more than three questions at a time, reflect each answer with its evidence and impact, and pause for my confirmation before each lifecycle gate.
```

The complete question order and answer-card format live in [`skills/graphite-mountain/WORKFLOW.md`](skills/graphite-mountain/WORKFLOW.md).

## Agentic workflows and self-created issues

Graphite Mountain includes reusable, GitHub-native workflow sources for durable goals, measurable Autoloops, issue discovery, and independent review. They live in [`.github/workflows/`](.github/workflows/) as auditable Markdown and use explicit permissions, integrity floors, safe outputs, one-checkpoint runs, durable memory, one canonical branch and draft PR, and team-visible issue comments.

Issue Forge can create at most three evidence-backed issues per run, but it never activates them. A maintainer reviews the evidence, strengthens the completion contract if needed, and applies `graphite-goal` or `graphite-program` deliberately. See the [workflow operating guide](skills/graphite-mountain/WORKFLOWS.md) and [GitHub setup guide](.github/workflows/README.md).

The committed `.lock.yml` files are generated workflow runtimes, not inert examples. Review or disable them before publishing a fork if you do not intend to run scheduled automation. Autoloop is opt-in through a reviewed issue, the `graphite-approved` label, a declared baseline, evaluator, budget, and stop condition; it produces a draft PR and evidence, never an automatic merge or deployment.

## Model suggestions

Choose a capability profile before a model brand or model ID. Record the exact provider/model, reasoning effort, tools, budget, fallback, and evidence date when they affect the work. A sensible default is:

| Work | Suggested profile | Why |
|---|---|---|
| Requirements, architecture, legal/IP issue-spotting, and review | Frontier reasoning at high effort; extra-high only for consequential uncertainty | These tasks resolve ambiguity and challenge assumptions |
| Construction and integration | Coding agent at medium or high effort | This is bounded execution with tests and actual-diff review |
| Autoloop | Strong planner/reviewer, cheaper executor where safe, deterministic evaluator every run | The metric decides retain/reject; the model proposes one experiment |
| Mechanical edits and issue discovery | Fast execution at none/low effort | Cost and latency matter when the task is well specified |

Model names and effort settings change. Current provider examples and the required run-record format live in [`skills/graphite-mountain/MODELS.md`](skills/graphite-mountain/MODELS.md). Never claim “built with GPT-6 Luna on Extra High” unless the exact model ID, setting, date, and run evidence are real.

## The team

| Canonical role | v0.x profile alias | The question they force the work to answer |
|---|---|---|
| **Delivery Chair** | Jared | Is the mission valuable, bounded, owned, sequenced, affordable, and provable? |
| **Architecture Lead** | Richard Hendricks | Which invariant, constraint, representation, or ethical boundary decides the approach? |
| **Engineering Lead** | Dinesh | Which complete user or caller path must work, and what is the cleanest practical implementation? |
| **Platform and Safety Lead** | Gilfoyle | Which trust boundary, failure mode, capacity limit, or recovery path decides whether this is safe to run? |
| **Adversarial Strategy Lead** | Jian-Yang | How can incentives, dependencies, claims, ownership, or competitors route around the intended outcome? |
| **Customer Advocate** | Erlich Bachman | Will the intended customer understand, trust, choose, use, adopt, and recommend this? |

The role names are now the durable contract. The aliases remain in v0.x so existing invocations and profile paths continue to work; new workflows and future surfaces use the professional role names first.

The six permanent roles are deliberately complemented by triggered advisors rather than a larger standing cast: Legal / Privacy Counsel for rights and regulated-data questions, Data / Evaluation for model and metric work, Product Design / Accessibility for customer journeys, and Release / Support Operations for live-system handover. Advisors add evidence and escalation; they do not grant authority or simulate sign-off.

Every member has equal rights to add context, challenge assumptions, propose changes, request evidence, and reopen decisions when new evidence matters. Accountability remains explicit: one chair, one decision owner, and one primary editor per bounded area.

## Install

The skill is plain Markdown and does not require a package manager, runtime service, or
platform-specific project layout. On any platform, clone or download the repository and
load [`skills/graphite-mountain/SKILL.md`](skills/graphite-mountain/SKILL.md) through the
agent runtime's documented skill mechanism. The skill folder is the portable unit; do not
copy only one profile or one workflow file.

For Claude Code users, the following clean-machine commands install the skill into the
standard user skill directory. Use the block for the shell you are running:

### macOS / Linux shell

This command temporarily clones the repository, installs the skill, and removes the checkout:

```bash
tmp="$(mktemp -d)"
git clone --depth 1 https://github.com/wilfgrainger/graphite-mountain.git "$tmp/graphite-mountain"
mkdir -p ~/.claude/skills
cp -R "$tmp/graphite-mountain/skills/graphite-mountain" ~/.claude/skills/
rm -rf "$tmp"
```

### Windows PowerShell

```powershell
$tmp = Join-Path ([System.IO.Path]::GetTempPath()) ("graphite-mountain-" + [guid]::NewGuid())
git clone --depth 1 https://github.com/wilfgrainger/graphite-mountain.git "$tmp\graphite-mountain"
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force "$tmp\graphite-mountain\skills\graphite-mountain" "$HOME\.claude\skills"
Remove-Item -Recurse -Force $tmp
```

If the runtime uses another skill directory, copy the same `skills/graphite-mountain`
folder to that runtime's documented location. Keep `AGENTS.md` as the repository policy;
do not create a second copy of the policy for each operating system.

Other runtimes can load [`skills/graphite-mountain/SKILL.md`](skills/graphite-mountain/SKILL.md) directly or add the folder to their skill-discovery path.

## Invoke

```text
Use Graphite Mountain in full-team mode to design and deliver this feature.
Use Graphite Mountain in review mode to inspect this repository and rank the improvements.
Use Graphite Mountain in rescue mode to stabilise this project and deliver the next proof point.
Use Graphite Mountain with Jared as chair and run a comprehensive requirements session.
Use Richard, Dinesh, and Gilfoyle to review this architecture and implementation.
Use Jian-Yang to challenge the claims, incentives, dependencies, and copyability.
Use Erlich as Voice of the Customer before we approve the requirements.
```

Available modes:

`full-team` · `requirements` · `architecture` · `construct` · `release` · `review` · `rescue` · `intake` · `goal` · `autoloop` · `issue-forge` · `review-loop` · any named team member

## Repository structure

```text
.
├── docs/
│   ├── index.html
│   ├── styles.css
│   ├── enhancements.css
│   ├── app.js
│   └── SHARING.md
├── scripts/
│   ├── validate.py
│   └── validate_ui.py
└── skills/graphite-mountain/
    ├── SKILL.md
    ├── MODELS.md
    ├── WORKFLOW.md
    └── team/
        ├── jared.md
        ├── richard-hendricks.md
        ├── dinesh.md
        ├── gilfoyle.md
        ├── jian-yang.md
        └── erlich-bachman.md
```

## Principles

- Evidence before confidence.
- Requirements before architecture; architecture before broad construction.
- Complete user journeys over isolated technical activity.
- Tests are part of construction, not a later ceremony.
- One editor per bounded area; independent review of the actual result.
- Security, accessibility, privacy, operability, migration, and rollback are design inputs.
- No deployment claim without target-environment evidence.
- No public claim stronger than the proof.
- Return to an earlier stage when evidence invalidates the current decision.

## Validate

```bash
python scripts/validate.py
python scripts/validate_ui.py
```

The validators check the skill contract, lifecycle, team, presence of the legal boundary, model guidance, static visual guide, responsive navigation, first-use modes, clean-machine install path, and progressive interactions. The same commands run in GitHub Actions.

## Status

Current version: **v0.0.1**

See the [changelog](CHANGELOG.md), [releases](https://github.com/wilfgrainger/graphite-mountain/releases), and [validation workflow](https://github.com/wilfgrainger/graphite-mountain/actions/workflows/validate.yml).

## Unofficial fan project

Graphite Mountain is an unofficial fan-inspired project. It is not affiliated with, endorsed by, or sponsored by HBO, Warner Bros. Discovery, or the creators or rights holders of *Silicon Valley*.

Character names are used as cultural references. This repository contains original methodology and writing; it does not include show logos, images, scripts, dialogue, audiovisual assets, or claims of official association. See [NOTICE.md](NOTICE.md).

Keep the humour and fan reference secondary to the original delivery method. “Parody” is not a blanket permission label; see the [public-sharing checklist](docs/SHARING.md) before a commercial, sponsored, or high-visibility launch.

## Contributing and security

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes and report vulnerabilities through the process in [SECURITY.md](SECURITY.md).

## Licence

The original code and documentation in this repository are released under the [MIT License](LICENSE). Third-party names and marks are not licensed by this repository.

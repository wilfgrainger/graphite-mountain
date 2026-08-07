# Graphite Delivery Lifecycle

This workflow is the operating system for Graphite Mountain. It is vendor-neutral, repository-aware, evidence-led, and designed for both single-agent and multi-agent execution.

It has four stages:

1. Requirements
2. Architecture
3. Construction & Verification
4. Deployment & Operations

The stages are gates, not a one-way conveyor belt. New evidence may send the team back to an earlier stage.

## Lifecycle governance

- The user is the principal and final authority.
- Jared is the standing delegated Product Owner, COO, and lifecycle chair.
- Every member has equal rights to contribute context, challenge, propose, request evidence, and reopen decisions.
- Domain accountability remains explicit.
- One primary editor owns each bounded area.
- The team returns one reconciled result.
- Humour never replaces evidence or action.

## Start here: establish truth and authority

Before planning, confirm or safely infer:

```text
Outcome: <observable customer or operational result>
Target: <repository, system, product, environment, or decision>
Current state: <verified branch, files, behaviour, tests, deployment, or production reality>
Constraints: <technical, legal, privacy, accessibility, cost, timing, compatibility, operational>
Authority: <read, edit, commit, push, merge, release, deploy, migrate, publish, delete>
Depth: <focused, standard, comprehensive>
```

Inspect repository instructions, current changes, delivery mechanisms, and evidence before prescribing a redesign.

## Guided intake: ask, reflect, then gate

When the user has not supplied a usable brief, do not jump straight to a plan or a persona performance. Run a short intake and make the answers visible before moving to the next gate.

Ask no more than three related questions in one turn. Skip anything the user has already answered, and do not ask for detail that cannot change scope, architecture, safety, cost, acceptance, or authority. After each reply:

1. **Reflect the answer** in plain language and label it as a fact, result, inference, assumption, decision, risk, or unknown.
2. **Show the consequence** — what the answer changes, leaves open, or rules out.
3. **Ask the next smallest set** of questions needed to close the current gate.
4. **Pause for confirmation** before treating a material assumption as accepted or advancing to the next gate.

Use this order unless the user supplies a better one:

| Round | Questions to guide the user through | Gate signal |
|---|---|---|
| 1. Outcome | Who needs what observable change, and why now? What happens if nothing changes? | Mission and value are bounded. |
| 2. Target and truth | Which repository, system, environment, or decision is in scope? What is verified today (files, behaviour, tests, deployment, or production state)? | Target and current state are evidenced. |
| 3. Journeys | Who are the primary, secondary, operator, support, abuse, and recovery actors? Which complete journey must work first? | Actors, permissions, failure paths, and accessibility needs are visible. |
| 4. Boundaries | What must remain true? What is explicitly out of scope? Which dependencies, compatibility, privacy, legal, cost, or timing constraints matter? | Scope and constraints are testable. |
| 5. Proof | What will count as success? Which checks would falsify the approach early? What evidence already exists? | Acceptance and requirement-to-proof links are explicit. |
| 6. Authority and depth | What may be read, edited, committed, pushed, merged, released, deployed, migrated, published, or deleted? How deep should this run: focused, standard, or comprehensive? | Actions are authorised and the work mode is proportionate. |

If an answer is unavailable, record a reversible assumption with an owner and a revisit trigger; do not silently convert a guess into a requirement. If the user asks to execute a consequential action without the required authority, stop at the exact authority gate and provide the ready handoff.

### Intake answer card

Capture each material answer in this compact form:

```text
Question: <the question asked>
Answer: <the user's answer or “not yet known”>
Evidence: <source, check, or “user-provided”>
Classification: <fact | result | inference | assumption | decision | risk | unknown>
Impact: <what this changes, rules out, or leaves open>
Owner / revisit: <who resolves it and when or on what trigger>
```

At the end of intake, show one reconciled summary containing the mission, target, current state, actors, constraints, acceptance, authority, open questions, and the selected mode. Ask the user to correct that summary before requirements or architecture are treated as approved.

# Stage 1 — Requirements

## Purpose

Determine what should change, for whom, why it matters, what must remain true, and how success will be recognised.

Substantial Graphite Mountain work defaults to comprehensive Requirements.

## Team questions

- **Jared:** Is the mission valuable, bounded, owned, sequenced, affordable, and compatible with commitments?
- **Erlich:** What does the customer actually need, understand, trust, adopt, and support—not merely what sounds impressive?
- **Richard:** Which technical invariants, feasibility limits, or ethical boundaries constrain the requirement?
- **Dinesh:** Which complete user or caller journeys must work, including failure and recovery?
- **Gilfoyle:** Which security, privacy, reliability, capacity, operational, and recovery requirements are missing?
- **Jian-Yang:** How can incentives, ambiguity, ownership, dependencies, competitors, or metric gaming invalidate the intended outcome?

## Requirements work

1. **Mission and problem**
   - identify the customer, user, operator, or stakeholder;
   - describe the current pain and desired observable change;
   - record why now and what happens if nothing changes.

2. **Current state**
   - inspect relevant code, data, architecture, tests, logs, interfaces, deployment, documentation, analytics, support evidence, and commitments;
   - separate fact from assumption;
   - identify constraints created by the existing system.

3. **Journeys and actors**
   - map primary, secondary, administrative, support, abuse, and recovery journeys;
   - include accessibility and internationalisation where relevant;
   - identify actors, permissions, incentives, and failure points.

4. **Requirements**
   - assign stable identifiers to material functional and non-functional requirements;
   - make them testable;
   - include security, privacy, performance, availability, resilience, capacity, compatibility, maintainability, observability, accessibility, support, cost, and legal needs where relevant.

5. **Acceptance and proof**
   - define observable acceptance criteria;
   - map each material requirement to intended proof;
   - identify evidence that can falsify the plan early.

6. **Scope**
   - define in-scope, non-goals, dependencies, assumptions, and deferred work;
   - split work into vertical units that can be built and proved independently.

7. **Risk and questions**
   - record consequence, likelihood or plausibility, mitigation, owner, trigger, and contingency;
   - ask only questions whose answers could change scope, architecture, safety, cost, or acceptance;
   - when the user cannot answer, research, inspect, prototype, or state a reversible assumption.

## Requirements Pack

Produce:

```text
Mission
Users and stakeholders
Current-state evidence
Journeys
Functional requirements
Non-functional requirements
Constraints and non-goals
Acceptance criteria
Requirement-to-proof map
Risks, assumptions, dependencies, and unknowns
Vertical work units and owners
Decisions required
```

## Gate 1 — Requirements ready

Proceed when:

- the outcome and acceptance criteria are clear enough to design;
- current state is sufficiently verified;
- material requirements are testable;
- critical unknowns are resolved, bounded, or explicitly accepted;
- scope, non-goals, dependencies, and work units are visible;
- the user or delegated authority accepts the Requirements Pack.

# Stage 2 — Architecture

## Purpose

Choose the smallest coherent system design that satisfies the Requirements Pack and can be built, verified, deployed, operated, and reversed responsibly.

## Architecture work

1. **Drivers and invariants**
   - rank the requirements that actually shape the design;
   - identify data, trust, latency, scale, availability, consistency, cost, compatibility, and ethical boundaries.

2. **Options**
   - compare at least the current/minimal option and one credible alternative when the decision is consequential;
   - assess complexity, delivery time, proof cost, migration, security, operability, lock-in, reversibility, and team comprehension;
   - do not manufacture alternatives for trivial decisions.

3. **System design**
   - define boundaries, components, responsibilities, data flow, state, interfaces, events, dependencies, failure behaviour, and ownership;
   - record diagrams as text or repository-native artefacts when useful;
   - identify what remains deliberately outside the system.

4. **Data and contracts**
   - define models, schemas, lifecycle, classification, ownership, retention, migration, validation, versioning, errors, idempotency, timeouts, retries, and compatibility.

5. **Security and privacy**
   - model assets, actors, entry points, trust boundaries, identity, permissions, secrets, abuse cases, auditability, and data minimisation;
   - choose controls proportionate to credible threats.

6. **Reliability and operations**
   - define service objectives or practical success thresholds;
   - cover capacity, quotas, degradation, backpressure, observability, alert ownership, backup, restore, rollback, and incident response.

7. **Construction strategy**
   - map vertical units to components and editors;
   - define integration order, feature flags, migrations, compatibility, and documentation;
   - identify the narrowest proof for high-risk claims.

8. **Verification strategy**
   - define unit, contract, integration, end-to-end, security, accessibility, performance, migration, rollback, and operational tests justified by risk;
   - preserve requirement-to-proof traceability.

9. **Deployment design**
   - define environments, artefacts, configuration, infrastructure, release strategy, verification, observability, rollback, recovery, and ownership before construction makes them expensive.

## Architecture Decision format

```text
Decision: <chosen approach>
Status: <proposed, accepted, superseded>
Drivers: <requirements and constraints>
Options: <credible alternatives>
Reason: <evidence and trade-off>
Consequences: <benefits, costs, risks, obligations>
Owner: <accountable role or user>
Revisit when: <specific trigger>
```

## Gate 2 — Architecture ready

Proceed when:

- one coherent design is selected;
- material alternatives and trade-offs are understood;
- system, data, interfaces, trust, failure, testing, migration, deployment, and recovery are designed at proportionate depth;
- units, editors, reviewers, integration order, and proof are defined;
- blocking team findings are resolved or explicitly accepted;
- the user or delegated authority approves construction.

# Stage 3 — Construction & Verification

## Purpose

Implement the approved design as the smallest complete, maintainable, tested, reviewable release candidate.

Testing is part of construction. It is not a later phase delegated to optimism.

## Before editing

- re-read the approved packs and repository instructions;
- verify branch, working tree, target paths, dependencies, and competing work;
- select the next vertical unit;
- state its requirement coverage, contracts, files, proof, migration, rollback, editor, and reviewers;
- return to Requirements or Architecture when new evidence invalidates the plan.

## Per-unit loop

1. **Unit contract** — define outcome, requirements, boundaries, stable interfaces, proof, owner, and completion.
2. **Detailed design** — specify only the implementation detail needed to code safely.
3. **Implement** — follow local conventions, keep the diff bounded, handle failure paths, preserve compatibility, instrument decision-relevant behaviour, and update affected documentation.
4. **Test continuously** — create focused tests alongside the change; include negative, boundary, permission, dependency, state, recovery, and regression cases where relevant.
5. **Inspect the actual diff** — include code, configuration, generated files, dependencies, lockfiles, migrations, documentation, and infrastructure.
6. **Independent review** — review evidence and actual changes, not the proposal.
7. **Correct** — send validated findings to the accountable editor; make the smallest complete correction.
8. **Prove** — run checks from focused to broad, proportionate to risk.
9. **Update traceability** — connect requirements, changes, tests, decisions, known limitations, and deferred work.

## Review responsibilities

- Jared: outcome, scope, acceptance, ownership, commitments, and release communication.
- Erlich: customer journey, language, usability, accessibility, onboarding, adoption, and support.
- Richard: architecture, algorithms, representation, performance, feasibility, and technical claims.
- Dinesh: implementation completeness, integration, contracts, maintainability, compatibility, and developer experience.
- Gilfoyle: security, platform, failure, observability, capacity, deployment, rollback, and recovery.
- Jian-Yang: incentives, loopholes, ownership, dependency, claims, copyability, substitution, and metric gaming.

Any member may propose and implement a correction when assigned a bounded area. The original editor must not self-certify consequential work without independent review.

## Proof order

Use relevant checks:

1. syntax, formatting, type, and static analysis;
2. focused unit and regression tests;
3. contracts and integration;
4. end-to-end journeys;
5. accessibility and security;
6. build, packaging, and reproducibility;
7. migration, rollback, restore, capacity, and performance;
8. broader repository suite.

Record what ran, where, against which version, the result, and limitations.

## Gate 3 — Release candidate ready

Proceed when:

- approved units are complete or explicitly descoped;
- requirement-to-proof traceability is current;
- decisive checks pass;
- actual changes received independent review;
- blocking findings are corrected;
- artefacts, configuration, migrations, documentation, and deployment instructions are ready;
- residual risk and limitations are explicit;
- the release candidate is reproducible from identified repository state.

# Stage 4 — Deployment & Operations

## Purpose

Release, verify, operate, support, and recover the result safely.

## Authority gate

Do not push, merge, publish, deploy, migrate production data, alter DNS, rotate or expose secrets, delete resources, enable paid services, or contact customers without authority for that action.

When authority is absent, complete the plan and exact handoff. Never imply deployment occurred.

## Deployment plan

```text
Release: <version, commit, artefact, or change set>
Environment: <target account, project, region, or host>
Owner: <release and incident owner>
Strategy: <rolling, canary, blue/green, recreate, feature flag, static publish, other>
Preconditions: <checks, backups, approvals, dependencies>
Migration: <ordered data and configuration steps>
Verification: <health, smoke, journeys, metrics, security>
Abort signals: <conditions that stop rollout>
Rollback: <trigger, steps, data implications>
Communication: <audience, message, owner>
```

## Pre-deployment readiness

Verify:

- approved source, artefacts, dependencies, and environments;
- identity, permissions, secrets, and configuration without disclosing them;
- infrastructure and configuration diffs;
- backups, recovery points, compatibility, quotas, capacity, certificates, domains, and dependencies;
- logs, metrics, traces, health checks, alerts, dashboards, runbooks, and ownership;
- customer impact, support readiness, cost, and rollback feasibility.

## Execute when authorised

1. capture pre-deployment state;
2. apply approved infrastructure and configuration;
3. run migrations in order;
4. deploy the identified release candidate;
5. bound rollout through environments, stages, canaries, or flags where appropriate;
6. observe abort signals;
7. record actual actions, versions, times, and outputs;
8. pause rather than bypass a failed safety control.

## Validate the real environment

Check:

- service and dependency health;
- critical customer, user, operator, and recovery journeys;
- permissions and isolation;
- data correctness and migration outcomes;
- logs, metrics, traces, alerts, latency, errors, saturation, and capacity;
- accessibility, device, integration, cache, CDN, DNS, certificate, and routing behaviour where relevant;
- rollback and recovery viability;
- unexpected cost, security, privacy, or data exposure.

A successful deployment command is not production proof.

## Release verdict

Jared reconciles:

```text
Verdict: <go, no-go, or go-with-conditions>
Evidence: <decisive environment proof>
Conditions: <owner, deadline, trigger>
Customer impact: <value, limitations, communication>
Rollback: <ready, used, or unavailable with reason>
Monitoring: <signals, period, owner>
```

Gilfoyle may issue a technical no-go for unresolved security, integrity, reliability, or recovery blockers. Dinesh may issue an integration no-go. Richard may block a disproved technical premise. Erlich may block a result that fails the agreed customer outcome. Jian-Yang may block a materially misleading claim or exploitable ownership/incentive flaw. Jared reconciles the recommendation; the user remains final authority.

## Operational handover

Leave:

- release identifier and change summary;
- architecture and operational deltas;
- health checks, dashboards, alerts, logs, and owners;
- runbook, incident path, backup, restore, rollback, and recovery;
- known issues, limitations, support guidance, and workarounds;
- customer or stakeholder communication;
- follow-up actions with owners and triggers;
- cleanup and decommissioning obligations;
- evidence of actual release state.

## Gate 4 — Delivered and operable

Complete when:

- release criteria are met or exceptions accepted;
- deployment status is truthful;
- critical journeys and operational signals are verified;
- support, ownership, rollback, and recovery are viable;
- residual risk and deferred work are explicit;
- the user receives one coherent report.

# Cross-stage controls

## Evidence strength

Prefer, in order:

1. reproduced behaviour, tests, logs, metrics, traces, benchmarks, or recovery exercises;
2. source, configuration, policies, manifests, schemas, and runtime state;
3. documentation confirmed against implementation;
4. reasoned inference;
5. unsupported claim.

Label inference and unsupported claims.

## Reopen rule

Return to an earlier stage when evidence changes:

- mission, scope, acceptance, or customer need;
- architecture or irreversible coupling;
- data ownership, privacy, security, or retention;
- performance, reliability, capacity, or cost assumptions;
- compatibility, migration, deployment, rollback, or recovery;
- a public commitment or claim.

Update the decision and traceability record rather than silently drifting.

## Decision rights

Every member has equal proposal and challenge rights. Decision ownership follows domain accountability. Jared chairs reconciliation. The user resolves accepted risk and any disagreement that remains material.

## Integrated delivery record

For substantial work, maintain repository-native artefacts where appropriate:

```text
docs/delivery/<work-slug>/
├── requirements.md
├── architecture.md
├── decisions.md
├── plan.md
├── verification.md
├── deployment.md
└── evidence.md
```

Do not create process files for tiny changes that do not need them.

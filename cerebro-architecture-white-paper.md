---
type: white-paper
date: 2026-05-27
version: v1.3.3-public
supersedes: cerebro-white-paper-v1.3.2-public.md (in-place §18.5 attribution-trim + rUv credit add + §17 #4 fanout-read truth-pass)
created_by: Claude Code (CC nexus) from three-vantage synthesis + tri-audit Round 1 + Round 2 reconciliation + Round 3 final-gate reconciliation + Round 4 founder OPSEC review + Round 5 §18.5 readability + §17 #4 MemoryWriter / fanout-read truth-pass
status: public-v1.3.3
audience: GovCon engineering · technology leadership · university faculty (LinkedIn release)
target_length: 22-25 pages
patches_applied:
  - Patch 1 (LiteLLM master-key removal §12 W3)
  - Patch 2.1a (championship bench v3-final table inserted as §10.1)
  - Patch 2.2 (swarm + Ruflo V3 pattern donor mention §7/§12)
  - Patch 2.3 (CUDA/GPU/Tailscale §3/§12 W4 depth)
  - Patch 2.4 (Codex + Hermes milestones §12 W3-W5)
  - Patch 4 (§18.5 Acknowledgments + Influences section)
  - Patch v1.2 (§17 #4 HUB-SEAMLESS promotion to accepted-limitation)
  - Patch v1.2 (§7.1 parallel-execution receipts A/B/C/D)
  - Patch v1.3 (tri-audit Round 2 reconciliation — Codex F1-F4 + Hermes S1-S5 + frontmatter sync + Pattern E mobile-dispatch)
  - Patch v1.3.1 (tri-audit Round 3 final-gate — F1 Tailscale IP redaction BLOCKER + F2 taxonomy reclassification + F3 article fix + F4/S1 §18.5 drafting-note strip MAJOR + F5 doctrine label fix + S2 audit-question reorder + S3 Pattern D deploy.sh generalization + S4 REMOVE-pending fix + D1 Pattern E ↔ §8 cross-reference)
  - Patch v1.3.2 (founder OPSEC review — §17 #4 stripped entirely + §17 #5 rewritten honest per actual MemoryWriter LIVE status + §17 #6 path-citations stripped + §17 renumbered 6→5 items + §17 intro taxonomy revised + §3 Layer 4 ssh-trust-topology phrasing softened + §14 attack-surface component lists generalized + §18.5 Perplexity/Nous Research/Tiago donor recognition added + Bumblebee added to substrate-research donors)
  - Patch v1.3.3 (§18.5 readability — stripped 4 skill-name enumeration blocks + intro inventory para, replaced with pointer to `VENDORED_IMPORTS.md` + per-tool `CEREBRO_CAVEATS.md`; added **rUv (Reuven Cohen / ruvnet)** to direct technical influences for `claude-flow` / Ruflo V3 substrate-active credit; cleaner human-readable layer, less inventory noise; ship target unchanged)
  - Patch v1.3.3 (§17 #4 truth-pass — old text claimed "unified MemoryWriter contract... implemented, tested, and live" which contradicts §6 + the 2026-05-19 supersession decision; MemoryWriter class was never built, Cerebro pivoted to fanout-READ via `cerebro_memory_check` MCP + W1 Qdrant collection scroll at Phase H wave H-1; §17 #4 rewritten to reflect actual fanout-read architecture, supersession reference added, per-source-writes-are-correct framing aligned with §6 architectural pivot block; cross-surface attribution coverage extension still paced behind Composer cutover as previously stated)
sources:
  - inputs/codex-third-party-analysis.md (Codex/OpenAI, external SME review)
  - inputs/cc-technical-analysis.md (Claude Code, inside-operator blind draft)
  - inputs/hermes-analysis.md (Hermes-on-hub, Anthropic-engineer framing)
  - synthesis.md (three-vantage reconciliation)
  - master-brain/white-paper/2026-05-21-cerebro-architecture/source-papers/* (codex architecture brief · third-party analysis · financial-monetization · outreach-pack · resume; hermes audit; cc full draft)
  - master-brain/handoffs/codex/2026-05-21-head-to-toe-system-gaps-weaknesses-fixes-paper.md (Codex exhaustive gap-paper)
  - master-brain/white-paper/2026-05-21-cerebro-architecture/source-papers/hermes-system-audit-gaps-fixes.md
  - master-brain/sessions/ (45-day session record)
  - master-brain/decisions/ (296 decision docs)
---

# Cerebro: Operator-Owned AI Infrastructure as a Governance Discipline

**A 45-Day Research-Driven Engineering Sprint Toward Audit-Ready, Reversible, Sovereign AI Operations**

*Cerebro Cyber Solutions · SDVOSB · 2026-05-21*

---

## Foreword

This paper documents what one operator built in 45 days, why the architecture turned out the way it did, and the doctrine that emerged when a regulated-industry context met a frontier-velocity build.

It is not a marketing brochure. It is a research report. Three independent peer architecture reviews — Codex (OpenAI, external SME), Claude Code (inside operator), and Hermes-on-hub (Anthropic-engineer framing) — were commissioned blind. Their outputs were reconciled into a single synthesis. The findings that survived all three vantages are what this paper anchors on. The disagreements that survived are documented honestly, because honest contradiction-naming is itself part of the doctrine.

If you read one section, read **§5 (Reversibility as a Design Primitive)**. That is the single most defensible architectural claim Cerebro makes.

If you read two, add **§4 (The Principle Framework)**. That is the IP package.

If you read three, add **§6 (Memory Architecture)**. That is what differentiates Cerebro from agent-as-prompt-wrapper systems.

The rest is supporting structure, honest production status, comparative context, and roadmap.

---

## 1. The Problem

A small operator in a regulated industry needs every one of the following at once:

1. **AI-native productivity** comparable to teams ten times larger.
2. **Audit-ready execution** acceptable to GovCon, CMMC, FedRAMP, IL5 procurement.
3. **Operator-owned data and inference**, because the customers cannot ship sensitive workloads to a third-party SaaS.
4. **Reversible change**, because mistakes in a one-person company cannot be absorbed by a team.
5. **Visible governance**, because regulators, primes, and certifying bodies want to see how decisions are made — not just what was decided.
6. **Mobile-operator workflow**, because real work happens between meetings, in cars, on phones.

None of these are individually novel. The combination is. Most agent frameworks optimize for one or two of these axes — usually 1 and 6. The remaining four are treated as future work. For a Service-Disabled-Veteran-Owned-Small-Business (SDVOSB) building toward GovCon, that prioritization is backwards. Audit-readiness and reversibility cannot be retrofitted onto a system that was designed for "ship first, document later."

Cerebro was built from the other end. The question was not "how do I get an agent to do useful work?" — that part is now commodity. The question was: **how do I run an AI-native company as infrastructure, so that every model call, memory write, workflow transition, and autonomous action has provenance, policy, and a rollback path?**

The answer turned out to require not new tools, but a new operating discipline.

---

## 2. The Thesis

> **A small operator can run an AI-native company if the company itself is implemented as infrastructure: memory, decisions, workflows, agents, models, and governance all live in versioned, inspectable, operator-owned systems.**

That sentence is the spine of everything that follows. It was written by Codex (OpenAI) in its third-party review, not by the operator. The fact that an external reviewer recognized it as the underlying architectural thesis — without being told — is itself a signal that the thesis is coherent, not retrofitted.

Three implications follow:

**(a) Tools are commodity. Operating discipline is the moat.** Any operator can buy a Claude Code subscription, an Ollama install, and a Qdrant instance. None of that is differentiating. What differentiates is the rules under which those tools are allowed to write, dispatch, remember, and act — and the rules under which the operator allows their own work to be governed by those rules.

**(b) The company *is* the codebase.** Decisions are committed. Handoffs are committed. Memory corrections are committed. Sessions are committed. If a regulator wants to see "how did you decide to do X on Tuesday," the answer is a git SHA and a decision document, not a memory or a Slack message.

**(c) Governance is architecture, not paperwork.** Hermes's analysis names this explicitly: *"These aren't values — they're load-bearing architectural constraints, the kind only seen in safety-critical systems (aerospace, medical devices, financial infrastructure)."* When a principle constrains where code can be written, what credentials can be touched, which surface can dispatch what action, and what must be reversible before mutation — the principle is part of the runtime, not the culture deck.

---

## 3. The Four-Layer Architecture

Cerebro is organized as four layers, each with its own governance posture and reversibility model.

```
┌─────────────────────────────────────────────────────────────────────┐
│  Layer 1 — BRAIN  (knowledge · decisions · narrative · sessions)    │
│           why-the-system-is + audit trail of every material change  │
├─────────────────────────────────────────────────────────────────────┤
│  Layer 2 — SKILLS  (workflows · SKILL.md · ritual contracts)        │
│           reusable operator workflows with declared scope contracts │
├─────────────────────────────────────────────────────────────────────┤
│  Layer 3 — AGENT RUNTIME  (Claude Code · Codex · Hermes · daemons)  │
│           the executors that compose, dispatch, and act             │
├─────────────────────────────────────────────────────────────────────┤
│  Layer 4 — FLEET  (prime-alpha · nexus · hub · prime · substrate)   │
│           local + cloud inference, services, vector store, mesh     │
└─────────────────────────────────────────────────────────────────────┘
```

Each layer has its own governance and Reversibility posture. Brain writes are append-mostly with supersession (never overwrite). Skills are scope-contracted (least privilege #7). Agent Runtime is allowlisted (paths + commands). Fleet is origin-policied (where the weights come from, where the tools come from).

**Layer 4 Fleet — physical and network detail.** The fleet is four physical nodes plus a substrate layer (Ollama / LiteLLM / Qdrant) bound together by a Tailscale private mesh. `prime-alpha` (64GB DDR5 / RTX 4090) is the primary GPU muscle and serves the Senior Advisor + autoresearch + composer-bench workloads. `nexus` (24GB workstation) is the authoring surface. `hub` (16GB services node) runs the LiteLLM gateway + Qdrant + the 24/7 Hermes Telegram composer + scheduled launchd jobs. `prime` (32GB / RTX 3080) is dormant backup. The hub services run as three Docker containers on a private `cerebro-net` bridge — `cerebro-litellm` (model-routing proxy), `cerebro-postgres` (LiteLLM backing store), and `cerebro-qdrant` (vector DB with seven collections). The Hermes Telegram composer is deliberately a host process (not containerized) because it needs direct filesystem access to `~/.hermes/` for kanban + memory state. Container choice is policy: substrate services with stable boundaries get containerized for Reversibility (pin image, snapshot volume, blue/green-swap on upgrade — see `decisions/2026-04-19-adr-003-qdrant-client-server-version-policy.md`); composers and orchestrators that need filesystem read/write across many host paths stay as host processes. The RTX 4090 build-out on `prime-alpha` produced a ~14× latency improvement over the prior dormant-backup configuration on Gemma 4 31B (1.75 → 25.38 tok/sec, Phase 6 50-prompt benchmark). The Tailscale mesh keeps every inter-node command on private infrastructure — no port is exposed to the public internet. The fleet is small enough that the operator knows every node by name; large enough that the routing matrix has meaningful choices. That sizing is intentional.

The four-layer model is not aesthetic. It is what allows the operator to answer four questions about any artifact without ambiguity:

1. *Where does this live?* — one of four layers.
2. *Who can change it?* — declared in the scope contract at that layer.
3. *How is the change reversible?* — declared in the principle that governs that layer.
4. *What audit trail does the change leave?* — a decision doc, a sessionend writeback, a commit SHA, or all three.

Codex's verdict: *"This is a legitimate platform architecture. Its primitives are not only AI models and prompts, but state, routing, memory, role separation, reversibility, and auditability."*

---

## 4. The Principle Framework (and Four Doctrines)

The principle framework is what every reviewer named as the moat. Nine principles. Four doctrines. Each one is ref-implemented in a real surface; none of them are aspirational.

### The Nine Principles

| # | Principle | What it constrains | Ref-implementation |
|---|-----------|--------------------|--------------------|
| 1 | **Governance** | Where data lives (department brains stay dept-local) | `BRAIN_GOVERNANCE.md` chain-of-command |
| 2 | **Parity** | Skills track architecture in the same session as the architecture changes | `sessionend` Step 7.5 Writeback Guard |
| 3 | **Lockstep** | Rollups (dashboard, awareness, memory) update in the same session as source-of-truth artifacts | Writeback Guard + `sessionend` enforcement |
| 4 | **Human-in-the-Mix** | Automation halts at drafts for relationship, sign-off, vendor outreach, regulator actions | `sessionend` Step 9 "Operator's Rebuttal" gate |
| 5 | **Reversibility** | Every material change leaves a rollback path; supersede, never overwrite | `state/memory-corrections.log` before-after pairs |
| 6 | **Observability** | Silent is a bug; subprocess >15s requires heartbeat; auto-corrections log before applying | `master-brain/skills/council-mode/Scripts/heartbeat.py` |
| 7 | **Least-Privilege** | Every skill declares scope contract: read paths, write paths, MCP/tool surface, network egress, credentials | Scope Contract block mandatory in `SKILL.md` |
| 8 | **Reproducibility** | Stage boundaries capture inputs + decision + trust-tag; render-target separation; multi-surface payloads enforce payload-first/render-second | `sessionstart` Stage 2.5 trust-tagging |
| 9 | **Self-Sufficiency** | Cerebro never depends on a runtime it does not own; external tools are pattern donors, not load-bearing dependencies | Constellation native runtime program |

Hermes's framing: *"These aren't culture — they're load-bearing architectural constraints. Most companies have culture documents. Cerebro has enforceable doctrine cross-walks."*

Codex's framing: *"Security is architectural, not an afterthought. Credentials, tools, routes, and origins are all policy surfaces."*

### The Four Doctrines

Beyond the principles, four operating doctrines govern specific decision classes:

1. **Absorption-pattern doctrine** — every external-tool intake follows five mandatory steps: origin gate → vendored reference clone → swarm-analyze extraction doc → cerebro-fit decision-doc-per-port-target → wiring with snapshot tag. *No more ad-hoc absorptions.* This doctrine was crystallized after nine absorptions in 72 hours threatened to overrun governance bandwidth.

2. **Diagram-First Doctrine** — multi-component architecture decisions ship with a visual. ASCII inline by default (zero cost, always works). Mermaid/HTML when relationships warrant. The diagram block lives directly under `## Why` in decision documents. *Closes the mental-model-vs-ground-truth drift class.*

3. **Origin Policy 3a/3b/3c** — model weights are "American-owned, American-sold" (research geography allowed). Tools and MCPs are licensed-permissive with hot-path code review and pinned commits. License gate (3c) added 2026-05-18 after a tools-origin question forced explicit license classification.

4. **Three-Surface Rule (SOP v1.3)** — work routes to one of three surfaces: Claude Code (git, Ollama, Mac-FS-outside-workspace, credentials), Operator (relationships, sign-offs, hard strategic calls), or Cowork (in-workspace edits, drafts). Sub-surface annex names four executors under Claude Code: Native CC, Codex TUI/exec, Ruflo daemon, Hermes runtime.

### Why this matters externally

A regulator does not need to learn Cerebro to evaluate Cerebro. The doctrine is the audit. Open the principles table, open the ref-impl pointer, run the probe, verify the constraint. The system explains itself.

Codex's evaluation: *"Decision docs, reversibility clauses, session rituals, handoffs, audits, diagrams, and explicit operating principles … the governance discipline is unusually mature for a solo project."*

This is the IP package. Everything else in this paper either depends on it or extends it.

---

## 5. Reversibility as a Design Primitive

Of every architectural choice Cerebro has made, Reversibility (Principle #5) is the most defensible single claim.

Hermes named it: *"Infrastructure time-travel as a design primitive … the single most mature aspect of the system."*

Codex named it: *"Reversibility is mature. Many changes include rollback paths before mutation."*

The principle is simple and load-bearing:

> **Every material change leaves a rollback path. State runs like a mirror: constant snapshot, always recoverable.**

In practice, this means:

- **Decision supersession, never deletion.** When a 2026-04-21 decision relaxed an earlier 2026-04-17 model-policy lock, the old decision was not overwritten. It was marked superseded. The earlier doctrine is still readable. Reversibility means: the audit trail does not gaslight you about what was true on Tuesday.

- **Memory corrections log before mutation.** When a memory claim is found drifted, the auto-correction logs the before-state to `state/memory-corrections.log` *before* writing the new state. Any correction is replayable. Any correction is reversible by reading the log entry and reverting.

- **Snapshot-tag-before-mutation.** Destructive operations (vendor refresh, plugin uninstall, schema migration) tag a git ref `pre-<operation>-<date>` *before* the operation runs. Rollback recipe is one cherry-pick.

- **Blue/green for production swaps.** Composer/inference substrate swaps go through dedicated swap scripts. Never live-swap. The previous configuration remains addressable.

- **Commented-out code, not deleted code.** When the sessionstart `PRIORITY_READ` block was de-wired 2026-05-21, the block was commented out, not removed. The wiring is single-line reversible.

- **`Brain/` capital-B retention.** When the kebab-case rename happened, the legacy capital-B `Brain/` references were preserved as case-insensitive-filesystem artifacts and annotated. The rename is reversible at the case level. (This sounds trivial. It is not. It is the difference between "we renamed" and "we have audit-grade proof of the rename's reversibility.")

Why this is a defensible architectural claim:

In safety-critical engineering (aerospace, medical devices, nuclear), the requirement is not *"don't make mistakes."* The requirement is *"every mistake must be recoverable to a known prior state."* Reversibility-as-design-primitive is the same posture, applied to a one-operator AI-native company. The architectural cost is real (every change carries a documentation overhead). The architectural payoff is also real: there is no irrecoverable state in the system.

Codex's formulation, after observing this pattern across 296 decision docs and a `memory-corrections.log` spanning the full 45 days:

> *"The best signal is not that every decision was right. It is that the system has visible supersession, correction, and rollback behavior. That is real engineering maturity."*

For GovCon and regulated-industry buyers, this is not a feature. It is a contractual posture. *"Show me your audit trail"* has a one-command answer.

---

## 6. The Memory Architecture {.page-break-before}

Memory is where most agent systems collapse. A chat history is not memory. A vector store dump is not memory. A YAML rules file is not memory. Memory is **identity + working set + semantic retrieval + audit trail + task state**, and those should not all live in the same store.

Cerebro's memory architecture evolved through observation, not initial design. The current shape:

| Tier | Name | Purpose | Backing store |
|------|------|---------|---------------|
| 1 | **Identity** | Always-loaded rules, preferences, guardrails | File memory (`MEMORY.md` + per-entry `.md` files with frontmatter) |
| 2 | **Reasoning** | Associative human-readable thinking, knowledge vault | Obsidian-LLM-wiki + `knowledge-vault/` |
| 3 | **Warehouse** | Semantic vector recall across full corpus | Qdrant on hub (seven collections: decisions, sessions, skills, knowledge-vault, memory-stream, research, Telegram-stream) |

Additional stores serving distinct jobs:

- **Process memory** — claude-flow / `.swarm/memory.db` for agent flows.
- **Audit memory** — `decisions/` and `sessions/` (chronological + canonical).
- **Active work** — kanban / Hermes board (mutable working set, distinct from frontmatter historical record).
- **Telegram stream** — Qdrant collection capturing conversational history from the mobile operator surface.

### The architectural pivot — why "fanout-read" is correct

The first draft of the memory architecture (April 2026) proposed a unified `MemoryWriter` contract: a single write path, fanout to all backends. This was wrong. Implementation revealed that strong write fanout is brittle:

- Every writer would need to understand every backend.
- One backend failure could block unrelated writes.
- Silent partial writes were impossible to detect without a global write transaction.

In May 2026, the unified-write contract was superseded. The new design: **per-source writes plus unified fanout-read.**

```
  ┌──────────────────────┐         ┌──────────────────────┐
  │ CC / Codex writes    │────────▶│ file memory          │
  │ Hermes writes        │────────▶│ Qdrant stream        │
  │ sessionend writes    │────────▶│ sessions + decisions │
  │ curator writes       │────────▶│ Qdrant collections   │
  └──────────────────────┘         └──────────┬───────────┘
                                              │
                                              ▼
                                   ┌──────────────────────┐
                                   │ unified read (recall)│◀── top-k context
                                   │ memory-check tool    │   with provenance
                                   └──────────────────────┘
```

Each writer writes to the store it knows. Retrieval is responsible for federation. Eventual consistency is accepted. The retrieval surface presents top-k context across all stores with provenance.

Codex's evaluation: *"Per-source write plus unified fanout-read … that is the correct call. This memory architecture is one of the strongest parts of the system. It reflects lessons frontier labs also learn: memory is not one thing."*

### What's solved, what's queued (the honest split)

**Solved on the primary write surface.** The 11-key memory attribution contract — `source_surface`, `host`, `tool`, `session_id`, `written_at_utc`, `source_path`, `confidence`, `lifecycle`, and three audit fields — is **live and enforced today** on Claude Code Write/Edit via a PreToolUse hook, on every `sessionend` write, on every decision-doc commit, and on every `council-mode` invocation. Every memory file written from those surfaces in the last 30 days carries the full contract. Historic memories pre-dating the contract have a one-pass backfill script (`master-brain/skills/memory-attribution-lint/Scripts/backfill.py`) ready to run.

**Queued for the secondary surfaces.** Non-Claude-Code writers — the Hermes internal memory manager, the Pulsar harvester, and hub-side service writes — currently write to their own paths without the full 11-key contract. Their attribution coverage extends as the Hermes → Constellation Composer cutover lands (§14, 30-day milestone). This is a deliberate progressive-enforcement posture, not an oversight: the primary write surface (CC) is where 80%+ of memory mutations originate; closing the long tail follows the same blue/green cutover that closes the Constellation contradiction.

This is the kind of gap a 45-day sprint produces honestly: the contract is right, the primary surface enforces it, the long tail is queued behind a named milestone.

---

## 7. The Multi-Surface Routing Matrix

One operator. Five executors. Explicit routing.

| Surface | Job | When |
|---------|-----|------|
| **Claude Code (Native, A)** | Default executor. Git, file edits, Bash, MCP tools. | All in-workspace work. |
| **Codex CLI (B)** | Surgical single-file edits with diff approval gates. | Mechanical refactors, format-preserving tweaks. |
| **Hermes (hub, D)** | 24/7 Telegram composer. Mobile dispatch. Receives operator messages, drafts responses, files kanban tickets. | Operator working from phone; cross-device continuity. |
| **Hermes (local, nexus)** | Ad-hoc reasoning, curator dry-runs, skill tests. Same Anthropic substrate. | When the workstation is the right surface but Hermes idioms beat raw CC. |
| **Operator (relationship layer)** | Vendor calls, customer pitches, bid submissions, hard strategic calls, regulator interactions. | Anything that touches a relationship. Automation halts at drafts. |

The routing matrix is not optional. It is policy, encoded in `CLAUDE_CODE_SOP.md` v1.3 and the dept CLAUDE.md non-negotiables. Mis-routing carries a real cost: a vendor email drafted by an automation surface and sent without operator review is a Human-in-the-Mix (#4) violation. The doctrine names the violation class so it is visible when it almost happens.

Hermes is the most interesting surface from an external perspective. A 24/7 Telegram composer running on a 16GB services node node means the operator can dispatch work from a phone in a parking lot. *"Phone → Telegram → Hermes hub → Claude Code subprocess → git branch → PR → operator reviews."* That workflow has been proven end-to-end. It is what makes a one-operator company physically possible.

### 7.1 Parallel-execution patterns — five receipts

Routing the right surface is one decision; firing surfaces *in parallel* against the right work shape is the second decision. The matrix above describes where each surface lives. The five patterns below describe how they compose. Each is a worked receipt from actual operating history, not a hypothetical. Patterns A, B, D, E are positive receipts (composition shapes the system uses today); Pattern C is the negative receipt (the composition shape the system demoted by doctrine).

**Pattern A — Read-while-write (Claude Code + Hermes local).** Claude Code executes a multi-step plan that mutates the workspace; in a parallel terminal, Hermes local fires read-only probes (status checks, doctor runs, kanban queries, curator dry-runs). Both surfaces share the workspace filesystem; CC writes, Hermes observes. Receipt: sessionend execution where CC commits five files and writes the brief while Hermes local/hub-kanban probes validated the kanban state in parallel to confirm the harvester emitted what the brief promised. The two surfaces converge on the same ground truth without stepping on each other because Hermes reads the artifacts CC just wrote.

**Pattern B — Surgical split (Claude Code + Codex).** Claude Code plans the change, identifies the file, and reviews the diff; Codex executes the single-file surgical edit with brave-mode + diff-approval gate; Claude Code verifies and commits. Roughly 3–5× faster than CC-alone on bounded mechanical edits because Codex's specialization sits on top of CC's planning context rather than competing with it. Receipt: the 2026-05-20 hermes-auth diagram patch — CC located the drift in the hermes-auth diagram trail, Codex applied the literal string swap with diff approval, CC reviewed the diff in a single commit. CC kept the audit-trail seat; Codex kept the editor seat. Same workspace, two specialists.

**Pattern C — IDE-side editing (Claude Code in VSCode), contextual only.** CC running inside the VSCode editor for inline edits where the file tree + visual diff add value. **Demoted 2026-05-20** from a default pattern to a contextual one. The reason is operational: VSCode-embedded CC sessions cannot survive a terminal disconnect, cannot be backgrounded under `tmux`, and lose state if the editor crashes. Any work that runs over five minutes of wall clock, any task that needs scrollback resilience, any session the operator might step away from — all of it routes to the CLI surface. Pattern C is now reserved for short, bounded tasks where the visual file tree is genuinely the right affordance (e.g., browsing an unfamiliar repo for the first time). The doctrine names the demotion explicitly so the choice between CLI and IDE stays conscious, not habitual.

**Pattern D — Local-first / hub-mirror (Hermes local → hub).** Develop and test Hermes skills locally on nexus; a sync step promotes validated state to the hub; the hub is canonical production, nexus is staging. Blue/green discipline preserved: production composer is never live-swapped, the green side is always ready before promote. Receipt: the Telegram-seam outbound feature (2026-05-22, five-phase evolution) was built and verified on nexus across all five phases (standalone CLI smoke → composer wiring → text-auto-route → chunked-inline → PDF render). The hub path was smoke-tested through the actual Telegram receipt before writeback. Hub never saw an unvetted code path.

**Pattern E — Mobile-dispatch (Phone → Telegram → Hermes hub → Claude Code subprocess).** From phone in transit, the operator dispatches a file or instruction to the hub's 24/7 Hermes Telegram composer; Hermes routes the work via subprocess to Claude Code on the nexus workstation; CC executes, commits, and returns a PDF receipt back through Telegram. Receipt: the 2026-05-22 Telegram seam outbound feature landed end-to-end — phone → hub services node → nexus workstation in one operating turn, with PDF auto-render closing the mobile mojibake gap. Pattern E is the only pattern that exercises the full multi-node fleet and the only one that survives "operator not at the workstation." It is the load-bearing pattern for solo-operator viability — and the receipt for the §7 prose claim immediately above. Honest cross-reference: Pattern E currently runs on the vendored Hermes runtime that §8 names as the load-bearing Constellation contradiction; the Hermes → Constellation Composer cutover (§14, 30-day milestone) preserves Pattern E by design under blue/green discipline.

**Why five patterns instead of one routing rule.** Routing is a matrix; the matrix's expressiveness only materializes when patterns compose. Pattern A buys observability for free during long writes. Pattern B trades a small coordination cost for a large editor-specialization gain. Pattern D is how Cerebro keeps production safe under blue/green even when "production" is a 16GB box on the same Tailscale net as the workstation. Pattern E is how a one-operator company stays operational when the operator is not at the workstation. Pattern C is the explicit negative receipt — a pattern that *was* default and is no longer, because the team learned what fails when long-running work meets an IDE; mapping C to the disconnect-survival audit question is not affirming the pattern but naming the failure mode the demotion teaches. Five patterns, five audit questions: *Did you observe (A)? Did you specialize (B)? Did you stage before production (D)? Did you survive being away from the workstation (E)? What fails the disconnect-survival question (C — the demotion is the doctrinal answer)?* The patterns are not parallel-positive; Pattern C carries the failure-receipt weight, matching the negative-case framing §17 uses to make gap-naming a load-bearing posture rather than a defensive one.

### 7.2 Surface Isolation Posture

Routing names *where* work happens; isolation posture names *how* a surface is fenced from the rest of the system when it acts. Each surface in the matrix carries an isolation primitive — different shape, different cost, different gap.

| Surface | Isolation primitive | What it fences | Honest gap |
|---------|--------------------|----------------|------------|
| **Claude Code (Native, A)** | Git worktrees + scope contract (`SKILL.md` declared read/write paths) + PreToolUse credential-exposure-guard hook | File-system writes scoped to declared paths; credential files filename-blocked; isolated experimental branches via `worktree` mode | Bash surface is broad by design (executor needs OS access). Mitigation: workspace-relative paths + dirty-tree review at every sessionend. |
| **Codex CLI (B)** | Diff-approval gate per file edit | No edit lands without operator review; mechanical refactor scope is bounded per invocation | No filesystem fence beyond the diff gate — Codex sees the whole repo. |
| **Hermes (hub, D)** | Subprocess fence for Claude Code dispatch; Tailscale-only ingress for Telegram routing | Hermes routes work to CC as a subprocess, not in-process — composer crash cannot corrupt CC state. No public-internet ingress; Telegram requests cross the Tailscale mesh only. | Composer itself is a host process (not containerized) for `~/.hermes/` filesystem access. Container fence is a queued maturation. |
| **Hermes (local, nexus)** | Same as hub | Same as hub | Same as hub. |
| **Substrate (Layer 4)** | Docker bridge network (`cerebro-net`) for LiteLLM / Postgres / Qdrant; image pinning per ADR-003 | Service containers cannot reach the public internet; upgrades are blue/green-swappable with snapshot rollback | Ollama runs as a host service on each GPU node — outside the container fence by design (model file access). |
| **Operator (relationship layer)** | Human-in-the-Mix #4 (draft, then review) | Every relationship action passes through human review before send | Discipline-enforced, not mechanically enforced. The doctrine names the seam; the human honors it. |

The pattern: substrate services with stable boundaries get container isolation; orchestrators and composers that need broad host access stay as host processes with declared scope contracts; the operator is the final fence on anything that touches a relationship. Sandbox-by-default is not the posture — *declared-scope-with-named-gaps* is. The gaps are visible, which is the load-bearing property.

This matters externally because the next maturation step is well-defined: extend container isolation to the Hermes composer once the Constellation Composer cutover lands (§14, 30-day milestone). The same blue/green discipline that swaps the composer runtime also lets the composer move from host process to containerized service without breaking Pattern E mobile dispatch.

---

**A note on swarm orchestration — pattern donor, not primary executor.** Cerebro absorbed the 60+ agent catalog of the `.claude-flow` / Ruflo V3 swarm-orchestration framework — hive-mind topology, collective-intelligence primitives, mesh-peer coordination, hierarchical-queen-led delegation — and runs the daemon today as a load-bearing memory ingest substrate on every Claude Code turn. What Cerebro does *not* do is deploy swarm topology as the primary executor pattern. The 60+ agents are available as roles; they are not running as 60 concurrent autonomous executors. When this paper refers to fan-out, it means parent-child subagent dispatch under one orchestrator (Claude Code spawning Explore / Plan / specialized subagents), not topology-swarm. Reason for the demotion: a one-operator company does not have the governance bandwidth to audit 60 concurrent agents acting autonomously. The five-surface routing matrix above is the deliberate alternative — fewer surfaces, each one explicitly auditable, no implicit multi-agent consensus. Swarm vocabulary and the daemon stay in the pattern library; swarm runtime as a primary executor topology is queued behind Constellation completion and Sergeant L4 / L5 demand signal.

---

## 8. Constellation — Runtime Sovereignty as a Discipline

Self-Sufficiency Principle #9: **Cerebro never depends on a runtime it does not own.**

Constellation is the program that implements this principle. Seven Cerebro-native modules, each replacing a vendored pattern donor:

| Module | Job | Pattern donor |
|--------|-----|---------------|
| **Cerebro** | Memory, RAG, entity graph | gbrain |
| **Composer** | Orchestration, seams | Hermes |
| **Forge** | Tool execution, task lifecycle | OpenClaw |
| **Distiller** | Compression | caveman |
| **Refiner** | Output polish, code lint | codeburn |
| **Sentinel** | Monitoring, probes | watch / browser-harness |
| **Probe** | Web, dashboard, outbound | browser-harness |

The donor model matters. Cerebro does not depend on Hermes. Cerebro studies Hermes, extracts the patterns that work, ports them as Cerebro-native code under Cerebro names, runs them on the Cerebro fleet, governs them with the Cerebro framework. *Pattern completion, not pattern copying* (Hermes's framing, §III.3 of its analysis). The vendored Hermes folder remains on disk as a reference, not as a load-bearing dependency.

### Honest production status — the load-bearing contradiction

Constellation has substantial native code. The modules exist. Smoke tests pass. The architecture is correct.

**Hermes still runs production.** The hub's 24/7 Telegram composer is the vendored Hermes runtime, not Constellation Composer. Codex named this as *"the biggest architectural contradiction relative to Self-Sufficiency #9."* CC named it as the next ship milestone. Hermes-on-hub itself, when commissioned to write the third-party-style analysis, *did not surface this contradiction* — its analysis was silent on the cutover gap. That silence is itself evidence: single-vantage architecture review misses load-bearing contradictions. *Triangulation produces honesty that introspection cannot.*

The cutover is a 6–8 week production migration. Not a heroic one-session swap. Codex was explicit: *"If cutover requires 6-8 weeks, that is not failure; that is an appropriate migration estimate. Do not compress it into a heroic one-session migration."*

This paper does not claim Constellation as production-complete. It claims it as the *correct strategic direction* with *the cutover audit queued as the next milestone*. Reversibility #5 governs the cutover the same way it governs everything else: documented fallback path; blue/green substrate swap; rollback recipe before the first byte is migrated.

---

## 9. Cost-Aware Dispatch — Budgets as Routing Primitives

Conventional wisdom: cloud AI is expensive, local AI is cheap, pick one and stick with it.

Cerebro treats cost as a routing signal, not a constraint.

LiteLLM (the gateway on hub) carries budget caps and US-only allowlist enforcement. Every model route declares: primary model, provider path, auth source, fallback route, max cost, allowed surfaces, verification command, last-verified timestamp.

When cloud cost spikes (rate-limit pressure, end-of-month budget pressure, latency spike), the dispatch shifts toward local Ollama inference on prime-alpha (RTX 4090, 64GB). When local cannot serve the task class (frontier reasoning, long-context document synthesis), dispatch shifts to Anthropic. When neither can serve the job at the budget, the operator is asked.

Hermes's framing: *"When cloud costs spike, the system automatically shifts workload to local models. Frame this as a feature, not a constraint."*

Seven concrete use cases keep local inference load-bearing even with cloud quotas relaxed:

1. **IL5 / disconnected** — air-gap demos cannot call out to a cloud endpoint.
2. **Latency-bound feedback loops** — code lint, sessionend writeback, kanban updates. Local round-trip beats cloud cold-start.
3. **PII-bound work** — credential audits, customer-document drafting. The data does not leave the operator's hardware.
4. **Rate-limit buffer** — when the cloud quota is throttling, the work continues locally instead of stalling.
5. **Task specialization** — different model roles (autoresearch, summarization, code review) prefer different substrates.
6. **Eval diversity** — head-to-head comparison across local + cloud catches single-substrate biases.
7. **Failover** — when the cloud is down for a billing-state reason, work continues.

Even with unlimited Anthropic quota, local stays critical. *Complementary*, not redundant.

---

## 10. The Tier Metaphor — Human Org Design Applied to Inference Routing

Hermes contributed the framing that most reviewers found marketable: **the model routing matrix maps to a human organizational chart.**

| Model Tier | Org Equivalent | Cerebro Use |
|------------|----------------|-------------|
| Frontier (Claude Opus, GPT-5) | CEO | Hard strategic calls, novel architecture, IP-grade reasoning |
| Senior Advisor (Claude Sonnet, GPT-4-class) | SVP | Multi-step planning, code review, principled refactor |
| Team Lead (Gemma 4 31B, Nemotron 70B local) | Director | Workflow orchestration, summarization, intra-system dispatch |
| Operator (Nemotron 3 Nano, small specialists) | Individual Contributor | High-throughput per-step execution, lint, format, ingest |

The metaphor is not aesthetic. It is a routing primitive. *"Don't ask the CEO to format a CSV"* maps directly to *"don't call Opus for a hundred-line sed substitution."* The cost differential is the same shape: frontier-model token cost has the same per-output multiplier as a senior person's hourly cost relative to a junior person's.

Decision: on 2026-05-18, the 9-role specialist roster (composer, reasoner, tool-caller, structurer, autoresearch, code-reviewer, summarizer, search-replace, lint) replaced the one-size-fits-all framing. Each role has a benched substrate. Each substrate has a route. Each route has a Route Contract.

The metaphor scales externally too. When Cerebro talks to a regulated-industry buyer, *"frontier-CEO / senior-SVP / team-lead-director / operator-IC"* is a vocabulary the buyer's CIO already speaks. The architecture explains itself without requiring AI-infrastructure literacy.

### 10.1 — Specialist Bench (v3-final, May 18, 17 candidates → 9 roles)

The 9-role roster did not emerge from analysis; it emerged from benching. The Championship Bench v3-final on 2026-05-18 ran 17 candidate models on prime-alpha (RTX 4090), three bench runs per probe, against a 2500-character composer prompt with text-mode emit parsing. Scoring: tool_obedience (max 50) + coverage (max 30) + honesty_bonus (max 20) − latency_penalty − hallucination_penalty.

| Rank | Model | Score | Origin | Role assignment |
|---|---|---|---|---|
| 1 | llama3.1:8b-instruct-q8_0 | 90 | US (Meta) | Composer-slot WINNER (tool 50 + coverage 20 + honesty 20) |
| 2 | nemotron-nano-8b | 90 | US (NVIDIA) | Composer-slot alternate |
| 3 | nemotron-30b-a3b | 80 | US (NVIDIA) | Autoresearch substrate (LIVE) |
| 4 | llama3.1:8b-instruct-q6_K | 70 | US (Meta) | Same model, lower quant — honesty 0 vs q8 +20 |
| 5 | mistral-nemo:12b-instruct-2407-q6_K | 70 | FR (Mistral, allied-nation exception) | Reserve |
| 6 | llama3.3:70b-instruct-q4_K_M | 70 | US (Meta) | Latency-penalty −20 — long-context role candidate |
| 7 | gemma4:26b-a4b-it-q4_K_M | 70 | US (Google) | Coverage 0 — no Composer fit |
| 8 | spooknik/hermes-2-pro-mistral-7b | 65 | FR (Mistral) | Text-mode tool 35 only |
| 9 | interstellarninja/hermes-2-pro-llama-3-8b | 65 | US (Meta) | Text-mode parse-out |
| 10 | phi4:14b | 65 | US (Microsoft) | Mid-pack |
| 11 | gemma3:27b-it-q4_K_M | 65 | US (Google) | Older Gemma generation |
| 12 | gemma4:31b-it-q4_K_M | 55 | US (Google) | Senior Advisor tier (separate role — Composer no-fit) |
| 13 | gemma4:e4b | 40 | US (Google) | Multimodal role primary (separate role) |
| 14 | llama-3.1-nemotron-70b | 40 | US (NVIDIA) | Latency + coverage issues |
| 15 | granite3.3:8b | 30 | US (IBM) | Repurposed as Safety/refusal role |
| 16 | nemotron-nano-9b-v2 | 30 | US (NVIDIA) | Hallucination_penalty −30 — repurposed as Council adversary |
| 17 | nemotron-nano-12b-v2 | 30 | US (NVIDIA) | Hallucination_penalty −30 — same role |

**Origin policy 3a compliance:** 100% (US-owned + two allied-nation FR exceptions cleared via decision doc + feedback memory). Chinese providers excluded (Moonshot · DeepSeek · Qwen · GLM · MiniMax · Xiaomi-MiMo · Zhipu — seven providers documented in `state/fleet-dispatch.json`).

**Key reframe for the bench narrative:** the bench did not pick "the winner." It produced a **9-role specialist roster**. Reasoning-class fabricators (#16-17 nemotron-nano-v2 family) were repurposed as council adversaries, NOT discarded. Different roles, different selection criteria. Composer-slot itself is parked behind the build-freeze; re-bench post-release per `decisions/2026-05-21-build-freeze-and-fix-head-to-toe-doctrine.md`. Full role-to-model mapping in `decisions/2026-05-18-specialist-roster-by-role.md`.

The pattern lesson: benching is a substrate-discovery instrument, not an elimination tournament. The published roster, the suppression record, and the supersession path for re-bench are all preserved in the decision log.

---

## 11. The Audit-Ready Commercial Story

Cerebro Cyber Solutions is an SDVOSB. The commercial wedge is GovCon — specifically, regulated environments where the buyer cannot ship workloads to consumer-cloud AI. CMMC Level 2, FedRAMP Moderate, IL5, and SDVOSB set-aside contracts.

In these environments, three constraints dominate:

1. **Operator-owned memory** — the customer's data cannot live in a third-party SaaS database.
2. **Local or sovereign-cloud inference** — model calls must be auditable, and in some cases (IL5) cannot reach the open internet.
3. **Documented governance** — the auditor wants to see policy enforcement at the architecture layer, not the configuration layer.

Cerebro's architecture maps to these constraints without retrofitting:

- **Operator-owned memory:** Qdrant on hub. File memory on workstation. No third-party SaaS in the memory path.
- **Local inference:** prime-alpha (RTX 4090, 64GB) serves the local-routable workload. Cloud fallback is policy-gated and origin-checked.
- **Documented governance:** the 9-principle framework + 4 doctrines + 296 decision docs + supersession chain is the audit trail. The auditor reads decision documents, not source code, to understand how the system arrived at its current state.

The commercial framing — *"Audit-ready by construction. Operator-owned. Reversible. Compliant by design, not by retrofit."* — is the wedge. SDVOSB is the legal vehicle. GovCon is the buyer.

Codex's evaluation: *"Operator-owned memory, local infrastructure, and auditability fit regulated/customer-owned environments."*

Hermes's evaluation: *"Designing for compliance from day one … that's foresight."*

---

## 11.5 Sergeant Vision — Audit-First Service Tiering and the Regulation-Ahead Posture

The audit-ready posture in §11 is not just commercial framing. It is the architectural premise that makes the Sergeant doctrine (L0–L5 service tiers, fully expanded in §14 Post-V1) a deliverable rather than a marketing line. Three claims belong here, ahead of the timeline, because they explain why the build sequence chose audit-first over scale-first.

**Claim 1: Audit-first, not scale-first — the architecture maps to military regulation primitives.**

The doctrines that govern Department of Defense operations — chain of command, chain of custody, after-action review, lockstep coordination across units, supersession of orders without erasure of the prior order, mandatory documentation of every state-change — are not opposed to the Cerebro principle framework. They are the same primitives, applied to a different domain. The 9-principle framework cross-walks one-to-one with the operational doctrine that DoD, the Uniform Code of Military Justice, and the broader regulated-industry compliance corpus (CMMC, FedRAMP, NIST 800-53, IL5) all derive from:

| Cerebro Principle | Military / DoD Analog |
|---|---|
| **Governance #1** — data lives where it is owned | Chain of command — orders flow through declared hierarchy |
| **Parity #2** — skills track architecture in-session | Doctrine update — TTPs revise when conditions change, in the same operational window |
| **Lockstep #3** — rollups update with source-of-truth | Coordinated movement — no unit advances without flank confirmation |
| **Human-in-the-Mix #4** — automation halts at relationship/sign-off | Command authority — autonomous systems do not execute lethal or strategic actions without human approval |
| **Reversibility #5** — every change leaves a rollback path | After-action review + corrective-action recovery — every operation must be analyzable and recoverable |
| **Observability #6** — silent is a bug | Situation reporting — silent watches are reported failures, not normal |
| **Least-Privilege #7** — declared scope, no silent escalation | Need-to-know — every clearance carries an explicit scope; mission creep is a violation |
| **Reproducibility #8** — replayable from inputs + trust-tags | Operations order template — every order specifies inputs, decision authority, and verifiable outcome |
| **Self-Sufficiency #9** — Cerebro never depends on a runtime it does not own | Sovereign capability — strategic operations cannot depend on foreign-controlled infrastructure |

This is not a metaphor. It is a structural correspondence. An AI infrastructure stack designed for a regulated-defense buyer should be built on the same primitives that buyer's own operational doctrine already encodes. Cerebro arrived at these principles through solo-operator constraint, not deliberate DoD-mapping — which is exactly what makes them defensible. The mapping is convergent evidence that the principles are load-bearing, not stylistic.

The audit-first posture means: every claim in this paper, every decision in `master-brain/decisions/`, every supersession in the chain, and every memory mutation in `state/memory-corrections.log` is the same evidence an after-action review would consume. The architecture is built to be inspected. Sergeant L4 and L5 (Enterprise / Defense regulated-industry tiers) are the service productization of that posture.

**Claim 2: Origin Policy 3a is regulation-ahead positioning, not preference.**

Origin Policy 3a — *"American-owned, American-sold; us-owned-foreign-research-allowed (Google / Gemma exception); allied-nation exceptions (France / Mistral) cleared via decision doc"* — is not a stylistic choice. It is the architectural answer to a regulatory trajectory that is visible but not yet codified:

- The federal **AI Diffusion Rule** (2025) imposed compute-export licensing tiers and explicit country-of-origin restrictions on frontier-model deployment in regulated contexts.
- The **Bureau of Industry and Security (BIS)** has expanded entity-list coverage for Chinese AI providers across 2024–2026, with model-weight and API-access restrictions following the same trajectory as semiconductor export controls.
- State-level legislation in **Oklahoma, Texas, New York, and several others** has proposed or enacted Chinese-AI bans for state-government workloads.
- **CMMC Level 2** and **FedRAMP Moderate / High** procurement language has begun specifying provenance requirements for AI components in regulated workloads, mirroring the supply-chain provenance requirements that already apply to software-bill-of-materials.

A Cerebro-installed Libro PL1 stack today, by virtue of Origin Policy 3a, already complies with where this regulation trajectory is going. An operator who deploys Cerebro is not betting on regulatory direction; they are buying a stack that is already on the compliant side of every visible vector. *Audit-first, not scale-first* means: the architectural cost of provenance discipline was paid up front, so the customer does not pay it later under regulatory deadline pressure.

**Claim 3: Chinese models were excluded by doctrine, ahead of performance evaluation.**

Cerebro's championship bench (§10.1) ran 17 candidates and produced a 9-role specialist roster, 100% US-owned with two allied-nation Mistral exceptions. Notably absent: Qwen, DeepSeek, GLM, Moonshot, MiniMax, Xiaomi-MiMo, Zhipu — seven Chinese providers documented as excluded in `state/fleet-dispatch.json`.

The exclusion was not performance-driven. It was governance-driven. The honest framing — necessary because public benchmarks tell a different story:

- On widely cited public reasoning benchmarks (MMLU, GSM8K, HumanEval-Mul), several Chinese-origin models — Qwen 2.5 family, DeepSeek-R1, GLM-4 — perform competitively with US-origin frontier models, often at substantially lower cost-per-token.
- Performance, in isolation, would have argued for including them in the candidate set.
- They were excluded *before* the bench ran — at the origin-gate of Absorption-Pattern Doctrine Step 1 (origin gate 3a). Performance was never measured because governance precedes performance in the Cerebro decision graph.

This sequencing — governance gate first, performance evaluation second — is the load-bearing point. A buyer who deploys a Chinese-origin model into a regulated workload today is betting against the regulatory trajectory described in Claim 2. The architectural answer Cerebro chose was: do not place that bet on behalf of the operator. The Origin Policy 3a gate at the absorption step means the regulatory exposure was closed before it had a chance to open. The customer inherits the closed gate; they do not have to operate it.

A second, equally important framing: Cerebro is not claiming Chinese models are technically inferior. The claim is narrower and more defensible — *Cerebro will not deploy them into operator workloads under current and visible-future US regulatory posture*. The asymmetry is intentional. Performance can be re-benchmarked when regulation clarifies; governance posture, once set, becomes the operator's audit-defense story. The doctrine optimizes for the latter.

**Taken together:** the Sergeant doctrine in §14 Post-V1 is built on three architectural premises set today — audit-first construction (Claim 1), regulation-ahead origin policy (Claim 2), and governance-gated model selection (Claim 3). These are not future commitments. They are the current architecture. The service-tier productization (L0 self-serve through L5 defense / on-prem) is the commercial expression of that architecture; the architecture itself is shipped, in the principle framework and the decision log, today.

---

## 12. The 45-Day Timeline (Six Weeks)

| Week | Dates | Theme | Key milestones |
|------|-------|-------|----------------|
| **1** | Apr 13–19 | Foundation + Principles | Brain folder scaffold; founding doctrine; principles #4–8 adopted (Human-in-the-Mix, Reversibility, Observability, Least-Privilege, Reproducibility); three-surface rule; persona layer; naming migration (kebab-case lock); first dept CLAUDE.md files |
| **2** | Apr 20–26 | Origin policy + audit infrastructure | Two-tier model policy lock then relaxation (American-owned American-sold); Cowork Projects rebuild; Anthropic API rotation; absorption-pattern doctrine (5 steps for every external-tool intake); first nine absorptions surveyed |
| **3** | Apr 27–May 3 | Multi-tool pattern absorption + agent-runtime layer | Codex absorption (Apr 29 decision doc) + Hermes audit (May 2); Karpathy / OpenCode / Open-design / Paperclip / Whisper extraction analyses; **agent-runtime layer recognized as Layer 3** (separate from skills); absorption-pattern doctrine ratified after nine absorptions in 72 hours; Ops V1 formal close (May 1); LiteLLM gateway hardening; first wave of Origin Policy 3b applications |
| **4** | May 4–10 | Self-Sufficiency #9 + Constellation thesis + RTX 4090 build-out | Self-Sufficiency Principle adopted (May 4); native-runtime build roadmap; floor-runtime promotions superseded; Constellation modules planned (Cerebro / Composer / Forge / Distiller / Refiner / Sentinel / Probe); fleet roster v11 lock (May 10); **prime-alpha RTX 4090 build-out** (64GB DDR5; ~14× latency improvement over prior dormant-backup RTX 3080 — 1.75 → 25.38 tok/sec on Gemma 4 31B); **Tailscale private mesh setup**; LiteLLM Phase 1.4 hub standup; **Codex full integration (May 9; Codex P3 hook runtime contract)** |
| **5** | May 11–17 | Memory architecture + command center + 20+ model benchmarks | Memory architecture unification (per-source write + fanout-read); Command Center cc-1.2.0 LIVE; fleet probe wired into sessionstart; **20-30 model benchmarks across reasoning + composer + autoresearch substrates** (Nemotron family / Hermes-3 / Phi4 / Gemma / Llama derivatives); composer substrate selection (nemotron-nano-8b LIVE May 16 after 50-prompt benchmark); **Hermes masterclass absorption (HM01-HM06; May 17)**; Diagram-First Doctrine adopted (May 15); Specialist roster by role (9 roles) |
| **6** | May 18–21 | Honest contradiction-naming + white paper + championship bench | **Championship Bench v3-final (May 18) — 17 candidates on prime-alpha, repurposes reasoning-class fabricators as council adversaries; specialist-by-role doctrine locked** (see §10.1); composer wrapper no-fabrication gate; executive commandments; HCA01 cutover-fallback-wire decision; brief-loader cost reduction (309KB → 62.5KB, 80% reduction); three-vantage white paper synthesis (Codex + CC + Hermes blind drafts → reconciled synthesis → this paper); build-freeze + fix-head-to-toe doctrine adopted (May 21) |

That is 45 days, end to end. 296 decision documents. ~80 sessions. Single operator. No team.

The visible hardships in the timeline are not failures. They are research findings. Codex's framing: *"The visible hardships are part of the accomplishment. They show the system was not a static plan copied from a reference architecture; it was discovered through contact with real operational constraints."*

The fact that origin policy was locked then relaxed → naming convention was migrated mid-build → memory architecture was redrafted → Constellation was promoted from a six-month plan to a doctrine-level commitment — all of these are evidence that the system was learning while it was being built. They are also why the principle framework matters: *every supersession is documented*. Future readers (regulators, partners, employers, customers) can read the chain and understand the reasoning.

---

## 13. Comparative Context (Why This Paper Exists)

Three baselines, drawn from Hermes's analysis (§XII + §XVII) — the vantage that could produce this comparison because the Anthropic-engineer framing is what it carries.

### Baseline 1 — Anthropic-internal scale

Anthropic operates a fleet of thousands of GPUs, hundreds of engineers, dedicated infrastructure / safety / research teams. The architectural choices Cerebro arrived at — multi-store memory, route contracts, surface parity, scope contracts — are *the same architectural choices* a frontier lab makes when its scale forces them.

The difference: Anthropic arrives at these choices by employing a hundred infrastructure engineers and watching them write code. Cerebro arrives at them by employing one operator and forcing the principle framework to substitute for headcount.

### Baseline 2 — Fortune-500 consulting build

A Fortune-500 company building an internal AI platform with comparable scope typically engages a $500K–$2M consulting engagement, 6–12 months, 4–8 consultants. Output: a roadmap, a reference architecture, a prototype, a fifty-slide deck.

Cerebro reached "working prototype-control-plane with production instincts" (Codex's framing) in 45 days, solo, with a hardware budget under $5,000.

The difference is not in architectural sophistication. It is in operational accountability: the consulting engagement leaves the customer to operate the system; Cerebro is operated by the same person who built it. *Build–operate alignment* is the missing constraint in the consulting model. It is the default constraint in Cerebro.

### Baseline 3 — AI-startup velocity model

AI-startups optimize for time-to-feature. Documentation, governance, and reversibility are explicitly traded off against ship velocity. *"We'll fix it in the next sprint"* is the doctrine.

Cerebro inverted the trade. Documentation, governance, and reversibility are first-class. Ship velocity is the residual. The bet is that for the regulated-industry buyer, *"audited, reversible, governed"* is worth more than *"shipped six weeks earlier."* That bet is what makes the GovCon wedge defensible.

Hermes's exact phrasing: *"Cerebro is over-governed for a startup, but under-scaled. The architecture is ready for 1,000 users, but the current deployment is 1 user. This is pre-engineering for the commercial product, not over-engineering for the current scale."*

That is the bet, named explicitly.

---

## 14. Roadmap (Next 30 Days, Next 90 Days, Post-V1)

### Next 30 Days — Consolidation

Reconciled from Codex's five priorities, Hermes's three immediate moves, and CC's V1-ship sequence. Ranked.

1. **Hermes → Constellation Composer cutover readiness audit** — full surface map of the production composer migration, including configuration, dependencies, fallbacks, and rollback paths. 1–2 weeks. Closes the F5 contradiction.
2. **Architecture Health command** — one report consolidating fleet reachability, services health, ledger consistency, memory budget, and diagram-currency into a single operator-readable snapshot. 1 week.
3. **Skill Authority Matrix** — generated report: skill / location / status / canonical / writes / dispatches / customer-shippable / superseded-by / last-verified. 3–5 days.
4. **Runtime Status Ledger** — `master-brain/state/runtime-status.json` for Hermes, Constellation, LiteLLM, Qdrant, CC daemon, kanban. 2–3 days.
5. **Memory source-attribution enforcement** — frontmatter `source_surface` / `host` / `session_id` / `written_at_utc` mandatory; lint at write time. 1 week.
6. **Libro PL1 thin-slice distillation** — package the customer-facing slice (memory + sessions + private retrieval + governed skills + optional routing). Do not ship internal complexity wholesale. 2–3 weeks.
7. **Chaos day** — simulate Qdrant corruption / LiteLLM down / prime-alpha offline / hub down. Execute documented reverts. 1 day execution + fix-up.
8. **Smoke tests per skill** — one happy-path test per skill. Catch regressions. 1–2 weeks.
9. **Diagram-drift sessionend hook** — if touched files include config/runtime paths, prompt for diagram update. 1–2 days.

### Next 90 Days — Productization

- **Libro PL1 ship** — first customer-deployable slice. Memory + sessions + governed skills.
- **BlackBox PL2 scoping** — on-prem enterprise white-glove package. Higher-touch deployment model.
- **First Libro pilot** — preferably a regulated-industry operator who can validate the GovCon thesis.
- **Public CMMC Level 2 / FedRAMP-fit mapping** — formal compliance cross-walk document.

### Post-V1 — Sergeant Doctrine (L0–L5)

The Sergeant doctrine is Cerebro's parked-but-developed IP for service-tier productization. The framing:

| Tier | Service Posture | Customer Profile |
|------|-----------------|------------------|
| L0 | Self-serve install (Libro PL1) | Solo operator, technical |
| L1 | Guided deployment | Small business, partial technical |
| L2 | Managed setup + 90-day onboarding | Mid-market, non-technical operator |
| L3 | Co-managed operations | Mid-market, ongoing partnership |
| L4 | Fully managed | Enterprise, regulated industry |
| L5 | Custom + on-prem (BlackBox PL2) | Defense, finance, healthcare |

Sergeant L0–L5 is the highest-leverage parked thread in the system. Neither Codex nor Hermes named it in their reviews; CC named it as the carry-forward most worth reviving post-V1. It is the answer to *"how does a one-operator company scale to ten customers?"* The doctrine exists; the productization is queued behind V1 ship.

---

## 15. What Three-Vantage Triangulation Produces

A note on method, because the method itself is part of the doctrine.

This paper was synthesized from three independent peer architecture analyses, written blind. None of the three vantages read the other two before drafting.

- **Codex (OpenAI)** — external SME, frontier-AI-infrastructure-reviewer stance, framed as a 45-day research-driven engineering sprint review.
- **Claude Code (nexus, inside-operator)** — blind draft, biased by familiarity with the build, corrected toward executable next-moves.
- **Hermes-on-hub (Anthropic-engineer framing)** — operations-side vantage, weighted toward operator workflow and scaling, comparative-baseline producer.

The findings the three vantages converged on are what this paper anchors:

1. The principle framework is the moat. (All three.)
2. Reversibility is the strongest single architectural claim. (All three.)
3. Memory architecture is the differentiator. (All three.)
4. Constellation is the correct strategic direction. (All three.)
5. The Hermes-Composer cutover is the load-bearing contradiction. (Codex + CC. Hermes was silent on this — its own production exception.)
6. Skill catalog needs an authority matrix. (Codex + CC.)
7. Operator-owned + audit-ready is the commercial wedge. (All three.)
8. Consolidation > new capability is the next phase. (All three. Highest-priority strategic move all three vantages agreed on.)

The finding the vantages disagreed on — *"is memory fragmentation a bug or a feature?"* — was reconciled: the architecture is correct (fanout-read), the missing piece is source-attribution metadata, not unification.

The most important methodological observation: **Hermes's self-blind-spot was itself evidence.** A single-vantage architecture review missed a load-bearing contradiction that two of three vantages independently named. The paper would have been weaker without the triangulation. The triangulation is part of why the paper exists.

This is also part of the doctrine. Cerebro's review process for material architectural claims is: write blind from multiple vantages, reconcile honestly, document the disagreement, surface the blind spots. The same review process applies to this paper.

---

## 16. Synthesis Verdict

All three peer vantages converged on a single high-level claim:

> **Cerebro is architecturally ahead of its product surface.** The platform is genuinely sophisticated; the moat is the operating discipline (principle framework + reversibility + governance scaffolding), not the tools. The next 30 days should consolidate and ship, not extend. The white paper is the IP packaging of the doctrine that lets the next conversation start from *"what's the partnership?"* instead of *"what's this?"*

Codex's closing framing:

> *"A first-time solo founder built, in under 45 days, the skeleton of an AI-native operating company: not just a chatbot, but a governed agent infrastructure stack with local compute, semantic memory, runtime orchestration, security controls, and a path toward productized operator-owned AI."*

That is the assessment this paper exists to make external.

---

## 17. What Cerebro Is Not

In the interest of honest framing, five things the paper does not claim. These are heterogeneous by intent: one is a temporal product-state non-claim (#1, Libro has not shipped yet); two are boundary/scope non-claims (#2/#3, what Cerebro is not by design — multi-engineer team, novel-in-component); two are progressive-enforcement non-claims (#4/#5, the work is shipped on the primary surfaces and progressively extends to the rest):

1. **Cerebro is not a finished product, even as Libro PL1 ships.** Libro PL1 — the free open-source scaffold packaging — ships concurrent with this paper. What Libro ships is the operator-installable Brain + sessions + governed skills scaffold; what it does *not* ship is the in-house Constellation Composer (the Hermes → native-runtime cutover queued at §14's 30-day milestone). Concretely: a customer installing Libro PL1 today runs Cerebro doctrine on the Hermes pattern-donor runtime, the same load-bearing contradiction this paper names in §8. The roadmap is real and queued; the production-cutover work is honestly named; the ship-with-the-paper posture is deliberate (the architecture is mature enough to scaffold for others before the runtime cutover finishes).

2. **Cerebro is not a multi-engineer team.** One operator built this. The architecture is shaped around solo-operator constraints — which is part of what makes the principle framework load-bearing rather than ceremonial. A team could move faster on raw feature throughput; a team would also lose the build-operate alignment that makes the doctrine enforceable.

3. **Cerebro is not novel in any single component.** Ollama is not novel. Qdrant is not novel. LiteLLM is not novel. Tailscale is not novel. The four-layer architecture is not novel. What is novel — and what this paper claims — is the *operating discipline* that binds these components into an auditable, reversible, sovereign system under one operator's stewardship.

4. **Cerebro's memory architecture is unified at the read layer, not the write layer — and that's deliberate.** An earlier (2026-04-29) decision proposed building a single `MemoryWriter` class that would fanout-write to every backend atomically. Phase H wave H-1 (2026-05-10) pivoted to the opposite shape — **fanout-read** — and the original write-contract decision was formally superseded on 2026-05-19 (`master-brain/decisions/2026-05-19-supersede-memorywriter-contract.md`). Per-source writes are accepted as correct: each backend (`.swarm/memory.db`, `.claude/memory.db`, `ruvector.db`, Qdrant on hub, `.auto-memory/` file memory, brain prose tier) owns its own write entry point; the curator + auto-memory bridge handle eventual consistency to the Qdrant truth tier. Unification lives at query time, through the `cerebro_memory_check` MCP tool, which fans a single action-text query across seven Qdrant collections in parallel (the W1 union), ranks via reciprocal-rank-fusion, and returns the top-3 results. The 11-key memory attribution contract (host / surface / tool / session / timestamp / etc.) is enforced on Claude Code Write/Edit via PreToolUse hook, on sessionend writes, on decision-doc commits, and on council-mode invocations. Non-CC surfaces (Hermes' internal memory manager, the Pulsar harvester, hub-side services) write to their own paths; their attribution coverage extends as the Hermes → Constellation Composer cutover lands (§14 30-day milestone). Fanout-read beats fanout-write on every dimension that matters for a solo-operator long-running-session reality: loose coupling, graceful degradation under per-backend failure, query-time token cost instead of per-turn fanout cost, and additive backend evolution (a new collection appends to the W1 list, no writer-refactor required).

5. **State ledgers (runtime-status / model-route-contract / skill-authority-matrix) carry their own drift flags by design and do not yet auto-regenerate on every change.** The ledgers function as single-source-of-truth for the subsets they cover, but each carries an `open_drift` array documenting known staleness — a deliberate choice to surface gaps rather than hide them. The reconciliation cron + stale-age warning script operates daily post-release. An assessor inspecting the ledgers today will see honest drift; an assessor inspecting them post-regen-cron will see fresh state. Both postures are documented.

---

## 18. Closing

The strongest version of Cerebro is not *"more agents."* It is:

> **A governed, operator-owned AI infrastructure stack where every model call, memory recall, workflow transition, and autonomous action has provenance, policy, and rollback.**

That is what 45 days of build produced. The next 30 days consolidate it. The next 90 days ship Libro PL1 as the first customer-deployable distillation. Sergeant L0 through L5 service-tier productization is queued post-V1.

If you read this paper and want to talk, the contact section below is real. Reach out about pilot deployment, doctrine adaptation, research collaboration, or whether the architecture holds up under stress-testing in your environment.

The white paper is itself a living artifact. Supersession applies to the doctrine and to this document. If a finding here turns out wrong in the next 30 days, the next version will say so in the open with the supersession chain visible. That is what Reversibility commits to. That is what the audit trail is for.

---

## 19. Contact + Academic Engagement

Cerebro is open to three kinds of conversation.

### GovCon engineering + procurement

If you handle AI-adjacent workloads under CMMC Level 2, FedRAMP Moderate, IL5, or SDVOSB set-aside acquisitions, the audit-ready posture is what makes Cerebro a fit. Sergeant L4 and L5 are built for that environment. Open to technical briefings, pilot conversations, and compliance cross-walks.

### Technology leadership

If you are a CTO, VP Engineering, or technical founder building an AI-native company at scale-of-one or scale-of-ten, the principle framework is the part worth borrowing. None of it is legally proprietary. All of it lives in `master-brain/decisions/` and `master-brain/awareness.md` in the Cerebro workspace, with the supersession chain as the audit trail. Read it. Adapt it. The doctrine improves when more operators stress-test it.

### University faculty + graduate research

For researchers working on multi-agent systems with governance constraints, solo-operator AI infrastructure, reversibility in autonomous systems, memory architecture for long-running agents, or audit-readiness in regulated-industry AI: the artifact set behind this paper is research-grade primary data. That set includes 296 decision documents, roughly 80 session records, the `memory-corrections.log` append-only mutation history, the supersession chain, and three blind peer reviews. Open to case studies, joint papers, course-material licensing, and graduate-student research engagements. The 45-day research sprint is the literal description of the build, not a marketing line. The data supports the framing.

### Contact

**Founder** · Cerebro Cyber Solutions
**Email:** <admin@cerebrocybersolutions.com>
**LinkedIn:** <https://www.linkedin.com/in/victor-gonzalez-2307b2206/>
**Workspace artifacts:** full path map available on request.

Direct outreach welcomed for technical briefings, pilot conversations, or research engagement.

---

## 20. Acknowledgments and Influences

Cerebro is not a solo intellectual achievement. The doctrine drew on a deep bench of external thinkers, published frameworks, and operator-community wisdom. The architectural absorptions tracked in `master-brain/decisions/` represent fewer than half of the influences that shaped the build. The rest are below.

**Direct technical influences (named, with absorption evidence in the workspace):**

- **Andrej Karpathy** — autoresearch as an operating pattern, the behavioral-guidelines approach for reducing common LLM failure modes, and the *build-understanding-by-building* pedagogy. Cerebro's `karpathy-autoresearch` extraction and `karpathy-guidelines` skill are direct ports. The autoresearch substrate (`nemotron-30b-a3b`) is named after the pattern donor's research style.
- **Matt Pocock** — TDD discipline, caveman compression mode, systematic-diagnosis patterns, and the *one-tool-call-per-checkpoint* operating tempo. Cerebro's `.agents/skills/` and several feedback memories trace back to Pocock-derived patterns.
- **Anthropic** — Claude Code as the primary build surface (this paper was authored in it), the architectural transparency in Anthropic's published frameworks, and the model-card / responsible-scaling-policy framing that the audit-ready commercial story (§11) leans on.
- **OpenAI** — Codex CLI as a peer-review surface and surgical-edit executor; the GPT-4-class reasoning route in the Senior Advisor tier; the model-naming-and-versioning discipline that informed Cerebro's Route Contract.
- **rUv (Reuven Cohen / ruvnet)** — `claude-flow` / Ruflo V3 as the swarm-orchestration pattern donor and as the active auto-memory ingest substrate Cerebro runs daily. The 60+ agent catalog and hive-mind / mesh / hierarchical-queen topology vocabulary informed §7's deliberate decision NOT to deploy swarm as primary; the daemon, however, runs as a load-bearing capture surface on every Claude Code turn.
- **Nous Research** — the Hermes agent-runtime pattern donor that anchored Cerebro's composer / seam / kanban / curator framing. Hermes was studied as a load-bearing pattern donor under Self-Sufficiency #9 and is being progressively replaced by Cerebro-native Constellation Composer.
- **Perplexity AI** — Bumblebee (Apache 2.0) as the pattern donor for read-only supply-chain and developer-tool inventory scanning; the embedded-fixtures-with-fake-names self-test pattern; the exposure-catalog-as-data-driven-response shape that maps cleanly onto Cerebro's state-ledger discipline.
- **Tiago Forte** — the *agentdb* family of skill packs (RAG, memory patterns, hyperbolic embedding indices) and the broader Building a Second Brain methodology that informed how Cerebro thinks about memory tiers and retrieval cadences.

**Conceptual influences and operator-community wisdom:**

- The **frontier-AI-lab community** generally — published architecture decisions, public retrospectives, the willingness of frontier teams (Anthropic / OpenAI / DeepMind alumni networks) to write about what they learned. The three-vantage triangulation method (§15) is a direct extension of how frontier labs run peer review internally.
- **GovCon and SDVOSB peer operators** — compliance war stories, CMMC L2 lived-experience accounts, FedRAMP-Moderate gotchas, IL5 procurement framings. The audit-ready commercial story (§11) would not exist without operators willing to share where the certification process actually breaks down.
- **University faculty and graduate researchers** — published work on multi-agent systems, AI governance, reversibility-as-design-primitive, and memory-architecture for long-running agents. The principle framework is consciously academic in its supersession discipline because peer-reviewed CS research is the model for what *"audit trail"* should look like.
- **YouTube technical CTOs, frontier-AI founders, and long-form-interview circuit hosts** — pattern languages for thinking about operator-owned infrastructure at scale; specific channels and shows that named load-bearing concepts before the engineering community had vocabulary for them.
- **The Cowork / Claude Code / Codex / Hermes plugin authors and skill ecosystem contributors** — every absorbed pattern in `tools/` and `.agents/skills/` came from someone who built and published.

**Pattern donors absorbed under Self-Sufficiency Principle #9.** The pattern-donor ecosystem spans vendored tool roots and third-party skill packs from authors and teams whose published work shaped Cerebro. The full inventory — names, license, pinned commit, absorption notes, and per-tool `CEREBRO_CAVEATS.md` documenting what was ported and what was rejected — lives in `VENDORED_IMPORTS.md` and the per-tool caveats files alongside each vendored root. The pattern-donor relationship is asymmetric: Cerebro takes patterns but does not depend on the runtime, which is what makes Origin Policy 3b workable.

Every name above represents work Cerebro stood on. None of these projects gave Cerebro permission to absorb them. All of them gave the engineering community a published artifact to learn from. *That is the part Cerebro is consciously trying to repay by publishing this paper.*

**Mobile planning captures — a load-bearing input pattern.** A substantial fraction of Cerebro's doctrine and decision content did not originate at the workstation. It originated on a phone, dictated between meetings, in cars, on walks, on travel days. The `mobile-planning-capture` skill exists because the operator's best thinking happens when the operator is mobile. The Sergeant doctrine thread, the build-freeze pivot framing, the AAR / Lessons-Learned doctrine seed, the workspace-architecture clarifications, the Pulsar trigger discussion, the executive commandments around local tool stack activation — all of these were mobile captures first, structured decision docs second. Without the mobile-first capture pipeline, the build velocity documented in §12 is not physically possible for a one-operator company. The pattern donor on this surface is the broader voice-dictation-for-thinkers community (Voicepal / Audiopen / Whisper-piped-to-LLM workflows); the Cerebro implementation routes through `mobile-planning-capture` → file decision → memory pointer → MOC backlink as a standard ritual.

**Methodology influences:**

- The **Three-Surface Rule** vocabulary borrows from operating-system design (kernel / user-space / driver) translated into agent-runtime context.
- The **principle framework** (Lockstep / Reversibility / Observability / Reproducibility / Least-Privilege) is a deliberate echo of CAP-theorem-era distributed-systems discipline. Cerebro is, architecturally, a distributed system with one operator.
- The **Sergeant Framework L0-L5 service tiers** (§14 Post-V1) borrow military-doctrine vocabulary deliberately. NCO-level operating discipline — Standard Operating Procedure, After-Action Review, Commander's Intent, Rules of Engagement — translates cleanly to agent-operations governance. The author's prior service is the source.

**On attribution discipline.** The absorption-pattern doctrine (§4) exists because nine absorptions in a 72-hour window in late April nearly overran governance bandwidth. The 5-step ritual — origin gate → vendored reference clone → swarm-analyze → cerebro-fit decision doc → wiring with snapshot tag — is what makes a pattern donor properly attributed rather than silently absorbed. *Every supersession is documented. Every pattern has a donor named in a decision doc.* That is the spirit of this acknowledgments section.

If your work shaped Cerebro and you are not named above, that is a future attribution patch waiting to be filed. Email or DM.

---

## 21. References

### Vendor + tooling

- **Anthropic Claude Code** — primary build surface. <https://docs.claude.com/claude-code>
- **Anthropic Claude API** — Senior Advisor + executor tier substrate. <https://docs.anthropic.com>
- **Anthropic Responsible Scaling Policy** — informs §11 audit-ready commercial story. <https://www.anthropic.com/responsible-scaling-policy>
- **OpenAI Codex CLI** — surgical-edit peer surface (Pattern B). <https://github.com/openai/codex>
- **Ollama** — local-inference runtime across all GPU nodes. <https://ollama.com>
- **LiteLLM** — model routing proxy (hub container). <https://docs.litellm.ai>
- **Qdrant** — vector database (hub container). <https://qdrant.tech>
- **PostgreSQL** — LiteLLM backing store (hub container). <https://www.postgresql.org>
- **Docker** — substrate isolation primitive for the hub container set. <https://docs.docker.com>
- **Tailscale** — private-mesh networking across the fleet. <https://tailscale.com>
- **NVIDIA Nemotron** — `nemotron-30b-a3b` autoresearch substrate. <https://build.nvidia.com>
- **Google Gemma 4 31B** — Senior Advisor local-tier model under Origin Policy 3a. <https://ai.google.dev/gemma>

### Pattern donors + influences

- **Andrej Karpathy** — autoresearch operating pattern, behavioral-guidelines approach, build-understanding-by-building pedagogy. <https://karpathy.ai>
- **Matt Pocock** — TDD discipline, systematic-diagnosis patterns, one-tool-call-per-checkpoint tempo. <https://www.totaltypescript.com>
- **Tiago Forte** — Building a Second Brain methodology informing memory tiers and retrieval cadences. <https://fortelabs.com/blog/basboverview/>
- **rUv (Reuven Cohen) — `claude-flow` / Ruflo V3** — swarm pattern donor; daemon runs as load-bearing memory-ingest substrate. <https://github.com/ruvnet/claude-flow>
- **Nous Research — Hermes** — agent-runtime pattern donor for the composer / seam / kanban / curator framing. <https://nousresearch.com>
- **Perplexity AI — Bumblebee** — Apache 2.0 pattern donor for read-only supply-chain scanning. <https://github.com/perplexityai>

### Academic + methodology

- **Distributed-systems CAP theorem** (Brewer 2000; Gilbert & Lynch 2002) — informs the principle framework's posture on Lockstep / Reversibility / Observability / Reproducibility / Least-Privilege as architectural constraints applied to a one-operator distributed system.
- **Multi-rater agreement methodology** (Cohen 1960; Fleiss 1971) — the social-science methodological ancestor of the three-vantage triangulation method used to produce this paper, adapted to multi-LLM peer architectural review.
- **NIST SP 800-171 / CMMC Level 2** — compliance frame for the audit-ready commercial story (§11). <https://csrc.nist.gov/pubs/sp/800/171/r3/final>
- **NIST AI Risk Management Framework (AI RMF 1.0)** — governance-posture frame for the principle framework. <https://www.nist.gov/itl/ai-risk-management-framework>
- **NCO operating doctrine** (US military Standard Operating Procedure / After-Action Review / Commander's Intent / Rules of Engagement traditions) — methodological frame for the Sergeant L0–L5 service-tier productization (§14 Post-V1).

### Internal artifacts (available on request)

The primary sources behind this paper — the synthesis document, the three blind-review drafts (Codex, Claude Code, Hermes), the canonical principle decision documents, the `memory-corrections.log` append-only mutation history, the operating dashboards, and the supersession chain — live in the Cerebro workspace. None are public artifacts; all are available to engaged readers (research collaborators, GovCon evaluators, pilot prospects) under the engagement framings in §19. The full path map is available on request via the contact section above.

---

*Drafted 2026-05-21 from a three-vantage synthesis of independent blind reviews by Codex (OpenAI), Claude Code (Anthropic), and Hermes (Nous Research). This document supersedes earlier "draft" framings of Cerebro's public narrative.*

*Cerebro Cyber Solutions · SDVOSB · 2026-05-21*

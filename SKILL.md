---
name: play-like-a-boss
description: Universal autonomous game player, deep auditor, and intelligent game repair engine. Triggers on "play this game", "play like a boss", "play start to finish", "find every bug", "deep audit", "audit this game", "audit this Three.js game", "fix all errors", "repair the game", "run everything", "test the game", "performance audit", "release audit", "regression guard", "boss mode". Works on web (Three.js/Phaser/PixiJS/Babylon/PlayCanvas/A-Frame), native engines (Unity/Unreal/Godot/RPG Maker/Construct/GameMaker), frameworks (Bevy/Raylib/Pygame), and desktop/mobile/emulator builds.
---

# PLAY LIKE A BOSS

You are the final boss of game quality. Your job is not to read code and guess — it is to **launch the game, play it like a human but with machine precision, audit every subsystem, find every defect including the ones nobody writes tickets for, repair them at the root, and prove the repairs hold.**

The deliverable is not a report. The deliverable is a game that has been played, audited, repaired, re-played, and verified.

## Grand Vision

Most "game audits" are code reviews with screenshots. This is not that.

The pipeline is:

```
LAUNCH → PLAY → OBSERVE → UNDERSTAND → FIND → DIAGNOSE → REPAIR → REBUILD → REPLAY → VERIFY → LEARN → REPEAT
```

You will drive the actual game through its actual input surface — keyboard, mouse, gamepad, touch, or whatever the platform exposes — across hundreds of state transitions, while observing renderer statistics, console output, memory, timing, physics state, and every other signal the platform gives you. When your direct instrumentation cannot see deep enough, you descend the capability ladder (native instrumentation → debug interfaces → browser automation → GUI automation → computer vision → screenshot → input simulation → human-assisted) until you either reach ground truth or exhaust the ladder honestly.

Then you do it again. And again. Until the game is clean or you have proven you cannot get cleaner.

## Non-Negotiables

1. **Play first, read second.** Never audit a game you haven't launched. Static review supplements live play; it never replaces it.
2. **Evidence or it didn't happen.** Every finding cites reproducible evidence: logs, screenshots, traces, metric deltas. "Looks wrong" is not a finding.
3. **Root cause, not symptom.** A repair that hides a bug is a failure. Fix the cause, prove the symptom is gone, prove nothing else broke.
4. **Capability honesty.** If the platform cannot expose a subsystem, say so explicitly and record it as a limitation. Never fabricate coverage.
5. **Minimal diffs.** Repairs touch as little code as possible. Refactors are out of scope unless they are the root cause.
6. **Safety first.** No destructive operations without a checkpoint. No edits to binary builds you cannot rebuild. Respect authorization limits on security testing.
7. **Session memory.** Every run accumulates knowledge in `.plab/`. Re-runs get smarter.

## Engine Compatibility Strategy

The skill is engine-agnostic. It does not assume Three.js. It detects the engine, selects the deepest viable adapter, and degrades gracefully when full instrumentation is unavailable.

| Engine family | Examples | Primary adapter |
|---|---|---|
| Web — custom/WebGL | Three.js, Babylon.js, PlayCanvas, A-Frame | `adapters/threejs.md`, `adapters/web-engines.md` |
| Web — 2D | Phaser, PixiJS, CreateJS, melonJS | `adapters/web-engines.md` |
| Native — commercial | Unity, Unreal, Godot, GameMaker, Construct | `adapters/unity.md`, `adapters/unreal.md`, `adapters/godot.md`, `adapters/rpg-maker.md` |
| Frameworks | Bevy, Raylib, Pygame, MonoGame, Love2D | `adapters/generic-engine.md` |
| Native desktop/mobile | Electron, Swift, Kotlin, platform builds | `adapters/generic-engine.md` |

Detection procedure: `core/universal-engine-detection.md`.

## Operational Modes

The user picks a mode, or you pick the right one from their request. If unclear, default to **BOSS MODE** — the full pipeline.

| Mode | Name | Scope | When to use |
|---|---|---|---|
| 1 | QUICK SCAN | 15–30 min smoke test | "does this work?", initial triage |
| 2 | FULL GAME AUDIT | Every audit dimension, no repair | "find every bug", "audit this game" |
| 3 | PLAY START→FINISH | Play the entire game start to credits/end | "play it all", regression baseline |
| 4 | DEEP BLIND SPOT HUNT | Adversarial edge-case probing | "find hidden bugs", "stress it" |
| 5 | FIX EVERYTHING | Audit + repair + verify loop | "fix all errors", "repair the game" |
| 6 | PERFORMANCE BEAST | Profiling, budgets, optimization | "it's slow", "optimize this" |
| 7 | REGRESSION GUARD | Re-run last known-good, diff findings | "did I break anything?" |
| 8 | FINAL RELEASE AUDIT | Gates A–F, ship/no-ship verdict | "prepare for release" |
| 9 | CONTINUOUS GAME QA | Iterative play-audit-fix cycles | "keep improving this game" |
| 10 | **BOSS MODE** | Full 18-phase pipeline, all subsystems, repair loop | Default. "run everything" |

Mode details and phase routing: this document, §18-Phase Pipeline.

## The 18-Phase BOSS MODE Pipeline

Every BOSS MODE run executes these phases in order. Phases may be skipped only with a documented reason in the audit record.

| # | Phase | Output |
|---|---|---|
| 1 | SESSION INIT | `.plab/` workspace, session config, mode selection |
| 2 | ENVIRONMENT RECON | Engine detection, platform, input surface, capabilities |
| 3 | GAME PROFILE | `templates/game-profile.md` filled: genre, mechanics, goals, controls |
| 4 | BUILD & LAUNCH | Build artifacts verified, game launched, first frame confirmed |
| 5 | SMOKE TEST | QUICK SCAN subset — launch, menu, core loop, quit |
| 6 | FUNCTIONAL AUDIT | `auditing/functional-audit.md` — every mechanic exercised |
| 7 | VISUAL AUDIT | `auditing/visual-audit.md` — rendering, UI, artifacts |
| 8 | PHYSICS AUDIT | `auditing/physics-audit.md` — collision, movement, constraints |
| 9 | ANIMATION AUDIT | `auditing/animation-audit.md` — states, transitions, blending |
| 10 | AUDIO AUDIT | `auditing/audio-audit.md` — playback, mixing, sync, lifecycle |
| 11 | AI/NPC AUDIT | `auditing/ai-audit.md` — behavior, pathing, edge cases |
| 12 | UI/UX AUDIT | `auditing/visual-audit.md` §UI + `auditing/functional-audit.md` §UI |
| 13 | PERFORMANCE AUDIT | `auditing/performance-audit.md` — FPS, memory, draw calls, leaks |
| 14 | SAVE/LOAD & MULTIPLAYER | save/load integrity, netcode sync where applicable |
| 15 | SECURITY AUDIT | `auditing/security-audit.md` — authorization-bounded |
| 16 | BLIND SPOT HUNT | `auditing/blind-spot-hunter.md` — all 7 categories |
| 17 | TRIAGE & REPAIR | `repair/intelligent-repair.md` — root cause, minimal diff, verify |
| 18 | FINAL REPORT | `templates/final-audit-report.md` — verdict, evidence, history |

Phases 6–16 can fan out across parallel agents when the runtime supports it. Phases 3, 5, 17, 18 are strictly sequential — they depend on accumulated state.

## Quality Gates

A run does not reach FINAL REPORT until every applicable gate passes. Gates are defined in `testing/release-validation.md`.

| Gate | Name | Pass condition |
|---|---|---|
| A | LAUNCH | Game launches to interactive state, no crash in first 60s |
| B | CORE LOOP | Primary mechanic works end-to-end at least once |
| C | COVERAGE | Every declared subsystem audited or explicitly marked UNREACHABLE with reason |
| D | FINDINGS | Every P0/P1 finding has a repair or a documented waiver with owner sign-off |
| E | REGRESSION | Re-run of repaired build shows no new findings vs. baseline |
| F | EVIDENCE | Final report contains reproducible evidence for every claim |

A gate FAIL halts the pipeline at the earliest responsible phase — you do not "finish" an audit with a broken gate; you go back and fix it.

## Decision Loop

Every action in the pipeline follows:

```
OBSERVE → UNDERSTAND → PLAN → ACT → VERIFY → LEARN → REPEAT
```

- **OBSERVE**: capture current state (screen, logs, metrics, memory, input surface).
- **UNDERSTAND**: compare observed state to expected state from the game profile or last known good.
- **PLAN**: choose the next action — play, probe, audit, repair, or escalate.
- **ACT**: execute via the deepest available adapter.
- **VERIFY**: confirm the action produced the expected state change.
- **LEARN**: write what you learned to `.plab/` session memory.
- **REPEAT**: until the mode's exit condition is met.

Full specification: `core/decision-engine.md`.

## Finding Format

Every defect discovered during audit or play is recorded as a `PLAB-NNNN` finding using `templates/bug-report.md`. Findings are the unit of work — they drive triage, repair, and regression.

Severity scale:

| Sev | Meaning | Examples |
|---|---|---|
| P0 | Game-breaking | Crash on launch, soft-lock, save corruption, core mechanic dead |
| P1 | Major | Progression blocked, major visual corruption, data loss, severe perf |
| P2 | Significant | Noticeable bugs, edge-case failures, minor perf issues |
| P3 | Minor | Cosmetic, rare edge cases, small inconsistencies |
| P4 | Polish | Nice-to-have, theoretical, documentation gaps |

## Repair Principles

Repairs follow `repair/intelligent-repair.md` and `repair/repair-safety.md`:

1. **Root cause first.** Reproduce → trace → identify the actual defect, not the symptom.
2. **Minimal diff.** Change the smallest surface that fixes the root cause.
3. **Checkpoint before touching.** Git branch or file snapshot before any edit.
4. **Rebuild and replay.** The repair is not done until the game is rebuilt, relaunched, and the original failure is shown to be gone.
5. **Regression sweep.** Re-run the affected audit dimensions plus a smoke pass to prove nothing else broke.
6. **Before/after evidence.** Capture the failing state, the fix, and the passing state.

## Safety Rules

- **Authorization-bounded security audit.** Only test what you own or have explicit permission to test. No exploitation of live services, no credential attacks, no data exfiltration. `auditing/security-audit.md` defines the boundaries.
- **No destructive ops without checkpoint.** Before any repair that touches source, save state, or config, create a restorable checkpoint.
- **No binary-only edits.** If the game ships only as a compiled binary you cannot rebuild, mark repair as BLOCKED and document the limitation.
- **Respect platform limits.** Some platforms (mobile, console, DRM'd builds) restrict instrumentation. Degrade honestly; never pretend coverage you don't have.
- **Human-assisted fallback.** When automation cannot reach a state (CAPTCHA, hardware-dependent, anti-cheat), hand off to the human with exact instructions rather than failing silently.

## Session Memory

Every run writes to `.plab/` in the game project root:

```
.plab/
  session-YYYYMMDD-HHMMSS/
    config.json          # mode, engine, adapter, capabilities
    game-profile.md      # filled template
    observations.jsonl   # append-only observation log
    findings/            # PLAB-NNNN bug reports
    repairs/             # repair reports
    evidence/            # screenshots, traces, logs, dumps
    test-results/        # matrix results
    final-report.md      # the verdict
  latest -> session-...  # symlink to most recent
```

Re-runs read `.plab/` first: prior findings, prior repairs, prior blockers. This is how the skill gets smarter over time. Schema: `core/gameplay-memory.md`.

## Module Map

| Need | Read |
|---|---|
| How to play the game autonomously | `core/autonomous-gameplay.md` |
| How the game thinks and what genre it is | `core/game-intelligence.md` |
| Detecting the engine and picking the adapter | `core/universal-engine-detection.md` |
| Session memory schema | `core/gameplay-memory.md` |
| Decision loop details | `core/decision-engine.md` |
| Three.js specifics | `adapters/threejs.md` |
| Babylon/Phaser/PixiJS/A-Frame/generic WebGL | `adapters/web-engines.md` |
| Unity | `adapters/unity.md` |
| Unreal | `adapters/unreal.md` |
| Godot | `adapters/godot.md` |
| RPG Maker | `adapters/rpg-maker.md` |
| Everything else | `adapters/generic-engine.md` |
| Functional audit checklist | `auditing/functional-audit.md` |
| Visual/UI audit checklist | `auditing/visual-audit.md` |
| Physics audit checklist | `auditing/physics-audit.md` |
| Animation audit checklist | `auditing/animation-audit.md` |
| Audio audit checklist | `auditing/audio-audit.md` |
| AI/NPC audit checklist | `auditing/ai-audit.md` |
| Performance audit checklist | `auditing/performance-audit.md` |
| Security audit checklist | `auditing/security-audit.md` |
| Blind spot hunting | `auditing/blind-spot-hunter.md` |
| Root cause analysis | `repair/root-cause-analysis.md` |
| Repair workflow | `repair/intelligent-repair.md` |
| Regression testing | `repair/regression-testing.md` |
| Repair safety | `repair/repair-safety.md` |
| Test matrix | `testing/gameplay-test-matrix.md` |
| Exploratory strategies | `testing/exploratory-testing.md` |
| Release gates | `testing/release-validation.md` |
| Report templates | `templates/` |

## Command Interpretation

Map natural-language requests to modes and phases:

| User says | Mode | Notes |
|---|---|---|
| "play this game" | BOSS MODE or PLAY START→FINISH | If they want coverage too, BOSS MODE |
| "find every bug" | FULL GAME AUDIT or FIX EVERYTHING | If they want repairs too, FIX EVERYTHING |
| "audit this Three.js game" | FULL GAME AUDIT | Three.js adapter + all audit dims |
| "fix all errors" | FIX EVERYTHING | Audit → repair → verify loop |
| "play like a boss" | BOSS MODE | Full pipeline |
| "run everything" | BOSS MODE | Full pipeline |
| "prepare for release" | FINAL RELEASE AUDIT | Gates A–F, ship verdict |
| "it's slow" / "optimize" | PERFORMANCE BEAST | Profiling + targeted repair |
| "did I break anything?" | REGRESSION GUARD | Re-run baseline, diff findings |
| "keep improving this" | CONTINUOUS GAME QA | Iterative cycles |
| "find hidden bugs" / "stress it" | DEEP BLIND SPOT HUNT | All 7 blind-spot categories |
| "does this work?" | QUICK SCAN | 15–30 min smoke test |

When the request is ambiguous between audit-only and audit+repair, default to the more thorough option (FIX EVERYTHING) unless the user explicitly says "just audit" or "don't change anything."

## How to Start

1. Read this file fully.
2. Run Phase 1–3: init session, recon environment, build game profile.
3. Route to the requested mode.
4. For BOSS MODE, execute all 18 phases.
5. Write the final report. Deliver the verdict.

Do not skip phases. Do not fabricate results. Do not stop early because it is hard.

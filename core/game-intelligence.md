# GAME INTELLIGENCE

The gameplay model that drives autonomous play. This is not a script — it is a reasoning layer that observes the game, infers its rules, and chooses actions that a competent human player would choose, but faster and more consistently.

## Core Principle

**Play the game, don't test the code.** You are not clicking buttons to hit code coverage. You are trying to *win*, *survive*, *explore*, and *break* the game the way a player would — then going further than a player would.

Every action should answer: "What would a player do next, and what would a player never think to try?"

## Gameplay Model

Maintain a live model of the game state in working memory:

```
GAME STATE
├── PLAYER STATE
│   ├── position, velocity, health, resources, inventory, equipment
│   ├── current animation state, current action state
│   └── status effects, buffs, debuffs
├── WORLD STATE
│   ├── level/map ID, zone, environment conditions
│   ├── NPC states, enemy states, interactive object states
│   └── time of day, weather, game phase
├── PROGRESSION STATE
│   ├── current objective, quest state, unlocks
│   ├── collectibles found, secrets discovered
│   └── checkpoints, save state
├── UI STATE
│   ├── current screen/menu/dialog
│   ├── active HUD elements, notifications
│   └── cursor/focus state
└── SESSION METRICS
    ├── play time, deaths, retries, items used
    ├── FPS, memory, console errors, warnings
    └── anomalies detected (see BLIND SPOT HUNTER)
```

Update this model after every action. Stale state is worse than no state.

## Genre-Adaptive Behavior

Different genres demand different play patterns. Detect genre in Phase 3 (Game Profile) and load the matching strategy.

### Platformer

- **Core loop**: move → jump → land → repeat, with obstacles and enemies.
- **Key probes**:
  - Jump height/distance boundaries — can you jump too far? Not far enough?
  - Coyote time — jump just after leaving a ledge.
  - Input buffering — press jump just before landing.
  - Wall jumps, double jumps, dash mechanics if present.
  - Fall damage boundaries — exact pixel/velocity thresholds.
  - Moving platform timing — jump on, ride, jump off.
- **Stuck patterns**: precision jumps, sequence breaks, soft-locks in vertical shafts.
- **Blind spots**: out-of-bounds clipping, ceiling bonks, enemy spawn camping, frame-perfect tricks.

### Action / Combat

- **Core loop**: approach → attack → dodge → reposition → repeat.
- **Key probes**:
  - Hitbox vs hurtbox boundaries — attack just outside range.
  - i-frames — attack during dodge window.
  - Combo chains — input buffering, cancel windows.
  - Enemy AI aggro ranges — pull adds, reset fights.
  - Resource management — run out of health/mana/ammo deliberately.
  - Crowd control — stun, slow, knockback edge cases.
- **Stuck patterns**: unwinnable fights, soft-locks on boss phases, ammo/health deadlocks.
- **Blind spots**: damage through walls, collision exploits, infinite combos, AI stuck states.

### RPG / JRPG

- **Core loop**: explore → talk → quest → battle → loot → level → repeat.
- **Key probes**:
  - Dialogue trees — every branch, every choice, every exit condition.
  - Quest states — accept, progress, complete, fail, abandon.
  - Inventory — full inventory, item stacking, equipment swaps, key items.
  - Party management — formation, leveling, skills, equipment loadouts.
  - Save/load — mid-quest, mid-battle, post-cutscene, on title screen.
  - Random encounters — grinding boundaries, rare spawns.
- **Stuck patterns**: missable quests, sequence breaks, save corruption, party wipe soft-locks.
- **Blind spots**: sequence breaks, out-of-order boss kills, item duplication, stat overflow.

### Strategy / RTS / Tower Defense

- **Core loop**: gather → build → defend → attack → expand → repeat.
- **Key probes**:
  - Resource caps — hit max supply/population/mana.
  - Build queues — spam-click, cancel, reorder.
  - Pathfinding — maze enemies, block chokepoints, wall off spawns.
  - Tech tree — rush strategies, skip requirements if possible.
  - Win/lose conditions — sudden death, timer expiry, last unit standing.
  - Multiplayer sync — desync, lag compensation, race conditions.
- **Stuck patterns**: soft-locks on resource deadlocks, unwinnable waves, UI deadlocks.
- **Blind spots**: resource exploits, pathfinding failures, build-order skips, AI cheats.

### Simulation / Sandbox / Life Sim

- **Core loop**: customize → simulate → observe → intervene → repeat.
- **Key probes**:
  - Time controls — pause, fast-forward, rewind if present.
  - Sandbox limits — spawn limits, terrain editing, object caps.
  - Emergent behavior — chaos scenarios, stress populations.
  - Save/load — mid-simulation, long-running stability.
  - Mod/plugin boundaries — if moddable, test the edges.
- **Stuck patterns**: simulation crashes, state corruption, memory growth.
- **Blind spots**: physics explosions, AI herd behavior, floating-point drift.

### Horror / Atmospheric

- **Core loop**: explore → tension → encounter → survive → progress.
- **Key probes**:
  - Fear triggers — scripted scares, jump scares, atmosphere breaks.
  - Resource scarcity — ammo, health, sanity/stamina.
  - Stealth mechanics — detection ranges, hiding spots, noise.
  - Multiple endings — choice consequences, missable paths.
- **Stuck patterns**: unwinnable encounters, missable keys, soft-locks.
- **Blind spots**: sequence breaks, out-of-bounds escapes, monster soft-locks.

### Puzzle / Adventure

- **Core loop**: observe → hypothesize → manipulate → verify → progress.
- **Key probes**:
  - Every interactable — not just obvious ones.
  - Sequence breaking — do puzzles in wrong order.
  - Item combination — use items on wrong targets.
  - Environmental storytelling — missable lore, hidden areas.
  - Backtracking — return to old areas, check for changes.
- **Stuck patterns**: unsolvable states, missed triggers, soft-locks.
- **Blind spots**: clip through walls, skip cutscenes, sequence breaks.

## Exploration Strategy

Systematic exploration beats random clicking. Use this order:

1. **Breadth first** — map the world. Visit every reachable area, note boundaries.
2. **Depth first** — within each area, probe interactables, secrets, edge cases.
3. **Backtracking** — return to previous areas after new abilities/items.
4. **Boundary pushing** — try to go where you're not supposed to go.
5. **Sequence breaking** — skip steps, do things out of order, use items early.
6. **Stress testing** — spam inputs, hold buttons, disconnect mid-action.
7. **Idle testing** — leave the game running, let systems tick, check for drift.

For each area, maintain an exploration log:

```
AREA: <name>
BOUNDARIES: <what blocks you, where>
INTERACTABLES: <list of objects/NPCs/doors/triggers>
SECRETS: <hidden items, easter eggs, missable content>
DEAD ENDS: <areas that lead nowhere>
ANOMALIES: <anything that behaved unexpectedly>
```

## Stuck Detection & Recovery

A stuck state is any situation where the game stops progressing for >30 seconds without a crash. Detect and classify:

| Stuck type | Signature | Recovery |
|---|---|---|
| Soft-lock | No valid inputs, no progress, no error | Reload last checkpoint, try alternate path |
| Dead end | Explored all options, no exit | Backtrack, use different ability/item |
| UI freeze | Input ignored, menu unresponsive | Check for modal dialogs, hidden overlays |
| Physics stuck | Character/object wedged in geometry | Nudge position, reload, try different approach |
| AI freeze | NPC/enemy stops responding | Wait, reload, check for triggers |
| Resource deadlock | Can't afford/progress, no alternative | Find exploit, reload, adjust strategy |
| Sequence break | Skipped required step, now blocked | Reload, follow intended order |
| Infinite loop | Game repeats same state/action | Break input pattern, reload |

When stuck:

1. **Capture evidence** — screenshot, log dump, state snapshot.
2. **Classify** — which stuck type?
3. **Attempt recovery** — reload, alternate path, exploit.
4. **If unrecoverable** — record as finding (P0/P1), move to next area.
5. **Never silently skip** — a stuck state you didn't investigate is a blind spot.

## Human-Like Action Patterns

Vary your play style to catch timing-dependent bugs:

- **Speed runner** — minimal inputs, skip cutscenes, sequence breaks.
- **Completionist** — every collectible, every secret, every side quest.
- **Chaos agent** — random inputs, spam, disconnects, weird combinations.
- **Casual player** — normal pace, read UI, follow tutorials.
- **Speedrunner + blindfold** — navigate by memory, test audio cues.
- **Input masher** — hold buttons, mash menus, spam interact.
- **Patient observer** — idle in areas, watch for ambient bugs.

Rotate through these patterns across sessions. Each catches different bug classes.

## Objective Tracking

Maintain a live objective stack:

```
PRIMARY OBJECTIVE: <main goal>
  ├── SUB-OBJECTIVE: <current step>
  │   ├── COMPLETED: <list>
  │   └── BLOCKED: <list with reasons>
  └── SIDE OBJECTIVES: <optional goals>
```

Update after every meaningful action. If the objective becomes unclear (game doesn't tell you what to do), that's a UI/UX finding.

## When to Stop Playing

Stop when:

- All areas explored, all objectives completed or blocked.
- No new findings in last N minutes (suggest 10–15 for active play).
- Game reaches credits/end state.
- Platform limits prevent further progress (hardware, DRM, anti-cheat).
- User requests stop.

Then move to audit phases. Playing and auditing are complementary, not sequential — interleave them.

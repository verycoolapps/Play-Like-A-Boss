# BLIND SPOT HUNTER

Adversarial edge-case probing that finds bugs nobody writes tickets for. This subsystem hunts for the defects that only appear at boundaries, during timing windows, in unusual states, or through exploitation.

## Philosophy

Most bugs are found by testing the happy path. Blind spot hunting tests everything else:

- **Boundaries** — exact limits, edge values, overflow conditions.
- **Timing** — frame-perfect inputs, race conditions, state transitions.
- **Interactions** — combining systems in unexpected ways.
- **States** — unusual game states, corrupted states, impossible states.
- **Environment** — extreme conditions, resource exhaustion, unusual setups.
- **Logic** — contradictions, paradoxes, sequence breaks.
- **Exploits** — ways to break the game intentionally.

## The 7 Blind Spot Categories

### 1. Boundary Blind Spots

**What**: Exact limits and edge values where behavior changes.

**Probe techniques**:

| Technique | Example | What to look for |
|---|---|---|
| Exact threshold | Health = 1, ammo = 0, inventory = max | Does behavior change at exact limit? |
| Off-by-one | Level 99 vs 100, day 364 vs 365 | Does progression work at boundaries? |
| Overflow | Gold = 999999, XP = max int | Does value wrap or crash? |
| Underflow | Health = -1, gold = -100 | Does game handle negative values? |
| Precision limits | Position = 0.000001, time = very small | Does physics/math break? |
| Resolution limits | Min/max supported resolution | Does UI break at extremes? |
| Count limits | 1000 enemies, 10000 items | Does game scale or crash? |

**Questions to ask**:
- What happens at exactly 0? At exactly max?
- Does the game handle values one above/below limits?
- Are there hardcoded limits that can be exceeded?
- Does the UI display extreme values correctly?

### 2. Timing Blind Spots

**What**: Frame-perfect windows, race conditions, and temporal edge cases.

**Probe techniques**:

| Technique | Example | What to look for |
|---|---|---|
| Frame-perfect input | Press jump on exact landing frame | Does coyote time work? |
| Race condition | Save during load, quit during autosave | Does state corrupt? |
| Transition window | Input during scene change | Does input get lost or duplicated? |
| Animation cancel | Cancel animation mid-frame | Does state stay consistent? |
| Network jitter | Packet arrives late/early | Does game handle lag? |
| Timer expiry | Timer hits 0 during action | Does action complete or abort? |
| Cooldown boundary | Use ability on exact cooldown end | Does cooldown reset correctly? |

**Questions to ask**:
- What happens if input arrives 1 frame early/late?
- Can you act during transitions?
- Do timers expire at correct times?
- Are there race conditions between systems?

### 3. Interaction Blind Spots

**What**: Combining systems or inputs in unexpected ways.

**Probe techniques**:

| Technique | Example | What to look for |
|---|---|---|
| System overlap | Pause during combat, save during cutscene | Do systems conflict? |
| Input combination | Jump + attack + interact simultaneously | Does game prioritize correctly? |
| State conflict | Dead but menu still open, invincible but damage taken | Does state stay consistent? |
| Resource conflict | Use last health potion during boss fight | Does game handle scarcity? |
| UI conflict | Open inventory during dialogue | Does UI layer correctly? |
| Audio-visual desync | Sound plays but animation doesn't | Are systems synchronized? |
| Physics-logic conflict | Object falls through floor but game thinks it's on floor | Do physics and logic agree? |

**Questions to ask**:
- What happens when two systems try to do opposite things?
- Can you be in two states at once?
- Do UI layers stack correctly?
- Are physics and game logic synchronized?

### 4. State Blind Spots

**What**: Unusual, corrupted, or impossible game states.

**Probe techniques**:

| Technique | Example | What to look for |
|---|---|---|
| Impossible state | Dead but alive, quest complete but not started | Does game handle contradictions? |
| Corrupted state | Negative health, NaN position, invalid item ID | Does game recover or crash? |
| Stale state | Load old save after update, continue after quit | Does state migrate correctly? |
| Partial state | Half-loaded level, half-saved game | Does game complete or abort? |
| Synced state | Multiplayer desync, server/client mismatch | Does game resolve conflicts? |
| Persistent state | Quit during autosave, load during transition | Is state preserved correctly? |

**Questions to ask**:
- What happens if state is corrupted?
- Can the game recover from bad state?
- Are state transitions atomic?
- Does the game validate state on load?

### 5. Environmental Blind Spots

**What**: Extreme conditions, resource exhaustion, and unusual environments.

**Probe techniques**:

| Technique | Example | What to look for |
|---|---|---|
| Low resources | 1% battery, low memory, slow CPU | Does game degrade gracefully? |
| High load | 100 enemies, 1000 particles, max draw calls | Does game maintain FPS? |
| Network issues | High latency, packet loss, disconnect | Does game handle gracefully? |
| Display issues | Tiny window, weird aspect ratio, multiple monitors | Does UI adapt? |
| Input issues | No keyboard, no mouse, controller only | Does game adapt? |
| Storage issues | Full disk, read-only filesystem | Does game handle gracefully? |
| Thermal issues | Overheating, thermal throttling | Does game reduce load? |

**Questions to ask**:
- What happens under extreme load?
- Does the game degrade gracefully?
- Are there hard limits that break the game?
- Does the game handle resource exhaustion?

### 6. Logic Blind Spots

**What**: Contradictions, paradoxes, and sequence breaks.

**Probe techniques**:

| Technique | Example | What to look for |
|---|---|---|
| Sequence break | Skip tutorial, enter area early, use item before obtaining | Does game handle out-of-order? |
| Logical contradiction | Quest says "kill 10 enemies" but only 5 exist | Does game detect impossibility? |
| Circular dependency | A requires B, B requires A | Does game detect deadlock? |
| Missing prerequisite | Use skill without learning it | Does game prevent or allow? |
| Impossible requirement | Collect item that doesn't exist | Does game handle gracefully? |
| Paradox | Save before and after same event | Does state stay consistent? |

**Questions to ask**:
- Can you break the intended sequence?
- Does the game detect impossible states?
- Are there circular dependencies?
- Can you complete the game without doing X?

### 7. Exploit Blind Spots

**What**: Ways to intentionally break the game.

**Probe techniques**:

| Technique | Example | What to look for |
|---|---|---|
| Speed hack | Move faster than intended | Does game detect/correct? |
| Teleport | Move to invalid locations | Does game clamp position? |
| Item duplication | Duplicate items via save/load | Does game prevent? |
| Stat overflow | Max out stats, overflow values | Does game handle extremes? |
| Sequence break | Skip required steps | Does game detect missing steps? |
| Resource exploit | Infinite money/items | Does game prevent? |
| Physics exploit | Clip through walls, fly | Does game prevent? |
| UI exploit | Click hidden buttons, spam inputs | Does game handle? |

**Questions to ask**:
- Can you get advantages not intended?
- Can you break game rules?
- Can you corrupt game state?
- Can you crash the game intentionally?

## The 8-Question Analysis Format

For every blind spot probe, answer these 8 questions:

```
BLIND SPOT ANALYSIS
├── 1. WHAT did you test?
│   └── Describe the exact scenario, inputs, and conditions.
│
├── 2. WHY did you test it?
│   └── What blind spot category? What edge case? What suspicion?
│
├── 3. HOW did you test it?
│   └── Exact steps, tools, timing, repetitions.
│
├── 4. WHAT happened?
│   └── Observed result, unexpected behavior, errors.
│
├── 5. WHAT should have happened?
│   └── Expected behavior based on game design.
│
├── 6. WHAT is the root cause?
│   └── Why did it happen? Code bug, design flaw, edge case?
│
├── 7. HOW severe is it?
│   └── P0–P4 severity, impact on gameplay.
│
└── 8. HOW to fix it?
    └── Recommended fix, workaround, or prevention.
```

## Probe Execution

### Systematic Probing

For each category, systematically test:

1. **Enumerate** — list all possible boundary values, states, combinations.
2. **Prioritize** — focus on high-risk areas first.
3. **Execute** — run probes systematically.
4. **Document** — record every result.
5. **Analyze** — look for patterns, root causes.

### Randomized Probing

Use seeded randomization for reproducibility:

```python
import random
random.seed(42)  # Reproducible

for i in range(1000):
    # Random inputs
    x = random.randint(-1000, 1000)
    y = random.randint(-1000, 1000)
    action = random.choice(['jump', 'attack', 'interact', 'move'])
    
    # Execute and observe
    result = game.execute(x, y, action)
    
    # Log anomalies
    if result.is_anomalous():
        log_finding(f"Random probe {i}: {result}")
```

### Differential Probing

Compare behavior across:

- Different builds (old vs new)
- Different platforms (PC vs mobile)
- Different settings (low vs high quality)
- Different states (new game vs continued)

### Stress Probing

Push systems to limits:

- Maximum entities (enemies, items, particles)
- Maximum duration (24-hour soak test)
- Maximum inputs (input spam, rapid actions)
- Maximum memory (memory leak detection)

## Blind Spot Categories by Genre

### Platformer

- **Boundary**: Exact jump height/distance, coyote time frames, ledge grab distance.
- **Timing**: Frame-perfect jumps, input buffering windows, animation cancel timing.
- **Interaction**: Jump + attack, crouch + jump, wall jump + dash.
- **State**: Dead but invincible, paused but physics running, checkpoint during fall.
- **Environmental**: Low FPS during precision jumps, lag spikes, resolution changes.
- **Logic**: Sequence breaks, skip areas, use abilities early.
- **Exploit**: Clip through walls, infinite jumps, teleport through barriers.

### RPG

- **Boundary**: Level cap, max stats, inventory limits, gold overflow.
- **Timing**: Save during battle, load during cutscene, quit during autosave.
- **Interaction**: Equip + use item, trade + quest, craft + sell.
- **State**: Dead party but quest active, item equipped but not owned, quest complete but not turned in.
- **Environmental**: Low memory with many items, long play sessions, save file corruption.
- **Logic**: Sequence breaks, missable quests, contradictory quest states.
- **Exploit**: Item duplication, stat overflow, sequence break, save editing.

### Strategy/RTS

- **Boundary**: Max units, max resources, max build queue, population cap.
- **Timing**: Build cancel timing, attack move timing, ability cooldowns.
- **Interaction**: Build + train, research + produce, multiple commands.
- **State**: No resources but units alive, research complete but not applied, building destroyed but queue continues.
- **Environmental**: Lag with many units, low FPS during large battles, network desync.
- **Logic**: Impossible build orders, resource deadlocks, unwinnable scenarios.
- **Exploit**: Resource duplication, unit spam, pathfinding exploits, AI cheats.

### Horror

- **Boundary**: Sanity/stamina limits, ammo limits, health thresholds.
- **Timing**: Jump scare timing, monster spawn timing, save during chase.
- **Interaction**: Flashlight + weapon, inventory + puzzle, stealth + combat.
- **State**: Dead but monster still chasing, item used but not consumed, puzzle solved but not registered.
- **Environmental**: Pitch black areas, loud environments, VR motion sickness.
- **Logic**: Sequence breaks, missable keys, impossible puzzles, soft-locks.
- **Exploit**: Sequence break, monster soft-lock, item duplication, save editing.

## Evidence Collection

For each blind spot probe:

1. **Setup** — describe the scenario.
2. **Inputs** — exact inputs sent.
3. **Timing** — when inputs were sent.
4. **Result** — what happened.
5. **Evidence** — screenshots, logs, state dumps.
6. **Analysis** — 8-question format.

Store evidence in `.plab/session-*/evidence/blind-spots/`.

## When to Stop

Stop blind spot hunting when:

- All 7 categories probed at least once.
- All P0/P1 findings documented.
- No new findings in last 20 probes.
- Time budget exhausted.
- Diminishing returns (probes yield no new findings).

## Integration with Other Audits

Blind spot findings often reveal issues in other dimensions:

- Boundary bug → functional audit
- Timing bug → physics audit
- Interaction bug → functional audit
- State bug → save/load audit
- Environmental bug → performance audit
- Logic bug → functional audit
- Exploit → security audit

Cross-reference findings and coordinate audits.

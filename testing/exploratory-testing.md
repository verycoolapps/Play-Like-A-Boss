# EXPLORATORY TESTING

Unscripted, creative testing approaches that go beyond scripted test cases. Exploratory testing finds bugs that scripted tests miss.

## Philosophy

**Scripted tests verify what you expect. Exploratory testing discovers what you don't expect.**

Exploratory testing is simultaneous learning, test design, and test execution. It's about exploring the game with a goal, but without a rigid script.

## Exploratory Testing Approaches

### 1. Scripted Testing

**What**: Follow predefined test cases exactly.

**When**: Regression testing, known bug verification, critical path validation.

**Process**:

1. Follow test case steps exactly.
2. Record results.
3. Compare to expected.
4. Document deviations.

**Limitation**: Only finds bugs you anticipated.

### 2. Exploratory Testing

**What**: Explore the game with a goal but no rigid script.

**When**: Initial exploration, bug hunting, learning the game.

**Process**:

1. **Define mission** — what are you trying to learn/explore?
2. **Explore freely** — try different approaches.
3. **Take notes** — record observations.
4. **Follow leads** — pursue interesting findings.
5. **Document bugs** — record any issues found.

**Example missions**:

- "Explore all areas of the map."
- "Try to break the combat system."
- "Find all hidden secrets."
- "Test the save/load system thoroughly."

### 3. Boundary Testing

**What**: Test exact limits and edge values.

**When**: After basic functionality works, before release.

**Process**:

1. **Identify boundaries** — what are the limits?
2. **Test exact values** — test at, above, below limits.
3. **Test combinations** — multiple boundaries at once.
4. **Document results** — record any issues.

**Examples**:

- Health = 0, 1, max, max+1
- Inventory = full, empty, one slot left
- Level = 1, max, max+1
- Coordinates = min, max, out of bounds

### 4. Randomized Testing

**What**: Use random inputs to discover unexpected behavior.

**When**: Stress testing, fuzzing, finding edge cases.

**Process**:

1. **Define input space** — what can be randomized?
2. **Generate random inputs** — use seeded random for reproducibility.
3. **Execute and observe** — run game with random inputs.
4. **Log anomalies** — record unexpected behavior.

**Example**:

```python
import random
random.seed(42)  # Reproducible

for i in range(1000):
    # Random inputs
    x = random.randint(-1000, 1000)
    y = random.randint(-1000, 1000)
    action = random.choice(['jump', 'attack', 'interact', 'move', 'use_item'])
    
    # Execute
    result = game.execute(x, y, action)
    
    # Log anomalies
    if result.is_anomalous():
        log_finding(f"Random probe {i}: {result}")
```

### 5. State Testing

**What**: Test unusual or corrupted game states.

**When**: After core functionality works, testing robustness.

**Process**:

1. **Identify states** — what states can the game be in?
2. **Create unusual states** — corrupt, partial, impossible states.
3. **Test transitions** — move between states.
4. **Document results** — record any issues.

**Examples**:

- Dead but menu still open
- Quest complete but not turned in
- Item equipped but not owned
- Save during cutscene, load during battle

### 6. Stress Testing

**What**: Push the game to its limits.

**When**: Performance testing, stability testing, finding breaking points.

**Process**:

1. **Identify limits** — what are the maximum values?
2. **Push to limits** — test at maximum load.
3. **Monitor** — watch for crashes, performance issues.
4. **Document** — record breaking points.

**Examples**:

- 1000 enemies on screen
- 10000 items in inventory
- 24-hour continuous play
- Maximum particles/effects
- Rapid input spam

### 7. Long-Session Testing

**What**: Play for extended periods to find time-dependent bugs.

**When**: Before release, testing stability.

**Process**:

1. **Set duration** — how long to test? (4 hours, 24 hours, etc.)
2. **Play continuously** — don't stop, keep playing.
3. **Monitor** — watch for degradation, leaks, crashes.
4. **Document** — record any issues over time.

**What to look for**:

- Memory leaks (memory grows over time)
- Performance degradation (FPS drops over time)
- State corruption (game state becomes inconsistent)
- Crashes (game crashes after extended play)
- Save corruption (saves become corrupted over time)

### 8. Differential Testing

**What**: Compare behavior across different versions/platforms/settings.

**When**: After updates, testing consistency.

**Process**:

1. **Identify variables** — what differs between versions?
2. **Run same tests** — execute identical tests on both.
3. **Compare results** — look for differences.
4. **Document** — record any inconsistencies.

**Examples**:

- Old version vs new version
- PC vs mobile
- Low quality vs high quality settings
- New game vs continued game

### 9. Reproducibility Testing

**What**: Ensure bugs can be reliably reproduced.

**When**: After finding bugs, verifying fixes.

**Process**:

1. **Document steps** — exact steps to reproduce.
2. **Run multiple times** — verify consistency.
3. **Identify variables** — what factors affect reproduction?
4. **Minimize** — reduce to simplest possible repro.

**Why it matters**: If you can't reproduce a bug, you can't verify it's fixed.

## Exploratory Testing Techniques

### Charter-Based Testing

**What**: Define a mission/charter for exploration.

**Example**:

```
CHARTER: Explore combat system
TIME: 30 minutes
FOCUS: Try to break combat mechanics
APPROACH: Vary attack timing, combine abilities, test edge cases
SUCCESS: Find at least 3 issues or confirm system is robust
```

### Session-Based Testing

**What**: Time-boxed exploration sessions.

**Example**:

```
SESSION 1 (30 min): Explore world map
SESSION 2 (30 min): Test combat system
SESSION 3 (30 min): Try to break save/load
SESSION 4 (30 min): Random input fuzzing
```

### Mind Mapping

**What**: Visually map out areas to explore.

**Example**:

```
Game
├── World
│   ├── Map 1
│   │   ├── Secrets
│   │   ├── Enemies
│   │   └── Items
│   └── Map 2
│       ├── Secrets
│       ├── Enemies
│       └── Items
├── Systems
│   ├── Combat
│   ├── Inventory
│   ├── Save/Load
│   └── UI
└── Edge Cases
    ├── Boundary values
    ├── Timing issues
    └── State conflicts
```

### Heuristic-Based Testing

**What**: Use heuristics to guide exploration.

**Common heuristics**:

- **CRUD** — Create, Read, Update, Delete operations.
- **Boundary** — Test at limits and edges.
- **State** — Test state transitions.
- **Interaction** — Test system interactions.
- **Error** — Test error handling.
- **Performance** — Test under load.
- **Security** — Test for vulnerabilities.
- **Usability** — Test user experience.

## Exploratory Testing Documentation

### Session Notes

```
EXPLORATORY TESTING SESSION
Date: 2026-10-13
Tester: PLAB
Duration: 60 minutes
Mission: Find bugs in combat system

OBSERVATIONS:
- Combat feels responsive, no input lag
- Combo system works well, timing is forgiving
- Found bug: Attack animation doesn't cancel properly (PLAB-0042)
- Found bug: Damage numbers overlap at high enemy count (PLAB-0043)
- Found bug: Block doesn't work against projectiles (PLAB-0044)

LEADS TO FOLLOW:
- Test combo system more thoroughly
- Test block against all enemy types
- Test damage numbers with 20+ enemies

NEXT SESSION:
- Focus on combo system edge cases
- Test block timing windows
- Stress test with maximum enemies
```

### Bug Report

Use `templates/bug-report.md` for each bug found.

## Exploratory Testing Tools

### Input Generation

```python
# Random input generator
import random

def random_input():
    inputs = ['jump', 'attack', 'interact', 'move_up', 'move_down', 'move_left', 'move_right']
    return random.choice(inputs)

# Seeded for reproducibility
random.seed(42)
for i in range(100):
    action = random_input()
    game.execute(action)
```

### State Inspection

```python
# Dump game state
def dump_state():
    return {
        'player': player.get_state(),
        'enemies': [e.get_state() for e in enemies],
        'inventory': inventory.get_items(),
        'quests': quest_log.get_quests(),
        'position': player.get_position(),
        'health': player.get_health()
    }
```

### Screenshot Capture

```python
# Capture screenshots for evidence
import pyautogui

for i in range(100):
    screenshot = pyautogui.screenshot()
    screenshot.save(f'screenshot_{i:03d}.png')
    time.sleep(1)
```

## When to Use Exploratory Testing

| Scenario | Approach |
|---|---|
| New game, unknown bugs | Exploratory testing |
| After major update | Differential testing |
| Before release | All approaches |
| Regression testing | Scripted testing |
| Bug verification | Reproducibility testing |
| Performance testing | Stress testing |
| Stability testing | Long-session testing |

## Exploratory Testing Checklist

- [ ] Define mission/charter.
- [ ] Set time limit.
- [ ] Take notes.
- [ ] Follow leads.
- [ ] Document bugs.
- [ ] Review findings.
- [ ] Plan next session.

## Integration with Other Modules

- **Test matrix** → `testing/gameplay-test-matrix.md`
- **Blind spot hunter** → `auditing/blind-spot-hunter.md`
- **Functional audit** → `auditing/functional-audit.md`
- **Release validation** → `testing/release-validation.md`

# REGRESSION TESTING

Ensuring repairs don't break existing functionality. Regression testing verifies that fixes don't introduce new bugs.

## Philosophy

**Every repair is a potential regression.** The fix for bug A might break bug B's fix, or introduce bug C. Regression testing catches this.

## Regression Testing Strategy

### Test Scope

For each repair, determine regression scope:

| Scope | When to Use | Examples |
|---|---|---|
| **Direct** | Code that calls the fixed code | Function callers, event handlers |
| **Related** | Systems that interact with fixed code | Physics → collision, UI → input |
| **Core** | Essential game functionality | Movement, combat, save/load |
| **Full** | Major changes, high-risk repairs | Engine updates, architecture changes |

### Regression Test Types

| Type | Purpose | When to Run |
|---|---|---|
| **Unit regression** | Test individual functions | After every code change |
| **Integration regression** | Test component interactions | After integration changes |
| **Functional regression** | Test game mechanics | After gameplay changes |
| **Visual regression** | Test visual output | After rendering changes |
| **Performance regression** | Test performance metrics | After optimization changes |
| **Save/load regression** | Test persistence | After save system changes |

## Regression Test Process

### Phase 1: Identify Affected Areas

**Goal**: Determine what could be affected by the repair.

**Process**:

1. **Read the diff** — what code changed?
2. **Trace dependencies** — what depends on changed code?
3. **Identify systems** — which game systems are affected?
4. **Prioritize** — which areas are highest risk?

**Output**: List of affected areas and test priorities.

### Phase 2: Design Regression Tests

**Goal**: Create tests that would catch regressions.

**Process**:

1. **Review existing tests** — are there tests for affected areas?
2. **Add missing tests** — create tests for untested areas.
3. **Design test cases** — what scenarios could break?
4. **Prioritize** — which tests are most important?

**Output**: Regression test plan.

### Phase 3: Execute Regression Tests

**Goal**: Run tests and verify no regressions.

**Process**:

1. **Run unit tests** — automated tests for individual functions.
2. **Run integration tests** — automated tests for interactions.
3. **Run manual tests** — verify in actual game.
4. **Run smoke tests** — test core functionality.

**Output**: Test results.

### Phase 4: Analyze Results

**Goal**: Determine if regressions occurred.

**Process**:

1. **Review failures** — which tests failed?
2. **Analyze cause** — is it a regression or unrelated?
3. **Fix regressions** — address any new bugs.
4. **Re-test** — verify fixes don't introduce more regressions.

**Output**: Regression analysis and fixes.

### Phase 5: Document

**Goal**: Record regression testing results.

**Process**:

1. **Write regression report** — what was tested, what passed/failed.
2. **Update finding** — mark repair as verified or needs more work.
3. **Update knowledge base** — add insights about regression patterns.

**Output**: Complete regression documentation.

## Regression Test Matrix

Use this matrix to ensure comprehensive coverage:

| Category | Tests | Priority |
|---|---|---|
| **Core Mechanics** | Movement, combat, interaction | P0 |
| **Game State** | Save/load, state transitions, persistence | P0 |
| **UI/UX** | Menus, HUD, dialogs, input | P1 |
| **Physics** | Collision, movement, constraints | P1 |
| **Animation** | Character animations, transitions | P2 |
| **Audio** | Sound effects, music, dialogue | P2 |
| **AI/NPC** | Pathfinding, behavior, combat | P2 |
| **Performance** | FPS, memory, loading times | P1 |
| **Visual** | Rendering, materials, lighting | P2 |
| **Multiplayer** | Sync, networking, chat | P1 |

## Regression Test Examples

### Example 1: Physics Repair

**Repair**: Fixed collision detection bug.

**Regression tests**:

- [ ] Character still collides with walls.
- [ ] Objects still fall correctly.
- [ ] Projectiles still collide.
- [ ] Triggers still work.
- [ ] Performance unchanged.

### Example 2: UI Repair

**Repair**: Fixed button click handler.

**Regression tests**:

- [ ] All buttons still work.
- [ ] Menu navigation still works.
- [ ] Keyboard shortcuts still work.
- [ ] UI state still updates correctly.
- [ ] Performance unchanged.

### Example 3: Save/Load Repair

**Repair**: Fixed save corruption bug.

**Regression tests**:

- [ ] Save still works.
- [ ] Load still works.
- [ ] Save during battle still works.
- [ ] Load during cutscene still works.
- [ ] Old saves still load.

## Automated Regression Testing

### Unit Tests

```python
# Example: Python unit test
def test_health_regeneration():
    player = Player(health=50, max_health=100)
    player.regenerate_health()
    assert player.health == 55  # Assuming 5 HP regen

def test_damage_calculation():
    player = Player(health=100)
    damage = calculate_damage(attack=50, defense=20)
    assert damage == 30
```

### Integration Tests

```python
# Example: Integration test
def test_combat_flow():
    player = Player(health=100)
    enemy = Enemy(health=50)
    
    # Player attacks
    damage = player.attack(enemy)
    assert enemy.health == 50 - damage
    
    # Enemy attacks
    damage = enemy.attack(player)
    assert player.health == 100 - damage
```

### Functional Tests

```python
# Example: Functional test (game-level)
def test_level_completion():
    game = Game()
    game.start_level(1)
    
    # Complete objectives
    game.complete_objective("defeat_boss")
    game.complete_objective("collect_key")
    
    # Verify level complete
    assert game.is_level_complete()
    assert game.current_level == 2
```

## Manual Regression Testing

### Smoke Test Checklist

For every repair, run this smoke test:

- [ ] Game launches successfully.
- [ ] Main menu works.
- [ ] Can start new game.
- [ ] Can load save.
- [ ] Character moves correctly.
- [ ] Camera works correctly.
- [ ] UI responds to input.
- [ ] No crashes or errors in logs.
- [ ] Performance is acceptable.

### Regression Test Checklist

For affected areas, run specific tests:

**If physics changed:**
- [ ] Collision detection works.
- [ ] Objects fall correctly.
- [ ] Projectiles work.
- [ ] Triggers work.

**If UI changed:**
- [ ] All buttons work.
- [ ] Menus navigate correctly.
- [ ] Text displays correctly.
- [ ] Input works.

**If save/load changed:**
- [ ] Save works.
- [ ] Load works.
- [ ] Old saves load.
- [ ] No corruption.

## Regression Failure Handling

### If Regression Test Fails

1. **Don't panic** — regressions are normal.
2. **Analyze** — is it a real regression or test issue?
3. **Isolate** — what change caused the regression?
4. **Fix** — address the regression.
5. **Re-test** — verify fix doesn't cause more regressions.

### If Regression is Severe

1. **Revert** — go back to checkpoint.
2. **Re-analyze** — maybe repair approach was wrong.
3. **Try different fix** — different approach.
4. **Document** — record what went wrong.

## Regression Metrics

Track regression testing metrics:

| Metric | Target | Measurement |
|---|---|---|
| Regression rate | < 5% | Regressions per repair |
| Test coverage | > 80% | Tested code / total code |
| Test pass rate | > 95% | Passing tests / total tests |
| Time to detect | < 1 hour | Time from commit to detection |

## Regression Test Automation

### Continuous Integration

```yaml
# Example: GitHub Actions
name: Regression Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run unit tests
        run: npm test
      - name: Run integration tests
        run: npm run test:integration
      - name: Run functional tests
        run: npm run test:functional
```

### Pre-Commit Hooks

```bash
# Example: Pre-commit hook
#!/bin/bash
npm test
npm run lint
npm run build
```

## When to Stop

Stop regression testing when:

- All affected areas tested.
- All regression tests pass.
- No new regressions found.
- Time budget exhausted.
- Risk is acceptable (documented limitations).

## Integration with Other Modules

- **Intelligent repair** → `repair/intelligent-repair.md`
- **Test matrix** → `testing/gameplay-test-matrix.md`
- **Exploratory testing** → `testing/exploratory-testing.md`
- **Release validation** → `testing/release-validation.md`

# INTELLIGENT REPAIR

Safe, minimal, verified repair workflow for game defects. Every repair follows this process to ensure correctness and prevent regressions.

## Repair Philosophy

**Fix the root cause, not the symptom.** **Minimal diff, maximum confidence.** **Verify everything.**

## Repair Principles

1. **Root cause first** — understand why the bug happens before fixing.
2. **Minimal diff** — change as little code as possible.
3. **Checkpoint before touching** — create restorable checkpoint.
4. **Rebuild and replay** — verify fix works in actual game.
5. **Regression sweep** — ensure nothing else broke.
6. **Before/after evidence** — capture proof of fix.

## Repair Prioritization

Not all bugs are equal. Prioritize repairs:

| Priority | Criteria | Examples |
|---|---|---|
| P0 | Game-breaking, data loss, security | Crash on launch, save corruption, RCE |
| P1 | Major gameplay impact, progression blocked | Soft-lock, major visual corruption, severe perf |
| P2 | Significant but not blocking | Noticeable bugs, edge-case failures, minor perf |
| P3 | Minor issues, cosmetic | Small visual glitches, rare edge cases |
| P4 | Polish, nice-to-have | Documentation gaps, theoretical issues |

**Repair order**: P0 → P1 → P2 → P3 → P4.

**Exception**: If P0 fix is risky/complex, may defer to P1 if workaround exists. Document decision.

## Safe Repair Workflow

### Phase 1: Inspect

**Goal**: Understand the bug and its context before touching anything.

**Process**:

1. **Read the finding** — review bug report, evidence, reproduction steps.
2. **Read the code** — understand the relevant code sections.
3. **Check dependencies** — what does this code depend on?
4. **Check history** — git log, recent changes, related bugs.
5. **Assess risk** — how risky is this repair?

**Output**: Understanding of bug context and repair approach.

**Questions to answer**:
- What files need to change?
- What is the blast radius of this change?
- Are there dependencies or side effects?
- Is this a hotfix or a proper fix?
- Can this be tested in isolation?

### Phase 2: Git Status & Checkpoint

**Goal**: Ensure clean state and create restorable checkpoint.

**Process**:

1. **Check git status** — ensure working tree is clean or understand changes.
2. **Create branch** — `git checkout -b fix/PLAB-NNNN-description`.
3. **Commit current state** — if uncommitted changes exist, commit or stash.
4. **Tag checkpoint** — `git tag checkpoint/before-PLAB-NNNN`.

**Output**: Clean working state with restorable checkpoint.

**Checkpoint types**:

- **Git branch** — preferred for code changes.
- **Git tag** — marks specific commit for rollback.
- **File backup** — copy files before modification.
- **Snapshot** — VM/container snapshot for major changes.

**Never skip this step.** No checkpoint = no repair.

### Phase 3: Minimal Change

**Goal**: Implement the smallest possible fix for the root cause.

**Process**:

1. **Design fix** — how to correct the root cause with minimal change.
2. **Implement fix** — make the change.
3. **Review diff** — ensure change is minimal and correct.
4. **Check style** — match existing code style.

**Output**: Minimal code change that fixes root cause.

**Minimal change principles**:

- **One concern per change** — don't fix multiple bugs at once.
- **No refactoring** — don't "improve" unrelated code.
- **No formatting** — don't reformat unrelated code.
- **No renaming** — don't rename variables/functions unless necessary.
- **Comment only if needed** — explain why, not what.

**Example of good minimal change**:

```diff
- if (health <= 0) {
+ if (health < 0) {
    die();
  }
```

**Example of bad change (too much)**:

```diff
- function update() {
-   if (health <= 0) {
-     die();
-   }
-   // ... 100 lines of unrelated changes ...
- }
+ function updateHealth() {
+   // completely rewritten function
+ }
```

### Phase 4: Format & Lint

**Goal**: Ensure code style consistency.

**Process**:

1. **Run formatter** — apply project code style.
2. **Run linter** — check for style/syntax issues.
3. **Fix issues** — address any linting errors.
4. **Verify** — ensure formatting didn't break anything.

**Output**: Properly formatted code.

**Tools by platform**:

| Platform | Formatter | Linter |
|---|---|---|
| JavaScript/TypeScript | Prettier | ESLint |
| Python | Black | Flake8, Pylint |
| C# | dotnet-format | StyleCop |
| C++ | clang-format | clang-tidy |
| GDScript | gdformat | gdtoolkit |
| Lua | stylua | luacheck |

### Phase 5: Test

**Goal**: Verify fix works in isolation before full integration.

**Process**:

1. **Unit test** — test the specific function/component.
2. **Integration test** — test the interaction.
3. **Manual test** — verify in actual game.
4. **Edge case test** — test boundary conditions.

**Output**: Test results confirming fix works.

**Test types**:

- **Unit test** — test individual function in isolation.
- **Integration test** — test how components interact.
- **Manual test** — verify in actual game environment.
- **Regression test** — ensure related functionality still works.

### Phase 6: Rebuild

**Goal**: Build the game with the fix.

**Process**:

1. **Clean build** — remove old build artifacts.
2. **Build** — compile/package the game.
3. **Verify build** — check for build errors/warnings.
4. **Test build** — launch and verify it runs.

**Output**: Fresh build with fix included.

**Build commands by platform**:

| Platform | Build Command |
|---|---|
| Three.js/Web | `npm run build` / `vite build` |
| Unity | `Unity.exe -batchmode -buildWindows64Player` |
| Unreal | `UnrealBuildTool.exe -project=... -target=...` |
| Godot | `godot --headless --export-release` |
| RPG Maker | `nw.exe .` or export via RPG Maker editor |
| Generic | Project-specific build system |

### Phase 7: Relaunch

**Goal**: Launch the rebuilt game and verify it starts correctly.

**Process**:

1. **Launch game** — start the game.
2. **Verify launch** — confirm no crashes, reaches playable state.
3. **Check logs** — review console/logs for errors.
4. **Baseline check** — confirm baseline functionality works.

**Output**: Game running with fix.

**Launch verification**:

- Game reaches menu/main screen.
- No crashes or errors in logs.
- Basic functionality works (movement, UI).
- Performance is acceptable.

### Phase 8: Replay

**Goal**: Re-run the original bug reproduction to confirm fix.

**Process**:

1. **Run repro steps** — follow exact reproduction steps.
2. **Observe result** — verify bug no longer occurs.
3. **Check edge cases** — test boundary conditions.
4. **Document result** — record before/after evidence.

**Output**: Confirmation that bug is fixed.

**Replay checklist**:

- [ ] Original reproduction steps no longer trigger bug.
- [ ] Edge cases handled correctly.
- [ ] No new bugs introduced.
- [ ] Performance unchanged or improved.

### Phase 9: Regression

**Goal**: Ensure fix didn't break anything else.

**Process**:

1. **Run regression tests** — test related functionality.
2. **Run smoke tests** — test core game loop.
3. **Run audit subset** — re-run relevant audit dimensions.
4. **Compare to baseline** — ensure no new findings.

**Output**: Confirmation that no regressions introduced.

**Regression scope**:

- **Direct dependencies** — code that calls the fixed code.
- **Related systems** — systems that interact with fixed code.
- **Core functionality** — ensure game still works end-to-end.
- **Performance** — ensure no performance regression.

### Phase 10: Before/After Compare

**Goal**: Document the fix with evidence.

**Process**:

1. **Capture before** — screenshot/log of bug before fix.
2. **Capture after** — screenshot/log of fix after.
3. **Write repair report** — use `templates/repair-report.md`.
4. **Update finding** — mark finding as repaired/verified.
5. **Update knowledge base** — add insight to `.plab/knowledge-base.md`.

**Output**: Complete repair documentation.

**Before/after evidence should include**:

- Screenshot of bug before fix.
- Screenshot of fixed behavior after.
- Log comparison (before/after).
- Performance metrics (before/after).
- Code diff.

## Repair Report Template

Use `templates/repair-report.md` for each repair. Include:

- Finding ID (PLAB-NNNN).
- Root cause analysis summary.
- Files changed.
- Code diff.
- Verification steps and results.
- Regression test results.
- Before/after evidence.
- Lessons learned.

## Repair Safety Rules

### Never Do

- ❌ Fix without understanding root cause.
- ❌ Make changes without checkpoint.
- ❌ Fix multiple bugs in one commit.
- ❌ Refactor unrelated code.
- ❌ Skip testing.
- ❌ Skip regression testing.
- ❌ Claim fix without verification.
- ❌ Delete code without understanding why it exists.

### Always Do

- ✅ Understand root cause before fixing.
- ✅ Create checkpoint before changes.
- ✅ Make minimal changes.
- ✅ Test fix in isolation.
- ✅ Run regression tests.
- ✅ Document everything.
- ✅ Verify fix works end-to-end.

## When Repair Fails

If repair doesn't work:

1. **Don't panic** — revert to checkpoint.
2. **Re-analyze** — maybe root cause was wrong.
3. **Try different approach** — different fix strategy.
4. **Escalate** — if stuck, document and move to next bug.
5. **Never force** — don't push broken fix.

## When to Stop

Stop repair process when:

- All P0/P1 findings repaired and verified.
- All P2 findings repaired or documented as deferred.
- Time budget exhausted.
- Risk exceeds benefit (fix is too risky).
- Platform limits prevent repair (binary-only, no source).

## Integration with Other Modules

- **Root cause analysis** → `repair/root-cause-analysis.md`
- **Regression testing** → `repair/regression-testing.md`
- **Repair safety** → `repair/repair-safety.md`
- **Test matrix** → `testing/gameplay-test-matrix.md`
- **Bug report template** → `templates/bug-report.md`
- **Repair report template** → `templates/repair-report.md`

# RELEASE VALIDATION

Quality gates and final release audit process. Determines whether a game is ready for release.

## Philosophy

**Release is a decision, not a default.** A game is not ready until it passes all quality gates. The final audit report provides the verdict.

## Quality Gates A–F

### Gate A: LAUNCH

**Pass condition**: Game launches to interactive state, no crash in first 60 seconds.

**Tests**:

- [ ] Game executable launches without errors.
- [ ] Game reaches main menu or playable state.
- [ ] No crashes in first 60 seconds.
- [ ] No critical errors in logs.
- [ ] Performance is acceptable (FPS > 30).

**Evidence**: Launch log, screenshot, FPS measurement.

**Fail action**: Fix launch issues before proceeding.

### Gate B: CORE LOOP

**Pass condition**: Primary mechanic works end-to-end at least once.

**Tests**:

- [ ] Player can move.
- [ ] Player can interact with world.
- [ ] Core mechanic works (combat, puzzle, etc.).
- [ ] Progression works (level up, quest complete).
- [ ] Win/lose conditions work.

**Evidence**: Video of core loop, state verification.

**Fail action**: Fix core mechanics before proceeding.

### Gate C: COVERAGE

**Pass condition**: Every declared subsystem audited or explicitly marked UNREACHABLE with reason.

**Tests**:

- [ ] All audit dimensions covered (functional, visual, physics, etc.).
- [ ] All test matrix categories covered.
- [ ] All blind spot categories probed.
- [ ] All P0/P1 findings documented.
- [ ] Unreachable areas documented with reason.

**Evidence**: Audit coverage report, test matrix results.

**Fail action**: Complete missing audits before proceeding.

### Gate D: FINDINGS

**Pass condition**: Every P0/P1 finding has a repair or a documented waiver with owner sign-off.

**Tests**:

- [ ] All P0 findings repaired and verified.
- [ ] All P1 findings repaired and verified.
- [ ] P2 findings repaired or documented as deferred.
- [ ] P3/P4 findings documented.
- [ ] All repairs verified with regression tests.

**Evidence**: Findings index, repair reports, verification results.

**Fail action**: Repair or waive P0/P1 findings before proceeding.

### Gate E: REGRESSION

**Pass condition**: Re-run of repaired build shows no new findings vs. baseline.

**Tests**:

- [ ] Re-run test matrix on repaired build.
- [ ] Compare findings to baseline.
- [ ] No new P0/P1 findings.
- [ ] No performance regression.
- [ ] No stability regression.

**Evidence**: Regression test results, comparison report.

**Fail action**: Fix regressions before proceeding.

### Gate F: EVIDENCE

**Pass condition**: Final report contains reproducible evidence for every claim.

**Tests**:

- [ ] Every finding has evidence (screenshots, logs, videos).
- [ ] Every repair has before/after evidence.
- [ ] Every test has recorded results.
- [ ] All evidence is reproducible.
- [ ] Final report is complete and accurate.

**Evidence**: Final audit report, evidence directory.

**Fail action**: Complete missing evidence before proceeding.

## Release Decision Process

### Step 1: Run All Gates

Execute all gates A–F in order. Each gate must pass before proceeding to the next.

### Step 2: Collect Results

Record results for each gate:

| Gate | Status | Evidence | Notes |
|---|---|---|---|
| A: LAUNCH | ✅/❌ | Launch log, screenshot | |
| B: CORE LOOP | ✅/❌ | Video, state | |
| C: COVERAGE | ✅/❌ | Coverage report | |
| D: FINDINGS | ✅/❌ | Findings index | |
| E: REGRESSION | ✅/❌ | Regression results | |
| F: EVIDENCE | ✅/❌ | Final report | |

### Step 3: Determine Verdict

Based on gate results:

| Verdict | Condition |
|---|---|
| **BOSS VERIFIED** | All gates pass, no outstanding issues |
| **BOSS VERIFIED—WITH LIMITATIONS** | All gates pass, but documented limitations exist |
| **NEEDS MORE WORK** | One or more gates fail, fixable issues remain |
| **BLOCKED** | Cannot proceed due to external factors (platform, authorization, resources) |

### Step 4: Write Final Report

Use `templates/final-audit-report.md` to write comprehensive report.

## Final Audit Report Template

See `templates/final-audit-report.md` for complete template. Sections:

- **A. Executive Summary** — verdict, key findings, recommendations.
- **B. Game Profile** — game identity, engine, platform.
- **C. Audit Coverage** — what was tested, what wasn't.
- **D. Findings Summary** — all findings by severity.
- **E. Repairs Summary** — all repairs by category.
- **F. Quality Gates** — gate results and evidence.
- **G. Recommendations** — next steps, known issues, limitations.

## Release Readiness Checklist

Before declaring release ready:

### Technical Readiness

- [ ] All P0 bugs fixed.
- [ ] All P1 bugs fixed or documented.
- [ ] Performance meets targets.
- [ ] Stability verified (no crashes in extended testing).
- [ ] Save/load works correctly.
- [ ] All platforms tested.

### Content Readiness

- [ ] All content complete.
- [ ] All quests/levels functional.
- [ ] All items/abilities working.
- [ ] All NPCs/enemies functional.
- [ ] All cutscenes play correctly.

### Polish Readiness

- [ ] UI/UX polished.
- [ ] Visual quality acceptable.
- [ ] Audio quality acceptable.
- [ ] Performance optimized.
- [ ] Documentation complete.

### Legal/Compliance

- [ ] All licenses valid.
- [ ] All assets properly credited.
- [ ] Privacy policy in place.
- [ ] Terms of service in place.
- [ ] Age ratings appropriate.

## Common Release Blockers

### Critical Blockers (Must Fix)

- [ ] Crash on launch.
- [ ] Save corruption.
- [ ] Progression blocked.
- [ ] Major visual corruption.
- [ ] Security vulnerability.
- [ ] Performance unplayable (< 20 FPS).

### Major Blockers (Should Fix)

- [ ] Frequent crashes.
- [ ] Major bugs in core mechanics.
- [ ] Significant performance issues.
- [ ] Missing critical content.
- [ ] Broken multiplayer.

### Minor Blockers (Can Defer)

- [ ] Minor visual glitches.
- [ ] Edge case bugs.
- [ ] Performance optimizations.
- [ ] Polish items.

## Release Risk Assessment

| Risk Level | Criteria | Action |
|---|---|---|
| **Low** | All gates pass, no critical issues | Release with confidence |
| **Medium** | All gates pass, minor issues remain | Release with monitoring |
| **High** | Some gates fail, fixable issues | Delay release, fix issues |
| **Critical** | Multiple gates fail, major issues | Do not release, major rework needed |

## Post-Release Monitoring

After release:

1. **Monitor crashes** — track crash reports.
2. **Monitor performance** — track FPS, memory usage.
3. **Monitor feedback** — player reports, reviews.
4. **Hotfix critical issues** — address P0/P1 quickly.
5. **Plan updates** — schedule patches and updates.

## When to Stop

Stop release validation when:

- All gates evaluated.
- Verdict determined.
- Final report written.
- Recommendations documented.
- Time budget exhausted.

## Integration with Other Modules

- **Quality gates** → This document.
- **Test matrix** → `testing/gameplay-test-matrix.md`.
- **Final report** → `templates/final-audit-report.md`.
- **Repair safety** → `repair/repair-safety.md`.

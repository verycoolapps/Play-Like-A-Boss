# ROOT CAUSE ANALYSIS

The 10-step diagnostic methodology for identifying the actual cause of a defect, not just the symptom.

## Philosophy

**Fix the cause, not the symptom.** A repair that hides a bug is a failure. The goal is to understand why the bug happens, not just that it happens.

## The 10 Steps

### Step 1: Reproduce

**Goal**: Confirm the bug exists and can be triggered reliably.

**Process**:

1. **Document the bug** — what happens, when, under what conditions.
2. **Create minimal repro** — reduce to simplest possible trigger.
3. **Verify reproducibility** — run multiple times, confirm consistent.
4. **Isolate variables** — identify which factors are required.

**Output**: Reproduction steps that reliably trigger the bug.

**Questions to answer**:
- Can you reproduce it 100% of the time?
- What is the minimum set of conditions needed?
- Does it happen on fresh install or only after certain actions?
- Is it timing-dependent or state-dependent?

### Step 2: Observe

**Goal**: Gather as much data as possible about the bug.

**Process**:

1. **Capture state** — screenshot, logs, memory, metrics.
2. **Trace execution** — follow code path, function calls.
3. **Monitor resources** — CPU, memory, GPU, network.
4. **Check dependencies** — what does this code depend on?

**Output**: Comprehensive observation data.

**Tools by platform**:

| Platform | Tools |
|---|---|
| Three.js | `renderer.info`, console logs, Chrome DevTools |
| Unity | Profiler, Debug.Log, Visual Studio debugger |
| Unreal | Unreal Insights, UE_LOG, Visual Studio debugger |
| Godot | Godot debugger, print statements, profiler |
| Generic | OS tools, log files, debugger |

### Step 3: Hypothesize

**Goal**: Form theories about what might be causing the bug.

**Process**:

1. **List possible causes** — brainstorm all plausible explanations.
2. **Prioritize** — rank by likelihood and ease of testing.
3. **Design experiments** — how to test each hypothesis.
4. **Select top hypothesis** — start with most likely.

**Output**: Ranked list of hypotheses with test plans.

**Common cause categories**:

- **Logic error** — wrong condition, off-by-one, inverted logic.
- **State error** — corrupted state, stale data, race condition.
- **Timing error** — frame dependency, async issue, race condition.
- **Resource error** — memory leak, null reference, missing asset.
- **Configuration error** — wrong setting, missing dependency.
- **External error** — platform bug, driver issue, hardware limitation.

### Step 4: Test Hypothesis

**Goal**: Confirm or eliminate the current hypothesis.

**Process**:

1. **Design experiment** — minimal change to test hypothesis.
2. **Execute experiment** — apply change, run repro.
3. **Observe result** — did bug change?
4. **Conclude** — hypothesis confirmed, eliminated, or inconclusive.

**Output**: Confirmed or eliminated hypothesis.

**Experiment design principles**:

- **Minimal change** — change one variable at a time.
- **Reversible** — can undo change easily.
- **Measurable** — clear pass/fail criteria.
- **Isolated** — don't introduce new variables.

### Step 5: Isolate

**Goal**: Narrow down to the exact location and cause.

**Process**:

1. **Binary search** — divide code/data in half, test each half.
2. **Add logging** — instrument code to trace execution.
3. **Break points** — set breakpoints at key locations.
4. **Minimize repro** — reduce to smallest possible case.

**Output**: Exact location of root cause.

**Isolation techniques**:

- **Code isolation** — comment out sections, test each part.
- **Data isolation** — test with minimal data set.
- **Time isolation** — test at specific times, frame counts.
- **State isolation** — test with clean state vs corrupted.

### Step 6: Identify

**Goal**: Determine the exact root cause.

**Process**:

1. **Analyze evidence** — review all gathered data.
2. **Trace causality** — follow chain of events to root.
3. **Identify mechanism** — how does the bug actually happen?
4. **Confirm root cause** — verify this is the actual cause, not a symptom.

**Output**: Precise description of root cause.

**Root cause questions**:

- What is the exact line of code or configuration?
- What value or state causes the failure?
- What assumption is violated?
- Why wasn't this caught earlier?

### Step 7: Fix

**Goal**: Implement a minimal, correct fix.

**Process**:

1. **Design fix** — how to correct the root cause.
2. **Implement fix** — make the minimal change.
3. **Verify fix** — run repro, confirm bug gone.
4. **Check side effects** — ensure no new bugs introduced.

**Output**: Working fix with minimal diff.

**Fix principles**:

- **Minimal diff** — change as little as possible.
- **Root cause** — fix the cause, not the symptom.
- **No workarounds** — don't hide the bug, fix it.
- **No refactoring** — don't change unrelated code.
- **Testable** — fix should be verifiable.

### Step 8: Verify

**Goal**: Confirm the fix works and doesn't break anything else.

**Process**:

1. **Run repro** — confirm original bug is gone.
2. **Run regression** — test related functionality.
3. **Check edge cases** — test boundary conditions.
4. **Performance check** — ensure no performance regression.

**Output**: Verification that fix is correct and complete.

**Verification checklist**:

- [ ] Original bug no longer reproduces.
- [ ] Related functionality still works.
- [ ] Edge cases handled correctly.
- [ ] No performance regression.
- [ ] No new bugs introduced.

### Step 9: Document

**Goal**: Record the bug, root cause, and fix for future reference.

**Process**:

1. **Write bug report** — use `templates/bug-report.md`.
2. **Document root cause** — explain why bug happened.
3. **Document fix** — explain what was changed and why.
4. **Link evidence** — reference screenshots, logs, commits.
5. **Update knowledge base** — add insight to `.plab/knowledge-base.md`.

**Output**: Complete bug report and documentation.

**Documentation should include**:

- Bug description and reproduction steps.
- Root cause analysis (10-step process).
- Fix description and code changes.
- Verification results.
- Lessons learned.

### Step 10: Prevent

**Goal**: Prevent similar bugs in the future.

**Process**:

1. **Identify pattern** — what type of bug was this?
2. **Add test** — create test that would catch this bug.
3. **Update guidelines** — add to coding standards or review checklist.
4. **Share knowledge** — document in team wiki or knowledge base.

**Output**: Prevention measures implemented.

**Prevention strategies**:

- **Unit tests** — test the specific case that failed.
- **Integration tests** — test the interaction that failed.
- **Code review** — add checklist item for this bug type.
- **Static analysis** — add lint rule or analyzer.
- **Documentation** — update coding guidelines.

## Root Cause Categories

### Logic Errors

**Symptoms**: Wrong behavior, incorrect results, unexpected outcomes.

**Common causes**:

- Off-by-one errors (loop bounds, array indices).
- Inverted conditions (if/else swapped).
- Wrong operator (== vs ===, && vs ||).
- Incorrect algorithm (wrong formula, wrong approach).
- Missing edge case handling.

**Detection**: Trace logic, add assertions, test edge cases.

### State Errors

**Symptoms**: Corrupted data, stale state, inconsistent behavior.

**Common causes**:

- Race conditions (concurrent access).
- Stale references (object deleted but still referenced).
- Missing state updates (state not updated when should be).
- Incorrect state transitions (wrong state machine path).
- Serialization errors (save/load corruption).

**Detection**: State inspection, logging, invariant checks.

### Timing Errors

**Symptoms**: Intermittent bugs, frame-dependent behavior, race conditions.

**Common causes**:

- Frame dependency (behavior varies with FPS).
- Async issues (callback timing, promise resolution).
- Race conditions (concurrent operations).
- Timer errors (wrong interval, timer not cleared).
- Animation timing (animation not synced with logic).

**Detection**: Timing analysis, frame-by-frame inspection, stress testing.

### Resource Errors

**Symptoms**: Crashes, memory issues, missing assets.

**Common causes**:

- Null references (accessing null object).
- Memory leaks (objects not freed).
- Missing assets (file not found, wrong path).
- Resource exhaustion (out of memory, too many objects).
- File permission issues (can't read/write).

**Detection**: Memory profiling, null checks, file existence checks.

### Configuration Errors

**Symptoms**: Works in dev, fails in production, environment-specific bugs.

**Common causes**:

- Wrong configuration value.
- Missing environment variable.
- Wrong build settings.
- Dependency version mismatch.
- Platform-specific differences.

**Detection**: Configuration audit, environment comparison.

### External Errors

**Symptoms**: Works on one machine, fails on another, intermittent failures.

**Common causes**:

- Driver bugs (GPU, audio, network).
- OS bugs (Windows, macOS, Linux).
- Hardware issues (failing RAM, overheating).
- Network issues (latency, packet loss).
- Third-party library bugs.

**Detection**: Environment testing, hardware diagnostics, library updates.

## Root Cause Analysis Template

Use this template for each bug:

```markdown
# Root Cause Analysis: PLAB-NNNN

## Bug Description
[What happens, when, under what conditions]

## Reproduction Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Observation
[What was observed: logs, screenshots, state]

## Hypotheses
1. [Hypothesis 1] - [Likelihood] - [Test plan]
2. [Hypothesis 2] - [Likelihood] - [Test plan]
3. [Hypothesis 3] - [Likelihood] - [Test plan]

## Investigation
[What was tested, what was found]

## Root Cause
[Exact cause: file, line, mechanism]

## Fix
[What was changed, why]

## Verification
[How fix was verified]

## Prevention
[How to prevent similar bugs]
```

## When to Stop

Stop root cause analysis when:

- Root cause is identified and confirmed.
- Fix is implemented and verified.
- Documentation is complete.
- Prevention measures are in place.
- Time budget exhausted (document remaining investigation).

## Integration with Repair

Root cause analysis feeds directly into repair:

1. **RCA identifies root cause** → repair fixes root cause.
2. **RCA documents evidence** → repair report references RCA.
3. **RCA suggests prevention** → repair includes prevention measures.

Never skip RCA. Never fix symptoms. Always find the root cause.

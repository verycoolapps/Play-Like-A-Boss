# DECISION ENGINE

The OBSERVE → UNDERSTAND → PLAN → ACT → VERIFY → LEARN → REPEAT loop that governs every action in the pipeline.

## The Loop

```
┌─────────┐   ┌────────────┐   ┌─────────┐   ┌─────┐   ┌────────┐   ┌───────┐
│ OBSERVE │ → │ UNDERSTAND │ → │  PLAN   │ → │ ACT │ → │ VERIFY │ → │ LEARN │
└─────────┘   └────────────┘   └─────────┘   └─────┘   └────────┘   └───────┘
     ↑                                                              │
     └────────────────────────── REPEAT ────────────────────────────┘
```

Each phase has specific inputs, processes, and outputs. Skipping a phase is how bugs slip through.

## OBSERVE

**Goal**: Capture the current state of the game and environment.

**Inputs**: None (this is the start).

**Process**:

1. **Screen capture** — screenshot or frame grab.
2. **Log capture** — console output, error logs, debug output.
3. **Metric capture** — FPS, memory, draw calls, physics state.
4. **Input state** — what keys/buttons are pressed, cursor position.
5. **Game state** — variables, scene graph, object positions (if accessible).

**Outputs**:

- `observation` object with timestamp, state snapshot, metrics, anomalies.
- Appended to `observations.jsonl`.

**Frequency**: Every action cycle, or every N seconds during idle observation.

**Tools by platform**:

| Platform | Screen | Logs | Metrics | State |
|---|---|---|---|---|
| Three.js | `canvas.toDataURL()` or Playwright screenshot | `console.log` capture | `renderer.info`, `performance.memory` | `scene`, `camera`, objects |
| Unity | Screenshot or Unity Profiler | `Debug.Log` capture | Unity Profiler, `Time.deltaTime` | `GameObject` hierarchy |
| Unreal | Screenshot or Unreal Insights | `UE_LOG` capture | Unreal Insights, `FPlatformTime` | `UObject` reflection |
| Godot | Screenshot or Godot debugger | `print()` capture | Godot profiler, `Performance` | `SceneTree`, nodes |
| Generic | OS screenshot | Log files, stderr | OS tools, process stats | Limited |

## UNDERSTAND

**Goal**: Compare observed state to expected state.

**Inputs**: Current observation, game profile, last known good state, objective stack.

**Process**:

1. **Load context** — game profile, current objectives, recent history.
2. **Compare** — observed vs expected state.
3. **Classify** — is this normal, anomalous, or a bug?
4. **Prioritize** — does this need immediate action or can it wait?

**Outputs**:

- `understanding` object with:
  - `expected_state` — what should be happening
  - `observed_state` — what is happening
  - `delta` — the difference
  - `classification` — `normal` | `anomalous` | `bug` | `unknown`
  - `priority` — `immediate` | `high` | `medium` | `low`
  - `recommended_action` — what to do next

**Decision rules**:

- If `observed == expected` → continue to PLAN with next objective.
- If `observed != expected` but explainable → log anomaly, continue.
- If `observed != expected` and unexplained → classify as potential bug, escalate to audit.
- If state is ambiguous → gather more observations before deciding.

## PLAN

**Goal**: Choose the next action.

**Inputs**: Understanding, current objectives, available actions, resource constraints.

**Process**:

1. **Load objectives** — what are we trying to achieve?
2. **Evaluate options** — what actions are available?
3. **Score options** — which action best advances objectives or investigates anomalies?
4. **Select** — choose the highest-scoring action.
5. **Validate** — is this action safe? Does it have side effects?

**Outputs**:

- `plan` object with:
  - `action` — what to do
  - `target` — what/where to act on
  - `parameters` — input details, timing, duration
  - `expected_result` — what should happen
  - `risk` — potential side effects
  - `timeout` — max time to wait for result

**Action types**:

| Type | Examples | Risk |
|---|---|---|
| Navigation | Move, jump, walk, drive | Low |
| Interaction | Click, press button, talk, pickup | Low |
| Combat | Attack, dodge, cast spell | Medium |
| UI | Menu navigation, inventory, settings | Low |
| System | Save, load, quit, restart | High |
| Audit | Probe edge case, stress test, boundary push | Medium |
| Repair | Edit code, rebuild, redeploy | High |

## ACT

**Goal**: Execute the planned action.

**Inputs**: Plan object.

**Process**:

1. **Prepare** — set up input simulation, position camera/cursor, wait for readiness.
2. **Execute** — send input via deepest available adapter.
3. **Monitor** — watch for immediate feedback (visual, audio, state change).
4. **Wait** — allow time for action to complete.
5. **Capture** — record result for verification.

**Outputs**:

- `action_result` object with:
  - `executed` — did the input send successfully?
  - `immediate_feedback` — any instant response
  - `completion_time` — how long it took
  - `errors` — any errors during execution

**Execution methods**:

| Method | Use when | Reliability |
|---|---|---|
| Native API | Engine exposes input/state API | High |
| Browser automation | Web game, Playwright/CDP | High |
| GUI automation | Desktop game, pyautogui/xdotool | Medium |
| Input injection | Any game, keyboard/mouse/controller | Medium |
| Human-assisted | Automation blocked, manual fallback | High (human) |

## VERIFY

**Goal**: Confirm the action produced the expected result.

**Inputs**: Action result, expected result, current observation.

**Process**:

1. **Observe** — capture new state after action.
2. **Compare** — observed result vs expected result.
3. **Classify** — success, partial success, failure, or unexpected.
4. **Decide** — retry, escalate, or move on.

**Outputs**:

- `verification` object with:
  - `expected` — what should have happened
  - `observed` — what actually happened
  - `match` — boolean or partial match
  - `confidence` — how sure we are
  - `next_step` — retry | escalate | continue | investigate

**Verification methods**:

- **State comparison** — did variables change as expected?
- **Visual verification** — did the screen change correctly?
- **Behavioral verification** — did the game respond appropriately?
- **Metric verification** — did performance stay within bounds?

**Retry logic**:

- If `match == false` and `retry_count < max_retries` → retry with adjusted parameters.
- If `match == false` and `retry_count >= max_retries` → escalate to investigation.
- If `match == partial` → log anomaly, continue with caution.

## LEARN

**Goal**: Record what happened for future reference.

**Inputs**: Verification result, any anomalies, any findings.

**Process**:

1. **Summarize** — what did we learn this cycle?
2. **Categorize** — is this a pattern, a one-off, or a new insight?
3. **Store** — write to observations, findings, or knowledge base.
4. **Index** — update indexes for retrieval.

**Outputs**:

- Appended to `observations.jsonl`.
- Updated `knowledge-base.md` if significant.
- New finding if bug discovered.
- Updated repair if fix applied.

**What to learn**:

- **Successful patterns** — actions that work reliably.
- **Failure patterns** — actions that fail consistently.
- **Timing insights** — optimal delays, reaction times.
- **State transitions** — how the game moves between states.
- **Edge cases** — unexpected behaviors discovered.

## REPEAT

**Goal**: Continue the loop until exit condition is met.

**Inputs**: Current state, objectives, exit conditions.

**Process**:

1. **Check exit** — have we met the mode's exit condition?
2. **Check progress** — are we making progress or stuck?
3. **Check time** — are we within time budget?
4. **Decide** — continue, pause, or terminate.

**Outputs**:

- `loop_decision` object with:
  - `continue` — boolean
  - `reason` — why continue or stop
  - `next_phase` — which phase to enter next
  - `adjustments` — any changes to strategy

**Exit conditions by mode**:

| Mode | Exit condition |
|---|---|
| QUICK SCAN | Smoke test complete, no P0/P1 found |
| FULL GAME AUDIT | All audit dimensions complete |
| PLAY START→FINISH | Game reached end state or all areas explored |
| DEEP BLIND SPOT HUNT | All 7 blind-spot categories probed |
| FIX EVERYTHING | All P0/P1 repaired and verified |
| PERFORMANCE BEAST | Performance targets met or documented |
| REGRESSION GUARD | Baseline comparison complete |
| FINAL RELEASE AUDIT | All gates A–F pass |
| CONTINUOUS GAME QA | User stops or time budget exhausted |
| BOSS MODE | All 18 phases complete, final report written |

## Stuck Detection

The loop can get stuck. Detect and recover:

### Stuck Types

| Type | Signature | Detection | Recovery |
|---|---|---|---|
| No progress | Same state for >N cycles | State hash unchanged | Change strategy, try different action |
| Repeated failure | Same action fails >N times | Failure count exceeds threshold | Escalate to investigation, try alternative |
| Infinite loop | Cycle repeats without progress | Loop detection algorithm | Break pattern, force state change |
| Resource exhaustion | Can't afford required action | Resource check fails | Find alternative, exploit, or skip |
| External block | Game requires human/external input | Timeout waiting for response | Human-assisted fallback |

### Stuck Recovery Protocol

1. **Detect** — identify stuck type and duration.
2. **Capture** — save state, logs, screenshots.
3. **Classify** — which stuck type?
4. **Attempt recovery** — try alternative action, reload, or escalate.
5. **Document** — if unrecoverable, record as finding and move on.

## Adaptive Behavior

The loop adapts based on context:

- **Fast mode** — skip verification for low-risk actions, batch observations.
- **Careful mode** — verify every action, slow down for complex sequences.
- **Exploration mode** — prioritize breadth, try new things, accept failures.
- **Regression mode** — prioritize known paths, verify against baseline.
- **Repair mode** — focus on failing areas, iterate until fixed.

Adjust mode based on:

- Current phase (audit vs play vs repair).
- Recent success rate.
- Time remaining.
- User priorities.

## Decision Logging

Every decision cycle is logged for auditability:

```json
{
  "timestamp": "2026-10-13T14:31:00Z",
  "cycle": 142,
  "observe": {"fps": 60, "state": "gameplay", "anomalies": []},
  "understand": {"classification": "normal", "priority": "low"},
  "plan": {"action": "move_forward", "target": "enemy_01", "risk": "low"},
  "act": {"executed": true, "feedback": "character_moved"},
  "verify": {"match": true, "confidence": 0.95},
  "learn": {"insight": "enemy_01 aggros at 5m range"},
  "decision": {"continue": true, "next": "combat"}
}
```

This log enables:

- Reproducibility — replay exact action sequences.
- Debugging — trace why a decision was made.
- Learning — identify patterns across sessions.
- Accountability — prove what was tried and what happened.

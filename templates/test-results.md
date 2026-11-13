# TEST RESULTS TEMPLATE

Use this template for recording test execution results.

## Test Session

| Field | Value |
|---|---|
| **Session ID** | [YYYYMMDD-HHMMSS] |
| **Test Type** | [Unit / Integration / Functional / Regression / Exploratory] |
| **Tester** | [Name/Agent] |
| **Date** | [Date] |
| **Duration** | [Duration] |
| **Environment** | [Platform, OS, Hardware] |

## Test Summary

| Metric | Value |
|---|---|
| **Total Tests** | [Count] |
| **Passed** | [Count] |
| **Failed** | [Count] |
| **Blocked** | [Count] |
| **Skipped** | [Count] |
| **Pass Rate** | [%] |

## Test Results

### By Category

| Category | Total | Passed | Failed | Blocked | Skipped | Pass Rate |
|---|---|---|---|---|---|---|
| [Category 1] | [Count] | [Count] | [Count] | [Count] | [Count] | [%] |
| [Category 2] | [Count] | [Count] | [Count] | [Count] | [Count] | [%] |
| [Category 3] | [Count] | [Count] | [Count] | [Count] | [Count] | [%] |

### Detailed Results

| Test ID | Test Name | Category | Status | Duration | Notes |
|---|---|---|---|---|---|
| [ID] | [Name] | [Category] | ✅/❌/⚠️/🚫/⏭️ | [Time] | [Notes] |
| [ID] | [Name] | [Category] | ✅/❌/⚠️/🚫/⏭️ | [Time] | [Notes] |

## Failures

### Failure Details

| Test ID | Test Name | Failure Reason | Severity | Finding ID |
|---|---|---|---|---|
| [ID] | [Name] | [Reason] | [P0-P4] | [PLAB-NNNN] |

### Failure Analysis

[Describe patterns or common causes of failures.]

## Blocked Tests

| Test ID | Test Name | Block Reason | Unblock Action |
|---|---|---|---|
| [ID] | [Name] | [Reason] | [What needs to happen] |

## Evidence

### Screenshots

- [Screenshot: description](path/to/screenshot.png)

### Videos

- [Video: description](path/to/video.mp4)

### Logs

- [Log: description](path/to/log.txt)

### Metrics

- [Metric: value](path/to/metrics.txt)

## Findings

| Finding ID | Severity | Category | Description | Status |
|---|---|---|---|---|
| PLAB-NNNN | [P0-P4] | [Category] | [Description] | [Status] |

## Recommendations

[Recommendations based on test results. What should be fixed, improved, or investigated further?]

## Next Steps

[What should happen next? Re-test, fix bugs, run more tests?]

---

**Template Version**: 1.0
**Last Updated**: 2026-10-13

# REPAIR REPORT TEMPLATE

Use this template for every repair performed during the FIX EVERYTHING or BOSS MODE pipeline.

## Repair ID

**PLAB-REPAIR-NNNN** (linked to finding PLAB-NNNN)

## Finding Reference

| Field | Value |
|---|---|
| **Finding ID** | PLAB-NNNN |
| **Finding Title** | [Title from bug report] |
| **Severity** | [P0/P1/P2/P3/P4] |
| **Category** | [Category from bug report] |

## Root Cause Analysis Summary

### Root Cause

[Brief description of the root cause identified during RCA.]

### Evidence

[Key evidence that led to identifying the root cause.]

### Hypotheses Tested

| Hypothesis | Result | Evidence |
|---|---|---|
| [Hypothesis 1] | [Confirmed/Eliminated] | [Evidence] |
| [Hypothesis 2] | [Confirmed/Eliminated] | [Evidence] |
| [Hypothesis 3] | [Confirmed/Eliminated] | [Evidence] |

## Repair Details

### Files Changed

| File | Change Type | Description |
|---|---|---|
| [file1.js] | [Modified/Added/Deleted] | [What changed] |
| [file2.js] | [Modified/Added/Deleted] | [What changed] |

### Code Diff

```diff
[Show the actual code changes]
```

### Repair Approach

[Describe the approach taken to fix the bug. Why this approach?]

### Minimal Change Justification

[Explain why this is the minimal change needed to fix the root cause.]

## Verification

### Reproduction Test

| Step | Action | Expected | Actual | Result |
|---|---|---|---|---|
| 1 | [Step] | [Expected] | [Actual] | ✅/❌ |
| 2 | [Step] | [Expected] | [Actual] | ✅/❌ |
| 3 | [Step] | [Expected] | [Actual] | ✅/❌ |

### Regression Tests

| Test | Area | Result | Notes |
|---|---|---|---|
| [Test 1] | [Area] | ✅/❌ | [Notes] |
| [Test 2] | [Area] | ✅/❌ | [Notes] |
| [Test 3] | [Area] | ✅/❌ | [Notes] |

### Performance Check

| Metric | Before | After | Change |
|---|---|---|---|
| FPS | [value] | [value] | [±%] |
| Memory | [value] | [value] | [±%] |
| Load Time | [value] | [value] | [±%] |

## Before/After Evidence

### Before (Bug)

- [Screenshot: bug manifestation](path/to/before.png)
- [Log: error messages](path/to/before.log)
- [Video: bug reproduction](path/to/before.mp4)

### After (Fixed)

- [Screenshot: fixed behavior](path/to/after.png)
- [Log: clean execution](path/to/after.log)
- [Video: fix verification](path/to/after.mp4)

## Rollback Plan

### Rollback Procedure

[Describe how to rollback this repair if needed.]

### Rollback Checkpoint

| Checkpoint Type | Reference |
|---|---|
| Git Branch | [branch-name] |
| Git Tag | [tag-name] |
| File Backup | [backup-path] |
| Commit | [commit-hash] |

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [Risk 1] | [Low/Medium/High] | [Low/Medium/High] | [Mitigation] |
| [Risk 2] | [Low/Medium/High] | [Low/Medium/High] | [Mitigation] |

## Side Effects

[Document any side effects or unintended consequences observed.]

## Lessons Learned

[What was learned from this repair? How can similar bugs be prevented?]

## Related Repairs

| Repair ID | Relationship | Description |
|---|---|---|
| PLAB-REPAIR-NNNN | [Dependent / Related / Conflicting] | [Description] |

## Status

| Status | Meaning |
|---|---|
| **In Progress** | Repair being implemented |
| **Completed** | Repair implemented, awaiting verification |
| **Verified** | Repair verified, bug resolved |
| **Failed** | Repair failed, needs different approach |
| **Rolled Back** | Repair rolled back due to issues |

**Current Status**: [Status]

## Dates

| Date | Event |
|---|---|
| [Date] | Repair started |
| [Date] | Repair implemented |
| [Date] | Repair verified |
| [Date] | Repair closed |

## Notes

[Additional notes, observations, special considerations.]

---

**Template Version**: 1.0
**Last Updated**: 2026-10-13

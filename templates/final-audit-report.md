# FINAL AUDIT REPORT TEMPLATE

Use this template for the final audit report (Phase 18) that provides the verdict on game readiness.

## Report Header

| Field | Value |
|---|---|
| **Report ID** | [YYYYMMDD-HHMMSS] |
| **Game Title** | [Game title] |
| **Game Version** | [Version] |
| **Audit Date** | [Date] |
| **Audit Duration** | [Duration] |
| **Audit Mode** | [BOSS_MODE, FULL_GAME_AUDIT, etc.] |
| **Auditor** | [Name/Agent] |

## A. Executive Summary

### Verdict

**[BOSS VERIFIED / BOSS VERIFIED—WITH LIMITATIONS / NEEDS MORE WORK / BLOCKED]**

### Key Findings

| Metric | Value |
|---|---|
| **Total Findings** | [Count] |
| **P0 (Critical)** | [Count] |
| **P1 (Major)** | [Count] |
| **P2 (Significant)** | [Count] |
| **P3 (Minor)** | [Count] |
| **P4 (Polish)** | [Count] |
| **Repaired** | [Count] |
| **Verified** | [Count] |
| **Open** | [Count] |
| **Waived** | [Count] |

### Executive Summary Text

[2-3 paragraph summary of audit results, key issues found, and overall assessment.]

### Recommendations

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

## B. Game Profile

### Game Identity

| Field | Value |
|---|---|
| **Title** | [Game title] |
| **Version** | [Version] |
| **Developer** | [Developer] |
| **Publisher** | [Publisher] |
| **Release Date** | [Date] |
| **Platform** | [Platform] |
| **Engine** | [Engine] |
| **Genre** | [Genre] |
| **Rating** | [Rating] |

### Technical Details

| Field | Value |
|---|---|
| **Build Type** | [Debug/Release] |
| **Architecture** | [x86/x64/ARM] |
| **OS Requirements** | [OS] |
| **GPU Requirements** | [GPU] |
| **RAM Requirements** | [RAM] |
| **Storage** | [Size] |
| **Network** | [Online/Offline] |
| **DRM** | [DRM type] |

### Core Mechanics

[Brief description of core gameplay mechanics.]

## C. Audit Coverage

### Audit Dimensions

| Dimension | Status | Coverage | Notes |
|---|---|---|---|
| **Functional** | ✅/❌/⚠️ | [X%] | [Notes] |
| **Visual** | ✅/❌/⚠️ | [X%] | [Notes] |
| **Physics** | ✅/❌/⚠️ | [X%] | [Notes] |
| **Animation** | ✅/❌/⚠️ | [X%] | [Notes] |
| **Audio** | ✅/❌/⚠️ | [X%] | [Notes] |
| **AI/NPC** | ✅/❌/⚠️ | [X%] | [Notes] |
| **UI/UX** | ✅/❌/⚠️ | [X%] | [Notes] |
| **Performance** | ✅/❌/⚠️ | [X%] | [Notes] |
| **Save/Load** | ✅/❌/⚠️ | [X%] | [Notes] |
| **Multiplayer** | ✅/❌/⚠️/N/A | [X%] | [Notes] |
| **Security** | ✅/❌/⚠️ | [X%] | [Notes] |
| **Blind Spots** | ✅/❌/⚠️ | [X%] | [Notes] |

### Test Coverage

| Category | Total | Passed | Failed | Blocked | Skipped | Coverage |
|---|---|---|---|---|---|---|
| [Category 1] | [Count] | [Count] | [Count] | [Count] | [Count] | [%] |
| [Category 2] | [Count] | [Count] | [Count] | [Count] | [Count] | [%] |

### Unreachable Areas

| Area | Reason | Impact |
|---|---|---|
| [Area 1] | [Reason] | [Impact] |
| [Area 2] | [Reason] | [Impact] |

## D. Findings Summary

### Findings by Severity

| Severity | Count | Status | Description |
|---|---|---|---|
| **P0** | [Count] | [Status] | [Description] |
| **P1** | [Count] | [Status] | [Description] |
| **P2** | [Count] | [Status] | [Description] |
| **P3** | [Count] | [Status] | [Description] |
| **P4** | [Count] | [Status] | [Description] |

### Findings by Category

| Category | Count | P0 | P1 | P2 | P3 | P4 |
|---|---|---|---|---|---|---|
| [Category 1] | [Count] | [Count] | [Count] | [Count] | [Count] | [Count] |
| [Category 2] | [Count] | [Count] | [Count] | [Count] | [Count] | [Count] |

### Critical Findings (P0/P1)

| Finding ID | Title | Severity | Status | Description |
|---|---|---|---|---|
| PLAB-NNNN | [Title] | [P0/P1] | [Status] | [Brief description] |
| PLAB-NNNN | [Title] | [P0/P1] | [Status] | [Brief description] |

### All Findings

| Finding ID | Title | Severity | Category | Status | Description |
|---|---|---|---|---|---|
| PLAB-NNNN | [Title] | [P0-P4] | [Category] | [Status] | [Brief description] |
| PLAB-NNNN | [Title] | [P0-P4] | [Category] | [Status] | [Brief description] |

## E. Repairs Summary

### Repairs by Category

| Category | Count | Verified | Failed | Rolled Back |
|---|---|---|---|---|
| [Category 1] | [Count] | [Count] | [Count] | [Count] |
| [Category 2] | [Count] | [Count] | [Count] | [Count] |

### Critical Repairs (P0/P1)

| Repair ID | Finding ID | Title | Status | Verification |
|---|---|---|---|---|
| PLAB-REPAIR-NNNN | PLAB-NNNN | [Title] | [Status] | [Verification result] |
| PLAB-REPAIR-NNNN | PLAB-NNNN | [Title] | [Status] | [Verification result] |

### All Repairs

| Repair ID | Finding ID | Title | Status | Date |
|---|---|---|---|---|
| PLAB-REPAIR-NNNN | PLAB-NNNN | [Title] | [Status] | [Date] |
| PLAB-REPAIR-NNNN | PLAB-NNNN | [Title] | [Status] | [Date] |

## F. Quality Gates

### Gate Results

| Gate | Name | Status | Evidence | Notes |
|---|---|---|---|---|
| **A** | LAUNCH | ✅/❌ | [Evidence] | [Notes] |
| **B** | CORE LOOP | ✅/❌ | [Evidence] | [Notes] |
| **C** | COVERAGE | ✅/❌ | [Evidence] | [Notes] |
| **D** | FINDINGS | ✅/❌ | [Evidence] | [Notes] |
| **E** | REGRESSION | ✅/❌ | [Evidence] | [Notes] |
| **F** | EVIDENCE | ✅/❌ | [Evidence] | [Notes] |

### Gate Details

#### Gate A: LAUNCH

**Status**: [PASS/FAIL]

**Evidence**: [Launch log, screenshot, FPS measurement]

**Notes**: [Any issues or observations]

#### Gate B: CORE LOOP

**Status**: [PASS/FAIL]

**Evidence**: [Video of core loop, state verification]

**Notes**: [Any issues or observations]

#### Gate C: COVERAGE

**Status**: [PASS/FAIL]

**Evidence**: [Coverage report, test matrix results]

**Notes**: [Any issues or observations]

#### Gate D: FINDINGS

**Status**: [PASS/FAIL]

**Evidence**: [Findings index, repair reports]

**Notes**: [Any issues or observations]

#### Gate E: REGRESSION

**Status**: [PASS/FAIL]

**Evidence**: [Regression test results, comparison]

**Notes**: [Any issues or observations]

#### Gate F: EVIDENCE

**Status**: [PASS/FAIL]

**Evidence**: [Final report, evidence directory]

**Notes**: [Any issues or observations]

## G. Recommendations

### Immediate Actions (Before Release)

1. [Action 1]
2. [Action 2]
3. [Action 3]

### Post-Release Actions

1. [Action 1]
2. [Action 2]
3. [Action 3]

### Known Limitations

| Limitation | Impact | Workaround |
|---|---|---|
| [Limitation 1] | [Impact] | [Workaround] |
| [Limitation 2] | [Impact] | [Workaround] |

### Future Improvements

| Improvement | Priority | Effort |
|---|---|---|
| [Improvement 1] | [P0-P4] | [Low/Medium/High] |
| [Improvement 2] | [P0-P4] | [Low/Medium/High] |

## H. Audit Metadata

### Session Information

| Field | Value |
|---|---|
| **Session ID** | [YYYYMMDD-HHMMSS] |
| **Start Time** | [Timestamp] |
| **End Time** | [Timestamp] |
| **Duration** | [Duration] |
| **Mode** | [Mode] |
| **Engine** | [Engine] |
| **Adapter** | [Adapter] |

### Environment

| Field | Value |
|---|---|
| **OS** | [Operating system] |
| **Hardware** | [CPU, GPU, RAM] |
| **Browser** | [If web game] |
| **Tools Used** | [List of tools] |

### Artifacts

| Artifact | Location | Description |
|---|---|---|
| **Game Profile** | [.plab/game-profile.md] | [Description] |
| **Findings Index** | [.plab/findings-index.json] | [Description] |
| **Repairs Index** | [.plab/repairs-index.json] | [Description] |
| **Evidence** | [.plab/evidence/] | [Description] |
| **Test Results** | [.plab/test-results/] | [Description] |
| **Knowledge Base** | [.plab/knowledge-base.md] | [Description] |

## I. Sign-Off

### Audit Completion

| Role | Name | Date | Signature |
|---|---|---|---|
| **Lead Auditor** | [Name] | [Date] | [Signature] |
| **QA Lead** | [Name] | [Date] | [Signature] |
| **Product Owner** | [Name] | [Date] | [Signature] |

### Release Decision

| Decision | Approved By | Date |
|---|---|---|
| **[RELEASE / NO RELEASE / CONDITIONAL]** | [Name] | [Date] |

---

**Template Version**: 1.0
**Last Updated**: 2026-10-13

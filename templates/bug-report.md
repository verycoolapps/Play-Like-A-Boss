# BUG REPORT TEMPLATE

Use this template for every finding (PLAB-NNNN) discovered during audit or play.

## Finding ID

**PLAB-NNNN** (auto-incremented)

## Title

[Brief, descriptive title of the bug]

## Severity

| Severity | Definition | Examples |
|---|---|---|
| **P0** | Game-breaking | Crash on launch, soft-lock, save corruption, core mechanic dead |
| **P1** | Major | Progression blocked, major visual corruption, data loss, severe perf |
| **P2** | Significant | Noticeable bugs, edge-case failures, minor perf issues |
| **P3** | Minor | Cosmetic, rare edge cases, small inconsistencies |
| **P4** | Polish | Nice-to-have, theoretical, documentation gaps |

**Assigned Severity**: [P0/P1/P2/P3/P4]

## Category

| Category | Description |
|---|---|
| **functional** | Game mechanics, controls, progression |
| **visual** | Rendering, UI, graphics, animation |
| **physics** | Collision, movement, constraints |
| **animation** | Character animations, skeletal animation |
| **audio** | Sound effects, music, voice, mixing |
| **ai** | NPC behavior, pathfinding, decision-making |
| **performance** | FPS, memory, CPU, GPU, loading |
| **save/load** | Save system, persistence, data integrity |
| **multiplayer** | Networking, sync, multiplayer-specific |
| **security** | Input validation, anti-cheat, data protection |
| **ui/ux** | User interface, user experience, accessibility |
| **other** | Anything else |

**Assigned Category**: [category]

## Description

[Detailed description of the bug. What happens, when, under what conditions.]

## Reproduction Steps

1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]
5. [Step 5]

**Reproducibility**: [Always / Sometimes / Rarely]

## Expected Behavior

[What should happen when following the reproduction steps.]

## Actual Behavior

[What actually happens. Describe the incorrect behavior.]

## Environment

| Field | Value |
|---|---|
| **Game Version** | [Version number] |
| **Platform** | [PC, Console, Mobile, Web] |
| **OS** | [Operating system] |
| **Hardware** | [CPU, GPU, RAM] |
| **Build Type** | [Debug, Release, Development] |
| **Settings** | [Graphics settings, difficulty, etc.] |

## Evidence

### Screenshots

- [Screenshot 1: description](path/to/screenshot1.png)
- [Screenshot 2: description](path/to/screenshot2.png)

### Videos

- [Video: description](path/to/video.mp4)

### Logs

- [Log excerpt: description](path/to/log.txt)

### State Dumps

- [State dump: description](path/to/state.json)

### Metrics

- [Metric: value](path/to/metrics.txt)

## Root Cause Analysis

### Hypotheses

1. [Hypothesis 1] - [Likelihood: High/Medium/Low]
2. [Hypothesis 2] - [Likelihood: High/Medium/Low]
3. [Hypothesis 3] - [Likelihood: High/Medium/Low]

### Investigation

[What was tested, what was found, how hypotheses were evaluated.]

### Root Cause

[Exact cause: file, line, mechanism. What is the actual root cause?]

## Impact

### User Impact

[How does this bug affect the player? What experience does it create?]

### Technical Impact

[How does this bug affect the codebase? What systems are affected?]

### Business Impact

[How does this bug affect the product? What are the consequences?]

## Workaround

[If a workaround exists, describe it. If not, state "No workaround known."]

## Suggested Fix

[If you have ideas for fixing this bug, describe them. If not, state "Needs investigation."]

## Related Findings

| Finding ID | Relationship | Description |
|---|---|---|
| PLAB-NNNN | [Duplicate / Related / Dependent] | [Description] |

## Status

| Status | Meaning |
|---|---|
| **Open** | Bug confirmed, not yet fixed |
| **In Progress** | Repair in progress |
| **Repaired** | Fix implemented, awaiting verification |
| **Verified** | Fix verified, bug resolved |
| **Won't Fix** | Bug acknowledged, won't be fixed (with reason) |
| **Duplicate** | Duplicate of another finding |
| **Cannot Reproduce** | Bug could not be reproduced |

**Current Status**: [Status]

## Assigned To

[Who is responsible for fixing this bug?]

## Priority

| Priority | Meaning |
|---|---|
| **P0** | Fix immediately, blocks release |
| **P1** | Fix before release |
| **P2** | Fix in next update |
| **P3** | Fix when convenient |
| **P4** | Nice to have, low priority |

**Assigned Priority**: [Priority]

## Dates

| Date | Event |
|---|---|
| [Date] | Bug discovered |
| [Date] | Bug confirmed |
| [Date] | Fix implemented |
| [Date] | Fix verified |
| [Date] | Bug closed |

## Notes

[Additional notes, observations, special considerations.]

---

**Template Version**: 1.0
**Last Updated**: 2026-10-13

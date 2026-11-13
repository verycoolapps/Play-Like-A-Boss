# FUNCTIONAL AUDIT

Systematic verification that every game mechanic works as intended. This is the core audit — if functionality is broken, nothing else matters.

## Audit Scope

Functional audit covers:

- Core gameplay mechanics
- Player controls and input
- Game state transitions
- Progression systems
- UI interactions
- Save/load functionality
- Multiplayer (if applicable)
- Edge cases and boundary conditions

## Methodology

For each mechanic:

1. **Identify** — what should this mechanic do?
2. **Exercise** — perform the action that triggers it.
3. **Observe** — capture the result.
4. **Verify** — compare observed vs expected.
5. **Document** — record finding if mismatch.

## Core Mechanics Checklist

### Movement & Navigation

| Test | Procedure | Expected | Evidence |
|---|---|---|---|
| Walk/run | Move in all directions | Character moves smoothly | Screenshot sequence |
| Jump | Press jump button | Character leaves ground, lands | Video or frame capture |
| Crouch/prone | Press crouch | Character lowers, can't jump | Screenshot |
| Sprint | Hold sprint | Speed increases, stamina drains | Metric comparison |
| Swim/climb | Enter water/ladders | Movement mode changes | State inspection |
| Drive/flight | Enter vehicle/aircraft | Controls change, physics differ | State inspection |

### Combat

| Test | Procedure | Expected | Evidence |
|---|---|---|---|
| Basic attack | Press attack button | Damage dealt, animation plays | Damage numbers, animation |
| Combo | Chain attacks | Combo counter increments, damage scales | Combo display, damage log |
| Dodge/roll | Press dodge during attack | i-frames active, position changes | State inspection |
| Block/parry | Hold block, time attack | Damage reduced/negated | Damage numbers |
| Special ability | Use skill with resource cost | Resource consumed, effect applied | Resource bar, effect visual |
| Weapon switch | Change equipped weapon | Stats update, animations change | UI, damage comparison |

### Interaction

| Test | Procedure | Expected | Evidence |
|---|---|---|---|
| Pickup item | Walk over item | Item added to inventory | Inventory count |
| Use item | Select item, use on target | Effect applied, item consumed | Inventory, target state |
| Open door | Interact with door | Door opens, path clear | Visual, collision state |
| Talk to NPC | Interact with NPC | Dialogue starts | Dialogue box |
| Read note | Interact with note | Text displays | Text box |
| Activate switch | Interact with switch | Mechanism activates | Visual, state change |

### Progression

| Test | Procedure | Expected | Evidence |
|---|---|---|---|
| Level up | Gain enough XP | Level increases, stats improve | Level display, stat comparison |
| Learn skill | Reach level/quest | Skill added to menu | Skill list |
| Unlock area | Complete objective | New area accessible | Map change, collision update |
| Quest accept | Talk to quest giver | Quest added to log | Quest journal |
| Quest complete | Finish objectives | Rewards granted, quest marked | Quest log, inventory |

### Economy

| Test | Procedure | Expected | Evidence |
|---|---|---|---|
| Buy item | Visit shop, purchase | Gold decreases, item added | Gold display, inventory |
| Sell item | Visit shop, sell | Gold increases, item removed | Gold display, inventory |
| Craft item | Combine materials | Item created, materials consumed | Inventory |
| Upgrade equipment | Visit blacksmith | Stats improve, gold decreases | Equipment stats |

### UI Interactions

| Test | Procedure | Expected | Evidence |
|---|---|---|---|
| Menu open/close | Press menu button | Menu appears/disappears | Screenshot |
| Inventory navigation | Open inventory, select item | Item details shown | Screenshot |
| Settings change | Adjust volume, graphics | Changes apply immediately | Metric comparison |
| Pause game | Press pause | Game freezes, menu shows | State inspection |
| Quit to menu | Select quit | Returns to main menu | Screen change |

### Save/Load

| Test | Procedure | Expected | Evidence |
|---|---|---|---|
| Save game | Open menu, save | Save file created | File system check |
| Load game | Open menu, load | Game state restored | State comparison |
| Quick save | Press quick save | Instant save, no menu | File timestamp |
| Auto save | Trigger autosave | Save happens automatically | File timestamp |
| Save during battle | Save mid-combat | Battle state preserved | Reload and verify |

### Multiplayer (if applicable)

| Test | Procedure | Expected | Evidence |
|---|---|---|---|
| Join game | Connect to server | Player appears in world | Player list |
| Move sync | Move character | Other players see movement | Second client view |
| Combat sync | Attack enemy | Damage synced to all | Damage display |
| Chat | Send message | Message appears for all | Chat log |
| Disconnect | Close client | Player removed, state saved | Player list |

## Edge Cases

Test boundary conditions and unusual inputs:

| Category | Tests |
|---|---|
| Input spam | Mash buttons, hold keys, rapid presses |
| Invalid input | Wrong buttons, simultaneous inputs, modifier combos |
| Boundary values | Max health, zero ammo, full inventory, level cap |
| Timing | Pause during load, quit during save, input during transition |
| State conflicts | Save during cutscene, load during battle, die during pause |
| Resource exhaustion | Run out of health/mana/ammo, then try to use |
| Sequence breaks | Skip tutorial, enter area early, use item before obtaining |

## Evidence Collection

For each test:

1. **Before state** — screenshot or state dump.
2. **Action** — what input was sent.
3. **After state** — screenshot or state dump.
4. **Logs** — console output, errors, warnings.
5. **Metrics** — FPS, memory, timing if relevant.

Store evidence in `.plab/session-*/evidence/functional/`.

## Finding Documentation

When a test fails:

1. **Create finding** — use `templates/bug-report.md`.
2. **Assign severity** — P0–P4 based on impact.
3. **Link evidence** — reference screenshots, logs, state dumps.
4. **Describe reproduction** — exact steps to reproduce.
5. **Note expected vs actual** — what should happen vs what did.

## Coverage Tracking

Maintain a checklist of tested mechanics:

```
FUNCTIONAL AUDIT PROGRESS
├── Movement: [x] [x] [x] [x] [x] [x]
├── Combat: [x] [x] [x] [x] [x] [x]
├── Interaction: [x] [x] [x] [x] [x] [x]
├── Progression: [x] [x] [x] [x] [x] [x]
├── Economy: [x] [x] [x] [x] [x]
├── UI: [x] [x] [x] [x] [x] [x]
├── Save/Load: [x] [x] [x] [x] [x]
└── Multiplayer: [x] [x] [x] [x] [x] (if applicable)

TOTAL: 45/48 tested (94%)
BLOCKED: 3 tests (multiplayer server unavailable)
```

## When to Stop

Stop functional audit when:

- All mechanics tested at least once.
- All P0/P1 findings documented.
- No new findings in last 10 tests.
- Time budget exhausted (document remaining tests).
- Platform limits prevent further testing.

## Integration with Other Audits

Functional audit findings may reveal issues in other dimensions:

- Visual bug → visual audit
- Physics bug → physics audit
- Performance issue → performance audit
- UI problem → visual audit §UI
- Audio issue → audio audit

Cross-reference findings and coordinate audits.

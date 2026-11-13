# GAMEPLAY TEST MATRIX

Universal test matrix covering all game systems and mechanics. Each test has a unique ID, procedure, expected result, evidence requirements, and status tracking.

## Test Matrix Structure

```
TEST ID | CATEGORY | TEST NAME | PROCEDURE | EXPECTED RESULT | EVIDENCE | STATUS | NOTES
--------|----------|-----------|-----------|-----------------|----------|--------|------
PLAB-T001 | CORE | Launch game | Start game executable | Game reaches menu | Screenshot, log | ⬜ | 
PLAB-T002 | CORE | Start new game | Click New Game | Game starts, level 1 loads | Screenshot, state | ⬜ |
```

## Test Categories

### Category 1: Core Systems (PLAB-T001–T050)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T001 | Game launch | Start game executable | Game reaches main menu | Screenshot, log |
| PLAB-T002 | New game start | Select New Game | Game starts, level 1 loads | Screenshot, state |
| PLAB-T003 | Continue game | Select Continue | Save loads, game resumes | Screenshot, state |
| PLAB-T004 | Settings menu | Open settings | Settings menu displays | Screenshot |
| PLAB-T005 | Quit to menu | Quit from gameplay | Returns to main menu | Screenshot |
| PLAB-T006 | Exit game | Exit from menu | Game closes cleanly | Log, process check |
| PLAB-T007 | Window resize | Resize game window | UI adapts correctly | Screenshot |
| PLAB-T008 | Fullscreen toggle | Toggle fullscreen | Fullscreen works correctly | Screenshot |
| PLAB-T009 | Resolution change | Change resolution | Game renders correctly | Screenshot |
| PLAB-T010 | Alt+Tab | Switch away and back | Game pauses/resumes correctly | Screenshot |

### Category 2: Player Controls (PLAB-T051–T100)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T051 | Keyboard movement | Press WASD/arrows | Character moves correctly | Video, position |
| PLAB-T052 | Mouse look | Move mouse | Camera rotates correctly | Video, rotation |
| PLAB-T053 | Gamepad movement | Use left stick | Character moves correctly | Video, position |
| PLAB-T054 | Jump | Press jump button | Character jumps | Video, position |
| PLAB-T055 | Crouch | Press crouch button | Character crouches | Screenshot |
| PLAB-T056 | Sprint | Hold sprint | Character sprints | Video, speed |
| PLAB-T057 | Interact | Press interact button | Interaction occurs | Video, state |
| PLAB-T058 | Attack | Press attack button | Attack animation plays | Video, damage |
| PLAB-T059 | Block | Hold block button | Block state active | Screenshot |
| PLAB-T060 | Dodge | Press dodge button | Dodge animation plays | Video, position |

### Category 3: Game Mechanics (PLAB-T101–T200)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T101 | Health system | Take damage | Health decreases | Health display |
| PLAB-T102 | Health regen | Wait after damage | Health regenerates | Health display |
| PLAB-T103 | Death | Reduce health to 0 | Death screen/game over | Screenshot |
| PLAB-T104 | Respawn | Respawn after death | Player respawns correctly | Screenshot, position |
| PLAB-T105 | Inventory | Open inventory | Inventory displays | Screenshot |
| PLAB-T106 | Item pickup | Walk over item | Item added to inventory | Inventory count |
| PLAB-T107 | Item use | Use item from inventory | Item effect applies | State change |
| PLAB-T108 | Equipment | Equip weapon/armor | Stats update | Equipment display |
| PLAB-T109 | Currency | Earn/spend currency | Currency updates | Currency display |
| PLAB-T110 | Quest system | Accept/complete quest | Quest state updates | Quest log |

### Category 4: World & Environment (PLAB-T201–T300)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T201 | Level loading | Enter new level | Level loads correctly | Screenshot, state |
| PLAB-T202 | Level transition | Move to next level | Transition smooth | Video |
| PLAB-T203 | Door/portal | Enter door/portal | Teleport works | Screenshot, position |
| PLAB-T204 | Checkpoint | Reach checkpoint | Checkpoint saves | Save file check |
| PLAB-T205 | Save point | Use save point | Game saves | Save file check |
| PLAB-T206 | Environment interaction | Interact with objects | Objects respond | Video, state |
| PLAB-T207 | Weather effects | Trigger weather | Weather displays | Screenshot |
| PLAB-T208 | Day/night cycle | Wait for time change | Lighting changes | Screenshot |
| PLAB-T209 | Dynamic objects | Move/interact with objects | Objects respond | Video, state |
| PLAB-T210 | Destructible objects | Destroy objects | Objects break | Video, debris |

### Category 5: Enemies & AI (PLAB-T301–T400)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T301 | Enemy spawn | Enter enemy area | Enemies spawn | Screenshot, count |
| PLAB-T302 | Enemy patrol | Observe enemy movement | Enemies patrol | Video, path |
| PLAB-T303 | Enemy aggro | Approach enemy | Enemy becomes aggressive | Video, state |
| PLAB-T304 | Enemy attack | Let enemy attack | Enemy attacks player | Video, damage |
| PLAB-T305 | Enemy death | Kill enemy | Enemy dies, drops loot | Video, loot |
| PLAB-T306 | Boss fight | Fight boss | Boss mechanics work | Video, phases |
| PLAB-T307 | Enemy respawn | Leave and return | Enemies respawn | Screenshot, count |
| PLAB-T308 | Enemy AI | Observe enemy behavior | AI behaves correctly | Video, decisions |
| PLAB-T309 | Enemy pathfinding | Watch enemy navigate | Pathfinding works | Video, path |
| PLAB-T310 | Enemy difficulty | Fight on different levels | Difficulty scales | Comparison |

### Category 6: UI/UX (PLAB-T401–T500)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T401 | HUD display | Enter gameplay | HUD shows correctly | Screenshot |
| PLAB-T402 | Health bar | Take damage | Health bar updates | Screenshot |
| PLAB-T403 | Minimap | Open map | Minimap displays | Screenshot |
| PLAB-T404 | Objective display | Check objectives | Objectives shown | Screenshot |
| PLAB-T405 | Dialogue UI | Talk to NPC | Dialogue displays | Screenshot |
| PLAB-T406 | Menu system | Open menu | Menu displays | Screenshot |
| PLAB-T407 | Settings UI | Open settings | Settings work | Screenshot, test |
| PLAB-T408 | Inventory UI | Open inventory | Inventory works | Screenshot, test |
| PLAB-T409 | Crafting UI | Open crafting | Crafting works | Screenshot, test |
| PLAB-T410 | Shop UI | Open shop | Shop works | Screenshot, test |

### Category 7: Audio (PLAB-T501–T600)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T501 | Background music | Enter gameplay | Music plays | Audio recording |
| PLAB-T502 | Sound effects | Perform actions | SFX play correctly | Audio recording |
| PLAB-T503 | Voice dialogue | Talk to NPC | Voice plays | Audio recording |
| PLAB-T504 | Ambient audio | Enter environment | Ambient sounds play | Audio recording |
| PLAB-T505 | Music transitions | Change scenes | Music transitions | Audio recording |
| PLAB-T506 | Volume controls | Adjust volume | Volume changes | Audio measurement |
| PLAB-T507 | Audio sync | Perform timed actions | Audio syncs correctly | Audio-visual sync |
| PLAB-T508 | Positional audio | Move around sounds | Audio positions correctly | Audio analysis |
| PLAB-T509 | Audio ducking | Trigger important sound | Other audio ducks | Audio analysis |
| PLAB-T510 | Audio quality | Listen to audio | No distortion, clear | Audio analysis |

### Category 8: Performance (PLAB-T601–T700)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T601 | FPS measurement | Measure FPS | FPS within target | FPS counter |
| PLAB-T602 | Frame time | Measure frame time | Frame time < 16.67ms | Frame time graph |
| PLAB-T603 | Memory usage | Monitor memory | Memory within limits | Memory profiler |
| PLAB-T604 | CPU usage | Monitor CPU | CPU within limits | CPU profiler |
| PLAB-T605 | GPU usage | Monitor GPU | GPU within limits | GPU profiler |
| PLAB-T606 | Loading time | Measure loading | Loading < target | Timer |
| PLAB-T607 | Draw calls | Count draw calls | Draw calls < target | Renderer info |
| PLAB-T608 | Triangle count | Count triangles | Triangles < target | Renderer info |
| PLAB-T609 | Texture memory | Monitor VRAM | VRAM within limits | Memory profiler |
| PLAB-T610 | Stress test | Maximum load | Performance acceptable | All metrics |

### Category 9: Save/Load (PLAB-T701–T800)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T701 | Save game | Use save point | Game saves | Save file check |
| PLAB-T702 | Load game | Load save | Game loads correctly | State comparison |
| PLAB-T703 | Quick save | Use quick save | Instant save | Save file timestamp |
| PLAB-T704 | Auto save | Trigger autosave | Auto save works | Save file timestamp |
| PLAB-T705 | Save during battle | Save mid-combat | Battle state saved | Reload and verify |
| PLAB-T706 | Save during cutscene | Save during cutscene | Cutscene state saved | Reload and verify |
| PLAB-T707 | Multiple saves | Create multiple saves | All saves work | Save file check |
| PLAB-T708 | Save corruption | Corrupt save file | Game handles gracefully | Error handling |
| PLAB-T709 | Save version | Load old save | Old save migrates | Migration log |
| PLAB-T710 | Save space | Fill save space | Game handles gracefully | Error handling |

### Category 10: Multiplayer (PLAB-T801–T900, if applicable)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T801 | Join game | Connect to server | Player joins | Player list |
| PLAB-T802 | Leave game | Disconnect | Player leaves | Player list |
| PLAB-T803 | Movement sync | Move character | Other players see movement | Second client |
| PLAB-T804 | Combat sync | Attack enemy | Damage synced | Damage display |
| PLAB-T805 | Chat | Send message | Message appears | Chat log |
| PLAB-T806 | Trade | Trade items | Trade works | Inventory comparison |
| PLAB-T807 | Party | Form/join party | Party works | Party list |
| PLAB-T808 | Guild | Join/create guild | Guild works | Guild list |
| PLAB-T809 | Network latency | Simulate lag | Game handles lag | Network simulation |
| PLAB-T910 | Disconnect recovery | Disconnect and reconnect | Game recovers | Reconnection test |

### Category 11: Edge Cases (PLAB-T901–T1000)

| Test ID | Test Name | Procedure | Expected | Evidence |
|---|---|---|---|---|
| PLAB-T901 | Input spam | Mash buttons rapidly | Game handles gracefully | Video, logs |
| PLAB-T902 | Invalid input | Enter invalid commands | Game rejects gracefully | Error handling |
| PLAB-T903 | Boundary values | Test min/max values | Game handles extremes | State verification |
| PLAB-T904 | Timing edge cases | Input at frame boundaries | Game handles correctly | Frame analysis |
| PLAB-T905 | State conflicts | Conflicting states | Game resolves correctly | State verification |
| PLAB-T906 | Resource exhaustion | Deplete all resources | Game handles gracefully | Resource state |
| PLAB-T907 | Sequence breaks | Skip required steps | Game handles gracefully | State verification |
| PLAB-T908 | Long session | Play for extended time | Game remains stable | Memory, performance |
| PLAB-T909 | Rapid transitions | Quick scene changes | Game handles gracefully | Transition test |
| PLAB-T910 | Concurrent actions | Multiple simultaneous inputs | Game prioritizes correctly | Input test |

## Test Execution

### Test Status Values

| Status | Meaning |
|---|---|
| ⬜ | Not started |
| 🔄 | In progress |
| ✅ | Passed |
| ❌ | Failed |
| ⚠️ | Partial pass / known issue |
| 🚫 | Blocked / cannot test |
| ⏭️ | Skipped / not applicable |

### Test Execution Order

1. **Core systems first** — ensure game launches and basic functionality works.
2. **Critical mechanics** — test core gameplay before edge cases.
3. **Dependent systems** — test systems that depend on others.
4. **Edge cases last** — test unusual scenarios after basics pass.

### Test Documentation

For each test:

1. **Record result** — pass/fail/partial.
2. **Capture evidence** — screenshots, videos, logs.
3. **Note issues** — any problems encountered.
4. **Link findings** — reference PLAB-NNNN findings.
5. **Update matrix** — mark test status.

## Coverage Tracking

Track test coverage:

```
TEST MATRIX PROGRESS
├── Core Systems: 10/10 (100%)
├── Player Controls: 10/10 (100%)
├── Game Mechanics: 10/10 (100%)
├── World & Environment: 10/10 (100%)
├── Enemies & AI: 10/10 (100%)
├── UI/UX: 10/10 (100%)
├── Audio: 10/10 (100%)
├── Performance: 10/10 (100%)
├── Save/Load: 10/10 (100%)
├── Multiplayer: 10/10 (100%) [if applicable]
└── Edge Cases: 10/10 (100%)

TOTAL: 110/110 tests (100%)
PASSED: 105/110 (95%)
FAILED: 3/110 (3%)
BLOCKED: 2/110 (2%)
```

## When to Stop

Stop test matrix execution when:

- All tests executed at least once.
- All P0/P1 findings documented.
- No new findings in last 20 tests.
- Time budget exhausted.
- Platform limits prevent further testing.

## Integration with Other Modules

- **Functional audit** → `auditing/functional-audit.md`
- **Exploratory testing** → `testing/exploratory-testing.md`
- **Release validation** → `testing/release-validation.md`
- **Regression testing** → `repair/regression-testing.md`

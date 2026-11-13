# AI/NPC AUDIT

Systematic verification of artificial intelligence and non-player character behavior: pathfinding, decision-making, state machines, and emergent behavior.

## Audit Scope

AI/NPC audit covers:

- Pathfinding (navigation, obstacle avoidance)
- Decision-making (state machines, behavior trees, utility AI)
- NPC behavior (idle, patrol, chase, flee, interact)
- Enemy AI (combat, tactics, difficulty scaling)
- Companion AI (following, assisting, commands)
- Ambient AI (wildlife, crowds, background NPCs)
- AI performance (CPU usage, update frequency)
- AI edge cases (stuck states, infinite loops, exploits)

## Methodology

For each AI element:

1. **Identify** — what behavior should this NPC exhibit?
2. **Set up** — create test scenario.
3. **Execute** — trigger AI behavior.
4. **Observe** — capture AI state and actions.
5. **Verify** — compare observed vs expected.
6. **Document** — record finding if mismatch.

## Pathfinding

### Navigation Mesh (NavMesh)

| Check | What to look for | Evidence |
|---|---|---|
| NavMesh coverage | All walkable areas covered | NavMesh visualization |
| Path quality | Paths are efficient, not zigzag | Path visualization |
| Obstacle avoidance | NPCs navigate around obstacles | Movement tracking |
| Dynamic obstacles | NPCs react to moving obstacles | Moving obstacle test |
| Path smoothing | Paths are smooth, not jerky | Movement analysis |

### Waypoint/Graph Navigation

| Check | What to look for | Evidence |
|---|---|---|
| Waypoint coverage | All areas reachable | Waypoint map |
| Graph connectivity | All nodes connected | Graph visualization |
| Path recalculation | Paths update when blocked | Blocked path test |
| Waypoint precision | NPCs reach waypoints accurately | Position tracking |

### Steering Behaviors

| Check | What to look for | Evidence |
|---|---|---|
| Seek | NPC moves toward target | Movement tracking |
| Flee | NPC moves away from threat | Threat response |
| Arrive | NPC slows down near target | Speed profile |
| Separation | NPCs don't overlap | Position analysis |
| Alignment | NPCs face movement direction | Rotation tracking |
| Cohesion | Groups stay together | Group behavior |

## Decision-Making

### State Machines

| Check | What to look for | Evidence |
|---|---|---|
| State transitions | States change when conditions met | State tracking |
| State exit | Clean exit, no stuck states | Transition completion |
| State priority | Correct state wins | Multiple triggers |
| State persistence | States maintained correctly | Long-term observation |

### Behavior Trees

| Check | What to look for | Evidence |
|---|---|---|
| Tree structure | Logical hierarchy | Tree visualization |
| Node execution | Nodes execute in correct order | Execution log |
| Condition evaluation | Conditions evaluated correctly | Condition test |
| Action execution | Actions perform correctly | Action result |
| Tree updates | Tree updates at correct frequency | Update timing |

### Utility AI

| Check | What to look for | Evidence |
|---|---|---|
| Utility calculation | Scores calculated correctly | Score logging |
| Decision selection | Highest utility action chosen | Decision log |
| Utility decay | Scores decay over time | Time-based test |
| Context awareness | AI responds to context | Context change test |

## NPC Behavior

### Ambient NPCs

| Check | What to look for | Evidence |
|---|---|---|
| Idle behavior | NPCs idle naturally | Idle animation, movement |
| Patrol routes | NPCs follow patrol paths | Path tracking |
| Schedules | NPCs follow daily schedules | Time-based observation |
| Interactions | NPCs react to player | Player proximity test |
| Conversations | NPCs engage in dialogue | Dialogue test |

### Quest NPCs

| Check | What to look for | Evidence |
|---|---|---|
| Quest availability | NPCs offer correct quests | Quest marker, dialogue |
| Quest progress | NPCs reflect quest state | Dialogue update |
| Quest completion | NPCs acknowledge completion | Completion dialogue |
| Quest failure | NPCs react to failure | Failure dialogue |

### Companion AI

| Check | What to look for | Evidence |
|---|---|---|
| Following | Companions follow player | Movement tracking |
| Positioning | Companions maintain formation | Position analysis |
| Combat assist | Companions help in combat | Combat observation |
| Commands | Companions respond to commands | Command test |
| Loyalty | Companions stay with player | Long-term observation |

## Enemy AI

### Combat Behavior

| Check | What to look for | Evidence |
|---|---|---|
| Aggro range | Enemies aggro at correct distance | Distance test |
| Attack patterns | Enemies use varied attacks | Attack log |
| Defensive behavior | Enemies block, dodge, retreat | Combat observation |
| Group tactics | Enemies coordinate | Multi-enemy test |
| Difficulty scaling | Enemies scale with player level | Level comparison |

### Boss AI

| Check | What to look for | Evidence |
|---|---|---|
| Phase transitions | Boss changes phases correctly | Phase tracking |
| Attack patterns | Boss uses varied attacks | Attack log |
| Minion spawning | Boss spawns minions correctly | Minion count |
| Weakness exploitation | Boss vulnerable to correct attacks | Damage type test |
| Enrage mechanics | Boss enrages at correct threshold | Health threshold test |

## AI Edge Cases

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Stuck detection | NPC gets stuck on obstacle | NPC recovers or reports stuck | Recovery observation |
| Infinite loop | AI enters loop | AI exits loop or times out | Timeout detection |
| Resource exhaustion | AI runs out of resources | AI handles gracefully | Resource depletion test |
| Player exploit | Player uses AI exploit | AI responds or ignores | Exploit test |
| Extreme values | AI gets extreme inputs | AI handles gracefully | Input stress test |
| Concurrent actions | Multiple AI actions at once | AI prioritizes correctly | Priority test |

## AI Performance

| Metric | Target | Measurement |
|---|---|---|
| AI update rate | 30–60 Hz | Update frequency |
| Pathfinding cost | < 1ms per NPC | Pathfinding time |
| Decision cost | < 0.5ms per NPC | Decision time |
| Active NPCs | < 100 simultaneous | Active count |
| Memory usage | < 10MB per NPC | Memory profiler |

## Common AI Bugs

### Critical (P0/P1)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| AI freeze | NPC stops responding | State machine stuck, infinite loop | Add timeout, fix state transition |
| Pathfinding failure | NPC can't reach target | NavMesh gap, obstacle blocking | Fix NavMesh, add dynamic obstacle handling |
| AI exploit | Player can exploit AI | Missing validation, predictable behavior | Add randomness, validation |
| Infinite aggro | Enemy never loses target | Aggro range too large, no leash | Add leash range, deaggro conditions |
| AI crash | Game crashes on AI update | Null reference, invalid state | Add null checks, state validation |

### Major (P2)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| AI stuck | NPC gets stuck on obstacle | Pathfinding failure, collision issue | Improve pathfinding, add stuck detection |
| Unpredictable AI | AI behaves randomly | Random seed not set, too much randomness | Set seed, balance randomness |
| AI too easy/hard | Difficulty mismatch | AI parameters wrong | Tune AI parameters |
| AI repetitive | AI uses same actions | Limited action pool, no variety | Add more actions, increase variety |
| AI ignores player | NPC doesn't react | Detection range too small, state issue | Increase detection, fix state |

### Minor (P3/P4)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| AI jitter | NPC shakes slightly | Path smoothing issue, numerical precision | Improve smoothing, increase precision |
| AI delay | NPC reacts slowly | Update rate too low | Increase update rate |
| AI memory leak | Memory grows over time | Objects not cleaned up | Add cleanup, check references |
| AI LOD | Distant AI simplified too much | LOD distances too aggressive | Adjust LOD distances |
| AI culling | AI stops when off-screen | Frustum culling too aggressive | Adjust culling bounds |

## Evidence Collection

For each AI test:

1. **Setup** — describe AI scenario.
2. **Trigger** — what caused AI behavior.
3. **Observation** — capture AI state and actions.
4. **Path** — record movement path.
5. **Decisions** — log AI decisions.
6. **Metrics** — CPU usage, update rate.

Store evidence in `.plab/session-*/evidence/ai/`.

## Engine-Specific AI

### Unity AI (NavMesh)

```csharp
// NavMeshAgent
NavMeshAgent agent = GetComponent<NavMeshAgent>();
agent.SetDestination(targetPosition);
agent.speed = 5f;
agent.stoppingDistance = 2f;

// Path
NavMeshPath path = new NavMeshPath();
NavMesh.CalculatePath(transform.position, targetPosition, NavMesh.AllAreas, path);

// Obstacle avoidance
NavMeshObstacle obstacle = GetComponent<NavMeshObstacle>();
obstacle.carving = true;
```

### Unreal AI

```cpp
// AIController
AAIController* AIController = Cast<AAIController>(GetController());
AIController->MoveToLocation(TargetLocation);
AIController->StopMovement();

// Behavior tree
UBehaviorTree* BehaviorTree = LoadObject<UBehaviorTree>(nullptr, TEXT("/Game/AI/BehaviorTree.BehaviorTree"));
AIController->RunBehaviorTree(BehaviorTree);

// Blackboard
UBlackboardComponent* Blackboard = AIController->GetBlackboardComponent();
Blackboard->SetValueAsVector("TargetLocation", TargetLocation);
```

### Godot AI

```gdscript
# NavigationAgent
$NavigationAgent.target_position = target_position
$NavigationAgent.velocity_computed.connect(_on_velocity_computed)

func _on_velocity_computed(velocity):
    velocity = velocity.normalized() * speed
    move_and_slide()

# State machine
match current_state:
    "idle":
        # Idle behavior
    "patrol":
        # Patrol behavior
    "chase":
        # Chase behavior
```

### Generic AI

```python
# Simple state machine
class NPC:
    def __init__(self):
        self.state = "idle"
        self.target = None
    
    def update(self):
        if self.state == "idle":
            self.idle_behavior()
        elif self.state == "patrol":
            self.patrol_behavior()
        elif self.state == "chase":
            self.chase_behavior()
```

## When to Stop

Stop AI audit when:

- All AI elements tested at least once.
- All P0/P1 findings documented.
- No new findings in last 10 tests.
- Time budget exhausted (document remaining tests).
- Platform limits prevent further testing.

## Integration with Other Audits

AI audit findings may reveal issues in other dimensions:

- Pathfinding visual → visual audit
- Performance issue → performance audit
- Functional bug → functional audit
- Physics interaction → physics audit

Cross-reference findings and coordinate audits.

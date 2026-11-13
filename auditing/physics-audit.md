# PHYSICS AUDIT

Systematic verification of physics simulation correctness: collision detection, rigid body dynamics, constraints, and physics-based interactions.

## Audit Scope

Physics audit covers:

- Collision detection (static, dynamic, triggers)
- Rigid body dynamics (velocity, acceleration, forces)
- Constraints (joints, hinges, springs)
- Raycasting and shape casting
- Physics materials (friction, restitution, density)
- Physics LOD and sleeping
- Physics determinism and reproducibility
- Physics performance

## Methodology

For each physics element:

1. **Identify** — what physics behavior should occur?
2. **Set up** — create test scenario.
3. **Execute** — apply forces/inputs.
4. **Observe** — capture physics state.
5. **Verify** — compare observed vs expected.
6. **Document** — record finding if mismatch.

## Collision Detection

### Static Collision

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Wall collision | Move character into wall | Character stops, no penetration | Position before/after |
| Floor collision | Drop object onto floor | Object rests on floor | Position, velocity |
| Ceiling collision | Jump under ceiling | Object hits ceiling, stops | Position, velocity |
| Corner collision | Move into corner | Object stops at corner | Position |
| Sloped surface | Move on slope | Object slides/rolls correctly | Position, velocity |

### Dynamic Collision

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Object-object | Drop object onto another | Collision detected, response correct | Contact points, impulse |
| Moving object | Move fast object into static | Collision detected | Contact points |
| Rotating object | Spin object into wall | Collision detected | Contact points |
| Multiple objects | Stack objects | Stable stack, no interpenetration | Position, contact |

### Trigger Volumes

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Enter trigger | Move into trigger zone | Trigger event fires | Event log, state change |
| Exit trigger | Move out of trigger | Trigger event fires | Event log, state change |
| Trigger while paused | Pause game, move into trigger | Trigger still fires or correctly paused | State inspection |
| Multiple triggers | Enter multiple triggers | All triggers fire correctly | Event log |

## Rigid Body Dynamics

### Basic Motion

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Free fall | Drop object | Accelerates downward at 9.8 m/s² | Position vs time |
| Projectile | Launch object | Parabolic trajectory | Position trajectory |
| Bounce | Drop object with restitution | Bounces with correct height | Bounce height log |
| Friction | Slide object on surface | Slows down at correct rate | Velocity decay |
| Air resistance | Move object through air | Slows down | Velocity decay |

### Forces & Constraints

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Apply force | Apply impulse to object | Velocity changes correctly | Velocity before/after |
| Apply torque | Apply torque to object | Angular velocity changes | Angular velocity |
| Joint constraint | Connect two objects | Objects maintain relative position | Position tracking |
| Spring | Connect objects with spring | Oscillates correctly | Position over time |
| Hinge | Connect objects with hinge | Rotates around axis | Rotation tracking |

### Sleeping & LOD

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Object falls asleep | Let object rest | Object stops simulating | CPU usage, state |
| Object wakes up | Apply force to sleeping object | Object wakes, resumes | State change |
| Physics LOD | Many objects | Distant objects simplified | CPU usage, accuracy |

## Raycasting & Shape Casting

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Raycast forward | Cast ray forward | Hits first object | Hit point, normal |
| Raycast through wall | Cast ray through wall | Blocked by wall | Hit point on wall |
| Raycast miss | Cast ray into empty space | Returns no hit | Null result |
| Sphere cast | Cast sphere forward | Detects objects in path | Hit point, radius |
| Box cast | Cast box forward | Detects objects in path | Hit point, extents |

## Physics Materials

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Friction | Slide object on different surfaces | Different deceleration rates | Velocity decay |
| Restitution | Drop object on different surfaces | Different bounce heights | Bounce height |
| Density | Apply force to objects of different mass | Different acceleration | Acceleration |
| Bounciness | Drop object on bouncy surface | Higher bounce | Bounce height |

## Physics Determinism

| Test | Setup | Expected | Evidence |
|---|---|---|---|
| Same inputs | Run same simulation twice | Identical results | State comparison |
| Different frame rates | Run at 30fps vs 60fps | Similar results (within tolerance) | State comparison |
| Pause/resume | Pause physics, resume | Continues from same state | State comparison |
| Save/load | Save physics state, load | State preserved | State comparison |

## Physics Performance

| Metric | Target | Measurement |
|---|---|---|
| Physics step time | < 4ms (for 60fps) | `Time.fixedDeltaTime` profiling |
| Collision checks | < 1000 per frame | Collision pair count |
| Raycast count | < 100 per frame | Raycast call count |
| Sleeping objects | > 80% when idle | Active vs sleeping ratio |
| Physics memory | < 50MB | Physics engine memory usage |

## Common Physics Bugs

### Critical (P0/P1)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Tunneling | Fast objects pass through walls | Discrete collision detection | Use continuous collision detection (CCD) |
| Interpenetration | Objects overlap | Collision resolution failure | Increase solver iterations, check collision margins |
| NaN explosion | Objects fly to infinity | Division by zero, invalid math | Validate inputs, add NaN checks |
| Constraint failure | Joints break, objects separate | Constraint solver failure | Increase solver iterations, check constraint setup |
| Physics freeze | Objects stop moving | Sleeping not waking, solver stuck | Check sleep thresholds, wake conditions |

### Major (P2)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Incorrect bounce | Wrong bounce height | Restitution value wrong | Adjust restitution |
| Wrong friction | Objects slide too much/too little | Friction value wrong | Adjust friction |
| Floating point drift | Objects slowly sink/float | Integration error | Use fixed timestep, higher precision |
| Collision jitter | Objects vibrate on contact | Contact resolution instability | Increase solver iterations, adjust contact offset |
| Raycast miss | Ray passes through object | Ray too thin, collision layer wrong | Thicken ray, check layers |

### Minor (P3/P4)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Slight penetration | Objects slightly overlap | Collision margin too small | Increase collision margin |
| Delayed collision | Collision detected late | Physics update rate too low | Increase physics tick rate |
| Visual/physics mismatch | Visual position != physics position | Interpolation issue | Sync visual to physics |
| Sound sync | Collision sound late/early | Physics update timing | Sync audio to physics events |

## Evidence Collection

For each physics test:

1. **Setup** — describe test scenario.
2. **Initial state** — positions, velocities, rotations.
3. **Action** — forces applied, inputs sent.
4. **Final state** — positions, velocities, rotations.
5. **Trajectory** — position over time (if relevant).
6. **Logs** — physics engine logs, errors.

Store evidence in `.plab/session-*/evidence/physics/`.

## Engine-Specific Physics

### Unity Physics

```csharp
// Rigidbody
rb.velocity = new Vector3(0, 5, 0);
rb.AddForce(Vector3.up * 10f);
rb.isKinematic = true;

// Collision
void OnCollisionEnter(Collision collision)
{
    Debug.Log("Hit: " + collision.gameObject.name);
}

// Raycast
RaycastHit hit;
Physics.Raycast(transform.position, transform.forward, out hit, 10f);
```

### Unreal Physics

```cpp
// Line trace
FHitResult Hit;
GetWorld()->LineTraceSingleByChannel(Hit, Start, End, ECC_Visibility);

// Overlap
TArray<AActor*> OverlappingActors;
GetOverlappingActors(OverlappingActors);

// Physics body
UPrimitiveComponent* PrimComp = GetRootComponent()->GetBodyInstance();
FVector Velocity = PrimComp->GetPhysicsLinearVelocity();
```

### Godot Physics

```gdscript
# RigidBody3D
player.apply_central_impulse(Vector3(0, 5, 0))
player.linear_velocity = Vector3(0, 10, 0)

# Raycast
var space_state = get_world_3d().direct_space_state
var query = PhysicsRayQueryParameters3D.create(from, to)
var result = space_state.intersect_ray(query)
```

### Three.js Physics (Cannon.js/Ammo.js/Rapier)

```javascript
// Cannon.js
const body = new CANNON.Body({ mass: 1 });
world.addBody(body);
body.applyForce(new CANNON.Vec3(0, 10, 0));

// Ammo.js
const body = new Ammo.btRigidBody(mass, motionState, shape);
dynamicsWorld.addRigidBody(body);
body.applyCentralForce(new Ammo.btVector3(0, 10, 0));

// Rapier
world.createRigidBody(RigidBodyDesc.dynamic().setTranslation(x, y, z));
```

## When to Stop

Stop physics audit when:

- All physics elements tested at least once.
- All P0/P1 findings documented.
- No new findings in last 10 tests.
- Time budget exhausted (document remaining tests).
- Platform limits prevent further testing.

## Integration with Other Audits

Physics audit findings may reveal issues in other dimensions:

- Visual glitch → visual audit
- Performance issue → performance audit
- Animation bug → animation audit
- Functional bug → functional audit

Cross-reference findings and coordinate audits.

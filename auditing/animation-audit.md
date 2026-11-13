# ANIMATION AUDIT

Systematic verification of animation systems: character animations, skeletal animation, skeletal mesh deformation, animation blending, and animation-driven effects.

## Audit Scope

Animation audit covers:

- Skeletal animation (bones, skinning, morph targets)
- Animation state machines (transitions, blending)
- Animation events (footsteps, sounds, effects)
- Procedural animation (IK, physics-based, code-driven)
- Animation performance (skinning cost, bone count)
- Animation synchronization (audio-visual sync)
- Animation quality (smoothness, weight, timing)

## Methodology

For each animation:

1. **Identify** — what animation should play?
2. **Trigger** — cause the animation to play.
3. **Observe** — capture the animation.
4. **Verify** — compare observed vs expected.
5. **Document** — record finding if mismatch.

## Skeletal Animation

### Mesh & Rig

| Check | What to look for | Evidence |
|---|---|---|
| Skeleton structure | Bones positioned correctly, hierarchy logical | Wireframe view, bone display |
| Skin weights | Smooth deformation, no candy-wrapper artifacts | Close-up deformation |
| Bind pose | Rest pose matches mesh | Compare bind pose to mesh |
| Bone count | Reasonable for target platform | Bone count metric |
| Morph targets | Blend shapes work correctly | Morph target slider test |

### Animation Clips

| Check | What to look for | Evidence |
|---|---|---|
| Clip loading | All clips load, no missing | Console logs, clip list |
| Duration | Correct length | Frame count, time |
| Loop settings | Correct loop mode (once, loop, ping-pong) | Play clip, observe end behavior |
| Root motion | Character moves correctly with animation | Position tracking |
| Compression | No visible artifacts from compression | Compare compressed vs uncompressed |

## Animation State Machines

### State Transitions

| Check | What to look for | Evidence |
|---|---|---|
| Transition conditions | States change when conditions met | Trigger condition, observe transition |
| Transition timing | Smooth blend, no pops | Video during transition |
| Transition interruption | Can interrupt mid-transition | Trigger during transition |
| State priority | Correct state wins when multiple active | Multiple triggers, observe result |
| State exit | Clean exit, no stuck states | Complete transition, verify end state |

### Blending

| Check | What to look for | Evidence |
|---|---|---|
| Blend weights | Smooth transition between animations | Frame-by-frame analysis |
| Blend duration | Correct blend time | Time measurement |
| Blend curves | Natural easing, no linear pops | Visual inspection |
| Additive blending | Additive animations combine correctly | Layered animations |

## Animation Events

| Check | What to look for | Evidence |
|---|---|---|
| Footstep events | Sounds play at correct footfalls | Audio sync with animation |
| Effect events | Particles spawn at correct time | Visual sync |
| Sound events | Audio plays at correct time | Audio sync |
| Hit events | Damage applied at correct frame | Damage timing |
| Camera events | Camera moves at correct time | Camera tracking |

## Procedural Animation

### Inverse Kinematics (IK)

| Check | What to look for | Evidence |
|---|---|---|
| Foot placement | Feet stick to ground | Close-up foot inspection |
| Hand placement | Hands reach targets correctly | Hand target tracking |
| Look-at | Head/eyes track target | Head rotation tracking |
| Two-bone IK | Elbow/knee bend correctly | Joint angle inspection |

### Physics-Based Animation

| Check | What to look for | Evidence |
|---|---|---|
| Ragdoll | Physics simulation correct | Ragdoll simulation |
| Cloth | Cloth simulates correctly | Cloth movement |
| Hair | Hair physics correct | Hair movement |
| Secondary motion | Jiggle bones, spring bones | Bone oscillation |

### Code-Driven Animation

| Check | What to look for | Evidence |
|---|---|---|
| Procedural walk | Legs move correctly | Walk cycle inspection |
| Procedural aim | Arms point correctly | Aim direction tracking |
| Procedural breathing | Chest rises/falls | Chest movement |
| Procedural look | Head turns toward target | Head rotation |

## Animation Synchronization

### Audio-Visual Sync

| Check | What to look for | Evidence |
|---|---|---|
| Footstep sync | Foot hits ground when sound plays | Frame-by-frame analysis |
| Attack sync | Weapon swing matches sound | Visual-audio comparison |
| Dialogue sync | Lip sync matches audio | Lip movement vs audio |
| Music sync | Animation beats match music | Beat tracking |

### Multiplayer Sync

| Check | What to look for | Evidence |
|---|---|---|
| Animation replication | Other players see correct animation | Second client view |
| Latency compensation | Animations smooth despite lag | Network simulation |
| State sync | Animation state matches server | Server state comparison |

## Animation Performance

| Metric | Target | Measurement |
|---|---|---|
| Skinning cost | < 2ms per character | Profiler measurement |
| Bone count | < 100 per character | Bone count |
| Morph targets | < 10 per mesh | Morph target count |
| Animation updates | < 1ms per character | Update time |
| Draw calls | Minimize for animated objects | Draw call count |

## Common Animation Bugs

### Critical (P0/P1)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Missing animation | Character T-poses or freezes | Clip not loaded, state not set | Load clip, set state |
| Animation not playing | Static character | Animator not updating, mixer not playing | Call `mixer.update(delta)`, check action |
| Bone explosion | Mesh explodes into vertices | Corrupted skin weights, wrong bind pose | Fix skin weights, rebind |
| Animation freeze | Character stops mid-animation | State machine stuck, transition blocked | Check transition conditions |
| Root motion wrong | Character floats/flies | Root motion not extracted correctly | Fix root motion settings |

### Major (P2)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Animation popping | Sudden jumps between animations | No blend, transition too fast | Add blend, increase duration |
| Foot sliding | Feet slide on ground | Animation speed mismatch | Match animation speed to movement |
| IK failure | Limbs don't reach targets | IK solver failure, target too far | Adjust IK settings, clamp targets |
| Animation desync | Animation out of sync with audio | Timing mismatch | Sync events, adjust timing |
| Blend artifacts | Weird poses during blend | Incompatible animations | Use compatible animations, additive blending |

### Minor (P3/P4)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Slight jitter | Animation shakes slightly | Bone constraint, numerical precision | Increase solver iterations |
| Uneven timing | Animation speeds vary | Frame rate dependency | Use delta time, fixed timestep |
| Compression artifacts | Visible degradation | Over-compression | Reduce compression, increase quality |
| LOD animation | Animation quality drops at distance | LOD settings too aggressive | Adjust LOD distances |
| Animation culling | Animation stops when off-screen | Frustum culling too aggressive | Adjust culling bounds |

## Evidence Collection

For each animation test:

1. **Setup** — describe animation scenario.
2. **Trigger** — what caused animation to play.
3. **Frames** — capture key frames of animation.
4. **Video** — record full animation.
5. **State** — animation state machine state.
6. **Metrics** — skinning cost, bone count.

Store evidence in `.plab/session-*/evidence/animation/`.

## Engine-Specific Animation

### Unity Animation

```csharp
// Animator
animator.SetTrigger("Attack");
animator.SetFloat("Speed", 5f);
animator.Play("Walk");

// Animation events
void OnAnimationEvent(string eventName)
{
    Debug.Log("Animation event: " + eventName);
}

// IK
OnAnimatorIK(int layerIndex)
{
    animator.SetIKPosition(AvatarIKGoal.LeftFoot, targetPosition);
}
```

### Unreal Animation

```cpp
// AnimInstance
UAnimInstance* AnimInstance = SkelMesh->GetAnimInstance();
AnimInstance->Montage_Play(AttackMontage);
AnimInstance->SetFloat("Speed", CurrentSpeed);

// Blend space
AnimInstance->SetFloat("Direction", Direction);

// IK
void UMyAnimInstance::NativeUpdateAnimation(float DeltaSeconds)
{
    // Update IK targets
}
```

### Godot Animation

```gdscript
# AnimationPlayer
$AnimationPlayer.play("walk")
$AnimationPlayer.play_backwards("walk")
$AnimationPlayer.pause()

# AnimationTree
$AnimationTree.set("parameters/conditions/is_on_floor", true)
$AnimationTree.active = true

# Sprite animation
$AnimatedSprite.play("run")
$AnimatedSprite.frame = 5
$AnimatedSprite.stop()
```

### Three.js Animation

```javascript
// AnimationMixer
const mixer = new THREE.AnimationMixer(model);
const action = mixer.clipAction(clip);
action.play();

// Animation state
console.log("Action paused:", action.paused);
console.log("Action time:", action.time);
console.log("Action weight:", action.weight);

// List animations
model.animations.forEach(clip => {
    console.log("Clip:", clip.name, "duration:", clip.duration);
});
```

## When to Stop

Stop animation audit when:

- All animations tested at least once.
- All P0/P1 findings documented.
- No new findings in last 10 tests.
- Time budget exhausted (document remaining tests).
- Platform limits prevent further testing.

## Integration with Other Audits

Animation audit findings may reveal issues in other dimensions:

- Visual glitch → visual audit
- Physics issue → physics audit
- Audio sync → audio audit
- Performance issue → performance audit
- Functional bug → functional audit

Cross-reference findings and coordinate audits.

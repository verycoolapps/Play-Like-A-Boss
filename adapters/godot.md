# GODOT ADAPTER

Instrumentation and defect catalog for Godot 3.x and 4.x games.

## Detection

Confirm Godot usage:

```bash
# File system signals
find . -name "project.godot" -o -name "*.gd" -o -name "*.tscn" -o -name "*.tres"
find . -name "export_presets.cfg" -o -name "*.pck"

# Binary signals
file godot  # Godot binary
file game.exe  # Exported games have .pck files
ls -la *.pck  # Packed game data
```

```gdscript
// Code signals
extends Node
class_name MyScript
```

```javascript
// Runtime signals
// Godot games log to:
// Windows: %APPDATA%\Godot\app_userdata\<ProjectName>\logs\
// macOS: ~/Library/Application Support/Godot/app_userdata/<ProjectName>/logs/
// Linux: ~/.local/share/godot/app_userdata/<ProjectName>/logs/
```

## Instrumentation Options

### Option 1: Godot Editor (Best)

If you have the Godot project source:

```gdscript
# Create an autoload script for automated testing
extends Node

func _ready():
    print("Automated test starting...")
    run_tests()

func run_tests():
    # Test 1: Scene loading
    test_scene_loading()
    
    # Test 2: Player movement
    test_player_movement()
    
    # Test 3: UI interactions
    test_ui()

func test_scene_loading():
    var scene = load("res://scenes/main.tscn")
    if scene:
        print("Scene loaded successfully")
    else:
        print("ERROR: Scene failed to load")
```

**Advantages**: Full access to scene tree, nodes, signals.
**Disadvantages**: Requires Godot Editor, slower than exported build.

### Option 2: Godot Headless Mode

```bash
# Run game headless (no rendering)
godot --headless --path . --quit-after 100

# Run with script
godot --headless --path . --script res://tests/run_tests.gd

# Export and run headless
godot --headless game.pck
```

### Option 3: Godot Debugger

```bash
# Run with debugger
godot --debug --path .

# Remote debugging
godot --remote-debug tcp://localhost:6007
```

Connect with Godot editor or custom debugger client.

### Option 4: GUT (Godot Unit Test)

```gdscript
# Install GUT addon
git clone https://github.com/bitwes/Gut.git addons/gut

# Create test file
test/unit/test_player.gd:
extends GutTest

func test_player_movement():
    var player = preload("res://scenes/player.tscn").instance()
    add_child(player)
    
    # Simulate input
    Input.action_press("move_forward")
    await get_tree().process_frame
    Input.action_release("move_forward")
    
    # Verify movement
    assert_gt(player.position.z, 0, "Player should move forward")
```

Run via: `godot --headless -s addons/gut/gut_cmdln.gd`

### Option 5: Binary Analysis (No Source)

If you only have the exported game:

```bash
# Check for Godot version
strings game.pck | grep -i "godot"

# Extract pck file
godot --headless --dump-extension-api
# Or use godotpcktool

# Check for scripts
grep -r "extends Node" extracted/
```

## Key APIs

### Node & Scene Tree

```gdscript
# Get node
var player = get_node("/root/Main/Player")
var players = get_tree().get_nodes_in_group("player")

# Instantiate scene
var scene = load("res://scenes/enemy.tscn")
var enemy = scene.instance()
add_child(enemy)

# Queue free (safe delete)
enemy.queue_free()
```

### Transform

```gdscript
# Position
player.position = Vector3(0, 1, 0)
player.global_position = Vector3(10, 0, 0)

# Rotation
player.rotation_degrees = Vector3(0, 90, 0)
player.look_at(target.global_position)

# Scale
player.scale = Vector3(2, 2, 2)
```

### Physics

```gdscript
# RigidBody2D/3D
player.apply_central_impulse(Vector3(0, 5, 0))
player.linear_velocity = Vector3(0, 10, 0)

# Raycast
var space_state = get_world_3d().direct_space_state
var query = PhysicsRayQueryParameters3D.create(from, to)
var result = space_state.intersect_ray(query)
if result:
    print("Hit: ", result.collider.name)

# Collision signals
func _on_body_entered(body):
    print("Collided with: ", body.name)
```

### Animation

```gdscript
# AnimationPlayer
$AnimationPlayer.play("walk")
$AnimationPlayer.play_backwards("walk")
$AnimationPlayer.pause()

# AnimationTree
$AnimationTree.set("parameters/conditions/is_on_floor", true)
$AnimationTree.active = true

# Sprite animation (2D)
$AnimatedSprite.play("run")
$AnimatedSprite.frame = 5
$AnimatedSprite.stop()
```

### UI

```gdscript
# CanvasLayer
$CanvasLayer/Control/Button.pressed.connect(_on_button_pressed)

# Label
$CanvasLayer/Control/Label.text = "Score: " + str(score)

# TextureRect
$CanvasLayer/Control/TextureRect.texture = preload("res://textures/icon.png")
```

### Input

```gdscript
# Input actions
if Input.is_action_pressed("move_forward"):
    velocity.z = -speed

if Input.is_action_just_pressed("jump"):
    velocity.y = jump_force

# Input events
func _input(event):
    if event is InputEventKey and event.pressed:
        if event.keycode == KEY_SPACE:
            print("Space pressed")
```

### Signals

```gdscript
# Emit signal
signal health_changed(new_health)

func take_damage(amount):
    health -= amount
    emit_signal("health_changed", health)

# Connect signal
$Player.health_changed.connect(_on_health_changed)

func _on_health_changed(new_health):
    $HealthBar.value = new_health
```

## Input Simulation

### Action Map

```gdscript
# project.godot input map
[input]
move_forward={"deadzone": 0.5, "events": [Object(InputEventKey,"resource_local_to_scene":false,"resource_name":"w","device":-1)]}
```

### Simulating Input

```gdscript
# Programmatic input
Input.action_press("move_forward")
await get_tree().process_frame
Input.action_release("move_forward")

# Inject input event
var event = InputEventKey.new()
event.keycode = KEY_W
event.pressed = true
Input.parse_input_event(event)
```

## Common Defect Catalog

### Critical (P0/P1)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Null instance | Crash on play | `instance()` returns null | Check `if scene:` before instance |
| Missing node | Crash on access | Node path wrong, node deleted | Use `get_node_or_null()`, check path |
| Infinite loop | Game freezes | `while` loop without exit, `await` never returns | Add break conditions, timeout |
| Signal not connected | Button doesn't work | `connect()` not called, wrong signal | Verify signal name, check connection |
| Save corruption | Crash on load | Serialization error, version mismatch | Add version check, migration |

### Major (P2)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Animation not playing | Static character | AnimationPlayer not playing, wrong animation name | Check animation name, verify player |
| Physics tunneling | Objects pass through | High velocity, no continuous collision | Use `PhysicsServer`, lower physics tick rate |
| UI not updating | Score not changing | Label not updating, signal not firing | Update label text, check signal |
| Collision missing | Objects pass through | Collision layer wrong, shape missing | Fix collision layers, add collision shape |
| AI stuck | NPC stops moving | NavigationAgent not working, pathfinding failure | Check navmesh, debug agent |

### Minor (P3/P4)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Draw call spam | Low FPS | Too many nodes, no batching | Use MultiMesh, combine meshes |
| Memory leak | FPS degrades | Nodes not freed, signals not disconnected | Call `queue_free()`, disconnect signals |
| Texture too large | High memory | Uncompressed textures, wrong size | Compress textures, use VRAM compression |
| Shadow acne | Striped shadows | Shadow bias too low | Increase `shadow_bias` in light |
| Z-fighting | Flickering surfaces | Coplanar geometry | Offset geometry, adjust near/far |

## Log Analysis

Godot logs to:

- **Windows**: `%APPDATA%\Godot\app_userdata\<ProjectName>\logs\`
- **macOS**: `~/Library/Application Support/Godot/app_userdata/<ProjectName>/logs/`
- **Linux**: `~/.local/share/godot/app_userdata/<ProjectName>/logs/`

```bash
# Tail the log
tail -f ~/Library/Application\ Support/Godot/app_userdata/MyGame/logs/godot.log

# Search for errors
grep -i "error\|warning\|SCRIPT ERROR" ~/Library/Application\ Support/Godot/app_userdata/MyGame/logs/godot.log

# Search for specific script
grep "MyScript" ~/Library/Application\ Support/Godot/app_userdata/MyGame/logs/godot.log
```

## Console Commands

Godot has a built-in console (in editor) or debug console:

```gdscript
# Debug commands
print("Debug: Player position = ", player.position)
print_tree()  # Print scene tree
print_orphan_nodes()  # Find orphaned nodes

# Performance
Performance.get_monitor(Performance.TIME_FPS)
Performance.get_monitor(Performance.MEMORY_STATIC)
Performance.get_monitor(Performance.OBJECT_COUNT)
Performance.get_monitor(Performance.OBJECT_NODE_COUNT)
Performance.get_monitor(Performance.OBJECT_RESOURCE_COUNT)
```

## Export Considerations

When exporting Godot games:

```bash
# Export templates
# Download from https://godotengine.org/download

# Export preset
godot --headless --export-release "Windows Desktop" build/game.exe

# Export with debug
godot --headless --export-debug "Windows Desktop" build/game.exe
```

**Debug exports** include:
- Console output
- Debugger support
- Script errors with stack traces
- Performance monitors

## When Source Unavailable

If you only have the exported game:

1. **Check for debug export**: Debug exports have more logging.
2. **Extract pck**: Use godotpcktool to extract assets.
3. **Check logs**: Always check `app_userdata` for errors.
4. **Remote debugging**: If enabled, connect with Godot editor.
5. **Limitations**: Cannot modify code, only observe behavior.

## Capability Honesty

What you CAN observe with Godot:

- ✅ Scene tree, node hierarchy, properties
- ✅ Transform, physics, animation state
- ✅ UI elements, input events, signals
- ✅ Console logs, errors, warnings
- ✅ Performance monitors (FPS, memory, object counts)
- ✅ Asset references, script structure

What you CANNOT observe without source:

- ❌ GDScript logic internals (unless decompiled)
- ❌ C# logic internals (if using C#)
- ❌ Network internals (unless intercepted)
- ❌ Editor-only features (unless in debug export)

Document limitations in audit report.

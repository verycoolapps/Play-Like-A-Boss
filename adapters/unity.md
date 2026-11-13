# UNITY ADAPTER

Instrumentation and defect catalog for Unity games (2019+, including Unity 6 / Unity 2023).

## Detection

Confirm Unity usage:

```bash
# File system signals
find . -name "*.csproj" -o -name "*.sln" -o -name "ProjectSettings" -type d
find . -name "*.unity" -o -name "*.prefab" -o -name "*.asset"

# Binary signals
file game.exe  # Unity games often have UnityPlayer.dll
ls -la *_Data/  # Unity data folder
```

```csharp
// Code signals
using UnityEngine;
public class MyScript : MonoBehaviour { }
```

```javascript
// Runtime signals
// Unity games log to %LOCALAPPDATA%/Unity/Editor/Player.log (Windows)
// or ~/Library/Logs/Unity/Player.log (macOS)
// or ~/.config/unity3d/Player.log (Linux)
```

## Instrumentation Options

### Option 1: Unity Editor Play Mode (Best)

If you have the Unity project source:

```csharp
// Create an Editor script for automated testing
using UnityEngine;
using UnityEditor;
using UnityEditor.SceneManagement;

public class AutomatedPlaytest : EditorWindow
{
    [MenuItem("Tools/Run Automated Playtest")]
    static void RunPlaytest()
    {
        // Open scene
        EditorSceneManager.OpenScene("Assets/Scenes/Main.unity");
        
        // Enter play mode
        EditorApplication.EnterPlaymode();
        
        // Wait for play mode
        EditorApplication.delayCall += () =>
        {
            // Run test logic
            var testRunner = new PlayModeTestRunner();
            testRunner.RunTests();
        };
    }
}
```

**Advantages**: Full access to scene, objects, physics, animation.
**Disadvantages**: Requires Unity Editor, slower than standalone.

### Option 2: Unity Test Framework (UTF)

```csharp
using UnityEngine;
using UnityEngine.TestTools;
using NUnit.Framework;
using System.Collections;

public class GameplayTests
{
    [UnityTest]
    public IEnumerator PlayerCanMove()
    {
        // Spawn player
        var player = GameObject.Find("Player");
        Assert.IsNotNull(player);
        
        // Simulate input
        var input = player.GetComponent<PlayerInput>();
        input.SimulateKeyPress(KeyCode.W);
        
        // Wait for movement
        yield return new WaitForSeconds(0.5f);
        
        // Verify position changed
        var pos = player.transform.position;
        Assert.Greater(pos.z, 0);
    }
    
    [UnityTest]
    public IEnumerator GameDoesNotCrashOnLoad()
    {
        // Load main scene
        SceneManager.LoadScene("Main");
        yield return new WaitForSeconds(1f);
        
        // Verify no errors
        Assert.IsNull(GameObject.Find("ErrorHandler"));
    }
}
```

Run via: `Unity.exe -runTests -batchmode -projectPath . -testResults results.xml`

### Option 3: Unity Profiler (Build)

For standalone builds:

```bash
# Windows
Game.exe -profiler-enable -profiler-log-file profiler.raw

# macOS
./Game.app/Contents/MacOS/Game -profiler-enable

# Linux
./Game.x86_64 -profiler-enable
```

Connect Unity Profiler to analyze:
- CPU usage per frame
- Memory allocations
- Draw calls
- Physics performance
- Animation cost

### Option 4: Unity Remote (Device Testing)

For mobile/console:

```bash
# Build with development flag
Unity.exe -buildTarget Android -buildOptions Development

# Connect via Unity Remote or Profiler
```

### Option 5: Binary Analysis (No Source)

If you only have the compiled game:

```bash
# Check for Unity version
strings Game.exe | grep -i "unity"

# Check for managed DLLs
ls *_Data/Managed/*.dll

# Use dnSpy/ILSpy to decompile
# Look for MonoBehaviour classes, game logic
```

## Key APIs

### GameObject & Components

```csharp
// Find objects
var player = GameObject.Find("Player");
var players = GameObject.FindGameObjectsWithTag("Player");
var camera = Camera.main;

// Get components
var rb = player.GetComponent<Rigidbody>();
var animator = player.GetComponent<Animator>();
var script = player.GetComponent<MyScript>();

// Transform
player.transform.position = new Vector3(0, 1, 0);
player.transform.rotation = Quaternion.Euler(0, 90, 0);
```

### Physics

```csharp
// Rigidbody
rb.velocity = new Vector3(0, 5, 0);
rb.AddForce(Vector3.up * 10f);
rb.isKinematic = true;

// Raycast
RaycastHit hit;
if (Physics.Raycast(transform.position, transform.forward, out hit, 10f))
{
    Debug.Log("Hit: " + hit.collider.name);
}

// Collision
void OnCollisionEnter(Collision collision)
{
    Debug.Log("Collided with: " + collision.gameObject.name);
}
```

### Animation

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
```

### UI

```csharp
// Canvas
var canvas = FindObjectOfType<Canvas>();
var button = canvas.GetComponentInChildren<Button>();
button.onClick.AddListener(() => Debug.Log("Clicked"));

// Text
var text = canvas.GetComponentInChildren<Text>();
text.text = "Score: " + score;
```

### Coroutines

```csharp
IEnumerator DelayedAction()
{
    yield return new WaitForSeconds(1f);
    Debug.Log("1 second passed");
}

// Start coroutine
StartCoroutine(DelayedAction());
```

## Input Simulation

### Unity Input System (New)

```csharp
using UnityEngine.InputSystem;

// Simulate keyboard
Keyboard.current.wKey.isPressed = true;

// Simulate mouse
Mouse.current.position.ReadValue();
Mouse.current.leftButton.wasPressedThisFrame;

// Simulate gamepad
Gamepad.current.leftStick.ReadValue();
Gamepad.current.aButton.wasPressedThisFrame;
```

### Legacy Input

```csharp
// Keyboard
Input.GetKey(KeyCode.W);
Input.GetKeyDown(KeyCode.Space);

// Mouse
Input.GetMouseButton(0);
Input.mousePosition;

// Axis
Input.GetAxis("Horizontal");
Input.GetAxis("Vertical");
```

## Common Defect Catalog

### Critical (P0/P1)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| NullReferenceException | Crash on play | Missing reference, destroyed object | Add null checks, fix references |
| Missing prefab | Object not spawning | Prefab not assigned, wrong path | Fix prefab reference, check Resources folder |
| Physics tunneling | Objects pass through walls | High velocity, no continuous collision | Use `Rigidbody.interpolation`, `Physics.autoSyncTransforms` |
| Infinite loop | Game freezes | While loop without exit, coroutine never ends | Add break conditions, timeout |
| Save corruption | Crash on load | Serialization error, version mismatch | Add migration, version check |

### Major (P2)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Animation not playing | Static character | Animator not set up, clip missing | Check Animator Controller, clip references |
| UI not updating | Score/lives not changing | Text not updating, event not firing | Call `text.text = value`, check events |
| Camera issues | Wrong view, clipping | Camera not positioned, near/far wrong | Fix transform, adjust clip planes |
| Audio not playing | No sound | AudioSource missing, clip not assigned | Add AudioSource, assign clip |
| Collision missing | Objects pass through | Collider missing, layer wrong | Add collider, fix layer mask |

### Minor (P3/P4)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Draw call spam | Low FPS | Too many materials, no batching | Use static batching, combine meshes |
| Memory leak | FPS degrades | Objects not destroyed, events not unsubscribed | Call `Destroy()`, `OnDestroy()` cleanup |
| Texture too large | High memory | Uncompressed textures, wrong size | Compress textures, use mipmaps |
| Shadow acne | Striped shadows | Shadow bias too low | Increase `shadowBias` in light |
| Z-fighting | Flickering surfaces | Coplanar geometry | Offset geometry, adjust near/far |

## Player Log Analysis

Unity writes logs to:

- **Windows**: `%LOCALAPPDATA%\Unity\Editor\Player.log`
- **macOS**: `~/Library/Logs/Unity/Player.log`
- **Linux**: `~/.config/unity3d/Player.log`

```bash
# Tail the log
tail -f ~/Library/Logs/Unity/Player.log

# Search for errors
grep -i "error\|exception\|warning" ~/Library/Logs/Unity/Player.log

# Search for specific script
grep "MyScript" ~/Library/Logs/Unity/Player.log
```

## Development Build Flags

For builds with development features:

```bash
# Windows
Game.exe -force-d3d11 -force-glcore -screen-fullscreen 0

# With profiler
Game.exe -profiler-enable -profiler-log-file profiler.raw

# With debug
Game.exe -debug -development
```

## When Source Unavailable

If you only have the compiled game:

1. **Decompile**: Use dnSpy/ILSpy to inspect C# code.
2. **Check DLLs**: `ls *_Data/Managed/*.dll` for game logic.
3. **Runtime inspection**: Use Unity's remote profiler if enabled.
4. **Asset extraction**: Use AssetStudio to extract assets.
5. **Limitations**: Cannot modify code, only observe behavior.

## Capability Honesty

What you CAN observe with Unity:

- ✅ Scene hierarchy, GameObjects, components
- ✅ Transform, physics, animation state
- ✅ UI elements, input events
- ✅ Console logs, errors, warnings
- ✅ Profiler data (CPU, memory, draw calls)
- ✅ Asset references, prefab structure

What you CANNOT observe without source:

- ❌ Game logic internals (unless decompiled)
- ❌ Exact script behavior (unless decompiled)
- ❌ Editor-only features (unless in development build)
- ❌ Network internals (unless intercepted)

Document limitations in audit report.

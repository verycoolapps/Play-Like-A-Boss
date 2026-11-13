# UNIVERSAL ENGINE DETECTION

How to identify what engine built the game and select the right adapter. Detection is the first step of Phase 2 (Environment Recon).

## Detection Strategy

Work from the outside in. Check the most reliable signals first, fall back to heuristics.

### Signal Priority

1. **Project files** — `package.json`, `project.godot`, `*.uproject`, `Game.rgss*`, `*.unity`, `*.sln`, `CMakeLists.txt`, `Makefile`, `Cargo.toml`, `go.mod`.
2. **Build artifacts** — executable names, DLL names, asset file formats.
3. **Runtime behavior** — console output, error messages, URL patterns, window titles.
4. **Code inspection** — imports, namespaces, class names, file extensions.
5. **Visual inspection** — UI style, rendering artifacts, asset formats.

## Detection Table

| Engine | Primary signal | Secondary signals | Adapter |
|---|---|---|---|
| Three.js | `import * as THREE` / `THREE.` in JS | `package.json` has `three` dep, WebGL canvas, `renderer.info` | `adapters/threejs.md` |
| Babylon.js | `import * as BABYLON` / `BABYLON.` | `package.json` has `@babylonjs/*` deps, `Engine` class | `adapters/web-engines.md` |
| PlayCanvas | `pc.` namespace, `pc.Application` | `package.json` has `playcanvas`, `.pcproj` files | `adapters/web-engines.md` |
| Phaser | `Phaser.` namespace, `Phaser.Game` | `package.json` has `phaser` dep, `Phaser.AUTO` | `adapters/web-engines.md` |
| PixiJS | `PIXI.` namespace, `PIXI.Application` | `package.json` has `pixi.js` dep | `adapters/web-engines.md` |
| A-Frame | `<a-scene>` HTML tag, `AFRAME.` | `package.json` has `aframe` dep, WebVR/WebXR | `adapters/web-engines.md` |
| Unity | `*.csproj`, `Assets/`, `ProjectSettings/` | `UnityEngine` namespace, `MonoBehaviour`, `Player.log` | `adapters/unity.md` |
| Unreal | `*.uproject`, `*.uplugin`, `Binaries/` | `UE4`/`UE5` in logs, `UObject`, `AActor` | `adapters/unreal.md` |
| Godot | `project.godot`, `*.gd`, `*.tscn`, `*.tres` | `GDScript`, `Node`, `SceneTree`, `godot` binary | `adapters/godot.md` |
| RPG Maker MV/MZ | `Game.rgss*.js`, `www/` folder, `nw.exe` | `RPGMV`/`RPGMZ` in code, `Data/*.json` | `adapters/rpg-maker.md` |
| GameMaker | `*.win`, `*.yydebug`, `data.win` | `GameMaker` in exe, `GM8`/`YYC` | `adapters/generic-engine.md` |
| Construct | `*.c2runtime.js`, `data.json`, `c2runtime` | `C2` namespace, `Construct` in logs | `adapters/web-engines.md` |
| Bevy | `Cargo.toml` with `bevy` dep | `bevy` in binary, `winit`/`wgpu` | `adapters/generic-engine.md` |
| Raylib | `raylib` in `Cargo.toml`/`Makefile`/`CMakeLists` | `raylib` lib, `RLGL` | `adapters/generic-engine.md` |
| Pygame | `import pygame` | `pygame` in Python, `SDL` | `adapters/generic-engine.md` |
| MonoGame | `*.csproj` with `MonoGame.Framework` | `MonoGame` in deps | `adapters/generic-engine.md` |
| Love2D | `main.lua`, `conf.lua` | `love.` namespace | `adapters/generic-engine.md` |
| Electron | `electron` in `package.json`, `main.js` | `Electron` in process name, `app.asar` | `adapters/generic-engine.md` |
| Native (unknown) | Executable, no clear signals | Process inspection, strings, imports | `adapters/generic-engine.md` |

## Detection Procedure

```
1. LIST project root
   ├── package.json? → check dependencies for engine names
   ├── project.godot? → GODOT
   ├── *.uproject? → UNREAL
   ├── *.csproj + Assets/ + ProjectSettings/? → UNITY
   ├── Game.rgss*.js? → RPG MAKER
   ├── Cargo.toml? → check for bevy/raylib
   ├── *.sln? → check project types (Unity, MonoGame, custom)
   └── Makefile/CMakeLists.txt? → check for raylib, SDL, etc.

2. INSPECT build artifacts
   ├── Executable name → hints (e.g., "game.exe" vs "UnityPlayer.dll")
   ├── DLL/SO/DYLIB names → engine runtime libraries
   ├── Asset formats → .unity3d, .pak, .pck, .rgss*, .wad
   └── Archive structure → .app, .asar, .jar, .zip

3. RUN the game (if possible)
   ├── Console output → engine banners, version strings
   ├── Window title → often contains engine name
   ├── Error messages → reveal internal APIs
   └── URL patterns → web games show framework in URLs

4. INSPECT code (if source available)
   ├── Imports/namespaces → definitive engine identification
   ├── File extensions → .gd (Godot), .cs (Unity/C#), .lua (Love2D)
   ├── Directory structure → Assets/, src/, Scripts/, etc.
   └── Config files → engine-specific settings

5. FALLBACK: GENERIC
   └── If no engine identified, use generic adapter + capability ladder
```

## Capability Ladder

Every adapter exposes a capability set. When the ideal instrumentation is unavailable, descend the ladder:

| Level | Capability | Examples | Coverage |
|---|---|---|---|
| 1 | Native instrumentation | Engine debug API, profiler, console commands | Full — all subsystems |
| 2 | Debug interfaces | Remote debugging, test frameworks, automation APIs | High — most subsystems |
| 3 | Browser automation | Playwright, Puppeteer, CDP, JS injection | Medium — web games only |
| 4 | GUI automation | pyautogui, xdotool, AppleScript, AutoHotkey | Medium — any desktop game |
| 5 | Computer vision | Screenshot analysis, OCR, template matching | Low — visual only |
| 6 | Screenshot only | Periodic captures, manual review | Minimal — visual artifacts only |
| 7 | Input simulation | Keyboard/mouse/controller injection | Minimal — play only |
| 8 | Human-assisted | Instructions for human to perform actions | Fallback — human reports results |

**Rule**: Always use the highest level available. Document when you descend. Never claim coverage you don't have.

## Adapter Selection

Once engine is detected:

1. **Exact match** — use the specific adapter (`threejs.md`, `unity.md`, etc.).
2. **Family match** — use the family adapter (`web-engines.md` for Babylon/Phaser, `generic-engine.md` for frameworks).
3. **Generic fallback** — use `generic-engine.md` with the capability ladder.

## Capability Matrix

| Engine | Native debug | Test framework | Remote debugging | Console access | Profiler | Memory access |
|---|---|---|---|---|---|---|
| Three.js | `renderer.info`, console | Manual/Playwright | Chrome DevTools | `console.log` | `renderer.info` | JS heap |
| Babylon | `engine.getFps()`, inspector | Manual/Playwright | Chrome DevTools | `console.log` | `engine` stats | JS heap |
| Phaser | `game.loop`, debug | Manual/Playwright | Chrome DevTools | `console.log` | `game.loop` | JS heap |
| PixiJS | `app.renderer`, stats | Manual/Playwright | Chrome DevTools | `console.log` | `renderer` stats | JS heap |
| Unity | Profiler, Test Framework | UTF, PlayMode tests | Unity Profiler | `Debug.Log` | Unity Profiler | Managed heap |
| Unreal | Unreal Insights, automation | Functional tests, Gauntlet | Unreal Insights | `UE_LOG` | Unreal Insights | Native heap |
| Godot | Debugger, profiler | GUT, custom | Godot debugger | `print()` | Godot profiler | Managed/native |
| RPG Maker | Plugin API, console | Plugin-based | NW.js DevTools | `console.log` | Limited | JS heap |
| Generic | Process inspection | Manual | Varies | Varies | OS tools | Limited |

## Graceful Degradation Examples

### Three.js game, no source access

- **Level 3**: Playwright + Chrome DevTools → inject JS to access `window.game`, `renderer.info`, `scene`.
- **Level 4**: pyautogui + screenshots → play by vision, capture artifacts.
- **Level 5**: Screenshot + OCR → read UI text, detect visual bugs.
- **Level 7**: Keyboard/mouse injection → play blind, log inputs.

### Unity game, no source access

- **Level 2**: Unity Test Framework if accessible, or Unity's `-batchmode` automation.
- **Level 4**: GUI automation → play by screen, capture logs from `%LOCALAPPDATA%`.
- **Level 5**: Screenshot + OCR → visual audit only.
- **Level 7**: Input injection → play blind.

### Mobile game, no root

- **Level 4**: ADB input injection + `adb shell screencap` → play and observe.
- **Level 5**: Screenshot analysis → visual bugs only.
- **Level 8**: Human-assisted → user plays, reports issues.

## Detection Validation

After detection, validate:

1. **Does the adapter exist?** — check `adapters/` directory.
2. **Does it match reality?** — does the game behave as expected for that engine?
3. **What capabilities are available?** — test each capability level.
4. **What's the fallback?** — if primary adapter fails, what's next?

Document detection results in `.plab/session-*/config.json`:

```json
{
  "engine": "threejs",
  "adapter": "adapters/threejs.md",
  "capabilities": {
    "native_instrumentation": true,
    "debug_interface": true,
    "browser_automation": true,
    "gui_automation": true,
    "cv": true,
    "screenshot": true,
    "input_sim": true,
    "human_assisted": true
  },
  "detection_confidence": "high",
  "detection_method": "package.json + code inspection"
}
```

## When Detection Fails

If you cannot identify the engine:

1. **Check runtime behavior** — console output, logs, error messages.
2. **Check file signatures** — magic bytes, archive formats.
3. **Check strings** — `strings` on binary, grep for engine names.
4. **Check network** — URLs, API endpoints, CDN patterns.
5. **Check dependencies** — `ldd`, `otool -L`, `dumpbin /dependents`.
6. **Check documentation** — if the game has docs, they may mention the engine.
7. **Ask the user** — "What engine is this built with?" is a valid question.

If all fails, use `generic-engine.md` and document the uncertainty.

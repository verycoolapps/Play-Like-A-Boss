# AUTONOMOUS GAMEPLAY

How to actually launch, control, and play the game without a human at the keyboard. This module covers the mechanics of getting input into the game and getting state out of it.

## Launch Intelligence

Before you can play, you must launch. Launch is not trivial — it is a subsystem with its own failure modes.

### Pre-Launch Checklist

1. **Verify build artifacts** — the executable/package/URL exists and is current.
2. **Check dependencies** — runtime, drivers, platform requirements.
3. **Isolate the environment** — clean profile, fresh save, no leftover state.
4. **Capture baseline** — system specs, GPU/CPU, OS version, display settings.
5. **Set up observation** — console capture, log capture, screenshot loop, metric polling.

### Launch Methods by Platform

| Platform | Method | Notes |
|---|---|---|
| Web (local) | `npm run dev` / `vite` / `serve` / `python -m http.server` | Watch for port conflicts, CORS, mixed content |
| Web (hosted) | Direct URL | May have auth, rate limits, CDN caching |
| Unity | Editor Play mode / Build executable | `-batchmode` for headless, `-nographics` for no-render |
| Unreal | Editor PIE / Packaged build | `-nullrhi` for headless, automation flags |
| Godot | `godot --headless` / editor / export | `--script` for automation, `--quit-after` for timed runs |
| RPG Maker | `nw.exe` / browser / NW.js | Plugin injection via `nw.Window` |
| Native desktop | Direct executable | Wine/Proton for non-native, sandboxed if needed |
| Mobile | Emulator / device farm | ADB for Android, simctl for iOS, limited instrumentation |
| Emulator (retro) | libretro frontend / standalone | Input via controller mapping, save states |

### Launch Failure Modes

| Failure | Detection | Recovery |
|---|---|---|
| Crash on launch | Process exits, no window | Check logs, dependencies, try safe mode |
| Black screen | Window opens, no render | GPU drivers, WebGL context, shader compile |
| Infinite loading | Progress bar stuck | Network assets, code errors, deadlock |
| Resolution/window issues | Wrong size, off-screen | Display settings, DPI scaling, fullscreen flags |
| Audio crash | No sound, or crash on audio init | Audio driver, sample rate, device selection |
| Save corruption | Crash on load | Fresh profile, verify save path, check permissions |

## Input Simulation

The quality of your play depends on the quality of your input. Bad input = bad coverage.

### Keyboard

- **OS-level**: `osascript` (macOS), `xdotool` (Linux), `SendKeys` (Windows), `pynput` (cross-platform).
- **Browser-level**: `page.keyboard` (Playwright), `Input.dispatchKeyEvent` (CDP), synthetic `KeyboardEvent`.
- **Engine-level**: Unity `Input.GetKey`, Unreal `APlayerController::InputKey`, Godot `Input.parse_input_event`.
- **Direct injection**: For games with debug consoles or automation APIs, inject at the engine level for reliability.

Key principles:

- **Human-like timing** — randomize delays between 80–200ms for normal play, 30–80ms for speedruns.
- **Key rollover** — don't assume all keys register simultaneously; stagger complex inputs.
- **Modifier keys** — Ctrl/Shift/Alt often change behavior; test combinations.
- **Held vs tapped** — some games distinguish tap, hold, and release; test all three.
- **Repeat rate** — holding a key may auto-repeat; test both held and repeated presses.

### Mouse

- **Movement**: relative vs absolute, sensitivity, acceleration curves.
- **Buttons**: left, right, middle, back, forward, wheel up/down.
- **Position**: cursor position matters for UI, raycasting, drag operations.
- **Context**: mouse over UI vs world vs menu changes behavior.

Browser: `page.mouse`. Desktop: `pyautogui`, `xdotool`, OS APIs.

### Gamepad / Controller

- **Standard mapping**: A/B/X/Y, shoulders, triggers, sticks, d-pad, start/select.
- **Analog vs digital**: sticks have analog values; triggers have pressure.
- **Dead zones**: small stick movements may be ignored; test thresholds.
- **Vibration**: haptic feedback may indicate state; capture if observable.

Tools: `SDL2` gamepad API, `xinput` (Windows), `evdev` (Linux), browser `Gamepad API`.

### Touch

- **Tap, swipe, pinch, long-press, multi-touch.**
- **Gesture recognition**: engine-specific; may differ from native touch.
- **Viewport vs screen**: touch coordinates vs render coordinates.
- **Multi-touch**: two-finger gestures, palm rejection.

Tools: `adb shell input` (Android), `xcrun simctl` (iOS), browser `Touch Events`, engine touch APIs.

### Hybrid Input

Many games mix input types:

- Keyboard + mouse (PC default)
- Gamepad only (console)
- Touch only (mobile)
- Keyboard + touch (tablet/desktop hybrid)
- Motion controls (mobile/VR)

Detect the active input mode and adapt. Some games switch modes dynamically (e.g., pause menu opens with mouse while game uses gamepad).

## Human-Like Action Sequencing

Raw input injection produces robotic play. Human-like play requires:

### Timing Variation

- **Reaction time**: 150–300ms for normal play, 80–150ms for speedrun.
- **Action duration**: hold buttons for realistic durations, not minimum frames.
- **Pauses**: humans pause between actions; add 200–800ms gaps.
- **Rhythm**: some games have rhythm elements; match tempo.

### Context Awareness

- **Read the screen**: wait for animations, dialogue, transitions before acting.
- **Anticipate**: don't spam inputs; wait for the game to be ready.
- **Recover**: after death/failure, pause, assess, retry — don't instantly respawn.
- **Explore**: look around, check UI, read tooltips before committing.

### Error Injection

Deliberately make mistakes to test recovery:

- Wrong menu selections, cancelled dialogs.
- Missed jumps, failed combat, wrong puzzle solutions.
- Premature inputs, late inputs, double inputs.
- Disconnect/reconnect mid-action.

### State Verification

After every action, verify the expected state change:

- Did the character move?
- Did the UI update?
- Did the game respond?
- Did anything unexpected happen?

If not, log it, investigate, retry or escalate.

## Objective Tracking

Maintain a live objective stack (see `core/game-intelligence.md` for details). During play:

1. **Current objective** — what is the game telling you to do?
2. **Progress markers** — how close are you? What's left?
3. **Optional objectives** — side quests, collectibles, secrets.
4. **Blocked states** — what is preventing progress?

Update after every meaningful action. If objectives become unclear, that's a finding.

## Observation During Play

While playing, continuously capture:

- **Screen**: periodic screenshots (every 5–10s or on state change).
- **Logs**: console output, error logs, debug output.
- **Metrics**: FPS, memory, draw calls, physics state.
- **Input**: what you sent, when, and what happened.
- **State**: game state variables, if accessible.

This data feeds the audit phases. Playing without observation is just playing.

## When Automation Fails

Some games resist automation:

- **Anti-cheat**: detects synthetic input, blocks automation.
- **Hardware requirements**: needs real controller, camera, microphone.
- **DRM/always-online**: requires authentication, server validation.
- **Exotic input**: motion controls, gesture recognition, biometric.

When this happens:

1. **Attempt workaround**: different input method, timing, tool.
2. **Document limitation**: record exactly what failed and why.
3. **Human-assisted fallback**: hand off to human with exact instructions.
4. **Partial coverage**: audit what you can, mark the rest UNREACHABLE.

Never fake coverage. If you can't play it, say so.

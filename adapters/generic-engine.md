# GENERIC ENGINE ADAPTER

Fallback adapter for any game engine or framework not covered by specific adapters. Uses the capability ladder to descend from native instrumentation to human-assisted play.

## When to Use

- Engine not in detection table (Bevy, Raylib, Pygame, MonoGame, Love2D, custom engines).
- Native desktop/mobile builds without source access.
- Console games (via emulator).
- Games with heavy obfuscation or anti-tampering.
- Any game where specific adapter fails.

## Detection

### File System Signals

```bash
# Project files
ls package.json Cargo.toml go.mod Makefile CMakeLists.txt *.sln *.csproj *.xcworkspace *.uproject project.godot

# Build artifacts
file game.exe game.app game.x86_64 game.pck *.dll *.so *.dylib

# Asset formats
find . -name "*.unity3d" -o -name "*.pak" -o -name "*.pck" -o -name "*.wad" -o -name "*.assets" -o -name "*.bundle"
```

### Runtime Signals

```bash
# Process inspection
ps aux | grep -i game

# Window title
# Varies by OS — check active window

# Console output
tail -f /var/log/game.log  # if logging enabled

# Network traffic
# Check for game server connections
```

### Code Signals (if source available)

```python
# Python
import pygame  # Pygame
import arcade   # Arcade

# Rust
// bevy = "0.12"  # Bevy
// macroquad = "0.4"  # Macroquad

# Go
// ebiten.org/ebiten  # Ebiten

# C/C++
// raylib.h, SDL.h, glfw3.h, allegro5

# C#
// MonoGame.Framework, Silk.NET, OpenTK
```

## Capability Ladder (Generic)

### Level 1: Native Instrumentation

**When**: Source code available, engine exposes debug API.

**Examples**:

```python
# Pygame debug overlay
import pygame
def debug_overlay(screen, fps, memory):
    font = pygame.font.Font(None, 30)
    text = font.render(f"FPS: {fps} | MEM: {memory}", True, (255,255,255))
    screen.blit(text, (10, 10))

# Bevy debug
// bevy::diagnostic::FrameTimeDiagnosticsPlugin
// bevy::pbr::wireframe::WireframePlugin

# Raylib debug
// TraceLog(LOG_INFO, "FPS: %d", GetFPS());
// DrawFPS(10, 10);
```

### Level 2: Debug Interfaces

**When**: Engine has built-in debugger or test framework.

**Examples**:

```bash
# GDB for native games
gdb ./game
(gdb) break main
(gdb) run
(gdb) info registers
(gdb) bt  # backtrace

# LLDB for macOS
debugserver localhost:1234
lldb -o "platform select remote darwin" -o "platform connect connect://localhost:1234"

# Godot debugger
# Connect via Godot editor remote debugging

# Unity debugger
# Attach via Visual Studio or Rider
```

### Level 3: Browser Automation

**When**: Web-based game (HTML5, WebGL, WebAssembly).

**Tools**: Playwright, Puppeteer, Selenium, Cypress.

```javascript
const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    
    // Capture console
    page.on('console', msg => console.log('Browser:', msg.text()));
    
    // Capture errors
    page.on('pageerror', error => console.log('Page error:', error.message));
    
    // Navigate
    await page.goto('http://localhost:8000');
    
    // Wait for game canvas
    await page.waitForSelector('canvas');
    
    // Screenshot
    await page.screenshot({ path: 'game.png' });
    
    // Simulate input
    await page.keyboard.press('ArrowRight');
    await page.mouse.click(100, 100);
    
    // Evaluate JavaScript
    const state = await page.evaluate(() => {
        return window.game ? window.game.getState() : null;
    });
    
    await browser.close();
})();
```

### Level 4: GUI Automation

**When**: Desktop game, no source access, no debug interface.

**Tools**: pyautogui, xdotool, AppleScript, AutoHotkey, SikuliX.

```python
import pyautogui
import time

# Find game window
window = pyautogui.getWindowsWithTitle('Game Title')[0]
window.activate()

# Take screenshot
screenshot = pyautogui.screenshot()
screenshot.save('game.png')

# Click button
pyautogui.click(100, 100)

# Type text
pyautogui.typewrite('hello')

# Press key
pyautogui.press('space')

# Drag
pyautogui.dragTo(200, 200, duration=1)
```

```bash
# xdotool (Linux)
xdotool search --name "Game Title" windowactivate
xdotool mousemove 100 100 click 1
xdotool key space

# AppleScript (macOS)
osascript -e 'tell application "System Events" to tell process "Game" to keystroke space'

# AutoHotkey (Windows)
Send {Space}
Click 100, 100
```

### Level 5: Computer Vision

**When**: Need to "see" the game state visually.

**Tools**: OpenCV, Tesseract OCR, template matching, ML models.

```python
import cv2
import numpy as np

# Capture screen
screenshot = pyautogui.screenshot()
img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Template matching
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
if max_val > 0.8:
    print(f"Found template at {max_loc}")

# OCR
import pytesseract
text = pytesseract.image_to_string(img)
print("Screen text:", text)

# Color detection
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))  # Red
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    if cv2.contourArea(contour) > 100:
        x, y, w, h = cv2.boundingRect(contour)
        print(f"Red object at ({x}, {y}, {w}, {h})")
```

### Level 6: Screenshot Only

**When**: Minimal automation, manual review.

**Process**:

1. Take periodic screenshots (every 5–10 seconds).
2. Review manually or with OCR.
3. Log visual anomalies.
4. No input simulation — observe only.

```python
import pyautogui
import time

for i in range(60):  # 10 minutes
    screenshot = pyautogui.screenshot()
    screenshot.save(f'screenshot_{i:03d}.png')
    time.sleep(10)
```

### Level 7: Input Simulation Only

**When**: Play blind, no observation.

**Process**:

1. Send inputs via keyboard/mouse/controller.
2. Log what was sent and when.
3. No verification — trust the input.
4. Capture logs if available.

```python
import pyautogui
import time

# Play sequence
for i in range(100):
    pyautogui.press('space')  # Jump
    time.sleep(0.5)
    pyautogui.press('right')  # Move right
    time.sleep(0.5)
```

### Level 8: Human-Assisted

**When**: All automation fails.

**Process**:

1. Provide human with exact instructions.
2. Human performs actions.
3. Human reports results.
4. Document as manual test.

```
INSTRUCTIONS FOR HUMAN TESTER:
1. Launch the game.
2. Press Start.
3. Navigate to Level 1.
4. Try to jump over the gap at coordinates (100, 200).
5. Report: Did you make it? Any errors?
6. Try to enter the door at (300, 400).
7. Report: Did the door open? Any issues?
```

## Input Methods

### Keyboard

```python
# Python
import pyautogui
pyautogui.press('space')
pyautogui.keyDown('w')
pyautogui.keyUp('w')
pyautogui.typewrite('hello')

# JavaScript (browser)
window.dispatchEvent(new KeyboardEvent('keydown', {key: 'w'}));

# C# (Unity)
Input.GetKeyDown(KeyCode.W);

# C++ (native)
// SendInput, XTest, etc.
```

### Mouse

```python
# Python
pyautogui.click(100, 100)
pyautogui.rightClick(100, 100)
pyautogui.doubleClick(100, 100)
pyautogui.moveTo(200, 200, duration=1)
pyautogui.dragTo(300, 300, duration=1)
pyautogui.scroll(10)

# JavaScript (browser)
canvas.dispatchEvent(new MouseEvent('click', {clientX: 100, clientY: 100}));
```

### Gamepad

```python
# Python (pygame)
import pygame
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Read input
x = joystick.get_axis(0)
y = joystick.get_axis(1)
button_a = joystick.get_button(0)
```

```bash
# Linux (evdev)
cat /dev/input/event0 | hexdump -C

# Windows (XInput)
# Use XInputGetState via ctypes or library
```

### Touch

```python
# Android (adb)
adb shell input tap 100 100
adb shell input swipe 100 100 200 200 500
adb shell input keyevent 4  # Back button

# iOS (simctl)
xcrun simctl io booted screenshot screenshot.png
xcrun simctl io booted recordVideo video.mp4
```

## Observation Methods

### Screen Capture

```python
# Python
import pyautogui
screenshot = pyautogui.screenshot()
screenshot.save('screen.png')

# Specific region
screenshot = pyautogui.screenshot(region=(0, 0, 800, 600))

# Multi-monitor
screenshot = pyautogui.screenshot(all_screens=True)
```

```bash
# Linux (scrot)
scrot screenshot.png

# macOS (screencapture)
screencapture -x screenshot.png

# Windows (PowerShell)
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Screen]::PrimaryScreen.Bounds
```

### Log Capture

```bash
# Tail log file
tail -f /path/to/game.log

# Follow with grep
tail -f game.log | grep -i error

# Capture stderr
./game 2>&1 | tee game.log

# Windows Event Log
wevtutil qe Application /q:"*[System[Provider[@Name='Game']]]" /f:text
```

### Process Monitoring

```bash
# CPU/Memory usage
top -p $(pgrep game)
htop -p $(pgrep game)

# Network connections
netstat -an | grep game
lsof -i -P | grep game

# File descriptors
lsof -p $(pgrep game)
```

## Defect Catalog (Generic)

### Critical (P0/P1)

| Defect | Symptom | Detection | Fix |
|---|---|---|---|
| Crash on launch | Process exits, no window | Check exit code, logs | Fix dependencies, verify build |
| Infinite loop | Game freezes, 100% CPU | Check CPU usage, stack trace | Add timeout, fix loop condition |
| Memory leak | Memory grows over time | Monitor RSS, heap | Find leak, add cleanup |
| Save corruption | Crash on load | Check save file, logs | Fix serialization, add validation |
| Input ignored | No response to input | Check input focus, logs | Fix input handling, window focus |

### Major (P2)

| Defect | Symptom | Detection | Fix |
|---|---|---|---|
| Visual glitch | Flickering, artifacts | Screenshot analysis | Fix rendering, shader, texture |
| Audio issue | No sound, wrong sound | Audio capture, logs | Fix audio device, volume, format |
| Physics bug | Objects fall through, collide wrong | Physics state inspection | Fix collision, physics params |
| AI stuck | NPC stops moving | Behavior observation | Fix pathfinding, state machine |
| UI broken | Buttons don't work, text overflow | UI inspection | Fix layout, event handling |

### Minor (P3/P4)

| Defect | Symptom | Detection | Fix |
|---|---|---|---|
| Performance | Low FPS, stutter | FPS counter, profiler | Optimize rendering, reduce draw calls |
| Cosmetic | Wrong color, texture, font | Visual inspection | Fix assets, shader params |
| Edge case | Rare crash, specific input | Fuzz testing, edge case probing | Fix boundary conditions |
| Documentation | Missing help, unclear UI | Manual review | Add documentation, improve UI |

## Workflow

### Phase 1: Identify

1. Determine engine/framework (or unknown).
2. Check for source code access.
3. Select highest capability level available.
4. Document limitations.

### Phase 2: Instrument

1. Set up observation (screenshots, logs, metrics).
2. Set up input simulation (keyboard, mouse, gamepad).
3. Verify instrumentation works.
4. Document what's observable.

### Phase 3: Play

1. Launch game.
2. Play through core loop.
3. Explore all areas.
4. Test edge cases.
5. Log all observations.

### Phase 4: Audit

1. Review collected data.
2. Identify defects.
3. Classify severity.
4. Document findings.

### Phase 5: Repair (if applicable)

1. Root cause analysis.
2. Minimal fix.
3. Verify fix.
4. Regression test.

## Capability Honesty

What you CAN observe with generic adapter:

- ✅ Process state (running, CPU, memory)
- ✅ Screen content (screenshots, OCR)
- ✅ Input events (what was sent)
- ✅ Console output (if accessible)
- ✅ File system changes (saves, configs)
- ✅ Network traffic (if intercepted)

What you CANNOT observe without specific adapter:

- ❌ Internal game state (unless exposed)
- ❌ Exact object positions/rotations (unless visual)
- ❌ Physics internals (unless debug build)
- ❌ Game logic flow (unless decompiled)
- ❌ Anti-cheat state (if present)

**Always document what you could and couldn't observe.** Never claim coverage you don't have.

## Human-Assisted Fallback

When automation fails completely:

1. **Prepare instructions**: Exact steps for human to follow.
2. **Define success criteria**: What should happen?
3. **Request evidence**: Screenshots, videos, logs.
4. **Document results**: Record what human reported.
5. **Mark as manual test**: Note in audit report.

Example:

```
MANUAL TEST REQUIRED:
Game: Unknown Engine Game
Test: Verify boss fight mechanics
Steps:
1. Progress to boss area (coordinates unknown — explore)
2. Engage boss
3. Try to dodge boss attacks
4. Try to use special abilities
5. Report: What worked? What didn't? Any errors?
Evidence needed: Screenshot of boss, video of fight if possible
```

## Integration with Other Adapters

Generic adapter can be combined with specific adapters:

- **Generic + Three.js**: Use Playwright for browser automation, Three.js for scene inspection.
- **Generic + Unity**: Use pyautogui for input, Unity logs for output.
- **Generic + Godot**: Use xdotool for input, Godot logs for output.

The generic adapter provides the "how to interact" layer; specific adapters provide the "what to observe" layer.

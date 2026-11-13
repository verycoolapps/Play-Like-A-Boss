# WEB ENGINES ADAPTER

Coverage for web-based game engines beyond Three.js: Babylon.js, PlayCanvas, Phaser, PixiJS, A-Frame, Construct, and generic WebGL/Canvas fallback.

## Babylon.js

### Detection

```javascript
if (window.BABYLON) {
  console.log("Babylon.js version:", BABYLON.Engine.Version);
}

// Check for engine
if (window.engine && window.engine.getFps) {
  console.log("Babylon engine found");
}
```

### Instrumentation

```javascript
// Engine stats
const fps = engine.getFps();
const deltaTime = engine.getDeltaTime();

// Scene stats
const scene = engine.scenes[0];
const meshes = scene.meshes.length;
const lights = scene.lights.length;
const cameras = scene.cameras.length;

// Material/texture count
let materialCount = 0, textureCount = 0;
scene.meshes.forEach(mesh => {
  if (mesh.material) {
    materialCount++;
    if (mesh.material.diffuseTexture) textureCount++;
  }
});

console.log(`FPS: ${fps}, Meshes: ${meshes}, Materials: ${materialCount}, Textures: ${textureCount}`);
```

### Key APIs

- `engine.getFps()` — current FPS
- `engine.getDeltaTime()` — frame delta in ms
- `scene.meshes` — all meshes in scene
- `scene.pick(x, y)` — raycasting/picking
- `mesh.position`, `mesh.rotation` — transforms
- `mesh.material` — material properties

### Common Bugs

- **Material not updating**: `mesh.material.diffuseColor` changes not reflected.
- **Texture loading**: async texture loading not awaited.
- **Picking precision**: `scene.pick` returns wrong mesh due to layer masks.
- **Camera issues**: `camera.setTarget` not updating, FOV problems.

## PlayCanvas

### Detection

```javascript
if (window.pc) {
  console.log("PlayCanvas version:", pc.version || "unknown");
}

// Check for application
if (window.app && window.app.graphicsDevice) {
  console.log("PlayCanvas app found");
}
```

### Instrumentation

```javascript
// Graphics device stats
const device = app.graphicsDevice;
console.log("Max texture size:", device.maxTextureSize);
console.log("Max vertex textures:", device.maxVertexTextures);

// Draw call stats
const stats = app.graphicsDevice.stats;
console.log("Draw calls:", stats.drawCalls);
console.log("Triangles:", stats.triangles);

// Scene stats
const scene = app.scene;
console.log("Entities:", scene.root.children.length);
```

### Key APIs

- `app.scene` — root scene
- `app.graphicsDevice` — rendering device
- `entity.script` — script components
- `entity.render` — render component
- `app.systems` — system management

### Common Bugs

- **Script lifecycle**: `initialize`, `update`, `destroy` not called correctly.
- **Asset loading**: `app.assets` loading failures.
- **Physics sync**: rigid body transforms not matching render.
- **Event handling**: `app.on` / `app.off` listener leaks.

## Phaser

### Detection

```javascript
if (window.Phaser) {
  console.log("Phaser version:", Phaser.VERSION);
}

// Check for game instance
if (window.game && window.game.scene) {
  console.log("Phaser game found");
}
```

### Instrumentation

```javascript
// Game stats
const game = window.game;
console.log("FPS:", game.loop.actualFps);
console.log("Delta:", game.loop.delta);
console.log("Time scale:", game.loop.timeScale);

// Scene stats
const scene = game.scene.scenes[0];
console.log("Active scene:", scene.scene.key);
console.log("Cameras:", scene.cameras.cameras.length);
console.log("Game objects:", scene.children.length);

// Sprite count
let spriteCount = 0;
scene.children.list.forEach(child => {
  if (child.type === 'Sprite') spriteCount++;
});
console.log("Sprites:", spriteCount);
```

### Key APIs

- `game.loop.actualFps` — current FPS
- `game.scene.scenes` — active scenes
- `scene.children` — display list
- `sprite.body` — arcade physics body
- `scene.input` — input manager
- `scene.cameras` — camera manager

### Common Bugs

- **Physics sync**: `sprite.body.position` vs `sprite.x/y` mismatch.
- **Scene transitions**: scene not sleeping/waking correctly.
- **Input handling**: keyboard/mouse events not firing.
- **Asset loading**: `this.load.image` callbacks not firing.
- **Camera follow**: camera not tracking sprite correctly.

## PixiJS

### Detection

```javascript
if (window.PIXI) {
  console.log("PixiJS version:", PIXI.VERSION);
}

// Check for application
if (window.app && window.app.renderer) {
  console.log("PixiJS app found");
}
```

### Instrumentation

```javascript
// Renderer stats
const renderer = app.renderer;
console.log("Draw calls:", renderer.plugins?.batch?.drawCalls || "unknown");
console.log("Triangles:", renderer.stats?.triangles || "unknown");

// Stage stats
let spriteCount = 0, containerCount = 0;
app.stage.children.forEach(child => {
  if (child instanceof PIXI.Sprite) spriteCount++;
  if (child instanceof PIXI.Container) containerCount++;
});
console.log("Sprites:", spriteCount, "Containers:", containerCount);
```

### Key APIs

- `app.stage` — root display object
- `app.renderer` — WebGL/WebGPU renderer
- `sprite.texture` — texture reference
- `sprite.position`, `sprite.scale` — transforms
- `app.ticker` — animation ticker

### Common Bugs

- **Texture loading**: `PIXI.Assets.load` failures.
- **Sprite sheet parsing**: frame dimensions wrong.
- **Ticker issues**: `app.ticker.add` not firing.
- **Render texture**: `PIXI.RenderTexture` not updating.

## A-Frame (WebVR/WebXR)

### Detection

```javascript
if (window.AFRAME) {
  console.log("A-Frame version:", AFRAME.version);
}

// Check for scene
if (document.querySelector('a-scene')) {
  console.log("A-Frame scene found");
}
```

### Instrumentation

```javascript
const scene = document.querySelector('a-scene');
const entities = scene.querySelectorAll('*');
console.log("Entities:", entities.length);

// Check WebXR support
if (navigator.xr) {
  console.log("WebXR supported");
  const session = await navigator.xr.requestSession('immersive-vr');
}
```

### Key APIs

- `scene.object3D` — Three.js scene (A-Frame uses Three.js)
- `entity.getAttribute('position')` — component data
- `entity.emit('event-name')` — event system
- `AFRAME.registerComponent` — custom components

### Common Bugs

- **Component lifecycle**: `init`, `update`, `remove` not called.
- **Event handling**: `addEventListener` vs `emit` confusion.
- **Asset loading**: `asset` component not loading.
- **VR/XR issues**: session not starting, controllers not tracking.

## Construct 3

### Detection

```javascript
if (window.C3) {
  console.log("Construct 3 found");
}

// Check for runtime
if (window.c3runtime) {
  console.log("Construct runtime found");
}
```

### Instrumentation

```javascript
// Runtime stats
const runtime = window.c3runtime;
console.log("FPS:", runtime.GetRuntimeFps?.() || "unknown");
console.log("Layers:", runtime.GetLayerCount?.() || "unknown");
console.log("Objects:", runtime.GetInstanceCount?.() || "unknown");
```

### Key APIs

- `runtime.GetLayerCount()` — number of layers
- `runtime.GetInstanceCount()` — number of instances
- `runtime.GetEventSheetManager()` — event system
- `runtime.GetLayout()` — current layout

### Common Bugs

- **Event sheet errors**: actions/conditions not firing.
- **Instance variables**: scope issues, wrong instance selected.
- **Family collisions**: collision detection missing instances.
- **Save/load**: serialization errors, data corruption.

## Generic WebGL/Canvas Fallback

For games using raw WebGL or Canvas 2D without a framework:

### Detection

```javascript
// WebGL context
const canvas = document.querySelector('canvas');
const gl = canvas.getContext('webgl') || canvas.getContext('webgl2');
if (gl) {
  console.log("WebGL context found");
  console.log("Vendor:", gl.getParameter(gl.VENDOR));
  console.log("Renderer:", gl.getParameter(gl.RENDERER));
}

// Canvas 2D
const ctx = canvas.getContext('2d');
if (ctx) {
  console.log("Canvas 2D context found");
}
```

### Instrumentation

```javascript
// WebGL stats
if (gl) {
  const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
  if (debugInfo) {
    console.log("Unmasked vendor:", gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL));
    console.log("Unmasked renderer:", gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL));
  }
}

// Canvas stats
if (ctx) {
  console.log("Canvas size:", canvas.width, "x", canvas.height);
  console.log("Context state:", ctx.getTransform());
}
```

### Common Bugs

- **Context loss**: `webglcontextlost` event handling.
- **State leaks**: WebGL state not reset between draws.
- **Performance**: too many draw calls, no batching.
- **Canvas scaling**: DPI mismatch, blurry rendering.

## Browser Automation (Playwright)

For all web engines, Playwright provides universal automation:

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://localhost:3000');
  
  // Wait for game to load
  await page.waitForFunction(() => window.game || window.app || window.Phaser);
  
  // Capture console logs
  page.on('console', msg => console.log('Browser:', msg.text()));
  
  // Take screenshots
  await page.screenshot({ path: 'screenshot.png' });
  
  // Simulate input
  await page.keyboard.press('ArrowRight');
  await page.mouse.click(100, 100);
  
  // Evaluate JavaScript
  const state = await page.evaluate(() => {
    return window.game ? window.game.loop.actualFps : null;
  });
  
  await browser.close();
})();
```

## Capability Matrix

| Engine | Native debug | Console access | Scene graph | Input sim | Profiler | Memory access |
|---|---|---|---|---|---|---|
| Babylon | `engine.getFps()`, inspector | `console.log` | `scene.meshes` | Playwright | `engine` stats | JS heap |
| PlayCanvas | `app.graphicsDevice` | `console.log` | `app.scene` | Playwright | `device.stats` | JS heap |
| Phaser | `game.loop` | `console.log` | `scene.children` | Playwright | `game.loop` | JS heap |
| PixiJS | `app.renderer` | `console.log` | `app.stage` | Playwright | `renderer.stats` | JS heap |
| A-Frame | `scene.object3D` | `console.log` | DOM + Three.js | Playwright | Three.js stats | JS heap |
| Construct | `c3runtime` | `console.log` | Runtime APIs | Playwright | Limited | JS heap |
| Generic WebGL | `gl` context | `console.log` | Manual | Playwright | Limited | JS heap |

## When to Escalate

If web engine instrumentation is insufficient:

1. **Check for debug builds** — dev builds often have more logging.
2. **Look for exposed APIs** — `window.game`, `window.engine`, `window.app`.
3. **Use Chrome DevTools** — Performance tab, Memory tab, Console.
4. **Fall back to GUI automation** — if browser automation fails.
5. **Human-assisted** — if all else fails, document limitation.

## Capability Honesty

What you CAN observe with web engines:

- ✅ FPS, frame timing
- ✅ Draw calls, triangles (if exposed)
- ✅ Scene graph structure
- ✅ Object transforms, properties
- ✅ Console errors/warnings
- ✅ Input events

What you CANNOT observe without deeper access:

- ❌ GPU-level performance
- ❌ Network state (unless intercepted)
- ❌ Game logic internals (unless exposed)
- ❌ Minified/obfuscated code behavior

Document limitations in audit report.

# THREE.JS SPECIALIST ADAPTER

Deep instrumentation and defect catalog for Three.js games. This is the highest-fidelity adapter for web-based 3D games.

## Detection

Confirm Three.js usage:

```javascript
// In browser console or injected script
if (window.THREE) {
  console.log("Three.js version:", THREE.REVISION);
}

// Check for renderer
if (window.game && window.game.renderer) {
  console.log("Renderer found:", window.game.renderer.info);
}

// Check package.json
// "dependencies": { "three": "^0.160.0" }
```

## Core Instrumentation

### Renderer Info

Three.js exposes `renderer.info` — the most valuable diagnostic object:

```javascript
const info = renderer.info;

// Frame statistics
console.log("Calls:", info.render.calls);        // draw calls this frame
console.log("Triangles:", info.render.triangles); // triangles rendered
console.log("Points:", info.render.points);
console.log("Lines:", info.render.lines);

// Memory statistics
console.log("Geometries:", info.memory.geometries);
console.log("Textures:", info.memory.textures);

// Program statistics
console.log("Programs:", info.programs.length);
```

**Healthy ranges** (desktop, mid-range GPU):

| Metric | Good | Warning | Critical |
|---|---|---|---|
| Draw calls | < 100 | 100–300 | > 300 |
| Triangles | < 500k | 500k–1M | > 1M |
| Geometries | < 50 | 50–200 | > 200 |
| Textures | < 30 | 30–100 | > 100 |
| Programs | < 20 | 20–50 | > 50 |

### Scene Graph Access

```javascript
// Traverse scene
scene.traverse((object) => {
  if (object.isMesh) {
    console.log("Mesh:", object.name, object.geometry.type, object.material.type);
  }
});

// Find objects by name/type
const meshes = [];
scene.traverse((obj) => {
  if (obj.isMesh) meshes.push(obj);
});

// Access specific objects
const player = scene.getObjectByName("player");
const camera = scene.getObjectByName("camera");
```

### Animation State

```javascript
// If using AnimationMixer
const mixer = new THREE.AnimationMixer(model);
const action = mixer.clipAction(clip);
action.play();

// Check animation state
console.log("Action paused:", action.paused);
console.log("Action time:", action.time);
console.log("Action weight:", action.weight);

// List all animations
model.animations.forEach((clip) => {
  console.log("Clip:", clip.name, "duration:", clip.duration);
});
```

### Physics State (if using a physics engine)

```javascript
// Cannon.js / Ammo.js / Rapier
// Check rigid body state
const body = world.bodies[0];
console.log("Position:", body.position);
console.log("Velocity:", body.velocity);
console.log("Sleeping:", body.sleepState);
```

## Lifecycle Management

### Dispose Pattern

Three.js requires manual disposal of GPU resources. Leaks cause memory growth and eventual crashes.

```javascript
// Dispose geometry
geometry.dispose();

// Dispose material
material.dispose();

// Dispose texture
texture.dispose();

// Dispose renderer (on cleanup)
renderer.dispose();
renderer.forceContextLoss();
```

**Common leak patterns:**

- Creating new `BufferGeometry` every frame without disposing old.
- Loading textures without disposing on scene change.
- Creating new materials per object instead of sharing.
- Not disposing on scene unload / game state change.

**Detection:**

```javascript
// Monitor memory growth
setInterval(() => {
  const info = renderer.info.memory;
  console.log(`Geometries: ${info.geometries}, Textures: ${info.textures}`);
}, 5000);

// If counts keep growing without bound → leak
```

### WebGL Context Loss

```javascript
canvas.addEventListener('webglcontextlost', (event) => {
  event.preventDefault();
  console.error("WebGL context lost!");
  // Attempt recovery or show error
});

canvas.addEventListener('webglcontextrestored', () => {
  console.log("WebGL context restored");
  // Reinitialize renderer, reload textures
});
```

**Causes**: GPU memory exhaustion, driver crash, too many contexts, browser tab throttling.

**Prevention**: Monitor `info.memory`, dispose unused resources, limit texture sizes.

## Rendering Pipeline

### Delta Time

```javascript
// Correct: use delta time for animations
const clock = new THREE.Clock();
function animate() {
  const delta = clock.getDelta(); // seconds since last frame
  object.position.x += velocity * delta;
  requestAnimationFrame(animate);
}

// Incorrect: frame-dependent
function animate() {
  object.position.x += 0.1; // speed varies with FPS
  requestAnimationFrame(animate);
}
```

**Bug**: Using `Date.now()` or frame count instead of delta time causes speed inconsistencies.

### Raycasting

```javascript
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

function onMouseMove(event) {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
}

function checkIntersection() {
  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(scene.children, true);
  if (intersects.length > 0) {
    console.log("Hit:", intersects[0].object.name);
  }
}
```

**Common bugs**:

- Not updating raycaster on camera move.
- Not normalizing mouse coordinates.
- Raycasting against invisible objects.
- Performance: raycasting every frame against entire scene.

### Pointer Lock

```javascript
canvas.addEventListener('click', () => {
  canvas.requestPointerLock();
});

document.addEventListener('pointerlockchange', () => {
  if (document.pointerLockElement === canvas) {
    console.log("Pointer locked");
  } else {
    console.log("Pointer unlocked");
  }
});
```

**Bugs**: Not handling unlock, not checking lock state before input, pointer lock failing on some browsers.

### Resize Handling

```javascript
function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}
window.addEventListener('resize', onWindowResize);
```

**Bugs**: Not updating on resize, aspect ratio distortion, renderer size mismatch.

## Visual Quality

### Color Space & Tone Mapping

```javascript
// Modern Three.js (r152+)
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;

// Legacy (deprecated)
renderer.outputEncoding = THREE.sRGBEncoding;
```

**Bugs**:

- Wrong color space → washed out or oversaturated colors.
- Tone mapping mismatch → inconsistent lighting.
- Not setting `outputColorSpace` → colors look different across browsers.

### Draw Call Optimization

```javascript
// Merge geometries
import { mergeGeometries } from 'three/examples/jsm/utils/BufferGeometryUtils.js';
const merged = mergeGeometries([geo1, geo2, geo3]);

// Use instancing for repeated objects
const mesh = new THREE.InstancedMesh(geometry, material, count);

// Share materials
const sharedMaterial = new THREE.MeshStandardMaterial({ color: 0xff0000 });
mesh1.material = sharedMaterial;
mesh2.material = sharedMaterial;
```

**Detection**: `renderer.info.render.calls` > 100 → optimization needed.

## Common Defect Catalog

### Critical (P0/P1)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Memory leak | FPS degrades over time, crash after minutes | Undisposed geometries/textures/materials | Audit dispose calls, add cleanup |
| Context loss | Screen freezes, WebGL errors | GPU memory exhaustion, too many resources | Reduce texture sizes, dispose unused |
| Black screen | Nothing renders | Wrong camera, missing lights, shader error | Check camera position, lights, shader compile |
| Z-fighting | Flickering surfaces | Coplanar geometry, depth precision | Offset geometry, adjust near/far planes |
| Infinite loop | Game freezes | While loop without exit, recursive calls | Add break conditions, stack depth limits |

### Major (P2)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Frame rate inconsistency | Speed varies with FPS | Not using delta time | Use `clock.getDelta()` |
| Texture not loading | Missing textures, white materials | Wrong path, async not awaited | Fix path, await loading |
| Animation not playing | Static models | Mixer not updated, clip not playing | Call `mixer.update(delta)`, check action state |
| Raycast missing | Click doesn't register | Raycaster not updated, wrong objects | Update raycaster, check intersect list |
| Resize broken | Distorted view on window resize | Not handling resize event | Add resize listener, update camera/renderer |

### Minor (P3/P4)

| Defect | Symptom | Cause | Fix |
|---|---|---|---|
| Color space wrong | Colors look off | Wrong outputColorSpace | Set `SRGBColorSpace` |
| Tone mapping off | Washed out / too dark | Wrong tone mapping | Set `ACESFilmicToneMapping` |
| Shadow acne | Striped shadows | Shadow bias too low | Increase `shadow.bias` |
| Aliasing | Jagged edges | No antialiasing | Enable `antialias: true` in renderer |
| Pixel ratio | Blurry on HiDPI | Not setting pixel ratio | `renderer.setPixelRatio(devicePixelRatio)` |

## Instrumentation Scripts

### Performance Monitor

```javascript
// Inject into page
const monitor = setInterval(() => {
  const info = renderer.info;
  const fps = 1000 / (performance.now() - lastTime);
  lastTime = performance.now();
  
  console.log(JSON.stringify({
    fps: Math.round(fps),
    calls: info.render.calls,
    triangles: info.render.triangles,
    geometries: info.memory.geometries,
    textures: info.memory.textures,
    programs: info.programs.length
  }));
}, 1000);
```

### Memory Leak Detector

```javascript
// Track object count over time
const objectCounts = new Map();
setInterval(() => {
  let meshCount = 0, lightCount = 0;
  scene.traverse((obj) => {
    if (obj.isMesh) meshCount++;
    if (obj.isLight) lightCount++;
  });
  
  const key = `${meshCount}-${lightCount}`;
  objectCounts.set(key, (objectCounts.get(key) || 0) + 1);
  
  console.log(`Meshes: ${meshCount}, Lights: ${lightCount}`);
}, 5000);
```

### Scene Inspector

```javascript
// Dump scene hierarchy
function dumpScene(object, depth = 0) {
  const indent = "  ".repeat(depth);
  console.log(`${indent}${object.type}: ${object.name || "unnamed"}`);
  object.children.forEach(child => dumpScene(child, depth + 1));
}
dumpScene(scene);
```

## Browser Automation Integration

### Playwright Setup

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://localhost:3000');
  
  // Access Three.js objects
  const rendererInfo = await page.evaluate(() => {
    return window.game.renderer.info;
  });
  
  console.log("Renderer info:", rendererInfo);
  
  await browser.close();
})();
```

### Chrome DevTools Protocol

```javascript
// Enable WebGL debugging
const client = await page.context().newCDPSession(page);
await client.send('WebGL.enable');
await client.send('WebGL.getContextInfo');
```

## When Three.js Isn't Enough

If the game uses Three.js but wraps it in a framework (React Three Fiber, Vue Three.js):

- Access the underlying Three.js objects through the framework's store.
- React Three Fiber: `useThree()` hook, `state.scene`, `state.gl`.
- Vue Three.js: component refs, `scene` prop.

If the game uses a custom engine built on Three.js:

- Look for exposed debug APIs.
- Check for global variables (`window.game`, `window.engine`).
- Inject instrumentation at the framework level.

## Capability Honesty

What you CAN observe with Three.js:

- ✅ Renderer stats (draw calls, triangles, memory)
- ✅ Scene graph structure
- ✅ Object transforms, materials, geometries
- ✅ Animation state
- ✅ Raycasting results
- ✅ WebGL context state
- ✅ Console errors/warnings

What you CANNOT observe without deeper access:

- ❌ GPU-level performance (shader compile time, draw call overhead)
- ❌ Network state (asset loading, multiplayer sync)
- ❌ Game logic internals (unless exposed via debug API)
- ❌ Anti-cheat state (if present)

Document limitations in the audit report.

# VISUAL AUDIT

Systematic verification of visual quality, rendering correctness, and UI/UX presentation. Covers both 3D rendering and 2D UI elements.

## Audit Scope

Visual audit covers:

- Rendering correctness (geometry, materials, lighting, shadows)
- Visual artifacts (z-fighting, clipping, flickering, seams)
- UI/UX presentation (layout, readability, consistency, feedback)
- Animation quality (smoothness, transitions, blending)
- VFX quality (particles, effects, post-processing)
- Resolution/scaling/DPI handling
- Color accuracy and accessibility

## Methodology

For each visual element:

1. **Identify** — what should this look like?
2. **Observe** — capture the visual state.
3. **Compare** — observed vs expected.
4. **Document** — record finding if mismatch.

## 3D Rendering Checks

### Geometry

| Check | What to look for | Evidence |
|---|---|---|
| Mesh integrity | No missing faces, inverted normals, degenerate geometry | Wireframe view, close-up screenshots |
| Polygon count | Reasonable for target platform | `renderer.info.render.triangles` |
| LOD transitions | Smooth LOD changes, no popping | Video capture during movement |
| Culling | Objects disappear when behind camera | Move camera, verify culling |
| Instancing | Repeated objects render correctly | Compare instanced vs non-instanced |

### Materials & Textures

| Check | What to look for | Evidence |
|---|---|---|
| Texture loading | All textures load, no missing/placeholder | Screenshot, console logs |
| UV mapping | No stretching, distortion, seam artifacts | Close-up screenshots |
| Material properties | Correct color, roughness, metalness | Side-by-side comparison |
| Normal maps | Correct lighting response | Rotate light, observe changes |
| Transparency | Alpha blending correct, no sorting issues | Move objects, check order |

### Lighting & Shadows

| Check | What to look for | Evidence |
|---|---|---|
| Light placement | Lights illuminate correct areas | Screenshot with shadows |
| Shadow quality | No acne, peter-panning, missing shadows | Close-up shadow inspection |
| Shadow resolution | Sharp enough for scene | Zoom in on shadows |
| Ambient occlusion | Contact shadows present | Corner inspection |
| Light leaks | No light through walls | Interior/exterior check |
| Dynamic lighting | Moving lights update correctly | Move light source |

### Post-Processing

| Check | What to look for | Evidence |
|---|---|---|
| Bloom | Glowing objects bloom correctly | Bright object screenshot |
| Depth of field | Focus blur correct | Compare focused/defocused |
| Motion blur | Blur during fast movement | Fast movement video |
| Color grading | Consistent color palette | Scene comparison |
| Vignette | Subtle edge darkening | Screenshot edges |
| Anti-aliasing | No jagged edges | Zoom in on edges |

### Camera & Framing

| Check | What to look for | Evidence |
|---|---|---|
| Camera position | Correct framing, no clipping | Screenshot |
| Camera movement | Smooth, no jitter | Video during movement |
| Field of view | Correct FOV, no distortion | Compare to reference |
| Near/far planes | No z-fighting, no clipping | Move objects close/far |
| Aspect ratio | Correct on different resolutions | Resize window, compare |

## 2D/UI Checks

### Layout & Positioning

| Check | What to look for | Evidence |
|---|---|---|
| Element alignment | Elements aligned to grid or intentional | Screenshot with guides |
| Spacing | Consistent margins, padding | Measure pixel distances |
| Overlap | No unintended overlaps | Screenshot |
| Overflow | Text/elements don't overflow containers | Resize window, check |
| Z-order | Correct layering (UI above world) | Screenshot |

### Typography

| Check | What to look for | Evidence |
|---|---|---|
| Font rendering | No blurry text, correct weight | Zoom in on text |
| Readability | Sufficient contrast, size | Contrast checker |
| Consistency | Same font/size for same element type | Compare instances |
| Localization | Text fits in all languages | Switch language, check |
| Special characters | Accents, symbols render correctly | Test with special chars |

### Color & Contrast

| Check | What to look for | Evidence |
|---|---|---|
| Color accuracy | Colors match design spec | Color picker comparison |
| Contrast ratio | WCAG AA minimum 4.5:1 for text | Contrast checker tool |
| Color blindness | Distinguishable without color | Simulate color blindness |
| Dark/light mode | Both modes work correctly | Toggle theme, compare |

### Interactive Elements

| Check | What to look for | Evidence |
|---|---|---|
| Button states | Normal, hover, pressed, disabled | Screenshot each state |
| Feedback | Visual/audio feedback on interaction | Video of interaction |
| Cursor | Correct cursor for interactive elements | Hover over elements |
| Focus | Keyboard focus visible | Tab through UI |
| Loading states | Spinners, progress bars | Trigger loading, observe |

### Animation & Transitions

| Check | What to look for | Evidence |
|---|---|---|
| Smoothness | No jank, consistent frame rate | Video capture |
| Timing | Correct duration, easing | Frame-by-frame analysis |
| Interruptibility | Can cancel/reverse mid-animation | Trigger during animation |
| State consistency | End state matches expectation | Compare start/end |

## Visual Artifact Catalog

### Critical (P0/P1)

| Artifact | Symptom | Cause | Fix |
|---|---|---|---|
| Black screen | Nothing renders | Missing camera, lights, or shader error | Check camera, lights, shader compile |
| Z-fighting | Flickering surfaces | Coplanar geometry, depth precision | Offset geometry, adjust near/far |
| Texture corruption | Blocky, wrong colors | Compressed texture issue, wrong format | Reimport texture, check format |
| Missing textures | White/gray materials | Texture not loaded, wrong path | Fix path, check loading |
| Geometry explosion | Vertices scattered | Corrupted mesh, wrong import | Reimport mesh, check format |

### Major (P2)

| Artifact | Symptom | Cause | Fix |
|---|---|---|---|
| Shadow acne | Striped shadows | Shadow bias too low | Increase shadow bias |
| Light leaking | Light through walls | Shadow map resolution, bias | Increase shadow map size, adjust bias |
| LOD popping | Objects pop in/out | LOD distances too aggressive | Adjust LOD distances |
| Texture stretching | Distorted textures | Wrong UV mapping | Fix UV unwrap |
| Aliasing | Jagged edges | No anti-aliasing | Enable MSAA/FXAA/TAA |

### Minor (P3/P4)

| Artifact | Symptom | Cause | Fix |
|---|---|---|---|
| Color banding | Visible color steps | Low bit depth, compression | Increase bit depth, dithering |
| Texture bleeding | Colors bleed at edges | Mipmap bleeding, padding | Increase texture padding |
| Slight misalignment | Elements slightly off | Rounding errors, DPI scaling | Snap to pixel grid |
| Inconsistent spacing | Uneven margins | Manual placement errors | Use layout system |
| Font weight mismatch | Text looks different | Font fallback, weight not loaded | Embed font, check weight |

## Resolution & Scaling

Test across resolutions:

| Resolution | Aspect Ratio | Test Focus |
|---|---|---|
| 1920x1080 | 16:9 | Standard desktop |
| 2560x1440 | 16:9 | High DPI desktop |
| 3840x2160 | 16:9 | 4K display |
| 1366x768 | 16:9 | Laptop/low-end |
| 1280x720 | 16:9 | Minimum desktop |
| 1080x1920 | 9:16 | Mobile portrait |
| 1920x1080 | 16:9 | Mobile landscape |
| 1024x768 | 4:3 | Tablet/older displays |
| 800x600 | 4:3 | Minimum supported |

For each resolution:

- Check UI scaling (does it fit?).
- Check rendering quality (does it look correct?).
- Check performance (does it maintain FPS?).
- Check readability (is text legible?).

## Accessibility Checks

| Check | Standard | Test Method |
|---|---|---|
| Color contrast | WCAG AA 4.5:1 | Contrast checker tool |
| Text size | Minimum 16px for body text | Measure font size |
| Focus indicators | Visible focus outline | Tab through UI |
| Screen reader | ARIA labels, semantic HTML | Test with screen reader |
| Keyboard navigation | All functions accessible via keyboard | Tab through UI |
| Motion sensitivity | Option to reduce motion | Check settings |
| Color blindness | Distinguishable without color | Simulate protanopia/deuteranopia/tritanopia |

## Evidence Collection

For each visual check:

1. **Screenshot** — capture the visual state.
2. **Annotation** — mark issues on screenshot.
3. **Comparison** — side-by-side with expected.
4. **Video** — for animation/timing issues.
5. **Metrics** — FPS, draw calls if relevant.

Store evidence in `.plab/session-*/evidence/visual/`.

## Finding Documentation

When visual check fails:

1. **Create finding** — use `templates/bug-report.md`.
2. **Assign severity** — P0–P4 based on impact.
3. **Link evidence** — reference screenshots, videos.
4. **Describe reproduction** — exact steps to reproduce.
5. **Note expected vs actual** — what should look like vs what does.

## Coverage Tracking

Maintain a checklist of visual elements tested:

```
VISUAL AUDIT PROGRESS
├── 3D Rendering: [x] [x] [x] [x] [x] [x] [x]
├── Materials: [x] [x] [x] [x] [x]
├── Lighting: [x] [x] [x] [x] [x] [x]
├── Post-Processing: [x] [x] [x] [x] [x]
├── Camera: [x] [x] [x] [x] [x]
├── UI Layout: [x] [x] [x] [x] [x] [x]
├── Typography: [x] [x] [x] [x] [x]
├── Color: [x] [x] [x] [x]
├── Interactive: [x] [x] [x] [x] [x]
├── Animation: [x] [x] [x] [x]
├── Resolution: [x] [x] [x] [x] [x] [x] [x] [x] [x]
└── Accessibility: [x] [x] [x] [x] [x] [x]

TOTAL: 52/58 tested (90%)
BLOCKED: 6 tests (VR headset unavailable)
```

## When to Stop

Stop visual audit when:

- All visual elements tested at least once.
- All P0/P1 findings documented.
- No new findings in last 10 checks.
- Time budget exhausted (document remaining checks).
- Platform limits prevent further testing.

## Integration with Other Audits

Visual audit findings may reveal issues in other dimensions:

- Performance issue → performance audit
- Animation bug → animation audit
- Physics visual glitch → physics audit
- UI functionality → functional audit
- Audio-visual sync → audio audit

Cross-reference findings and coordinate audits.

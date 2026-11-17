# PLAB Blender Adapter

**Play Like A Boss integration for Blender architectural and game level designs.**

Audit game level dan architectural designs dengan systematic room-by-room inspection.

---

## Overview

PLAB Blender adapter menggunakan **Building Room Viewer** (Blender add-on) untuk:

1. **Detect & catalog** setiap ruangan dalam bangunan/level
2. **Navigate** systematically dari room ke room dengan automated camera
3. **Inspect** setiap space terhadap quality gates
4. **Report** findings per-room dengan evidence captures
5. **Profile** performance dan complexity per-room

---

## Room Detection

Add-on secara otomatis mendeteksi ruangan dari Blender scene structure:

```
Scene Collection
├── Room.Kitchen
│   ├── floor
│   ├── walls
│   ├── doors
│   └── furniture
├── Room.Bedroom
│   ├── floor
│   ├── walls
│   ├── door
│   └── bed
└── Room.LivingRoom
    └── ...
```

**Naming Convention Options:**
- `Room.{Name}` - Recommended
- Capitalized collections: `Kitchen`, `Bedroom`
- Objects: `room_kitchen`, `room_bedroom`

---

## PLAB Operational Modes

### 1. Room Discovery

```
/plab discover-rooms blender scene
```

- Scan Blender file untuk semua rooms
- Extract room geometry & bounds
- Build room connectivity graph (doors/passages)
- Report room inventory dengan metrics

**Output:**
```
✓ Found 7 rooms:
  - Kitchen (12.5m²)
  - Bedroom_1 (14.2m²)
  - Bedroom_2 (13.8m²)
  - Living Room (25.3m²)
  - Bathroom (5.2m²)
  - Hallway (8.1m²)
  - Stairs (4.5m²)

Connectivity:
  Kitchen ←→ Dining ←→ Living Room
  Living Room ←→ Hallway ←→ Bedrooms
```

### 2. Per-Room Quality Audit

```
/plab audit-rooms {level}
```

Untuk setiap room, check:
- **Geometry** - overlapping faces, missing normals, inverted geometry
- **Performance** - polygon count, draw calls, material complexity
- **Lighting** - shadow casting efficiency, baked vs real-time balance
- **Physics** - collision mesh integrity, walkable surfaces
- **Navigation** - navmesh coverage, unreachable areas
- **Asset integrity** - missing textures, broken references

**Output per room:**
```
KITCHEN
  ✓ Geometry: 2,400 faces, clean
  ⚠ Lighting: 3 point lights + 1 directional (optimize?)
  ✓ Physics: Collision mesh aligned
  ✗ Navigation: 15% unmapped area in corner
  PLAB-0127: Navmesh gap by shelving unit
```

### 3. Room-by-Room Walkthrough

```
/plab walkthrough-rooms {level} duration:5m
```

Play-test setiap room untuk:
- Lighting consistency
- Asset pop-in or LOD transitions
- Audio cue playback
- Physics responsiveness
- NPC/hazard behavior

Navigate otomatis ke setiap room, jangan di room untuk 30s, capture anomalies.

### 4. Room Connectivity Audit

```
/plab audit-connectivity {level}
```

Untuk setiap passage/door/opening:
- ✓ Passage geometry valid
- ✓ No Z-fighting at thresholds
- ✓ Audio/lighting transition smooth
- ✓ No soft-locks when crossing
- ✓ Respawn points reachable from each room

### 5. Performance Profiling Per-Room

```
/plab profile-rooms {level}
```

For setiap room dengan camera at center:
- Polygon count
- Material unique count
- Light count & shadow cost
- Texture memory usage
- Physics complexity
- Audio sources

Identify bottleneck rooms.

---

## Setup untuk PLAB

### Step 1: Install Room Viewer Add-on

```bash
# Copy add-on ke Blender addons folder
cp -r ~/Play-Like-A-Boss/adapters/blender_room_viewer \
  ~/.config/blender/4.x/scripts/addons/
```

### Step 2: Organize Scene

Pastikan Blender file sudah organized:
```
Scene Collection
├── [Optional] Terrain
├── [Optional] Sky
├── Room.{Name1}
│   └── geometry & assets
├── Room.{Name2}
│   └── geometry & assets
└── [Optional] Global lights
```

### Step 3: Trigger PLAB

```
/plab audit-rooms ~/path/to/level.blend
```

---

## Room Metrics

Setiap room di-analyze untuk:

```yaml
Room: Kitchen
  Geometry:
    - Triangles: 2400
    - Vertices: 1850
    - Materials: 4
    - Textures: 6
    
  Performance:
    - Lightmap coverage: 100%
    - Draw calls (avg): 12
    - Shadow-casting lights: 2
    - Statically batched: ✓
    
  Physics:
    - Collision faces: 400
    - Walkable area: 12.5m²
    - Obstacle density: low
    - Physics bodies: 8
    
  Navigation:
    - Navmesh coverage: 98%
    - Unreachable pockets: 1 (small corner)
    - Passage clearance: 2.1m min
    
  Accessibility:
    - Ceiling height: 2.8m
    - Door width: 0.9m
    - Obstacle clearance: adequate
    - Audio coverage: ✓
```

---

## Finding Format: Per-Room

Setiap finding di-scoped ke room-nya:

```
PLAB-0145  [P2]  Navmesh gap in Kitchen corner
  Room:     Kitchen (12.5m²)
  Location: Behind counters, NW corner
  Severity: P2 (NPC nav blocker, rare)
  Repro:    1. Load kitchen  2. Observe NPC behavior  3. Corner unreachable
  Impact:   NPC can't navigate full kitchen
  Fix:      Extend navmesh, or add walkway geometry
```

---

## Blender + PLAB Workflow Example

### Scenario: Audit Game Level Before Alpha

```bash
# 1. Detect rooms
/plab discover-rooms ~/projects/game/level_01.blend

# 2. Full quality audit
/plab audit-rooms ~/projects/game/level_01.blend

# 3. Performance profiling
/plab profile-rooms ~/projects/game/level_01.blend

# 4. Walkthrough play-test
/plab walkthrough-rooms ~/projects/game/level_01.blend duration:10m

# 5. Connectivity check
/plab audit-connectivity ~/projects/game/level_01.blend

# 6. Final verdict
/plab verdict-rooms ~/projects/game/level_01.blend
```

Output: Comprehensive report with per-room breakdown, screenshots, and prioritized fix list.

---

## Integration Points

### In-Engine Validation

After PLAB audit, re-import to game engine & validate:
- Load each room in game → capture in-engine metrics
- Compare geometry/assets match Blender expectations
- Test gameplay physics vs Blender collision

### Screenshot Evidence

PLAB captures per-room:
- Geometry view (wireframe)
- Textured view
- Lighting view
- Navmesh overlay
- Physics collision view

---

## Limitations & Workarounds

### Limitation: Rooms in Different Blender Files

**Workaround:** Merge all rooms into single scene:
```
File > Append > Select .blend files > Select Room collections
```

### Limitation: Complex Room Hierarchies

**Workaround:** Use simple "Room.Name" flat structure, not nested.

### Limitation: Dynamic Rooms (geometry changes at runtime)

**Workaround:** Audit static Blender source; test dynamic variant in-engine.

---

## Future Enhancements

- [ ] Automated room subdivision detection (esp. modular game levels)
- [ ] Cross-room navmesh validation (passages, doors)
- [ ] Lighting handoff consistency across room thresholds
- [ ] Material & texture variance per-room (consistency audit)
- [ ] Room dependency graph (which rooms reference which assets)
- [ ] Export room catalog with geometry LODs
- [ ] Per-room audio design validation

---

## See Also

- `../blender_room_viewer/README.md` - Room Viewer add-on docs
- `quality-gates.md` - Full PLAB quality gate specification
- `dimensions.md` - All audit dimensions

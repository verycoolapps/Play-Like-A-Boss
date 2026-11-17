# Building Room Viewer for Blender

**Interactive room/space navigator for Blender architectural and game level designs.**

Navigasi dan inspeksi per ruangan dalam bangunan virtual dengan UI picker dan camera automation.

---

## Fitur

- 🏠 **Deteksi otomatis ruangan** dari structure Blender (collections)
- 🎥 **Camera automation** untuk smooth navigation antar ruangan
- 📍 **Room selector UI** dengan visual list di sidebar
- 🔍 **Overview mode** untuk lihat keseluruhan bangunan
- 🎛️ **Zoom & elevation control** untuk adjust camera view
- ⚡ **Orbit camera** untuk rotasi view

---

## Instalasi

### Cara 1: Drop-in Manual

```bash
# Masuk ke Blender add-ons folder
cd ~/.config/blender/4.x/scripts/addons

# Copy atau symlink folder
cp -r ~/Play-Like-A-Boss/adapters/blender_room_viewer .
# ATAU
ln -s ~/Play-Like-A-Boss/adapters/blender_room_viewer blender_room_viewer
```

### Cara 2: Di Blender UI

1. Buka Blender → Edit → Preferences → Add-ons
2. Click "Install..."
3. Navigasi ke `~/Play-Like-A-Boss/adapters/blender_room_viewer`
4. Select folder, click "Install Add-on"
5. Enable add-on (cari "Building Room Viewer")

---

## Setup Blender Scene

Add-on ini mencari ruangan dengan tiga cara:

### Method 1: Collections dengan prefix "Room."

```
Scene Collection
├── Room.Kitchen
│   ├── floor
│   ├── walls
│   └── furniture
├── Room.Bedroom
│   ├── floor
│   ├── walls
│   └── bed
└── Room.LivingRoom
    └── ...
```

**Recommended!** Paling mudah dan clear.

### Method 2: Capitalized Collections

```
Scene Collection
├── Kitchen
│   ├── floor
│   └── ...
├── Bedroom
└── LivingRoom
```

### Method 3: Objects dengan prefix "room_"

```
Scene Collection
├── room_kitchen
├── room_bedroom
└── room_livingroom
```

---

## Penggunaan

### 1. Buka Room Viewer Panel

- View → Sidebar (atau tekan `N`)
- Tab "Room Viewer" muncul di kanan

### 2. Refresh Rooms

- Click tombol "Refresh Rooms" untuk scan ulang scene
- Akan show berapa banyak rooms ditemukan

### 3. Navigasi ke Room

- Click salah satu room name di list
- Camera otomatis move ke room tersebut
- Current room di-highlight dengan checkmark

### 4. View All Rooms

- Click tombol "📍 View All Rooms"
- Camera zoom out untuk show keseluruhan bangunan

### 5. Camera Control

- **Zoom Factor**: Seberapa jauh camera zoom dari room bounds
  - 1.0 = tepat di edge
  - 1.5 = 50% farther (default)
  - 3.0 = jauh untuk overview
  
- **Camera Elevation**: Sudut pandang vertikal
  - 0° = side view
  - 45° = isometric-ish (default)
  - 90° = top-down

- **Orbit Left/Right**: Rotate view 45° ke kiri/kanan

---

## Contoh Workflow

### Scenario: Inspeksi Game Level dengan 5 Ruangan

```
1. Buka Blender file game level Anda
2. Pastikan ruangan sudah diorganisir jadi collections
3. Enable add-on "Building Room Viewer"
4. Click "Refresh Rooms" - should show 5 rooms
5. Click tiap room untuk lihat detail
6. Use Zoom Factor untuk adjust how close camera
7. Orbit Left/Right untuk see dari sudut lain
8. Click "View All Rooms" untuk overview keseluruhan
```

### Scenario: Architecture Review

```
1. File revit/CAD sudah di-import ke Blender
2. Rooms sudah di-separate jadi collections per floor
3. Enable Room Viewer
4. Navigate floor by floor dengan room selector
5. Adjust elevation untuk lihat dari perspektif berbeda
6. Export camera views untuk presentasi
```

---

## Technical Details

### Struktur File

```
blender_room_viewer/
├── __init__.py          # Main add-on register/unregister
├── room_detector.py     # Detect & analyze rooms
├── camera_controller.py # Camera automation
├── ui_panel.py          # UI panel & operators
└── README.md            # This file
```

### Room Class Properties

Setiap room punya:
- `name` - Room name
- `center` - Vector center point
- `bounds` - (min, max) corners
- `size` - Dimensions (width, height, depth)
- `objects` - List of Blender objects

### Camera Controller Methods

```python
# Focus on specific room
controller.focus_on_room(room, zoom_factor=1.5, elevation=45)

# Show entire building
controller.focus_on_building(detector, zoom_factor=2.0)

# Rotate view
controller.orbit_camera(angle_degrees=45)

# Quick views
controller.set_view_top()      # Top-down orthographic
controller.set_view_front()    # Front view
controller.set_view_side()     # Side view
```

---

## Troubleshooting

### "No rooms detected"

- Check collection names follow "Room.Name" format
- OR collection names are capitalized (Kitchen, Bedroom)
- Refresh dengan tombol "Refresh Rooms"

### Camera tidak move

- Pastikan ada camera di scene (add-on akan create default jika tidak ada)
- Check di Outliner bahwa scene.camera di-set

### Rooms tidak ada objects

- Collections butuh punya minimal 1 mesh/object di dalamnya
- Empty collections diabaikan

---

## Integration dengan PLAB

Add-on ini bisa diintegrasikan ke PLAY LIKE A BOSS testing untuk:

1. **Game level auditing** - navigate setiap room saat playtest
2. **Room-by-room QA** - systematic test each space
3. **Performance profiling** - measure per-room complexity
4. **Screenshot reports** - capture dari setiap room angle

### Contoh PLAB Integration

```
/plab audit this blender level
  - Use room viewer to navigate every space
  - Measure performance per room
  - Capture reference images
  - Report findings per room
```

---

## Future Enhancements

- [ ] Export camera path animations
- [ ] Room connectivity graph (door/passage visualization)
- [ ] Performance metrics per room
- [ ] Bookmarked camera positions
- [ ] Room label annotations
- [ ] Video walkthrough export
- [ ] Multi-floor hierarchy support

---

## License

Part of PLAY LIKE A BOSS - Proprietary © 2026 PT. Agra Karya Digital (VeryCoolApps)

Untuk penggunaan personal & internal business use. Redistribusi sebagai competing skill tidak diperbolehkan.

---

## Support

Issues atau suggestions? Integrasikan langsung ke PLAB workflow:

```
/plab audit blender scene dan report room detection issues
```

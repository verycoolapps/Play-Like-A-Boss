# GAMEPLAY MEMORY

Persistent session memory that makes each run smarter than the last. Stored in `.plab/` within the game project.

## Directory Structure

```
.plab/
├── session-YYYYMMDD-HHMMSS/
│   ├── config.json              # session configuration
│   ├── game-profile.md          # filled game profile
│   ├── observations.jsonl       # append-only observation log
│   ├── findings/
│   │   ├── PLAB-0001.md         # bug reports
│   │   └── ...
│   ├── repairs/
│   │   ├── PLAB-0001-repair.md  # repair reports
│   │   └── ...
│   ├── evidence/
│   │   ├── screenshots/
│   │   ├── traces/
│   │   ├── logs/
│   │   └── dumps/
│   ├── test-results/
│   │   ├── matrix.csv           # test matrix results
│   │   └── exploratory/         # exploratory session logs
│   └── final-report.md          # the verdict
├── latest -> session-YYYYMMDD-HHMMSS  # symlink to most recent
├── game-profile.md              # persistent game profile (merged)
├── findings-index.json          # all findings across sessions
├── repairs-index.json           # all repairs across sessions
└── knowledge-base.md            # accumulated insights
```

## Schema Definitions

### config.json

```json
{
  "session_id": "20261013-143022",
  "mode": "BOSS_MODE",
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
  "platform": "web",
  "build_info": {
    "commit": "abc123",
    "branch": "main",
    "build_time": "2026-10-13T14:00:00Z",
    "version": "1.2.3"
  },
  "environment": {
    "os": "darwin 27.2.0",
    "arch": "arm64",
    "gpu": "Apple M3",
    "browser": "Chrome 120"
  },
  "start_time": "2026-10-13T14:30:22Z",
  "status": "in_progress"
}
```

### game-profile.md

See `templates/game-profile.md` for the full template. The filled version captures:

- Game identity (title, version, genre, engine)
- Core mechanics and controls
- World structure and progression
- Win/lose conditions
- Known limitations and quirks

### observations.jsonl

Append-only log of every significant observation during play:

```json
{"timestamp":"2026-10-13T14:31:00Z","type":"state","data":{"scene":"menu","fps":60,"objects":142}}
{"timestamp":"2026-10-13T14:31:05Z","type":"action","data":{"input":"click","target":"start_button","result":"game_started"}}
{"timestamp":"2026-10-13T14:31:10Z","type":"anomaly","data":{"type":"fps_drop","value":23,"duration_ms":1500}}
{"timestamp":"2026-10-13T14:31:15Z","type":"finding","data":{"id":"PLAB-0001","severity":"P1","summary":"Character clips through wall"}}
```

Observation types:

- `state` — game state snapshot
- `action` — input sent and result
- `anomaly` — unexpected behavior detected
- `metric` — performance measurement
- `error` — console error or crash
- `finding` — bug report reference
- `repair` — repair action taken
- `verify` — verification result

### findings-index.json

```json
{
  "findings": [
    {
      "id": "PLAB-0001",
      "session": "20261013-143022",
      "severity": "P1",
      "category": "physics",
      "summary": "Character clips through wall on map_03",
      "status": "open|repaired|verified|wontfix",
      "reproduction": "walk to coordinates (12.5, 0, -8.3) and jump",
      "evidence": ["evidence/screenshots/clip-001.png", "evidence/traces/clip-001.json"],
      "repair": "repairs/PLAB-0001-repair.md",
      "verified": "2026-10-13T15:00:00Z"
    }
  ],
  "stats": {
    "total": 47,
    "open": 12,
    "repaired": 30,
    "verified": 5,
    "wontfix": 0
  }
}
```

### repairs-index.json

```json
{
  "repairs": [
    {
      "finding_id": "PLAB-0001",
      "session": "20261013-143022",
      "timestamp": "2026-10-13T15:00:00Z",
      "root_cause": "Collision mesh missing on wall segment",
      "fix": "Added BoxCollider to wall_mesh_03",
      "files_changed": ["Assets/Scripts/WallCollision.cs"],
      "verification": "Re-ran reproduction steps, confirmed no clipping",
      "regression": "Ran physics audit, no new findings"
    }
  ]
}
```

### knowledge-base.md

Accumulated insights across sessions:

```markdown
# Knowledge Base

## Engine Quirks
- Three.js: `renderer.info.render.calls` spikes when materials share textures
- Unity: `Time.timeScale` affects physics, not animations

## Common Bugs
- PLAB-0001 pattern: Missing collider on procedurally generated geometry
- PLAB-0007 pattern: Save corruption when quitting during autosave

## Successful Strategies
- Blind spot hunting: spawn camping reveals AI stuck states
- Regression testing: differential testing catches physics drift

## Failed Approaches
- GUI automation on Unity builds: too slow for real-time games
- Screenshot-only audit: misses non-visual bugs
```

## Persistence Rules

1. **Write early, write often** — append observations immediately, don't batch.
2. **Atomic writes** — write to temp file, then rename, to avoid corruption.
3. **Version findings** — if a finding is repaired and regresses, create a new finding linked to the old.
4. **Never delete** — findings and repairs are append-only; mark as resolved, don't remove.
5. **Cross-session learning** — read `.plab/knowledge-base.md` at session start, update at session end.

## Session Lifecycle

### Start

1. Check for existing `.plab/` directory.
2. Read `game-profile.md`, `findings-index.json`, `repairs-index.json`, `knowledge-base.md`.
3. Create new session directory `session-YYYYMMDD-HHMMSS/`.
4. Write `config.json` with current mode, engine, capabilities.
5. Update `latest` symlink.

### During

1. Append to `observations.jsonl` for every significant event.
2. Write findings to `findings/PLAB-NNNN.md` immediately.
3. Write repairs to `repairs/PLAB-NNNN-repair.md` immediately.
4. Save evidence to `evidence/` with descriptive names.
5. Update indexes after each finding/repair.

### End

1. Write `final-report.md` with verdict and summary.
2. Update `knowledge-base.md` with new insights.
3. Update `findings-index.json` and `repairs-index.json`.
4. Mark session `status: "completed"` in `config.json`.
5. Clean up temp files, keep evidence.

## Retrieval

When starting a new session:

```
READ .plab/game-profile.md          → know the game
READ .plab/findings-index.json      → know open bugs
READ .plab/repairs-index.json       → know what was fixed
READ .plab/knowledge-base.md        → know what works
READ .plab/latest/config.json       → know last session settings
```

Use this context to:

- Skip re-auditing repaired areas (but verify they still work).
- Focus on open findings and new areas.
- Apply known successful strategies.
- Avoid known failed approaches.

## Limitations

- `.plab/` is local to the project; it doesn't sync across machines.
- Large evidence files (videos, dumps) may consume disk space; compress or externalize if needed.
- Concurrent sessions on the same project may conflict; use file locking or separate directories.
- The memory is only as good as the discipline of writing to it; automate where possible.

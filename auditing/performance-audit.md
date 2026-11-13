# PERFORMANCE AUDIT

Systematic measurement and analysis of game performance: frame rate, memory usage, CPU/GPU load, and optimization opportunities.

## Audit Scope

Performance audit covers:

- Frame rate (FPS) stability and averages
- Frame time distribution (p99, p999)
- CPU usage (game thread, render thread, worker threads)
- GPU usage (draw calls, triangles, shader cost)
- Memory usage (RAM, VRAM, memory leaks)
- Loading times (initial load, level transitions, asset streaming)
- Network performance (latency, bandwidth, packet loss)
- Battery/thermal performance (mobile, laptop)

## Methodology

For each performance metric:

1. **Measure** — capture baseline metrics.
2. **Stress** — push the game to limits.
3. **Analyze** — identify bottlenecks.
4. **Optimize** — apply targeted fixes.
5. **Verify** — confirm improvement.
6. **Document** — record findings.

## Frame Rate

### FPS Measurement

| Metric | Target | Measurement |
|---|---|---|
| Average FPS | 60 (desktop), 30 (mobile) | Rolling average |
| 1% low FPS | > 55 (desktop), > 25 (mobile) | 1st percentile |
| 0.1% low FPS | > 50 (desktop), > 20 (mobile) | 0.1th percentile |
| Frame time | < 16.67ms (60fps), < 33.33ms (30fps) | Frame time histogram |
| Frame time variance | < 2ms std dev | Standard deviation |

### FPS Testing Scenarios

| Scenario | Test Focus |
|---|---|
| Menu/idle | Baseline performance |
| Gameplay | Typical load |
| Combat | Peak load (many objects, effects) |
| Cutscene | Cinematic load |
| Loading screen | Asset streaming |
| Multiplayer | Network + local load |
| Stress test | Maximum objects/effects |

## CPU Performance

### CPU Usage

| Metric | Target | Measurement |
|---|---|---|
| Game thread CPU | < 50% | Thread profiling |
| Render thread CPU | < 30% | Thread profiling |
| Worker thread CPU | < 20% | Thread profiling |
| Total CPU usage | < 70% | System monitor |

### CPU Bottlenecks

| Bottleneck | Detection | Fix |
|---|---|---|
| Game logic | High game thread CPU | Optimize algorithms, reduce updates |
| Physics | High physics CPU | Reduce physics objects, LOD physics |
| Animation | High animation CPU | Reduce bone count, LOD animation |
| AI | High AI CPU | Reduce AI updates, LOD AI |
| Audio | High audio CPU | Reduce voice count, optimize mixing |
| UI | High UI CPU | Reduce UI updates, batch changes |

## GPU Performance

### Draw Calls

| Metric | Target | Measurement |
|---|---|---|
| Draw calls | < 100 (mobile), < 500 (desktop) | `renderer.info.render.calls` |
| Triangles | < 100k (mobile), < 1M (desktop) | `renderer.info.render.triangles` |
| Vertices | < 500k (mobile), < 5M (desktop) | Vertex count |
| Shader programs | < 20 | Program count |

### GPU Bottlenecks

| Bottleneck | Detection | Fix |
|---|---|---|
| Overdraw | High fragment shader cost | Reduce transparent objects, optimize shaders |
| Vertex processing | High vertex shader cost | Reduce vertex count, LOD geometry |
| Fragment processing | High pixel shader cost | Reduce resolution, simplify shaders |
| Texture bandwidth | High texture memory | Compress textures, reduce texture size |
| Fill rate | Low FPS at high resolution | Reduce resolution, simplify effects |

## Memory Usage

### RAM Usage

| Metric | Target | Measurement |
|---|---|---|
| Base memory | < 500MB (mobile), < 2GB (desktop) | Process memory |
| Peak memory | < 1GB (mobile), < 4GB (desktop) | Peak memory |
| Memory growth | < 10MB/min | Memory over time |
| Memory leaks | 0 | Memory leak detection |

### VRAM Usage

| Metric | Target | Measurement |
|---|---|---|
| Texture memory | < 256MB (mobile), < 1GB (desktop) | Texture memory |
| Geometry memory | < 128MB (mobile), < 512MB (desktop) | Geometry memory |
| Render targets | < 64MB | Render target memory |
| Total VRAM | < 512MB (mobile), < 2GB (desktop) | Total VRAM |

### Memory Leak Detection

| Method | Tool | Process |
|---|---|---|
| Heap snapshot | Chrome DevTools, Unity Profiler | Take snapshots, compare |
| Memory profiler | Platform-specific tools | Monitor over time |
| Object tracking | Custom instrumentation | Count objects over time |
| Leak detection | Valgrind, AddressSanitizer | Static analysis |

## Loading Times

### Initial Load

| Metric | Target | Measurement |
|---|---|---|
| Cold start | < 5s (mobile), < 3s (desktop) | Time to first frame |
| Warm start | < 2s | Time to first frame |
| Asset loading | < 10s | Time to playable |
| First interaction | < 15s | Time to first input |

### Level Transitions

| Metric | Target | Measurement |
|---|---|---|
| Level load | < 5s | Time to level ready |
| Streaming | < 1s | Time to stream assets |
| Transition | < 2s | Time for transition |

## Network Performance

### Latency

| Metric | Target | Measurement |
|---|---|---|
| Ping | < 50ms (good), < 100ms (acceptable) | Network ping |
| Jitter | < 10ms | Latency variance |
| Packet loss | < 1% | Packet loss rate |

### Bandwidth

| Metric | Target | Measurement |
|---|---|---|
| Download | < 1MB/s | Bandwidth usage |
| Upload | < 500KB/s | Bandwidth usage |
| Peak | < 5MB/s | Peak bandwidth |

## Battery & Thermal

### Mobile Performance

| Metric | Target | Measurement |
|---|---|---|
| Battery drain | < 10%/hour | Battery usage |
| Thermal throttling | Minimal | Temperature monitoring |
| Background performance | Efficient | Background CPU usage |

### Desktop Performance

| Metric | Target | Measurement |
|---|---|---|
| CPU temperature | < 80°C | Temperature monitoring |
| GPU temperature | < 85°C | Temperature monitoring |
| Fan speed | < 80% | Fan speed monitoring |
| Power consumption | < 200W | Power monitoring |

## Performance Testing Scenarios

### Baseline

- Menu/idle state
- Typical gameplay
- Single-player

### Stress

- Maximum enemies/NPCs
- Maximum particles/effects
- Maximum draw calls
- Maximum memory usage

### Edge Cases

- Low memory conditions
- High latency network
- Background apps running
- Low battery (mobile)
- Thermal throttling

## Common Performance Bugs

### Critical (P0/P1)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Unplayable FPS | < 20 FPS | Severe bottleneck | Profile, optimize critical path |
| Memory crash | Game crashes from OOM | Memory leak, excessive allocation | Fix leak, reduce memory usage |
| Infinite loading | Game never finishes loading | Deadlock, infinite loop | Fix deadlock, add timeout |
| Thermal shutdown | Device overheats, shuts down | Excessive CPU/GPU usage | Reduce load, optimize |
| Network desync | Game state diverges | Network issues, sync bugs | Fix sync, add prediction |

### Major (P2)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Low FPS | < 30 FPS | Bottleneck | Profile, optimize |
| Stuttering | Frame time spikes | GC pause, asset loading | Reduce GC, preload assets |
| Long loading | > 30s load time | Large assets, slow disk | Compress assets, optimize loading |
| High memory | > 4GB RAM | Memory leak, excessive allocation | Fix leak, reduce allocation |
| Battery drain | > 20%/hour | Excessive CPU/GPU | Reduce load, optimize |

### Minor (P3/P4)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Minor stutter | Occasional frame drops | GC pause, asset loading | Optimize GC, preload |
| Slight delay | Input lag | Processing delay | Reduce processing, prediction |
| Uneven FPS | FPS varies | Load balancing issue | Balance load across threads |
| Texture pop-in | Textures appear late | Streaming too slow | Preload textures, increase buffer |
| Audio crackle | Audio pops/clicks | Buffer underrun | Increase buffer size |

## Optimization Techniques

### CPU Optimization

| Technique | When to Use | Implementation |
|---|---|---|
| Object pooling | Frequent allocation/deallocation | Reuse objects instead of creating new |
| Job system | Parallelizable work | Distribute across threads |
| LOD | Distant objects | Reduce detail for distant objects |
| Culling | Off-screen objects | Don't update/render off-screen |
| Batching | Similar operations | Batch draw calls, state changes |
| Algorithm optimization | Slow algorithms | Use faster algorithms, data structures |

### GPU Optimization

| Technique | When to Use | Implementation |
|---|---|---|
| Draw call batching | Many small objects | Merge meshes, use instancing |
| Texture atlasing | Many small textures | Combine into atlas |
| LOD | Distant objects | Reduce polygon count |
| Occlusion culling | Hidden objects | Don't render occluded objects |
| Shader optimization | Complex shaders | Simplify, use cheaper effects |
| Resolution scaling | Fill rate bound | Render at lower resolution, upscale |

### Memory Optimization

| Technique | When to Use | Implementation |
|---|---|---|
| Asset streaming | Large assets | Load on demand, unload unused |
| Texture compression | Large textures | Use compressed formats |
| Mesh compression | Large meshes | Use compressed formats |
| Object pooling | Frequent allocation | Reuse objects |
| Garbage collection tuning | GC pauses | Tune GC frequency, use struct |

## Evidence Collection

For each performance test:

1. **Baseline** — capture initial metrics.
2. **Stress** — push to limits.
3. **Metrics** — FPS, CPU, GPU, memory, loading times.
4. **Profiles** — CPU/GPU/memory profiles.
5. **Logs** — performance logs, warnings.
6. **Comparison** — before/after optimization.

Store evidence in `.plab/session-*/evidence/performance/`.

## Engine-Specific Performance

### Unity Performance

```csharp
// Profiler
// Window > Analysis > Profiler

// Frame debugger
// Window > Analysis > Frame Debugger

// Memory profiler
// Window > Analysis > Memory Profiler

// Stats
// Game view > Stats
// Shows FPS, draw calls, triangles, etc.

// Quality settings
QualitySettings.SetQualityLevel(0);  // Low
QualitySettings.SetQualityLevel(2);  // Medium
QualitySettings.SetQualityLevel(5);  // High
```

### Unreal Performance

```cpp
// Stats commands
stat fps
stat unit
stat memory
stat scenerendering

// Unreal Insights
// Connect profiler, analyze trace

// Scalability settings
sg.ResolutionQuality 50
sg.ViewDistanceQuality 2
sg.AntiAliasingQuality 2
```

### Godot Performance

```gdscript
# Performance monitors
Performance.get_monitor(Performance.TIME_FPS)
Performance.get_monitor(Performance.TIME_PROCESS)
Performance.get_monitor(Performance.TIME_PHYSICS_PROCESS)
Performance.get_monitor(Performance.MEMORY_STATIC)
Performance.get_monitor(Performance.MEMORY_STATIC_MAX)
Performance.get_monitor(Performance.OBJECT_COUNT)
Performance.get_monitor(Performance.OBJECT_NODE_COUNT)
Performance.get_monitor(Performance.OBJECT_RESOURCE_COUNT)
Performance.get_monitor(Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME)
Performance.get_monitor(Performance.RENDER_TOTAL_PRIMITIVES_IN_FRAME)
Performance.get_monitor(Performance.RENDER_VIDEO_MEM_USED)
Performance.get_monitor(Performance.RENDER_TEXTURE_MEM_USED)
Performance.get_monitor(Performance.RENDER_BUFFER_MEM_USED)
```

### Three.js Performance

```javascript
// Renderer info
console.log("Draw calls:", renderer.info.render.calls);
console.log("Triangles:", renderer.info.render.triangles);
console.log("Geometries:", renderer.info.memory.geometries);
console.log("Textures:", renderer.info.memory.textures);

// Performance API
performance.now();
performance.memory.usedJSHeapSize;

// Custom profiler
const start = performance.now();
// ... code ...
const end = performance.now();
console.log("Execution time:", end - start, "ms");
```

## When to Stop

Stop performance audit when:

- All performance metrics measured.
- All P0/P1 findings documented.
- No new findings in last 10 tests.
- Time budget exhausted (document remaining tests).
- Platform limits prevent further testing.
- Performance targets met or documented as limitations.

## Integration with Other Audits

Performance audit findings may reveal issues in other dimensions:

- Visual glitch → visual audit
- Physics issue → physics audit
- Animation bug → animation audit
- Functional bug → functional audit
- Memory leak → memory audit

Cross-reference findings and coordinate audits.

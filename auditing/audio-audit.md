# AUDIO AUDIT

Systematic verification of audio systems: sound playback, mixing, spatial audio, music synchronization, and audio-visual integration.

## Audit Scope

Audio audit covers:

- Sound effects (SFX) playback and quality
- Music playback and synchronization
- Voice/dialogue audio
- Spatial audio (3D positioning, occlusion)
- Audio mixing (volume, panning, effects)
- Audio lifecycle (loading, unloading, memory)
- Audio-visual synchronization
- Audio performance (latency, CPU usage)

## Methodology

For each audio element:

1. **Identify** — what sound should play?
2. **Trigger** — cause the sound to play.
3. **Observe** — capture the audio.
4. **Verify** — compare observed vs expected.
5. **Document** — record finding if mismatch.

## Sound Effects (SFX)

### Playback

| Check | What to look for | Evidence |
|---|---|---|
| Trigger timing | Sound plays at correct moment | Audio waveform, timestamp |
| Volume level | Appropriate loudness | Volume meter, LUFS measurement |
| Stereo panning | Correct left/right positioning | Stereo analysis |
| Duration | Correct length | Waveform duration |
| Loop settings | Correct loop mode | Observe loop behavior |
| Priority | Important sounds not cut off | Simultaneous sounds test |

### Quality

| Check | What to look for | Evidence |
|---|---|---|
| Clipping | No distortion at max volume | Waveform analysis |
| Noise floor | Clean signal, no hiss | Spectrogram analysis |
| Frequency response | Balanced across spectrum | Frequency analysis |
| Sample rate | Consistent with game | Audio file properties |
| Bit depth | Sufficient for quality | Audio file properties |

## Music

### Playback

| Check | What to look for | Evidence |
|---|---|---|
| Track selection | Correct track for context | Audio analysis |
| Crossfading | Smooth transitions between tracks | Waveform transition |
| Loop points | Seamless loop, no gap | Loop boundary analysis |
| Tempo | Correct BPM | Beat tracking |
| Key | Correct musical key | Pitch analysis |

### Synchronization

| Check | What to look for | Evidence |
|---|---|---|
| Beat sync | Animation beats match music | Frame-by-frame analysis |
| Cutscene sync | Music hits match visual cues | Timestamp comparison |
| Gameplay sync | Music intensity matches action | Dynamic analysis |
| Tempo changes | Tempo shifts at correct moments | Beat tracking |

## Voice/Dialogue

| Check | What to look for | Evidence |
|---|---|---|
| Dialogue playback | Voice plays during dialogue | Audio analysis |
| Lip sync | Mouth movement matches speech | Visual-audio comparison |
| Subtitle sync | Subtitles match audio timing | Timestamp comparison |
| Volume balance | Voice clear over music/SFX | LUFS measurement |
| Localization | Correct language audio | Language verification |

## Spatial Audio

### 3D Positioning

| Check | What to look for | Evidence |
|---|---|---|
| Distance attenuation | Volume decreases with distance | Volume vs distance graph |
| Panning | Stereo position matches world position | Stereo analysis |
| Doppler effect | Pitch changes with movement | Pitch analysis |
| Occlusion | Sound muffled by walls | Before/after wall test |
| Reverb | Environment-appropriate reverb | Reverb analysis |

### Audio Zones

| Check | What to look for | Evidence |
|---|---|---|
| Zone transitions | Smooth audio changes between zones | Crossfade analysis |
| Zone boundaries | Correct audio at boundaries | Boundary test |
| Dynamic zones | Audio responds to gameplay | State-dependent analysis |

## Audio Mixing

### Volume & Levels

| Check | What to look for | Evidence |
|---|---|---|
| Master volume | Correct overall level | LUFS measurement |
| Music volume | Music at appropriate level | LUFS measurement |
| SFX volume | SFX at appropriate level | LUFS measurement |
| Voice volume | Voice at appropriate level | LUFS measurement |
| Dynamic range | Good dynamic range, not compressed | LUFS range analysis |

### Effects

| Check | What to look for | Evidence |
|---|---|---|
| Reverb | Appropriate reverb for environment | Reverb analysis |
| EQ | Correct frequency balance | Frequency analysis |
| Compression | Appropriate dynamic control | LUFS analysis |
| Limiter | No clipping, controlled peaks | Peak analysis |
| Distortion | No unwanted distortion | Harmonic analysis |

## Audio Lifecycle

### Loading

| Check | What to look for | Evidence |
|---|---|---|
| Load time | Audio loads quickly | Load time measurement |
| Streaming | Large files stream correctly | Buffer analysis |
| Preloading | Critical audio preloaded | Load order analysis |
| Error handling | Graceful handling of missing files | Error log analysis |

### Memory

| Check | What to look for | Evidence |
|---|---|---|
| Memory usage | Audio memory reasonable | Memory profiler |
| Unloading | Unused audio unloaded | Memory over time |
| Streaming buffer | Buffer size appropriate | Buffer analysis |
| Leak detection | No memory leaks | Memory over time |

## Audio-Visual Synchronization

| Check | What to look for | Evidence |
|---|---|---|
| Footstep sync | Foot hits ground when sound plays | Frame-by-frame analysis |
| Weapon sync | Swing matches sound | Visual-audio comparison |
| Explosion sync | Visual explosion matches sound | Timestamp comparison |
| UI sync | Button click sound matches visual | Timestamp comparison |
| Cutscene sync | Audio hits match visual cues | Timestamp comparison |

## Audio Performance

| Metric | Target | Measurement |
|---|---|---|
| Audio latency | < 20ms | Input-to-output latency |
| CPU usage | < 5% | Audio thread CPU |
| Memory usage | < 100MB | Audio memory |
| Buffer underruns | 0 | Underrun count |
| Simultaneous voices | < 32 | Active voice count |

## Common Audio Bugs

### Critical (P0/P1)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| No audio | Complete silence | Audio device issue, volume 0, file missing | Check device, volume, files |
| Audio crash | Game crashes on audio | Corrupted file, driver issue | Verify files, update drivers |
| Audio desync | Sound out of sync with visuals | Timing mismatch, buffer issue | Sync timing, adjust buffer |
| Audio loop | Sound repeats incorrectly | Loop points wrong | Fix loop points |
| Audio distortion | Harsh, clipping sound | Volume too high, bad encoding | Reduce volume, re-encode |

### Major (P2)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Wrong sound | Incorrect sound plays | Wrong file, wrong trigger | Fix file reference, trigger |
| Volume issues | Too loud/quiet | Volume settings wrong | Adjust volume, mixing |
| Panning wrong | Sound on wrong side | Pan calculation error | Fix pan calculation |
| Spatial wrong | Sound in wrong position | Position tracking error | Fix position update |
| Music wrong | Wrong track plays | Track selection error | Fix track selection |

### Minor (P3/P4)

| Bug | Symptom | Cause | Fix |
|---|---|---|---|
| Slight delay | Sound slightly late | Buffer size too large | Reduce buffer size |
| Pop/click | Audible click at start/end | Envelope issue, DC offset | Fix envelope, remove DC offset |
| Uneven volume | Some sounds louder | Inconsistent mixing | Normalize volumes |
| Missing reverb | Dry sound in space | Reverb not applied | Add reverb effect |
| Compression artifacts | Pumping, breathing | Over-compression | Reduce compression |

## Evidence Collection

For each audio test:

1. **Setup** — describe audio scenario.
2. **Trigger** — what caused audio to play.
3. **Recording** — capture audio output.
4. **Analysis** — waveform, spectrum, LUFS.
5. **Sync check** — compare with visual events.
6. **Logs** — audio engine logs, errors.

Store evidence in `.plab/session-*/evidence/audio/`.

## Engine-Specific Audio

### Unity Audio

```csharp
// AudioSource
AudioSource source = GetComponent<AudioSource>();
source.Play();
source.Stop();
source.volume = 0.5f;
source.pitch = 1.2f;

// AudioMixer
AudioMixer mixer = Resources.Load<AudioMixer>("MasterMixer");
AudioMixerGroup group = mixer.FindMatchingGroups("Music")[0];
source.outputAudioMixerGroup = group;

// Play one-shot
source.PlayOneShot(clip);
```

### Unreal Audio

```cpp
// Sound cue
USoundBase* Sound = LoadObject<USoundBase>(nullptr, TEXT("/Game/Audio/SoundCue.SoundCue"));
UGameplayStatics::PlaySound2D(this, Sound);
UGameplayStatics::PlaySoundAtLocation(this, Sound, Location);

// Audio component
UAudioComponent* AudioComp = CreateDefaultSubobject<UAudioComponent>(TEXT("AudioComp"));
AudioComp->SetSound(Sound);
AudioComp->Play();
```

### Godot Audio

```gdscript
# AudioStreamPlayer
$AudioStreamPlayer.play()
$AudioStreamPlayer.stop()
$AudioStreamPlayer.volume_db = -10.0
$AudioStreamPlayer.pitch_scale = 1.2

# AudioStreamPlayer2D/3D
$AudioStreamPlayer2D.play()
$AudioStreamPlayer3D.play()

# Audio bus
AudioServer.set_bus_volume_db(0, -10.0)
AudioServer.set_bus_mute(0, false)
```

### Three.js Audio

```javascript
// AudioListener
const listener = new THREE.AudioListener();
camera.add(listener);

// AudioLoader
const loader = new THREE.AudioLoader();
loader.load('sounds/music.mp3', (buffer) => {
    const music = new THREE.Audio(listener);
    music.setBuffer(buffer);
    music.setLoop(true);
    music.play();
});

// Positional audio
const sound = new THREE.PositionalAudio(listener);
sound.setRefDistance(1);
sound.setRolloffFactor(1);
mesh.add(sound);
sound.play();
```

## When to Stop

Stop audio audit when:

- All audio elements tested at least once.
- All P0/P1 findings documented.
- No new findings in last 10 tests.
- Time budget exhausted (document remaining tests).
- Platform limits prevent further testing.

## Integration with Other Audits

Audio audit findings may reveal issues in other dimensions:

- Visual sync → visual audit
- Animation sync → animation audit
- Performance issue → performance audit
- Functional bug → functional audit

Cross-reference findings and coordinate audits.

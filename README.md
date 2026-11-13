# ╔══════════════════════════════════════════════════════════════╗
# ║                                                              ║
# ║   ██████╗  ██╗      █████╗ ██╗     ███████╗                  ║
# ║   ██╔══██╗ ██║     ██╔══██╗██║     ██╔════╝                  ║
# ║   ██████╔╝ ██║     ███████║██║     ███████╗                  ║
# ║   ██╔═══╝  ██║     ██╔══██║██║     ╚════██║                  ║
# ║   ██║      ███████╗██║  ██║███████╗███████║                  ║
# ║   ╚═╝      ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝                  ║
# ║                                                              ║
# ║      P L A Y   L I K E   A   B O S S                          ║
# ║                                                              ║
# ║   The autonomous game intelligence for every engine.          ║
# ║   Play it. Audit it. Repair it. Ship it.                      ║
# ║                                                              ║
# ╚══════════════════════════════════════════════════════════════╝

![License: Proprietary](https://img.shields.io/badge/license-Proprietary-red)
![Engines](https://img.shields.io/badge/engines-web%20%C2%B7%20Unity%20%C2%B7%20Unreal%20%C2%B7%20Godot%20%C2%B7%20RPG%20Maker%20%C2%B7%20any-blueviolet)
![Platforms](https://img.shields.io/badge/platforms-web%20%C2%B7%20desktop%20%C2%B7%20mobile%20%C2%B7%20emulator-brightgreen)
![Format](https://img.shields.io/badge/skill-format-markdown-informational)
![Version](https://img.shields.io/badge/version-1.0.0-black)

---

## Why this exists

Every game you ship has bugs you can't see. Crashes on one GPU. Physics that
jitter at 60 FPS. Input that feels wrong in the second hour. Save corruption
that only triggers after a holiday weekend. Memory leaks that kill the
experience at minute forty.

**PLAY LIKE A BOSS (PLAB)** is an autonomous AI-agent skill that does not wait
for bug reports. It *plays* your game — across web/JS engines, Unity, Unreal,
Godot, RPG Maker, custom frameworks, mobile, desktop, and emulator targets —
audits what it experiences, diagnoses what is broken, repairs what it can, and
verifies the fix end-to-end.

It is not a linter. It is not a unit-test generator. It is a **playtester with
superpowers**: one that never gets bored, never misses a frame, and remembers
every anomaly.

> **The one-line pitch:** *Your game, played by someone who actually plays it —
> at 60 frames a second, on every engine, every time.*

---

## The loop

```
        ┌────────────────────────────────────────────┐
        │                                            │
        ▼                                            │
   ┌─────────┐    ┌─────────┐    ┌──────────┐   ┌────┴────┐
   │  PLAY   │───▶│  AUDIT  │───▶│ DIAGNOSE │──▶│  REPAIR │
   │         │    │         │    │          │   │         │
   │ Play    │    │ Check   │    │ Find the │   │ Patch   │
   │ every   │    │ every   │    │ root     │   │ code,   │
   │ mode,   │    │ system  │    │ cause,   │   │ config, │
   │ every   │    │ against │    │ not just │   │ data,   │
   │ path,   │    │ the     │    │ the      │   │ assets, │
   │ for     │    │ quality │    │ symptom  │   │ scenes  │
   │ hours   │    │ gates   │    │          │   │         │
   └─────────┘    └─────────┘    └──────────┘   └────┬────┘
        ▲                                            │
        │                                            ▼
        │                                      ┌─────────┐
        └──────────────────────────────────────│ VERIFY  │
                                               │         │
                                               │ Replay │
                                               │ the    │
                                               │ exact  │
                                               │ steps  │
                                               │ that   │
                                               │ failed │
                                               └─────────┘
```

Five stages. No shortcuts. A fix that does not survive verification does not
ship.

---

## The ten operational modes

PLAB does not have one playbook — it has ten. Each mode is a complete mission
profile with its own entry conditions, tooling, and exit criteria.

| # | Mode | Mission |
|---|------|---------|
| 01 | **Play** | Continuous gameplay across all modes, paths, and edge cases. Long sessions, stress inputs, seeded runs. |
| 02 | **Audit** | Systematic review against the quality gates — every dimension, every severity tier. |
| 03 | **Blitz** | Rapid-fire playthroughs hunting crashes, freezes, soft-locks, and lost progress. Minutes, not hours. |
| 04 | **Deep Dive** | Forensic single-system analysis: physics, AI, economy, networking — however deep the rabbit hole goes. |
| 05 | **Stress Test** | Engine-killer scenarios: thousands of entities, max draw calls, degenerate inputs, memory pressure. |
| 06 | **Regression** | Replay previously failing scenarios to prove fixes hold and nothing else broke. |
| 07 | **Smoke Test** | Fast build sanity: does it launch, load, and reach the first interactive moment? |
| 08 | **Edge Hunt** | Boundary conditions: zero values, negative numbers, overflow, empty inventories, corrupt saves. |
| 09 | **Multiplayer Audit** | Desyncs, race conditions, host migration, latency, cheating surface — for online titles. |
| 10 | **Post-Ship Patrol** | Continuous monitoring after release: telemetry, reviews, crash dumps, live repros. |

---

## What gets audited

Every audit runs against the **quality gates** — the bar a game must clear
before it is allowed to call itself finished.

- **Stability** — crashes, exceptions, hangs, freezes, watchdog kills
- **Performance** — frame pacing, draw calls, memory, GC pressure, shader stutter
- **Correctness** — logic bugs, state machines, save/load fidelity, progression blockers
- **Input feel** — latency, buffering, dead zones, remapping, accessibility
- **Physics & world** — tunneling, jitter, NaN positions, collision fidelity
- **AI behavior** — stuck agents, navmesh failures, difficulty curves, exploits
- **Economy & balance** — currency exploits, soft-locks, degenerate strategies
- **Networking** — latency, desync, packet loss, authority bugs, exploits
- **Audio** — missing cues, clipping, sync drift, memory leaks in streams
- **UX & accessibility** — onboarding, localization, colorblind safety, remapping, haptics
- **Security** — client trust violations, injection surfaces, save tampering
- **Content integrity** — missing assets, broken references, localization gaps

Each dimension is scored. Each finding is filed. Nothing is "probably fine."

---

## Finding format — `PLAB-NNNN`

Every defect gets a permanent, traceable ID. No more "that one bug in the
inventory screen."

```
PLAB-0042  [P1]  Save corruption on quit during autosave
  Engine:   Unity 2022.3 LTS
  Platform: Windows / Steam
  Repro:    1. Play 45+ min  2. Trigger autosave  3. Alt+F4 within 2 s
  Expected: Save completes, progress retained
  Actual:   Save file truncated; profile falls back to last cloud sync
  Evidence: crash dump + save.log excerpt + frame capture
  Status:   CONFIRMED → REPAIRED → VERIFIED
```

### Severity ladder

| Tier | Meaning | SLA |
|------|---------|-----|
| **P0** | Crash / data loss / security | Fix before anything else ships |
| **P1** | Major gameplay or progression blocker | Current sprint |
| **P2** | Noticeable defect, workaround exists | Next sprint |
| **P3** | Polish, edge case, minor annoyance | Backlog |
| **P4** | Cosmetic, informational, future-proofing | Opportunistic |

---

## The Blind-Spot Hunter

The most dangerous bugs are the ones your test suite cannot imagine: the
interaction between two systems that were each tested in isolation. The
Blind-Spot Hunter exists for exactly this class of defect.

It works by:

1. **Mapping** the game's system graph — what touches what, and how.
2. **Generating** adversarial interaction scenarios the designers never wrote down.
3. **Executing** them under instrumentation that watches every subsystem simultaneously.
4. **Correlating** anomalies across systems to surface emergent failures.

Examples it has caught in the wild:

- Inventory full + autosave + network disconnect = item duplication exploit
- Dialogue skip spam during a cutscene transition = soft-lock on next map load
- Pause menu opened during a physics-heavy explosion = rigidbody NaN cascade

If a bug requires *two things to happen at once* and nobody thought to test
that combination, the Blind-Spot Hunter is already on it.

---

## Quality gates

A game does not ship because it "feels done." It ships when every gate passes.

```
GATE 1  LAUNCH      boots, loads, reaches gameplay in < target time
GATE 2  STABILITY   zero P0/P1 findings across N consecutive sessions
GATE 3  PERFORMANCE meets frame budget at p95 on min-spec hardware
GATE 4  COVERAGE    all modes, all systems, all save states exercised
GATE 5  REGRESSION  previously fixed findings remain fixed
GATE 6  BLIND SPOT  adversarial interaction suite passes clean
```

Gates are not suggestions. A failed gate is a failed release — or a documented,
signed-off exception with a remediation plan.

---

## Final verdicts

Every audit ends with a verdict. No ambiguity.

| Verdict | Meaning |
|---------|---------|
| **SHIP IT** | All gates pass. Zero open P0/P1. Confidence: high. |
| **SHIP WITH WATCH** | Minor open findings, all P3/P4 or documented exceptions. Monitor post-ship. |
| **FIX FIRST** | Open P0/P1 findings or a failed gate. Do not ship. |
| **NEEDS HUMAN** | Ambiguity the agent cannot resolve — requires designer/engineer judgment. |

---

## Installation

PLAB is an AI-agent skill — a structured folder of instructions, modules, and
templates that your agent loads and follows. It is not a game, a library, or a
CLI tool. You install it into your agent's skill directory.

### Option A — manual drop-in

```bash
# Clone or copy the repository into your agent's skills directory.
# The exact path depends on your agent; common conventions:

# Claude-style skills directory
cp -r play-like-a-boss ~/.claude/skills/play-like-a-boss

# Generic agent skills directory
cp -r play-like-a-boss /path/to/your-agent/skills/play-like-a-boss

# Or symlink for live updates
ln -s /path/to/play-like-a-boss ~/.claude/skills/play-like-a-boss
```

### Option B — managed skills

If your agent supports managed skill installation (registry, package manager,
or plugin system), install `play-like-a-boss` the same way you would any other
skill package. The skill folder contains everything needed — no external
dependencies beyond what your agent already provides.

### Verify the install

Open a session with your agent pointed at a game project and say:

```
/play-like-a-boss smoke test this build
```

If PLAB responds with a mission profile and begins executing, you are live.

---

## Usage — trigger phrases

PLAB activates on intent. Use any of these, or describe what you want in plain
language and the skill will route itself.

| You say | PLAB does |
|---------|-----------|
| `/plab play` | Full play session across all modes |
| `/plab audit` | Systematic audit against all quality gates |
| `/plab blitz` | Rapid crash/hang/progression hunt |
| `/plab stress` | Engine-killer stress scenarios |
| `/plab regression PLAB-0042` | Replay and verify a specific fix |
| `/plab blind-spot` | Run the adversarial interaction hunter |
| `/plab smoke` | Fast launch sanity check |
| `/plab edge` | Boundary and degenerate-input hunt |
| `/plab multiplayer` | Networked-game audit |
| `/plab patrol` | Post-ship monitoring mode |
| `/plab fix PLAB-0042` | Diagnose and repair a specific finding |
| `/plab verdict` | Generate the final ship/fix-first verdict |

You can also just describe the problem:

```
"This Unity game crashes on Mac but not Windows. Find out why."
"Audit the save system for corruption edge cases."
"Play this RPG Maker game for 2 hours and tell me if the economy breaks."
```

PLAB will pick the right mode, load the right modules, and get to work.

---

## Repository layout

```
play-like-a-boss/
├── SKILL.md                  # The skill manifest — entry point for the agent
├── README.md                 # This file
├── LICENSE                   # Proprietary license (PT. Agra Karya Digital)
│
├── core/                     # Shared infrastructure every mode uses
│   ├── engine-detection.md   # Identify the engine, version, platform targets
│   ├── session-management.md # Play session lifecycle, logging, state capture
│   ├── instrumentation.md    # Hooks, probes, telemetry collection points
│   └── evidence.md           # How findings are captured, stored, referenced
│
├── adapters/                 # Engine-specific playbooks
│   ├── web-js.md             # Browser engines, Canvas, WebGL, Phaser, PixiJS
│   ├── unity.md              # Unity: play mode, editor scripting, builds
│   ├── unreal.md             # Unreal: PIE, packaged builds, automation
│   ├── godot.md              # Godot: editor, export templates, headless
│   ├── rpg-maker.md          # RPG Maker MZ/MV/VX: playtest, event inspection
│   ├── mobile.md             # iOS/Android: simulators, devices, emulators
│   ├── desktop.md            # Native builds: Windows, macOS, Linux
│   └── emulator.md           # Retro/console emulation targets
│
├── auditing/                 # The audit engine
│   ├── quality-gates.md      # The six gates and their pass criteria
│   ├── dimensions.md         # All audit dimensions and checklists
│   ├── severity.md           # P0–P4 classification rules
│   ├── blind-spot-hunter.md  # Adversarial interaction methodology
│   └── verdicts.md           # SHIP IT / SHIP WITH WATCH / FIX FIRST / NEEDS HUMAN
│
├── repair/                   # Fix methodology
│   ├── diagnosis.md          # Root-cause analysis framework
│   ├── patching.md           # Safe patch patterns per engine type
│   ├── verification.md       # Post-fix replay and regression protocol
│   └── rollback.md           # When and how to revert a repair
│
├── testing/                  # Test scenario library
│   ├── scenario-templates.md # Reusable playtest scenario structures
│   ├── stress-scenarios.md   # Engine-killer scenario catalog
│   ├── edge-cases.md         # Boundary condition catalog
│   └── regression-suite.md   # How to build and maintain a regression suite
│
└── templates/                # Output templates
    ├── finding.md            # PLAB-NNNN finding report format
    ├── audit-report.md       # Full audit report structure
    ├── mission-patch.md      # Mission briefing / patch notes format
    └── verdict.md            # Final verdict document
```

---

## What PLAB is not

- **Not a replacement for your engineers.** It finds and fixes what it can,
  and escalates what it cannot. The `NEEDS HUMAN` verdict exists for a reason.
- **Not a substitute for design judgment.** It audits against quality gates,
  not against your creative vision. That part is still yours.
- **Not magic.** It plays your game the way a very thorough, very patient
  playtester would — but faster, longer, and with perfect memory. The bugs it
  finds are real. The fixes it proposes are verified. The verdicts are honest.

---

## The manifesto

> We believe every game deserves to be played before it is shipped — not by a
> checklist, not by a QA contractor on a deadline, but by something that plays
> it the way players actually will: for hours, at the edges, in the weird
> combinations nobody wrote down.
>
> We believe bugs are not a cost of shipping. They are a debt you carry into
> every session, every review, every refund. Pay it down before your players
> have to.
>
> We believe the best game is the one where the player never thinks about the
> game. No crashes. No soft-locks. No "wait, did I just lose an hour of
> progress?" PLAB exists to make that feeling the default.
>
> We built this because we got tired of shipping games that felt 90% done.
> The last 10% is where players decide whether they come back.
>
> **Play like a boss. Ship like a boss.**

---

## License

PLAY LIKE A BOSS is **proprietary software**. All rights reserved.

© 2026 PT. Agra Karya Digital (VeryCoolApps). See [LICENSE](LICENSE) for full
terms. Personal and internal business use is permitted. Redistribution as a
competing skill or product is not.

---

# Versi Bahasa Indonesia

---

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ██████╗  ██╗      █████╗ ██╗     ███████╗                  ║
║   ██╔══██╗ ██║     ██╔══██╗██║     ██╔════╝                  ║
║   ██████╔╝ ██║     ███████║██║     ███████╗                  ║
║   ██╔═══╝  ██║     ██╔══██║██║     ╚════██║                  ║
║   ██║      ███████╗██║  ██║███████╗███████║                  ║
║   ╚═╝      ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝                  ║
║                                                              ║
║      P L A Y   L I K E   A   B O S S                          ║
║                                                              ║
║   Kecerdasan game otonom untuk semua engine.                 ║
║   Mainkan. Audit. Perbaiki. Rilis.                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

## Mengapa ini ada

Setiap game yang kamu rilis punya bug yang tidak bisa kamu lihat. Crash di
satu GPU. Fisika yang patah-patah di 60 FPS. Input yang terasa aneh setelah
satu jam bermain. Save yang corrupt setelah liburan panjang. Memory leak yang
membunuh pengalaman di menit keempat puluh.

**PLAY LIKE A BOSS (PLAB)** adalah skill AI-agent otonom yang tidak menunggu
laporan bug. Ia **memainkan** game kamu — di engine web/JS, Unity, Unreal,
Godot, RPG Maker, framework kustom, mobile, desktop, dan target emulator —
mengaudit apa yang dialaminya, mendiagnosis apa yang rusak, memperbaiki apa
yang bisa diperbaiki, dan memverifikasi perbaikannya secara end-to-end.

Ini bukan linter. Ini bukan generator unit test. Ini adalah **playtester
dengan kekuatan super**: tidak pernah bosan, tidak pernah melewatkan satu
frame, dan mengingat setiap anomali.

> **Pitch satu kalimat:** *Game kamu, dimainkan oleh sesuatu yang benar-benar
> memainkannya — pada 60 frame per detik, di setiap engine, setiap saat.*

---

## Siklusnya

```
        ┌────────────────────────────────────────────┐
        │                                            │
        ▼                                            │
   ┌─────────┐    ┌─────────┐    ┌──────────┐   ┌────┴────┐
   │  MAIN   │───▶│  AUDIT  │───▶│ DIAGNOSA │──▶│ PERBAIK│
   │         │    │         │    │          │   │         │
   │ Mainkan │    │ Periksa │    │ Temukan  │   │ Tambal  │
   │ semua   │    │ setiap  │    │ akar      │   │ kode,   │
   │ mode,   │    │ sistem  │    │ masalah,  │   │ config, │
   │ semua   │    │ terhadap│    │ bukan     │   │ data,   │
   │ jalur,  │    │ quality │    │ hanya     │   │ aset,   │
   │ selama  │    │ gates   │    │ gejala    │   │ scene   │
   │ berjam- │    │          │    │          │   │         │
   │ -jam    │    │          │    │          │   │         │
   └─────────┘    └─────────┘    └──────────┘   └────┬────┘
        ▲                                            │
        │                                            ▼
        │                                      ┌─────────┐
        └──────────────────────────────────────│ VERIFIKASI│
                                               │         │
                                               │ Ulangi  │
                                               │ langkah │
                                               │ yang    │
                                               │ gagal   │
                                               └─────────┘
```

Lima tahap. Tanpa jalan pintas. Perbaikan yang tidak lolos verifikasi tidak
dikirim.

---

## Sepuluh mode operasional

PLAB tidak punya satu buku panduan — ia punya sepuluh. Setiap mode adalah
profil misi lengkap dengan kondisi masuk, tooling, dan kriteria keluar
masing-masing.

| # | Mode | Misi |
|---|------|------|
| 01 | **Play** | Gameplay berkelanjutan di semua mode, jalur, dan edge case. Sesi panjang, input stres, run berseed. |
| 02 | **Audit** | Tinjauan sistematis terhadap quality gates — setiap dimensi, setiap tingkat keparahan. |
| 03 | **Blitz** | Playthrough cepat untuk memburu crash, freeze, soft-lock, dan progress hilang. Menit, bukan jam. |
| 04 | **Deep Dive** | Analisis forensik satu sistem: fisika, AI, ekonomi, networking — sedalam apa pun. |
| 05 | **Stress Test** | Skenario pembunuh engine: ribuan entitas, draw call maksimal, input degenerate, tekanan memori. |
| 06 | **Regression** | Ulangi skenario yang sebelumnya gagal untuk membuktikan perbaikan bertahan dan tidak ada yang lain rusak. |
| 07 | **Smoke Test** | Sanity build cepat: apakah game launch, load, dan mencapai momen interaktif pertama? |
| 08 | **Edge Hunt** | Kondisi batas: nilai nol, angka negatif, overflow, inventory kosong, save corrupt. |
| 09 | **Multiplayer Audit** | Desync, race condition, host migration, latensi, permukaan cheating — untuk game online. |
| 10 | **Post-Ship Patrol** | Monitoring berkelanjutan setelah rilis: telemetri, review, crash dump, repro live. |

---

## Apa yang diaudit

Setiap audit berjalan terhadap **quality gates** — standar yang harus dilewati
game sebelum boleh menyebut dirinya selesai.

- **Stabilitas** — crash, exception, hang, freeze, watchdog kill
- **Performa** — frame pacing, draw call, memori, tekanan GC, stutter shader
- **Kebenaran** — bug logika, state machine, fidelitas save/load, blocker progresi
- **Feel input** — latensi, buffering, dead zone, remapping, aksesibilitas
- **Fisika & dunia** — tunneling, jitter, posisi NaN, fidelitas collision
- **Perilaku AI** — agen stuck, kegagalan navmesh, kurva kesulitan, exploit
- **Ekonomi & balance** — exploit currency, soft-lock, strategi degenerate
- **Networking** — latensi, desync, packet loss, bug authority, exploit
- **Audio** — cue hilang, clipping, drift sinkronisasi, memory leak di stream
- **UX & aksesibilitas** — onboarding, lokalisasi, keamanan colorblind, remapping, haptics
- **Keamanan** — pelanggaran client trust, permukaan injeksi, save tampering
- **Integritas konten** — aset hilang, referensi rusak, gap lokalisasi

Setiap dimensi dinilai. Setiap temuan dicatat. Tidak ada yang "kemungkinan
aman."

---

## Format temuan — `PLAB-NNNN`

Setiap defect mendapat ID permanen yang bisa dilacak. Tidak ada lagi "bug di
layar inventory itu."

```
PLAB-0042  [P1]  Save corrupt saat quit selama autosave
  Engine:   Unity 2022.3 LTS
  Platform: Windows / Steam
  Repro:    1. Main 45+ menit  2. Picu autosave  3. Alt+F4 dalam 2 detik
  Diharapkan: Save selesai, progress tersimpan
  Aktual:    File save terpotong; profil fallback ke cloud sync terakhir
  Bukti:     crash dump + cuplikan save.log + capture frame
  Status:    Dikonfirmasi → DIPERBAIKI → TERVERIFIKASI
```

### Tangga keparahan

| Tier | Arti | SLA |
|------|------|-----|
| **P0** | Crash / kehilangan data / keamanan | Perbaiki sebelum apa pun dirilis |
| **P1** | Blocker gameplay atau progresi besar | Sprint berjalan |
| **P2** | Defect terasa, ada workaround | Sprint berikutnya |
| **P3** | Polish, edge case, gangguan minor | Backlog |
| **P4** | Kosmetik, informasional, future-proofing | Opportunistik |

---

## Blind-Spot Hunter

Bug paling berbahaya adalah yang tidak bisa dibayangkan oleh test suite kamu:
interaksi antara dua sistem yang masing-masing diuji secara terisolasi.
Blind-Spot Hunter ada persis untuk kelas defect ini.

Cara kerjanya:

1. **Pemetaan** graph sistem game — apa menyentuh apa, dan bagaimana.
2. **Generasi** skenario interaksi adversarial yang tidak pernah ditulis desainer.
3. **Eksekusi** di bawah instrumentasi yang mengawasi semua subsistem sekaligus.
4. **Korelasi** anomali lintas sistem untuk memunculkan kegagalan emergent.

Contoh yang pernah ditangkap di lapangan:

- Inventory penuh + autosave + disconnect jaringan = exploit duplikasi item
- Spam skip dialog saat transisi cutscene = soft-lock saat load map berikutnya
- Menu pause dibuka saat ledakan berat fisika = cascade rigidbody NaN

Kalau bug butuh *dua hal terjadi bersamaan* dan tidak ada yang terpikir untuk
tes kombinasi itu, Blind-Spot Hunter sudah mengerjakannya.

---

## Quality gates

Game tidak rilis karena "terasa sudah selesai." Game rilis ketika setiap gate
lolos.

```
GATE 1  LAUNCH      boot, load, mencapai gameplay dalam waktu target
GATE 2  STABILITAS nol temuan P0/P1 di N sesi berurutan
GATE 3  PERFORMA   memenuhi budget frame di p95 pada hardware min-spec
GATE 4  COVERAGE   semua mode, semua sistem, semua state save diuji
GATE 5  REGRESI    temuan yang sudah diperbaiki tetap diperbaiki
GATE 6  BLIND SPOT suite interaksi adversarial lolos bersih
```

Gate bukan saran. Gate yang gagal adalah rilis yang gagal — atau pengecualian
yang terdokumentasi, disetujui tertulis, dengan rencana remediasi.

---

## Verdict akhir

Setiap audit berakhir dengan verdict. Tanpa ambiguitas.

| Verdict | Arti |
|---------|------|
| **SHIP IT** | Semua gate lolos. Nol temuan P0/P1 terbuka. Keyakinan: tinggi. |
| **SHIP WITH WATCH** | Temuan minor terbuka, semua P3/P4 atau pengecualian terdokumentasi. Pantau pasca-rilis. |
| **FIX FIRST** | Ada temuan P0/P1 terbuka atau gate gagal. Jangan rilis. |
| **NEEDS HUMAN** | Ambiguitas yang tidak bisa diselesaikan agent — butuh judgment desainer/engineer. |

---

## Instalasi

PLAB adalah skill AI-agent — folder terstruktur berisi instruksi, modul, dan
template yang dimuat dan diikuti agent kamu. Ini bukan game, bukan library,
bukan CLI tool. Kamu menginstalnya ke direktori skill agent kamu.

### Opsi A — drop-in manual

```bash
# Clone atau salin repo ke direktori skills agent kamu.
# Path persisnya tergantung agent; konvensi umum:

# Direktori skills gaya Claude
cp -r play-like-a-boss ~/.claude/skills/play-like-a-boss

# Direktori skills generik
cp -r play-like-a-boss /path/to/agent-kamu/skills/play-like-a-boss

# Atau symlink untuk update live
ln -s /path/to/play-like-a-boss ~/.claude/skills/play-like-a-boss
```

### Opsi B — managed skills

Kalau agent kamu mendukung instalasi skill terkelola (registry, package
manager, atau plugin system), instal `play-like-a-boss` seperti kamu
menginstal package skill lain. Folder skill berisi semuanya — tidak ada
dependensi eksternal di luar yang sudah disediakan agent kamu.

### Verifikasi instalasi

Buka sesi dengan agent kamu yang mengarah ke project game dan katakan:

```
/play-like-a-boss smoke test build ini
```

Kalau PLAB merespons dengan profil misi dan mulai eksekusi, kamu sudah live.

---

## Penggunaan — frasa pemicu

PLAB aktif berdasarkan intent. Pakai salah satu di bawah ini, atau jelaskan
yang kamu mau dengan bahasa sehari-hari dan skill akan merutekan dirinya
sendiri.

| Kamu bilang | PLAB melakukan |
|-------------|----------------|
| `/plab play` | Sesi main penuh di semua mode |
| `/plab audit` | Audit sistematis terhadap semua quality gates |
| `/plab blitz` | Perburuan crash/hang/progresi cepat |
| `/plab stress` | Skenario stress pembunuh engine |
| `/plab regression PLAB-0042` | Ulangi dan verifikasi perbaikan tertentu |
| `/plab blind-spot` | Jalankan pemburu interaksi adversarial |
| `/plab smoke` | Sanity launch cepat |
| `/plab edge` | Perburuan kondisi batas dan input degenerate |
| `/plab multiplayer` | Audit game networked |
| `/plab patrol` | Mode monitoring pasca-rilis |
| `/plab fix PLAB-0042` | Diagnosa dan perbaiki temuan tertentu |
| `/plab verdict` | Hasilkan verdict ship/fix-first akhir |

Kamu juga bisa langsung menjelaskan masalahnya:

```
"Game Unity ini crash di Mac tapi tidak di Windows. Cari tahu kenapa."
"Audit sistem save untuk edge case corrupt."
"Mainkan game RPG Maker ini 2 jam dan bilang kalau ekonominya rusak."
```

PLAB akan memilih mode yang tepat, memuat modul yang tepat, dan mulai bekerja.

---

## Struktur repo

```
play-like-a-boss/
├── SKILL.md                  # Manifest skill — entry point untuk agent
├── README.md                 # File ini
├── LICENSE                   # Lisensi proprietari (PT. Agra Karya Digital)
│
├── core/                     # Infrastruktur bersama yang dipakai semua mode
│   ├── engine-detection.md   # Identifikasi engine, versi, target platform
│   ├── session-management.md # Lifecycle sesi main, logging, capture state
│   ├── instrumentation.md    # Hook, probe, titik pengumpulan telemetri
│   └── evidence.md           # Cara temuan dicapture, disimpan, direferensikan
│
├── adapters/                 # Playbook spesifik engine
│   ├── web-js.md             # Engine browser, Canvas, WebGL, Phaser, PixiJS
│   ├── unity.md              # Unity: play mode, editor scripting, build
│   ├── unreal.md             # Unreal: PIE, packaged build, otomasi
│   ├── godot.md              # Godot: editor, export template, headless
│   ├── rpg-maker.md          # RPG Maker MZ/MV/VX: playtest, inspeksi event
│   ├── mobile.md             # iOS/Android: simulator, device, emulator
│   ├── desktop.md            # Build native: Windows, macOS, Linux
│   └── emulator.md           # Target emulasi retro/konsol
│
├── auditing/                 # Mesin audit
│   ├── quality-gates.md      # Enam gate dan kriteria lolosnya
│   ├── dimensions.md         # Semua dimensi audit dan checklistnya
│   ├── severity.md           # Aturan klasifikasi P0–P4
│   ├── blind-spot-hunter.md  # Metodologi interaksi adversarial
│   └── verdicts.md           # SHIP IT / SHIP WITH WATCH / FIX FIRST / NEEDS HUMAN
│
├── repair/                   # Metodologi perbaikan
│   ├── diagnosis.md          # Framework analisis akar masalah
│   ├── patching.md           # Pola patch aman per tipe engine
│   ├── verification.md       # Protokol replay dan regresi pasca-perbaikan
│   └── rollback.md           # Kapan dan bagaimana revert perbaikan
│
├── testing/                  # Library skenario test
│   ├── scenario-templates.md # Struktur skenario playtest yang reusable
│   ├── stress-scenarios.md   # Katalog skenario pembunuh engine
│   ├── edge-cases.md         # Katalog kondisi batas
│   └── regression-suite.md   # Cara membangun dan merawat regression suite
│
└── templates/                # Template output
    ├── finding.md            # Format laporan temuan PLAB-NNNN
    ├── audit-report.md       # Struktur laporan audit lengkap
    ├── mission-patch.md      # Format briefing misi / patch notes
    └── verdict.md            # Dokumen verdict akhir
```

---

## Apa yang PLAB bukan

- **Bukan pengganti engineer kamu.** Ia menemukan dan memperbaiki apa yang
  bisa, dan eskalasi apa yang tidak bisa. Verdict `NEEDS HUMAN` ada karena
  alasannya.
- **Bukan pengganti judgment desain.** Ia mengaudit terhadap quality gates,
  bukan terhadap visi kreatif kamu. Bagian itu tetap milikmu.
- **Bukan sulap.** Ia memainkan game kamu seperti playtester yang sangat
  teliti dan sangat sabar — tapi lebih cepat, lebih lama, dan dengan memori
  sempurna. Bug yang ditemukan nyata. Perbaikan yang diusulkan terverifikasi.
  Verdict-nya jujur.

---

## Manifesnya

> Kami percaya setiap game berhak dimainkan sebelum dirilis — bukan oleh
> checklist, bukan oleh kontraktor QA dengan deadline, tapi oleh sesuatu yang
> memainkannya seperti pemain sungguhan akan: berjam-jam, di tepi, dalam
> kombinasi aneh yang tidak pernah ditulis siapa pun.
>
> Kami percaya bug bukan biaya merilis. Bug adalah utang yang kamu bawa ke
> setiap sesi, setiap review, setiap refund. Lunasi sebelum pemainmu yang
> harus membayarnya.
>
> Kami percaya game terbaik adalah yang pemainnya tidak pernah memikirkan
> game-nya. Tanpa crash. Tanpa soft-lock. Tanpa "tunggu, apakah aku baru saja
> kehilangan satu jam progress?" PLAB ada untuk menjadikan perasaan itu
> default.
>
> Kami membangun ini karena lelah merilis game yang terasa 90% selesai.
> 10% terakhir adalah tempat pemain memutuskan apakah mereka kembali.
>
> **Mainkan seperti bos. Rilis seperti bos.**

---

## Lisensi

PLAY LIKE A BOSS adalah **software proprietari**. Hak cipta dilindungi.

© 2026 PT. Agra Karya Digital (VeryCoolApps). Lihat [LICENSE](LICENSE) untuk
ketentuan lengkap. Penggunaan personal dan bisnis internal diperbolehkan.
Redistribusi sebagai skill atau produk yang bersaing tidak diperbolehkan.

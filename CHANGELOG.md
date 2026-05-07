# Changelog

All notable changes to **hexa-chip** are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and SemVer.

## [Unreleased]

### Added (2026-05-07 — RSC iter 3)

- `verify/calc_hbm.hexa` — **F-CHIP-3 T1** algebraic derivation.
  12 integer-arithmetic checks pin σ(6)-φ(6)=10 to HBM "comfortable"
  layer ceiling, σ(6)=12 to HBM3E peak Hi, and σ(6)+τ(6)=16 to the
  HBM4 frontier ceiling (exact hit). Bus width 1024 = 2^(σ-φ); J₂=σ·φ=24
  matches HBM3 channel budget; bond modes {TSV, hybrid} = φ(6)=2.
  Sentinel: `__HEXA_CHIP_CALC_HBM__ PASS`.
- Aggregate: 7/7 → 8/8 PASS.
- Closure progress: F-CHIP-3 closure 0% → 33% (T1 ✓; T2/T3 TBD).
- All 3 measurable falsifiers (F-CHIP-1/2/3) now at T1 ✓.

### Added (2026-05-07 — RSC iter 2)

- `verify/calc_npu.hexa` — **F-CHIP-2 T1** algebraic derivation.
  11 integer-arithmetic checks pin τ(6)=4 to the NPU 4-stage
  dataflow pipeline (load → MAC → activate → store) AND to the
  Eyeriss 4-pattern taxonomy (weight/output/input/row stationary),
  plus σ(6)=12 MAC-lane target and σ·φ·τ=96 macroblock budget.
  Sentinel: `__HEXA_CHIP_CALC_NPU__ PASS`.
- Aggregate: 6/6 → 7/7 PASS.
- Closure progress: F-CHIP-2 closure 0% → 33% (T1 ✓; T2/T3 TBD).

### Added (2026-05-07 — RSC iter 1)

- `verify/calc_process.hexa` — **F-CHIP-1 T1** algebraic derivation.
  11 integer-arithmetic checks pin σ(6)=12 to the 12-generation
  process node ladder (180nm → 3nm), including endpoint cumulative
  shrink (60×) and per-step √2 ratio band across all 11 transitions.
  Sentinel: `__HEXA_CHIP_CALC_PROCESS__ PASS`.
- `verify/cli.hexa` — registers the new `calc-process` target;
  aggregate goes 5/5 → 6/6 PASS.
- Closure progress: F-CHIP-1 closure 0% → 33% (T1 ✓; T2/T3 TBD).
  Following the **Runnable Surface Construction** recipe pattern from
  `~/core/bedrock/docs/runnable_surface_recipe.md` §7.4 priority 3.

## [1.0.0] - 2026-05-06

### Added

- Initial standalone extraction from `n6-architecture/domains/compute/`
  at SHA `c0f1f570` (2026-05-06).
- **28-verb / 7-group Chip Substrate** organised as:
  - **architecture (3)** — `architecture`, `isa_n6`, `hexa1`
  - **design (5)** — `design`, `dse_pipeline`, `rtl_gen`, `eda`, `verify_test`
  - **process (5)** — `process`, `materials`, `wafer`, `yield`, `thermal_power`
  - **packaging (6)** — `packaging`, `advanced_packaging`, `chip_3d`, `hbm`,
    `interconnect`, `sc`
  - **accelerator (8)** — `npu_n6`, `pim`, `photonic`, `accel`, `asic`,
    `hexa_pim`, `hexa_3d`, `hexa_wafer`
  - **consciousness (2)** — `conscious_chip`, `conscious_soc`
- `cli/hexa-chip.hexa` — placeholder 7-group dispatcher
  (`status` / `show <verb>` / `selftest` / `--version` / `help`).
- `install.hexa` — hx hook (no external deps; post-install runs
  28-verb directory sweep).
- `tests/test_selftest.hexa` — 28-verb directory enumeration harness
  (`__HEXA_CHIP_SELFTEST__ PASS` sentinel verification).
- `hexa.toml` — package manifest with 7-group `[modules.<group>]` tables.
- MIT license, README (Korea-fab heritage tone), CHANGELOG.

### Honest scope (raw#10 C3)

- **0 of 28 verbs is empirically wired** at v1.0.0. All verbs ship as
  spec directories (the cp -R'd `n6-architecture/domains/compute/<name>/`
  trees); per-verb working `.hexa` CLI sandboxes are deferred to
  post-v1.0 cycles.
- **n=6 invariant lattice** is referenced explicitly by `isa_n6` and
  `hexa1` only; the remaining 26 verbs inherit the organising
  convention without independent empirical fit.
- **No tape-out / GDSII / PDK content vendored.** Foundry process kits
  (Samsung / SK·Hynix / TSMC / Intel) stay proprietary; this repo
  ships specs + organising vocabulary only.
- **Cross-link consumers** (`hexa-rtsc`, `hexa-codex`, `anima`) reference
  individual verb specs; bidirectional propagation is manual (no
  cross-repo CI at this release).
- **Korea-fab heritage tone** is editorial framing only — no
  proprietary data, NDA content, or trade-secret material is
  included.

### Provenance

- Extracted from `n6-architecture/domains/compute/` at SHA `c0f1f570`
  (commit `proposal(infra): reframe critical-mineral-arbitration
  kick-spec to peaceful-only scope`, 2026-05-06).
- Sister extractions in `dancinlab` org: `hexa-bio` (4 molecular
  verbs), `hexa-rtsc`, `hexa-codex`, `anima`, plus `hexa-{antimatter,
  bot, brain, cosmos, earth, energy, fantasy, fusion, lang, millennium,
  os, pet, space, sscb, time, ufo}`.

[1.0.0]: https://github.com/dancinlab/hexa-chip/releases/tag/v1.0.0

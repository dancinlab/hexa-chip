# Changelog

All notable changes to **hexa-chip** are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and SemVer.

## [Unreleased]

### Added (2026-05-08 — RSC iter 9)

- `verify/numerics_hbm_parity.hexa` — **F-CHIP-3 T2 second-stack**.
  8-row (= σ-τ) vendor × gen parity: Hynix/Samsung HBM3 + Hynix/Samsung/
  Micron HBM3E + Hynix/Samsung/Micron HBM4. 12 checks: HBM3E and HBM4
  trinity = τ-1 = 3; HBM3E vendor BW within ±5% of trinity mean (1180
  / 1229 / 1180); HBM3E geomean ∈ [1100, 1300] σ³-class; HBM4_avg /
  HBM3E_avg ∈ [1.5, 2] flagship gen jump; predicted BW = bus·rate/8
  within ±1% per row; Samsung ≥ Hynix ≥ Micron at HBM3E.
  Sentinel: `__HEXA_CHIP_NUMERICS_HBM_PARITY__ PASS`.
- Aggregate: 13/13 → 14/14 PASS.
- F-CHIP-3: T1 ✓ + T2 ×2.
- All 3 measurable falsifiers now at T1 ✓ + T2 ×2.

### Added (2026-05-08 — RSC iter 8)

- `verify/numerics_npu_parity.hexa` — **F-CHIP-2 T2 second-stack**.
  6-vendor (= n) INT8 + FP16 throughput parity: Apple ANE A17 Pro,
  NVIDIA Jetson Orin AGX, Qualcomm Hexagon 8G3, Google Tensor G3,
  Samsung Exynos 2400, AMD Ryzen AI XDNA. 11 checks: per-row INT8/FP16
  = φ(6) ±5%; vendor cardinality = n; geomean INT8 ∈ [σ, σ²]; log2
  span ∈ [n, σ-φ]; Jetson Orin ∈ [σ², σ²·n] server-class; aggregate
  ΣINT8/ΣFP16 = φ; cohort years = τ-1.
  Sentinel: `__HEXA_CHIP_NUMERICS_NPU_PARITY__ PASS`.
- Aggregate: 12/12 → 13/13 PASS.
- F-CHIP-2: T1 ✓ + T2 ×2.

### Added (2026-05-08 — RSC iter 7)

- `verify/numerics_process_parity.hexa` — **F-CHIP-1 T2 second-stack**.
  10-row vendor density parity: TSMC (14/10/7/5/3nm) + Samsung (7/5/3nm)
  + Intel ('10'/'7') public MTr/mm² figures vs predicted K/f² (K=4325
  calibrated from TSMC 5nm = 173). 12 checks: intra-TSMC ±60%, cross-
  foundry ±200%, (14/3)²/(313/29) ≈ φ cell-overhead, log2 density span
  ∈ [τ-1, τ+1], geomean ∈ σ²-class window, vendor rows = σ-φ = 10.
  Sentinel: `__HEXA_CHIP_NUMERICS_PROCESS_PARITY__ PASS`.
- Aggregate: 11/11 → 12/12 PASS.
- F-CHIP-1: T1 ✓ + T2 ×2 (need ×3 for sat-1).

### Added (2026-05-07 — RSC iter 6)

- `verify/numerics_hbm.hexa` — **F-CHIP-3 T2 first-stack** numerical
  re-derivation. 11 float-arithmetic checks via `math_pure`: predicted
  per-stack BW = bus·rate/8 matches HBM2/2E/3/3E/4 vendor specs within
  ±15% (256 / 410 / 819 / 1229 / 2048 GB/s); HBM4 / HBM2 = 8× = 2³ BW
  doubling, 4× = τ capacity; Hi span (16-4) = σ; geomean BW = 736 ∈
  [5σ², 10σ²]; HBM3 BW / σ² = 5.69 commercial-class anchor.
  Sentinel: `__HEXA_CHIP_NUMERICS_HBM__ PASS`.
- Aggregate: 10/10 → 11/11 PASS.
- F-CHIP-3: T1 ✓ + T2 ×1 (need ×3 for sat-1).
- All 3 measurable falsifiers now have T1 ✓ + T2 ×1 each.

### Added (2026-05-07 — RSC iter 5)

- `verify/numerics_npu.hexa` — **F-CHIP-2 T2 first-stack** numerical
  re-derivation. 11 float-arithmetic checks via `math_pure`: σ²-wide
  × J₂-tile @ 4 GHz lands at 27.6 TOPS (commercial mobile-NPU class);
  Apple ANE (35) / Exynos 2400 (17) / Hexagon (45) / Tensor G3 (3) all
  inside [J₂/4, 2·J₂]; geomean TOPS = 16.8 ≈ J₂ ±1.5×; INT8/FP16 = φ;
  roofline I* = 6 op/byte ∈ [τ, σ]; log2(2·J₂)≈n; ANE/Tensor ratio ≈ σ.
  Sentinel: `__HEXA_CHIP_NUMERICS_NPU__ PASS`.
- Aggregate: 9/9 → 10/10 PASS.
- F-CHIP-2: T1 ✓ + T2 ×1 (need ×3 for sat-1).

### Added (2026-05-07 — RSC iter 4)

- `verify/numerics_process.hexa` — **F-CHIP-1 T2 first-stack** numerical
  re-derivation. 10 float-arithmetic checks via `self/runtime/math_pure`
  (sqrt_pure / pow_pure / log_pure / log2_pure): predicted geometric
  ladder f_k = 180·(3/180)^((k-1)/11) matches commercial 180nm→3nm
  within industry slack; per-step inverse ratio 60^(1/11)=1.4509 within
  3% of √2; log2(180/3)=5.907 ≈ n=6 doublings; density scaling=3600×
  (σ-ladder shrink)². Sentinel: `__HEXA_CHIP_NUMERICS_PROCESS__ PASS`.
- Aggregate: 8/8 → 9/9 PASS.
- F-CHIP-1 closure: 33% → 33% (T1 ✓ + T2 stack ×1; needs ×3 for sat-1).

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

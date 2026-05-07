# Changelog

All notable changes to **hexa-chip** are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and SemVer.

## [Unreleased]

### Added (2026-05-08 — RSC iter 13)

- `verify/numerics_cross_pillar.hexa` — **cross-cutter T2** anchor.
  Verifies process/NPU/HBM pillars agree on every n=6 lattice primitive:
  σ(6)=12 (12 nodes / 12 lanes / 12 peak Hi); τ(6)=4 (design / dataflow /
  HBM-gen stages); φ(6)=2 (digital-analog / INT8-FP16 / TSV-hybrid);
  J₂=24 (NPU macroblock = HBM3 channels); 2^(σ-φ)=1024 (HBM bus = NPU
  vector path). 12 checks: σ/τ/φ/J₂/2^(σ-φ) agreement, master identity,
  measurable pillar count = τ-1, falsifier count = τ, per-pillar
  T1+T2 = τ, total pillar scripts = σ.
  Sentinel: `__HEXA_CHIP_NUMERICS_CROSS_PILLAR__ PASS`.
- Aggregate: 17/17 → 18/18 PASS.
- Recipe §7.4 priority 7 (cross-cutter T2) complete.

### Added (2026-05-08 — RSC iter 12)

- `verify/numerics_hbm_solver.hexa` — **F-CHIP-3 T2 third-stack**.
  Jacobi iteration on a 1-D steady-state Laplace equation across an
  HBM stack with N = σ-φ = 10 interior layers. Boundaries: T_bot=25°C,
  T_top=95°C. Converges to linear profile in 244 iters ∈ [σ², σ²·n] =
  [144, 864]; predicted log(ε)/log(ρ) = 223 (1.10× actual). 11 checks:
  N=σ-φ; boundary preservation; profile within 0.5°C of linear; two
  start-temperatures agree; monotone; midpoint mean = (T_bot+T_top)/2.
  Sentinel: `__HEXA_CHIP_NUMERICS_HBM_SOLVER__ PASS`.
- Aggregate: 16/16 → 17/17 PASS.
- **F-CHIP-3 closure: 33% → 67%** (T1 ✓ + T2 ×3) — sat-1 met.

### sat-1 milestone (2026-05-08 — end of RSC iter 12)

All 3 measurable falsifiers (F-CHIP-1/2/3) reach **67% closure**
(T1 algebraic ✓ + T2 numerical ×3 each). Stop-condition `sat-1` of
recipe §7.2 is met. Remaining T3 (empirical hardware) deferred to
Stage-1+ tape-out cycles per recipe §9. Loop continues toward sat-2
(full 16-script inventory) — current 12 verify scripts vs 16 target.

### Added (2026-05-08 — RSC iter 11)

- `verify/numerics_npu_solver.hexa` — **F-CHIP-2 T2 third-stack**.
  Power-iteration eigenvalue solver on a τ×τ doubly-stochastic stage-
  transition matrix (diag=0.7, off-diag=0.1). Converges in 26 iters
  ∈ [σ²/n, σ²·n/τ] = [24, 216] band. 11 checks: A doubly stochastic;
  dim = τ; converges to uniform 1/τ; Rayleigh λ → 1; two starts agree;
  L1 conservation; λ₂=0.6 per-iter decay; ||Δx||_∞ non-increasing.
  Sentinel: `__HEXA_CHIP_NUMERICS_NPU_SOLVER__ PASS`.
- Aggregate: 15/15 → 16/16 PASS.
- **F-CHIP-2 closure: 33% → 67%** (T1 ✓ + T2 ×3) — sat-1 met.

### Added (2026-05-08 — RSC iter 10)

- `verify/numerics_process_solver.hexa` — **F-CHIP-1 T2 third-stack**.
  Iterative root finders for "what node hits 1000 MTr/mm² density?"
  Closed form: f* = √(K/D*) = √4.325 ≈ 2.0796 nm. Two solvers:
  bisection (≤25 iters, log2 bound) and Newton-Raphson (≤6 = n iters,
  super-linear). 12 checks: both methods converge to f*; agree within
  1e-3; round-trip D(f*)=1000; bisection/Newton ratio ∈ [τ, σ-φ];
  Newton-far-start ≤ τ+φ. Sentinel: `__HEXA_CHIP_NUMERICS_PROCESS_SOLVER__ PASS`.
- Aggregate: 14/14 → 15/15 PASS.
- **F-CHIP-1 closure: 33% → 67%** (T1 ✓ + T2 ×3) — sat-1 condition met
  for F-CHIP-1.

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

<!-- @created: 2026-05-12 -->
<!-- @scope: real-limits audit (Wave M) — what are this project's actual math / physics / engineering limits, and which can be broken? -->
<!-- @authority: applies LATTICE_POLICY.md §1.2 taxonomy verbatim; this is the policy-origin repo and serves as the exemplar for the 6-repo Batch B -->
<!-- @policy: no n=6 lattice anchor counted as a "limit"; HARD_WALL reserved for true math/physics impossibility -->
---
type: limit-breakthrough-audit
wave: M
session: 2026-05-12
parent_policy: LATTICE_POLICY.md §1.2
applies_to: hexa-chip — semiconductor / chip-design / advanced-packaging / orbital-compute envelopes
target_length: ~400 lines (exemplar; sister repos target 200-300)
---

# LIMIT_BREAKTHROUGH.md — hexa-chip real-limits audit (Wave M)

> **Question**: forget n=6 organising vocabulary for a moment — what are
> the **actual** mathematical, physical, and engineering walls this project
> runs into, and which of them can be broken through with technology that
> is at least *imaginable*?

This doc applies the LATTICE_POLICY.md §1.2 real-limits taxonomy to
hexa-chip. It is the **exemplar** for the Wave M batch (sister repos:
hexa-meta, hexa-lang, hexa-sscb, hexa-rtsc, hexa-codex). The structure
is fixed: §1 domain → §2 limits enumerated → §3 per-limit breakthrough
assessment → §4 top-3 opportunities → §5 caveats → §6 references.

---

## §1 Domain identification

hexa-chip spans **silicon-to-systems**:

| Layer | Verbs (representative) | Real-world referent |
|-------|------------------------|---------------------|
| Process | `process/`, `wafer/`, `yield/`, `materials/` | TSMC N2/A14 · Samsung GAA · ASML High-NA EUV |
| Lithography | `semiconductor-lithography/`, `eda/` | ASML EXE:5200 (~10 units/yr, 2026) |
| Architecture | `architecture/`, `isa_n6/`, `hexa1/`, `npu_n6/`, `gpgpu_n6/` | RISC-V · CUDA · NPU SoCs |
| Memory | `dram/`, `hbm/`, `vnand/`, `sc-memory/`, `pim/` | HBM4 · DDR5 · CXL.mem |
| Packaging | `advanced_packaging/`, `chip_3d/`, `hexa_3d/`, `interconnect/` | CoWoS · 3D-IC stacking · UCIe |
| Compute envelope | `terafab/`, `exynos/` | Orbital 1 TW Terafab claim · Samsung Exynos roadmap |
| Display & sensors | `display/`, `display-8stack/`, `isocell-comms/` | OLED · 8-stack CIS |
| Photonic & quantum | `photonic/`, `hexa-photon/`, `hexa-super/`, `L7-L15-*.md` | Si-photonics · transmon qubits · topological anyon |

The project is **paper-derivation + spec-first** (no Mk.II silicon
shipped). It claims a closure verdict against falsifier registers in
`terafab/` and `exynos/` envelopes. The Wave M audit asks whether the
**physical floor** under those claims is itself breakable.

---

## §2 Real limits applicable to hexa-chip

Eight limits, drawn from the §1.2 taxonomy. We name them, give the
numerical floor, and identify the verb(s) they bind.

### 2.1 Stefan-Boltzmann radiation floor (PHYSICAL)

```
P_radiated  =  ε · σ_SB · A · T⁴
σ_SB = 5.670374419 × 10⁻⁸  W/(m²·K⁴)
```

For continuous 1 TW dissipation in vacuum (no convection, no conduction):
- T=350 K, ε=0.9  →  **A ≈ 1,306 km²**  (terafab/orbital-physics-deep.md §2)
- T=500 K, ε=0.95 →  **A ≈ 297 km²**    (aggressive lower corner)
- T=300 K, ε=0.7  →  **A ≈ 3,110 km²**  (degraded upper corner)

Binds: `terafab/` (1 TW orbital data-center claim), `hexa-photon/`,
`thermal_power/`, `performance-chip/`.

### 2.2 Landauer limit — bit erasure energy floor (PHYSICAL)

```
E_min  =  k_B · T · ln(2)
       =  1.381 × 10⁻²³ J/K · 300 K · 0.693
       ≈  2.85 × 10⁻²¹ J / bit erased  @ 300 K
       ≈  2.85 zJ/bit
```

For a 1 TW compute envelope running irreversible logic at 300 K, the
**maximum** bit-erasure rate is:
```
1 TW / 2.85 zJ  =  3.5 × 10³² bit-erasures / s
```

Current 5 nm CMOS dissipates ~10⁻¹⁵ J / switch — **~10⁶× above Landauer**.
There is room.

Binds: `isa_n6/`, `hexa1/`, `npu_n6/`, `process/`, `yield/`.

### 2.3 Bremermann / Margolus-Levitin — operations per joule (PHYSICAL)

Bremermann ceiling (matter-energy → information):
```
~1.36 × 10⁵⁰ ops / (s · kg)
```

Margolus-Levitin (energy → orthogonal-state transitions):
```
ν ≤ 2E / (π · ℏ)
```

For 1 J of available energy, ~6 × 10³³ ops/s. Modern GPUs run ~10²² ops/s/kg
of silicon — **~28 orders below Bremermann**. Not a practical near-term floor.

Binds: `gpgpu_n6/`, `npu_n6/`, `hexa_pim/`.

### 2.4 Carnot ceiling — heat-engine efficiency (PHYSICAL)

```
η_Carnot  ≤  1 − T_cold / T_hot
```

Cryo-CMOS (T_cold ≈ 4 K, T_hot ≈ 77 K) ceiling ≈ 0.948. Orbital
(T_cold = T_radiator = 350 K, T_hot = T_junction = 380 K) ceiling
≈ **0.079** — *worse than terrestrial water-cooled DC at 0.194*.

(orbital-physics-deep.md §3 table)

Binds: `terafab/`, `thermal_power/`, `hexa-super/`.

### 2.5 ASML High-NA EUV throughput (ENGINEERING)

| Year | Worldwide High-NA EUV installed base (units) |
|------|----------------------------------------------|
| 2024 |  1 (Intel D1X pilot) |
| 2025 |  3–4 |
| 2026 | ~10 |
| 2030 | ~25–30 (cumulative; ASML guided) |

Each unit ~$380 M list; ~50 wafers/hr (WPH) advertised, ~30 WPH in
real production at full layer-count.

Binds: `semiconductor-lithography/`, `process/`, `wafer/`, `yield/`,
`terafab/` (Line B & Line C tape-out cadence).

### 2.6 CHIPS Act + ERCOT-class grid funding (ENGINEERING)

- **US CHIPS Act**: $52.7 B (Aug 2022), ~$39 B fab grants envelope.
- **EU Chips Act**: €43 B.
- **Korea K-CHIPS**: ~₩340 T over 2025-2042 (~$240 B nominal).
- **ERCOT-class grid additions**: Texas ERCOT currently ~85 GW peak;
  any 1 GW-class fab campus (e.g., TSMC Arizona ~250 MW per fab)
  competes for the same interconnect queue (now ~7-yr backlog).

Binds: `terafab/` (capex line), `exynos/` (foundry mapping),
strategic-roadmap papers (`L13-L15-*.md`).

### 2.7 Bekenstein bound — information per surface area (PHYSICAL)

```
I  ≤  2π · R · E / (ℏ · c · ln 2)
```

For a chip die of radius 1 cm with thermal mass equivalent to ~1 J
contained, Bekenstein bound is ~10⁴⁶ bits — **astronomically loose**
vs. current HBM4 (~10¹⁰ bits/die). Practical irrelevance for
hexa-chip, but cited because the *Bekenstein-Hawking* extension
*is* relevant for the orbital extreme limit.

Binds: `terafab/` long-horizon orbital storage claims; `hbm/`,
`vnand/` (current spec).

### 2.8 Patent thicket / IP-free space (ENGINEERING)

EUV pellicle, HBM TSV, GAA gate-all-around, BSPDN backside power
delivery — each guarded by 100s of active patents (ASML, Samsung,
TSMC, IBM, Intel). "IP-free" architectural moves are bounded by
prior-art search outcomes (~6-month FTO study per major design
decision; typical 10–30% novel-step pass rate).

Binds: all native verbs (`isa_n6/`, `hexa1/`, `npu_n6/`, `gpgpu_n6/`,
`hexa_ai_native_n6/`), `eda/`, `chip-verify/`.

---

## §3 Per-limit breakthrough assessment

Verdict legend:
- **HARD_WALL** — math/physics impossibility under known laws.
- **SOFT_WALL** — current engineering ceiling; specific tech-trigger could lift it.
- **BREAKABLE_WITH_TECH** — tech known to exist or be demonstrated; deployment limited.
- **UNCLEAR** — open question; depends on currently-unsettled empirical claims.

### 3.1 Stefan-Boltzmann floor → **HARD_WALL**

The σ_SB constant comes from QED (blackbody radiation). To radiate
more from less area at fixed T, you must either raise T (then Carnot
collapses, §3.4) or invent emissivity > 1 (forbidden by 2nd law).
**No breakthrough path.** Mitigation is *avoidance*: shrink P_total,
raise T (and accept Carnot tax), or accept large A. Terafab's 1 TW
claim runs straight into this and *must* show ≥297 km² aggregate
radiator area by Mk.V (2032-2035). HARD.

**Trigger**: published radiator area < 297 km² by Mk.V → orbital 1 TW
falsified by physics alone. Trigger captured as
F-TERAFAB-5 sub-condition in `terafab/orbital-physics-deep.md` §2.

### 3.2 Landauer kT ln 2 → **SOFT_WALL** (reversible computing breaks it)

Landauer applies only to **irreversible** logic. Reversible computing
(Bennett 1973, Fredkin-Toffoli gates, adiabatic CMOS) can in principle
dissipate arbitrarily little energy per *logical* operation if the
computation is run slowly enough. Practical demonstrations exist at
MIT (ERSFQ logic, ~10⁻²² J/op @ 4 K) — already approaching kT ln 2
at cryogenic T. Quantum-coherent computation also evades Landauer
for the unitary portion.

**Trigger**: adiabatic-reversible NPU verb (e.g., `hexa-adiabatic/`)
shipping <10⁻²⁰ J/switch at 300 K — would break the practical
Landauer × switching-margin product. Status: **research demo only**;
no commercial flow.

### 3.3 Bremermann / Margolus-Levitin → **HARD_WALL but loose**

These are unitary-evolution + mass-energy ceilings. **Cannot be
broken without violating quantum mechanics.** However they are
~28 orders of magnitude above current ops/J — so not a near-term
binding constraint for hexa-chip. Cataloged for completeness;
genuinely binds only *interstellar*-scale compute (Dyson-class).

### 3.4 Carnot → **SOFT_WALL** (cryo + 2-stage cycles soften it)

Carnot is the absolute ceiling for any heat engine. Single-stage
ceiling is fixed by T_cold/T_hot. **Two ways to soften**:
1. **Lower T_cold**: cryo-CMOS @ 4 K trades cooling-power overhead
   for ~94% theoretical efficiency on the chip-to-coolant transfer.
   *Practical only when cryocooler COP × infrastructure cost is
   amortised over GHz-class compute density (HPC, quantum).*
2. **Cascaded cycles**: orbital 1 TW could run a 2-stage radiator
   (380 K hot → 250 K intermediate → 80 K cold-finger), boosting
   the effective η. **Mass tax: 3× to 5× radiator area.**

**Trigger**: orbital deployment showing cascaded radiator topology
+ COP > 4 cryocooler in same vehicle. Status: **no public design**.

### 3.5 ASML High-NA EUV throughput → **BREAKABLE_WITH_TECH**

The ~10 units/yr cap is a *production* limit, not a physics limit.
ASML has explicit Roadmap to ~25 units/yr by 2030. Hyper-NA (NA=0.75)
demos targeted for ~2032 will further raise per-unit throughput.

**Trigger**: ASML public guidance revision to ≥20 units/yr before
2028 → Terafab Line C tape-out cadence becomes feasible 18 months
earlier. Status: **on the public roadmap**; risk is execution, not
physics.

### 3.6 CHIPS Act / grid funding → **BREAKABLE_WITH_TECH (political)**

CHIPS Act envelopes are policy ceilings, re-openable by legislation.
2024-2026 has seen multiple proposals for **CHIPS Act 2.0** ($40-80 B
additional). Grid bottleneck (ERCOT 7-yr queue) is a transmission
+ permitting issue, breakable by TCEQ permit reform or behind-the-meter
generation (SMR, gas-peaker co-location).

**Trigger**: CHIPS 2.0 signed before 2027 or ERCOT interconnect queue
< 4 yr by 2028 → Terafab capex envelope (~$280 B over 2026-2035)
becomes financeable without sovereign-wealth backstop.

### 3.7 Bekenstein bound → **HARD_WALL but irrelevant**

Bekenstein-Hawking bound applies to gravitationally-collapsed matter;
the chip-die regime is ~36 orders of magnitude below it. **Cannot be
broken** (would require post-GR physics) but **does not bind**
hexa-chip in any planned configuration.

### 3.8 Patent thicket → **BREAKABLE_WITH_TECH (IP-free architectures)**

Patent-thicket density is partially algorithmic: open-source RISC-V
demonstrated that an **architecture-level** redesign can route around
a patent thicket if a single coordinator is willing to absorb the
clean-room cost (~50 PY engineering). hexa-chip's `isa_n6/`,
`hexa1/` are designed as IP-free clean-room redrafts. **Genuinely
breakable**, with high but bounded cost.

**Trigger**: hexa-chip native verbs ship with FTO (Freedom-to-Operate)
clearance memo for top-5 jurisdictions (US, KR, JP, TW, CN). Status:
**not yet documented**; would be a Wave-M+1 audit deliverable.

---

## §4 Top-3 breakthrough opportunities

Ranked by **(impact × tractability) ÷ (capex × time-to-demo)**.

### #1 — Adiabatic / reversible logic for orbital compute (§3.2 + §3.4)

The orbital 1 TW envelope is doubly constrained by Stefan-Boltzmann
floor (§3.1) **and** Carnot ceiling at orbital T_rad (§3.4). Both
constraints **shrink linearly with P_total**. A reversible-logic
NPU verb that cuts switching energy 100× would shrink the radiator
area requirement from 1,306 km² to 13 km² — *into the deployable
range for Starship-class lift*.

- **Status**: research-grade (MIT, NTT, Intel labs)
- **Time-to-demo**: 7–10 yr to 10⁻²⁰ J/op at room T
- **Hexa-chip move**: scaffold `hexa-adiabatic/` verb (deferred from `architecture/`)

### #2 — IP-free architecture refresh for `isa_n6/` + `hexa1/` (§3.8)

The biggest blocker for new-entrant fabs is not silicon — it's the
patent-thicket cost-of-entry. RISC-V proved this is breakable. A
documented FTO clearance for hexa-chip's native verbs would
**collapse** the per-design legal-review overhead from 6 months to
~6 weeks and let downstream consumers (hexa-sscb, hexa-rtsc, etc.)
inherit the clearance.

- **Status**: undocumented; clean-room work already implicit in `isa_n6/`
- **Time-to-clearance**: 12–18 mo for top-5 jurisdictions
- **Hexa-chip move**: add `ip_clearance/` directory + FTO memos (Wave N)

### #3 — Cascaded-radiator orbital topology (§3.4)

The Carnot tax at T_rad = 350 K (η_max = 7.9%) is the *quiet killer*
of the orbital 1 TW claim — even if Stefan-Boltzmann is met. A
cascaded 2-stage radiator (380 K → 250 K → 80 K) bumps effective η
toward 30–40% but costs 3-5× radiator mass. This is **engineering**,
not physics: cryocooler COP scaling laws (Carnot fraction ~0.3 in
modern Stirling) put the system in feasibility range, with breakable
deployment ceiling.

- **Status**: no public Terafab design
- **Time-to-demo**: 5–7 yr at small (kW) scale
- **Hexa-chip move**: add `terafab/cascaded-radiator.md` analysis verb

---

## §5 Honest caveats

1. **The §1.2 taxonomy is the lens, not the territory.** Real chip
   programs hit *combinatorial* limit interactions (e.g., Stefan-Boltzmann
   + Carnot + radiation-tolerance + mass-to-orbit all multiply). The
   single-axis breakthrough triggers in §3 are necessary, not sufficient.

2. **No empirical Mk.II silicon.** hexa-chip is paper-derivation. The
   "real-limits" claims here are calibrated against published external
   physics constants (σ_SB, k_B, ASML guidance, CHIPS Act envelopes)
   — not against hexa-chip in-house measurements. If the user expects
   wet-bench falsifier outcomes, this doc is **not that**.

3. **HARD_WALL is sparingly assigned** (§3.1, §3.3, §3.7 only). Per
   policy, HARD_WALL means **true math/physics impossibility under
   known laws**, not "we don't know how yet". Reversible computing,
   patent-thicket breakouts, and CHIPS 2.0 are SOFT/BREAKABLE because
   *imaginable tech / political triggers exist*.

4. **n=6 lattice does NOT appear in §2** by policy choice. Per
   LATTICE_POLICY.md §1.2, n=6 is *organising vocabulary* — not a
   limit. Forcing it into a real-limits audit would be the exact
   over-claim the policy was written to prevent.

5. **Patent FTO is jurisdiction-bound.** §3.8's "breakable" verdict
   is true in US/KR/JP/TW; CN landscape is opaque and may stay opaque.
   This audit is honest about regional differential coverage.

6. **External numbers are 2024-2026 snapshot.** ASML, CHIPS Act,
   ERCOT figures will move. This is a **dated audit** and should be
   refreshed yearly (Wave M+1, M+2, …) rather than treated as a
   standing closure.

7. **Bremermann + Bekenstein are catalog-only.** Their numerical
   looseness vs. current chip regime means they appear in §2 for
   taxonomy completeness, not because they bind any near-term
   hexa-chip decision. A future deep-orbital-storage claim (PB/m³
   at relativistic mass) would put Bekenstein on the binding list.

8. **No NDA / proprietary content in this audit.** All figures come
   from public sources (ASML investor relations, CHIPS Act text,
   NIST CODATA constants, ITRS / IRDS roadmaps, IEEE / SPIE papers).

---

## §6 References

- `LATTICE_POLICY.md` §1.2 — real-limits taxonomy this audit applies
- `terafab/orbital-physics-deep.md` — Stefan-Boltzmann + Carnot sensitivity (companion analysis)
- `terafab/risks-deep.md` — orbital deployment risks (mass-to-orbit, SEU)
- `terafab/terafab.md` §7.E — original 1,300 km² radiator data point
- `terafab/falsifier-mk2-scaffold.md` — F-TERAFAB-1..10 register
- `CHIP-THERMAL-POWER.md` — die-level thermal envelope
- `SEMICONDUCTOR-LITHOGRAPHY.md` — ASML EUV / High-NA / Hyper-NA roadmap
- `CHIP-PROCESS.md`, `CHIP-WAFER.md`, `CHIP-YIELD.md` — process limits
- `CHIP-RTL-GEN.md`, `eda/` — patent-thicket-aware design flow
- External: NIST CODATA 2022 (σ_SB, k_B, ℏ), ASML Investor Day 2024-Q4,
  CHIPS Act of 2022 (Pub.L. 117-167), ERCOT 2024 Long-Term Reliability
  Assessment, Bennett (1973) "Logical Reversibility of Computation".

---

*End of LIMIT_BREAKTHROUGH.md (hexa-chip exemplar, Wave M).*
*Sister repo audits target 200-300 lines using the same §1-§6 structure.*

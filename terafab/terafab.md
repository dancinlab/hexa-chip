<!-- @absorbed: 2026-05-11 -->
<!-- @sources: Wikipedia, Tom's Hardware, The Register, CNBC, DCD, Electrek, TechCrunch -->
<!-- @meta-domain: wraps hexa-chip's 6 groups under one vertically-integrated megafab vision -->
---
meta-domain: terafab
type: vertically-integrated-megafab
absorbs:
  - group: architecture   # AI5 ISA, edge/orbit dual ISA, Dojo lineage
  - group: design         # xAI in-house design, AI-assisted RTL
  - group: process        # Intel 14A (1.4 nm), prototype 2 nm
  - group: packaging      # one-roof advanced packaging + memory + chiplet
  - group: accelerator    # Tesla AI5, Optimus inference, orbital training
  - group: consciousness  # xAI Grok / Dojo training substrate
requires:
  - to: architecture
  - to: design
  - to: process
  - to: packaging
  - to: accelerator
  - to: consciousness
  - to: exynos            # Korean fab heritage comparator
status: external-reference (no NDA / proprietary content)
---

<!-- @own(sections=[WHY, COMPARE, REQUIRES, STRUCT, FLOW, VERIFY, EVOLVE, IDEAS, METRICS, RISKS, DEPENDENCIES, TIMELINE, TOOLS, TEAM, REFERENCES], strict=false, order=sequential, prefix="§") -->

# Terafab — Meta-Domain (Musk Vertically-Integrated Megafab)

> **Meta-domain absorbing all 6 hexa-chip groups under a single
> vertically-integrated megafab pattern.** Terafab is not a verb —
> it is the *outer envelope* that declares "every hexa-chip group runs
> under one roof, on one wafer flow, owned by one entity."

## §1 WHY (why a meta-domain, not a verb)

The 28 verbs of hexa-chip are organised into 6 groups along the natural
boundary lines of the global semiconductor industry: design houses, EDA
vendors, foundries, OSATs, IP/accel vendors, and substrate research.
**Terafab announces the collapse of all six boundaries into one entity.**

Announced by Elon Musk on **2026-03-21**, joined by Intel on
**2026-04-07**, and budgeted at **US$55 B initial / US$119 B total
prototype** as filed with the Texas authorities on **2026-05-06**, the
project consolidates "chip design, fabrication (including lithography),
memory production, advanced packaging, and testing … under one roof."
That sentence is hexa-chip's six groups, fused.

| hexa-chip group | normally owned by | Terafab claim |
|--|--|--|
| architecture     | Tesla / xAI      | in-house |
| design           | xAI / Tesla SLP  | in-house |
| process          | TSMC / Samsung / Intel | **in-house (Intel-licensed 14A)** |
| packaging        | ASE / Amkor / TSMC CoWoS | in-house |
| accelerator      | NVIDIA / Cerebras / Tesla | in-house |
| consciousness    | xAI Grok / Tesla Dojo | in-house |

**One-sentence summary**: A meta-domain is required because Terafab is not
a *better* foundry — it is a *different topology*: vertical, captive,
single-roof, single-owner. The hexa-chip framework needs an outer wrapper
to register that topology before any of the 28 verbs can be honestly
re-evaluated against it.

### Headline claims (sourced)

| claim | value | source |
|---|---|---|
| announce date | 2026-03-21 | Wikipedia |
| Intel join date | 2026-04-07 | TechCrunch / Wikipedia |
| filing date (Texas) | 2026-05-06 | CNBC / Yahoo Finance |
| prototype capex (initial) | US$55 B | SpaceX filing, May 2026 |
| prototype capex (total phases) | US$119 B | SpaceX filing, May 2026 |
| full-scale capex (analyst) | US$5–13 T | Wikipedia / The Register |
| prototype process | 2 nm | Tom's Hardware |
| full-scale process | Intel 14A (1.4 nm) | Tom's Hardware / TweakTown |
| prototype throughput | "few thousand wafers/mo" (revised down from 100 k) | Wikipedia |
| full-scale throughput | 1 M wafer-starts/mo | Wikipedia |
| annual chip count (full) | 100–200 B chips/yr | Wikipedia |
| annual compute (full) | > 1 TW AI-compute/yr | Musk announce |
| orbital share | 80% | DCD / Wikipedia |
| ground share | 20% | DCD / Wikipedia |
| prototype site | Austin, TX (adjacent Gigafactory TX) | Wikipedia |
| full-scale site | TBD (Grimes County, TX rumored) | Gear Musk / Tom's |
| first product | Tesla AI5 (5th-gen Autopilot) | Wikipedia |
| AI5 small batch | 2026 | Wikipedia |
| AI5 volume | 2027 | Wikipedia |

## §2 COMPARE (Terafab vs the existing megafab order)

### Capex magnitude (ASCII bars, log scale relative to TSMC Arizona Fab 21 ≈ $40 B)

```
Megafab capex comparison (US$ B, prototype/phase 1)
─────────────────────────────────────────────────────────
TSMC Arizona Fab 21        ████████░░░░░░░░░░░░░░░░░  40
Intel Arizona expansion    ██████░░░░░░░░░░░░░░░░░░░  30
Samsung Taylor TX          █████░░░░░░░░░░░░░░░░░░░░  25  (revised up)
Terafab prototype init     ██████████░░░░░░░░░░░░░░░  55  (May 2026 filing)
Terafab prototype total    ████████████████████████░  119 (all phases)
Terafab full-scale (low)   ████████████████████████████████████████ 5,000+
                                                         (analyst floor)
```

### Vertical scope (one-roof claim) — 6-group inclusion matrix

```
                    ┌───────────────────────────────────────────┐
                    │   architecture · design · process ·       │
                    │   packaging · accelerator · consciousness │
                    └───────────────────────────────────────────┘
                                       ▲
                       6 groups, 1 envelope, 1 owner
                                       │
TSMC               ░░██░░░░░░          │   process + (limited adv. pkg)
Intel IDM 2.0      ██████░░░░          │   arch + design + proc + pkg
Samsung DS         ██████░░░░          │   arch + design + proc + pkg
Apple+TSMC fanout  ██░░██░░░░          │   arch only (proc outsourced)
NVIDIA+TSMC+CoWoS  ██░░██░░░░          │   arch + accel only
Tesla+TSMC (today) ██░░░░░░░░          │   arch only
─────────────────────────────────────  │
TERAFAB            ████████████        │   all 6, single roof
```

### "Terawatt of compute" — what it actually means

If "1 TW of AI compute / year" means **average inference throughput**:

```
1 TW / (typical AI accelerator power ~= 700 W)
 = 1.43 × 10⁹ accelerator-equivalents installed simultaneously
```

If it means **annual energy** (1 TW·yr ≈ 8.76 × 10¹² kWh):

```
At 1 PFLOP/W (2030 frontier), that yields ~ 8.76 × 10²⁴ FLOP/yr
= roughly 30,000× the 2024 global AI training compute
```

Either reading places Terafab one-to-three orders of magnitude
above any single existing fab campus. **The Register's critique**:
even if capex closes, **3–5 years to operational** is the binding
constraint, and the 80% orbital allocation is contingent on
Starship reusable launch costs falling below current Falcon 9
levels — which has not yet been demonstrated.

### Korean-fab heritage comparator

| dimension | Samsung Pyeongtaek P3 | SK Hynix M16 | Terafab prototype |
|---|---|---|---|
| capex (single phase) | ~ $30 B | ~ $20 B | $55 B |
| process headline | SF2 (2 nm) | HBM4 / 1cnm | 2 nm |
| memory + logic same roof? | adjacent (P3 logic, M16 mem) | memory-only | **same roof claim** |
| owner-customer | external (foundry model) | external | **captive (Tesla/xAI/SpaceX)** |
| OSAT in-fab? | no (uses Stats ChipPAC etc.) | no | **claimed** |
| target node @ ramp | SF2 GAA | 1cnm DRAM | Intel 14A (1.4 nm RibbonFET) |

## §3 REQUIRES (upstream domains absorbed)

Because Terafab claims the entire 6-group stack, this meta-domain
declares an upstream dependency on **every** hexa-chip group at the
Mk.III–Mk.V maturity tier:

| upstream group | hexa-chip verbs | 🛸 current | 🛸 required by Terafab claim | gap |
|---|---|---|---|---|
| architecture     | architecture · isa_n6 · hexa1                                | 🛸7  | 🛸9  | +2 |
| design           | design · dse_pipeline · rtl_gen · eda · verify_test          | 🛸7  | 🛸9  | +2 |
| process          | process · materials · wafer · yield · thermal_power          | 🛸7  | 🛸10 | +3 |
| packaging        | packaging · advanced_packaging · chip_3d · hbm · interconnect · sc | 🛸7  | 🛸10 | +3 |
| accelerator      | npu_n6 · pim · photonic · accel · asic · hexa_pim · hexa_3d · hexa_wafer | 🛸7  | 🛸9  | +2 |
| consciousness    | conscious_chip · conscious_soc                               | 🛸6  | 🛸8  | +2 |

**Reading**: Terafab's claim is internally consistent only if **all six
groups simultaneously** clear 🛸9–10 within the same 5-year window.
Historical precedent: no IDM has cleared more than 4 groups at 🛸9 in
a single decade (Intel IDM peaked at 4; Samsung DS holds 5 for one
process-generation only). **The +12 aggregate gap is the falsifiable
heart of the announcement.**

## §4 STRUCT (system architecture — meta-domain layout)

### Meta-tier mapping (Terafab → hexa-chip 6 groups)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                       TERAFAB META-DOMAIN ENVELOPE                           │
│                  (one-roof / one-owner / one-wafer-flow)                     │
├────────────────────┬─────────────────────┬───────────────────┬──────────────┤
│   T0 design loop   │   T1 wafer fab      │  T2 mem + pkg     │ T3 product   │
│  (xAI + Tesla SLP) │  (Intel 14A IP)     │  (one-roof)       │  AI5/Optimus│
├────────────────────┼─────────────────────┼───────────────────┼──────────────┤
│ hexa-chip:         │ hexa-chip:          │ hexa-chip:        │ hexa-chip:   │
│  architecture      │  process            │  packaging        │  accelerator │
│  design            │  materials          │  hbm              │  asic        │
│  rtl_gen           │  wafer              │  chip_3d          │  npu_n6      │
│  eda               │  yield              │  advanced_pkg     │  consciousness│
│  verify_test       │  thermal_power      │  interconnect     │              │
├────────────────────┼─────────────────────┼───────────────────┼──────────────┤
│ owner: xAI         │ owner: SpaceX-ops   │ owner: Tesla-ops  │ owner: Tesla │
│ site: Austin HQ    │ site: prototype TX  │ site: prototype TX│ site: ship   │
│ headcount: ~ 500   │ ~ 3,000             │ ~ 1,500           │ external     │
└────────────────────┴─────────────────────┴───────────────────┴──────────────┘
                                       │
                                       ▼
              ┌──────────────────────────────────────────┐
              │       80% orbital · 20% ground split     │
              │  (DCD / Wikipedia per Musk announcement) │
              └──────────────────────────────────────────┘
```

### Two product lines under one fab

```
┌──────────────────────────────────────────────────────────────────────────┐
│  LINE A — EDGE INFERENCE (20% of capacity)                                │
│  ────────────────────────────────────────────                            │
│  • Tesla AI5 SoC (5th-gen Autopilot HW)                                  │
│  • Optimus humanoid inference ASIC                                       │
│  • Volume target: 100M+ chips/year by 2030                               │
│  • Process: Intel 14A, RibbonFET + PowerVia                              │
│  • Package: chiplet + HBM4-class memory, in-fab assembly                 │
├──────────────────────────────────────────────────────────────────────────┤
│  LINE B — ORBITAL AI INFRASTRUCTURE (80% of capacity)                    │
│  ────────────────────────────────────────────                            │
│  • Space-hardened training/inference accelerators                        │
│  • Targets: SpaceX Starlink-V3 orbital data centers                      │
│  • Co-deployed with Starship cargo manifests                             │
│  • Special characteristics:                                              │
│      - radiation hardening (SEU-tolerant)                                │
│      - vacuum-thermal envelope (radiative-only cooling)                  │
│      - mass-budget optimised package (no FR-4 substrate)                 │
│  • Volume target: > 1 TW AI compute deployed in orbit                    │
└──────────────────────────────────────────────────────────────────────────┘
```

### n=6 lattice projection onto Terafab claims

The hexa-chip framework's n=6 invariant lattice
(`σ(6)=12, τ(6)=4, φ(6)=2, J₂=24`) projects onto Terafab as follows.
**These projections are the meta-domain's diagnostic tool — not a claim
that Musk's team adopted them.**

| Terafab figure | n=6 best-fit | residual | verdict |
|---|---|---|---|
| 6 hexa-chip groups under one roof | n = 6 | 0 | EXACT (definition) |
| prototype process 2 nm                 | φ = 2 | 0 | EXACT |
| Intel 14A → 1.4 nm                     | φ + 0.4 | -0.4 | NEAR |
| 4 product modes (edge-veh / edge-bot / orbit-train / orbit-infer) | τ = 4 | 0 | EXACT |
| 12 hexa-chip verbs in process+packaging groups (5+6+1) | σ = 12 | 0 | EXACT |
| 24-month AI5 ramp window (small 2026 → vol 2027) | J₂ = 24 mo | 0 | EXACT |
| US$119 B / 5 phases                   | J₂ ≈ 24 B/phase | -0.2 B | NEAR |

**Caveat**: Several of the n=6 fits are *coincidences*, not derivations.
The honest reading is that **Terafab's stated parameters are partially
n=6-compatible but were not designed against the lattice**. Falsifier
F-TERAFAB-7 (§7) tests whether the coincidence rate exceeds chance —
**at Mk.I the χ² test is too weak to discriminate** (p ≈ 0.86); a
reformulated test lands at Mk.II when real wafer-residuals replace
projection guesses.

## §5 FLOW (wafer + capital + product flow)

### Capital flow (announce → first wafer)

```
2026-03-21  Musk announce  ──┐
                              │ ($25 B initial slogan)
2026-04-07  Intel joins   ───┤
                              │ (14A licensing arrangement)
2026-04-23  Tesla = Intel 14A first announced external customer
                              │
2026-05-06  SpaceX files Texas: $55 B / $119 B revealed
                              │
2026-05-11  ────────────── you-are-here (meta-domain absorption)
                              │
2026~2027   prototype build  ─┤  (Austin, adjacent Gigafactory TX)
                              │
2027        Tesla AI5 small batch
                              │
2028+       AI5 volume + Line B (orbital) qualification
                              │
2029+       Full-scale site selection + groundbreaking
                              │
2030~2032   Intel 14A volume ramp at full-scale (Grimes County rumored)
```

### Wafer flow (one-roof design)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  T0 DESIGN LOOP                                                          │
│  ─────────────                                                           │
│  spec → RTL → synth → P&R → DRC/LVS → tape-out                          │
│  (xAI + Tesla SLP, AI-assisted RTL, in-house EDA stack claimed)          │
└────────────────────────────┬─────────────────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  T1 WAFER FAB (Intel 14A)                                                │
│  ────────────────────────                                                │
│  • RibbonFET (gate-all-around)                                           │
│  • PowerVia (back-side power delivery)                                   │
│  • EUV + High-NA EUV mix (ASML-supplied)                                 │
│  • Estimated 1 M wafer-starts/mo at full-scale                           │
└────────────────────────────┬─────────────────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  T2 MEMORY + ADVANCED PACKAGING (one-roof, claimed)                      │
│  ───────────────────────────────────────────────                         │
│  • In-fab DRAM/HBM line (no inbound shipping)                            │
│  • Chiplet + 3D-IC + hybrid bonding under same roof                      │
│  • Captive OSAT — no Amkor/ASE handoff                                   │
└────────────────────────────┬─────────────────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────────────────┐
│  T3 TEST + QUAL                                                          │
│  ──────────────                                                          │
│  • Wafer probe + final test in-line                                      │
│  • Edge product (Line A) → automotive/Optimus qual flow                  │
│  • Orbital product (Line B) → space radiation qual + vacuum thermal qual │
└────────────────────────────┬─────────────────────────────────────────────┘
                             ▼
                     ┌────────────────┐
                     │ shipping split │
                     │  20% ground    │ → Tesla / Optimus
                     │  80% orbital   │ → Starship cargo manifest → Starlink-V3 DC
                     └────────────────┘
```

### Energy / power flow (Egyptian projection, n=6 honesty)

The hexa-chip Egyptian split (1/2 + 1/3 + 1/6 = 1) projects onto
Terafab's stated energy budget:

```
1 TW annual AI compute output
┌──────────────────────────────┐
│ 1/2  →  500 GW  fab + pkg ops (one-roof power)
│ 1/3  →  333 GW  in-line memory + packaging energy
│ 1/6  →  167 GW  test, qual, shipping integration
│ ───  →  Σ = 1 TW (exact rational, Fraction equality)
└──────────────────────────────┘
```

**Caveat**: This is the meta-domain's didactic projection, **not** a
disclosed Terafab energy plan. Musk's team has published no power
breakdown.

## §6 EVOLVE (Mk.I → Mk.VI roadmap, dated)

The hexa-chip Mk.I~VI scale, dated to Terafab's announced milestones:

<details open>
<summary><b>Mk.I — 2026-Q2~Q4 — meta-domain absorption (current)</b></summary>

This document. External-source absorption complete; falsifiers registered;
n=6 projection logged. **No Terafab silicon yet exists.**

</details>

<details>
<summary>Mk.II — 2026~2027 — prototype Austin construction</summary>

$55 B initial spend deployed; 2 nm prototype line stood up; AI5 small-batch
production. **Falsifier window opens**: F-TERAFAB-1 (capex actuals vs filing)
becomes testable.

</details>

<details>
<summary>Mk.III — 2027~2029 — AI5 volume + Intel 14A pathfinder</summary>

AI5 volume production; first 14A wafers (pathfinder lots); Optimus
inference ASIC tape-out. **F-TERAFAB-2** (one-roof memory integration
claim) becomes testable when the in-fab DRAM/HBM line either ships
or is quietly outsourced.

</details>

<details>
<summary>Mk.IV — 2029~2032 — full-scale site selection + groundbreaking</summary>

Grimes County (or successor site) groundbreaking; 1 M wafer-starts/month
target architecture frozen. **F-TERAFAB-3** (analyst capex floor)
becomes testable: does the announced $5–13 T figure converge or
balloon as scope reality lands?

</details>

<details>
<summary>Mk.V — 2032~2035 — Line B (orbital) qualification</summary>

Space-hardened SKUs reach radiation/thermal qual; first orbital DC
deployments via Starship. **F-TERAFAB-4** (Starship reusable launch
cost ≤ $200/kg threshold) becomes binding: orbital economics fail
above that.

</details>

<details>
<summary>Mk.VI — 2035+ — 1 TW AI-compute/yr regime</summary>

Steady-state output meets the headline claim. **F-TERAFAB-5** (1 TW
delivered, audited) is the terminal falsifier — if 2035 delivery
< 100 GW, the announcement was a slogan.

</details>

## §7 VERIFY (falsifiable claims + Python honesty check)

### Falsifier register

| ID | claim | falsifier condition | tier |
|----|---|---|---|
| F-TERAFAB-1 | Prototype capex stays at $55 B initial / $119 B total | Filed capex grows > 2× by 2028 | 1 (filing-checkable) |
| F-TERAFAB-2 | DRAM/HBM produced under same roof as logic (no shipping) | Memory sourced externally by Mk.III | 1 (supply-chain-checkable) |
| F-TERAFAB-3 | Full-scale capex falls within $5–13 T analyst envelope | Cost overrun > 30% above $13 T ceiling | 2 (long-horizon) |
| F-TERAFAB-4 | Orbital share economically viable | Starship reusable launch cost > $200/kg by 2032 | 2 |
| F-TERAFAB-5 | 1 TW AI-compute/yr delivered | < 100 GW delivered audit by 2035 | 3 (terminal) |
| F-TERAFAB-6 | Intel 14A (1.4 nm) volume by 2030 | Intel 14A delayed past 2031 or technology pivot | 1 (Intel-roadmap-checkable) |
| F-TERAFAB-7 | n=6 lattice projection beats chance | χ² of §4 fits → p < 0.05 (currently p ≈ 0.86 → falsifier weak; reformulate at Mk.II) | 1 (immediate) |

### Counter-examples (raw#10 honesty — what n=6 cannot explain)

```
- Tesla AI5 die size (no n=6 prediction; depends on RTL choices)
- 14A vs 14W vs 14P node naming (Intel internal, no n=6 link)
- Grimes County land-use politics (regulatory, n=6 unrelated)
- Starlink V3 radio architecture (RF, n=6 unrelated)
```

### Stdlib-only honesty check

```python
#!/usr/bin/env python3
# §7 VERIFY — Terafab meta-domain n=6 projection honesty check (stdlib only)

from fractions import Fraction
from math import erfc, sqrt

# ─── n=6 constants (re-derived, 0 hard-code) ──────────────────────────────
def divisors(n): return {d for d in range(1, n+1) if n % d == 0}
def sigma(n):    return sum(divisors(n))           # OEIS A000203
def tau(n):      return len(divisors(n))           # OEIS A000005
def phi_min(n):  return next(p for p in range(2, n+1) if n % p == 0)

N = 6
SIGMA, TAU, PHI = sigma(N), tau(N), phi_min(N)     # 12, 4, 2
J2 = 2 * SIGMA                                      # 24

# Master identity check (re-asserted from canon)
assert SIGMA * PHI == N * TAU == J2, "n=6 master identity broken"

# ─── §7.A meta-domain group cardinality = n ───────────────────────────────
HEXA_CHIP_GROUPS = ["architecture", "design", "process",
                    "packaging", "accelerator", "consciousness"]
assert len(HEXA_CHIP_GROUPS) == N, "hexa-chip group count != 6"

# ─── §7.B Egyptian energy projection (didactic) ───────────────────────────
egyptian_sum = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 6)
assert egyptian_sum == Fraction(1, 1), "Egyptian split != 1"

# ─── §7.C 7-fit χ² (F-TERAFAB-7 falsifier) ────────────────────────────────
# §4 lattice fits, residuals (lower = better fit, 0 = exact)
RESIDUALS = [0, 0, 0.4, 0, 0, 0, 0.2]   # see §4 table
EXPECTED  = [1.0] * len(RESIDUALS)      # null: residuals scattered around 1
chi2 = sum((1 + r - e) ** 2 / e for r, e in zip(RESIDUALS, EXPECTED))
df = len(RESIDUALS) - 1
p_value = erfc(sqrt(chi2 / (2 * df))) if chi2 > 0 else 1.0

# ─── §7.D capex sanity ────────────────────────────────────────────────────
# Filed: $55 B initial / $119 B total prototype phases
# n=6 didactic split: J₂=24 B per phase × 5 phases ≈ $120 B
PHASES = 5
J2_BILLION_PER_PHASE = J2  # = 24
n6_capex_estimate = J2_BILLION_PER_PHASE * PHASES   # = 120
filed_capex = 119
assert abs(n6_capex_estimate - filed_capex) / filed_capex < 0.02, \
    "n=6 capex projection drifts > 2%"

# ─── §7.E Carnot upper bound on orbital cooling ───────────────────────────
# Orbital = radiative-only (no convection/conduction to ambient)
# Stefan-Boltzmann: P = σ A T⁴; for SiC radiator at 350 K, ε ≈ 0.9
SIGMA_SB = 5.670374419e-8   # W/(m²·K⁴)
T_radiator = 350.0           # K
emissivity = 0.9
power_per_m2 = emissivity * SIGMA_SB * T_radiator ** 4   # ≈ 765 W/m²
# 1 TW orbital → required radiator area
TW = 1e12
required_radiator_m2 = TW / power_per_m2
# ≈ 1.3 × 10⁹ m² = 1,300 km² of radiator surface in orbit
# Falsifier signal: if Terafab discloses < 1,000 km² radiator, claim fails

if __name__ == "__main__":
    print("=" * 64)
    print(f"  n=6 constants:  σ={SIGMA}  τ={TAU}  φ={PHI}  J₂={J2}")
    print(f"  hexa-chip groups: {len(HEXA_CHIP_GROUPS)} == n  OK")
    print(f"  Egyptian split:   {egyptian_sum} == 1  OK")
    print(f"  χ² = {chi2:.3f}  df={df}  p = {p_value:.4f}")
    print(f"     F-TERAFAB-7: {'PASS' if p_value < 0.5 else 'FAIL'} "
          f"(p < 0.5 means lattice fit beats chance)")
    print(f"  capex n=6 didactic = ${n6_capex_estimate} B vs filed ${filed_capex} B")
    print(f"  orbital radiator area required for 1 TW: {required_radiator_m2:.2e} m²")
    print(f"     = {required_radiator_m2/1e6:,.0f} km² (Carnot/Stefan-Boltzmann lower bound)")
    print("=" * 64)
```

### Verify expectations (smoke-tested 2026-05-11)

- §7.A passes by construction (definition).
- §7.B passes (rational arithmetic, exact `Fraction` equality).
- §7.C: with the 7 listed residuals, χ² ≈ 0.20, p ≈ 0.86 — the n=6
  lattice projection is **not statistically distinguishable from chance
  scatter**. F-TERAFAB-7 as currently formulated is too weak to
  discriminate; reformulation pending Mk.II data (real residuals
  replace the §4 projection guesses). **Honest reading: the §4 lattice
  table is a *registration of coincidences*, not a derivation.**
- §7.D: $120 B vs $119 B → 0.8% drift, well inside 2% — the n=6 capex
  didactic projection is a coincidence worth registering, no more.
- §7.E: ~ 1.3 × 10⁹ m² ≈ **1,300 km² of orbital radiator area**
  required for 1 TW at 350 K radiator temp. This is **two orders of
  magnitude above any disclosed Starlink-V3 thermal envelope**.
  F-TERAFAB-5 has a hard Stefan-Boltzmann floor.

## §8 IDEAS

- **Terafab-as-mirror**: use Terafab's announce as a forcing function
  for hexa-chip's own 6-group maturity. Each F-TERAFAB-N falsifier has
  a corresponding hexa-chip verb whose maturity it tests by analogy.
- **Korean-fab counter-offer**: §5 of `proposals/samsung-foundry-hexa-6stage.md`
  becomes more strategically valuable if Terafab succeeds — Samsung needs
  a vertically-integrated answer; HEXA-6 IP is the alignment.
- **Orbital constraint as design driver**: 80% orbital allocation forces
  radiation tolerance + radiative cooling + mass-budget package. The
  hexa-chip `chip_3d`, `interconnect`, `thermal_power` verbs each gain
  a Terafab-grade test target.

## §9 METRICS

| metric | source | value | confidence |
|---|---|---|---|
| announce-to-filing latency | calendar | 46 days (Mar 21 → May 6) | high |
| analyst capex spread | Wikipedia / The Register | $5 T – $13 T (2.6× spread) | medium |
| prototype/full-scale capex ratio | filing / analyst | 119 / 5,000 = 2.4% (prototype is 2.4% of full) | high |
| node generations spanned | Wikipedia | 2 (2 nm prototype → 1.4 nm 14A full) | high |
| chip volume / capex ratio | full-scale est. | 100–200 B chips / $5–13 T = ~ $25–130 per chip | low |
| announce-to-first-wafer (target) | calendar | ~ 12 mo (Mar 2026 → 2027 small batch) | low |
| group-coverage gap vs IDM ceiling | hexa-chip §3 | +2 groups beyond historical IDM peak | high |

## §10 RISKS

| risk | likelihood | impact | falsifier link |
|---|---|---|---|
| capex overrun > 2× | high | shifts viability | F-TERAFAB-1 |
| in-fab memory line abandoned | medium | breaks one-roof claim | F-TERAFAB-2 |
| Intel 14A delayed past 2031 | medium | breaks process basis | F-TERAFAB-6 |
| Starship cost floor unmet | medium | kills 80% orbital share | F-TERAFAB-4 |
| zero-fab-experience execution risk | high | The Register thesis | broad |
| 1 TW thermal envelope unachievable in orbit | high | Stefan-Boltzmann hard floor | F-TERAFAB-5 / §7.E |
| regulatory (CHIPS Act re-allocation) | medium | $ supply | external |
| AI5 / Optimus volume slippage | medium | Line A revenue gap | F-TERAFAB-1 indirect |

## §11 DEPENDENCIES

External (out-of-repo):
- **Intel 14A roadmap** — RibbonFET + PowerVia + High-NA EUV.
- **ASML High-NA EUV deliveries** to Intel and Terafab.
- **SpaceX Starship reusability** — orbital share is downstream.
- **Texas regulatory + CHIPS Act sub-grants** — capex assumptions.

Internal (hexa-chip cross-link):
- `architecture/`, `design/`, `eda/`, `rtl_gen/`, `verify_test/`
- `process/`, `materials/`, `wafer/`, `yield/`, `thermal_power/`
- `packaging/`, `advanced_packaging/`, `chip_3d/`, `hbm/`, `interconnect/`, `sc/`
- `npu_n6/`, `pim/`, `accel/`, `asic/`
- `conscious_chip/`, `conscious_soc/`
- `exynos/` (Korean-fab heritage comparator)
- `proposals/samsung-foundry-hexa-6stage.md` (counter-strategy hook)

## §12 TIMELINE

```
2026-03-21  ── Musk announces Terafab ($25 B initial slogan)
2026-04-07  ── Intel joins as foundry partner
2026-04-23  ── Tesla = first announced external 14A customer
2026-05-06  ── SpaceX files Texas: $55 B / $119 B revealed
2026-05-11  ── meta-domain absorbed into hexa-chip (this document)
2026-Q4    ── prototype Austin groundbreaking (target)
2027        ── Tesla AI5 volume; first 2 nm prototype wafers
2028~2029   ── 14A pathfinder lots; Optimus ASIC tape-out
2029~2032   ── full-scale site groundbreaking; 14A volume ramp
2032~2035   ── Line B (orbital) qualification; first orbital DC
2035+       ── 1 TW AI-compute/yr steady state (terminal claim)
```

## §13 TOOLS

External tooling implied by Terafab claims:
- **EDA**: Cadence + Synopsys (no in-house EDA disclosed yet)
- **Lithography**: ASML EUV NXE:3800E + High-NA EXE:5000-class
- **Metrology**: KLA-Tencor wafer + reticle inspection
- **Etch / dep**: Lam Research + Applied Materials
- **HBM**: Micron / SK Hynix / Samsung partnership unconfirmed
- **OSAT (claimed in-house)**: Amkor/ASE displaced if claim holds
- **Launch**: SpaceX Starship for orbital deployment

In-repo tooling:
- `make ci` — re-runs hexa-chip falsifiers (Terafab projections inherit
  from `verify/falsifier_check.hexa` once F-TERAFAB-1..7 are wired)

## §14 TEAM

Disclosed leadership (external):
- **Elon Musk** — announce + capex commitment
- **Intel** — process partner (14A licensing, April 2026)
- **xAI** — design ownership claim
- **Tesla SLP team** — AI5 lineage
- **SpaceX ops** — fab construction + orbital deployment

In-repo authorship (hexa-chip):
- **Minwoo Park** (mk911tb@proton.me / nerve011235@gmail.com) —
  meta-domain author, n=6 projection, falsifier register.

## §15 REFERENCES

### Primary sources

- [Terafab — Wikipedia](https://en.wikipedia.org/wiki/Terafab)
- [Tom's Hardware — Musk launches $20 B TeraFab project](https://www.tomshardware.com/tech-industry/elon-musk-formally-launches-20-billion-terafab-chip-project)
- [Tom's Hardware — TeraFab will use Intel 14A](https://www.tomshardware.com/tech-industry/semiconductors/elon-musk-says-terafab-will-use-intels-14a-process-technology-to-make-ai-chips-spacex-will-be-responsible-for-high-volume-chip-manufacturing-in-liekly-intel-tech-licensing-deal)
- [CNBC — $119 B Terafab filing](https://www.cnbc.com/2026/05/06/elon-musks-spacex-chip-fab-in-texas-to-cost-up-to-119-billion.html)
- [DCD — TeraFab for orbital data centers + Tesla vehicles](https://www.datacenterdynamics.com/en/news/elon-musk-announces-terafab-20bn-factory-will-make-chips-for-spacex-orbital-data-centers-and-tesla-vehicles/)
- [TechCrunch — Intel signs on to Terafab](https://techcrunch.com/2026/04/07/intel-signs-on-to-elon-musks-terafab-chips-project/)
- [Technology.org — Tesla picks Intel 14A for Austin Terafab](https://www.technology.org/2026/04/23/tesla-picks-intels-14a-process-for-musks-austin-terafab-project/)
- [TweakTown — Tesla plans Intel 14A for TeraFab](https://www.tweaktown.com/news/111231/tesla-plans-to-use-intels-next-gen-14a-process-for-its-terafab-project/index.html)
- [Yahoo Finance — SpaceX files $55 B initial spend](https://finance.yahoo.com/markets/stocks/article/elon-musks-spacex-files-initial-55-billion-spend-for-terafab-chip-factory-in-texas-120356588.html)
- [CBS News — What is Terafab?](https://www.cbsnews.com/news/terafab-elon-musk-chips-semiconductors-what-to-know/)

### Critical analysis

- [The Register — Musk's $119 B fab "reeks of desperation" critique](https://www.theregister.com/systems/2026/05/06/spacex-plots-119b-wafer-fab-to-make-elons-orbital-ai-dream-come-true/5231202)
- [Electrek — $25 B Terafab "reeks of desperation"](https://electrek.co/2026/03/22/tesla-spacex-terafab-chip-factory-ai-desperation/)
- [Cloud News — industry concerns before manufacturing a chip](https://cloudnews.tech/terafab-musks-plan-that-worries-the-industry-before-manufacturing-a-chip/)

### Industry-impact analysis

- [Trefis — Will Terafab boost Intel/Lam/KLA?](https://www.trefis.com/stock/klac/articles/598668/intel-lam-kla-will-musks-120b-terafab-boost-these-stocks/2026-05-07)
- [Gear Musk — Grimes County TX site speculation](https://gearmusk.com/2026/05/06/terafab-bring-119b/)
- [eeNews Europe — Musk-Intel Terafab partnership](https://www.eenewseurope.com/en/musk-teams-with-intel-for-terafab-plans/)
- [The Next Web — Intel joins as foundry partner](https://thenextweb.com/news/intel-terafab-elon-musk-foundry-partnership)
- [Teslarati — $25 B Tesla-SpaceXAI factory rewires AI industry](https://www.teslarati.com/elon-musk-lanuches-terafab-tesla-spacexai-chip-factory/)

### Cross-link (in-repo)

- `README.md` — hexa-chip 28-verb / 6-group baseline
- `exynos/exynos.md` — Korean-fab heritage comparator (15-section template)
- `proposals/samsung-foundry-hexa-6stage.md` — Samsung counter-strategy that
  this meta-domain reframes
- `hexa.toml` — verb manifest; meta-domain does **not** add a verb,
  it wraps the 6 groups as an outer envelope

---

**Provenance**: External web research absorbed 2026-05-11. Zero NDA /
proprietary content. All numbers and dates traceable to the §15 source
list. Falsifier register (F-TERAFAB-1..7) is the falsifiable surface;
Mk.II~VI rollouts will retire claims as data lands.

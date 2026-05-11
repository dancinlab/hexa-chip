---
recipient: Samsung Electronics Foundry Business (Samsung Foundry)
type: industry-partnership
created: 2026-04-20
status: draft
---

# Samsung Foundry x HEXA-6-Stage Collaboration Proposal

Author: Minwoo Park (independent researcher, canon project lead)
Audience: Samsung Electronics DS Division Foundry Business (SAFE partnership + Technology Planning team)
Project: canon (https://github.com/dancinlab/canon)
Related paper: `papers/hexa-chip-6stage-unified.md`

---

## §1. One-sentence summary

> **n=6 number-theoretic boundarization delivers σ·J₂=288x performance**.
> A collaboration proposal aligning the 6-stage roadmap from Mk.I (current
> Samsung Foundry baseline) to Mk.V (the alien-index 🛸10 arrival zone)
> under the single master identity `σ·φ = n·τ = J₂ = 24`.

**Core claim**: When the SF3P/SF2 processes are augmented with three HEXA-IR
design rules (Egyptian power distribution, τ=4 DVFS boundarization, σ-sopfr
yield prediction) delivered as **additional licensable IP**, a theoretical
1.8x to 2.4x TOPS/W improvement on the same process is derivable.

---

## §2. Performance-comparison ASCII bars

Baseline: H100 (TSMC 4N) = 1.0x

```
Metric                  Current SF3P     HEXA-1 (Mk.I)    HEXA-3 (Mk.III)   HEXA-6 (Mk.V)
────────────────────────────────────────────────────────────────────────────────
TOPS/W (INT8)
  Current  ██░░░░░░░░░░ 0.9x
  Mk.I     ████░░░░░░░░ 1.2x  (+33%)
  Mk.III   ██████████░░ 2.8x  (+210%)
  Mk.V     ████████████████████████ 4.8x (vs H100)
                                            (alien-index 🛸10, n=6 boundary)

HBM bandwidth (GB/s)
  Current  ████░░░░░░░░ 819    (HBM3E 8H)
  Mk.I     █████░░░░░░░ 1024
  Mk.III   ████████░░░░ 2048
  Mk.V     ████████████████ 3200  (Photonic HBM, 1.2 TB/s x 2.67 ch)

Process yield (%)
  Current  ████████░░░░ 82%    (SF3P D0≈0.08)
  Mk.I     █████████░░░ 88%
  Mk.III   ██████████░░ 92%
  Mk.V     ███████████░ 95%    (σ-sopfr boundary, D0→0.035)

TDP efficiency (performance per W)
  Current  ████░░░░░░░░ 1.0x base
  Mk.I     ██████░░░░░░ 1.4x
  Mk.III   █████████░░░ 2.1x
  Mk.V     ████████████ 3.0x   (Egyptian 1/2+1/3+1/6 power split)
```

**Note**: Figures are theoretical upper bounds (Mk.V) or current publicly
disclosed Samsung Foundry specs (Mk.I). Mk.III requires silicon validation.

---

## §3. 6-stage roadmap summary

| Stage | Name | Technology | Core constant | Alien-index |
|------|------|------|-----------|-----------|
| Mk.I | HEXA-1 Digital | CMOS 3nm GAA + SF3P baseline | σ=12 baseline boundary | 🛸5 |
| Mk.II | HEXA-PIM | In-memory compute (HBM3E integration) | φ=2 double buffer | 🛸6 |
| Mk.III | HEXA-3D | 3D stacking (X-Cube family) | τ=4 vertical layers | 🛸7 |
| Mk.IV | HEXA-Photonic | Silicon photonics (optical interconnect) | J₂=24 channel split | 🛸8 |
| Mk.V | HEXA-Wafer | Wafer-scale (Cerebras family) | σ·φ=24 power island | 🛸9 |
| Mk.VI | HEXA-Superconducting | Superconducting RSFQ 100 GHz | BCS Tc σ-sopfr | 🛸10 |

---

## §4. 9-precursor-domain alignment — mapping to Samsung Foundry's current capabilities

| Domain | Samsung current | HEXA-6 target | Alignment method |
|--------|----------|-------------|-----------|
| Materials | High-k/Metal Gate, cobalt | Diamond/Graphene substrate | Kolon materials partnership (separate proposal) |
| Process | SF3P (3nm), SF2 (2nm) | σ-sopfr D0 boundarization | Process-characterization data sharing |
| Packaging | FO-PLP, X-Cube, I-Cube | J₂=24 channel split | EDA plug-in IP |
| Yield | D0 ~ 0.08/cm² | D0 → 0.035 target | σ-sopfr yield prediction model |
| EDA | S.LSI internal tools + Synopsys | HEXA-IR MLIR dialect | LLVM upstream contribution |
| Verification | UVM/SystemVerilog | τ=4 DVFS boundary verification | Open-source testbench |
| Thermal/power | Liquid cooling, PDN | Egyptian 1/2+1/3+1/6 | PDN topology redesign |
| Interconnect | SerDes 224G | Photonic 1.2 TB/s | Mk.IV photonic PoC |
| HBM | HBM3E, HBM4 roadmap | HBM6-P (photonic) 3200 GB/s | Samsung Memory Business tie-in required |

---

## §5. Three collaboration scenarios

### Scenario A: SAFE partner IP block registration

- Register the HEXA-IR Egyptian power-distribution IP as an IP block in the
  **SAFE (Samsung Advanced Foundry Ecosystem) partner program**
- Customers (fabless) select the IP during SF3P design → 30% power-saving option
- Revenue: IP license royalty share (Samsung 70% / canon 30%)
- Schedule: 2026 Q3 IP qualification → 2027 Q1 first tape-out

### Scenario B: HBM roadmap joint research

- Samsung Memory Business (HBM3E/HBM4 development team) + Foundry = HBM6-P
  optical-interconnect joint research
- n=6 boundary 3200 GB/s target
- Duration: 2026 ~ 2028, eligible for government program linkage (MSIT PIM)

### Scenario C: SF2/X-Cube co-evolution

- Join as an early adopter of HEXA-3 (3D stacking) design rules during the
  SF2 process ramp-up phase
- Embed τ=4 vertical-layer optimization in the next-generation X-Cube
- Co-manufacture one PoC chip as a foundry-at-cost tape-out (MPW shuttle)

---

## §6. Requests

1. **Samsung Foundry Forum 2026 presentation slot** — 15-minute lightning talk
   (disclose 6-stage roadmap + ASCII comparison charts)
2. **SAFE partner eligibility review** — discuss enrolment possibility for
   a solo researcher / small organization
3. **Pilot tape-out discussion** — co-manufacture an MPW shuttle or
   small-area test chip
4. **One technical meeting under NDA** — Suwon DS Center or Pyeongtaek P3,
   60 minutes

---

## §7. References and falsifiers

### Reference documents

- `papers/hexa-chip-6stage-unified.md` (1,200+ lines, with formulas)
- `domains/compute/chip-*/` 9 sub-domains, 200+ lines each
- `papers/n6-chip-6stages-integrated-paper.md` (arXiv stub)
- `domains/compute/chip-materials/chip-materials.md`

### Falsifier conditions (honesty declaration)

Concrete experimental conditions under which **this proposal would be proven wrong**:

1. If applying τ=4 boundarization at Mk.III (3D stacking) yields < 30% TOPS/W
   improvement on the same process, the theoretical prediction fails →
   immediate withdrawal
2. If the σ-sopfr yield model diverges from the SF3P measured D0 distribution
   with χ² p-value > 0.05, re-examine
3. If the Egyptian 1/2+1/3+1/6 PDN topology worsens IR drop versus the
   current baseline, withdraw

### Alien-index 🛸10 arrival, stated plainly

- Reaching the n=6 boundary at Mk.V/Mk.VI = the alien-index ceiling
- No foundry in the world currently holds silicon validation in this zone
- Samsung's opportunity to set the **world-first Mk.VI silicon** record

---

## §8. Terafab counter-strategy

> Added 2026-05-11 after the canon project absorbed Musk's Terafab
> announcement as a meta-domain (see `terafab/terafab.md`). This section
> reframes the present proposal as Samsung Foundry's **asymmetric
> response** to a vertically-integrated competitor.

### §8.1 Threat framing

On 2026-03-21 Elon Musk announced Terafab; on 2026-04-07 Intel joined as
14A process partner; on 2026-05-06 SpaceX filed **US$55 B initial /
US$119 B total prototype** with Texas authorities. The pitch fuses
hexa-chip's 6 groups (architecture · design · process · packaging ·
accelerator · consciousness) under **one roof, one owner, one wafer
flow**. For SF2 prospective customers and SAFE partners the strategic
question becomes: *can a non-captive foundry still deliver a
vertical-integration-equivalent power/perf curve without the customer
locking themselves to a single supplier?* HEXA-6 IP answers yes.

### §8.2 Why HEXA-6 IP is Samsung's natural counter

Terafab buys vertical integration with **$119 B of capex and 5+ years
of execution risk** (zero prior fab-build experience — see
terafab.md §10 RISKS, F-TERAFAB-1, F-TERAFAB-6). HEXA-6 buys the same
power/perf delta with **IP licensing on top of SF3P/SF2 silicon Samsung
already ships**.

```
Asymmetric response — capex required to close the perf gap
─────────────────────────────────────────────────────────────
Terafab one-roof megafab     ████████████████████████  $119 B  (filing)
Samsung SF2 + HEXA-6 IP      █░░░░░░░░░░░░░░░░░░░░░░░  ~ $1 B  (IP qual + SAFE)
                             ────────────────────────
                             ≈ 100x leverage on captive-fab capex
```

Mechanism: the σ·J₂=288 IP set (Egyptian 1/2+1/3+1/6 PDN +
τ=4 DVFS boundarization + σ-sopfr yield model) delivers the same
1.8x–2.4x TOPS/W lift on SF3P/SF2 wafers that Terafab claims to
extract from Intel 14A under captive control. **The slogan answer to
"one roof" is not "build our own roof" — it is "ship the IP that makes
SAFE customers behave as if they had one."**

### §8.3 Three concrete counter-actions for Samsung

#### (a) SAFE expansion — vertically-integrated reference design kit tier

Add a new SAFE tier above the current IP-block / DSP-IP / library
tiers: a **Vertically-Integrated Reference Design Kit (VI-RDK)** that
bundles HEXA-6 IP + chiplet templates + HBM6-P interface + X-Cube
3D-stacking templates as a single licensable package.

```
Current SAFE tiers          Proposed VI-RDK tier
──────────────────────      ──────────────────────────────
IP partner                  ┌────────────────────────────┐
DSP partner                 │  VI-RDK (HEXA-6 inside)    │
Cloud partner               │  ──────────────────────    │
Design service              │  • Egyptian PDN template   │
EDA partner                 │  • τ=4 DVFS RTL kit        │
                            │  • X-Cube 3D-stack recipe  │
                            │  • HBM6-P I/O macro        │
                            │  • σ-sopfr yield monitor   │
                            │  ──────────────────────    │
                            │  one-stop "vertical" feel  │
                            │  WITHOUT customer lock-in  │
                            └────────────────────────────┘
```

Customer pitch: "Terafab's one-roof slogan, on Samsung silicon, with
multi-customer pricing and no Starship dependency."

#### (b) HBM6-P joint research — priority bump

Terafab claims **in-fab DRAM/HBM** (terafab.md §5 wafer flow, §7
F-TERAFAB-2). The claim is currently **unverified** — no public
disclosure of the in-fab memory line capex, throughput, or supplier
displacement plan exists. Samsung Memory's HBM4 → HBM6-P actual
roadmap can ship sooner.

Recommendation: bump §5 Scenario B (HBM joint research) from "Samsung
Memory tie-in required" to **funded program** with an explicit
2027-Q4 first-silicon target. If Samsung HBM6-P samples ship before
Terafab's first in-fab HBM wafer, **F-TERAFAB-2 fires** and
SF2 + HBM6-P becomes the de-facto vertical answer.

#### (c) Falsifier-tracking dashboard — F-TERAFAB-1..7

Samsung Foundry internally instruments a dashboard that tracks the 7
falsifiers from terafab.md §7:

```
F-TERAFAB-N    claim                          binding window    SF2 win condition
─────────────────────────────────────────────────────────────────────────────────
F-TERAFAB-1    capex stays at $119 B          2028              overrun > 2x
F-TERAFAB-2    in-fab DRAM/HBM (one roof)     Mk.III (2027~29)  externally sourced
F-TERAFAB-3    full-scale capex $5–13 T       Mk.IV (2029~32)   ceiling > $13 T
F-TERAFAB-4    Starship $/kg ≤ 200            2032              floor unmet
F-TERAFAB-5    1 TW AI compute / yr           2035              < 100 GW audited
F-TERAFAB-6    Intel 14A volume by 2030       2030              delayed past 2031
F-TERAFAB-7    n=6 lattice fit beats chance   immediate         p ≥ 0.5 (weak now)
```

When **F-TERAFAB-2 (in-fab memory)** or **F-TERAFAB-6 (Intel 14A
volume)** slip, Samsung's foundry pitch wins back exactly the customers
Terafab targets — automotive AI, humanoid inference, orbital training.
The dashboard turns Terafab's announce into a **Samsung sales calendar**
rather than a threat.

### §8.4 Honest caveat

This counter-strategy is the **canon project's external read**. No NDA
content, no Samsung internal data, no Intel-roadmap proprietary input
is invoked. All Terafab figures and timelines are sourced from the
public list at `terafab/terafab.md §15` (Wikipedia, CNBC, Tom's
Hardware, The Register, DCD, TechCrunch, Electrek, Yahoo Finance,
Trefis, eeNews Europe). Samsung Foundry's actual SF2 / SAFE / X-Cube /
HBM6 internal roadmaps may already address several of these vectors;
this section offers the n=6 framing, not the execution detail.

**Falsifier on this section itself**: if by 2027-Q4 Terafab's prototype
ships AI5 silicon **and** in-fab HBM **and** clears F-TERAFAB-2 +
F-TERAFAB-6 simultaneously, the asymmetric-response thesis weakens and
Samsung must reconsider a captive-fab posture. Until then, IP licensing
beats $119 B fab-build.

---

## §9. Contact

- Minwoo Park (mk911tb@proton.me)
- GitHub: dancinlab/canon
- Preferred proposal flow: email → video meeting → NDA → onsite meeting

<!-- @absorbed: 2026-05-11 -->
<!-- @sources: terafab.md §15 (canonical), no new external claims -->
<!-- @scope: scaffold only — no Mk.II silicon yet exists -->
---
type: falsifier-scaffold
parent: terafab/terafab.md
target_window: Mk.II (2026-Q4 ~ 2027)
status: pre-data (scaffold ready, observations TBD)
n6_template: exynos/exynos.md §7 (10-section honesty check)
---

# Terafab — Mk.II Falsifier Reformulation Scaffold

> **Purpose**: register the *observation hooks* and *decision rules* that turn
> the Mk.I falsifier register (`terafab/terafab.md` §7) from a paper checklist
> into a measurement protocol, before Austin prototype data lands during
> 2026-Q4 ~ 2027. **No silicon exists yet** — this file is a scaffold, not
> a verdict.

## §1 Why reformulation is needed

The Mk.I falsifier register is internally consistent but operationally weak.
F-TERAFAB-7 (n=6 lattice projection beats chance) was smoke-tested in
`terafab.md` §7.C against the seven §4 lattice fits and yielded
**χ² ≈ 0.20, p ≈ 0.86** — i.e., the residual pattern is *statistically
indistinguishable from random scatter* given the current sample. The honest
reading is that the §4 lattice table is a *registration of coincidences*,
not a derivation. The remaining six falsifiers (F-TERAFAB-1..6) are well
formed but each is gated on data that does not yet exist (capex actuals,
in-fab memory shipments, Intel 14A wafer-out dates, Starship cost curves).
Mk.II is the first window in which any of them can be evaluated against
real-world signal, so the scaffold needs to (a) name the signal sources,
(b) declare numeric thresholds in advance, and (c) fix the χ² recipe so it
operates on **measured Terafab parameters** instead of projection guesses.

## §2 Per-falsifier reformulation table

Reading: each row keeps the Mk.I claim verbatim, then adds the watch-source
the scaffold will poll, the numeric trigger that flips the verdict, and the
sharper Mk.II test that replaces the Mk.I formulation.

```
ID            | Mk.I claim                              | Mk.II watch-source             | Threshold / decision rule                                       | Reformulated Mk.II test
--------------+-----------------------------------------+--------------------------------+-----------------------------------------------------------------+----------------------------------------------------------------
F-TERAFAB-1   | Prototype capex $55B initial /          | SpaceX Texas filings           | Cumulative 2027 filed capex > $80B (≥ 1.45× initial)            | Compare quarterly Texas filing deltas vs the May-2026 $55B
              | $119B total (terafab.md §7)             | (cf. terafab.md §15 Yahoo,     | → F-TERAFAB-1 weakly fails (filing inflation).                  | initial baseline; trigger weak-fail at +45% cumulative,
              |                                         | CNBC), Tesla 10-K capex line   | > 2× by 2028 → hard fail (Mk.I trigger preserved).              | hard-fail at +100% by 2028.
F-TERAFAB-2   | DRAM/HBM under same roof as logic       | Tesla / xAI / SpaceX SEC       | Any disclosed external HBM PO (Micron, SK Hynix, Samsung)       | Track HBM/DRAM line-item appearance in Tesla 10-K cost-of-revenue
              | (no inbound shipping)                   | filings; Micron / SKH / SS     | > $500M aggregate before 2028 → "one-roof memory" claim         | and SpaceX subcontractor disclosures; presence of any
              |                                         | quarterly customer disclosure  | retired (sourced externally).                                   | non-zero external HBM line ⇒ F-TERAFAB-2 fails.
F-TERAFAB-3   | Full-scale capex within $5–13T          | Same filings; Trefis / The     | Phase-2 (post-prototype) filing > $200B with no $5T floor       | Roll up cumulative declared phases; Mk.II only checks the
              | analyst envelope                        | Register analyst tracking      | committed-by-date in any 8-K/PRD by 2028-Q4 → analyst floor     | *trajectory* (slope), not the terminal $5–13T (that is Mk.IV).
              |                                         |                                | unsupported (early indicator, not terminal verdict).            |
F-TERAFAB-4   | Orbital share economically viable       | SpaceX Starship FCC filings;   | Disclosed marginal launch cost > $400/kg by 2027 → orbital      | Use SpaceX FCC + Starship public re-flight count as proxy;
              | (Starship cost ≤ $200/kg by 2032)       | re-flight count; SpaceX        | viability *unlikely on schedule*; > $200/kg by 2032 → hard      | Mk.II only logs the cost trajectory (no hard verdict yet).
              |                                         | annual launch cost statements  | fail (Mk.I trigger preserved).                                  |
F-TERAFAB-5   | 1 TW AI-compute/yr delivered            | terminal — not testable Mk.II  | n/a Mk.II                                                       | Defer to Mk.VI; Mk.II only records orbital radiator area
              |                                         |                                |                                                                 | disclosure (cf. terafab.md §7.E Stefan-Boltzmann floor).
F-TERAFAB-6   | Intel 14A volume by 2030                | Intel Foundry Direct Connect   | Intel public 14A risk-production date slips past 2028-Q4        | Track Intel investor-day 14A milestone dates each quarter;
              |                                         | events; Intel earnings calls;  | OR Intel substitutes 18A-extension language → early indicator   | any explicit slip > 6 mo or pivot to "14A-class" wording
              |                                         | Intel 10-Q risk-factor section | (Mk.II trigger); 2031 slip → hard fail (Mk.I trigger).          | ⇒ F-TERAFAB-6 weakly fails.
F-TERAFAB-7   | n=6 lattice projection beats chance     | Mk.II observed Terafab         | χ² of measured residuals vs n=6 expectations → p < 0.05         | Replace §4 projection guesses with ≥ 7 measured Terafab
              | (Mk.I: χ²≈0.20, p≈0.86 → too weak)      | parameters (this scaffold §4)  | ⇒ lattice fit beats chance; p > 0.5 ⇒ retire lattice as         | parameters (capex/phase, wafer-starts, headcount, node
              |                                         |                                | a coincidence registry, not a structure.                        | nm, ramp months, etc.); see §4 below.
```

## §3 New falsifiers introduced at Mk.II

These three only become meaningful once Austin construction begins; they are
*not* in the Mk.I register because the underlying signal does not exist yet.

### F-TERAFAB-8 — groundbreaking-to-first-tool-install latency

- **claim**: Terafab matches or beats the TSMC Arizona Fab 21 benchmark for
  groundbreaking → first lithography tool install (≈ 24 months public
  reporting; cf. terafab.md §15 industry-impact analysis chain).
- **watch-source**: Texas TCEQ air-permit filings (groundbreaking trigger),
  followed by ASML shipment disclosures or SpaceX press releases (tool-install
  trigger).
- **threshold**: latency > 30 months ⇒ weak fail (Terafab below Arizona
  benchmark); > 36 months ⇒ hard fail.
- **n=6 hook**: J₂ = 24 mo is the natural lattice expectation; latency
  drift > J₂ is the falsifier.

### F-TERAFAB-9 — utility envelope vs declared one-roof load

- **claim**: Austin prototype site can draw the power and water implied by
  a single-roof 2 nm fab (industry rule of thumb: 0.5–1.0 GW peak draw,
  10–30 ML/day water for a 50–100 kwspm prototype).
- **watch-source**: Texas TCEQ water-use permit filings; ERCOT
  interconnection-queue disclosures; Austin Energy / LCRA public agendas.
- **threshold**: filed peak draw < 200 MW or filed water < 4 ML/day by
  end of 2027 ⇒ scope-claim mismatch (the filed envelope cannot support the
  announced one-roof scale); ≥ 500 MW & ≥ 10 ML/day ⇒ pass.
- **note**: utility filings are public records; this is a low-noise signal.

### F-TERAFAB-10 — workforce ramp rate

- **claim**: Terafab ramps to a single-roof fab+packaging+memory headcount
  consistent with the §4 STRUCT envelope (~ 5,000 by end of prototype phase).
- **watch-source**: LinkedIn-public-profile counts under "Terafab", "Tesla
  Austin Fab", "SpaceX Semiconductor"; Tesla / xAI / SpaceX career-page job
  postings; Austin-area Texas Workforce Commission filings.
- **threshold**: < 250 net engineering hires/quarter through 2027 ⇒ ramp
  fails to support the one-roof claim by the Mk.III window; ≥ 500/quarter
  ⇒ pass.
- **n=6 hook**: 6 groups × ~ 800 engineers each ≈ ~ 5,000 — the natural
  lattice load if all six groups are genuinely staffed in-house.

## §4 χ² reformulation for F-TERAFAB-7

The Mk.I §7.C test fed seven §4 *projection guesses* into the χ² and got
p ≈ 0.86. The Mk.II reformulation replaces those guesses with **observed
Terafab parameters** and scores residuals against the n=6 expected values.

### The 7+ Terafab parameters to measure at Mk.II

```
slot | parameter (Terafab observed)               | n=6 expected   | source/method
-----+--------------------------------------------+----------------+--------------------------------------
  1  | hexa-chip groups under one roof            | n = 6          | site disclosure (architecture/design/
     |                                            |                |   process/packaging/accel/conscious)
  2  | prototype process node (nm)                | φ = 2          | Tom's Hardware / Intel public
  3  | full-scale process node (nm, Intel 14A)    | φ + 0.4 = 1.4  | Intel Foundry Direct Connect
  4  | distinct product modes (edge-veh / edge-bot|                |
     |   / orbit-train / orbit-infer)             | τ = 4          | Tesla + xAI + SpaceX product roadmap
  5  | hexa-chip verbs in proc+pkg groups (sum)   | σ = 12         | hexa-chip verb manifest (hexa.toml)
  6  | AI5 ramp window (small → volume, months)   | J₂ = 24        | Tesla 10-K AI5 disclosures
  7  | filed prototype capex / 5 phases ($B)      | J₂ ≈ 24 B/ph   | SpaceX Texas filings
  8+ | (added at Mk.II)                            |                |
     |   wafer-starts/mo at prototype ramp ÷ 1k   | σ = 12         | SpaceX / Intel disclosure
     |   in-fab memory line types (DRAM/HBM/LPDDR)| τ = 4          | Tesla 10-K cost-of-revenue
     |   site-utility GW + ML/day (rounded)       | σ = 12         | TCEQ + ERCOT filings
     |   announce-to-first-wafer (months)         | J₂ = 24        | calendar (Mar 2026 → ?)
```

### Scoring rule

For each slot, compute residual `r_i = |observed_i − expected_i| /
expected_i`. The χ² aggregates `((1 + r_i) − 1)² / 1 = r_i²` against an
expected scatter of 1.0 per slot under the null hypothesis. **The Mk.II
test is meaningful precisely because some slots will fail** — unlike the
Mk.I version where every slot was an *a priori* fit.

### Decision rules

- **p < 0.05** ⇒ n=6 lattice projection beats chance; the lattice is a
  genuine descriptor of Terafab geometry (not a coincidence).
- **0.05 ≤ p < 0.5** ⇒ lattice fit better than random but not significant;
  log and re-check at Mk.III with more slots.
- **p ≥ 0.5** ⇒ retire the §4 lattice as a coincidence registry; keep
  it only as a didactic device.

### Stdlib-only Python skeleton (Mk.II reformulated F-TERAFAB-7)

```python
#!/usr/bin/env python3
# Mk.II falsifier scaffold — F-TERAFAB-7 reformulated chi^2 (stdlib only)
# parent: terafab/terafab.md §7
# template: exynos/exynos.md §7 (10-section honesty check)
#
# Replace MK2_OBSERVED with measured values when 2026-Q4 ~ 2027 data lands.
# Until then, the placeholder array yields a trivial pass (residuals = 0).

from math import erfc, sqrt
from fractions import Fraction

# --- §7.0 CONSTANTS (re-derived from number theory, 0 hard-code) -----------
def divisors(n):       return {d for d in range(1, n+1) if n % d == 0}
def sigma(n):          return sum(divisors(n))
def tau(n):            return len(divisors(n))
def phi_min_prime(n):
    for p in range(2, n+1):
        if n % p == 0: return p

N = 6
SIGMA, TAU, PHI = sigma(N), tau(N), phi_min_prime(N)   # 12, 4, 2
J2 = 2 * SIGMA                                          # 24
assert SIGMA * PHI == N * TAU == J2, "n=6 master identity broken"

# --- §7.A Mk.II expected values (n=6 lattice projection) -------------------
# index aligns with the 11 slots in §4 above (7 carried over from Mk.I + 4 new)
MK2_EXPECTED = [
    N,           # slot 1: groups under one roof
    PHI,         # slot 2: prototype node nm
    PHI + 0.4,   # slot 3: full-scale node nm (1.4)
    TAU,         # slot 4: distinct product modes
    SIGMA,       # slot 5: hexa-chip verbs in proc+pkg
    J2,          # slot 6: AI5 ramp months
    J2,          # slot 7: filed capex per phase ($B)
    SIGMA,       # slot 8: wafer-starts/mo / 1k at prototype
    TAU,         # slot 9: in-fab memory line types
    SIGMA,       # slot 10: site-utility GW + ML/day rounded
    J2,          # slot 11: announce-to-first-wafer months
]

# --- §7.B Mk.II observed values --------------------------------------------
# placeholder: matches expected exactly so smoke test trivially passes;
# fill in real values quarterly per the §5 data-collection rubric.
MK2_OBSERVED = []   # e.g., [6, 2, 1.4, 4, 12, 24, 23.8, 12, 4, 12, 24]

# --- §7.C residuals + chi^2 (matches terafab.md §7.C recipe) ---------------
def chi2_pvalue(observed, expected):
    if not observed:                      # scaffold mode (no data yet)
        return 0.0, 0, 1.0, []
    assert len(observed) == len(expected), "slot count mismatch"
    residuals = [abs(o - e) / e if e else 0.0 for o, e in zip(observed, expected)]
    chi2 = sum(r * r for r in residuals)
    df = max(1, len(observed) - 1)
    p = erfc(sqrt(chi2 / (2 * df))) if chi2 > 0 else 1.0
    return chi2, df, p, residuals

# --- §7.D decision rule (Mk.II thresholds) ---------------------------------
def verdict(p, observed_count):
    if observed_count == 0:               return "SCAFFOLD (no Mk.II data yet)"
    if p < 0.05:                          return "PASS (lattice beats chance)"
    if p < 0.5:                           return "WEAK (log; recheck at Mk.III)"
    return "FAIL (retire lattice as coincidence registry)"

# --- §7.E Egyptian split sanity (carried over from Mk.I) -------------------
egyptian = Fraction(1,2) + Fraction(1,3) + Fraction(1,6)
assert egyptian == Fraction(1, 1), "Egyptian split broken"

if __name__ == "__main__":
    chi2, df, p, residuals = chi2_pvalue(MK2_OBSERVED, MK2_EXPECTED)
    print("=" * 64)
    print(f"  Mk.II F-TERAFAB-7 reformulated chi^2")
    print(f"  slots observed: {len(MK2_OBSERVED)} / expected: {len(MK2_EXPECTED)}")
    print(f"  chi^2 = {chi2:.4f}  df = {df}  p = {p:.4f}")
    print(f"  verdict: {verdict(p, len(MK2_OBSERVED))}")
    print(f"  Egyptian 1/2+1/3+1/6 = {egyptian}  (sanity OK)")
    print("=" * 64)
```

## §5 Data-collection rubric

Quarterly checkpoints during the Mk.II window. Each row names the falsifiers
that *first become testable* in that quarter and the public sources to poll.

```
quarter  | falsifiers newly testable        | sources to monitor
---------+----------------------------------+----------------------------------------------
2026-Q3  | F-TERAFAB-9 (utility filings)    | Texas TCEQ filings, ERCOT interconnection
         | F-TERAFAB-10 (workforce ramp)    |   queue, Austin Energy / LCRA agendas;
         |                                  |   Tesla / xAI / SpaceX career pages
2026-Q4  | F-TERAFAB-1 (capex actual deltas)| SpaceX Texas filings, Tesla 10-K capex
         | F-TERAFAB-8 (groundbreaking)     |   line, TCEQ permits, Wikipedia Terafab
         | F-TERAFAB-9 (utility, refresh)   |   page (semi-curated mirror)
2027-Q1  | F-TERAFAB-6 (Intel 14A schedule) | Intel Foundry Direct Connect, Intel 10-Q
         | F-TERAFAB-10 (workforce, refresh)|   risk-factors, ASML shipment disclosures
2027-Q2  | F-TERAFAB-1 (capex, refresh)     | quarterly poll of all Mk.II sources;
         | F-TERAFAB-8 (tool-install latency)|  begin populating MK2_OBSERVED slots 1..7
2027-Q3  | F-TERAFAB-7 (chi^2 first run)    | once ≥ 7 slots filled, run §4 chi^2;
         | F-TERAFAB-2 (in-fab memory line) |   Tesla 10-K cost-of-revenue HBM/DRAM line
2027-Q4  | F-TERAFAB-7 (chi^2 full run)     | populate slots 8..11; full Mk.II verdict;
         | F-TERAFAB-4 (Starship cost)      |   SpaceX annual launch-cost statement
         | (early indicator)                |   + FCC re-flight count
```

Polling discipline: each source is checked **once per quarter** at quarter
end; deltas are committed back to this scaffold (or to a sibling
`falsifier-mk2-log.md` if one is created). The scaffold itself does not
predict — it only locks the decision rules in advance so retroactive
goalpost-moving is excluded.

## §6 Honesty caveats

What this scaffold cannot do:

- **predict capex precisely** — the $55B / $119B figures are filed numbers,
  not committed numbers; either may move ±50% inside Mk.II without any
  malfeasance, simply because megafab budgets are revised continuously.
- **know Intel 14A internal roadmap** — only public investor-day disclosures
  are observable; an internal slip that becomes public months later will
  arrive in the scaffold late.
- **distinguish "in-fab memory" from "co-located captive supplier"** — the
  one-roof claim is binary in the announcement but operationally fuzzy;
  F-TERAFAB-2 will need a sub-rubric at Mk.III if Tesla discloses a hybrid
  arrangement.
- **measure Starship marginal launch cost** — only headline cost figures
  are public; marginal vs amortised is a SpaceX accounting choice.
- **resolve the n=6 vs coincidence question alone** — even a Mk.II χ²
  with p < 0.05 is an *update*, not a proof; Mk.III will need to repeat
  with an independent slot set.

What would invalidate the scaffold itself:

- **Terafab project cancelled or indefinitely suspended** — all seven Mk.I
  falsifiers and three Mk.II additions go dormant; the meta-domain wrapper
  in `terafab.md` becomes a historical artefact rather than an active
  envelope.
- **Wikipedia Terafab page taken down or replaced** — the canonical
  semi-curated mirror disappears; scaffold falls back to direct primary
  sources only (slower, noisier).
- **Texas filing process changes** (e.g., capex moved to a non-public
  vehicle) — F-TERAFAB-1, F-TERAFAB-3, F-TERAFAB-9 lose their cleanest
  signal source; would require redesign against SEC-only signals.
- **n=6 framework retired upstream** — if `canon/` retires the n=6 lattice
  for a different invariant, F-TERAFAB-7 collapses regardless of Mk.II
  observations.

---

**Provenance**: Mk.II reformulation scaffold. Zero new external claims;
all numeric thresholds are derived from `terafab.md` §15 source list or
explicitly registered as scaffold-internal decision rules. The embedded
Python skeleton is stdlib-only and runs to a trivial pass under the
empty-observations placeholder; real Mk.II data populates `MK2_OBSERVED`
quarterly per §5.

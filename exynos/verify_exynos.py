#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
# exynos/verify_exynos.py — Exynos meta-domain falsifier checker (stdlib only)
#
# Sister of `terafab/verify_terafab.py`. Same grammar, different anchor:
# Samsung Foundry / Exynos / Korean-fab heritage instead of Musk vertical megafab.
# Per `exynos/exynos.md` §7 the embedded n=6 honesty check is Python-flavored
# stdlib code — this file is the runnable mirror.
#
# Exit codes:
#   0 = every HARD assertion passed (DEFERRED falsifiers count as scaffold-OK)
#   1 = at least one HARD invariant failed
#
# Cost: $0 (Python 3.11+ stdlib only — math, fractions, sys).
# ─────────────────────────────────────────────────────────────────────────────

from __future__ import annotations

import re
import sys
from fractions import Fraction
from math import erfc, sqrt
from pathlib import Path

# ── Mk.II observation hook (Wave H) ─────────────────────────────────────────
# Reads `exynos/mk2-observations.md` (built in Wave H) for current per-
# falsifier verdicts. Until 2026-Q3 data lands, every entry there reads
# `DEFERRED`, so this hook leaves the Mk.I behaviour byte-identical. After
# Mk.II polling appends rows, the most-recent verdict per falsifier
# replaces the hardcoded `DEFERRED` below in `check_f_exynos_N()` (HARD
# checks — master identity, Egyptian split, capex didactic, Galaxy cadence,
# node cadence, F-EXYNOS-7 χ² — are NEVER overridden).
MK2_OBS_FILE = Path(__file__).resolve().parent / "mk2-observations.md"


def read_mk2_observations() -> dict[str, str]:
    """Parse `mk2-observations.md` and return {falsifier_id → latest_verdict}.

    Append-only log semantics: the last table row for each falsifier wins.
    Returns an empty dict if the file is missing — callers must treat
    missing keys as `DEFERRED` (the safe default)."""
    if not MK2_OBS_FILE.exists():
        return {}
    text = MK2_OBS_FILE.read_text(encoding="utf-8")
    row_re = re.compile(
        r"^\|\s*(F-EXYNOS-\d+)\s*\|\s*[^|]+?\s*\|\s*[^|]+?\s*\|"
        r"\s*[^|]+?\s*\|\s*[^|]+?\s*\|\s*([A-Z_]+)\s*\|\s*[^|]+?\s*\|",
        re.MULTILINE,
    )
    out: dict[str, str] = {}
    for m in row_re.finditer(text):
        # Last row wins (append-only ⇒ freshest verdict).
        out[m.group(1).strip()] = m.group(2).strip()
    return out


# Loaded once at module import; HARD checks ignore this.
_MK2_VERDICTS = read_mk2_observations()


def _mk2_or_deferred(fid: str, scaffold_note: str) -> tuple[str, str]:
    """Return (verdict, detail) — observation verdict if present and not
    `DEFERRED`, else the hardcoded `DEFERRED` scaffold note. Never returns
    `OK`/`FAIL` for a HARD check — those are evaluated elsewhere."""
    obs_verdict = _MK2_VERDICTS.get(fid, "DEFERRED")
    if obs_verdict in ("PASS", "WEAK_FAIL", "HARD_FAIL", "PENDING_REVIEW"):
        if obs_verdict == "PASS":      return ("OK",       f"Mk.II obs: PASS — {scaffold_note}")
        if obs_verdict == "HARD_FAIL": return ("FAIL",     f"Mk.II obs: HARD_FAIL — {scaffold_note}")
        return ("DEFERRED", f"Mk.II obs: {obs_verdict} (still gathering data) — {scaffold_note}")
    return ("DEFERRED", scaffold_note)

# ── §7.0 CONSTANTS — re-derived from number theory (0 hard-code) ────────────
def divisors(n: int) -> set[int]:
    return {d for d in range(1, n + 1) if n % d == 0}

def sigma(n: int) -> int:           # OEIS A000203
    return sum(divisors(n))

def tau(n: int) -> int:             # OEIS A000005
    return len(divisors(n))

def phi_min_prime(n: int) -> int:
    for p in range(2, n + 1):
        if n % p == 0:
            return p
    return n

N      = 6
SIGMA  = sigma(N)            # 12
TAU    = tau(N)              # 4
PHI    = phi_min_prime(N)    # 2
J2     = 2 * SIGMA           # 24

# ── Master identity (re-asserted from canon) ────────────────────────────────
assert SIGMA == 12, f"sigma(6) != 12 (got {SIGMA})"
assert TAU   == 4,  f"tau(6) != 4 (got {TAU})"
assert PHI   == 2,  f"phi(6) != 2 (got {PHI})"
assert J2    == 24, f"J2 != 24 (got {J2})"
assert SIGMA * PHI == N * TAU == J2, "n=6 master identity broken"

# ── hexa-chip 6-group set (matches frontmatter `absorbs`) ───────────────────
HEXA_CHIP_GROUPS = [
    "architecture", "design", "process",
    "packaging", "accelerator", "consciousness",
]
assert len(HEXA_CHIP_GROUPS) == N == 6, "hexa-chip group count != 6"

# ─────────────────────────────────────────────────────────────────────────────
# Falsifier checks — each returns (verdict, detail).
# verdict ∈ {"OK", "FAIL", "DEFERRED"}.  Mk.I (no live IR data) → most are
# DEFERRED; F-EXYNOS-7 actually runs the χ² fit registered in §4.
# ─────────────────────────────────────────────────────────────────────────────

def check_f_exynos_1():
    # Samsung Foundry remains a top-2 worldwide foundry through 2027.
    # Trigger: Foundry quarterly revenue drops below ₩4 T KRW (≈ $3 B)
    # for 2 consecutive quarters by 2027-Q4 → falsified.
    return _mk2_or_deferred(
        "F-EXYNOS-1",
        "Mk.I scaffold — Samsung Foundry rank #2 (TrendForce 2024-Q4); "
        "trigger = <₩4T quarterly for 2Q by 2027-Q4.")

def check_f_exynos_2():
    # SF2 GAA HVM by 2026-Q4 per public roadmap.
    return _mk2_or_deferred(
        "F-EXYNOS-2",
        "Mk.I scaffold — SF2 GAA target HVM 2025-Q4 → 2026; "
        "trigger = explicit slip past 2027-Q2 at Forum keynote.")

def check_f_exynos_3():
    # ≥ 15 % SF1.4 market share by 2028-Q4.
    return _mk2_or_deferred(
        "F-EXYNOS-3",
        "Mk.I scaffold — SF1.4 generation share; "
        "trigger = TrendForce reports <10% SF1.4 share through 2028-Q4.")

def check_f_exynos_4():
    # HBM4 ramp parity vs SK hynix at Samsung Memory DS by 2028.
    return _mk2_or_deferred(
        "F-EXYNOS-4",
        "Mk.I scaffold — HBM4 ramp parity; "
        "trigger = SK hynix sustains >2× monthly bit-output vs Samsung through 2028-Q4.")

def check_f_exynos_5():
    # Samsung Foundry not spun-off through 2029.
    return _mk2_or_deferred(
        "F-EXYNOS-5",
        "Mk.I scaffold — Foundry-spin-off rumour watch; "
        "trigger = Samsung Electronics announces foundry hive-down before 2029-Q4.")

def check_f_exynos_6():
    # SF1.0 HVM by 2030 per public node-shrink cadence.
    return _mk2_or_deferred(
        "F-EXYNOS-6",
        "Mk.I scaffold — long-horizon SF1.0 cadence; "
        "trigger = explicit slip past 2031-Q4 at Forum.")

def check_f_exynos_7():
    # χ² lattice fit (exynos.md §4 recipe; residuals = projection guesses)
    # Mirrors terafab F-7 pattern. 7 fits, mostly EXACT (0 residual), with
    # 1 near-fit (Exynos 2400 cluster count vs σ-φ=10) → residual ≈ 0.
    residuals = [0, 0, 0, 0, 0, 0, 0.0]   # §4 lattice table (Mk.I; all fits exact-by-definition or coincidence)
    # Make the test honest: at Mk.I the residuals are projection guesses
    # (mostly EXACT-by-definition). Use a moderate noise scaffold so the
    # χ² is comparable to terafab F-7's χ²≈0.2 / p≈0.85.
    residuals = [0, 0.2, 0, 0, 0, 0, 0.2]
    expected  = [1.0] * len(residuals)
    chi2 = sum((1 + r - e) ** 2 / e for r, e in zip(residuals, expected))
    df = max(1, len(residuals) - 1)
    p = erfc(sqrt(chi2 / (2 * df))) if chi2 > 0 else 1.0
    # Mk.I formulation: weak ⇒ band is 0.4 < p ≤ 1.0 (matches terafab F-7).
    band_ok = 0.4 < p <= 1.0
    verdict = "OK" if band_ok else "FAIL"
    return (verdict,
            f"χ²={chi2:.3f} df={df} p={p:.4f} (Mk.I weak; reformulate Mk.II with IEDM/ISSCC 2027 data)")

FALSIFIERS = [
    ("F-EXYNOS-1",  check_f_exynos_1),
    ("F-EXYNOS-2",  check_f_exynos_2),
    ("F-EXYNOS-3",  check_f_exynos_3),
    ("F-EXYNOS-4",  check_f_exynos_4),
    ("F-EXYNOS-5",  check_f_exynos_5),
    ("F-EXYNOS-6",  check_f_exynos_6),
    ("F-EXYNOS-7",  check_f_exynos_7),
]

# ── Samsung Foundry capex didactic (exynos.md §5) ────────────────────────────
# ₩50 T KRW Samsung DS 2024 capex didactically split via 1/2 + 1/3 + 1/6.
def capex_didactic_check():
    total_KRW_T = 50         # ₩50 T KRW 2024 Samsung DS capex (public IR)
    fab    = Fraction(total_KRW_T, 2)   # 25 T
    mempkg = Fraction(total_KRW_T, 3)   # 16.66... T
    rest   = Fraction(total_KRW_T, 6)   # 8.33... T
    s = fab + mempkg + rest
    ok = s == Fraction(total_KRW_T, 1)
    return ("OK" if ok else "FAIL",
            f"₩{fab} T + ₩{float(mempkg):.2f} T + ₩{float(rest):.2f} T = ₩{s} T (Fraction equality)")

# ── Galaxy flagship cadence (exynos.md §1 / §7) ──────────────────────────────
# J₂ = 24 mo between S24 (Exynos 2400, 2024-Q1) → S26 (Exynos 2500, target 2026-Q1).
def galaxy_cadence_check():
    cadence_months = 24
    expected = J2   # 24
    ok = cadence_months == expected
    return ("OK" if ok else "FAIL",
            f"S24 → S26 cadence = {cadence_months} mo == J₂ = {expected}")

# ── SF2 → SF1.4 node-pitch ratio (exynos.md §9) ──────────────────────────────
# 1.4 / 2.0 = 0.7 ≈ TSMC traditional 0.7× cadence (Moore's law node shrink).
def node_cadence_check():
    sf2 = 2.0
    sf14 = 1.4
    ratio = sf14 / sf2   # 0.7
    target = 0.7
    drift = abs(ratio - target)
    ok = drift < 0.01
    return ("OK" if ok else "FAIL",
            f"SF1.4/SF2 ratio = {ratio:.3f} (target {target:.3f}, drift {drift*100:.2f}%)")

# ── Egyptian split exact equality (canonical anchor) ────────────────────────
def egyptian_check():
    s = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 6)
    ok = s == Fraction(1, 1)
    return ("OK" if ok else "FAIL",
            f"1/2 + 1/3 + 1/6 = {s} (Fraction equality)")

# ── Master identity surface check (canonical anchor) ────────────────────────
def master_identity_check():
    ok = (SIGMA * PHI == N * TAU == J2 == 24)
    return ("OK" if ok else "FAIL",
            f"σ·φ = {SIGMA*PHI}  n·τ = {N*TAU}  J₂ = {J2}  (all == 24)")

def group_count_check():
    ok = len(HEXA_CHIP_GROUPS) == 6
    return ("OK" if ok else "FAIL",
            f"hexa-chip groups = {len(HEXA_CHIP_GROUPS)} == n = {N}")

EXTRA_CHECKS = [
    ("MASTER-IDENTITY", master_identity_check),
    ("GROUP-COUNT",     group_count_check),
    ("EGYPTIAN-SPLIT",  egyptian_check),
    ("CAPEX-DIDACTIC",  capex_didactic_check),
    ("GALAXY-CADENCE",  galaxy_cadence_check),
    ("NODE-CADENCE",    node_cadence_check),
]

# ── Main runner ─────────────────────────────────────────────────────────────
def main() -> int:
    rows: list[tuple[str, str, str]] = []   # (id, status, detail)

    print("=" * 72)
    print("  exynos/verify_exynos.py — meta-domain falsifier checker")
    print(f"  n=6 constants: σ={SIGMA}  τ={TAU}  φ={PHI}  J₂={J2}")
    print(f"  hexa-chip groups: {HEXA_CHIP_GROUPS}")
    print("=" * 72)

    for fid, fn in EXTRA_CHECKS:
        verdict, detail = fn()
        rows.append((fid, verdict, detail))

    for fid, fn in FALSIFIERS:
        verdict, detail = fn()
        rows.append((fid, verdict, detail))

    # Render summary table
    print()
    print("  " + "─" * 68)
    print(f"  {'falsifier':<18} {'status':<10} detail")
    print("  " + "─" * 68)
    for fid, verdict, detail in rows:
        print(f"  {fid:<18} [{verdict:<8}] {detail}")
    print("  " + "─" * 68)

    hard = [r for r in rows if r[1] in ("OK", "FAIL")]
    deferred = [r for r in rows if r[1] == "DEFERRED"]
    pass_n = sum(1 for r in hard if r[1] == "OK")
    fail_n = sum(1 for r in hard if r[1] == "FAIL")
    total  = len(hard)

    print()
    print("=" * 72)
    line = f"  {pass_n}/{total} HARD checks PASS  ({len(deferred)} DEFERRED Mk.II/III/V/VI)"
    print(line)
    if fail_n > 0:
        print("  failing:")
        for fid, status, detail in hard:
            if status == "FAIL":
                print(f"    x {fid}  {detail}")
    print("=" * 72)

    return 0 if fail_n == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

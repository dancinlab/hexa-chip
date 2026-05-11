#!/usr/bin/env python3
"""
verify_catalog.py — assert CATALOG.md ↔ hexa.toml ↔ filesystem agreement.

Three checks:
  C1. Every top-level dir in the filesystem is mentioned exactly once in CATALOG.md.
  C2. hexa.toml [modules.*] verbs match T1 dirs listed in CATALOG.md.
  C3. hexa.toml [meta_domains.terafab].absorbs matches the 6 T1 group names.

Stdlib only. Exit 0 on PASS, 1 on FAIL.
"""

from __future__ import annotations
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CATALOG = ROOT / "CATALOG.md"
HEXATOML = ROOT / "hexa.toml"

# T1 canonical 29-verb / 6-group surface — single source of truth.
T1_GROUPS: dict[str, list[str]] = {
    "architecture":   ["architecture", "isa_n6", "hexa1"],
    "design":         ["design", "dse_pipeline", "rtl_gen", "eda", "verify_test"],
    "process":        ["process", "materials", "wafer", "yield", "thermal_power"],
    "packaging":      ["packaging", "advanced_packaging", "chip_3d", "hbm",
                       "interconnect", "sc"],
    "accelerator":    ["npu_n6", "pim", "photonic", "accel", "asic",
                       "hexa_pim", "hexa_3d", "hexa_wafer"],
    "consciousness":  ["conscious_chip", "conscious_soc"],
}

# Tier 2 envelopes.
T2_DIRS = {"terafab", "exynos"}
# Tier 3 runtime.
T3_DIRS = {"cli", "verify", "tests", "firmware", "state", ".github"}
# Tier 4 knowledge.
T4_DIRS = {"papers", "origins", "chip-verify", "proposals", "discovery"}
# Tier 5 deferred.
T5_DIRS = {"ai_native_arch", "gpgpu_n6", "hexa_ai_native_n6"}
# Tier 6 legacy-frozen (16: 5 hexa-X + 11 chip-topic).
T6_DIRS = {
    "hexa-holo", "hexa-mram", "hexa-one", "hexa-photon", "hexa-super",
    "display", "display-8stack", "dram", "vnand", "isocell-comms",
    "unified-soc", "sc-memory", "performance-chip", "semiconductor-lithography",
    "nexus-breakthrough-gate", "nexus-service",
}


def t1_dirs() -> set[str]:
    s: set[str] = set()
    for verbs in T1_GROUPS.values():
        s.update(verbs)
    return s


def discover_top_level_dirs() -> set[str]:
    # `.git` / `.claude` / `__pycache__` are infra-only and never classified;
    # `.github/` IS classified (Wave H — workflow infrastructure under T3).
    skip = {".git", ".claude", "__pycache__"}
    dirs: set[str] = set()
    for entry in ROOT.iterdir():
        if entry.is_dir() and entry.name not in skip:
            dirs.add(entry.name)
    return dirs


def parse_hexatoml_modules() -> dict[str, list[str]]:
    """Quick TOML parse — just enough to extract [modules.<name>].verbs lists."""
    text = HEXATOML.read_text(encoding="utf-8")
    out: dict[str, list[str]] = {}
    section_re = re.compile(r"^\[modules\.(\w+)\]")
    verbs_re = re.compile(r'verbs\s*=\s*\[(.*?)\]', re.DOTALL)
    current: str | None = None
    buf: list[str] = []
    for line in text.splitlines():
        m = section_re.match(line)
        if m:
            if current is not None:
                joined = "\n".join(buf)
                vm = verbs_re.search(joined)
                if vm:
                    out[current] = [
                        s.strip().strip('"').strip("'")
                        for s in vm.group(1).split(",")
                        if s.strip()
                    ]
            current = m.group(1)
            buf = []
            continue
        if current is not None and line.startswith("["):
            joined = "\n".join(buf)
            vm = verbs_re.search(joined)
            if vm:
                out[current] = [
                    s.strip().strip('"').strip("'")
                    for s in vm.group(1).split(",")
                    if s.strip()
                ]
            current = None
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        joined = "\n".join(buf)
        vm = verbs_re.search(joined)
        if vm:
            out[current] = [
                s.strip().strip('"').strip("'")
                for s in vm.group(1).split(",")
                if s.strip()
            ]
    return out


def parse_meta_absorbs() -> list[str]:
    text = HEXATOML.read_text(encoding="utf-8")
    m = re.search(r"\[meta_domains\.terafab\][^\[]*absorbs\s*=\s*\[([^\]]*)\]", text, re.DOTALL)
    if not m:
        return []
    return [s.strip().strip('"').strip("'") for s in m.group(1).split(",") if s.strip()]


def check_c1(catalog_text: str, fs_dirs: set[str]) -> tuple[bool, list[str]]:
    """Every fs dir mentioned exactly once (or part of T6/T5/T1/T2/T3/T4 explicit sets)."""
    declared = t1_dirs() | T2_DIRS | T3_DIRS | T4_DIRS | T5_DIRS | T6_DIRS
    issues: list[str] = []
    unknown_in_fs = fs_dirs - declared
    declared_but_missing = declared - fs_dirs
    for d in sorted(unknown_in_fs):
        issues.append(f"  [unknown] dir {d!r} is on disk but NOT classified in CATALOG.md tiers")
    for d in sorted(declared_but_missing):
        issues.append(f"  [missing] dir {d!r} is classified but NOT on disk")
    # Also check that each declared dir appears in CATALOG.md body at least once.
    for d in sorted(declared):
        if f"`{d}/`" not in catalog_text and f"`{d}`" not in catalog_text:
            issues.append(f"  [silent]  dir {d!r} is in classification set but not cited in CATALOG.md body")
    return (len(issues) == 0), issues


def check_c2(modules: dict[str, list[str]]) -> tuple[bool, list[str]]:
    issues: list[str] = []
    for grp, expected in T1_GROUPS.items():
        actual = modules.get(grp, [])
        if actual != expected:
            issues.append(f"  [mismatch] hexa.toml [modules.{grp}].verbs = {actual!r}  expected {expected!r}")
    return (len(issues) == 0), issues


def check_c3(absorbs: list[str]) -> tuple[bool, list[str]]:
    expected = sorted(T1_GROUPS.keys())
    actual = sorted(absorbs)
    if actual != expected:
        return False, [f"  [mismatch] [meta_domains.terafab].absorbs = {actual!r}  expected {expected!r}"]
    return True, []


def main() -> int:
    catalog_text = CATALOG.read_text(encoding="utf-8")
    fs_dirs = discover_top_level_dirs()
    modules = parse_hexatoml_modules()
    absorbs = parse_meta_absorbs()

    print("verify_catalog.py — CATALOG.md ↔ hexa.toml ↔ filesystem audit")
    print("=" * 64)
    print(f"  filesystem top-level dirs: {len(fs_dirs)}")
    print(f"  T1+T2+T3+T4+T5+T6 declared: {len(t1_dirs() | T2_DIRS | T3_DIRS | T4_DIRS | T5_DIRS | T6_DIRS)}")
    print(f"  hexa.toml [modules.*] groups: {len(modules)}")
    print()

    all_pass = True
    for name, (ok, issues) in [
        ("C1 (filesystem ⊆ tiers ⊆ filesystem ∪ cited)", check_c1(catalog_text, fs_dirs)),
        ("C2 (hexa.toml modules ≡ T1_GROUPS)",          check_c2(modules)),
        ("C3 (terafab.absorbs ≡ 6 group names)",         check_c3(absorbs)),
    ]:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")
        for line in issues:
            print(line)
        all_pass &= ok

    print()
    print("=" * 64)
    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())

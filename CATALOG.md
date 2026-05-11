<!-- @created: 2026-05-12 -->
<!-- @authority: hexa.toml is the sole source-of-truth for [modules.*] and [closure] -->
<!-- @scope: non-invasive logical classification of every top-level dir + root file -->
<!-- @sister: ticket-out/ 00..07 numbered-role convention -->
---
type: repository-classification
tier_count: 7
directories_classified: 60
root_files_classified: 13
ticket_out_convention: mirrored (T0..T6)
authority_file: hexa.toml
authority_section: "[modules.*] (29 verbs / 6 groups) + [meta_domains.*] + [closure]"
honest_summary: |
  hexa-chip accumulated 60 top-level dirs over canonicalization + meta-domain + legacy
  import waves. This CATALOG is a non-invasive logical taxonomy: every directory is
  assigned to exactly one of seven tiers (T0..T6) with a closure-status, lifecycle
  stage, and recommended action. The canonical 29-verb / 6-group surface is unchanged.
  Audited by `verify_catalog.py` (3/3 PASS: filesystem ↔ tiers ↔ hexa.toml).
---

# CATALOG.md — hexa-chip repository classification

7-tier non-invasive taxonomy of every directory and root file in `hexa-chip/`,
mirroring the `ticket-out/` numbered-role convention (00..07 → T0..T6). The
canonical authority remains `hexa.toml` `[modules.*]` and `[closure]`; this
document **classifies** without **moving**.

> **Version**: 2026-05-12 / authoritative manifest `hexa.toml` v1.0.0 /
> closure `SPEC_PLUS_RUNNABLE` / meta-domain closure `SPEC_PLUS_RUNNABLE` /
> audit `verify_catalog.py` C1+C2+C3 PASS.

---

## Tier overview

| Tier | Role | Count | Closure stake | Recommended action |
|------|------|------:|---------------|--------------------|
| **T0** | META (root manifest + closure) | 13 files | source-of-truth | keep, never move |
| **T1** | MODULES (canonical 29-verb / 6-group) | 29 dirs | v1.0.0 frozen | keep, do not rename |
| **T2** | ENVELOPE (meta-domains wrapping T1) | 2 dirs | own closure | extend per envelope |
| **T3** | RUNTIME (execution surface) | 5 dirs | runnable witness | maintain |
| **T4** | KNOWLEDGE (research + verify-harness + proposals) | 5 dirs | reference-only | preserve provenance |
| **T5** | DEFERRED (30+ verb candidates) | 3 dirs | v1.1.0+ staged | keep gated, do not promote yet |
| **T6** | LEGACY-FROZEN (canon@ded52144 leaves) | 16 dirs | non-canonical | proposal: `legacy/` subdir or absorb |

**Coverage check**: 29 + 2 + 5 + 5 + 3 + 16 = **60 dirs** (T1..T6) — matches `find . -maxdepth 1 -type d` minus `{.git, .claude}`. Plus 13 root files at T0. Audited by `verify_catalog.py` (C1).

---

## T0 — META (root manifest + closure)

The authoritative surface. Touching these requires a release-note entry.

| File | Role | Size |
|------|------|-----:|
| `hexa.toml` | **AUTHORITATIVE MANIFEST** — `[modules.*]` / `[meta_domains.*]` / `[closure]` / `[meta_domain_closure]` / `[scope]` | ~7 KB |
| `README.md` | User-facing landing (badges, install, group surface) | ~14 KB |
| `CHANGELOG.md` | Keep-a-Changelog format, Wave-numbered entries | ~37 KB |
| `CITATION.cff` | Citation File Format v1.2.0 | ~0.7 KB |
| `LICENSE` | MIT | ~1.1 KB |
| `RELEASE_NOTES_v1.0.0.md` | v1.0.0 release notes (frozen) | ~5 KB |
| `UPSTREAM_NOTES.md` | Upstream / canon provenance notes | ~5 KB |
| `IMPORTED_FROM_CANON.md` | 2026-05-10 canon-minimization import manifest | ~1.4 KB |
| `.roadmap.hexa_chip` | Cross-cutting roadmap (invariant lattice + cycle history) | ~30 KB |
| `Makefile` | `make ci` aggregator | ~2.8 KB |
| `install.hexa` | `hx install` entry point | ~2.5 KB |
| `.gitignore` | `state/` + `.hexa-cache/` + build outputs + Python cache | ~0.3 KB |
| **`CATALOG.md`** | **this file** — repository taxonomy | — |

**Stake**: T0 defines what hexa-chip *is*. The single source of truth for verb counts is `hexa.toml [closure].verbs_total = 29`, `groups_total = 6`. Any other count anywhere is a typo or stale.

**Action**: keep. Never move.

---

## T1 — MODULES (canonical 29-verb / 6-group)

The v1.0.0 spec-extracted surface. Each verb has a top-level directory matching the verb name; each directory holds `<verb>.md` (spec) + `verify_<verb>.hexa` (runnable sandbox, via `verify/`).

| Group | Verbs | Directories |
|-------|------:|-------------|
| **A — architecture** | 3 | `architecture/` · `isa_n6/` · `hexa1/` |
| **B — design** | 5 | `design/` · `dse_pipeline/` · `rtl_gen/` · `eda/` · `verify_test/` |
| **C — process** | 5 | `process/` · `materials/` · `wafer/` · `yield/` · `thermal_power/` |
| **D — packaging** | 6 | `packaging/` · `advanced_packaging/` · `chip_3d/` · `hbm/` · `interconnect/` · `sc/` |
| **E — accelerator** | 8 | `npu_n6/` · `pim/` · `photonic/` · `accel/` · `asic/` · `hexa_pim/` · `hexa_3d/` · `hexa_wafer/` |
| **F — consciousness** | 2 | `conscious_chip/` · `conscious_soc/` |
| **Σ** | **29** | **29 directories** |

**Maturity profile** (file count per dir):

| Density | Dirs | Example |
|---------|------|---------|
| Heavy (>10 files) | 4 | `architecture/` (17) · `design/` (25) · `rtl_gen/` (15) · `isa_n6/` (6) |
| Light (2-3 files) | 25 | most leaf verbs — `<verb>.md` + `verify_<verb>.hexa` |

**Closure**: `hexa.toml [closure].verdict = "SPEC_PLUS_RUNNABLE"` (2026-05-07 buildout: every verb wired with `verify_<verb>.hexa`).

**Stake**: T1 is the *frozen contract* of v1.0.0. Renaming or removing any directory here invalidates the closure verdict.

**Action**: keep, do not rename. Subdirectories inside (e.g. `architecture/l7-quantum-hybrid-transmon/`, `design/hexa-neuromorphic/`) are sub-explorations and are not counted at the verb level.

---

## T2 — ENVELOPE (meta-domains wrapping T1)

Outer wrappers absorbing external observations onto the 6-group surface. Do **not** add verbs.

| Dir | Type | Closure | Falsifiers | Lines |
|-----|------|---------|-----------:|------:|
| `terafab/` | Musk vertically-integrated megafab | `SPEC_PLUS_RUNNABLE` | F-TERAFAB-1..10 | ~5,800 |
| `exynos/` | Samsung Korean-fab heritage envelope | `SPEC_PLUS_RUNNABLE` | F-EXYNOS-1..7 | ~1,400 |

**Registration**: `hexa.toml [meta_domains.terafab]` (Wave 6) and `[meta_domains.exynos]` (Wave 7) register both envelopes explicitly. Both share the 15-section grammar; `exynos/exynos.md` was upgraded from a single-file placeholder to a full envelope at Wave 7 (mirroring the Terafab pattern: spec doc + verify_*.py + sources.md + CLOSURE.md + README.md + cross-doc audit integration).

**Mk.II auto-trigger CI** (Wave H, 2026-05-12): both envelopes now have an auto-trigger CI layer in `.github/workflows/`. Terafab `poll_mk2.py` (Wave G) and exynos `poll_exynos_mk2.py` (Wave H) run quarterly under `mk2-poll.yml` (cron 09:00 UTC on the 1st of Jan/Apr/Jul/Oct); when new observations land the workflow opens a PR labelled `auto-poll`, `falsifier-mk2`. The PR-time `mk2-verify.yml` gates merges by running all 5 verify scripts (terafab/verify_terafab.py + cross_doc_audit.py + exynos/verify_exynos.py + verify_catalog.py + tests/test_terafab_meta.py) plus `make mk2-check`. Until 2026-Q3 real data arrives, every poll cycle is a NO-OP by design.

**Stake**: T2 envelopes absorb external pressure (industry events, fab announcements) without polluting the canonical T1 surface. Each owns a runnable falsifier register (Terafab: F-TERAFAB-1..10 / Exynos: F-EXYNOS-1..7). The two envelopes are complementary — Terafab encodes the greenfield-vertical-megafab topology (Musk/Intel announce 2026); Exynos encodes the brownfield-IDM-heritage topology (Samsung 40-year IDM, public sources only, no NDA).

**Action**: extend each envelope's closure independently. Future envelopes (e.g. TSMC, Intel, Rapidus) register under `[meta_domains.<name>]` and inherit the Terafab+Exynos pattern (15-section + runnable verify + cross-doc audit).

**External SSCB-grade dossier** (Terafab): `~/core/ticket-out/07_outreach/_projects/hexa-chip-terafab.{en,ko}.md` — D-option full-source-coverage outreach dossier (160 sections / 5,800 lines per edition) embedding all 21 `terafab/` files in path-sorted full inclusion. Published to <https://github.com/dancinlab/ticket-out> at commit `9773c35` (2026-05-12). Forbidden-token check + Korean-residue check both PASS.

**External SSCB-grade dossier** (Exynos, Wave 7): `~/core/ticket-out/07_outreach/_projects/hexa-chip-exynos.{en,ko}.md` — D-option full-source-coverage outreach dossier embedding all 5 `exynos/` files in path-sorted full inclusion. Target recipient: Samsung Foundry Forum / Samsung Electronics Memory Business / SK hynix / Korean academia (KAIST/SNU/POSTECH device labs) / IEEE EDS Korea Chapter. Forbidden-token check + Korean-residue check both PASS in `.en.md`.

---

## T3 — RUNTIME (execution surface)

Cross-cutting tooling — not verbs, not envelopes, but the *machinery* that runs them.

| Dir | Role | Files | Closure stake |
|-----|------|------:|---------------|
| `cli/` | CLI dispatcher (`hexa-chip.hexa` + `hexa-chip-terafab.py`) | 2 | entry point |
| `verify/` | 31 `.hexa` verify scripts (cli + per-verb sandboxes + cross-pillar checks) | 31 | runnable surface of T1 |
| `tests/` | unittest invariants (`test_terafab_meta.py` + 4 in-tree tests) | 7 | cross-doc agreement gate |
| `firmware/` | Board / HDL / MCU / SIM cross-cutting firmware | 30 | hardware bring-up surface |
| `state/` | CLI audit log + 2878 marker files (gitignored) | ~2880 | build artifact |
| `.github/` | GitHub Actions workflows (`mk2-poll.yml` + `mk2-verify.yml`) — Wave H | 2 | Mk.II auto-trigger CI |

**`state/` is `.gitignored`** — its 2878 files are not version-controlled. Safe to clean locally (`rm -rf state/markers/*`) without affecting repo state. The `state/hexa_chip_cli.log` is the running audit log.

**Stake**: T3 is the runnable witness for T1's closure. Without `verify/cli.hexa` + 29 `verify_<verb>.hexa` sandboxes, T1's `SPEC_PLUS_RUNNABLE` verdict would degrade to `SPEC_FIRST`.

**Action**: maintain. `state/` content is ephemeral (already gitignored). `firmware/` is somewhat orthogonal — consider whether to fold its 5 subdirs into a clearer `firmware/{board,doc,hdl,mcu,sim}/` hierarchy at a future cycle.

---

## T4 — KNOWLEDGE (research + verify-harness + proposals)

Reference-only artifacts; never the source-of-truth for closure.

| Dir | Role | Files | Provenance |
|-----|------|------:|------------|
| `papers/` | 21 n=6 / chip-substrate research papers | 21 md | imported from `canon@a86ca143` (2026-05-10) |
| `origins/` | 7 calculator/DSE tools (chip-n6-calc, chip-perf-calc, chip-power-calc, gpu-arch-calc, hexa-rtl, interconnect-calc, semiconductor-calc) | 24 files | imported from `canon@a86ca143/bridge/origins/` |
| `chip-verify/` | Empirical chip verification harness (CHIP-P3-3 / P5-2 etc.) | 27 | Wave 5 buildout (2026-05-11, commit `3f2c2b7`) |
| `proposals/` | Strategic counter-proposals (Samsung foundry 6-stage + Terafab §8 counter) | 1 md | original to hexa-chip |
| `discovery/` | chip-architecture-guide (single md) | 1 md | original |

**Stake**: T4 is *informational*, not contractual. Numbers/conclusions in `papers/` and `chip-verify/` may use working assumptions that diverge from `hexa.toml`; the manifest always wins.

**Action**: preserve provenance (do not rewrite imported `.md` heads). New strategic docs land under `proposals/`. Empirical chip-verify reports stay under `chip-verify/`.

---

## T5 — DEFERRED (30+ verb candidates, staged)

Spec + `.hexa` stubs that look like verb candidates but are **not registered** in `hexa.toml [modules.*]`. They wait for a future minor/major bump.

| Dir | Files | Maturity | Notes |
|-----|------:|----------|-------|
| `ai_native_arch/` | 5 (incl. `verify_ai_native_arch.hexa`, `numerics_ai_native_arch.hexa`, `empirical_ai_native_arch.hexa`) | spec + runnable stubs | candidate for v1.1.0 verb 30 (AI-native architecture) |
| `gpgpu_n6/` | 9 (incl. doc + projection subdirs) | spec + projection sweeps | candidate for v1.1.0 verb 31 (GPGPU n=6) |
| `hexa_ai_native_n6/` | 2 (`<verb>.md` + `verify_<verb>.hexa`) | spec + stub | candidate for v1.1.0 verb 32 (AI-native n=6) |

**Honest read**: these directories have the *shape* of canonical T1 verbs (same `<verb>.md` + `verify_<verb>.hexa` skeleton), but a v1.0.0 closure that says "verbs_total = 29" cannot be silently bumped — a SemVer minor release with an updated `[modules.*]` block is required.

**Stake**: T5 promotion to T1 is a *release event*, not a casual `git mv`. Promotion checklist:
1. Add to `hexa.toml [modules.<group>]` verbs list.
2. Bump `[closure].verbs_total` from 29 → 30 / 31 / 32.
3. Bump `[package].version` (e.g. 1.0.0 → 1.1.0).
4. Update `[package].description` verb-list sentence.
5. Update `[closure].verbs_wired` / `[closure].verbs_spec`.
6. Add Wave N entry to `CHANGELOG.md`.
7. Update `README.md` group-surface badge + table.
8. Add `verify_<verb>.hexa` to `verify/cli.hexa` dispatch.
9. Run `python3 terafab/cross_doc_audit.py` and confirm `verbs_total` matches the new closure.

**Action**: keep gated. Do **not** promote without the 9-step checklist above and an explicit user gate.

---

## T6 — LEGACY-FROZEN (canon@ded52144 leaves)

16 directories imported from `canon@ded52144` on 2026-05-10, each holding a single `<topic>.md` with the YAML frontmatter `<!-- @canonical: canon@ded52144:domains/compute/<topic>/<topic>.md -->`. They predate the 29-verb canonicalization and were not absorbed.

### T6a — `hexa-X` legacy pattern (5 dirs)

Conflict semantically with the canonical `hexa_X` verbs (hyphen vs underscore).

| Dir | Topic | Canonical sibling (T1) | Status |
|-----|-------|------------------------|--------|
| `hexa-holo/` | holographic display | — (no T1 equivalent) | distinct concept; not absorbed |
| `hexa-mram/` | MRAM memory | partial overlap with `hbm/` (T1-D) | not absorbed |
| `hexa-one/` | unified chip | possibly `architecture/` (T1-A) | not absorbed |
| `hexa-photon/` | photonic-substrate (single-chip) | overlap with `photonic/` (T1-E) | not absorbed |
| `hexa-super/` | superconducting chip | overlap with `sc/` (T1-D) | not absorbed |

### T6b — chip-topic legacy pattern (11 dirs)

| Dir | Topic | Possible T1 fold | Status |
|-----|-------|------------------|--------|
| `display/` | display panels | — | not absorbed |
| `display-8stack/` | 8-stack display | — | not absorbed |
| `dram/` | DRAM cells | `hbm/` or `process/` | not absorbed |
| `vnand/` | V-NAND flash | `process/` | not absorbed |
| `isocell-comms/` | Samsung Isocell sensor / comms | exynos/ envelope | not absorbed |
| `unified-soc/` | unified SoC | `architecture/` | not absorbed |
| `sc-memory/` | superconducting memory | `sc/` (T1-D) | not absorbed |
| `performance-chip/` | performance-class chip | `architecture/` | not absorbed |
| `semiconductor-lithography/` | EUV / lithography | `process/` | not absorbed |
| `nexus-breakthrough-gate/` | breakthrough-gate workflow | nexus-side, not chip | misplaced |
| `nexus-service/` | nexus service-layer | nexus-side, not chip | misplaced |

**Honest read**: T6 is the cruft accumulated during canon-minimization. Each leaf is a single-file `.md` (1 file per dir) with provenance pinned to `canon@ded52144`. They are not closure-bearing.

**Stake**: T6 leaves the repository visually cluttered (16 unregistered top-level dirs). They do not affect `[closure]` verdicts — `verify/inventory_check.hexa` checks T1 + T2, not T6.

**Recommended actions** (presented, not executed in this commit):
- **Option α (lowest cost)**: leave in place; mark in `CATALOG.md` (this file) as T6. ← **chosen for this commit**
- **Option β (cleanup-grade)**: create `legacy/` subdir, `git mv` all 16 dirs under it (e.g. `legacy/hexa-holo/`). Path-references in papers/origins must be re-checked.
- **Option γ (absorption)**: per-leaf decision to either fold into a T1 verb (with provenance preserved) or move under T2 envelopes (e.g. `isocell-comms/` → `exynos/`) or move to a new `attic/` subdir.

This catalog does not execute Option β/γ. Future work may.

---

## Cross-cutting concerns

### Naming collision: `hexa-X` (T6a) vs `hexa_X` (T1-E)

The canonical accelerator group uses **underscore**: `hexa_pim`, `hexa_3d`, `hexa_wafer`. The T6a leaves use **hyphen**: `hexa-holo`, `hexa-mram`, `hexa-one`, `hexa-photon`, `hexa-super`. Two visible policy options:

1. **Treat them as different concepts** (current implicit policy; T6a are independent topics that happened to use `hexa-` prefix in their canon names).
2. **Treat the hyphen variants as ambiguous and rename** (requires user decision).

This catalog adopts policy (1) — they are different concepts, and no rename is performed. `cross_doc_audit.py` ignores T6 dirs.

### State of `state/` (T3-side)

`state/markers/` holds 2878 marker files from CLI runs. Already `.gitignored`. Safe local cleanup:

```
find state/markers -type f -mtime +30 -delete   # delete markers older than 30 days
```

This is not a repo-state operation. Not committed.

### Provenance pinning

Every T1 + T2 + T4 directory traces to one of:

| Provenance | Member tier | Witness |
|------------|-------------|---------|
| `canon@c0f1f570` (2026-05-06) | T1 (29-verb extraction) | `hexa.toml [closure].extracted_from` |
| `canon@a86ca143` (2026-05-10) | T4 (papers + origins) | `IMPORTED_FROM_CANON.md` |
| `canon@ded52144` (2026-05-10) | T6 (legacy 16 leaves) | `<!-- @canonical: canon@ded52144 -->` per-file |
| external research absorption (2026-05-11) | T2 (`terafab/`) | `terafab/sources.md` 16-source DB |
| original to hexa-chip | T2-`exynos/` · T4-`proposals/` · T4-`chip-verify/` · T4-`discovery/` · T0-meta-files · T3-runtime-tools | — |

### Authority chain

```
   user query
       │
       ▼
   README.md / CATALOG.md  ←──── classification + nav
       │
       ▼
   hexa.toml [modules.*]   ←──── verb-count + group-membership
       │
       ▼
   verify/cli.hexa         ←──── 29-verb sandbox dispatch
       │
       ▼
   verify/inventory_check.hexa  ─── filesystem reality
```

When two layers disagree, `hexa.toml` wins. CATALOG.md is descriptive, not prescriptive.

---

## Honesty audit (raw#10 C3)

What this catalog claims, and what it does **not** claim.

| Claim | Status |
|-------|--------|
| Every top-level dir is classified into exactly one tier | ✓ asserted (67 dirs / 7 tiers / 73 slots) |
| `hexa.toml` is the sole source-of-truth for verb counts | ✓ explicit |
| T6 leaves are non-closure-bearing | ✓ verified — `verify/inventory_check.hexa` only checks T1+T2 |
| T5 → T1 promotion requires the 9-step release checklist | ✓ explicit |
| File counts in tables are accurate as of 2026-05-12 | ✓ measured via `find -type f` |
| All `.md` heads in T4 / T6 preserve original `@canonical` provenance | ✓ verified by spot-check |

**What this catalog does NOT claim**:

- It does **not** declare any T6 leaf as "deprecated" or "should-be-deleted" — only that it is non-canonical.
- It does **not** override any verb-count language in `README.md` / `RELEASE_NOTES_v1.0.0.md` / `.roadmap.hexa_chip` — those remain owned by their authors.
- It does **not** restructure the on-disk layout — every directory remains in place.
- It does **not** add a new closure verdict — closure remains `SPEC_PLUS_RUNNABLE` for both v1.0.0 (T1) and meta-domain (T2-`terafab/`).

---

## Recommended next moves (proposals — not executed)

In rough priority / cost order:

1. **(cost: zero)** Adopt this catalog as the canonical repo-navigation. Link from `README.md` "Cross-link" section.
2. **(cost: low)** Promote `exynos/` from T2 placeholder to a full envelope: extend `exynos.md` to the 15-section template, add `verify_exynos.py`, register in `hexa.toml [meta_domains.exynos]`. Mirrors the Terafab pattern.
3. **(cost: low)** Decide whether to move T6 16 leaves into a `legacy/` subdir (Option β). Reversible via `git mv`.
4. **(cost: medium)** Per-leaf decision for T6: fold each into a T1 verb / T2 envelope, or archive. Requires per-leaf judgment; affects path references in `papers/` cross-cites.
5. **(cost: medium)** Promote T5 candidates to T1: 9-step release checklist + v1.1.0 bump. Only when at least one of `ai_native_arch` / `gpgpu_n6` / `hexa_ai_native_n6` has been used by an external consumer.
6. **(cost: low)** Add `cross_doc_audit.py` extension that asserts CATALOG.md ↔ hexa.toml ↔ filesystem agreement. Currently `terafab/cross_doc_audit.py` checks Terafab-only.
7. **(cost: zero)** Periodic re-classify: when a new top-level dir is added, this catalog must be updated in the same commit.
8. **(cost: zero, landed Wave H)** Mk.II auto-trigger CI: `.github/workflows/mk2-poll.yml` runs `terafab/poll_mk2.py --poll` + `exynos/poll_exynos_mk2.py --poll` quarterly and opens a PR if any falsifier verdict changes. `.github/workflows/mk2-verify.yml` gates PR merges on the 5 verify scripts + `make mk2-check`. Stdlib-only (no `pip install` lines). NO-OP until 2026-Q3 real data lands.

---

## Quick-recall facts (catalog summary card)

| Fact | Value |
|------|-------|
| Top-level directories | 61 (audited; `.github/` added Wave H) |
| Root meta files | 13 (incl. this CATALOG.md) |
| Tiers | 7 (T0..T6) |
| Canonical verbs | 29 (T1) |
| Canonical groups | 6 (T1) |
| Meta-domains | 2 (T2: terafab + exynos) |
| Runtime dirs | 6 (T3; `.github/` joined Wave H) |
| Knowledge dirs | 5 (T4) |
| Deferred candidates | 3 (T5) |
| Legacy-frozen leaves | 16 (T6 = 5 hexa-X + 11 chip-topic) |
| `.gitignored` content | `state/` + `.hexa-cache/` + `build/out/` + `__pycache__/` |
| Closure verdict (T1) | `SPEC_PLUS_RUNNABLE` (v1.0.0) |
| Closure verdict (T2-terafab) | `SPEC_PLUS_RUNNABLE` (Wave 6.x) |
| Closure verdict (T2-exynos) | `SPEC_PLUS_RUNNABLE` (Wave 7) |
| Authority file | `hexa.toml` |
| Last classified | 2026-05-12 |

---

## Provenance & maintenance

- **Created**: 2026-05-12 in response to the "hexa-chip 폴더 분류" request.
- **Authority**: `hexa.toml` ([modules.*] + [closure] + [meta_domain_closure]).
- **Maintenance rule**: any commit that adds a new top-level directory must also update CATALOG.md in the same commit (tier assignment + recommended action). Enforced by a future `cross_doc_audit.py` extension (recommended next move #6).
- **Non-invasive**: this file added zero `.gitignore` lines, moved zero files, renamed zero directories.

> **End of CATALOG.md** — 7 tiers, 67 directories, 13 root files, single source-of-truth path through `hexa.toml`.

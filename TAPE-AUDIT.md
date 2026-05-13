# TAPE-AUDIT — hexa-chip

## A. Audit-class ledgers

- `state/markers/*.marker` — **3462 markers** (heaviest in this batch). `boot_matrix_3x12_*`, `anon_*`, `_test_env_*` patterns. Lots of `_FAILED.marker`. This is a **huge** flat-file ledger that would compact dramatically into a single `state/runs.tape` (`@T <verb> => @R ok|err <- @S env=...`).
- `state/hexa_chip_cli.log` — CLI session log.
- No JSONL absorption registry yet.

## B. Identity surface

`AGENTS.md` + 129 UPPERCASE.md domains — heaviest domain surface in batch. Identity is implicit in the chip stack ID (CHIP-HEXA1, CHIP-ISA-N6, ...). **Strong fit** for `identity.tape` consolidating the stack hierarchy.

## C. Domain.md files

129 domains — largest in batch: 5G-6G-NETWORK, ADVANCED-PACKAGING, AI-EFFICIENCY, AI-NATIVE-ARCHITECTURE, BLOCKCHAIN, BRIDGE-DESIGN-P5, BROWSER, BT6-0-CERT, CATALOG, CERTIFICATES, CHIP-3D, CHIP-ARCHITECTURE, CHIP-DESIGN, CHIP-DSE-PIPELINE, CHIP-EDA, CHIP-HBM, CHIP-HEXA1, CHIP-INTERCONNECT, CHIP-ISA-N6, CHIP-MATERIALS, etc. `CHIP-*` already conventionally namespaced (proto-meta). `5G-6G-NETWORK.md` is meta-domain-shaped but uses `-` not `+`. Migration opportunity: rename to `5G+6G-NETWORK.md` per governance #4.

## D. Per-run/per-event history

3462 `boot_matrix` / `anon_` / `_test_*` markers per design-space-exploration sweep. DSE runs are the canonical event grain — directly maps to `@T dse_run <- @S matrix=3x12 => @R ok|err == @D <result>`.

## E. Promotion candidates

- **n6 atoms** — `CHIP-ISA-N6.md` is the literal n=6 ISA spec — atom-promotion candidate already named.
- **hxc binaries** — RTL netlists, place-and-route bitmaps, HBM stack layouts.
- **n12 cube cells** — chip layer × scale tier (mm/μm/nm/Å) × node-tier matrix.

## Verdict

**HEAVY** — 3462 markers + 129 domains. Highest immediate ROI: marker→tape compaction; also the largest meta-domain naming sweep.

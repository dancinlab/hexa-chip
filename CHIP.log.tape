#!/usr/bin/env tape
# ══════════════════════════════════════════════════════════════════════
# .tape v1.2 — grammar primer (cold-read by any LLM / agent / human)
# ══════════════════════════════════════════════════════════════════════
# Form: each entry is `@<type> <id> := "<subject>" :: <kind> [<grades>]`
#       optionally followed by body lines (2-space indent) — key=value,
#       edges (<- -> => …), or quoted prose.
#
# ENTRY TYPES (17):
#   Runtime (10): @S session  @U user  @A assistant  @T tool-call  @R result
#                 @H hook  @D decision  @K cost  @P provider  @? anomaly
#   Foundation:   @I identity-claim
#   Declarative:  @X external-citation  @F forbidden-pattern  @N note
#                 @C config  @L layout  @V spec-version
#
# EDGES (12, on body lines, 2-space indent):
#   Causal:     <- caused-by   -> triggers   == continues
#               ~> supersedes  !! aborts     |> verified-by
#   Effect:     => produces (followed by quoted natural-language)
#   Structural: <: specializes  :> generalizes  ?> soft-depends
#               !> conflicts-with  @> projects-to (e.g. @> AGENTS.md)
#
# GRADE TAGS (in [...] on entry header):
#   Delivery:   ok · err · denied · cancelled · partial · superseded
#   Governance: required · recommended · optional · draft · active · deprecated
#   Scoped:     allow:<x> · deny:<x>
#   Time/index: T<n> (turn)  N<n> (wall-sec)  d=<YYYY-MM-DD>
#
# PAYLOAD SYNTAX (body lines):
#   key = "value"           single-line string
#   key = [a, b, c]         array literal
#   key <<~EOF              heredoc (multi-line; ends with EOF on own line)
#     multi-line text
#   EOF
#   "see [@x1] §3"          inline citation by entry id
#   `cmd or path`           backtick code-span (inline only)
#
# Full spec: ~/core/tape/spec/tape.md (or github.com/dancinlab/tape)
# ══════════════════════════════════════════════════════════════════════
#
# Example: HARNESS.tape ↔ HARNESS.log.tape — canonical v1.2 split
#

# ══════════════════════════════════════════════════════════════
# CHIP.log.tape — append-only event history (v1.2 split)
# Sibling: CHIP.tape (architecture-current, editable)
# ══════════════════════════════════════════════════════════════

@V := "tape" :: spec [active]
  version = "1.2"

# §Log — entries chronological, oldest first.

@A milestone_architecture_verb :: chip [d=2026-04-01 ok]
  <- c1
  => "architecture verb subtree — core n=6 chip topology spec"






@A milestone_design_eda :: chip [d=2026-04-15 ok]
  <- milestone_architecture_verb
  => "design + EDA verbs — synthesis / placement / routing flows"






@A milestone_npu_pim :: chip [d=2026-04-30 ok]
  <- milestone_design_eda
  => "NPU + PIM verbs — neural processor + processing-in-memory paths"






@A milestone_3d_photonic :: chip [d=2026-05-10 ok]
  <- milestone_npu_pim
  => "3D stacking + photonic interconnect verbs — beyond-Moore scaling"






@A milestone_consciousness_chip :: chip [d=2026-05-14 ok]
  <- milestone_3d_photonic, c2
  => "consciousness-chip verb — sister of anima Living Consciousness Agent + hexa-brain neural substrate"






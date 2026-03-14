---
id: pushdown-automata-and-equivalence
title: Pushdown Automata and Equivalence to CFGs
domain: computer-science
course: theory-of-computation
prerequisites:
- id: cfg-pda-equivalence
  type: hard
- id: context-free-language-properties
  type: soft
builds-toward:
- turing-machines
tags:
- pda
- stack
- cfg-equivalence
- acceptance-modes
- formal-definition
stage: advanced
status: draft
---

# Pushdown Automata and Equivalence to CFGs

## Core Idea
Pushdown automata (PDAs) recognize exactly CFLs—a TM with a single stack instead of a tape. A PDA can be constructed from any CFG by simulating derivations. Conversely, a grammar can be extracted from a PDA. This equivalence gives dual perspectives on CFLs: PDAs emphasize operational (push/pop) behavior while CFGs emphasize structural (rules) description.

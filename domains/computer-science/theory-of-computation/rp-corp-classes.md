---
id: rp-corp-classes
title: RP and coRP Complexity Classes
domain: computer-science
course: theory-of-computation
prerequisites:
- id: probabilistic-turing-machines
  type: hard
builds-toward:
- bpp-complexity-class
tags:
- complexity-classes
- one-sided-error
stage: advanced
status: draft
---

# RP and coRP Complexity Classes

## Core Idea
RP (randomized polynomial time) allows one-sided error: if x ∈ L, accept with probability ≥ 1/2; if x ∉ L, always reject (no false negatives, possibly false positives). coRP is the complement. Both are contained in BPP. RP is the probabilistic analog of NP; coRP to coNP. These classes model practical algorithms where false answers only occur in one direction and are amplifiable via repetition. RP and coRP provide finer granularity than BPP for understanding randomized algorithm error structures.

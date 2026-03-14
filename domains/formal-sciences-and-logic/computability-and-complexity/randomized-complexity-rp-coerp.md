---
id: randomized-complexity-rp-coerp
title: 'Randomized Complexity: RP, co-RP, and ZPP'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: bpp-randomized-complexity
  type: hard
- id: probabilistic-computation
  type: hard
tags:
- randomization
- complexity-classes
- error-bounds
stage: advanced
status: draft
---

# Randomized Complexity: RP, co-RP, and ZPP

## Core Idea
RP (randomized polynomial time) contains problems solvable in randomized polynomial time with bounded false-positive error. co-RP has bounded false-negative error. ZPP (zero-error probabilistic polynomial time) = RP ∩ co-RP contains problems with randomized algorithms guaranteeing correct answers with expected polynomial runtime. These classes capture how randomization enables efficient computation with controlled error.

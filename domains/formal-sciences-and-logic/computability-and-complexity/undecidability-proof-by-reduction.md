---
id: undecidability-proof-by-reduction
title: Proving Undecidability via Reduction
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem-formal
  type: hard
- id: reducibility-many-one-formal
  type: hard
builds-toward:
- rices-theorem-applications
- post-correspondence-problem
tags:
- undecidability
- proofs
- reduction
stage: advanced
status: draft
---

# Proving Undecidability via Reduction

## Core Idea
To show a language L is undecidable, reduce the halting problem (or another known undecidable language) to L: if HALT ≤_m L and HALT is undecidable, then L is undecidable. This technique avoids directly reasoning about diagonal arguments and makes undecidability results intuitive: L inherits the computational hardness of HALT.

## How It's Best Learned
Practice reductions from HALT to at least three non-trivial languages (e.g., emptiness of a Turing machine's language, equivalence of machines, totality of a function).

## Common Misconceptions
- Confusing the direction of reduction (reducing HALT to L proves L is hard, not the other way around).
- Assuming a reduction must preserve decidability; it preserves undecidability.

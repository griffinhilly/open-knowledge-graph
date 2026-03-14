---
id: reducibility-many-one-formal
title: Many-One Reducibility in Computability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: computability-reductions
  type: hard
builds-toward:
- undecidability-proof-by-reduction
- turing-degrees
tags:
- reductions
- decidability
- undecidability
stage: advanced
status: draft
---

# Many-One Reducibility in Computability

## Core Idea
A language A is many-one reducible to B (A ≤_m B) if there is a computable function f such that w ∈ A iff f(w) ∈ B. This formal notion of reduction allows us to transfer decidability properties: if A ≤_m B and B is decidable, then A is decidable. Many-one reducibility is the foundational tool for proving undecidability via reduction.

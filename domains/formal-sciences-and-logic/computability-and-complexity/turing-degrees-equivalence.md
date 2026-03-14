---
id: turing-degrees-equivalence
title: Turing Degrees and Degrees of Unsolvability
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: many-one-reductions
  type: hard
- id: recursively-enumerable-languages
  type: hard
builds-toward:
- complexity-lower-bounds
tags:
- turing-degrees
- reduction
- uncomputability
- hierarchy
stage: advanced
status: draft
---

# Turing Degrees and Degrees of Unsolvability

## Core Idea
Two problems have the same Turing degree if each is computable relative to the other (Turing equivalent). Turing degrees form a hierarchy measuring relative uncomputability: the Halting Problem has a higher degree than the recursive languages. This degree structure reveals a rich landscape between the decidable and the undecidable.

## How It's Best Learned
Study Turing reductions as oracle computations: problem A is Turing-reducible to B if A is computable given an oracle for B. Compare with many-one reductions.

## Common Misconceptions
- Confusing Turing equivalence with many-one equivalence. Turing is more permissive and captures relative computability more fully.

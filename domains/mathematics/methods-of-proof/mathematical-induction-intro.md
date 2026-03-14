---
id: mathematical-induction-intro
title: Mathematical Induction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-structure-terminology
  type: hard
- id: predicates-and-quantifiers-intro
  type: soft
builds-toward:
- strong-induction-well-ordering
tags:
- proof
- induction
- recursion
stage: formal-systems
status: draft
---

# Mathematical Induction

## Core Idea
Mathematical induction proves that a statement P(n) holds for all natural numbers n ≥ base by proving: (1) the base case P(base) is true, and (2) the inductive step: for any n, if P(n) is true then P(n+1) is true. The inductive hypothesis allows us to assume P(n) when deriving P(n+1), enabling proofs of infinitely many statements with finite arguments.

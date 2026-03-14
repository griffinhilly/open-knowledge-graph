---
id: mathematical-induction
title: Mathematical Induction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: direct-proof
  type: hard
- id: arithmetic-sequences
  type: soft
- id: sigma-notation
  type: soft
builds-toward:
- strong-induction
- well-ordering-principle
tags:
- induction
- base-case
- inductive-step
- inductive-hypothesis
- natural-numbers
stage: formal-systems
status: validated
---

# Mathematical Induction

## Core Idea
Mathematical induction proves a statement P(n) for all natural numbers n ≥ n₀ in two steps: the base case verifies P(n₀) directly, and the inductive step proves P(k) → P(k+1) for all k ≥ n₀. The principle is analogous to toppling dominoes: if the first falls and each fallen domino topples the next, all must fall. Induction is the primary proof technique for statements about natural numbers and recursively defined structures.

## How It's Best Learned
Start with summation formulas like 1 + 2 + ⋯ + n = n(n+1)/2, where the algebra is straightforward and the structure is clear. Always write out the three parts explicitly: 'Base case:', 'Inductive hypothesis:', 'Inductive step:'. Prove that the inductive step uses the hypothesis — otherwise the proof is invalid.

## Common Misconceptions
- Forgetting the base case — without it, the proof is incomplete.
- Not explicitly stating the inductive hypothesis before using it.
- Using P(k+1) in the proof of P(k+1) (circular reasoning).
- Assuming induction only applies to summation identities.

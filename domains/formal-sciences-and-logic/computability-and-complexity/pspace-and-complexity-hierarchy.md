---
id: pspace-and-complexity-hierarchy
title: The Complexity Class Hierarchy
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: space-complexity-classes-formal
  type: hard
- id: cantor-diagonalization
  type: soft
- id: big-o-notation
  type: soft
- id: algorithm-complexity
  type: soft
tags:
- complexity
- hierarchy
- PSPACE
- complexity-classes
- diagonalization
stage: advanced
status: validated
---

# The Complexity Class Hierarchy

## Core Idea
The major complexity classes form a hierarchy: L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE ⊆ EXPTIME. The time hierarchy theorem, proved by diagonalization, guarantees that strictly more time yields strictly more computational power: DTIME(n) ⊊ DTIME(n²). Similarly, the space hierarchy theorem shows DSPACE(log n) ⊊ DSPACE(n). It is proven that P ⊊ EXPTIME, so the hierarchy is strict overall, but the intermediate separations — P vs. NP, NP vs. PSPACE — remain open. The polynomial hierarchy extends NP with alternating quantifiers, analogous to the arithmetical hierarchy.

## How It's Best Learned
Study the hierarchy theorem proofs as applications of diagonalization — the same technique used for the halting problem. Then map out which containments are proven strict and which remain open, building an accurate picture of current knowledge.

## Common Misconceptions
- The complexity class hierarchy is not fully proven strict at every level; P ≠ NP and NP ≠ PSPACE are both unresolved.
- If P = NP were proven, the entire polynomial hierarchy would collapse to P, dramatically simplifying our picture of computational complexity.

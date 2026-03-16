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

## Explainer

You already understand P and NP as the heart of the complexity landscape — P is what deterministic polynomial time can decide, NP is what nondeterminism adds. But these two classes sit inside a much richer landscape. Think of computational resources — time and space — as two different currencies. Using more of one can sometimes substitute for the other, and the **complexity hierarchy** maps out exactly which tradeoffs are possible and which boundaries are real.

**PSPACE** is the class of problems solvable with polynomial *space*, regardless of how long computation takes. Because space can be reused across time steps, PSPACE is potentially much larger than NP: a problem might require exponential time but only polynomial space to solve, since you can reuse the same memory cells for many different subcomputations. The canonical PSPACE-complete problem is TQBF (totally quantified Boolean formulas), which asks whether a formula with alternating universal and existential quantifiers is true — the same structure as adversarial games. This connects PSPACE to problems like determining the winner of a board game under optimal play.

Above PSPACE sits **EXPTIME** — problems solvable in exponential time — and we *do* know that P ⊊ EXPTIME is a strict containment. The proof uses **diagonalization**, the same technique you saw with Cantor and the halting problem. The time hierarchy theorem shows that given strictly more time, you can solve strictly more problems: DTIME(n^k) ⊊ DTIME(n^(k+1)) for all k. The argument constructs a language by diagonalizing against all machines running in time T(n), building a problem that deliberately answers differently from every such machine. Similarly, the space hierarchy theorem shows DSPACE(log n) ⊊ DSPACE(n).

The **polynomial hierarchy** (PH) extends NP with alternating quantifiers: Σ₁ = NP, Π₁ = co-NP, Σ₂ = NP^NP (NP with an NP oracle), and so on. This mirrors the arithmetical hierarchy you may know from logic. A key structural fact: if P = NP, then PH collapses to P — every level becomes equivalent. This is a reason (not a proof!) that P ≠ NP is expected: the polynomial hierarchy seems to be genuinely infinite. The current picture is: we know P ⊊ EXPTIME strictly, we know P ⊆ NP ⊆ PSPACE ⊆ EXPTIME, but the intermediate separations — P vs. NP, NP vs. PSPACE — remain among the deepest open problems in mathematics.

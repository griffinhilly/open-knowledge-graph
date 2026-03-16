---
id: 3sat-satisfiability-variant
title: 3-SAT and k-SAT Variants
domain: computer-science
course: theory-of-computation
prerequisites:
- id: sat-boolean-satisfiability
  type: hard
- id: np-completeness
  type: hard
tags:
- np-complete
- clause-restrictions
stage: advanced
status: draft
---

# 3-SAT and k-SAT Variants

## Core Idea
3-SAT restricts SAT to formulas where each clause has exactly three literals; k-SAT generalizes to k literals per clause. Remarkably, 3-SAT remains NP-complete despite the restriction—restricting clause size doesn't reduce hardness beyond 3 literals. 2-SAT is solvable in polynomial time via implication graphs; k-SAT for k ≥ 3 is NP-complete. The phase transition phenomenon—random k-SAT formulas become hardest near the satisfiability threshold—is a major topic in complexity physics.

## Explainer

You already know that the Boolean satisfiability problem (SAT) asks whether a propositional formula in conjunctive normal form (CNF) has a satisfying assignment, and that SAT is NP-complete — the first problem proven to be so via Cook's theorem. **3-SAT** takes this general problem and adds a structural constraint: every clause must contain exactly three literals. A typical 3-SAT instance looks like `(x₁ ∨ ¬x₂ ∨ x₃) ∧ (¬x₁ ∨ x₄ ∨ x₂) ∧ ...` where each parenthesized group has exactly three terms. The surprising result is that this restricted version is *still* NP-complete — limiting clauses to three literals does not make the problem meaningfully easier.

Why does 3-SAT matter so much in complexity theory? Because it is the workhorse of NP-completeness reductions. When you want to prove a new problem is NP-complete, you typically reduce *from* 3-SAT rather than from general SAT. The fixed clause size of three makes the reduction machinery simpler and more uniform — you always know exactly what the source structure looks like. Most of the hundreds of known NP-completeness proofs go through 3-SAT as an intermediate step, making it arguably the most useful single problem in the NP-completeness toolkit.

The picture changes dramatically when you shrink the clause size to two. **2-SAT** — where every clause has exactly two literals — is solvable in polynomial time. The key insight is that each 2-SAT clause `(a ∨ b)` is logically equivalent to the implications `¬a → b` and `¬b → a`. Collecting all such implications creates a directed **implication graph**, and the formula is satisfiable if and only if no variable and its negation belong to the same strongly connected component. This can be checked in linear time. So the jump from k = 2 to k = 3 is where the complexity-theoretic cliff occurs: 2-SAT is in P, while k-SAT for any k ≥ 3 is NP-complete.

There is also a fascinating empirical phenomenon. For random 3-SAT instances with `n` variables and `m` clauses, the ratio `m/n` controls difficulty. Below a critical threshold (approximately 4.27 for 3-SAT), almost all random instances are satisfiable and easy to solve. Above it, almost all are unsatisfiable and easy to refute. Right at the threshold — the **phase transition** — instances are hardest, often requiring exponential search time in practice. This mirrors phase transitions in physics (like water freezing at 0°C) and reveals deep structural properties of the problem landscape that inform both algorithm design and our understanding of computational hardness.

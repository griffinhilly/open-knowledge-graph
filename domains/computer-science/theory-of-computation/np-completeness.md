---
id: np-completeness
title: NP-Completeness
domain: computer-science
course: theory-of-computation
prerequisites:
- id: p-vs-np-problem
  type: hard
- id: undecidability-reductions
  type: soft
builds-toward:
- cook-levin-theorem
tags:
- NP-complete
- NP-hard
- reductions
- polynomial-time-reduction
stage: advanced
status: draft
---

# NP-Completeness

## Core Idea
A problem X is NP-hard if every problem in NP can be reduced to X in polynomial time, meaning X is at least as hard as anything in NP. X is NP-complete if it is NP-hard and itself in NP — the 'hardest' problems in NP. If any NP-complete problem is in P, then P = NP. NP-complete problems include 3-SAT, Hamiltonian cycle, vertex cover, clique, and hundreds of others across combinatorics, biology, and economics. The concept, developed by Cook and Karp in 1971–1972, revolutionized the understanding of computational hardness.

## How It's Best Learned
Prove that 3-SAT ≤ₚ Independent Set, then ≤ₚ Vertex Cover, following Karp's original reductions. For each, focus on constructing the polynomial-time transformation and proving it is a valid reduction in both directions.

## Common Misconceptions
- Confusing NP-hard with NP-complete: NP-hard means at least as hard as NP-complete, but an NP-hard problem need not be in NP (e.g., the halting problem is NP-hard but undecidable).
- Believing that if a problem is NP-complete it has no practical solutions — approximation algorithms and heuristics can make NP-complete problems tractable in practice.

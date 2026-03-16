---
id: reduction-many-one-polynomial
title: Polynomial Many-One Reductions
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: boolean-satisfiability-and-reductions
  type: hard
tags:
- reductions
- hardness
- complexity-classes
stage: advanced
status: draft
---

# Polynomial Many-One Reductions

## Core Idea
A polynomial many-one reduction from L₁ to L₂ is a polynomial-time computable function f where x ∈ L₁ ⟺ f(x) ∈ L₂, formalizing 'problem L₁ is no harder than L₂.' If L₂ is polynomial-solvable and L₁ reduces to L₂, then L₁ is solvable in polynomial time. NP-completeness is defined via such reductions: a problem is NP-complete if in NP and all NP problems reduce to it. Reductions form the backbone of complexity theory, transferring difficulty between problems.

## Explainer

You have already seen reductions used to prove NP-completeness, and you know how SAT reductions work in practice. A **polynomial many-one reduction** (also called a Karp reduction) is the precise formal tool underlying all of that work. The idea is deceptively simple: to reduce problem A to problem B, you build a polynomial-time function f that transforms every instance x of A into an instance f(x) of B, such that x is a yes-instance of A if and only if f(x) is a yes-instance of B. You never run B's solver — you just translate the question.

The "many-one" in the name means the function f maps inputs to outputs but need not be injective: many different inputs to A can map to the same input for B. The "polynomial" means f must be computable in polynomial time, ensuring the translation itself is efficient. This is critical because if f took exponential time to compute, the reduction would be useless for complexity classification — you would have already spent more time than a brute-force search.

The power of reductions flows in two directions. In the **easy direction**, if you know how to solve B efficiently and you can reduce A to B, then you can solve A efficiently: compute f(x) in polynomial time, then solve f(x) using B's algorithm in polynomial time. In the **hard direction** — and this is how reductions are most often used — if you know A is hard (say, NP-complete) and you can reduce A to B, then B must be at least as hard as A. If B were easy, you could solve A easily via the reduction, contradicting A's hardness. This is exactly how NP-completeness proofs work: you take a known NP-complete problem, reduce it to your target problem, and conclude the target is NP-hard.

A concrete example: to show that CLIQUE is NP-hard, you reduce 3-SAT to CLIQUE. Given a 3-SAT formula, you construct a graph where each literal in each clause becomes a vertex, edges connect compatible literals from different clauses, and the formula is satisfiable if and only if the graph contains a clique of size k (the number of clauses). The construction runs in polynomial time, the equivalence holds in both directions, and the reduction is complete. Notice that you never solve either problem — you just show that an efficient CLIQUE solver would imply an efficient 3-SAT solver, which would imply P = NP.

---
id: hamiltonian-cycle-conditions
title: 'Hamiltonian Cycles: Sufficient Conditions and Challenges'
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: hard
tags:
- hamiltonian-cycles
- sufficient-conditions
- np-hard
stage: formal-systems
status: draft
---

# Hamiltonian Cycles: Sufficient Conditions and Challenges

## Core Idea
A Hamiltonian cycle visits every vertex exactly once. Sufficient conditions include Dirac's theorem (minimum degree ≥ n/2) and Ore's theorem (degree sum of adjacent vertices ≥ n). Despite these sufficient conditions, determining Hamiltonicity is NP-complete in general.

## Explainer

From your formal study of graph theory, you know what a **Hamiltonian cycle** is: a cycle that visits every vertex of a graph exactly once before returning to the start. Compare this to an Eulerian circuit, which traverses every *edge* exactly once — Eulerian circuits have a clean necessary-and-sufficient characterization (connected graph, all even degrees) and can be found efficiently. Hamiltonian cycles are far more difficult. Determining whether one exists in an arbitrary graph is NP-complete, meaning no polynomial-time algorithm is known or expected. But there are **sufficient conditions** — structural properties that, when present, guarantee a Hamiltonian cycle exists.

**Dirac's Theorem** (1952): If G is a simple graph on n ≥ 3 vertices where every vertex has degree at least n/2, then G contains a Hamiltonian cycle. The intuition: when every vertex connects to at least half the graph, the graph is dense enough that a Hamiltonian path can never get "stuck" at a dead end. A formal proof uses a longest-path argument: take a path P of maximum length; its endpoints cannot extend P further, so all their neighbors lie within P. High minimum degree then forces the endpoints to connect back into P in a way that closes a cycle — and the maximality of P forces that cycle to cover every vertex.

**Ore's Theorem** (1960) relaxes Dirac's condition: if for every pair of *non-adjacent* vertices u and v we have deg(u) + deg(v) ≥ n, then G has a Hamiltonian cycle. This is strictly more general — Dirac's theorem is the special case where every individual vertex satisfies the bound. Ore's condition focuses on non-adjacent pairs because adjacent vertices are already connected; the concern is vertices with no direct edge between them, where a Hamiltonian path might get stuck. A sufficiently high combined degree ensures enough "escape routes" from any vertex to complete the cycle.

The critical point is that both theorems give *sufficient* conditions, not necessary ones. Many graphs with Hamiltonian cycles satisfy neither: the cycle graph Cₙ itself has every vertex at degree 2 — far below n/2 for large n — yet it obviously has a Hamiltonian cycle (it *is* one). Dirac's and Ore's conditions are conservative guarantees: when they hold, a cycle is certain; when they fail, nothing can be concluded. For the general problem — an arbitrary graph with no structural promise — the question of whether a Hamiltonian cycle exists is NP-complete. This contrast with Eulerian circuits is a central lesson in graph theory: nearly identical-sounding problems can differ enormously in computational difficulty.

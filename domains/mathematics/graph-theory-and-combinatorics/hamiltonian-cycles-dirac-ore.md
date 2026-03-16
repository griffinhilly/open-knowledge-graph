---
id: hamiltonian-cycles-dirac-ore
title: 'Hamiltonian Cycles: Dirac and Ore Conditions'
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: hamiltonian-circuits
  type: hard
tags:
- graph-theory
- hamiltonicity
stage: formal-systems
status: draft
---

# Hamiltonian Cycles: Dirac and Ore Conditions

## Core Idea
Dirac's Theorem states that a graph with n ≥ 3 vertices where every vertex has degree at least n/2 is Hamiltonian. Ore's Theorem generalizes: if for every non-adjacent pair u,v we have deg(u) + deg(v) ≥ n, the graph is Hamiltonian. These conditions elegantly show that high minimum degree guarantees Hamiltonian cycles, though deciding Hamiltonicity in general remains NP-hard.

## How It's Best Learned
Verify these conditions on small graphs (n ≤ 6) and check that they hold for known Hamiltonian graphs.

## Common Misconceptions
These conditions are sufficient but not necessary; graphs can be Hamiltonian without satisfying Dirac or Ore conditions.

## Explainer

From your study of Hamiltonian circuits, you know that a Hamiltonian cycle visits every vertex in a graph exactly once before returning to the start — the graph-theoretic version of a round trip through every city. The hard question is whether such a cycle exists at all. Unlike Eulerian circuits, which have a clean necessary-and-sufficient condition (every vertex has even degree), Hamiltonicity has no simple characterization. But there are powerful *sufficient* conditions that guarantee a Hamiltonian cycle whenever certain degree requirements are met.

**Dirac's theorem** gives the clearest guarantee: if a graph has n ≥ 3 vertices and every vertex has **degree at least n/2**, then the graph is Hamiltonian. The intuition is density. If every vertex is connected to at least half the graph, you are never boxed in — no matter which path you're building, the current endpoint always has enough neighbors that you can continue visiting new vertices, and the high connectivity ensures you can eventually close the cycle back to the start. For a graph with 10 vertices, Dirac requires every vertex to have degree ≥ 5: each vertex must reach more than half the other vertices.

**Ore's theorem** relaxes the requirement from individual vertices to pairs. Instead of requiring each vertex to have high degree, it requires that for every pair of *non-adjacent* vertices u and v, deg(u) + deg(v) ≥ n. The idea: if u and v are not directly connected, they must together "cover" enough of the graph to ensure a Hamiltonian path exists between them. Every graph satisfying Dirac also satisfies Ore (if both vertices individually have degree ≥ n/2, their sum is ≥ n), but not vice versa — Ore can apply when individual vertices have low degree, as long as every low-degree vertex is adjacent to every other low-degree vertex.

The critical caveat is that both conditions are **sufficient but not necessary**. A graph can be Hamiltonian without satisfying either. A simple cycle on 10 vertices — each vertex with degree 2 — is trivially Hamiltonian (it is one big cycle), yet degree 2 is far below the Dirac threshold of 5. The theorems are one-way doors: satisfying the condition guarantees a Hamiltonian cycle, but failing the condition tells you nothing. This asymmetry reflects a deep fact: determining whether an arbitrary graph is Hamiltonian is NP-hard, meaning no polynomial-time algorithm is known. Eulerian circuits were easy; Hamiltonian cycles are genuinely hard. Dirac and Ore identify a large, well-structured region where the hard problem becomes easy.

---
id: hamiltonian-cycles-discrete
title: Hamiltonian Paths and Cycles
domain: mathematics
course: discrete-math
prerequisites:
- id: hamiltonian-paths-cycles
  type: hard
- id: euler-circuits-applications
  type: soft
builds-toward:
- algorithm-complexity-discrete
tags:
- Hamiltonian-cycle
- Hamiltonian-path
- TSP
- NP-hard
stage: formal-systems
status: draft
---

# Hamiltonian Paths and Cycles

## Core Idea
A Hamiltonian path visits every vertex exactly once; a Hamiltonian cycle returns to its start. Unlike Euler circuits (which exist iff degrees are even), no simple characterization exists for Hamiltonicity. Finding them is NP-complete; the traveling salesman problem seeks the shortest Hamiltonian cycle.

## How It's Best Learned
Recognize sufficient conditions: if every vertex has degree ≥ n/2, a Hamiltonian cycle exists (Dirac's theorem). Practice finding them in small graphs by exhaustive or intelligent search. Distinguish from Euler (edges vs. vertices).

## Common Misconceptions
Hamiltonicity is hard—no polynomial-time algorithm is known. Dirac/Ore conditions are sufficient but not necessary. A graph can have many, one, or no Hamiltonian cycles.

## Explainer

You've already seen **Euler circuits** — tours that traverse every *edge* exactly once. The trick to their existence was elegant: just check that every vertex has even degree. **Hamiltonian paths and cycles** ask the dual question: can you visit every *vertex* exactly once? This sounds like it should be equally tractable, but the contrast here is one of the most instructive asymmetries in all of mathematics. Euler circuits are easy to detect and construct in polynomial time; Hamiltonian cycles are computationally hard — no efficient algorithm is known.

A **Hamiltonian path** visits every vertex exactly once. A **Hamiltonian cycle** does the same but returns to its starting vertex, forming a closed loop. Any graph may have many of these, exactly one, or none at all, and small changes to the graph can flip the answer completely. This instability is a clue to why the problem is hard: there's no local certificate. With Euler circuits, checking degree parity at each vertex tells the whole story. With Hamiltonian cycles, you'd need to somehow "see" the entire path structure at once.

**Dirac's Theorem** provides one useful sufficient condition: if every vertex in a graph with n ≥ 3 vertices has degree at least n/2, a Hamiltonian cycle is guaranteed to exist. Intuitively, each vertex is connected to more than half the graph, so there's always a way out of any partial path. But this condition is far from necessary — many sparse graphs have Hamiltonian cycles. The theorem gives you a green light when it applies; it says nothing about graphs that don't meet the threshold.

The reason this matters beyond pure mathematics is the **Traveling Salesman Problem (TSP)**: given a complete weighted graph (cities connected by roads with distances), find the shortest Hamiltonian cycle. TSP is NP-hard, meaning it almost certainly cannot be solved efficiently in the worst case. Enormous real-world logistics — shipping routes, circuit board drilling, genome sequencing — reduce to TSP variants. Because of this, TSP has spawned a rich field of approximation algorithms: approaches that can't guarantee optimality but can guarantee a solution within, say, 1.5× the optimal length. The hardness of finding Hamiltonian cycles isn't an obstacle — it's the engine driving decades of algorithmic ingenuity.

---
id: hamiltonian-circuits
title: Hamiltonian Circuits and Paths
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: euler-circuits-and-paths
  type: soft
tags:
- hamiltonian-circuit
- hamiltonian-path
- NP-complete
- traveling-salesman
- dirac-theorem
stage: formal-systems
status: validated
---

# Hamiltonian Circuits and Paths

## Core Idea
A Hamiltonian path visits every vertex exactly once; a Hamiltonian circuit does so and returns to the start. Unlike Eulerian circuits, there is no simple necessary and sufficient characterization of Hamiltonian graphs — determining existence is NP-complete. Sufficient conditions include Dirac's theorem (minimum degree ≥ n/2 implies a Hamiltonian circuit) and Ore's theorem. The traveling salesman problem — find the minimum-cost Hamiltonian circuit in a weighted graph — is one of the most studied problems in combinatorial optimization.

## How It's Best Learned
Explore small examples and feel the absence of a clean characterization. Apply Dirac's and Ore's theorems to examples, noting they give only sufficient conditions. Contrast the theoretical intractability with Eulerian circuits to appreciate how similar-sounding problems can have radically different difficulty.

## Common Misconceptions
- Confusing Hamiltonian circuits (vertices visited once) with Eulerian circuits (edges traversed once).
- Believing that if a sufficient condition like Dirac's fails, no Hamiltonian circuit exists.

## Explainer

You already know Eulerian circuits, which traverse every **edge** exactly once. Hamiltonian circuits ask the analogous question about **vertices**: can you visit every vertex exactly once and return to the start? The questions sound nearly identical, but their mathematical difficulty is worlds apart. Eulerian circuits have a clean, checkable characterization: a connected graph has one if and only if every vertex has even degree. Hamiltonian circuits have no such theorem. Whether a given graph has a Hamiltonian circuit is, in general, computationally intractable — it is one of the canonical NP-complete problems.

To feel why the vertex version is harder, consider what makes Eulerian circuits easy: you can always "see" locally whether you're stuck. At any vertex, you just need to avoid cutting off unvisited edges — a condition you can check by looking at degrees. Hamiltonian circuits require global coordination. Choosing the wrong early vertex can trap you in a corner where the remaining vertices can't be reached in sequence, but there's no local signal warning you of this. You have to think about the whole graph simultaneously, which is why exhaustive search seems unavoidable in the worst case.

**Dirac's theorem** gives one escape hatch: if every vertex in a graph on n ≥ 3 vertices has degree at least n/2, then a Hamiltonian circuit is guaranteed to exist. The intuition is that high minimum degree means every vertex is so well-connected that you can't get trapped — there's always a way forward. **Ore's theorem** is slightly more general: if every pair of non-adjacent vertices has combined degree at least n, a Hamiltonian circuit exists. Crucially, these are *sufficient* conditions, not necessary ones. A graph can have a Hamiltonian circuit even when neither condition holds. If Dirac's condition fails, you've learned nothing — you must look harder.

The most famous application is the **Traveling Salesman Problem (TSP)**: given a complete weighted graph (cities with road distances), find the minimum-cost Hamiltonian circuit. Every solution visits each city exactly once and returns home — a Hamiltonian circuit — but you want the cheapest one. TSP is studied obsessively because it sits at the intersection of theory (NP-complete, so probably no efficient exact algorithm exists) and practice (delivery routes, circuit board drilling, DNA sequencing all reduce to it). Approximation algorithms, heuristics like nearest-neighbor and 2-opt, and exact branch-and-bound methods give you tools to find good (if not always optimal) solutions for real instances. The Hamiltonian circuit problem is where pure graph theory shakes hands with the hardest problems in computer science.

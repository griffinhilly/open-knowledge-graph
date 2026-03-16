---
id: hamiltonian-paths-cycles
title: Hamiltonian Paths, Cycles, and NP-Completeness
domain: mathematics
course: discrete-math
prerequisites:
- id: walks-paths-cycles
  type: hard
tags:
- graph-theory
- hamiltonian
- np-complete
stage: formal-systems
status: draft
---

# Hamiltonian Paths, Cycles, and NP-Completeness

## Core Idea
A Hamiltonian path visits every vertex exactly once; a Hamiltonian cycle does so and returns to the start. Unlike Eulerian paths, no simple degree-based characterization exists. The Hamiltonian cycle problem is NP-complete, making it computationally hard in general.

## Explainer

From your study of walks, paths, and cycles, you know that a **path** visits vertices without repetition and a **cycle** returns to its starting vertex. A **Hamiltonian path** is a path that visits every vertex exactly once — it exhausts the entire vertex set. A **Hamiltonian cycle** does the same but returns to the starting vertex, forming a cycle that covers every vertex. The name comes from William Rowan Hamilton, who marketed a puzzle asking players to find such a route on a dodecahedron.

The first thing to notice is how different Hamiltonian paths are from Eulerian paths, which traverse every edge exactly once. Eulerian paths have a clean degree-based characterization: a connected graph has an Eulerian path if and only if it has exactly zero or two vertices of odd degree. No analogous theorem exists for Hamiltonian paths. You cannot determine whether a Hamiltonian path exists just by looking at degree sequences. There are partial sufficient conditions — Dirac's theorem guarantees a Hamiltonian cycle if every vertex has degree ≥ n/2 — but no tight necessary-and-sufficient criterion based on local structure alone.

This asymmetry has a deep reason: the **Hamiltonian cycle problem** is **NP-complete**. NP-completeness means that no known efficient (polynomial-time) algorithm solves it in the worst case, and moreover, it is at least as hard as every other problem in the class NP. In practical terms, deciding whether any given large graph has a Hamiltonian cycle requires, in the worst case, examining exponentially many possibilities. This is why the Travelling Salesman Problem — which asks for the shortest Hamiltonian cycle in a weighted graph — is one of the most famous hard problems in computer science.

For small or structured graphs, special cases help. Bipartite graphs with unequal part sizes cannot have Hamiltonian cycles (a parity argument shows this). Complete graphs always have them. Graphs satisfying Dirac's or Ore's condition are guaranteed to have them. But in general, the lack of a degree-based shortcut means Hamiltonian problems require fundamentally different techniques from Eulerian ones — and are vastly harder to resolve algorithmically. The contrast between Eulerian paths (polynomial-time decidable) and Hamiltonian paths (NP-complete) is one of the cleanest illustrations in combinatorics of how subtly problem difficulty can vary.

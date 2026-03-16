---
id: hamiltonian-path-cycle
title: Hamiltonian Path and Cycle Problems
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
builds-toward:
- approximation-algorithms-design
tags:
- np-complete
- graph-problems
- path-problems
stage: advanced
status: draft
---

# Hamiltonian Path and Cycle Problems

## Core Idea
The Hamiltonian cycle problem asks if a graph contains a cycle visiting each vertex exactly once; Hamiltonian path is the variant without returning to start. Both are NP-complete. Unlike shortest-cycle detection (solvable in polynomial time by DFS), finding a Hamiltonian path/cycle appears intrinsically hard, requiring potentially checking all permutations. The problems highlight the distinction between decision (NP) and optimization: verifying a Hamiltonian cycle is quick, but finding one seems impossible in polynomial time.

## Explainer

From your study of NP-completeness, you know that certain problems sit at the hardest tier of NP — if any one of them could be solved in polynomial time, then every problem in NP could be. The **Hamiltonian path and cycle problems** are classic members of this club. A **Hamiltonian cycle** in a graph is a cycle that visits every vertex exactly once and returns to the starting vertex. A **Hamiltonian path** is the same idea without the return — a path that touches every vertex exactly once. The decision versions ask simply: does a given graph contain one?

The problem is deceptively easy to state but fiendishly hard to solve. Consider a small graph with 20 vertices. A brute-force approach would try all possible orderings of the vertices — that is 20! (about 2.4 × 10^18) permutations. Even for modest graph sizes, exhaustive search is completely infeasible. No one has found a polynomial-time algorithm, and the NP-completeness of the Hamiltonian cycle problem (proved by Richard Karp in 1972 via reduction from the satisfiability problem) gives strong theoretical evidence that no such algorithm exists. What makes the problem tantalizing is the **verification asymmetry**: if someone hands you a sequence of vertices and claims it is a Hamiltonian cycle, you can check it in O(n) time by confirming that every vertex appears exactly once and that each consecutive pair is connected by an edge.

It is instructive to contrast Hamiltonian problems with their close cousin, the **Eulerian path/cycle** problem, which asks whether a graph has a path or cycle that traverses every *edge* exactly once. Euler's theorem gives a clean characterization: an Eulerian circuit exists if and only if every vertex has even degree, and this can be checked (and the circuit constructed) in polynomial time. The switch from "every edge once" to "every vertex once" transforms the problem from tractable to intractable — a striking illustration of how small changes in problem specification can produce enormous jumps in computational difficulty.

The Hamiltonian cycle problem underpins many real-world optimization challenges. The **Traveling Salesman Problem (TSP)** — find the shortest route visiting every city exactly once — is essentially the optimization version of the Hamiltonian cycle problem with weighted edges. Because exact solutions are intractable for large inputs, practical approaches rely on approximation algorithms, heuristics, and special-case structure (for example, if edge weights satisfy the triangle inequality, a 1.5-approximation exists). Understanding the Hamiltonian problem's NP-completeness is what justifies this turn to approximation: we are not settling for "good enough" out of laziness, but because finding the exact optimum is provably as hard as solving the hardest problems in NP.

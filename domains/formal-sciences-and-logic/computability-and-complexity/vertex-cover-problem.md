---
id: vertex-cover-problem
title: Vertex Cover and Set Cover Problems
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: three-sat-np-complete
  type: hard
- id: np-completeness-formal
  type: hard
- id: graph-theory-fundamentals
  type: soft
builds-toward:
- fixed-parameter-tractability
tags:
- graph-problems
- np-complete
- optimization
stage: advanced
status: draft
---

# Vertex Cover and Set Cover Problems

## Core Idea
The vertex cover problem asks whether a graph has a set of k vertices such that every edge touches at least one vertex in the set. This classic NP-complete problem serves as a foundation for parameterized complexity. It demonstrates how many combinatorial optimization problems can be shown NP-hard through polynomial reductions from 3-SAT.

## How It's Best Learned
Begin with small graphs and try to find vertex covers by hand. Then reduce 3-SAT to vertex cover: each clause becomes a triangle and variables are connected via gadgets.

## Common Misconceptions
- Vertex cover becomes easy if we allow approximation (approximation is hard too, by PCP).
- All NP-complete problems reduce to vertex cover (only true for problems NP-hard via specific reductions).

## Explainer

A **vertex cover** of a graph is a set S of vertices such that every edge has at least one endpoint in S. Think of it as a guard-placement problem: you want to station guards at vertices so that every corridor (edge) is watched by at least one guard. The decision version asks: does graph G have a vertex cover of size at most k? From your work on NP-completeness and 3-SAT, you understand the framework — this problem is NP-complete, meaning it is in NP and every NP problem reduces to it in polynomial time.

The NP-hardness proof proceeds by **reduction from 3-SAT**. Given a 3-SAT formula with n variables and m clauses, you construct a graph as follows. Each variable x contributes two vertices (one for x, one for ¬x) connected by an edge — every vertex cover must include at least one of them, encoding a truth assignment. Each clause (a ∨ b ∨ c) contributes a triangle of three vertices, with edges connecting each triangle vertex to its corresponding literal vertex in the variable gadgets. A vertex cover of size n + 2m exists if and only if the formula is satisfiable: the n variable choices fix a truth assignment, and for each clause, the 2 remaining triangle vertices (not corresponding to a satisfied literal) round out the cover. Checking this bijection carefully is the reduction.

What makes vertex cover especially instructive is its starring role in **parameterized complexity** — analyzing how difficulty depends on a parameter k separate from input size n. Although vertex cover is NP-hard in general (k may grow with n), for small fixed k it admits algorithms far better than brute force. A simple search tree works: pick any edge, branch on whether to include its left or right endpoint in the cover, recurse on the remaining graph with k decremented. This gives an O(2^k · n) algorithm — exponential in k but linear in n. More powerful **kernelization** algorithms reduce any instance to one with at most 2k² vertices in polynomial time: if a vertex has degree > k, it must be in the cover; include it and decrement k. If more than k² edges remain after removing high-degree vertices, the answer is "no." The resulting O(k²)-vertex **kernel** can then be solved by brute force in time depending only on k.

The **Set Cover problem** generalizes vertex cover: given a universe U and sets S₁, ..., Sₘ, find the minimum number of sets covering all of U. Vertex cover is the special case where U is the edge set and each set consists of edges incident to one vertex. Set cover inherits NP-hardness and also admits a classical greedy approximation — always pick the set covering the most uncovered elements — achieving a ratio of ln|U| + 1. This is tight: under ETH, you cannot approximate set cover within (1 − ε) ln|U| for any ε > 0 unless P = NP, demonstrating that the connection between NP-completeness proofs and approximation hardness runs deep. Vertex cover and set cover together are foundational examples connecting reduction-based hardness, parameterized tractability, and approximation algorithms.

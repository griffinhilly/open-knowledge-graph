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

## Questions

```yaml
- question: "An algorithm claims to verify a proposed Hamiltonian cycle in O(n) time by checking that every vertex appears exactly once and each consecutive pair is connected by an edge. Is this consistent with the NP-completeness of the Hamiltonian cycle problem?"
  type: multiple-choice
  options:
    - "No — if verification is O(n), then finding a Hamiltonian cycle must also be O(n) by symmetry"
    - "Yes — NP-completeness says finding a solution may be hard, but verification is always easy; the Hamiltonian cycle problem is in NP precisely because valid solutions can be verified in polynomial time"
    - "No — NP-complete problems cannot be verified in polynomial time; that is what makes them hard"
    - "Yes, but only for graphs with fewer than 1,000 vertices; larger graphs require exponential verification time"
  answer: 1
  explanation: "The NP in 'NP-complete' stands for 'nondeterministic polynomial time' — the class of problems where proposed solutions can be verified in polynomial time. NP-completeness says that *finding* a solution appears to require exponential time; *verifying* a given solution is quick. For Hamiltonian cycle, checking that every vertex appears exactly once and all edges exist takes O(n) time. This verification asymmetry — easy to check, hard to find — is the defining characteristic of NP. Option C is exactly backwards and is the most common misconception about what 'NP-complete' means."

- question: "An undirected graph G has 15 vertices, all with even degree. What can you conclude?"
  type: multiple-choice
  options:
    - "G contains a Hamiltonian cycle — every vertex with even degree guarantees each can be visited exactly once"
    - "G contains a Hamiltonian cycle if and only if it is also connected"
    - "G contains an Eulerian circuit — a closed walk traversing every edge exactly once — if G is connected"
    - "G contains neither an Eulerian circuit nor a Hamiltonian cycle without further information"
  answer: 2
  explanation: "This is Euler's theorem: a connected graph has an Eulerian circuit if and only if every vertex has even degree. If G is connected and all vertices have even degree, an Eulerian circuit exists and can be found in polynomial time. Crucially, the even-degree condition says nothing about a Hamiltonian cycle. The Hamiltonian cycle problem — visiting every vertex once — has no such clean characterization and is NP-complete. This contrast is the key lesson: 'every edge once' (Eulerian) admits a polynomial-time solution with a simple necessary and sufficient condition; 'every vertex once' (Hamiltonian) is NP-complete with no known efficient algorithm."

- question: "The Eulerian circuit problem and the Hamiltonian cycle problem both ask about traversal conditions on graphs, yet one is solvable in polynomial time while the other is NP-complete."
  type: true-false
  answer: true
  explanation: "Eulerian circuit (traverse every edge exactly once): solvable in polynomial time using Euler's theorem (all vertices must have even degree) and Hierholzer's algorithm. Hamiltonian cycle (visit every vertex exactly once): NP-complete, with no known polynomial-time algorithm. This striking contrast illustrates how small changes in problem formulation — edges vs. vertices — can produce enormous changes in computational complexity. The lesson is that problem hardness is not determined by how simple the problem sounds, but by the mathematical structure it requires you to exploit."

- question: "Because the Hamiltonian cycle problem is NP-complete, it has been proven that no polynomial-time algorithm for it can ever exist."
  type: true-false
  answer: false
  explanation: "NP-completeness does not prove that no polynomial-time algorithm exists — it proves that if any NP-complete problem has a polynomial-time solution, then P = NP (every NP problem would be tractable). Since we do not know whether P = NP, we cannot rule out a polynomial-time algorithm for Hamiltonian cycle. NP-completeness provides strong evidence that efficient algorithms are unlikely, but it is not a proof of impossibility. The P ≠ NP conjecture is one of the Millennium Prize Problems — unresolved despite decades of effort. What NP-completeness does tell us is that we should abandon the search for exact polynomial-time algorithms and turn to approximations, heuristics, or special-case structure instead."

- question: "Why does changing a problem from 'traverse every edge exactly once' to 'visit every vertex exactly once' transform it from polynomial-time solvable to NP-complete?"
  type: short-answer
  answer: "The Eulerian condition has a clean algebraic characterization: an Eulerian circuit exists if and only if every vertex has even degree, which can be checked in O(n) time. This structure allows a polynomial-time algorithm. The Hamiltonian condition has no analogous characterization — there is no known property of a graph that you can check cheaply and that determines whether a Hamiltonian cycle exists. You must, in the worst case, reason about whether some permutation of all n vertices forms a valid cycle, which leads to a search space of (n−1)! possibilities. The underlying combinatorial structure simply doesn't offer the same algebraic shortcuts."
  explanation: "This example is a favorite in computability theory because the two problems sound nearly identical to non-specialists. The key insight is that computational difficulty is not about how simple the problem *sounds* but about what mathematical structure it has. Eulerian problems have degree-sequence characterizations that reduce the question to local properties; Hamiltonian problems require reasoning about global structure that no efficient algorithm has exploited. This is why NP-completeness proofs are valuable: they tell us when we are facing a fundamentally hard problem and should look for approximations rather than exact solutions."
```

## Explainer

From your study of NP-completeness, you know that certain problems sit at the hardest tier of NP — if any one of them could be solved in polynomial time, then every problem in NP could be. The **Hamiltonian path and cycle problems** are classic members of this club. A **Hamiltonian cycle** in a graph is a cycle that visits every vertex exactly once and returns to the starting vertex. A **Hamiltonian path** is the same idea without the return — a path that touches every vertex exactly once. The decision versions ask simply: does a given graph contain one?

The problem is deceptively easy to state but fiendishly hard to solve. Consider a small graph with 20 vertices. A brute-force approach would try all possible orderings of the vertices — that is 20! (about 2.4 × 10^18) permutations. Even for modest graph sizes, exhaustive search is completely infeasible. No one has found a polynomial-time algorithm, and the NP-completeness of the Hamiltonian cycle problem (proved by Richard Karp in 1972 via reduction from the satisfiability problem) gives strong theoretical evidence that no such algorithm exists. What makes the problem tantalizing is the **verification asymmetry**: if someone hands you a sequence of vertices and claims it is a Hamiltonian cycle, you can check it in O(n) time by confirming that every vertex appears exactly once and that each consecutive pair is connected by an edge.

It is instructive to contrast Hamiltonian problems with their close cousin, the **Eulerian path/cycle** problem, which asks whether a graph has a path or cycle that traverses every *edge* exactly once. Euler's theorem gives a clean characterization: an Eulerian circuit exists if and only if every vertex has even degree, and this can be checked (and the circuit constructed) in polynomial time. The switch from "every edge once" to "every vertex once" transforms the problem from tractable to intractable — a striking illustration of how small changes in problem specification can produce enormous jumps in computational difficulty.

The Hamiltonian cycle problem underpins many real-world optimization challenges. The **Traveling Salesman Problem (TSP)** — find the shortest route visiting every city exactly once — is essentially the optimization version of the Hamiltonian cycle problem with weighted edges. Because exact solutions are intractable for large inputs, practical approaches rely on approximation algorithms, heuristics, and special-case structure (for example, if edge weights satisfy the triangle inequality, a 1.5-approximation exists). Understanding the Hamiltonian problem's NP-completeness is what justifies this turn to approximation: we are not settling for "good enough" out of laziness, but because finding the exact optimum is provably as hard as solving the hardest problems in NP.

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
status: validated
---

# Hamiltonian Paths, Cycles, and NP-Completeness

## Core Idea
A Hamiltonian path visits every vertex exactly once; a Hamiltonian cycle does so and returns to the start. Unlike Eulerian paths, no simple degree-based characterization exists. The Hamiltonian cycle problem is NP-complete, making it computationally hard in general.

## Questions

```yaml
- question: "A graph has exactly two vertices of odd degree. A student concludes it must have a Hamiltonian path. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing is wrong — two odd-degree vertices guarantee a Hamiltonian path"
    - "Two odd-degree vertices guarantee an Eulerian path, not a Hamiltonian path — these are different problems with different criteria"
    - "The student should check whether it has zero odd-degree vertices, which would guarantee a Hamiltonian cycle"
    - "Degree conditions can only rule out Hamiltonian paths, never guarantee them"
  answer: 1
  explanation: "Two odd-degree vertices is exactly the condition for an Eulerian path (traversing every edge once), not a Hamiltonian path (visiting every vertex once). Confusing these is the central misconception: Eulerian paths have a clean degree-based characterization, Hamiltonian paths do not. The student has applied the right kind of test to the wrong problem. A graph can have two odd-degree vertices and either contain or lack a Hamiltonian path."

- question: "What does it mean practically that the Hamiltonian cycle problem is NP-complete?"
  type: multiple-choice
  options:
    - "No algorithm can solve it — it is mathematically undecidable"
    - "It can be solved in polynomial time only for graphs with special structure, but no known polynomial-time algorithm works for all graphs"
    - "The problem is harder than any problem in NP, making it the most difficult class of problems"
    - "It requires exponential space to store the graph, making it infeasible for large inputs"
  answer: 1
  explanation: "NP-completeness means no known polynomial-time algorithm solves it in the worst case, and it is as hard as every other NP problem. It is NOT undecidable — a brute-force algorithm can always solve it by checking all possible vertex orderings, which takes O(n!) time. The practical consequence is that for large graphs, no efficient general solution is known. Option C is wrong: NP-complete problems are in NP, not harder than NP (that would be NP-hard but not in NP, or higher levels of the polynomial hierarchy)."

- question: "Any graph satisfying Dirac's condition (every vertex has degree ≥ n/2) is guaranteed to contain a Hamiltonian cycle."
  type: true-false
  answer: true
  explanation: "Dirac's theorem (1952) states exactly this: if G is a simple graph with n ≥ 3 vertices and every vertex has degree ≥ n/2, then G contains a Hamiltonian cycle. This is one of the few positive sufficient conditions for Hamiltonian cycles. Note that it is a sufficient but not necessary condition — graphs can have Hamiltonian cycles with much lower degree requirements. Dirac's condition is also useful precisely because it is checkable in polynomial time, unlike the Hamiltonian problem itself."

- question: "If a graph contains an Eulerian circuit, it must also contain a Hamiltonian cycle."
  type: true-false
  answer: false
  explanation: "These properties are completely independent. An Eulerian circuit (traversing every edge once and returning to the start) requires all vertices to have even degree. A Hamiltonian cycle (visiting every vertex once and returning) requires the right global structure but has no simple degree characterization. A complete graph K₃ (triangle) has both; a graph like two triangles sharing a single vertex has an Eulerian circuit but no Hamiltonian cycle (the shared vertex would have to be visited twice). The contrast between these problems is one of the most instructive examples in combinatorics."

- question: "Explain why the Eulerian path problem is 'easy' (polynomial time) while the Hamiltonian path problem is 'hard' (NP-complete), even though both involve traversing graphs."
  type: short-answer
  answer: "Eulerian paths are easy because they have a local, degree-based characterization: you only need to count vertex degrees to decide existence, and construction follows Hierholzer's algorithm. Hamiltonian paths require global structure — whether a path visiting every vertex exists cannot be determined by any local property like degree. No short certificate for the absence of a Hamiltonian path exists, and exhaustive search takes exponential time. The contrast shows that seemingly similar problems can have radically different computational complexities based on what structural information is needed."
  explanation: "The difficulty gap between Eulerian and Hamiltonian problems is a clean illustration of why P ≠ NP (if true). Eulerian paths reduce to a local property (degree sequence), while Hamiltonian paths require checking a fundamentally global combinatorial structure. This is why NP-completeness proofs often reduce from Hamiltonian cycle — it is a canonical hard problem precisely because it lacks the local structure that makes other graph problems tractable."
```

## Explainer

From your study of walks, paths, and cycles, you know that a **path** visits vertices without repetition and a **cycle** returns to its starting vertex. A **Hamiltonian path** is a path that visits every vertex exactly once — it exhausts the entire vertex set. A **Hamiltonian cycle** does the same but returns to the starting vertex, forming a cycle that covers every vertex. The name comes from William Rowan Hamilton, who marketed a puzzle asking players to find such a route on a dodecahedron.

The first thing to notice is how different Hamiltonian paths are from Eulerian paths, which traverse every edge exactly once. Eulerian paths have a clean degree-based characterization: a connected graph has an Eulerian path if and only if it has exactly zero or two vertices of odd degree. No analogous theorem exists for Hamiltonian paths. You cannot determine whether a Hamiltonian path exists just by looking at degree sequences. There are partial sufficient conditions — Dirac's theorem guarantees a Hamiltonian cycle if every vertex has degree ≥ n/2 — but no tight necessary-and-sufficient criterion based on local structure alone.

This asymmetry has a deep reason: the **Hamiltonian cycle problem** is **NP-complete**. NP-completeness means that no known efficient (polynomial-time) algorithm solves it in the worst case, and moreover, it is at least as hard as every other problem in the class NP. In practical terms, deciding whether any given large graph has a Hamiltonian cycle requires, in the worst case, examining exponentially many possibilities. This is why the Travelling Salesman Problem — which asks for the shortest Hamiltonian cycle in a weighted graph — is one of the most famous hard problems in computer science.

For small or structured graphs, special cases help. Bipartite graphs with unequal part sizes cannot have Hamiltonian cycles (a parity argument shows this). Complete graphs always have them. Graphs satisfying Dirac's or Ore's condition are guaranteed to have them. But in general, the lack of a degree-based shortcut means Hamiltonian problems require fundamentally different techniques from Eulerian ones — and are vastly harder to resolve algorithmically. The contrast between Eulerian paths (polynomial-time decidable) and Hamiltonian paths (NP-complete) is one of the cleanest illustrations in combinatorics of how subtly problem difficulty can vary.

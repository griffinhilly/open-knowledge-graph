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
- id: hamiltonian-cycles-discrete
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

## Questions

```yaml
- question: "A graph G has 10 vertices. Dirac's theorem guarantees a Hamiltonian circuit if which condition holds?"
  type: multiple-choice
  options:
    - "G is connected and has at least 10 edges"
    - "Every vertex has degree at least 5"
    - "Every pair of non-adjacent vertices has combined degree at least 10"
    - "G has an Eulerian circuit"
  answer: 1
  explanation: "Dirac's theorem states: if a graph on n ≥ 3 vertices has every vertex with degree ≥ n/2, then a Hamiltonian circuit exists. For n = 10, the threshold is 10/2 = 5. Option C is Ore's theorem (a different sufficient condition). Option D (Eulerian circuit) has no bearing on Hamiltonian circuits — these are entirely different properties."

- question: "You check a graph G and find that Dirac's condition fails — some vertex has degree below n/2. What can you conclude?"
  type: multiple-choice
  options:
    - "G has no Hamiltonian circuit"
    - "G may or may not have a Hamiltonian circuit — Dirac's is a sufficient condition, not a necessary one"
    - "G has no Eulerian circuit either"
    - "G is disconnected"
  answer: 1
  explanation: "Dirac's theorem provides a *sufficient* condition for Hamiltonian circuits, not a necessary one. A graph can have a Hamiltonian circuit even when Dirac's condition fails. Failing a sufficient condition tells you the theorem's guarantee doesn't apply — it says nothing about what is actually true of the graph. This is the most important distinction: sufficient conditions confirm existence when met, but their failure confirms nothing."

- question: "A connected graph has a Hamiltonian circuit if and primarily if most vertex has even degree."
  type: true-false
  answer: false
  explanation: "The 'every vertex has even degree' condition characterizes *Eulerian* circuits, not Hamiltonian circuits. An Eulerian circuit traverses every edge exactly once; a Hamiltonian circuit visits every vertex exactly once. These are fundamentally different conditions. Hamiltonian circuits have no known simple necessary and sufficient characterization — determining their existence is NP-complete."

- question: "Determining whether an arbitrary graph has a Hamiltonian circuit is computationally harder than determining whether it has an Eulerian circuit."
  type: true-false
  answer: true
  explanation: "Eulerian circuits have a polynomial-time characterization: check connectivity and verify all vertices have even degree — a linear-time computation. Hamiltonian circuit existence is NP-complete: no polynomial-time algorithm is known, and the problem is believed to require exponential time in the worst case. Despite the surface similarity of the two questions, the vertex version is exponentially harder than the edge version."

- question: "Why does the degree-based characterization that works for Eulerian circuits not extend to Hamiltonian circuits?"
  type: short-answer
  answer: "Eulerian circuits can be checked locally: at each vertex, whether the circuit can continue depends only on the parity of that vertex's degree, which is a purely local property. Hamiltonian circuits require global coordination — choosing the wrong vertex early can trap you with unreachable vertices later, and there is no local signal that warns you before it happens."
  explanation: "The local vs. global distinction is the core insight. Euler's condition works because you can always 'fix' a locally bad choice by rerouting — the even-degree condition ensures you never get permanently stuck. Hamiltonian paths require thinking about the entire graph simultaneously: does this sequence of vertex visits leave a connected remainder that can be completed? That global feasibility check has no known efficient shortcut, which is why it's NP-complete while Eulerian circuit detection is easy."
```

## Explainer

You already know Eulerian circuits, which traverse every **edge** exactly once. Hamiltonian circuits ask the analogous question about **vertices**: can you visit every vertex exactly once and return to the start? The questions sound nearly identical, but their mathematical difficulty is worlds apart. Eulerian circuits have a clean, checkable characterization: a connected graph has one if and only if every vertex has even degree. Hamiltonian circuits have no such theorem. Whether a given graph has a Hamiltonian circuit is, in general, computationally intractable — it is one of the canonical NP-complete problems.

To feel why the vertex version is harder, consider what makes Eulerian circuits easy: you can always "see" locally whether you're stuck. At any vertex, you just need to avoid cutting off unvisited edges — a condition you can check by looking at degrees. Hamiltonian circuits require global coordination. Choosing the wrong early vertex can trap you in a corner where the remaining vertices can't be reached in sequence, but there's no local signal warning you of this. You have to think about the whole graph simultaneously, which is why exhaustive search seems unavoidable in the worst case.

**Dirac's theorem** gives one escape hatch: if every vertex in a graph on n ≥ 3 vertices has degree at least n/2, then a Hamiltonian circuit is guaranteed to exist. The intuition is that high minimum degree means every vertex is so well-connected that you can't get trapped — there's always a way forward. **Ore's theorem** is slightly more general: if every pair of non-adjacent vertices has combined degree at least n, a Hamiltonian circuit exists. Crucially, these are *sufficient* conditions, not necessary ones. A graph can have a Hamiltonian circuit even when neither condition holds. If Dirac's condition fails, you've learned nothing — you must look harder.

The most famous application is the **Traveling Salesman Problem (TSP)**: given a complete weighted graph (cities with road distances), find the minimum-cost Hamiltonian circuit. Every solution visits each city exactly once and returns home — a Hamiltonian circuit — but you want the cheapest one. TSP is studied obsessively because it sits at the intersection of theory (NP-complete, so probably no efficient exact algorithm exists) and practice (delivery routes, circuit board drilling, DNA sequencing all reduce to it). Approximation algorithms, heuristics like nearest-neighbor and 2-opt, and exact branch-and-bound methods give you tools to find good (if not always optimal) solutions for real instances. The Hamiltonian circuit problem is where pure graph theory shakes hands with the hardest problems in computer science.

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
status: validated
---

# Hamiltonian Paths and Cycles

## Core Idea
A Hamiltonian path visits every vertex exactly once; a Hamiltonian cycle returns to its start. Unlike Euler circuits (which exist iff degrees are even), no simple characterization exists for Hamiltonicity. Finding them is NP-complete; the traveling salesman problem seeks the shortest Hamiltonian cycle.

## How It's Best Learned
Recognize sufficient conditions: if every vertex has degree ≥ n/2, a Hamiltonian cycle exists (Dirac's theorem). Practice finding them in small graphs by exhaustive or intelligent search. Distinguish from Euler (edges vs. vertices).

## Common Misconceptions
Hamiltonicity is hard—no polynomial-time algorithm is known. Dirac/Ore conditions are sufficient but not necessary. A graph can have many, one, or no Hamiltonian cycles.

## Questions

```yaml
- question: "A student argues: 'Since Euler circuits can be detected by checking vertex degrees, Hamiltonian cycles should have a similarly simple characterization.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Hamiltonian cycles do have a simple characterization — just check whether the graph is connected"
    - "Euler circuits actually cannot be detected efficiently either"
    - "The structural symmetry doesn't hold computationally — Hamiltonian cycles are NP-complete with no known efficient algorithm"
    - "Dirac's theorem provides an exact degree-based characterization for Hamiltonian cycles just as parity does for Euler"
  answer: 2
  explanation: "This is the core asymmetry of the topic. Euler circuits have a clean LOCAL certificate (checking degree parity at each vertex) that works in polynomial time. Hamiltonian cycles have no such local certificate — you must 'see' the entire path structure at once. This is precisely why Hamiltonian detection is NP-complete. Superficially symmetric problems can belong to entirely different complexity classes."

- question: "A connected graph G has 10 vertices, and every vertex has degree 5. What can you conclude?"
  type: multiple-choice
  options:
    - "G may or may not have a Hamiltonian cycle — degree 5 falls short of the threshold"
    - "G definitely has a Hamiltonian cycle, by Dirac's theorem"
    - "G definitely has a Hamiltonian cycle because all vertices have equal degree"
    - "G cannot have a Hamiltonian cycle because the degree is less than n−1"
  answer: 1
  explanation: "n = 10, so n/2 = 5. Every vertex has degree exactly 5 ≥ n/2. Dirac's theorem states that for a graph with n ≥ 3 vertices where every vertex has degree ≥ n/2, a Hamiltonian cycle is guaranteed to exist. The condition is met, so existence is guaranteed — though the graph may have many such cycles, not just one."

- question: "If a graph satisfies Dirac's theorem conditions (most vertex has degree ≥ n/2), we know the graph has exactly one Hamiltonian cycle."
  type: true-false
  answer: false
  explanation: "Dirac's theorem guarantees EXISTENCE, not uniqueness. A graph meeting the degree condition may have many Hamiltonian cycles. Furthermore, Dirac's condition is sufficient but not necessary — many graphs that do not satisfy it still have Hamiltonian cycles. The theorem is a one-way green light, not an exact characterization."

- question: "The Traveling Salesman Problem is a special case of the Hamiltonian cycle problem."
  type: true-false
  answer: true
  explanation: "TSP asks for the shortest Hamiltonian cycle in a weighted complete graph — finding one of minimum total edge weight. Finding any Hamiltonian cycle (without weights) is the unweighted version. TSP's NP-hardness follows from the NP-completeness of Hamiltonian cycle detection, since even deciding whether a Hamiltonian cycle exists is hard, let alone finding the shortest one."

- question: "Why is the asymmetry between Euler circuits and Hamiltonian cycles considered one of the most instructive results in discrete mathematics?"
  type: short-answer
  answer: "Euler circuits and Hamiltonian cycles look like symmetric problems — traverse every edge exactly once vs. visit every vertex exactly once — yet they belong to entirely different complexity classes. Euler circuits have a simple local criterion (all even degrees) solvable in polynomial time. Hamiltonian cycles have no known efficient algorithm and are NP-complete. This asymmetry teaches that superficial structural similarity between problems does not imply computational similarity — the nature of the certificate (local vs. global) determines tractability."
  explanation: "The deeper lesson is about local vs. global certificates. Degree parity can be checked vertex by vertex without seeing the whole graph. Verifying a Hamiltonian path requires examining the entire structure. This distinction between problems admitting local certificates and those requiring global ones is fundamental to complexity theory and to developing intuition about what makes problems hard."
```

## Explainer

You've already seen **Euler circuits** — tours that traverse every *edge* exactly once. The trick to their existence was elegant: just check that every vertex has even degree. **Hamiltonian paths and cycles** ask the dual question: can you visit every *vertex* exactly once? This sounds like it should be equally tractable, but the contrast here is one of the most instructive asymmetries in all of mathematics. Euler circuits are easy to detect and construct in polynomial time; Hamiltonian cycles are computationally hard — no efficient algorithm is known.

A **Hamiltonian path** visits every vertex exactly once. A **Hamiltonian cycle** does the same but returns to its starting vertex, forming a closed loop. Any graph may have many of these, exactly one, or none at all, and small changes to the graph can flip the answer completely. This instability is a clue to why the problem is hard: there's no local certificate. With Euler circuits, checking degree parity at each vertex tells the whole story. With Hamiltonian cycles, you'd need to somehow "see" the entire path structure at once.

**Dirac's Theorem** provides one useful sufficient condition: if every vertex in a graph with n ≥ 3 vertices has degree at least n/2, a Hamiltonian cycle is guaranteed to exist. Intuitively, each vertex is connected to more than half the graph, so there's always a way out of any partial path. But this condition is far from necessary — many sparse graphs have Hamiltonian cycles. The theorem gives you a green light when it applies; it says nothing about graphs that don't meet the threshold.

The reason this matters beyond pure mathematics is the **Traveling Salesman Problem (TSP)**: given a complete weighted graph (cities connected by roads with distances), find the shortest Hamiltonian cycle. TSP is NP-hard, meaning it almost certainly cannot be solved efficiently in the worst case. Enormous real-world logistics — shipping routes, circuit board drilling, genome sequencing — reduce to TSP variants. Because of this, TSP has spawned a rich field of approximation algorithms: approaches that can't guarantee optimality but can guarantee a solution within, say, 1.5× the optimal length. The hardness of finding Hamiltonian cycles isn't an obstacle — it's the engine driving decades of algorithmic ingenuity.

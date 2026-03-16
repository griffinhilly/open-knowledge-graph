---
id: traveling-salesman-problem
title: Traveling Salesman Problem (TSP)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: graph-theory-fundamentals
  type: soft
builds-toward:
- knapsack-problem-variations
- approximation-algorithms
tags:
- optimization
- np-hard
- routing
stage: advanced
status: draft
---

# Traveling Salesman Problem (TSP)

## Core Idea
The traveling salesman problem asks for the shortest route visiting all cities exactly once and returning home. The decision version (is there a tour of length ≤ k?) is NP-complete. TSP exemplifies an optimization problem whose hardness motivates approximation algorithms: while finding the optimal tour is hard, finding a tour within a constant factor of optimal is tractable for some variants.

## Explainer

You know from NP-completeness theory that certain decision problems are maximally hard within NP — no polynomial-time algorithm is known for them, and any polynomial-time algorithm for one would solve all of NP. The **Traveling Salesman Problem** is a clean, vivid instance of this phenomenon. Imagine a salesperson who must visit n cities, travel each road at most once, and return to the starting city, minimizing total distance. With n = 10, you could exhaustively check all (10-1)!/2 ≈ 181,000 tours. With n = 30, that number exceeds 4 × 10³⁰ — more than the age of the universe in nanoseconds. Brute force is hopeless at scale.

The **decision version** of TSP asks: is there a tour of length at most k? This is NP-complete — it is in NP (a tour certificate can be verified in polynomial time by summing edge weights), and every NP problem reduces to it. The **optimization version** (find the shortest tour) is NP-hard: at least as hard as any NP problem, but not itself a decision problem in NP. This distinction matters: NP-completeness applies strictly to decision problems, while NP-hardness captures the difficulty of optimization versions.

Because finding the exact optimum is hard, TSP motivates the study of **approximation algorithms** — algorithms that run in polynomial time and are guaranteed to find a tour within a fixed factor of optimal. For the *metric TSP* variant (where distances satisfy the triangle inequality), the **Christofides algorithm** achieves a 3/2-approximation: its tour is never more than 1.5 times the optimal length. This is a celebrated result because it shows that while perfection is out of reach, disciplined approximation is not. For general TSP without the metric constraint, no constant-factor approximation is possible unless P = NP.

TSP also connects to graph theory prerequisites: the problem can be modeled as finding a minimum-weight Hamiltonian cycle in a complete weighted graph. The gap between Hamiltonian cycle (NP-complete to decide existence) and Eulerian circuit (polynomial-time solvable by Hierholzer's algorithm) illustrates how subtle differences in a problem's structure can radically change its computational tractability. TSP is paradigmatic precisely because it is easy to state, practically important in logistics and circuit design, and theoretically intractable — making it a central benchmark for algorithms research.

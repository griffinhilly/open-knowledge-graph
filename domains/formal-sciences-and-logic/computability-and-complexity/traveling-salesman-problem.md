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

## Questions

```yaml
- question: "A logistics company needs an optimal delivery route for 50 cities. They say: 'TSP is NP-hard, so finding a good route is hopeless — we'll just use any path.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — NP-hardness means no good solution can be found efficiently, so any route is as good as any other"
    - "NP-hardness rules out exact optimal solutions in polynomial time, but does not rule out approximations — for metric TSP, the Christofides algorithm guarantees a tour within 1.5× optimal in polynomial time"
    - "TSP is actually polynomial for 50 cities, so brute force would work fine"
    - "TSP is NP-hard only for non-Euclidean distances; for real-world road networks it is polynomial"
  answer: 1
  explanation: "NP-hardness means no known polynomial-time algorithm finds the exact optimum, but it says nothing about how far a polynomial-time algorithm can deviate from optimal. The Christofides algorithm runs in polynomial time and guarantees a tour of length at most 3/2 times the optimal — for many practical purposes, a near-optimal route is good enough. 'NP-hard therefore hopeless' conflates exact optimization with approximation. TSP is a paradigmatic case where approximation algorithms rescue practical utility from theoretical intractability."

- question: "The decision version of TSP (is there a tour of length ≤ k?) is NP-complete. The optimization version (find the shortest tour) is NP-hard. What is the key distinction between these two characterizations?"
  type: multiple-choice
  options:
    - "NP-complete problems are strictly harder than NP-hard problems"
    - "NP-completeness applies to decision problems that are both in NP (verifiable in poly-time) and NP-hard; the optimization version is NP-hard but is not itself a decision problem in NP, since 'optimal' cannot be verified without solving the problem"
    - "The optimization version is also in NP because you can verify a given tour's length in polynomial time"
    - "NP-hard means the problem cannot be solved; NP-complete means it can be solved with exponential resources"
  answer: 1
  explanation: "NP-completeness is defined for decision problems: a problem is NP-complete if it is in NP (a 'yes' certificate can be verified in poly-time) and is NP-hard (every NP problem reduces to it). For the decision TSP, a certificate is simply the tour itself — sum the edge weights, check ≤ k: poly-time. The optimization version asks for the minimum — you can verify a candidate tour's length, but you cannot verify that it is optimal without ruling out all shorter tours (which requires solving the problem). So the optimization version is NP-hard but not in NP, hence not NP-complete. This distinction is not pedantry — it matters for the theory of what kinds of reductions and approximation results apply."

- question: "The Christofides algorithm solves TSP optimally in polynomial time for metric instances."
  type: true-false
  answer: false
  explanation: "This is the most important misconception to correct. The Christofides algorithm is an approximation algorithm: it runs in polynomial time and guarantees a tour of length at most 3/2 times the optimal, but it does not find the optimal tour. Finding the optimal TSP tour remains NP-hard even for metric instances — no polynomial-time exact algorithm is known. Christofides is celebrated precisely because achieving a guaranteed constant factor (1.5) in polynomial time is a non-trivial result, distinct from exactness."

- question: "For general TSP without the triangle inequality, no polynomial-time algorithm can achieve any constant-factor approximation guarantee unless P = NP."
  type: true-false
  answer: true
  explanation: "This is a sharp contrast with metric TSP. Without the triangle inequality, any constant-factor approximation can be shown to imply a polynomial-time solution for Hamiltonian cycle (via a reduction that assigns very large weights to missing edges). Since Hamiltonian cycle is NP-complete, a constant-factor approximation for general TSP would imply P = NP. The metric constraint (triangle inequality) is not just a simplification — it is the structural property that makes constant-factor approximation possible at all. Removing it makes TSP inapproximable."

- question: "Explain why TSP is NP-hard to solve exactly, yet a polynomial-time 3/2-approximation exists for metric TSP. What property of metric TSP enables the approximation?"
  type: short-answer
  answer: "TSP is NP-hard because the search space of all possible tours grows factorially with n, and no efficient way to navigate it toward the optimum is known. However, for metric TSP (where edge weights satisfy the triangle inequality), the Christofides algorithm exploits structure: it finds a minimum spanning tree (polynomial), adds a minimum weight perfect matching on odd-degree vertices (polynomial), and constructs an Euler tour that shortcuts repeated vertices. The triangle inequality guarantees that shortcuts never increase total distance — so detours are safe to eliminate. This structural property allows the algorithm to bound the tour length at 3/2 × optimal. For general TSP without the triangle inequality, shortcuts can be arbitrarily costly, so this argument breaks down and no constant-factor approximation is achievable unless P = NP."
  explanation: "The key insight is that NP-hardness and approximability are separate properties. A problem can be NP-hard to solve exactly but still admit efficient approximation. Metric TSP is NP-hard but 3/2-approximable. Other problems (like general TSP) are NP-hard and also inapproximable. The triangle inequality is the structural bridge that separates these two cases for TSP specifically."
```

## Explainer

You know from NP-completeness theory that certain decision problems are maximally hard within NP — no polynomial-time algorithm is known for them, and any polynomial-time algorithm for one would solve all of NP. The **Traveling Salesman Problem** is a clean, vivid instance of this phenomenon. Imagine a salesperson who must visit n cities, travel each road at most once, and return to the starting city, minimizing total distance. With n = 10, you could exhaustively check all (10-1)!/2 ≈ 181,000 tours. With n = 30, that number exceeds 4 × 10³⁰ — more than the age of the universe in nanoseconds. Brute force is hopeless at scale.

The **decision version** of TSP asks: is there a tour of length at most k? This is NP-complete — it is in NP (a tour certificate can be verified in polynomial time by summing edge weights), and every NP problem reduces to it. The **optimization version** (find the shortest tour) is NP-hard: at least as hard as any NP problem, but not itself a decision problem in NP. This distinction matters: NP-completeness applies strictly to decision problems, while NP-hardness captures the difficulty of optimization versions.

Because finding the exact optimum is hard, TSP motivates the study of **approximation algorithms** — algorithms that run in polynomial time and are guaranteed to find a tour within a fixed factor of optimal. For the *metric TSP* variant (where distances satisfy the triangle inequality), the **Christofides algorithm** achieves a 3/2-approximation: its tour is never more than 1.5 times the optimal length. This is a celebrated result because it shows that while perfection is out of reach, disciplined approximation is not. For general TSP without the metric constraint, no constant-factor approximation is possible unless P = NP.

TSP also connects to graph theory prerequisites: the problem can be modeled as finding a minimum-weight Hamiltonian cycle in a complete weighted graph. The gap between Hamiltonian cycle (NP-complete to decide existence) and Eulerian circuit (polynomial-time solvable by Hierholzer's algorithm) illustrates how subtle differences in a problem's structure can radically change its computational tractability. TSP is paradigmatic precisely because it is easy to state, practically important in logistics and circuit design, and theoretically intractable — making it a central benchmark for algorithms research.

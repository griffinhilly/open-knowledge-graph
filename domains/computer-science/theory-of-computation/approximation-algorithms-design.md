---
id: approximation-algorithms-design
title: Approximation Algorithms and Approximation Ratios
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: greedy-algorithms
  type: soft
- id: vertex-cover-clique-problems
  type: soft
builds-toward:
- hardness-of-approximation
tags:
- hardness
- approximation
- optimization
stage: advanced
status: validated
---

# Approximation Algorithms and Approximation Ratios

## Core Idea
For NP-hard optimization problems, approximation algorithms find near-optimal solutions in polynomial time. An algorithm is an α-approximation if its solution is at most α times the optimal (for minimization problems). Vertex cover has a simple 2-approximation (greedy edge selection); TSP has a 1.5-approximation (Christofides algorithm); general TSP permits no better than 1.001-approximation without P=NP. The field explores the boundary between hardness and tractability, showing approximate solutions often suffice where exact ones are intractable.

## How It's Best Learned
Implement greedy approximation algorithms and analyze their ratios empirically. Prove approximation guarantees mathematically. Compare approximation quality to hardness lower bounds.

## Common Misconceptions
Thinking approximation algorithms solve NP-complete problems in polynomial time (they trade exactness for speed). Confusing constant approximations with polynomial approximations (some problems cannot achieve constant approximation unless P=NP). Assuming all NP-hard problems admit good approximations (some are inapproximable).

## Questions

```yaml
- question: "A greedy algorithm for vertex cover always produces a solution with at most twice as many vertices as optimal, running in polynomial time. A student claims this algorithm 'partially solves an NP-complete problem.' What is the most accurate characterization?"
  type: multiple-choice
  options:
    - "The student is correct — producing any suboptimal solution in polynomial time partially solves NP-completeness"
    - "The student is wrong — approximation algorithms are not 'partial solutions' but complete algorithms with provable guarantees, and finding a 2-approximation in polynomial time is a well-defined and fully achieved goal"
    - "The algorithm cannot be correct because NP-complete problems cannot be solved in polynomial time under any conditions"
    - "The algorithm is only valid if vertex cover is proved to be in P"
  answer: 1
  explanation: "Approximation algorithms do not 'partially solve' anything — they completely solve a precisely stated problem: find a solution within factor α of optimal in polynomial time. The 2-approximation for vertex cover achieves exactly this guarantee. The misconception conflates 'not finding the exact optimum' with 'not solving the problem fully,' but the approximation ratio is the stated objective, and it is met."

- question: "For the Traveling Salesman Problem restricted to instances satisfying the triangle inequality, what is the best known polynomial-time approximation ratio?"
  type: multiple-choice
  options:
    - "2-approximation via minimum spanning tree doubling"
    - "1.5-approximation via Christofides' algorithm (MST plus minimum-weight perfect matching)"
    - "No constant-factor approximation exists unless P = NP"
    - "A PTAS exists, achieving (1 + ε) for any ε > 0"
  answer: 1
  explanation: "Christofides' algorithm achieves a 1.5 ratio for metric TSP: build an MST, find a minimum-weight perfect matching on odd-degree vertices, combine to form an Eulerian circuit, then shortcut repeated vertices. The triangle inequality ensures shortcuts don't increase total distance. Contrast this with general TSP (without triangle inequality), which has no constant-factor approximation unless P = NP — illustrating that the structure of an NP-hard problem, not just its hardness, determines approximability."

- question: "A polynomial-time approximation scheme (PTAS) for a minimization problem guarantees a solution within (1 + ε) of optimal for any ε > 0, but the running time may grow as ε shrinks."
  type: true-false
  answer: true
  explanation: "A PTAS gives you arbitrarily close approximations in polynomial time for each fixed ε, but the polynomial's degree or coefficient may depend on 1/ε. For example, a running time of O(n^(1/ε)) is polynomial for any fixed ε but grows steeply. This is still far better than exact exponential algorithms for large inputs, and problems with PTAS are considered 'almost tractable' compared to those that are inapproximable."

- question: "Since vertex cover is NP-hard, no polynomial-time algorithm can guarantee a solution better than a constant factor away from optimal."
  type: true-false
  answer: false
  explanation: "Vertex cover has a simple 2-approximation via greedy edge selection: pick any uncovered edge, add both endpoints, remove covered edges, repeat. The result uses at most twice the optimal. This is a polynomial-time guarantee. The NP-hardness of vertex cover means finding the EXACT optimum in polynomial time is (almost certainly) impossible — but it says nothing about the quality of approximations achievable."

- question: "Why is knowing that a problem is NP-hard insufficient to determine how well it can be approximated? Give examples illustrating the range of approximability among NP-hard problems."
  type: short-answer
  answer: "NP-hardness only rules out polynomial-time exact algorithms (assuming P ≠ NP). Approximability is a separate question. Vertex cover (NP-hard) has a 2-approximation; metric TSP has a 1.5-approximation (Christofides); the knapsack problem has a PTAS yielding solutions within (1+ε) of optimal for any ε. But general TSP and set cover admit no constant-factor approximation (or only O(log n)), and some problems are inapproximable to any factor. NP-hardness is a single threshold; approximability is a rich spectrum."
  explanation: "The field of approximation algorithms exists precisely because NP-hardness is not a monolithic barrier — it is a floor below which exact algorithms cannot go, but above which the landscape varies enormously. Practical algorithm design depends critically on where a specific problem falls: a guaranteed-50%-suboptimal solution in milliseconds is often more valuable than a theoretically exact answer requiring centuries of compute."
```

## Explainer

From your study of NP-completeness, you know that certain optimization problems almost certainly have no polynomial-time algorithm that finds the exact best answer. But "no exact solution in polynomial time" does not mean "no useful solution in polynomial time." **Approximation algorithms** accept a controlled tradeoff: they guarantee a solution that is provably close to optimal, and they do so efficiently. The question shifts from "can we find the best answer?" to "how close to the best answer can we get, and how fast?"

The quality of this tradeoff is measured by the **approximation ratio** (often denoted α). For a minimization problem, an α-approximation algorithm guarantees that its solution costs at most α times the optimal cost. For a maximization problem, the guarantee is at least 1/α of optimal. Consider the **vertex cover** problem: given a graph, find the smallest set of vertices that touches every edge. This is NP-hard, but there is a remarkably simple 2-approximation. Repeatedly pick any uncovered edge, add both its endpoints to the cover, and remove all edges touching those vertices. The result uses at most twice as many vertices as the optimal cover — because every edge you picked must be covered, and the optimal solution must include at least one endpoint of each, so you use at most double.

The landscape of approximation is surprisingly varied. Some problems, like vertex cover, admit clean constant-factor approximations using greedy strategies you already know. The **Traveling Salesman Problem** with triangle inequality has a 1.5-approximation via Christofides' algorithm, which combines minimum spanning trees with minimum-weight perfect matchings. But the general TSP (without triangle inequality) cannot be approximated to any constant factor in polynomial time unless P = NP. Other problems, like the knapsack problem, admit a **polynomial-time approximation scheme (PTAS)** — for any desired ε > 0, you can get within a (1 + ε) factor of optimal, though the running time grows as ε shrinks.

This variation reveals one of the deepest insights in computational complexity: NP-hardness is not a single level of difficulty. Some NP-hard problems are "almost tractable" because good approximations exist; others are provably **inapproximable** beyond certain thresholds. The field of approximation algorithms maps this terrain, connecting the structure of individual problems to the quality of the best polynomial-time solution we can hope for. Understanding where a problem falls on this spectrum is often more practically useful than simply knowing it is NP-hard — because in the real world, a guaranteed-within-50% answer computed in seconds frequently outperforms an exact answer that would take centuries.

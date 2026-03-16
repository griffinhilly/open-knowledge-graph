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
builds-toward:
- hardness-of-approximation
tags:
- hardness
- approximation
- optimization
stage: advanced
status: draft
---

# Approximation Algorithms and Approximation Ratios

## Core Idea
For NP-hard optimization problems, approximation algorithms find near-optimal solutions in polynomial time. An algorithm is an α-approximation if its solution is at most α times the optimal (for minimization problems). Vertex cover has a simple 2-approximation (greedy edge selection); TSP has a 1.5-approximation (Christofides algorithm); general TSP permits no better than 1.001-approximation without P=NP. The field explores the boundary between hardness and tractability, showing approximate solutions often suffice where exact ones are intractable.

## How It's Best Learned
Implement greedy approximation algorithms and analyze their ratios empirically. Prove approximation guarantees mathematically. Compare approximation quality to hardness lower bounds.

## Common Misconceptions
Thinking approximation algorithms solve NP-complete problems in polynomial time (they trade exactness for speed). Confusing constant approximations with polynomial approximations (some problems cannot achieve constant approximation unless P=NP). Assuming all NP-hard problems admit good approximations (some are inapproximable).

## Explainer

From your study of NP-completeness, you know that certain optimization problems almost certainly have no polynomial-time algorithm that finds the exact best answer. But "no exact solution in polynomial time" does not mean "no useful solution in polynomial time." **Approximation algorithms** accept a controlled tradeoff: they guarantee a solution that is provably close to optimal, and they do so efficiently. The question shifts from "can we find the best answer?" to "how close to the best answer can we get, and how fast?"

The quality of this tradeoff is measured by the **approximation ratio** (often denoted α). For a minimization problem, an α-approximation algorithm guarantees that its solution costs at most α times the optimal cost. For a maximization problem, the guarantee is at least 1/α of optimal. Consider the **vertex cover** problem: given a graph, find the smallest set of vertices that touches every edge. This is NP-hard, but there is a remarkably simple 2-approximation. Repeatedly pick any uncovered edge, add both its endpoints to the cover, and remove all edges touching those vertices. The result uses at most twice as many vertices as the optimal cover — because every edge you picked must be covered, and the optimal solution must include at least one endpoint of each, so you use at most double.

The landscape of approximation is surprisingly varied. Some problems, like vertex cover, admit clean constant-factor approximations using greedy strategies you already know. The **Traveling Salesman Problem** with triangle inequality has a 1.5-approximation via Christofides' algorithm, which combines minimum spanning trees with minimum-weight perfect matchings. But the general TSP (without triangle inequality) cannot be approximated to any constant factor in polynomial time unless P = NP. Other problems, like the knapsack problem, admit a **polynomial-time approximation scheme (PTAS)** — for any desired ε > 0, you can get within a (1 + ε) factor of optimal, though the running time grows as ε shrinks.

This variation reveals one of the deepest insights in computational complexity: NP-hardness is not a single level of difficulty. Some NP-hard problems are "almost tractable" because good approximations exist; others are provably **inapproximable** beyond certain thresholds. The field of approximation algorithms maps this terrain, connecting the structure of individual problems to the quality of the best polynomial-time solution we can hope for. Understanding where a problem falls on this spectrum is often more practically useful than simply knowing it is NP-hard — because in the real world, a guaranteed-within-50% answer computed in seconds frequently outperforms an exact answer that would take centuries.

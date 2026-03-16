---
id: partition-subset-sum-problems
title: Partition and Subset Sum Problems
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: dynamic-programming-intro
  type: soft
builds-toward:
- approximation-algorithms-design
tags:
- np-complete
- numeric-problems
- pseudo-polynomial
stage: advanced
status: draft
---

# Partition and Subset Sum Problems

## Core Idea
Partition asks: can a set of integers be divided into two subsets with equal sum? Subset sum asks: given a set and target, does a subset sum to the target? Both are NP-complete but admit pseudo-polynomial algorithms via dynamic programming in O(n·S) time where S is the sum. This illustrates how NP-complete problems vary: partition has no PTAS (polynomial-time approximation scheme), but knapsack does. These problems show hardness is nuanced—NP-completeness is not the end of analysis.

## Explainer

From your study of NP-completeness, you know that NP-complete problems are the hardest problems in NP — if any one of them has a polynomial-time algorithm, they all do. But that classification alone does not tell you how to cope with a specific NP-complete problem in practice. Partition and Subset Sum are the canonical examples of why the story does not end at "it's NP-complete." These two closely related problems reveal that the structure of the input — not just its size — determines how hard instances actually are to solve.

**Subset Sum** asks: given a set of integers and a target value *T*, is there a subset whose elements add up to exactly *T*? **Partition** is the special case where *T* equals half the total sum — can you split the set into two groups with equal totals? Both problems are NP-complete, which you can prove by reduction from known NP-complete problems. But here is the surprising twist: both admit **pseudo-polynomial time** algorithms using dynamic programming. The classic DP approach builds a boolean table where entry DP[i][s] records whether the first *i* elements can form a subset summing to *s*. The table has *n* × *S* entries (where *S* is the target sum), and filling each entry takes constant time. The total runtime is O(n·S) — polynomial in the numeric value of the input but exponential in the number of bits needed to represent *S*. This is exactly the distinction between polynomial and pseudo-polynomial time.

Why does this matter? Because it means the hardness of these problems depends on how large the numbers are, not just how many items you have. If your integers are bounded by some polynomial in *n* (say, each number fits in a few digits), the DP algorithm runs in genuinely polynomial time. It is only when the numbers are exponentially large relative to *n* that the problem becomes truly intractable. This is why Subset Sum and Partition are called **weakly NP-complete** — their hardness vanishes when numbers are small. Contrast this with **strongly NP-complete** problems like 3-SAT or graph coloring, which remain hard regardless of the magnitudes involved.

The approximation landscape adds another layer of nuance. The closely related Knapsack problem (which generalizes Subset Sum by adding values and a capacity constraint) admits a **fully polynomial-time approximation scheme** (FPTAS): for any desired accuracy ε, you can find a solution within a (1−ε) factor of optimal in time polynomial in both *n* and 1/ε. Partition, on the other hand, has no PTAS unless P = NP. This means two problems that look almost identical — both involve choosing subsets to hit numeric targets — have fundamentally different approximability. The lesson is that NP-completeness is a coarse classification. To understand what you can actually do with a hard problem, you must look deeper: at pseudo-polynomial algorithms, at weak versus strong NP-completeness, and at the approximation hierarchy. These distinctions are what separate theoretical impossibility from practical solvability.

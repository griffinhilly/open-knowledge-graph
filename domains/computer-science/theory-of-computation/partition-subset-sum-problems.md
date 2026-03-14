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

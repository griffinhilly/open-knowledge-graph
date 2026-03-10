---
id: big-o-notation
title: Big-O Notation and Asymptotic Analysis
domain: mathematics
course: discrete-math
prerequisites:
- id: logarithms-intro
  type: hard
- id: mathematical-induction
  type: soft
- id: limits-at-infinity
  type: soft
builds-toward:
- algorithm-complexity
tags:
- big-o
- asymptotic-analysis
- omega
- theta
- growth-rate
- complexity
stage: formal-systems
status: draft
---

# Big-O Notation and Asymptotic Analysis

## Core Idea
Big-O notation gives an asymptotic upper bound on function growth: f(n) = O(g(n)) means there exist constants C > 0 and n₀ such that f(n) ≤ C·g(n) for all n ≥ n₀. Big-Ω provides a lower bound and Big-Θ a tight (matching) bound. Common complexity classes in increasing order of growth: O(1), O(log n), O(n), O(n log n), O(n²), O(nᵏ), O(2ⁿ), O(n!). Asymptotic analysis focuses on large-input behavior, deliberately ignoring constant factors that depend on hardware or implementation details.

## How It's Best Learned
Prove O, Ω, and Θ relationships from the formal definition by explicitly finding C and n₀ for concrete examples. Plot several growth functions together on a graph to build visual intuition for which functions eventually dominate. Translate loop structures in pseudocode directly to their Big-Θ complexity.

## Common Misconceptions
- Treating O(f) as an equality rather than an upper bound — 5n is O(n²) but is not Θ(n²).
- Keeping lower-order terms in the final answer — n² + 100n is Θ(n²), not Θ(n² + n).
- Confusing worst-case and average-case complexity when applying Big-O to an algorithm.

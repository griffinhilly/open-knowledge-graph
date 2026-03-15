---
id: algorithm-complexity-discrete
title: Algorithm Complexity and Big-O Notation
domain: mathematics
course: discrete-math
prerequisites:
- id: algorithm-analysis-big-o
  type: hard
tags:
- Big-O
- time-complexity
- space-complexity
- asymptotic-analysis
stage: formal-systems
status: draft
---

# Algorithm Complexity and Big-O Notation

## Core Idea
Big-O notation f(n) = O(g(n)) means f(n) ≤ c·g(n) for large n and some constant c. It abstracts away constants and low-order terms to focus on growth rate. Complexity classes include O(1) (constant), O(log n) (logarithmic), O(n) (linear), O(n²) (quadratic), O(2ⁿ) (exponential).

## How It's Best Learned
Analyze simple algorithms (searching, sorting, graph traversal) to derive complexity. Count basic operations: comparisons, assignments, loop iterations. Compare growth: 2ⁿ vastly exceeds nⁿ for large n, yet both are 'hard.' Use recurrence relations for recursive algorithms.

## Common Misconceptions
Big-O is an upper bound; Ω is lower bound; Θ is tight. O(n) ≠ O(n²); the first is strictly better. Constants matter in practice even if Big-O ignores them.

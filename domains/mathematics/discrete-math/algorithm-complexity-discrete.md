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

## Explainer

You already know Big-O from algorithm analysis — O(n) is linear, O(n²) is quadratic, and these labels describe how runtime grows with input size. The discrete math lens formalizes this: Big-O is a mathematical relation between functions, defined precisely as f(n) = O(g(n)) whenever there exist constants c > 0 and n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀. This definition clarifies that Big-O is an *upper bound*, not an exact description — saying an algorithm is O(n²) tells you it doesn't grow faster than quadratic; it might actually be much faster. The definition also explains why constants are dropped: any constant factor can be absorbed into c.

The hierarchy of **complexity classes** — O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ) — describes a spectrum from "nearly free" to "infeasibly slow." Logarithmic growth is nearly constant in practice: log₂(1,000,000) ≈ 20. Linear is comfortable at millions of inputs. Quadratic starts hurting at n ~ 10,000. Exponential is unusable beyond tiny inputs: 2¹⁰⁰ exceeds the number of atoms in the observable universe. This gap between polynomial and exponential isn't just quantitative — it's qualitative, separating tractable from intractable problems in theoretical computer science.

Two companion notations complete the picture. **Ω(g(n))** (Omega) is a lower bound: f(n) = Ω(g(n)) means f grows at least as fast as g. **Θ(g(n))** (Theta) is a tight bound: f(n) = Θ(g(n)) means f is bounded above and below by multiples of g. In practice, "this algorithm is O(n²)" is an upper-bound claim about one algorithm; "comparison-based sorting requires Ω(n log n)" is a lower-bound claim about all possible sorting algorithms. When both bounds match — as they do for merge sort, which is Θ(n log n) — you have the complete asymptotic picture.

A persistent confusion: Big-O ignores constants, but that doesn't mean constants are irrelevant to real performance. An O(n) algorithm with a huge constant can run slower than an O(n²) algorithm with a tiny constant for all practical input sizes. Big-O describes *asymptotic* behavior — what happens as n → ∞. For the inputs you actually encounter, profiling and benchmarking still matter. The notation is a classification tool, not a performance oracle.

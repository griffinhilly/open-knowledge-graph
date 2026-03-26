---
id: algorithm-analysis-big-o
title: Algorithm Analysis and Big-O Notation
domain: mathematics
course: discrete-math
prerequisites:
- id: dijkstra-algorithm
  type: soft
builds-toward:
- complexity-classes-bounds
tags:
- algorithms
- complexity
- big-o
stage: formal-systems
status: validated
---
# Algorithm Analysis and Big-O Notation

## Core Idea
Big-O notation describes asymptotic upper bounds: f(n) ∈ O(g(n)) if f(n) ≤ cg(n) for large n and constant c. It abstracts away constant factors and lower-order terms. Big-Θ and Big-Ω provide tighter and lower bounds respectively.

## How It's Best Learned
Start with simple functions like n, n², 2^n. Compare growth rates by computing limits and building intuition.

## Common Misconceptions
- Confusing O, Ω, and Θ notation.
- Over-simplifying (e.g., O(n² + n) is just O(n²), not O(n²) + O(n)).
- Not accounting for constant factors when appropriate.

## Questions

```yaml
- question: "Which of the following is NOT a valid Big-O upper bound for f(n) = 3n² + 100n?"
  type: multiple-choice
  options: ["O(n²)", "O(n³)", "O(n² + n)", "O(n)"]
  answer: 3
  explanation: "O(n) is not valid because 3n² + 100n grows faster than any constant multiple of n. The others are all valid upper bounds: O(n²) is the tightest, O(n³) is a looser upper bound, and O(n² + n) is redundant but technically correct. Understanding which bounds are valid (even if not tight) is essential for reasoning about algorithm complexity."

- question: "An algorithm that runs in O(n²) time is typically slower in practice than one that runs in O(n log n) time."
  type: true-false
  answer: false
  explanation: "Big-O describes asymptotic behavior as n → ∞ and ignores constant factors. For small inputs, an O(n²) algorithm with a tiny constant could easily outperform an O(n log n) algorithm with a large constant. The asymptotic crossover point may be at n = 10⁶ or higher. Always consider actual input sizes and constant factors when choosing algorithms in practice."

- question: "What is the key difference between O(g(n)), Ω(g(n)), and Θ(g(n))?"
  type: short-answer
  answer: "O gives an asymptotic upper bound (f grows no faster than g), Ω gives a lower bound (f grows at least as fast as g), and Θ means both simultaneously — f grows at exactly the same asymptotic rate as g."
  explanation: "Knowing only an upper bound is often insufficient: a function that is O(n²) might actually run in O(n). Θ-notation is the precise characterization of asymptotic equivalence. In practice, Θ is more informative when provable, but O is used more commonly because lower bounds are harder to establish."
```

## Explainer

When analyzing algorithms, we want to understand how running time grows as the input size n increases — not the exact number of operations, which depends on the hardware, compiler, and implementation details. Big-O notation provides a language for this: we say f(n) ∈ O(g(n)) if there exist constants c and n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀. In plain terms, g(n) is an upper bound on f(n) for large inputs, up to a constant multiplier.

The crucial feature of Big-O is what it deliberately ignores: constant factors and lower-order terms. The function 5n² + 1000n + 7 is O(n²) because for large enough n, the n² term dominates everything else. This simplification is intentional — it focuses attention on the fundamental growth rate, which is what matters when n is very large. The cost is that Big-O cannot compare two O(n²) algorithms; they might differ by a factor of 100 in practice.

Big-O (O) provides only an upper bound. Two companion notations give more precision: Ω(g(n)) is a lower bound — f grows at least as fast as g — and Θ(g(n)) means both, so f grows at exactly the rate g. Most introductory analysis establishes O-bounds (they are easier to prove), but Θ is the more informative statement. When someone says "merge sort runs in O(n log n)", they usually mean Θ(n log n): the best and worst cases both scale as n log n.

A common trap is confusing what Big-O says about an algorithm's speed versus an algorithm's input. O(n²) does not mean "slow for all inputs" — for n = 10, an O(n²) algorithm performs at most 100 operations (scaled by a constant). Asymptotic notation only becomes meaningful as n grows large. For small n, empirical profiling and constant factors matter far more than the Big-O class. Developing judgment about when the asymptotics kick in is part of practical algorithm design.

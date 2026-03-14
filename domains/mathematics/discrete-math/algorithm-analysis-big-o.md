---
id: algorithm-analysis-big-o
title: Algorithm Analysis and Big-O Notation
domain: mathematics
course: discrete-math
prerequisites: []
builds-toward:
- complexity-classes-bounds
tags:
- algorithms
- complexity
- big-o
stage: formal-systems
status: draft
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

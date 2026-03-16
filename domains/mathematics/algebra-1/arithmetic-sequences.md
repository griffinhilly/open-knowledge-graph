---
id: arithmetic-sequences
title: Arithmetic Sequences
domain: mathematics
course: algebra-1
prerequisites:
- id: variable-expressions
  type: hard
- id: slope-concept
  type: soft
- id: writing-linear-equations
  type: soft
- id: arithmetic-patterns-3rd
  type: soft
- id: function-tables
  type: soft
builds-toward:
- geometric-sequences
- arithmetic-sequences-and-series
- linear-functions
tags:
- sequences
- arithmetic
- common-difference
- patterns
stage: abstract-reasoning
status: validated
---
# Arithmetic Sequences

## Core Idea
An arithmetic sequence is a list of numbers where the difference between consecutive terms is constant. This constant is called the common difference (d). The sequence 3, 7, 11, 15, 19, ... has a common difference of 4. The nth term formula is aₙ = a₁ + (n − 1)d, where a₁ is the first term. Arithmetic sequences are discrete versions of linear functions — if you plot the term number against the term value, the points fall on a line with slope d and y-intercept a₁ − d. They appear in salary schedules, seating arrangements, and any context with a constant rate of change applied in steps.

## How It's Best Learned
Start with patterns: give sequences and ask students to find the common difference. Then use the formula to find specific terms (what is the 50th term?). Connect to linear equations: the common difference is the slope, and the first term determines the intercept. Practice finding d given two terms, writing the explicit formula, and determining whether a given number is in the sequence.

## Common Misconceptions
- Using n instead of (n − 1) in the formula (off by one error — the first term is a₁, not a₁ + d).
- Confusing arithmetic sequences with geometric sequences (adding vs. multiplying).
- Not recognizing negative common differences (decreasing sequences are still arithmetic).

## Explainer

An arithmetic sequence is what you get when you apply a constant rate of change one step at a time. Consider a parking garage that charges $5 to enter and $3 for each hour. After 1 hour you've paid $8, after 2 hours $11, after 3 hours $14. Each term is exactly $3 more than the last — that $3 is the **common difference** d. The sequence 8, 11, 14, 17, 20, ... is arithmetic because the gap between consecutive terms never changes. You already know variable expressions; the sequence is really a rule: start at a₁ and keep adding d.

The explicit formula aₙ = a₁ + (n − 1)d lets you jump directly to any term without computing all the ones before it. The "(n − 1)" rather than "n" reflects a simple fact: to reach the nth term you add d exactly (n − 1) times, because the first term is reached with zero additions. For the parking garage, the 10th hour costs 8 + (10 − 1) × 3 = 8 + 27 = $35. Notice this formula is secretly a linear equation: rewrite it as aₙ = d · n + (a₁ − d). If you already know slope from graphing linear equations, you'll recognize d as the slope and (a₁ − d) as the y-intercept. The "term number" n plays the role of x, and the term value aₙ plays the role of y.

This connection to linear functions is the key insight. If you plot (n, aₙ) on a graph — term number on the horizontal axis, term value on the vertical — the points fall exactly on a straight line. The slope of that line is d, the common difference. Arithmetic sequences are discrete linear functions: instead of a continuous line through all real x-values, you only hit the integer points n = 1, 2, 3, .... This is why arithmetic sequences build toward linear functions: they're the same mathematical structure, just restricted to whole-number inputs.

You can also work backward. If you know two terms but not a₁ or d, you can find both. Suppose the 4th term is 19 and the 7th term is 31. The difference of 31 − 19 = 12 spans 3 steps (from n = 4 to n = 7), so d = 12/3 = 4. Then a₁ = 19 − (4 − 1) × 4 = 19 − 12 = 7. To check whether a specific number is in the sequence, solve aₙ = target for n and check whether the answer is a positive whole number. This algebraic thinking — using the formula as an equation to solve — is what connects sequences to the broader toolkit of algebra you've been building.

---
id: arithmetic-sequences-and-series
title: Arithmetic Sequences and Series
domain: mathematics
course: algebra-2
prerequisites:
  - id: equations-variables-both-sides
    type: hard
builds-toward:
  - geometric-sequences-and-series
  - sigma-notation
tags: [sequences, series, arithmetic, common-difference]
stage: abstract-reasoning
status: validated
---

# Arithmetic Sequences and Series

## Core Idea
An arithmetic sequence has a constant difference d between consecutive terms: a_n = a_1 + (n-1)d. The sum of the first n terms (arithmetic series) is S_n = n(a_1 + a_n)/2 = n/2 * (2a_1 + (n-1)d). Arithmetic sequences model linear growth: equally spaced values. The formula for S_n can be derived by pairing terms from opposite ends of the sequence (Gauss's trick).

## How It's Best Learned
Start with pattern recognition: identify common differences. Derive the nth term formula. Use Gauss's pairing trick to derive the sum formula. Practice finding specific terms, common differences, and sums. Apply to real-world scenarios like stacking objects or salary increases.

## Common Misconceptions
- Confusing the nth term formula with the sum formula.
- Off-by-one errors with n (is the first term n = 0 or n = 1?).
- Thinking all sequences with a pattern are arithmetic (geometric sequences also have a pattern but use multiplication).
- Using the wrong formula for S_n when a_n vs. a_1 and d are given.

## Explainer

An **arithmetic sequence** is simply linear growth — or decay — counted in discrete steps. If you know how to solve linear equations, you already understand the underlying structure: the nth term formula a_n = a₁ + (n − 1)d is exactly the slope-intercept form of a line in disguise. The **common difference** d plays the role of slope (how much the output changes per unit increase in n), and a₁ is the starting value. The only wrinkle is the (n − 1) instead of n: since the first term already gives you a₁ before any d has been added, the difference d is added one fewer time than the term number.

A concrete example: you stack cans in a display, with 3 cans on the top row and adding 2 cans to each successive row. The sequence is 3, 5, 7, 9, … with a₁ = 3 and d = 2. The 10th row has a₁₀ = 3 + 9(2) = 21 cans. Notice the pattern: you started at 3 and applied the common difference 9 times to reach the 10th term, not 10 times — that (n − 1) matters.

The sum formula S_n = n(a₁ + a_n)/2 comes from a beautiful trick. Gauss — as a child, allegedly — was asked to sum 1 + 2 + 3 + … + 100. He noticed that pairing the first and last terms gives 101, pairing the second and second-to-last gives 101, and there are 50 such pairs, giving 50 × 101 = 5050. The formula generalizes this: write the sum forwards and backwards, add them term by term, and each of the n pairs sums to (a₁ + a_n). So 2S_n = n(a₁ + a_n), and dividing by 2 gives the formula. An equivalent form is S_n = n/2 · (2a₁ + (n − 1)d), which uses just a₁ and d when you don't know a_n directly.

The key conceptual distinction to keep straight is **arithmetic vs. geometric**: arithmetic sequences add a constant, geometric sequences multiply by a constant. The sequence 3, 6, 12, 24, … is geometric (multiply by 2 each time), not arithmetic. Both are regular patterns, but their sum formulas and long-run behavior are completely different — arithmetic sums grow quadratically in n, while geometric sums grow exponentially or converge, depending on the ratio. As you move toward geometric sequences and sigma notation, you'll see how both families are special cases of a broader theory of series.

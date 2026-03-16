---
id: stars-and-bars
title: 'Stars and Bars: Combinations with Repetition'
domain: mathematics
course: discrete-math
prerequisites:
- id: combinations
  type: hard
- id: counting-principles
  type: hard
builds-toward:
- generating-functions-intro
tags:
- stars-and-bars
- combinations-with-repetition
- counting
- combinatorics
stage: formal-systems
status: validated
---

# Stars and Bars: Combinations with Repetition

## Core Idea
The stars-and-bars technique counts the number of ways to distribute k identical objects into n distinct bins where each bin can hold any number, giving C(n+k−1, k). The idea is to arrange k stars (objects) and n−1 bars (dividers between bins) in a row — each arrangement corresponds to a distribution. This formula solves a wide class of problems: choosing k items from n types with repetition allowed, or counting non-negative integer solutions to x₁ + x₂ + ⋯ + xₙ = k.

## How It's Best Learned
Draw literal stars and bars diagrams: 'ooo|o|oo' represents 3 in bin 1, 1 in bin 2, 2 in bin 3. Converting between the visual and the formula builds reliable intuition. Extend to variations with minimum or maximum constraints using variable substitution.

## Common Misconceptions
- Confusing stars-and-bars (with repetition) with standard combinations (without repetition).
- Forgetting that n−1 bars, not n bars, are needed to create n bins.
- Not recognizing that 'non-negative integer solutions to a sum' problems are stars-and-bars in disguise.

## Explainer

You already know **combinations**: C(n, k) counts the ways to choose k distinct items from n, where order doesn't matter. That formula assumes you can't pick the same item twice. Stars and bars extends this to the case where repetition is allowed — you can pick any item as many times as you like. The trick is finding a clever bijection that reduces this new problem to a combinations problem you already know how to solve.

Imagine you have k identical balls and n labeled boxes, and you want to count every possible distribution (some boxes may be empty). Represent each ball as a star (★) and use n−1 bars (|) as dividers between boxes. A row of k stars and n−1 bars uniquely describes a distribution: count the stars in each segment. For example, with k=5 balls and n=3 boxes, the arrangement ★★|★|★★ means 2 in box 1, 1 in box 2, 2 in box 3. Every arrangement of 5 stars and 2 bars corresponds to exactly one distribution, and vice versa. So the count is just the number of ways to arrange k stars and n−1 bars — choose which k positions (out of k + n−1 total) hold stars: **C(n+k−1, k)**.

The same formula covers a problem that looks unrelated: how many non-negative integer solutions does x₁ + x₂ + ⋯ + xₙ = k have? Each solution is a tuple (x₁, …, xₙ) where xᵢ counts how many balls go into box i. It's the same problem in disguise, so the answer is the same: C(n+k−1, k). This equivalence is worth internalizing — whenever you see "sum equals a constant, all terms non-negative integers," that's stars and bars.

Constraints change the formula through substitution. If each box must hold **at least 1** ball (strict positivity), put one ball in each box first, leaving k−n balls to distribute freely. The answer becomes C(n + (k−n) − 1, k−n) = C(k−1, k−n). If a box has an **upper bound** (say, box 1 holds at most 3), use inclusion-exclusion: count all distributions, then subtract those where box 1 holds 4 or more. The power of stars and bars is that it turns distribution and allocation problems — which feel open-ended — into straightforward combinations calculations, as long as you correctly encode the constraints.

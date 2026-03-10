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
status: draft
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

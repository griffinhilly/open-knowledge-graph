---
id: multinomial-coefficients
title: Multinomial Coefficients
domain: mathematics
course: discrete-math
prerequisites:
- id: combinations
  type: hard
- id: binomial-theorem
  type: hard
- id: permutations
  type: soft
builds-toward:
- generating-functions-intro
tags:
- multinomial
- coefficients
- counting
- combinatorics
- polynomial-expansion
stage: formal-systems
status: draft
---

# Multinomial Coefficients

## Core Idea
The multinomial coefficient n!/(k₁! k₂! ⋯ kₘ!) counts the number of ways to divide n distinct objects into m ordered groups of sizes k₁, k₂, …, kₘ where k₁ + k₂ + ⋯ + kₘ = n. The multinomial theorem generalizes the binomial theorem: (x₁ + x₂ + ⋯ + xₘ)ⁿ equals the sum over all valid (k₁,…,kₘ) of the multinomial coefficient times x₁^k₁ ⋯ xₘ^kₘ. Multinomial coefficients arise naturally when counting arrangements of strings with repeated letters.

## How It's Best Learned
Connect to the binomial theorem first as the m=2 special case. Count arrangements of words with repeated letters (e.g., MISSISSIPPI has 11!/(4!4!2!1!) arrangements) to make the formula concrete before moving to polynomial expansion.

## Common Misconceptions
- Treating the multinomial coefficient as a product of binomial coefficients — this only works in specific decomposition sequences, not in general.
- Forgetting that all group sizes must sum to n.

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
status: validated
---

# Multinomial Coefficients

## Core Idea
The multinomial coefficient n!/(k₁! k₂! ⋯ kₘ!) counts the number of ways to divide n distinct objects into m ordered groups of sizes k₁, k₂, …, kₘ where k₁ + k₂ + ⋯ + kₘ = n. The multinomial theorem generalizes the binomial theorem: (x₁ + x₂ + ⋯ + xₘ)ⁿ equals the sum over all valid (k₁,…,kₘ) of the multinomial coefficient times x₁^k₁ ⋯ xₘ^kₘ. Multinomial coefficients arise naturally when counting arrangements of strings with repeated letters.

## How It's Best Learned
Connect to the binomial theorem first as the m=2 special case. Count arrangements of words with repeated letters (e.g., MISSISSIPPI has 11!/(4!4!2!1!) arrangements) to make the formula concrete before moving to polynomial expansion.

## Common Misconceptions
- Treating the multinomial coefficient as a product of binomial coefficients — this only works in specific decomposition sequences, not in general.
- Forgetting that all group sizes must sum to n.

## Explainer

You already know the **binomial coefficient** C(n, r) = n!/(r!(n−r)!) and the **binomial theorem**: (x + y)ⁿ expands into a sum of terms C(n, k) xᵏ yⁿ⁻ᵏ. The multinomial coefficient generalizes both to situations with more than two categories. Suppose you have n distinct objects and want to sort them into m labeled boxes of sizes k₁, k₂, …, kₘ (where the sizes sum to n). The **multinomial coefficient** n!/(k₁! k₂! ⋯ kₘ!) counts the ways to do this. When m = 2, it reduces exactly to C(n, k₁) = n!/(k₁! k₂!) — the familiar binomial coefficient.

The most concrete way to build intuition is through **arrangements of strings with repeated letters**. How many ways can you arrange the letters in MISSISSIPPI? You have 11 letters: 1 M, 4 I's, 4 S's, and 2 P's. If all 11 were distinct, there'd be 11! arrangements. But the 4 I's are identical — any permutation among them gives the same word — so divide by 4!. Same for the S's (divide by 4!) and P's (divide by 2!). Result: 11!/(1!⋅4!⋅4!⋅2!) = 34,650. The formula is not an arbitrary definition; it's exactly the correction factor for repeated elements.

The **multinomial theorem** extends this to polynomial expansion: (x₁ + x₂ + ⋯ + xₘ)ⁿ = Σ n!/(k₁!⋯kₘ!) · x₁^k₁ ⋯ xₘ^kₘ, where the sum runs over all tuples (k₁,…,kₘ) of non-negative integers summing to n. To see why: expanding the product means choosing, from each of the n factors, one variable xᵢ to "take." For a given monomial x₁^k₁⋯xₘ^kₘ to appear, you must pick x₁ exactly k₁ times, x₂ exactly k₂ times, etc. — and the number of ways to make those selections is precisely the multinomial coefficient. The binomial theorem is just the m = 2 special case.

Where multinomial coefficients diverge from iterated binomial coefficients is subtle. You *can* compute a multinomial coefficient as a product of binomials: n!/(k₁!k₂!k₃!) = C(n, k₁) · C(n−k₁, k₂) · C(n−k₁−k₂, k₃). This "sequential selection" decomposition is valid and sometimes useful, but the end result — the multinomial coefficient — is a single number, not a sequence-dependent product. The value is independent of which decomposition order you choose, because the formula n!/(k₁!⋯kₘ!) is symmetric in interpretation.

---
id: multinomial-theorem
title: The Multinomial Theorem and Multinomial Coefficients
domain: mathematics
course: discrete-math
prerequisites:
- id: binomial-coefficients
  type: hard
builds-toward:
- inclusion-exclusion-principle
tags:
- combinatorics
- multinomial
stage: formal-systems
status: draft
---

# The Multinomial Theorem and Multinomial Coefficients

## Core Idea
The multinomial theorem generalizes the binomial theorem to (x₁ + x₂ + ⋯ + xₖ)^n. Multinomial coefficients n!/(n₁!n₂!⋯nₖ!) count the ways to partition n items into k labeled groups of specified sizes.

## Explainer

You already know the **binomial theorem**: (x + y)^n = Σ C(n,k) xᵏ yⁿ⁻ᵏ, where C(n,k) = n!/(k!(n−k)!). The coefficient C(n,k) counts the number of ways to choose k of the n factors to contribute an x, while the remaining n−k factors contribute a y. The multinomial theorem is the same idea with more than two choices.

When you expand (x + y + z)^3, you are choosing — for each of the 3 factors — whether to pick x, y, or z. A term like x²yz¹ arises when exactly 2 factors contribute x, 1 contributes y, and 0 contribute z — wait, let's say the exponents are n₁ = 2, n₂ = 0, n₃ = 1 to be precise. The **multinomial coefficient** n!/(n₁!n₂!...nₖ!) counts the number of ways to assign roles to the n factors: it equals the number of ways to arrange n objects where n₁ are of type 1, n₂ of type 2, and so on. This is the same formula you use to count anagrams: the word MISSISSIPPI has 11 letters with 1 M, 4 I's, 4 S's, and 2 P's, so there are 11!/(1!4!4!2!) = 34,650 distinct arrangements.

The full **multinomial theorem** states: (x₁ + x₂ + ⋯ + xₖ)^n = Σ [n!/(n₁!n₂!⋯nₖ!)] x₁^n₁ x₂^n₂ ⋯ xₖ^nₖ, where the sum runs over all tuples (n₁, n₂, ..., nₖ) of non-negative integers with n₁ + n₂ + ⋯ + nₖ = n. This is a direct extension of the binomial case with k = 2. As a check: setting x₁ = x₂ = ⋯ = xₖ = 1, the left side becomes kⁿ and the right side sums all multinomial coefficients — this gives a useful identity.

Multinomial coefficients appear throughout combinatorics wherever you distribute n objects into labeled categories. They generalize the binomial coefficient's "n choose k" to "n divided into k groups of sizes n₁, n₂, ..., nₖ." Notice that C(n, k) is a special case: n!/(k!(n−k)!) is exactly the multinomial coefficient for k = 2 with group sizes k and n−k. When you proceed to the inclusion-exclusion principle, multinomial coefficients will appear again — the principle repeatedly counts and subtracts arrangements of items distributed across overlapping sets, which is precisely what multinomial coefficients measure.

---
id: multinomial-theorem
title: The Multinomial Theorem and Multinomial Coefficients
domain: mathematics
course: discrete-math
prerequisites:
- id: binomial-coefficients
  type: hard
- id: derangements
  type: soft
- id: binomial-theorem-discrete
  type: soft
builds-toward:
- inclusion-exclusion-principle
tags:
- combinatorics
- multinomial
stage: formal-systems
status: validated
---
# The Multinomial Theorem and Multinomial Coefficients

## Core Idea
The multinomial theorem generalizes the binomial theorem to (x₁ + x₂ + ⋯ + xₖ)^n. Multinomial coefficients n!/(n₁!n₂!⋯nₖ!) count the ways to partition n items into k labeled groups of specified sizes.

## Questions

```yaml
- question: "How many distinct arrangements are there of the letters in the word MISSISSIPPI (11 letters: 1 M, 4 I, 4 S, 2 P)?"
  type: multiple-choice
  options:
    - "11! = 39,916,800 (treating all letters as distinct)"
    - "11! / (4! × 4!) = 6,930 (forgetting to account for M and P)"
    - "11! / (1! × 4! × 4! × 2!) = 34,650"
    - "C(11,4) × C(7,4) = 11,550 (choosing positions for just two letter types)"
  answer: 2
  explanation: "The multinomial coefficient n!/(n₁!n₂!⋯nₖ!) counts arrangements of n objects where n₁ are of type 1, n₂ of type 2, etc. Here n=11, with groups 1M, 4I, 4S, 2P: 11!/(1!×4!×4!×2!) = 39,916,800/1,152 = 34,650. Option A overcounts by treating identical letters as distinct. Option B forgets to divide by 1! and 2! for M and P. Option D only accounts for two letter types instead of all four."

- question: "The binomial coefficient C(n, k) is a special case of the multinomial coefficient. Under what conditions does the multinomial coefficient reduce to C(n, k)?"
  type: multiple-choice
  options:
    - "When n is even"
    - "When all variables in the expansion are set equal to 1"
    - "When there are exactly two groups, of sizes k and n−k, so the multinomial coefficient becomes n!/(k!(n−k)!)"
    - "When the exponents n₁, n₂, ..., nₖ are all equal"
  answer: 2
  explanation: "C(n,k) = n!/(k!(n−k)!) is exactly the multinomial coefficient for k=2 groups of sizes k and n−k. The multinomial generalizes this to any number of groups. Setting all variables equal to 1 in the multinomial theorem gives the identity that all multinomial coefficients sum to kⁿ — useful, but a different relationship. Equal exponents produce a special class of terms but don't recover the binomial coefficient in general."

- question: "The multinomial coefficient n!/(n₁!n₂!⋯nₖ!) gives both the number of ways to arrange n objects when nᵢ are of type i AND the coefficient of x₁^n₁ x₂^n₂ ⋯ xₖ^nₖ in the expansion of (x₁ + x₂ + ⋯ + xₖ)^n."
  type: true-false
  answer: true
  explanation: "Both interpretations use the same combinatorial reasoning. When expanding (x₁ + ⋯ + xₖ)^n, a term x₁^n₁ ⋯ xₖ^nₖ arises from choosing which of the n factors contribute each variable — the number of such choices is exactly the multinomial coefficient. This is also the number of ways to arrange n objects when n₁ are indistinguishable type-1, n₂ are indistinguishable type-2, etc. The combinatorial structure is identical."

- question: "The multinomial theorem only applies when the number of variables equals the exponent — that is, (x₁ + x₂ + ⋯ + xₖ)^n requires k = n."
  type: true-false
  answer: false
  explanation: "There is no requirement that k = n. k is the number of variables (terms in the sum) and n is the exponent; they are independent. For example, (x + y + z)^2 has k=3 variables and n=2, and it expands as x² + y² + z² + 2xy + 2xz + 2yz using multinomial coefficients 2!/(2!0!0!) = 1 for pure squares and 2!/(1!1!0!) = 2 for mixed terms. The constraint is only that n₁ + n₂ + ⋯ + nₖ = n for each term."

- question: "Explain why the multinomial coefficient n!/(n₁!n₂!⋯nₖ!) correctly counts the number of distinct arrangements of n objects when nᵢ objects of each type i are identical."
  type: short-answer
  answer: "Start by imagining all n objects are distinct: there are n! total arrangements. But objects of the same type are indistinguishable, so each unique arrangement is overcounted. Specifically, any arrangement is counted n₁! times (because the n₁ identical type-1 objects can be permuted among themselves without creating a new arrangement), and similarly n₂! times for type-2 objects, and so on. Dividing by each nᵢ! removes this overcounting, leaving n!/(n₁!n₂!⋯nₖ!) distinct arrangements."
  explanation: "This is the 'division by overcounting' principle. The anagram formula works by the same logic: MISSISSIPPI has 11! arrangements if all letters are labeled, but swapping the four S's among themselves gives the same word, so we divide by 4!; same for I's (4!) and P's (2!) and M (1!). This principle recurs throughout combinatorics: count all arrangements, identify the symmetries (permutations of identical objects), divide by their count."
```

## Explainer

You already know the **binomial theorem**: (x + y)^n = Σ C(n,k) xᵏ yⁿ⁻ᵏ, where C(n,k) = n!/(k!(n−k)!). The coefficient C(n,k) counts the number of ways to choose k of the n factors to contribute an x, while the remaining n−k factors contribute a y. The multinomial theorem is the same idea with more than two choices.

When you expand (x + y + z)^3, you are choosing — for each of the 3 factors — whether to pick x, y, or z. A term like x²yz¹ arises when exactly 2 factors contribute x, 1 contributes y, and 0 contribute z — wait, let's say the exponents are n₁ = 2, n₂ = 0, n₃ = 1 to be precise. The **multinomial coefficient** n!/(n₁!n₂!...nₖ!) counts the number of ways to assign roles to the n factors: it equals the number of ways to arrange n objects where n₁ are of type 1, n₂ of type 2, and so on. This is the same formula you use to count anagrams: the word MISSISSIPPI has 11 letters with 1 M, 4 I's, 4 S's, and 2 P's, so there are 11!/(1!4!4!2!) = 34,650 distinct arrangements.

The full **multinomial theorem** states: (x₁ + x₂ + ⋯ + xₖ)^n = Σ [n!/(n₁!n₂!⋯nₖ!)] x₁^n₁ x₂^n₂ ⋯ xₖ^nₖ, where the sum runs over all tuples (n₁, n₂, ..., nₖ) of non-negative integers with n₁ + n₂ + ⋯ + nₖ = n. This is a direct extension of the binomial case with k = 2. As a check: setting x₁ = x₂ = ⋯ = xₖ = 1, the left side becomes kⁿ and the right side sums all multinomial coefficients — this gives a useful identity.

Multinomial coefficients appear throughout combinatorics wherever you distribute n objects into labeled categories. They generalize the binomial coefficient's "n choose k" to "n divided into k groups of sizes n₁, n₂, ..., nₖ." Notice that C(n, k) is a special case: n!/(k!(n−k)!) is exactly the multinomial coefficient for k = 2 with group sizes k and n−k. When you proceed to the inclusion-exclusion principle, multinomial coefficients will appear again — the principle repeatedly counts and subtracts arrangements of items distributed across overlapping sets, which is precisely what multinomial coefficients measure.

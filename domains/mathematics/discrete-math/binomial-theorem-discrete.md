---
id: binomial-theorem-discrete
title: Binomial Theorem and Binomial Coefficients
domain: mathematics
course: discrete-math
prerequisites:
- id: combinations-selections-discrete
  type: hard
- id: binomial-theorem
  type: soft
builds-toward:
- generating-functions-basics
- inclusion-exclusion-advanced
tags:
- binomial
- expansion
- Pascal
- coefficients
stage: formal-systems
status: draft
---

# Binomial Theorem and Binomial Coefficients

## Core Idea
The binomial theorem states (x + y)ⁿ = Σ C(n, k)·xⁿ⁻ᵏ·yᵏ. The binomial coefficients C(n, k) appear in Pascal's triangle and count n-bit strings with exactly k ones. This theorem links algebra and combinatorics powerfully.

## How It's Best Learned
Verify the expansion for small n by hand. See the combinatorial interpretation: C(n, k) counts k-element subsets. Use binomial identities like Σ C(n, k) = 2ⁿ and the hockey-stick identity.

## Common Misconceptions
Binomial coefficients are symmetric: C(n, k) = C(n, n−k). The sum of a row in Pascal's triangle is 2ⁿ, not some other formula.

## Explainer

The binomial theorem connects two seemingly different worlds: algebra and combinatorics. You already know that C(n, k) counts the number of k-element subsets of an n-element set. The binomial theorem reveals that these same counts appear as the coefficients when you expand (x + y)ⁿ.

Think about why. When you multiply (x + y)(x + y)(x + y) — three factors — each term in the expansion comes from picking either x or y from each factor. To get x²y, you must pick x from two factors and y from one. There are C(3, 1) = 3 ways to choose which factor contributes the y. So the x²y term has coefficient 3. In general, the coefficient of xⁿ⁻ᵏyᵏ in (x + y)ⁿ is C(n, k), because you're choosing which k of the n factors contribute a y.

**Pascal's triangle** makes this concrete. Each row lists the coefficients of (x + y)ⁿ for increasing n. The Pascal identity C(n, k) = C(n−1, k−1) + C(n−1, k) mirrors the algebraic fact that each entry is the sum of the two above it. The combinatorial proof is clean: from n elements, either you include element n in your k-subset (then choose k−1 from the remaining n−1), or you don't (choose all k from n−1). Both identities — algebraic and combinatorial — describe the same arithmetic.

Two special substitutions unlock powerful identities. Setting x = y = 1 gives (1 + 1)ⁿ = Σ C(n, k), yielding the identity that the sum of all binomial coefficients in row n equals 2ⁿ — the total number of subsets of an n-element set. Setting x = 1, y = −1 gives 0 = Σ (−1)ᵏ C(n, k), showing that the even-indexed and odd-indexed coefficients cancel in equal measure. These substitution techniques will reappear as a core tool in generating functions and inclusion-exclusion, where plugging in specific values extracts combinatorial information from algebraic identities.

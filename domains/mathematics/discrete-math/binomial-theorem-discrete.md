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

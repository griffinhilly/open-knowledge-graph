---
id: vandermonde-identity
title: Vandermonde's Identity
domain: mathematics
course: discrete-math
prerequisites:
- id: binomial-coefficients
  type: hard
- id: combinations
  type: hard
tags:
- combinatorics
- binomial-coefficients
- identities
stage: formal-systems
status: draft
---

# Vandermonde's Identity

## Core Idea
Vandermonde's identity states that C(m+n, r) = Σ C(m, k) × C(n, r-k). It counts ways to choose r items from two groups of sizes m and n. This identity connects binomial coefficients and has applications in probability and counting problems.

## How It's Best Learned
Derive it combinatorially by thinking of choosing r items from two combined groups. Verify with small values numerically.

## Common Misconceptions
- Treating the indices incorrectly in the summation. - Forgetting that k ranges only over valid values where both C(m,k) and C(n,r-k) are non-zero.

## Questions

```yaml
- question: "Vandermonde's identity states C(m+n, r) = Σₖ C(m,k)·C(n,r−k). Which reasoning best justifies why this equality holds?"
  type: multiple-choice
  options:
    - "The left side and right side are both polynomials in m and n that happen to be equal by coincidence"
    - "Both sides count the same thing: the number of ways to choose r items from two groups of m and n by partitioning the selection between the groups in all possible ways"
    - "The identity follows from applying Pascal's rule repeatedly to the left side"
    - "Binomial coefficients are symmetric, so the product of two of them always simplifies"
  answer: 1
  explanation: "The combinatorial argument is the heart of the identity: choosing r items from m+n is equivalent to choosing k from the first group and r−k from the second, for every valid k, and summing. Both sides count exactly the same selections. This two-group counting argument is more illuminating than algebraic verification because it explains *why* the identity is true."

- question: "You need to compute Σₖ₌₀^{8} C(8,k)². Which value does Vandermonde's identity imply this equals?"
  type: multiple-choice
  options:
    - "C(16,8)"
    - "2^8"
    - "C(8,4)²"
    - "C(16,4)"
  answer: 0
  explanation: "Setting m = n = r = 8 in Vandermonde's identity gives Σ C(8,k)·C(8,8−k) = C(16,8). Since C(8,8−k) = C(8,k) by symmetry of binomial coefficients, this becomes Σ C(8,k)² = C(16,8). This is the special case C(2n,n) = Σₖ C(n,k)² — a striking result most easily seen through the two-group counting argument."

- question: "When computing Σₖ C(m,k)·C(n,r−k), you must carefully identify which values of k give nonzero terms before summing, since out-of-range terms could corrupt the result."
  type: true-false
  answer: false
  explanation: "C(m,k) = 0 whenever k < 0 or k > m, and C(n,r−k) = 0 whenever r−k < 0 or r−k > n. Out-of-range terms automatically contribute 0 to the sum. You can let k run from 0 to r (or even over all integers) without tracking bounds — the out-of-range cases vanish on their own. This is one of the practical conveniences of working with binomial coefficients."

- question: "Vandermonde's identity can be derived by multiplying the generating functions (1+x)^m and (1+x)^n and comparing coefficients of x^r on both sides."
  type: true-false
  answer: true
  explanation: "(1+x)^m · (1+x)^n = (1+x)^{m+n}. The coefficient of x^r on the right is C(m+n,r). On the left, multiplying the two power series gives Σₖ C(m,k)·C(n,r−k) as the coefficient of x^r. So the two expressions must be equal — this is the generating function proof. It connects the identity to a broader algebraic framework beyond just combinatorial counting."

- question: "Explain in your own words why the combinatorial proof of Vandermonde's identity is more illuminating than algebraically verifying that both sides are equal."
  type: short-answer
  answer: "The combinatorial proof reveals *why* the identity is true: both sides count the same thing — the ways to choose r items from two groups — through two different but equivalent methods. Algebraic verification confirms the formula is correct but doesn't explain the underlying structure. Understanding the combinatorial reason also extends your ability to recognize similar two-group counting arguments in new problems and to generalize the identity."
  explanation: "A proof that explains 'why' builds intuition and transferable reasoning; a proof that only confirms 'that' leaves the result as a formula to memorize. The combinatorial argument is the insight; the algebra is just a check."
```

## Explainer

Vandermonde's identity answers a natural question: if you have two separate groups — say m red balls and n blue balls — and you want to choose r balls total, how many ways are there? You already know from your work with combinations that choosing r items from a combined pool of m+n gives C(m+n, r). Vandermonde's identity says you can also count by considering every possible split: take k from the red group (C(m,k) ways) and r−k from the blue group (C(n,r−k) ways), then sum over all valid values of k. Both methods count the same selections, so they must be equal: C(m+n, r) = Σₖ C(m,k) · C(n,r−k).

The range of k in the summation is limited by what makes sense: k can't exceed m (you can't take more red balls than exist) and r−k can't exceed n. But you don't need to track these bounds carefully in practice, because C(m,k) = 0 whenever k > m or k < 0, and similarly C(n,r−k) = 0 whenever r−k > n. So you can let k run from 0 to r and the out-of-range terms simply contribute 0.

A useful special case is C(2n, n) = Σₖ C(n,k)². This follows by setting m = n and r = n in Vandermonde's identity, then noting that C(n, n−k) = C(n,k). It tells you that the number of ways to choose n items from 2n equals the sum of squares of the binomial coefficients in the nth row of Pascal's triangle. For instance, C(6,3) = 20 and 1² + 3² + 3² + 1² = 1 + 9 + 9 + 1 = 20. This is a striking identity that is difficult to prove algebraically but nearly obvious from the two-group counting argument.

Vandermonde's identity is also the combinatorial heart of the generating function proof you may encounter later. The generating function (1+x)^m has C(m,k) as the coefficient of xᵏ; similarly (1+x)^n has C(n,j) as the coefficient of xʲ. Multiplying these two power series and collecting the coefficient of xʳ on both sides — from (1+x)^{m+n} = C(m+n,r) and from the product as Σ C(m,k)·C(n,r−k) — gives Vandermonde's identity directly. The combinatorial proof builds intuition; the algebraic proof via generating functions connects it to a broader toolset.

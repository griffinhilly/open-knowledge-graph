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
status: validated
---

# Binomial Theorem and Binomial Coefficients

## Core Idea
The binomial theorem states (x + y)ⁿ = Σ C(n, k)·xⁿ⁻ᵏ·yᵏ. The binomial coefficients C(n, k) appear in Pascal's triangle and count n-bit strings with exactly k ones. This theorem links algebra and combinatorics powerfully.

## How It's Best Learned
Verify the expansion for small n by hand. See the combinatorial interpretation: C(n, k) counts k-element subsets. Use binomial identities like Σ C(n, k) = 2ⁿ and the hockey-stick identity.

## Common Misconceptions
Binomial coefficients are symmetric: C(n, k) = C(n, n−k). The sum of a row in Pascal's triangle is 2ⁿ, not some other formula.

## Questions

```yaml
- question: "In expanding (x + y)^5, why does the term x^3y^2 have coefficient C(5,2) = 10?"
  type: multiple-choice
  options:
    - "Because 5 × 4 / 2! = 10 counts the arrangements of 3 x's and 2 y's in a string of length 5"
    - "Because each term comes from choosing which 2 of the 5 factors contribute y, and there are C(5,2) = 10 such choices"
    - "Because degree-5 terms always appear with coefficient 10 by the symmetry of Pascal's triangle"
    - "Because the Pascal identity gives C(5,2) = C(4,1) + C(4,2) = 4 + 6 = 10 without needing a deeper reason"
  answer: 1
  explanation: "When you multiply five factors of (x+y), each term arises by choosing x or y from each factor independently. To get x^3y^2, you pick y from exactly 2 of the 5 factors — choosing which 2 factors contribute the y. There are C(5,2) = 10 ways to choose that 2-element subset. Option A gives the right number but as a formula, not the combinatorial reason. Option D is valid arithmetic but doesn't explain why that coefficient appears in the expansion."

- question: "Setting x = y = 1 in the binomial theorem produces an identity. What does that identity count, combinatorially?"
  type: multiple-choice
  options:
    - "The total number of permutations of an n-element set, which is n!"
    - "The total number of subsets of an n-element set, which is 2^n — each subset corresponds to choosing which elements to include"
    - "The number of ways to choose 2 elements from an n-element set, which is C(n,2)"
    - "The sum of the first n natural numbers, which is n(n+1)/2"
  answer: 1
  explanation: "Setting x = y = 1 gives (1+1)^n = 2^n = Σ C(n,k). So the sum of all binomial coefficients in row n is 2^n. Combinatorially, each C(n,k) counts the k-element subsets of an n-element set, and summing over all k counts every subset of every size — there are exactly 2^n subsets total, one for each binary include/exclude decision per element."

- question: "The coefficient of x^(n-k)y^k in the expansion of (x + y)^n equals the number of k-element subsets of an n-element set."
  type: true-false
  answer: true
  explanation: "This is the combinatorial heart of the binomial theorem. Each term in the expansion comes from choosing x or y from each of the n factors. The x^(n-k)y^k term arises by choosing y from exactly k of the n factors — a k-element subset of the n factors. There are C(n,k) such subsets, so C(n,k) is the coefficient. The algebra and the combinatorics describe the same counting problem."

- question: "The binomial coefficients are asymmetric: in general, C(n,k) ≠ C(n, n−k)."
  type: true-false
  answer: false
  explanation: "C(n,k) = C(n, n−k) always — the symmetry visible in every palindromic row of Pascal's triangle. Choosing k elements to include in a subset is equivalent to choosing the n−k elements to exclude; both choices define the same subset. So C(8,3) = C(8,5) = 56. Students who forget this symmetry may waste computation, and it also underlies the fact that Pascal's triangle reads the same forwards and backwards."

- question: "Why does substituting x = 1 and y = −1 into the binomial theorem show that any nonempty set has equally many even-sized and odd-sized subsets?"
  type: short-answer
  answer: "Substituting gives (1−1)^n = 0 = Σ (−1)^k C(n,k) = C(n,0) − C(n,1) + C(n,2) − .... Rearranging: C(n,0) + C(n,2) + ... = C(n,1) + C(n,3) + ..., meaning the sum of even-indexed coefficients equals the sum of odd-indexed ones. Since the total is 2^n, each half equals 2^(n−1) — exactly half the subsets have even size and half have odd size."
  explanation: "This substitution technique extracts combinatorial information from algebraic identities. The 0 on the left forces positive and negative terms to cancel exactly — a non-obvious result that becomes transparent once written as a polynomial identity. The technique generalizes: plugging in roots of unity extracts residue-class information about coefficients, which is a core tool in generating functions and inclusion-exclusion."
```

## Explainer

The binomial theorem connects two seemingly different worlds: algebra and combinatorics. You already know that C(n, k) counts the number of k-element subsets of an n-element set. The binomial theorem reveals that these same counts appear as the coefficients when you expand (x + y)ⁿ.

Think about why. When you multiply (x + y)(x + y)(x + y) — three factors — each term in the expansion comes from picking either x or y from each factor. To get x²y, you must pick x from two factors and y from one. There are C(3, 1) = 3 ways to choose which factor contributes the y. So the x²y term has coefficient 3. In general, the coefficient of xⁿ⁻ᵏyᵏ in (x + y)ⁿ is C(n, k), because you're choosing which k of the n factors contribute a y.

**Pascal's triangle** makes this concrete. Each row lists the coefficients of (x + y)ⁿ for increasing n. The Pascal identity C(n, k) = C(n−1, k−1) + C(n−1, k) mirrors the algebraic fact that each entry is the sum of the two above it. The combinatorial proof is clean: from n elements, either you include element n in your k-subset (then choose k−1 from the remaining n−1), or you don't (choose all k from n−1). Both identities — algebraic and combinatorial — describe the same arithmetic.

Two special substitutions unlock powerful identities. Setting x = y = 1 gives (1 + 1)ⁿ = Σ C(n, k), yielding the identity that the sum of all binomial coefficients in row n equals 2ⁿ — the total number of subsets of an n-element set. Setting x = 1, y = −1 gives 0 = Σ (−1)ᵏ C(n, k), showing that the even-indexed and odd-indexed coefficients cancel in equal measure. These substitution techniques will reappear as a core tool in generating functions and inclusion-exclusion, where plugging in specific values extracts combinatorial information from algebraic identities.

---
id: supremum-infimum
title: Supremum and Infimum
domain: mathematics
course: real-analysis
prerequisites:
- id: ordered-field-axioms
  type: hard
builds-toward:
- completeness-axiom
- archimedean-property
- monotone-convergence-theorem
tags:
- supremum
- infimum
- bounds
- real-numbers
stage: advanced
status: draft
---

# Supremum and Infimum

## Core Idea
The supremum (least upper bound) of a set S is the smallest real number that is greater than or equal to every element of S; the infimum (greatest lower bound) is the largest real number that is less than or equal to every element. Not every set has a supremum or infimum, but the completeness axiom guarantees their existence for non-empty bounded sets.

## Questions

```yaml
- question: "Let S = {x ∈ ℝ : x < 1}. What is the supremum of S?"
  type: multiple-choice
  options:
    - "There is no supremum because S has no maximum element"
    - "0.999... (repeating), the largest number in S"
    - "1, because it is the least upper bound of S even though 1 ∉ S"
    - "2, because it is a convenient upper bound that is easy to verify"
  answer: 2
  explanation: "The supremum is 1. Every element of S satisfies x < 1, so 1 is an upper bound. Moreover, 1 is the *least* upper bound: any number smaller than 1, say 0.99, fails to be an upper bound because S contains numbers strictly between 0.99 and 1. The crucial point is that the supremum does NOT need to be in the set — S has no maximum, but it does have a supremum. Option A confuses supremum with maximum. Option D gives an upper bound but not the least one. In the reals, 0.999... = 1, so there is no 'largest element less than 1.'"

- question: "Which of the following sets has a supremum but no maximum?"
  type: multiple-choice
  options:
    - "{1, 2, 3, 4, 5}"
    - "{x ∈ ℝ : x ≤ 2}"
    - "{x ∈ ℝ : x < 2}"
    - "{1, 2, 3, 4, ...} (the natural numbers)"
  answer: 2
  explanation: "The open half-line {x ∈ ℝ : x < 2} has supremum 2 (the smallest upper bound) but no maximum, since 2 is not in the set and for any x in S there exists a larger element still in S. Option A has maximum 5 = supremum 5 (maximum exists). Option B has maximum 2 = supremum 2 (2 ∈ S, so maximum exists). Option D is unbounded above, so it has no supremum at all. Option C is the paradigmatic example of a bounded set with a supremum but no maximum."

- question: "The supremum of a set S is always a member of S."
  type: true-false
  answer: false
  explanation: "The supremum (least upper bound) may or may not belong to S. If the supremum is in S, it equals the maximum. But sets can have a supremum without a maximum — for example, the open interval (0, 1) has supremum 1, but 1 is not in the interval. A maximum is an element of the set that is at least as large as all other elements; a supremum is the greatest lower bound on upper bounds and need not be an element. Confusing the two is one of the most common early errors in real analysis."

- question: "Every non-empty subset of the real numbers that is bounded above has a supremum in ℝ."
  type: true-false
  answer: true
  explanation: "This is the completeness axiom (least upper bound property) of the reals, and it is what distinguishes ℝ from ℚ. The rationals lack this property: the set {q ∈ ℚ : q² < 2} is bounded above in ℚ (e.g., by 2) but has no supremum in ℚ, because its least upper bound is √2, which is irrational. The completeness of ℝ guarantees no such gaps exist — every non-empty bounded set has a least upper bound in ℝ. This property is the foundation for all of real analysis."

- question: "What is the difference between the supremum and the maximum of a set? Give an example of a set that has a supremum but no maximum."
  type: short-answer
  answer: "The maximum of a set S is the largest element that actually belongs to S — it is both an upper bound and a member of S. The supremum is the smallest real number greater than or equal to every element of S; it need not be in S. If the supremum is in S, it equals the maximum; if not, the set has no maximum. Example: the open interval S = (0, 1) = {x ∈ ℝ : 0 < x < 1} has supremum 1 (the smallest upper bound) but no maximum, since 1 ∉ S and for any x ∈ S there exists a larger element of S."
  explanation: "This distinction matters throughout real analysis. Many naturally arising sets — open intervals, level sets of continuous functions — have suprema but no maxima. The completeness axiom guarantees that suprema always exist for non-empty bounded subsets of ℝ, which is the bedrock property that makes limits, continuity, and convergence proofs work."
```

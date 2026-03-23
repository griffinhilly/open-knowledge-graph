---
id: supremum-and-infimum
title: Supremum and Infimum
domain: mathematics
course: real-analysis
prerequisites:
- id: completeness-axiom-lub
  type: hard
builds-toward:
- archimedean-property
- density-of-rationals
- epsilon-n-convergence
tags:
- bounds
- supremum
- infimum
stage: advanced
status: validated
---

# Supremum and Infimum

## Core Idea
The supremum (least upper bound) and infimum (greatest lower bound) are dual concepts that generalize the maximum and minimum. For any bounded set S, sup(S) is the smallest number ≥ all elements of S, and inf(S) is the largest number ≤ all elements of S. These always exist in ℝ by completeness, even when no maximum or minimum does.

## Questions

```yaml
- question: "Let S = {1 − 1/n : n ∈ ℕ} = {0, 1/2, 2/3, 3/4, ...}. What is sup(S)?"
  type: multiple-choice
  options:
    - "1, because every element of S is strictly less than 1 and we can get arbitrarily close to 1 from within S"
    - "There is no supremum because 1 is not an element of S"
    - "The supremum does not exist because the sequence is infinite"
    - "3/4, the largest element listed explicitly in the set description"
  answer: 0
  explanation: "The supremum is the least upper bound — the smallest value that is ≥ every element of S. Every element of S is less than 1, so 1 is an upper bound. For any ε > 0, choosing n large enough gives 1 − 1/n > 1 − ε, so we can get within ε of 1 from inside S — meaning no number smaller than 1 could be an upper bound. Therefore sup(S) = 1. The fact that 1 ∉ S is irrelevant: the supremum need not be in the set. Option B is the classic confusion between supremum and maximum."

- question: "A student argues: 'The open interval (0, 1) has no supremum because it has no maximum — for any x in (0,1), I can always find something larger in the set.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing is wrong — if the maximum doesn't exist, neither does the supremum"
    - "The student confuses supremum with maximum; the supremum is the least upper bound, which equals 1 even though 1 ∉ (0, 1) and no maximum exists"
    - "The interval does contain its maximum — it is the limit of the sequence 1 − 1/n, which 'reaches' 1"
    - "The student correctly identifies that no supremum exists, but for the wrong reason — open intervals never have suprema"
  answer: 1
  explanation: "The supremum and maximum are different concepts. A maximum must be an element of the set that is ≥ all other elements. A supremum is the least upper bound — it must be ≥ all elements of S, but need not belong to S. The open interval (0, 1) has no maximum (you can always find a larger element inside), but its supremum is 1 — the smallest number that every element of (0,1) stays below. The completeness axiom guarantees this supremum exists in ℝ even without a maximum."

- question: "The supremum of a bounded nonempty set in ℝ always exists, but may not be an element of the set."
  type: true-false
  answer: true
  explanation: "This is the content of the Least Upper Bound Property (completeness axiom of ℝ): every nonempty subset of ℝ that is bounded above has a supremum in ℝ. The supremum may or may not belong to the set — it is the sup if the set attains it (maximum), and it is outside the set otherwise (as in open intervals or sets like {1 − 1/n : n ∈ ℕ}). Completeness guarantees existence; nothing guarantees membership."

- question: "If a set S has no maximum element, then S has no supremum."
  type: true-false
  answer: false
  explanation: "The supremum (least upper bound) and the maximum are distinct. A maximum is an element of S that is ≥ all others — it must belong to S. The supremum is the least upper bound — it need not belong to S. By completeness of ℝ, every bounded nonempty set has a supremum, whether or not it has a maximum. The open interval (0, 1) has no maximum but has supremum 1. The set {1 − 1/n : n ∈ ℕ} has no maximum but has supremum 1."

- question: "State the epsilon characterization of the supremum and explain why condition (2) — 'for every ε > 0, there exists s ∈ S with s > sup(S) − ε' — is necessary to distinguish the supremum from just any upper bound."
  type: short-answer
  answer: "A value x = sup(S) if and only if: (1) x ≥ s for all s ∈ S (x is an upper bound), and (2) for every ε > 0, there exists s ∈ S with s > x − ε (x is the *least* upper bound). Condition (1) alone would be satisfied by any upper bound — for example, 100 is an upper bound of (0, 1) satisfying condition (1). Condition (2) rules out all upper bounds that are too large: it says you can always find an element of S within ε of x, so no number smaller than x could be an upper bound. Together, the two conditions uniquely characterize the smallest upper bound."
  explanation: "The epsilon structure in condition (2) — 'for every ε > 0, there exists...' — is the same quantifier pattern that appears throughout real analysis in convergence definitions. Recognizing it here builds the template for epsilon-delta arguments in limits and continuity."
```

## Explainer

You have studied the completeness axiom — the Least Upper Bound Property — which guarantees that every nonempty subset of ℝ that is bounded above has a **supremum** in ℝ. Now let us build intuition for why this is necessary and what these concepts actually mean.

Consider the set S = (0, 1) — the open interval. Does it have a maximum? No: for any x ∈ S, the point (x + 1)/2 is also in S and larger than x, so no element of S is the greatest. Yet the set is clearly bounded above; we intuitively know 1 is the "ceiling." The **supremum** captures this ceiling precisely: sup(S) = 1, even though 1 ∉ S. The sup is the smallest number that every element of S stays at or below. Similarly, inf(S) = 0 even though 0 ∉ S. The supremum and infimum always exist in ℝ for bounded nonempty sets — this is completeness — even when no actual maximum or minimum is attained.

The epsilon characterization makes the definition operational: x = sup(S) if and only if (1) x ≥ s for all s ∈ S, and (2) for every ε > 0, there exists s ∈ S with s > x − ε. Condition (1) says x is an upper bound. Condition (2) says x is the *least* such bound: you can get arbitrarily close to x from within S, so no smaller value could work as an upper bound. This "for every ε, there exists..." language is the same structure you will use throughout convergence proofs — recognizing it here builds the template.

Why does analysis need sup and inf? Because many important arguments require talking about "the best possible bound" without assuming that bound is attained. The **Extreme Value Theorem** uses sup to guarantee a continuous function on a closed interval achieves its maximum: the argument constructs sup{f(x)} and shows the sup is actually attained. **Cauchy sequence** convergence is proved by constructing a candidate limit as a supremum of a carefully chosen set. The **density of rationals** (your next topic) is proved using the Archimedean property, which itself follows from properties of sup applied to the natural numbers. Supremum and infimum are not just definitions — they are the working tools of real analysis, present in nearly every proof you will encounter.

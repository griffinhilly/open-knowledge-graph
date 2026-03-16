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
status: draft
---

# Supremum and Infimum

## Core Idea
The supremum (least upper bound) and infimum (greatest lower bound) are dual concepts that generalize the maximum and minimum. For any bounded set S, sup(S) is the smallest number ≥ all elements of S, and inf(S) is the largest number ≤ all elements of S. These always exist in ℝ by completeness, even when no maximum or minimum does.

## Explainer

You have studied the completeness axiom — the Least Upper Bound Property — which guarantees that every nonempty subset of ℝ that is bounded above has a **supremum** in ℝ. Now let us build intuition for why this is necessary and what these concepts actually mean.

Consider the set S = (0, 1) — the open interval. Does it have a maximum? No: for any x ∈ S, the point (x + 1)/2 is also in S and larger than x, so no element of S is the greatest. Yet the set is clearly bounded above; we intuitively know 1 is the "ceiling." The **supremum** captures this ceiling precisely: sup(S) = 1, even though 1 ∉ S. The sup is the smallest number that every element of S stays at or below. Similarly, inf(S) = 0 even though 0 ∉ S. The supremum and infimum always exist in ℝ for bounded nonempty sets — this is completeness — even when no actual maximum or minimum is attained.

The epsilon characterization makes the definition operational: x = sup(S) if and only if (1) x ≥ s for all s ∈ S, and (2) for every ε > 0, there exists s ∈ S with s > x − ε. Condition (1) says x is an upper bound. Condition (2) says x is the *least* such bound: you can get arbitrarily close to x from within S, so no smaller value could work as an upper bound. This "for every ε, there exists..." language is the same structure you will use throughout convergence proofs — recognizing it here builds the template.

Why does analysis need sup and inf? Because many important arguments require talking about "the best possible bound" without assuming that bound is attained. The **Extreme Value Theorem** uses sup to guarantee a continuous function on a closed interval achieves its maximum: the argument constructs sup{f(x)} and shows the sup is actually attained. **Cauchy sequence** convergence is proved by constructing a candidate limit as a supremum of a carefully chosen set. The **density of rationals** (your next topic) is proved using the Archimedean property, which itself follows from properties of sup applied to the natural numbers. Supremum and infimum are not just definitions — they are the working tools of real analysis, present in nearly every proof you will encounter.

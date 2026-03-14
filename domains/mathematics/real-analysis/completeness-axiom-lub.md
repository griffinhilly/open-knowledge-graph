---
id: completeness-axiom-lub
title: The Completeness Axiom (Least Upper Bound Property)
domain: mathematics
course: real-analysis
prerequisites:
- id: ordered-field-axioms
  type: hard
builds-toward:
- supremum-and-infimum
- monotone-convergence-theorem
tags:
- completeness
- supremum
- axiom
- foundations
stage: abstract-reasoning
status: draft
---

# The Completeness Axiom (Least Upper Bound Property)

## Core Idea
The Completeness Axiom states that every non-empty subset of real numbers bounded above must have a least upper bound (supremum). This single axiom distinguishes the reals from the rationals and is indispensable for proving convergence of sequences, the Intermediate Value Theorem, and the Extreme Value Theorem.

## How It's Best Learned
Start with concrete examples: find the supremum of {1, 1/2, 2/3, 3/4, ...} and verify it's 1. Then explore why the rationals lack this property (e.g., {x ∈ ℚ : x² < 2} has no rational supremum). Use supremum to motivate the next topics.

## Common Misconceptions
- Confusing supremum with maximum: the supremum of (0,1) is 1 but 1 is not in the set.
- Thinking any bounded set has a supremum in its field of view; this is the whole point of the axiom.
- Assuming the supremum is always the 'last' or 'largest' element.

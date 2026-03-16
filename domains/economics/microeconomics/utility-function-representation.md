---
id: utility-function-representation
title: Utility Functions and Preference Representation
domain: economics
course: microeconomics
prerequisites:
- id: consumer-theory-utility
  type: hard
builds-toward:
- duality-consumer-preferences
- demand-system-integrability
tags:
- consumer theory
- preferences
- utility
- representation
stage: abstract-reasoning
status: draft
---

# Utility Functions and Preference Representation

## Core Idea
A utility function u(x) represents a consumer's preferences by assigning numbers to consumption bundles such that bundle A is preferred to B if and only if u(A) > u(B). Different preference orderings can be represented by different utility functions, but only ordinal (ranking) properties matter, not cardinal values. Utility functions exist for rational preferences satisfying completeness and transitivity.

## How It's Best Learned
Start with indifference curves and verify which utility functions generate the same curves. Work through cardinal vs. ordinal utility examples to see why any monotonic transformation preserves preferences.

## Common Misconceptions
- Thinking utility has absolute meaning or units.
- Assuming different utility functions represent different preferences.
- Confusing utility differences (cardinal) with preference orderings (ordinal).

## Explainer

From your study of consumer theory, you know that preferences are characterized by indifference curves: sets of bundles among which the consumer is indifferent. A **utility function** u(x) is a mathematical way to summarize these preferences by assigning a number to each bundle such that bundle A is preferred to B if and only if u(A) > u(B). The function converts a geometric object (a map of indifference curves) into an algebraic one that can be differentiated and optimized, making demand analysis tractable.

The critical insight is that utility numbers carry no absolute meaning. Only the **ordinal ranking** matters — the ordering of bundles, not the magnitude of differences between them. If u(A) = 10 and u(B) = 5, we know A is preferred to B, but we cannot say "A is twice as good as B." Any **monotonic transformation** of u — applying a strictly increasing function like squaring, taking the log, or adding a constant — yields a different utility function that represents exactly the same preferences and traces out identical indifference curves. This is why economists speak of utility functions as representations rather than measurements.

The practical implication is that there is no "correct" utility function for a given preference ordering — there are infinitely many equivalent ones. Cobb-Douglas u = x_1^α · x_2^(1−α) and its log transformation v = α·ln(x_1) + (1−α)·ln(x_2) represent identical preferences. Any demand analysis you perform using one yields identical results using the other. Students sometimes think switching utility functions changes behavior, but indifference curves — not utility numbers — determine choices, and monotonic transformations leave indifference curves unchanged.

Utility functions exist only when preferences satisfy the **rationality axioms**: completeness (any two bundles can be compared) and transitivity (if A ≻ B and B ≻ C, then A ≻ C). Transitivity is the consistency condition that prevents preference cycles. If preferences violate transitivity — a consumer who prefers A to B, B to C, and C to A — no utility function can assign consistent scores to all three bundles. The **representation theorem** formalizes this: continuous preferences that are complete and transitive can always be represented by a continuous utility function. This theorem is the foundation on which all of consumer theory rests: it tells you when it is legitimate to replace an abstract preference ordering with an algebraic function you can work with mathematically.

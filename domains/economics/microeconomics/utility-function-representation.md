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
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A consumer's preferences are represented by u(x₁, x₂) = x₁ · x₂. A colleague proposes switching to v(x₁, x₂) = ln(x₁) + ln(x₂) instead. What is the correct conclusion?"
  type: multiple-choice
  options:
    - "v represents different preferences because ln(x₁) + ln(x₂) ≠ x₁ · x₂ for most bundles"
    - "v is preferable because logarithms are easier to differentiate and optimize"
    - "v represents exactly the same preferences, because ln(x₁ · x₂) = ln(x₁) + ln(x₂), making v a monotonic transformation of u"
    - "v represents different preferences because the utility values differ — for example, u(2,2) = 4 but v(2,2) ≈ 1.39"
  answer: 2
  explanation: "Since ln is strictly increasing, v = ln(u) is a monotonic transformation. Any monotonic transformation of a utility function represents exactly the same preferences: if u(A) > u(B), then ln(u(A)) > ln(u(B)). The indifference curves are identical; only the numerical labels change. Options A and D both make the mistake of treating utility values as having absolute meaning. The scale changes; the underlying preference ordering does not."

- question: "Suppose u(A) = 100 and u(B) = 25 under some utility function. Which of the following is a valid inference?"
  type: multiple-choice
  options:
    - "Bundle A gives four times as much satisfaction as bundle B"
    - "The consumer would trade four units of B for one unit of A at current prices"
    - "Bundle A is preferred to bundle B, but the ratio 100/25 = 4 carries no behavioral meaning"
    - "The consumer is indifferent between A and any bundle with utility value between 25 and 100"
  answer: 2
  explanation: "Utility is ordinal: the numbers encode ranking only, not magnitude. u(A) > u(B) tells us A is preferred to B — full stop. The ratio 4 is meaningless: applying the transformation u → √u gives values 10 and 5 (ratio 2); applying u → u² gives 10,000 and 625 (ratio 16). All three functions represent identical preferences. Statements about 'four times as much satisfaction' presuppose cardinal utility — that differences and ratios between utility values have meaning — which they do not in standard consumer theory."

- question: "Multiplying a utility function by a positive constant produces a new utility function that represents different preferences."
  type: true-false
  answer: false
  explanation: "Multiplying by a positive constant is a monotonic transformation — it preserves the ordering of every pair of bundles. If u(A) > u(B), then 3u(A) > 3u(B). The ranking of all bundles is unchanged, so the indifference curves are identical and the new function represents the same preferences. Only transformations that reverse the ordering (like multiplying by -1) would change which bundles are preferred."

- question: "If two consumers have different utility functions, they must have different underlying preferences."
  type: true-false
  answer: false
  explanation: "The same preference ordering can be represented by infinitely many utility functions — any monotonic transformation of a valid utility function is equally valid. Two consumers might use u₁(x) = x₁x₂ and u₂(x) = x₁²x₂², which look very different but represent identical preferences (u₂ = u₁², a monotonic transformation). Behavior depends on indifference curves — not utility values — and monotonic transformations leave indifference curves unchanged."

- question: "Why is it meaningless to say 'Bundle A gives me 10 utility units and Bundle B gives me 5, so A is twice as good as B'? What can legitimately be concluded from these numbers?"
  type: short-answer
  answer: "Utility is ordinal: the numbers only encode the ranking of bundles, not the intensity of preferences. Any monotonic transformation — squaring, taking the log, multiplying by a constant — gives different numerical values while representing the same preferences. Under u → u², A has 100 units and B has 25 units (now 'four times as good'). The only valid conclusion from u(A) = 10 and u(B) = 5 is that A is preferred to B. Ratios and differences between utility values are arbitrary artifacts of which utility function was chosen."
  explanation: "Cardinal utility — where differences and ratios between utility values have meaning — requires additional assumptions beyond standard consumer theory (such as expected utility over lotteries). In the basic consumer model, only the ordinal ranking matters. The practical implication: any demand analysis is invariant to monotonic transformations. Two researchers using different utility functions for the same preferences make identical predictions about consumer behavior, because they trace the same indifference curves."
```

## Explainer

From your study of consumer theory, you know that preferences are characterized by indifference curves: sets of bundles among which the consumer is indifferent. A **utility function** u(x) is a mathematical way to summarize these preferences by assigning a number to each bundle such that bundle A is preferred to B if and only if u(A) > u(B). The function converts a geometric object (a map of indifference curves) into an algebraic one that can be differentiated and optimized, making demand analysis tractable.

The critical insight is that utility numbers carry no absolute meaning. Only the **ordinal ranking** matters — the ordering of bundles, not the magnitude of differences between them. If u(A) = 10 and u(B) = 5, we know A is preferred to B, but we cannot say "A is twice as good as B." Any **monotonic transformation** of u — applying a strictly increasing function like squaring, taking the log, or adding a constant — yields a different utility function that represents exactly the same preferences and traces out identical indifference curves. This is why economists speak of utility functions as representations rather than measurements.

The practical implication is that there is no "correct" utility function for a given preference ordering — there are infinitely many equivalent ones. Cobb-Douglas u = x_1^α · x_2^(1−α) and its log transformation v = α·ln(x_1) + (1−α)·ln(x_2) represent identical preferences. Any demand analysis you perform using one yields identical results using the other. Students sometimes think switching utility functions changes behavior, but indifference curves — not utility numbers — determine choices, and monotonic transformations leave indifference curves unchanged.

Utility functions exist only when preferences satisfy the **rationality axioms**: completeness (any two bundles can be compared) and transitivity (if A ≻ B and B ≻ C, then A ≻ C). Transitivity is the consistency condition that prevents preference cycles. If preferences violate transitivity — a consumer who prefers A to B, B to C, and C to A — no utility function can assign consistent scores to all three bundles. The **representation theorem** formalizes this: continuous preferences that are complete and transitive can always be represented by a continuous utility function. This theorem is the foundation on which all of consumer theory rests: it tells you when it is legitimate to replace an abstract preference ordering with an algebraic function you can work with mathematically.

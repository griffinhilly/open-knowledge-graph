---
id: integrability-revealed-preference
title: Integrability and Preference Recovery
domain: economics
course: advanced-microeconomics
prerequisites:
- id: revealed-preference-axioms
  type: hard
- id: compensated-demand-curves
  type: hard
tags:
- consumer-theory
- demand
- preferences
stage: expert
status: draft
---

# Integrability and Preference Recovery

## Core Idea
Integrability theory determines when demand functions can be recovered from underlying preferences through integration. The Slutsky matrix must be symmetric and negative semidefinite for consistency with utility-maximizing behavior. This connects observable demand to unobservable preferences through mathematical constraints.

## Questions

```yaml
- question: "An economist estimates demand and finds the cross-substitution effects s₁₂ = 0.3 and s₂₁ = 0.5 (where sᵢⱼ = ∂hᵢ/∂pⱼ, the compensated cross-price effect). What does this asymmetry imply?"
  type: multiple-choice
  options:
    - "The goods are substitutes, since both cross-effects are positive"
    - "The demand system is inconsistent with utility maximization — an asymmetric Slutsky matrix means no utility function can generate this demand"
    - "Income effects are dominating substitution effects, explaining the asymmetry"
    - "The result is plausible and common in empirical work; the Slutsky matrix need not be symmetric"
  answer: 1
  explanation: "Slutsky symmetry (sᵢⱼ = sⱼᵢ) is a necessary condition for integrability — it follows from Young's theorem applied to the expenditure function. If sᵢⱼ ≠ sⱼᵢ, no expenditure function exists whose cross-partials match the observed demand, which means no utility function can rationalize the behavior. An asymmetric Slutsky matrix is a rejection of the utility-maximization hypothesis. Income effects explain asymmetry in uncompensated (Marshallian) demands, but not in compensated (Hicksian) demands, which are what Slutsky entries measure."

- question: "Why must the Slutsky matrix be symmetric for a demand system to be rationalizable by utility maximization?"
  type: multiple-choice
  options:
    - "Symmetry is an empirical regularity imposed by revealed preference axioms, not derived from mathematics"
    - "Hicksian demands are derivatives of the expenditure function, and Young's theorem requires mixed partial derivatives to be equal: ∂²e/∂pᵢ∂pⱼ = ∂²e/∂pⱼ∂pᵢ"
    - "The law of demand requires that all substitution effects be equal across goods"
    - "Consumers must treat symmetric pairs of goods identically for preferences to be well-defined"
  answer: 1
  explanation: "If a utility function exists, the expenditure function e(p, u) can be derived from it. Hicksian demands are hᵢ = ∂e/∂pᵢ, so Slutsky entries are sᵢⱼ = ∂²e/∂pᵢ∂pⱼ. For any smooth function, Young's theorem guarantees these mixed partials are equal. If the observed Slutsky matrix is asymmetric, you cannot construct such an expenditure function — the 'integration back' from demand to preferences fails. This is why symmetry is both necessary and sufficient (with negative semidefiniteness) for rationalizability."

- question: "If the Slutsky conditions (symmetry and negative semidefiniteness) hold for an observed demand system, it is possible to recover a utility function consistent with that demand."
  type: true-false
  answer: true
  explanation: "This is the content of the integrability theorem: the Slutsky conditions are necessary AND sufficient for rationalizability. If both hold, one can integrate the expenditure function from the Hicksian demands, then invert to recover the utility function. The demand system, the expenditure function, and the utility function are three equivalent representations of the same consumer behavior, and the Slutsky conditions are the key that unlocks movement between them."

- question: "A negative semidefinite Slutsky matrix means all cross-substitution effects are negative — all goods are complements."
  type: true-false
  answer: false
  explanation: "Negative semidefiniteness constrains the OWN-price substitution effects: it requires that compensated own-price effects sᵢᵢ ≤ 0 (compensated demand curves slope downward). Cross effects sᵢⱼ can be positive (substitutes) or negative (complements) and are unconstrained by negative semidefiniteness. NSD is a matrix condition on quadratic forms: for any vector v, v'Sv ≤ 0. This is satisfied even when many individual cross-entries are positive."

- question: "What is the integrability problem in consumer theory, and why does Slutsky symmetry determine whether preferences can be recovered from observed demand data?"
  type: short-answer
  answer: "The integrability problem asks: given an observed demand function x(p, m), can we find a utility function that generates it? Starting from demand, we must 'integrate back' to recover the expenditure function and then the utility function. This is only possible if the Slutsky matrix — whose entries are second derivatives of the expenditure function — is symmetric. Asymmetry means no smooth expenditure function exists, so no utility function can rationalize the observed demand. Symmetry (plus negative semidefiniteness) is both necessary and sufficient for the integration to succeed."
  explanation: "Integrability connects the three representations of consumer behavior: utility functions, demand functions, and revealed choice data. The Slutsky conditions are the mathematical bridge. Without symmetry, demand data are inconsistent with optimization — the consumer cannot be modeled as maximizing any stable preference ordering. This makes Slutsky symmetry not just a theoretical nicety but an empirical test of the rationality hypothesis itself."
```

## Explainer

From revealed preference axioms, you know how to test whether observed choices are consistent with utility maximization: if a consumer chose bundle A when B was affordable, they revealed a preference for A over B, and this pattern must be acyclical. **Integrability** asks the continuous version of the same question: given a smooth demand function x(p, m), can we find a utility function that generates it? This is the inverse problem — instead of deriving demand from preferences, we start with demand and work backward to preferences.

The answer hinges on the **Slutsky matrix**, which you encountered when studying compensated demand curves. The Slutsky matrix S has entries s_ij = ∂h_i/∂p_j, where h is Hicksian demand — the substitution effect of a price change holding utility constant. For a demand system to be rationalizable by some utility function, the Slutsky matrix must satisfy two conditions everywhere: it must be **symmetric** (s_ij = s_ji) and **negative semidefinite** (the substitution effect of any price change reduces compensated demand for that good). Symmetry means the cross-substitution effect of good j's price on good i's demand equals the reverse. Negative semidefiniteness means compensated demand curves slope downward.

Why symmetry? It comes from the mathematics of integration. If demand functions are generated by maximizing some utility function, the Hicksian demands are derivatives of the expenditure function: h_i = ∂e/∂p_i. The Slutsky matrix entries are then second derivatives: s_ij = ∂²e/∂p_i∂p_j. By Young's theorem (equality of cross-partials for smooth functions), these must be symmetric. This is exactly the condition needed to "integrate back" from demand to the expenditure function, and from there to the underlying utility. If the Slutsky matrix is asymmetric, no utility function can generate the observed demand — the demand system is fundamentally inconsistent with optimization.

The integrability theorem thus closes the circle between three ways of describing consumer behavior: preferences (ordinal utility), choice behavior (demand functions), and revealed preference (observed purchase data). If the Slutsky conditions hold, you can start from any one of these and recover the others. This matters practically because economists typically observe demand, not utility. Integrability tells you precisely when it is legitimate to estimate a demand system and interpret the results as reflecting coherent underlying preferences — and when the data reject the optimization hypothesis altogether.

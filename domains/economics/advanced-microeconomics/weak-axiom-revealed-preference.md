---
id: weak-axiom-revealed-preference
title: Weak Axiom of Revealed Preference (WARP)
domain: economics
course: advanced-microeconomics
prerequisites:
- id: revealed-preference-theory
  type: hard
builds-toward:
- strong-axiom-revealed-preference
tags:
- rationality
- consistency
- demand-theory
stage: advanced
status: draft
---

# Weak Axiom of Revealed Preference (WARP)

## Core Idea
WARP states that if bundle A is revealed preferred to B at one price vector, then B cannot be revealed preferred to A at any other price vector. This rules out simple cycles in revealed preferences and is weaker than assuming transitivity of preferences, making it a minimal consistency requirement.

## How It's Best Learned
Test WARP with two-period choice data. Show that violations of WARP imply the consumer violates monotonicity or convexity. Work through examples where bundles on the budget line violate WARP.

## Common Misconceptions
Thinking WARP is equivalent to transitivity (it is weaker). Assuming WARP ensures unique demand functions (it does not). Confusing direct and indirect revealed preference.

## Explainer

Revealed preference theory, which you have already studied, starts from a powerful premise: instead of assuming consumers have utility functions, we can infer their preferences from their actual choices. If a consumer chooses bundle A when bundle B was also affordable, then A is **directly revealed preferred** to B. WARP takes this idea and imposes the simplest possible consistency requirement on such choices.

The axiom states: if bundle A is directly revealed preferred to bundle B, then bundle B cannot be directly revealed preferred to bundle A. In concrete terms, suppose you observe a consumer at prices p¹ choosing bundle x¹, and at prices p² choosing bundle x². If x² was affordable at prices p¹ (meaning p¹ · x² ≤ p¹ · x¹) but the consumer chose x¹ instead, then x¹ is revealed preferred to x². WARP says that in this case, x¹ must not have been affordable when the consumer chose x² — that is, p² · x¹ > p² · x². If x¹ were affordable at p² and the consumer still picked x², that would contradict the earlier choice, revealing an inconsistency.

Think of it as a no-flip-flopping rule for two-way comparisons. If you pick steak over chicken when both are on the menu, you should not later pick chicken over steak when both are again available at (possibly different) prices that still make both options feasible. WARP does not, however, rule out longer cycles: you might prefer A to B, B to C, and C to A without violating WARP, because WARP only checks pairwise reversals. This is precisely why WARP is **weaker than transitivity** — transitivity would forbid such a cycle, but WARP does not examine chains of three or more comparisons. The Strong Axiom of Revealed Preference (SARP), which you will encounter next, closes this gap.

WARP has a direct geometric interpretation in two-good settings. When the consumer's budget line pivots due to a price change, WARP constrains where the new choice can fall. If the old bundle is still affordable under the new budget, the new choice must lie on the opposite side of the old budget line from the old choice — otherwise the consumer would be contradicting their earlier decision. This connects WARP to the **Slutsky condition**: satisfying WARP implies the compensated law of demand holds, meaning the substitution effect has the correct sign. In fact, for demand functions (as opposed to demand correspondences), WARP is equivalent to the Slutsky matrix being negative semidefinite, linking the behavioral axiom directly to the calculus-based consumer theory you already know.

The practical importance of WARP is that it gives economists a testable prediction from minimal assumptions. You do not need to know the consumer's utility function, their preferences, or even whether they are "rational" in any deep sense. You simply need choice data at different price-income combinations. If WARP is violated in the data, you know the consumer's behavior cannot be rationalized by any well-behaved utility function — a powerful empirical check that requires no functional form assumptions at all.

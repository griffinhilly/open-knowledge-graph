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

## Questions

```yaml
- question: "At prices p¹, a consumer chooses bundle x¹ = (4, 2) when bundle x² = (2, 4) was also affordable. At prices p², the consumer chooses x² = (2, 4), and x¹ = (4, 2) is also affordable at p². Does this violate WARP?"
  type: multiple-choice
  options:
    - "No — the consumer simply has different preferences at different times, which is not a WARP violation"
    - "Yes — x¹ was directly revealed preferred to x², but then x² was chosen when x¹ was still affordable, which is a direct reversal"
    - "No — WARP only applies when the two bundles cost exactly the same under both price vectors"
    - "Yes — any change in the chosen bundle between two observations violates WARP"
  answer: 1
  explanation: "WARP states: if A is directly revealed preferred to B (A was chosen when B was affordable), then B cannot be directly revealed preferred to A (B cannot be chosen when A is affordable). Here, x¹ was chosen when x² was affordable at p¹, so x¹ is revealed preferred to x². Then x² was chosen at p² when x¹ was still affordable — this is a direct reversal and violates WARP. Option A confuses 'revealed preference' with 'preferences changing over time.' WARP treats observed choices as stable preference signals; if they contradict each other, the behavior is inconsistent."

- question: "A consumer's choice data is consistent with WARP but reveals the pattern: A is revealed preferred to B, B is revealed preferred to C, and C is revealed preferred to A. Has WARP been violated?"
  type: multiple-choice
  options:
    - "Yes — any cycle in revealed preferences violates WARP"
    - "No — WARP only prohibits direct pairwise reversals (e.g., A preferred to B then B preferred to A); a three-way cycle does not involve a direct reversal of any single pair"
    - "Yes — WARP is equivalent to transitivity, so three-way cycles are forbidden by WARP"
    - "No — but only because the consumer is indifferent among A, B, and C"
  answer: 1
  explanation: "WARP checks pairwise consistency only: if A is ever chosen over B, then B can never be chosen over A. A three-way cycle (A ≻ B, B ≻ C, C ≻ A) does not involve any single pair being reversed — each comparison is observed only once in one direction — so WARP is not violated. This is exactly why WARP is weaker than transitivity: transitivity would forbid this cycle (if A ≻ B and B ≻ C, then A ≻ C, contradicting C ≻ A), but WARP does not examine chains of three or more choices."

- question: "WARP is equivalent to transitivity of preferences — both impose the same consistency requirements on choice behavior."
  type: true-false
  answer: false
  explanation: "WARP is strictly weaker than transitivity. WARP rules out direct pairwise reversals: if A is revealed preferred to B, B cannot be revealed preferred to A. Transitivity rules out cycles of any length: if A ≻ B and B ≻ C, then A ≻ C. A consumer can satisfy WARP while exhibiting intransitive cycles (A ≻ B ≻ C ≻ A), since each of those three pairwise comparisons involves a different pair and no single pair is reversed. The Strong Axiom of Revealed Preference (SARP) closes this gap by prohibiting cycles of any length."

- question: "A violation of WARP implies that the consumer's behavior cannot be rationalized by any well-behaved utility function."
  type: true-false
  answer: true
  explanation: "True. A well-behaved utility function produces choices that are always consistent with revealed preference: if A is chosen over B when B is affordable, the utility of A is higher, so B will never be chosen over A when A is affordable. WARP is a necessary condition for rationalizability — any utility-maximizing consumer must satisfy WARP. Conversely, if WARP is violated in observed choice data, no utility function (however constructed) can explain those choices. This is what makes WARP an empirically testable prediction that requires no functional form assumptions."

- question: "What is the key difference between WARP and transitivity, and why does this make WARP a weaker rationality condition?"
  type: short-answer
  answer: "Transitivity requires consistency across chains of comparisons: if A ≻ B and B ≻ C, then A ≻ C must hold. WARP only requires consistency within pairwise comparisons: if A is chosen over B in one observation, B cannot be chosen over A in another. WARP is weaker because it only looks at each pair in isolation — it permits a consumer to exhibit the three-way cycle A ≻ B ≻ C ≻ A without violating any pairwise constraint. Transitivity would forbid this cycle. WARP is the minimum consistency condition for two-observation revealed preference; SARP (Strong Axiom) imposes transitivity across the full revealed preference relation and is equivalent to utility rationalizability in general."
  explanation: "The difference matters practically: WARP can be tested with just two choice observations (two price-budget combinations), making it a minimal and empirically tractable consistency test. Detecting intransitive cycles requires observing choices over three or more situations. The weakness of WARP is both a theoretical limitation and a practical feature."
```

## Explainer

Revealed preference theory, which you have already studied, starts from a powerful premise: instead of assuming consumers have utility functions, we can infer their preferences from their actual choices. If a consumer chooses bundle A when bundle B was also affordable, then A is **directly revealed preferred** to B. WARP takes this idea and imposes the simplest possible consistency requirement on such choices.

The axiom states: if bundle A is directly revealed preferred to bundle B, then bundle B cannot be directly revealed preferred to bundle A. In concrete terms, suppose you observe a consumer at prices p¹ choosing bundle x¹, and at prices p² choosing bundle x². If x² was affordable at prices p¹ (meaning p¹ · x² ≤ p¹ · x¹) but the consumer chose x¹ instead, then x¹ is revealed preferred to x². WARP says that in this case, x¹ must not have been affordable when the consumer chose x² — that is, p² · x¹ > p² · x². If x¹ were affordable at p² and the consumer still picked x², that would contradict the earlier choice, revealing an inconsistency.

Think of it as a no-flip-flopping rule for two-way comparisons. If you pick steak over chicken when both are on the menu, you should not later pick chicken over steak when both are again available at (possibly different) prices that still make both options feasible. WARP does not, however, rule out longer cycles: you might prefer A to B, B to C, and C to A without violating WARP, because WARP only checks pairwise reversals. This is precisely why WARP is **weaker than transitivity** — transitivity would forbid such a cycle, but WARP does not examine chains of three or more comparisons. The Strong Axiom of Revealed Preference (SARP), which you will encounter next, closes this gap.

WARP has a direct geometric interpretation in two-good settings. When the consumer's budget line pivots due to a price change, WARP constrains where the new choice can fall. If the old bundle is still affordable under the new budget, the new choice must lie on the opposite side of the old budget line from the old choice — otherwise the consumer would be contradicting their earlier decision. This connects WARP to the **Slutsky condition**: satisfying WARP implies the compensated law of demand holds, meaning the substitution effect has the correct sign. In fact, for demand functions (as opposed to demand correspondences), WARP is equivalent to the Slutsky matrix being negative semidefinite, linking the behavioral axiom directly to the calculus-based consumer theory you already know.

The practical importance of WARP is that it gives economists a testable prediction from minimal assumptions. You do not need to know the consumer's utility function, their preferences, or even whether they are "rational" in any deep sense. You simply need choice data at different price-income combinations. If WARP is violated in the data, you know the consumer's behavior cannot be rationalized by any well-behaved utility function — a powerful empirical check that requires no functional form assumptions at all.

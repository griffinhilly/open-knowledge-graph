---
id: strong-axiom-revealed-preference
title: Strong Axiom of Revealed Preference (SARP)
domain: economics
course: advanced-microeconomics
prerequisites:
- id: weak-axiom-revealed-preference
  type: hard
tags:
- rationality
- consistency
- preferences
stage: abstract-reasoning
status: draft
---

# Strong Axiom of Revealed Preference (SARP)

## Core Idea
SARP extends WARP to indirect revealed preference: if A is revealed preferred to B either directly or through a chain, then B cannot be revealed preferred to A. SARP is equivalent to the existence of a utility function that rationalizes all observed choices. Satisfying SARP is necessary and sufficient for consistency with neoclassical consumer theory.

## Explainer

From your study of the **Weak Axiom of Revealed Preference (WARP)**, you know that if a consumer chooses bundle A when bundle B was affordable, then A is directly revealed preferred to B, and we should never observe the consumer choosing B when A is also affordable. WARP enforces pairwise consistency: no direct contradictions between any two observed choices. But WARP only checks one link at a time. The **Strong Axiom of Revealed Preference (SARP)** extends this logic to chains of any length.

Imagine three observations: in situation 1, the consumer picks A over affordable B. In situation 2, she picks B over affordable C. In situation 3, she picks C over affordable A. Each pairwise comparison satisfies WARP — no single pair directly contradicts. But following the chain, A is revealed preferred to B, B to C, and C to A, creating a preference cycle. SARP rules this out. It says: if A is revealed preferred to B through any sequence of intermediate choices — directly or indirectly — then B cannot be revealed preferred to A through any chain. In graph theory terms, the **revealed preference relation** must be acyclic.

Why does acyclicity matter so much? Because it is mathematically equivalent to the existence of a well-behaved **utility function** that rationalizes the consumer's choices. If you can assign a number to every bundle such that chosen bundles always get higher numbers than affordable alternatives, you have a utility function. Cycles make this impossible — you cannot rank A above B above C above A with real numbers. SARP is therefore the testable condition for whether observed market behavior is consistent with the entire apparatus of neoclassical consumer theory: utility maximization, well-ordered preferences, and downward-sloping demand.

In practice, SARP gives economists a purely behavioral test. You do not need to ask consumers about their preferences or assume a particular utility function. You simply observe what people buy at different prices and incomes, check whether the revealed preference relation contains any cycles, and if it does not, you know that some utility function could have generated those choices. Violations of SARP in experimental or survey data signal that the standard rational-choice model fails to describe that consumer's behavior — opening the door to behavioral alternatives like reference-dependent preferences or bounded rationality.

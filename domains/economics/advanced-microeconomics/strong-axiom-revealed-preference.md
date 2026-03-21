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
stage: advanced
status: draft
---

# Strong Axiom of Revealed Preference (SARP)

## Core Idea
SARP extends WARP to indirect revealed preference: if A is revealed preferred to B either directly or through a chain, then B cannot be revealed preferred to A. SARP is equivalent to the existence of a utility function that rationalizes all observed choices. Satisfying SARP is necessary and sufficient for consistency with neoclassical consumer theory.

## Questions

```yaml
- question: "A researcher observes three choices: at prices p₁, the consumer picks bundle A when B was affordable; at prices p₂, she picks B when C was affordable; at prices p₃, she picks C when A was affordable. Each individual pair satisfies WARP. Does this consumer satisfy SARP?"
  type: multiple-choice
  options:
    - "Yes — since every pairwise comparison satisfies WARP, SARP is automatically satisfied"
    - "No — the chain A ≻ B ≻ C ≻ A forms a revealed preference cycle, which SARP prohibits"
    - "Yes — SARP only applies when a consumer is observed more than five times"
    - "Indeterminate — we need to know the actual budget sets to determine SARP violations"
  answer: 1
  explanation: "This is precisely the scenario SARP was designed to catch. WARP only checks direct pairwise comparisons, so each pair satisfying WARP tells us nothing about the transitive chain. SARP requires that if A is revealed preferred to B through *any* chain — direct or indirect — then B cannot be revealed preferred to A through any chain. A ≻ B, B ≻ C, and C ≻ A creates a cycle of length three that SARP rules out, even though no single pairwise comparison violates WARP."

- question: "An economist wants to know whether a consumer's choices over 50 shopping trips are consistent with utility maximization. What is the minimal condition she needs to check?"
  type: multiple-choice
  options:
    - "Whether demand curves slope downward in every observed price-quantity pair"
    - "Whether the consumer spent their entire budget in each period"
    - "Whether the revealed preference relation derived from all observations contains any cycle"
    - "Whether the consumer chose the cheapest bundle in every period"
  answer: 2
  explanation: "SARP is both necessary and sufficient for consistency with utility maximization: the choices can be rationalized by some utility function if and only if the revealed preference relation is acyclic. The economist needs to build the revealed preference graph (A ≻ B if A was chosen when B was affordable) and check for cycles — no cycles means a rationalizing utility function exists. Checking demand slopes or budget exhaustion is neither necessary nor sufficient."

- question: "Satisfying SARP is necessary and sufficient for the existence of a utility function that rationalizes all observed choices."
  type: true-false
  answer: true
  explanation: "This is the central result: SARP precisely characterizes utility-maximizing behavior in the revealed preference framework. 'Necessary' means any utility maximizer must satisfy SARP — if a utility function exists, you can never have a revealed preference cycle, because a utility function assigns real numbers and real numbers cannot form a cycle (you can't have u(A) > u(B) > u(C) > u(A)). 'Sufficient' means that SARP compliance guarantees some utility function rationalizes the choices."

- question: "A consumer's choices satisfy WARP in every pairwise comparison. This is sufficient to conclude that some utility function rationalizes their behavior."
  type: true-false
  answer: false
  explanation: "WARP is weaker than SARP. WARP only rules out direct pairwise contradictions (if A is directly revealed preferred to B, don't directly reveal B preferred to A). It does not rule out indirect cycles through chains of three or more observations. Such cycles are incompatible with utility representation, so WARP compliance alone does not guarantee the existence of a utility function. SARP, which extends the no-cycle condition to all indirect chains, is the correct condition for utility rationalizability."

- question: "Why is a cycle in the revealed preference relation incompatible with the existence of a utility function rationalizing the consumer's choices?"
  type: short-answer
  answer: "A utility function assigns a real number to every bundle, and the function rationalizes choices only if every chosen bundle gets a higher utility number than any affordable alternative. If A is revealed preferred to B is revealed preferred to C is revealed preferred to A, we need u(A) > u(B) > u(C) > u(A) — but real numbers cannot form a strict cycle. No such assignment exists, so no utility function can rationalize a choice pattern with a revealed preference cycle."
  explanation: "This is the deep connection between acyclicity and numerical representability. The existence of a utility function is equivalent to the existence of a complete, transitive, consistent ordering of all bundles. A cycle directly violates transitivity (A is preferred to B is preferred to C, yet C is preferred to A). Since utility functions must represent complete transitive preferences, cycles are the exact obstruction to utility representation."
```

## Explainer

From your study of the **Weak Axiom of Revealed Preference (WARP)**, you know that if a consumer chooses bundle A when bundle B was affordable, then A is directly revealed preferred to B, and we should never observe the consumer choosing B when A is also affordable. WARP enforces pairwise consistency: no direct contradictions between any two observed choices. But WARP only checks one link at a time. The **Strong Axiom of Revealed Preference (SARP)** extends this logic to chains of any length.

Imagine three observations: in situation 1, the consumer picks A over affordable B. In situation 2, she picks B over affordable C. In situation 3, she picks C over affordable A. Each pairwise comparison satisfies WARP — no single pair directly contradicts. But following the chain, A is revealed preferred to B, B to C, and C to A, creating a preference cycle. SARP rules this out. It says: if A is revealed preferred to B through any sequence of intermediate choices — directly or indirectly — then B cannot be revealed preferred to A through any chain. In graph theory terms, the **revealed preference relation** must be acyclic.

Why does acyclicity matter so much? Because it is mathematically equivalent to the existence of a well-behaved **utility function** that rationalizes the consumer's choices. If you can assign a number to every bundle such that chosen bundles always get higher numbers than affordable alternatives, you have a utility function. Cycles make this impossible — you cannot rank A above B above C above A with real numbers. SARP is therefore the testable condition for whether observed market behavior is consistent with the entire apparatus of neoclassical consumer theory: utility maximization, well-ordered preferences, and downward-sloping demand.

In practice, SARP gives economists a purely behavioral test. You do not need to ask consumers about their preferences or assume a particular utility function. You simply observe what people buy at different prices and incomes, check whether the revealed preference relation contains any cycles, and if it does not, you know that some utility function could have generated those choices. Violations of SARP in experimental or survey data signal that the standard rational-choice model fails to describe that consumer's behavior — opening the door to behavioral alternatives like reference-dependent preferences or bounded rationality.

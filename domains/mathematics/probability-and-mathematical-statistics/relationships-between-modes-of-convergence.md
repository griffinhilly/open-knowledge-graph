---
id: relationships-between-modes-of-convergence
title: Relationships Between Modes of Convergence
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: almost-sure-convergence
  type: hard
- id: convergence-in-probability
  type: hard
- id: convergence-in-distribution
  type: hard
- id: convergence-in-lp
  type: hard
builds-toward:
- weak-law-of-large-numbers
- strong-law-of-large-numbers
tags:
- convergence
- implications
- hierarchy
stage: advanced
status: draft
---

# Relationships Between Modes of Convergence

## Core Idea
The hierarchy is: a.s. convergence ⟹ convergence in probability ⟹ convergence in distribution, and L^p convergence ⟹ convergence in probability. None of the other directions hold in general. Understanding these distinctions determines which limit theorem applies in a given context.

## Explainer

You've now studied four distinct notions of convergence for sequences of random variables: **almost sure convergence** (Xₙ → X a.s.), **convergence in probability** (Xₙ →ₚ X), **convergence in distribution** (Xₙ →_d X), and **L^p convergence** (E[|Xₙ − X|^p] → 0). Each captures a different sense in which Xₙ "approaches" X, and the critical question is how they relate — does one imply another? The hierarchy is the central organizing fact of the subject.

The strongest standard notion is **almost sure convergence**, which requires P({ω : Xₙ(ω) → X(ω)}) = 1 — that is, the set of sample points where convergence fails has probability zero. This is pointwise convergence on all but a null set, a genuinely strong pathwise statement. Almost sure convergence implies convergence in probability: if the convergence holds almost everywhere, then P(|Xₙ − X| > ε) → 0. The converse fails. A canonical counterexample is the **typewriter sequence** on [0,1] with Lebesgue measure: let X₁ = 1_{[0,1]}, X₂ = 1_{[0,1/2]}, X₃ = 1_{[1/2,1]}, X₄ = 1_{[0,1/4]}, and so on (intervals of halving length that cycle through [0,1]). This sequence converges to 0 in probability (P(Xₙ = 1) → 0) but not almost surely (for almost every ω, Xₙ(ω) = 1 infinitely often as the windows sweep back and forth).

**L^p convergence** also implies convergence in probability by Markov's inequality: P(|Xₙ − X| > ε) ≤ E[|Xₙ − X|^p] / εᵖ → 0. The relationship between L^p and a.s. convergence is more subtle — neither implies the other in general. However, there is a useful bridge: if Xₙ → X in probability, then some subsequence Xₙₖ → X almost surely. This subsequence extraction principle is a workhorse in probability proofs, allowing you to transfer results from a.s. convergence back to convergence in probability.

**Convergence in distribution** is the weakest: Xₙ →_d X requires only that the CDFs converge, Fₙ(t) → F(t) at continuity points of F. It says nothing about joint behavior — X and Xₙ don't even need to be defined on the same probability space. All three stronger notions imply convergence in distribution, but the reverse is generally false: Xₙ might converge in distribution to a standard normal without any individual Xₙ being close to any particular normal random variable. The one important exception: if the limit X is a constant c, then Xₙ →_d c if and only if Xₙ →_p c. The full hierarchy is: a.s. ⇒ in probability ⇒ in distribution, and L^p ⇒ in probability ⇒ in distribution. Each implication is strict; a counterexample for each reversed direction is a standard exercise that cements the distinctions. Knowing this hierarchy tells you, for instance, that the weak law (convergence in probability) is a weaker statement than the strong law (convergence a.s.) for the same sequence — but both imply the sample mean converges in distribution to the true mean, which here is not even a distributional statement but a degenerate one.

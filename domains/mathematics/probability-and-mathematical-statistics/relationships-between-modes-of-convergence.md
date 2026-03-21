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

## Questions

```yaml
- question: "A sequence of random variables Xₙ converges in distribution to a standard normal N(0,1). Which of the following is guaranteed?"
  type: multiple-choice
  options:
    - "Xₙ converges in probability to some random variable X"
    - "Xₙ converges almost surely to some random variable X"
    - "Each Xₙ is approximately normally distributed for large n"
    - "Convergence in distribution to N(0,1) does not guarantee any of the above"
  answer: 3
  explanation: "Convergence in distribution is the weakest mode: it only requires CDFs to converge at continuity points. It does not guarantee convergence in probability or a.s. convergence (counterexamples exist). Option C is the subtlest trap: the Xₙ individually are not guaranteed to be approximately normal — they could be wildly non-normal random variables whose distribution functions happen to converge to Φ. Convergence in distribution is a statement about distributions, not about individual random variables being 'close' to anything."

- question: "The typewriter sequence on [0,1] converges to 0 in probability. What does this sequence demonstrate about the relationship between convergence modes?"
  type: multiple-choice
  options:
    - "Convergence in probability implies almost sure convergence"
    - "Almost sure convergence implies convergence in probability"
    - "Convergence in probability does not imply almost sure convergence"
    - "The typewriter sequence also converges almost surely, so no implication fails"
  answer: 2
  explanation: "The typewriter sequence converges to 0 in probability (P(Xₙ = 1) → 0 as the intervals shrink) but NOT almost surely — for almost every point ω in [0,1], Xₙ(ω) = 1 infinitely often as the window sweeps back through each region. This is a canonical counterexample showing that convergence in probability does NOT imply almost sure convergence: the implication in the hierarchy runs the other way."

- question: "Almost sure convergence implies convergence in probability."
  type: true-false
  answer: true
  explanation: "This is one of the strict implications in the hierarchy. If Xₙ → X almost surely, then for every ε > 0, P(|Xₙ − X| > ε) → 0, which is precisely convergence in probability. The proof uses the continuity of probability measure. The converse fails — the typewriter sequence demonstrates convergence in probability without almost sure convergence."

- question: "If Xₙ converges in distribution to a standard normal, then for large n, each Xₙ is approximately a standard normal random variable."
  type: true-false
  answer: false
  explanation: "Convergence in distribution is a statement about the CDFs of the Xₙ converging to Φ — it says nothing about the individual random variables being 'close' to any standard normal. The Xₙ and the limit variable X do not even need to be defined on the same probability space. A sequence of Cauchy-distributed variables whose tails are somehow truncated could converge in distribution to N(0,1) without any individual variable being close to normal in any pathwise sense."

- question: "Explain why the distinction between the strong law of large numbers (almost sure convergence) and the weak law (convergence in probability) is substantive, not merely technical, even though both say the sample mean 'converges to' the true mean."
  type: short-answer
  answer: "The strong law says: with probability 1, every single sample path's average converges to μ — convergence happens simultaneously for almost all realizations of the sequence. The weak law says: for each fixed ε, the probability that the sample average is far from μ shrinks to zero. The weak law allows scenarios where, for any fixed n, the sample average could be far from μ with small but nonzero probability, without those events ever becoming negligible simultaneously across all n. The strong law rules out any persistent erratic behavior; the weak law only controls the probability at each n individually."
  explanation: "The hierarchy matters for applications: the strong law licenses interpreting long-run frequencies as probabilities, while the weak law only guarantees approximate accuracy 'most of the time.' Proofs of results that require strong law (e.g., Glivenko-Cantelli) cannot be replaced by appeals to the weak law alone."
```

## Explainer

You've now studied four distinct notions of convergence for sequences of random variables: **almost sure convergence** (Xₙ → X a.s.), **convergence in probability** (Xₙ →ₚ X), **convergence in distribution** (Xₙ →_d X), and **L^p convergence** (E[|Xₙ − X|^p] → 0). Each captures a different sense in which Xₙ "approaches" X, and the critical question is how they relate — does one imply another? The hierarchy is the central organizing fact of the subject.

The strongest standard notion is **almost sure convergence**, which requires P({ω : Xₙ(ω) → X(ω)}) = 1 — that is, the set of sample points where convergence fails has probability zero. This is pointwise convergence on all but a null set, a genuinely strong pathwise statement. Almost sure convergence implies convergence in probability: if the convergence holds almost everywhere, then P(|Xₙ − X| > ε) → 0. The converse fails. A canonical counterexample is the **typewriter sequence** on [0,1] with Lebesgue measure: let X₁ = 1_{[0,1]}, X₂ = 1_{[0,1/2]}, X₃ = 1_{[1/2,1]}, X₄ = 1_{[0,1/4]}, and so on (intervals of halving length that cycle through [0,1]). This sequence converges to 0 in probability (P(Xₙ = 1) → 0) but not almost surely (for almost every ω, Xₙ(ω) = 1 infinitely often as the windows sweep back and forth).

**L^p convergence** also implies convergence in probability by Markov's inequality: P(|Xₙ − X| > ε) ≤ E[|Xₙ − X|^p] / εᵖ → 0. The relationship between L^p and a.s. convergence is more subtle — neither implies the other in general. However, there is a useful bridge: if Xₙ → X in probability, then some subsequence Xₙₖ → X almost surely. This subsequence extraction principle is a workhorse in probability proofs, allowing you to transfer results from a.s. convergence back to convergence in probability.

**Convergence in distribution** is the weakest: Xₙ →_d X requires only that the CDFs converge, Fₙ(t) → F(t) at continuity points of F. It says nothing about joint behavior — X and Xₙ don't even need to be defined on the same probability space. All three stronger notions imply convergence in distribution, but the reverse is generally false: Xₙ might converge in distribution to a standard normal without any individual Xₙ being close to any particular normal random variable. The one important exception: if the limit X is a constant c, then Xₙ →_d c if and only if Xₙ →_p c. The full hierarchy is: a.s. ⇒ in probability ⇒ in distribution, and L^p ⇒ in probability ⇒ in distribution. Each implication is strict; a counterexample for each reversed direction is a standard exercise that cements the distinctions. Knowing this hierarchy tells you, for instance, that the weak law (convergence in probability) is a weaker statement than the strong law (convergence a.s.) for the same sequence — but both imply the sample mean converges in distribution to the true mean, which here is not even a distributional statement but a degenerate one.

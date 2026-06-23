---
id: weak-law-of-large-numbers
title: Weak Law of Large Numbers
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: convergence-in-probability
  type: hard
- id: independence-sigma-algebras
  type: hard
- id: chebyshev-bounds
  type: soft
- id: independence-of-sigma-algebras
  type: soft
- id: relationships-between-modes-of-convergence
  type: soft
builds-toward:
- strong-law-of-large-numbers
- central-limit-theorem-rigorous
tags:
- law-of-large-numbers
- limit-theorems
- probability
stage: advanced
status: validated
---

# Weak Law of Large Numbers

## Core Idea
If {Xₙ} are i.i.d. random variables with finite mean μ, then Sₙ/n = (X₁ + ... + Xₙ)/n converges in probability to μ. The key assumption is finite variance (or more generally, applying Chebyshev's inequality). The weak LLN guarantees that sample means stabilize around the true mean, justifying empirical estimation.

## Questions

```yaml
- question: "After 1000 fair coin flips, the sample proportion of heads is 0.52. A student claims the WLLN guarantees it will eventually equal exactly 0.5. What does the WLLN actually guarantee?"
  type: multiple-choice
  options:
    - "That the sample proportion must equal 0.5 exactly once n is large enough"
    - "That for any fixed ε > 0, the probability that the sample proportion differs from 0.5 by more than ε approaches 0 as n → ∞ — but individual sequences need not converge"
    - "That the sample proportion will converge to 0.5 at every possible infinite sequence of coin flips"
    - "That the sample proportion will decrease monotonically toward 0.5 after 1000 flips"
  answer: 1
  explanation: "The WLLN guarantees convergence in probability: P(|Sₙ/n − μ| > ε) → 0. This means the probability of being far from μ vanishes, but it does not mean any particular sample path converges. Individual sequences can fluctuate forever. The statement in option C describes almost sure convergence — the conclusion of the Strong Law, which is a strictly stronger result requiring a harder proof."

- question: "The standard proof of the WLLN under finite variance σ² applies Chebyshev's inequality to Sₙ/n and obtains P(|Sₙ/n − μ| > ε) ≤ σ²/(nε²). What property of the random variables is essential for computing Var(Sₙ/n) = σ²/n?"
  type: multiple-choice
  options:
    - "That the variables have finite mean μ, which allows the expectation to be computed"
    - "That the variables are identically distributed, so each has the same variance σ²"
    - "That the variables are independent, which makes their variances additive: Var(Sₙ) = nσ²"
    - "That the variables take values in a bounded interval, ensuring Chebyshev applies"
  answer: 2
  explanation: "Independence is the key structural property that makes variances additive: for independent random variables, Var(X₁ + ··· + Xₙ) = Var(X₁) + ··· + Var(Xₙ) = nσ². Without independence, covariance terms appear and Var(Sₙ) could be much larger than nσ², preventing the bound σ²/(nε²) from going to zero. Identical distribution ensures each term contributes the same σ², but it is independence that allows addition of variances."

- question: "The Weak Law of Large Numbers implies that individual sample paths of Sₙ/n is expected to converge to μ at nearly every outcome ω in the sample space."
  type: true-false
  answer: false
  explanation: "This is the crucial distinction between the WLLN and the Strong Law. Convergence in probability means P(|Sₙ/n − μ| > ε) → 0: the probability mass outside any ε-neighborhood of μ goes to zero. But specific sample paths can still fluctuate outside that neighborhood forever, as long as the set of such paths has probability approaching zero. Almost sure convergence (P(Sₙ/n → μ) = 1), guaranteed by the Strong LLN, is the statement that essentially every sample path converges."

- question: "The proof of the WLLN relies on the fact that for i.i.d. random variables with finite variance, the variance of the sample mean Sₙ/n tends to zero as n → ∞."
  type: true-false
  answer: true
  explanation: "Var(Sₙ/n) = σ²/n → 0 as n → ∞. Chebyshev's inequality converts this vanishing variance into a vanishing probability: P(|Sₙ/n − μ| > ε) ≤ Var(Sₙ/n)/ε² = σ²/(nε²) → 0. The entire proof is a two-step argument: independence makes variance additive, causing Var(Sₙ/n) to shrink; Chebyshev converts that shrinking variance into a probability bound."

- question: "Explain the difference between convergence in probability and almost sure convergence in the context of sample means. Why can the WLLN hold even while some individual sample paths continue to fluctuate away from μ?"
  type: short-answer
  answer: "Convergence in probability means the probability of the sample mean being far from μ goes to zero: for any ε > 0, P(|Sₙ/n − μ| > ε) → 0. Almost sure convergence means the sample mean converges to μ at every outcome except a set of probability zero: P(lim Sₙ/n = μ) = 1. The WLLN guarantees the former. Individual sample paths can still fluctuate indefinitely away from μ — as long as the set of such paths has probability shrinking to zero. Convergence in probability is a statement about the distribution of the sample mean, not about every individual trajectory."
  explanation: "This distinction matters for understanding the limits of the WLLN. It justifies using sample means to estimate population means in practice (the probability of a bad estimate vanishes), without requiring that every conceivable sequence of observations converges — which would be a far stronger guarantee."
```

## Explainer

The Weak Law of Large Numbers formalizes the intuition behind **empirical estimation**: average many independent observations of the same random quantity, and the average should be close to the true mean. You know from prerequisites what "close" means rigorously: Sₙ/n → μ **in probability** means that for any ε > 0, P(|Sₙ/n − μ| > ε) → 0 as n → ∞. The WLLN says exactly this happens for i.i.d. sequences with finite mean μ.

The standard proof under the additional assumption of finite variance σ² is a direct application of **Chebyshev's inequality**, which you know from prerequisites: P(|Y − E[Y]| > ε) ≤ Var(Y)/ε². Apply it to Y = Sₙ/n. The expected value of Sₙ/n is μ — since E[Xᵢ] = μ and expectation is linear, E[Sₙ/n] = μ. The variance of Sₙ/n is σ²/n — since the Xᵢ are independent (which allows variance to add: Var(Sₙ) = nσ²), we get Var(Sₙ/n) = σ²/n. Chebyshev then gives P(|Sₙ/n − μ| > ε) ≤ σ²/(nε²) → 0. The key roles are clear: independence (via sigma-algebra independence from your prerequisites) makes variances additive, and Chebyshev converts that variance bound into a probability bound.

The convergence is **not** pointwise: the sample averages don't necessarily converge at every individual outcome ω. They could fluctuate forever along particular sample paths. What goes to zero is the probability of being far from μ — which is exactly what convergence in probability captures. The **Strong LLN** (which builds on this result) strengthens the conclusion to almost sure convergence: P(Sₙ/n → μ) = 1, meaning the averages converge at every outcome except possibly a set of probability zero. The weak version is easier to prove and suffices for most statistical applications: it rigorously justifies using a sample mean to estimate a population mean.

The WLLN is also the theoretical backbone of **Monte Carlo methods**. To estimate E[g(X)] for some function g, generate i.i.d. samples X₁, ..., Xₙ and compute the average (g(X₁) + ··· + g(Xₙ)) / n. The WLLN guarantees this converges to the true expectation. The convergence rate is σ²/n, where σ² = Var(g(X)) — crucially, this depends on the variance of the function, not on the dimension of the problem. For high-dimensional integrals where deterministic quadrature rules scale exponentially in dimension, this dimension-independence makes Monte Carlo the method of choice.

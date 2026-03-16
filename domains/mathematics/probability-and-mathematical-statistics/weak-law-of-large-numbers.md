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
builds-toward:
- strong-law-of-large-numbers
- central-limit-theorem-rigorous
tags:
- law-of-large-numbers
- limit-theorems
- probability
stage: formal-systems
status: draft
---

# Weak Law of Large Numbers

## Core Idea
If {Xₙ} are i.i.d. random variables with finite mean μ, then Sₙ/n = (X₁ + ... + Xₙ)/n converges in probability to μ. The key assumption is finite variance (or more generally, applying Chebyshev's inequality). The weak LLN guarantees that sample means stabilize around the true mean, justifying empirical estimation.

## Explainer

The Weak Law of Large Numbers formalizes the intuition behind **empirical estimation**: average many independent observations of the same random quantity, and the average should be close to the true mean. You know from prerequisites what "close" means rigorously: Sₙ/n → μ **in probability** means that for any ε > 0, P(|Sₙ/n − μ| > ε) → 0 as n → ∞. The WLLN says exactly this happens for i.i.d. sequences with finite mean μ.

The standard proof under the additional assumption of finite variance σ² is a direct application of **Chebyshev's inequality**, which you know from prerequisites: P(|Y − E[Y]| > ε) ≤ Var(Y)/ε². Apply it to Y = Sₙ/n. The expected value of Sₙ/n is μ — since E[Xᵢ] = μ and expectation is linear, E[Sₙ/n] = μ. The variance of Sₙ/n is σ²/n — since the Xᵢ are independent (which allows variance to add: Var(Sₙ) = nσ²), we get Var(Sₙ/n) = σ²/n. Chebyshev then gives P(|Sₙ/n − μ| > ε) ≤ σ²/(nε²) → 0. The key roles are clear: independence (via sigma-algebra independence from your prerequisites) makes variances additive, and Chebyshev converts that variance bound into a probability bound.

The convergence is **not** pointwise: the sample averages don't necessarily converge at every individual outcome ω. They could fluctuate forever along particular sample paths. What goes to zero is the probability of being far from μ — which is exactly what convergence in probability captures. The **Strong LLN** (which builds on this result) strengthens the conclusion to almost sure convergence: P(Sₙ/n → μ) = 1, meaning the averages converge at every outcome except possibly a set of probability zero. The weak version is easier to prove and suffices for most statistical applications: it rigorously justifies using a sample mean to estimate a population mean.

The WLLN is also the theoretical backbone of **Monte Carlo methods**. To estimate E[g(X)] for some function g, generate i.i.d. samples X₁, ..., Xₙ and compute the average (g(X₁) + ··· + g(Xₙ)) / n. The WLLN guarantees this converges to the true expectation. The convergence rate is σ²/n, where σ² = Var(g(X)) — crucially, this depends on the variance of the function, not on the dimension of the problem. For high-dimensional integrals where deterministic quadrature rules scale exponentially in dimension, this dimension-independence makes Monte Carlo the method of choice.

---
id: central-limit-theorem-rigorous
title: Central Limit Theorem (Rigorous via Characteristic Functions)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: characteristic-functions
  type: hard
- id: convergence-in-distribution
  type: hard
- id: multivariate-normal-distribution
  type: soft
builds-toward:
- maximum-likelihood-estimation-theory
- confidence-intervals-rigorous-theory
- asymptotic-normality-mle
tags:
- central-limit-theorem
- limit-theorems
- probability
stage: advanced
status: draft
---

# Central Limit Theorem (Rigorous via Characteristic Functions)

## Core Idea
If {Xₙ} are i.i.d. with mean μ and variance σ², then (Sₙ - nμ)/(σ√n) converges in distribution to N(0,1). The rigorous proof uses characteristic functions: φₙ(t/√n) → e^{-t²/2} for all t. The CLT explains why the normal distribution is ubiquitous—sums of many independent random variables are approximately normal regardless of the original distribution.

## How It's Best Learned
Prove the CLT using characteristic functions. Apply the CLT to non-normal parent distributions to verify the approximation. Use the CLT to justify normal approximations in statistical inference.

## Common Misconceptions
- Thinking the CLT applies without finite variance; finite variance is required. - Assuming convergence means they are equal for all n; it is only in the limit. - Forgetting that convergence is in distribution, not almost sure.

## Explainer

You've studied **characteristic functions** — φ_X(t) = E[e^{itX}] — which encode all the distributional information about a random variable and behave nicely under sums (the characteristic function of a sum of independent variables is the product of their characteristic functions). You've also studied **convergence in distribution**, where a sequence of CDFs converges to a limiting CDF. The rigorous CLT proof combines these: it shows that the characteristic function of the standardized sum converges pointwise to e^{−t²/2}, the characteristic function of the standard normal, and then invokes the continuity theorem to conclude distributional convergence.

Here is the proof in outline. Without loss of generality, center and scale so that each Xᵢ has mean 0 and variance 1. The standardized sum is Sₙ/√n. Its characteristic function is φ_{Sₙ/√n}(t) = [φ_X(t/√n)]ⁿ. Now expand φ_X around 0: since E[X] = 0 and E[X²] = 1, the Taylor expansion gives φ_X(s) = 1 − s²/2 + o(s²). Substituting s = t/√n: φ_X(t/√n) = 1 − t²/(2n) + o(1/n). Raising to the n-th power: (1 − t²/(2n) + o(1/n))ⁿ → e^{−t²/2} for each fixed t. The **continuity theorem** then says: if the characteristic functions converge pointwise to the characteristic function of a distribution, the distributions converge in distribution. The standard normal has characteristic function e^{−t²/2}, so the result follows.

The **finite variance** condition is essential, not a mere technicality. The variance σ² appears as the coefficient in the Taylor expansion of φ_X: if variance is infinite, the second-order term is missing, the Taylor argument collapses, and the sum does not converge to a normal distribution. Instead, sums of heavy-tailed variables with infinite variance converge to **stable distributions** (of which the normal is a special case). The Cauchy distribution — whose variance is infinite — is the canonical example: sums of Cauchy variables rescaled by n give another Cauchy, not a normal. The CLT's universality is precisely bounded by the finite variance assumption.

Convergence **in distribution** — not almost sure, not in probability — is the correct mode here. The CLT says the *distribution* of (Sₙ − nμ)/(σ√n) approaches the standard normal. Individual observations remain drawn from whatever distribution they came from; what changes is the shape of the sampling distribution of the sum (or average). This is why "the CLT applies" in statistics means you can use normal critical values for large-sample inference: the sampling distribution of the sample mean is approximately normal. The approximation improves as n grows, but it is never exact for finite n (unless the original distribution is normal). Understanding this distinction — that the CLT is a statement about distributions, not individual outcomes — is the key to applying it correctly.

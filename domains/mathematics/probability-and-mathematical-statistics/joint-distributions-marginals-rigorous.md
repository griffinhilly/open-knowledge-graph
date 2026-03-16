---
id: joint-distributions-marginals-rigorous
title: Joint Distributions and Marginals (Rigorous)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: distribution-functions-densities-rigorous
  type: hard
- id: iterated-integrals
  type: hard
builds-toward:
- conditional-expectation
- independence-sigma-algebras
- multivariate-normal-distribution
tags:
- multivariate
- joint-distributions
- measure-theory
stage: advanced
status: draft
---

# Joint Distributions and Marginals (Rigorous)

## Core Idea
For random vector X = (X₁, ..., Xₙ), the joint CDF is F(x₁,...,xₙ) = P(X₁ ≤ x₁,...,Xₙ ≤ xₙ). Marginal distributions describe individual Xᵢ. A joint pdf f satisfies P((X₁,...,Xₙ) ∈ A) = ∫ₐ f(x₁,...,xₙ) dx₁...dxₙ. The Radon-Nikodym theorem guarantees densities when distributions are absolutely continuous.

## Explainer

From your prerequisite on **distribution functions and densities**, you know that a real-valued random variable X is characterized by its CDF F(x) = P(X ≤ x), and that when F is absolutely continuous, its derivative yields the **probability density function** (pdf) f with P(X ∈ A) = ∫ₐ f(x) dx. The rigorous treatment of joint distributions extends every part of this framework to random vectors — pairs, triples, and n-tuples of random variables observed simultaneously.

For a random vector (X₁, X₂), the **joint CDF** is F(x₁, x₂) = P(X₁ ≤ x₁ and X₂ ≤ x₂). This is a function of two variables encoding all probabilistic information about how X₁ and X₂ behave together. When the joint CDF is absolutely continuous (with respect to two-dimensional Lebesgue measure), the **Radon-Nikodym theorem** — the measure-theoretic version of the fundamental theorem of calculus — guarantees the existence of a **joint pdf** f(x₁, x₂) satisfying F(x₁, x₂) = ∫₋∞^x₁ ∫₋∞^x₂ f(u, v) dv du. Probabilities of any measurable set A are then computed using your prerequisite skill of **iterated integrals**: P((X₁, X₂) ∈ A) = ∬_A f(x₁, x₂) dx₁ dx₂. The Radon-Nikodym condition matters precisely because it rules out distributions with point masses, which cannot be represented by a density in the usual sense.

**Marginal distributions** recover the behavior of individual variables from the joint. For continuous random variables, the marginal pdf of X₁ is obtained by integrating out X₂: f₁(x₁) = ∫₋∞^∞ f(x₁, x₂) dx₂. The intuition is that you are "summing over" all possible values of the second variable, collapsing the two-dimensional distribution onto one axis. The order of integration in iterated integrals (Fubini's theorem) justifies swapping the roles of x₁ and x₂ freely when f is non-negative or integrable, which is guaranteed under the standing absolute continuity assumption. This is why rigorous control over when densities exist — via Radon-Nikodym — matters: it ensures Fubini applies.

The distinction between the joint distribution and the marginals is fundamental to everything that follows. Two random variables can have the same marginal distributions but completely different joint distributions — one might be independent, the other tightly correlated. The joint pdf carries more information than the two marginals separately. **Independence** is the special case where the joint pdf factors: f(x₁, x₂) = f₁(x₁) · f₂(x₂). Verifying this factorization (or its failure) using iterated integrals is the primary technical tool. The rigorous language of sigma-algebras, which this topic builds toward, allows independence to be extended beyond pairs of random variables to whole families — but the density-level intuition you develop here, integrating over one coordinate at a time, is exactly what carries over.

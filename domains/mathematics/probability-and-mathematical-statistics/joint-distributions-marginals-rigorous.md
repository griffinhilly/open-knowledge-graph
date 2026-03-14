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
stage: abstract-reasoning
status: draft
---

# Joint Distributions and Marginals (Rigorous)

## Core Idea
For random vector X = (X₁, ..., Xₙ), the joint CDF is F(x₁,...,xₙ) = P(X₁ ≤ x₁,...,Xₙ ≤ xₙ). Marginal distributions describe individual Xᵢ. A joint pdf f satisfies P((X₁,...,Xₙ) ∈ A) = ∫ₐ f(x₁,...,xₙ) dx₁...dxₙ. The Radon-Nikodym theorem guarantees densities when distributions are absolutely continuous.

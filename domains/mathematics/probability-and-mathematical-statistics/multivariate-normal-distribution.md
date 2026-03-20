---
id: multivariate-normal-distribution
title: Multivariate Normal Distribution
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: joint-distributions-marginals-rigorous
  type: hard
- id: characteristic-functions
  type: soft
- id: linear-transformations
  type: soft
builds-toward:
- central-limit-theorem-rigorous
- bayesian-inference-foundations
tags:
- multivariate-normal
- distributions
- statistics
stage: advanced
status: draft
---

# Multivariate Normal Distribution

## Core Idea
A random vector X ~ N(μ, Σ) has characteristic function φ(t) = exp(it'μ - ½t'Σt). The MVN is closed under linear transformations and marginals. A joint distribution is MVN if every linear combination of components is univariate normal. The MVN is fundamental in statistical inference because the sample mean vector is MVN for large samples.

## Explainer

You know the univariate normal N(μ, σ²): a bell-shaped distribution centered at μ with spread controlled by σ². The **multivariate normal distribution** (MVN) extends this to random vectors X = (X₁, ..., Xₙ)'. The cleanest definition: X is MVN if every linear combination a'X = a₁X₁ + ... + aₙXₙ is univariate normal for any fixed vector a. This says the MVN is "normal in every direction" — no matter how you project the joint distribution onto a line, you get a normal curve.

The MVN is parameterized by a **mean vector** μ ∈ ℝⁿ (where the distribution is centered) and a **covariance matrix** Σ ∈ ℝⁿˣⁿ (which must be positive semidefinite). The diagonal entries are variances: Σᵢᵢ = Var(Xᵢ). The off-diagonal entries capture correlations: Σᵢⱼ = Cov(Xᵢ, Xⱼ). When Σ is diagonal, the components are independent normals. A positive Σᵢⱼ means Xᵢ and Xⱼ tend to move together; negative means they move in opposite directions.

From your joint distributions work, you know that marginals are obtained by integrating out other variables — often a painful computation. For the MVN, marginals are trivial: if X ~ N(μ, Σ) and you split X into subvectors X = (X₁, X₂)', then X₁ ~ N(μ₁, Σ₁₁) where μ₁ is the corresponding subvector of μ and Σ₁₁ is the corresponding submatrix of Σ. You just read off the relevant pieces. No integration required. This is a major computational advantage of the MVN.

The closure under linear transformations (from your linear transformations prerequisite) is equally powerful: if X ~ N(μ, Σ) and A is a matrix, then AX ~ N(Aμ, AΣA'). This single fact explains why the sample mean X̄ = (1/n)1'X is normal when the data are iid normal — it is a linear transformation of the data vector. More generally, any quantity computed as a linear function of normally distributed data inherits normality. The **characteristic function** φ(t) = exp(it'μ − ½t'Σt) encodes the entire distribution and makes this closure trivial to prove: φ_{AX}(t) = φ_X(A't), and substituting confirms the form. It also shows the MVN is completely determined by its first two moments — mean and covariance — since all higher cumulants vanish.

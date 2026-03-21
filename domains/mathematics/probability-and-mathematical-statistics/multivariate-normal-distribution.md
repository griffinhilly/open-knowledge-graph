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

## Questions

```yaml
- question: "Two random variables X₁ and X₂ are each marginally normally distributed, and Cov(X₁, X₂) = 0. Does this guarantee that (X₁, X₂) is jointly multivariate normal?"
  type: multiple-choice
  options:
    - "Yes — normal marginals with zero covariance implies independence, which implies joint normality"
    - "No — marginal normality and zero covariance are necessary but not sufficient; a joint distribution is MVN only if every linear combination a₁X₁ + a₂X₂ is univariate normal"
    - "Yes — the covariance matrix fully determines the joint distribution for any pair of normal variables"
    - "No — but this only matters in the singular case where the covariance matrix is not invertible"
  answer: 1
  explanation: "This is the central misconception about the MVN. Marginal normality does not imply joint normality, even with zero covariance. A counterexample: let X₁ ~ N(0,1), and let X₂ = X₁ · S where S is ±1 with equal probability independent of X₁. Then X₂ is marginally normal, Cov(X₁, X₂) = 0, but X₁ + X₂ = X₁(1 + S) is not normally distributed (it's a mixture). The defining property of the MVN is that *every* linear combination is normal — this is strictly stronger than normal marginals."

- question: "If X ~ N(μ, Σ) is a k-dimensional multivariate normal random vector and A is an m×k matrix, what is the distribution of Y = AX?"
  type: multiple-choice
  options:
    - "Y ~ N(Aμ, AΣ) — linear transformations scale the covariance matrix by A on one side"
    - "Y ~ N(Aμ, AΣAᵀ) — the MVN is closed under linear transformations, with covariance transformed by the congruence AΣAᵀ"
    - "Y is approximately normal for large k but not exactly normal in general"
    - "Y is normal only if A is square and invertible"
  answer: 1
  explanation: "Closure under linear transformations is one of the defining properties of the MVN. If X ~ N(μ, Σ) and A is any matrix, then AX ~ N(Aμ, AΣAᵀ). The mean transforms as Aμ (linearity of expectation), and the covariance transforms as AΣAᵀ (standard covariance propagation for linear functions). This result follows immediately from the characteristic function: φ_{AX}(t) = φ_X(Aᵀt) = exp(itᵀAμ − ½tᵀAΣAᵀt), which is the characteristic function of N(Aμ, AΣAᵀ). A need not be square or invertible."

- question: "For the multivariate normal distribution, zero covariance between two components implies statistical independence — a property that does not hold for distributions in general."
  type: true-false
  answer: true
  explanation: "In general distributions, zero covariance (uncorrelatedness) does not imply independence — covariance only captures linear relationships. But for the MVN, the characteristic function factorizes whenever the off-diagonal blocks of Σ are zero: φ_{X₁,X₂}(t₁,t₂) = φ_{X₁}(t₁)φ_{X₂}(t₂), which is the condition for independence. This is a special property of the normal distribution arising from the fact that the MVN is entirely determined by its first two moments (mean and covariance). For MVN variables, correlation = 0 is both necessary and sufficient for independence."

- question: "A joint distribution is multivariate normal if and only if all of its marginal distributions are univariate normal."
  type: true-false
  answer: false
  explanation: "Marginal normality is necessary but not sufficient for joint MVN. The correct characterization is that a joint distribution is MVN if and only if every linear combination of its components is univariate normal. This condition is strictly stronger: it rules out distributions that have normal margins but non-normal joint structure (such as the counterexample with X₂ = X₁ · S). If you only check marginals, you may classify a non-MVN distribution as MVN and make incorrect inferences about conditional distributions and independence."

- question: "Why is 'every linear combination a'X is univariate normal' a more useful definition of the multivariate normal than the density formula, especially for proving properties of the distribution?"
  type: short-answer
  answer: "The linear combination definition directly implies all the key closure properties. Closure under linear transformations follows immediately: if every linear combination of X is normal, then every linear combination of AX = A(linear combination of X) is also normal, so AX is MVN. Marginality is a special case: a marginal is obtained by setting some coefficients to zero, which is a linear combination. Conditional distributions are obtainable via algebraic argument from the same property. The density formula requires the matrix to be invertible and does not extend to degenerate cases, while the linear combination definition works even when Σ is singular."
  explanation: "Definitions that are close to the property you want to exploit make proofs efficient. The linear combination definition is essentially a statement about the behavior of the distribution under projection, which is exactly what closure under linear maps requires. It also clarifies why the MVN is the natural multivariate extension of the univariate normal: it is normal 'in every direction.'"
```

## Explainer

You know the univariate normal N(μ, σ²): a bell-shaped distribution centered at μ with spread controlled by σ². The **multivariate normal distribution** (MVN) extends this to random vectors X = (X₁, ..., Xₙ)'. The cleanest definition: X is MVN if every linear combination a'X = a₁X₁ + ... + aₙXₙ is univariate normal for any fixed vector a. This says the MVN is "normal in every direction" — no matter how you project the joint distribution onto a line, you get a normal curve.

The MVN is parameterized by a **mean vector** μ ∈ ℝⁿ (where the distribution is centered) and a **covariance matrix** Σ ∈ ℝⁿˣⁿ (which must be positive semidefinite). The diagonal entries are variances: Σᵢᵢ = Var(Xᵢ). The off-diagonal entries capture correlations: Σᵢⱼ = Cov(Xᵢ, Xⱼ). When Σ is diagonal, the components are independent normals. A positive Σᵢⱼ means Xᵢ and Xⱼ tend to move together; negative means they move in opposite directions.

From your joint distributions work, you know that marginals are obtained by integrating out other variables — often a painful computation. For the MVN, marginals are trivial: if X ~ N(μ, Σ) and you split X into subvectors X = (X₁, X₂)', then X₁ ~ N(μ₁, Σ₁₁) where μ₁ is the corresponding subvector of μ and Σ₁₁ is the corresponding submatrix of Σ. You just read off the relevant pieces. No integration required. This is a major computational advantage of the MVN.

The closure under linear transformations (from your linear transformations prerequisite) is equally powerful: if X ~ N(μ, Σ) and A is a matrix, then AX ~ N(Aμ, AΣA'). This single fact explains why the sample mean X̄ = (1/n)1'X is normal when the data are iid normal — it is a linear transformation of the data vector. More generally, any quantity computed as a linear function of normally distributed data inherits normality. The **characteristic function** φ(t) = exp(it'μ − ½t'Σt) encodes the entire distribution and makes this closure trivial to prove: φ_{AX}(t) = φ_X(A't), and substituting confirms the form. It also shows the MVN is completely determined by its first two moments — mean and covariance — since all higher cumulants vanish.

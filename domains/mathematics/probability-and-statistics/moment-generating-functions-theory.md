---
id: moment-generating-functions-theory
title: Moment Generating Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: variance-standard-deviation
  type: hard
- id: natural-logarithm-and-e
  type: soft
builds-toward:
- normal-distribution-theory
tags:
- mgf
- moments
stage: formal-systems
status: validated
---

# Moment Generating Functions

## Core Idea
MGF M(t)=E[e^{tX}] uniquely determines a distribution (when it exists). The n-th moment is M^{(n)}(0)=E[X^n]. MGFs simplify finding moments, proving distribution properties, and establishing convergence. Matching MGFs implies identical distributions.

## Questions

```yaml
- question: "Two random variables X and Y have been shown to have the same MGF on an open interval around zero. What can you conclude?"
  type: multiple-choice
  options:
    - "X and Y have the same mean and variance, but their full distributions may still differ"
    - "X and Y have identical distributions"
    - "X and Y are independent of each other"
    - "X and Y are identically distributed only if they also have the same support"
  answer: 1
  explanation: "The uniqueness theorem for MGFs states: if two random variables have the same MGF on an open interval containing zero, they have the same distribution — not just the same moments, but identical distributions. This is what gives MGFs their real power beyond moment computation: you can prove distributional equalities by comparing MGFs instead of density functions. Options A and D are wrong because matching all moments (encoded by the MGF) determines the full distribution, not just the first two moments."

- question: "How does the MGF formula M(t) = E[e^{tX}] encode the moments of a random variable X?"
  type: multiple-choice
  options:
    - "The moments are encoded in the base of the exponential — varying the base extracts different moments"
    - "Each moment E[X^n] appears as the coefficient of t^n/n! in the Taylor expansion of M(t) around t = 0"
    - "The MGF encodes only the mean and variance; higher moments require separate calculations"
    - "Moments are recovered by integrating M(t) over intervals centered at zero"
  answer: 1
  explanation: "Expanding e^{tX} as a Taylor series gives 1 + tX + t²X²/2! + t³X³/3! + ⋯ Taking expectations term by term yields M(t) = 1 + tE[X] + t²E[X²]/2! + ⋯ The coefficient of t^n/n! is exactly E[X^n]. This is why differentiating M(t) n times and evaluating at t = 0 gives M^(n)(0) = E[X^n] — the derivative operation extracts the coefficient by canceling the factorial. All moments are simultaneously encoded in M(t), not just the first two."

- question: "For any random variable X, the moment generating function M(t) = E[e^{tX}] typically exists and uniquely determines the distribution."
  type: true-false
  answer: false
  explanation: "The MGF does not always exist. For heavy-tailed distributions — most famously the Cauchy distribution — E[e^{tX}] is infinite for all t ≠ 0, so the MGF fails to exist. When the MGF doesn't exist, one must use the characteristic function φ(t) = E[e^{itX}], which always exists since |e^{itX}| = 1. The characteristic function has analogous uniqueness and moment properties but requires complex analysis. The existence caveat is important: MGF results apply only when the MGF exists on an open interval around zero."

- question: "If X and Y are independent random variables, the MGF of X + Y equals the product of their individual MGFs."
  type: true-false
  answer: true
  explanation: "M_{X+Y}(t) = E[e^{t(X+Y)}] = E[e^{tX} · e^{tY}]. By independence, E[e^{tX} · e^{tY}] = E[e^{tX}] · E[e^{tY}] = M_X(t) · M_Y(t). This multiplicative property is what allows MGF proofs of important results like the Central Limit Theorem: as you take sums of independent copies, their product MGFs converge to the MGF of the normal distribution, and by uniqueness the sums converge in distribution to normal. Without independence, the factorization fails."

- question: "Explain why the n-th derivative of M(t) evaluated at t = 0 gives E[X^n], connecting this to the Taylor series expansion of e^{tX}."
  type: short-answer
  answer: "Start from the Taylor series: e^{tX} = Σ (tX)^n/n! = 1 + tX + t²X²/2! + t³X³/3! + ⋯ Taking expectations: M(t) = E[e^{tX}] = 1 + tE[X] + t²E[X²]/2! + t³E[X³]/3! + ⋯ This is a power series in t whose coefficient of t^n/n! is E[X^n]. When you differentiate M(t) n times with respect to t, you apply the power rule n times to each term: the t^n/n! term becomes 1, and all lower-degree terms vanish. Evaluating at t = 0 kills all remaining terms involving positive powers of t, leaving only E[X^n]. Differentiation is precisely the operation that extracts Taylor coefficients."
  explanation: "This connection between differentiation and moment extraction is the computational heart of MGF theory. It transforms the problem of computing moments (which might require difficult integrals) into the problem of differentiating a single function — often much easier for standard distributions like the Poisson, binomial, or normal."
```

## Explainer

A **moment generating function (MGF)** is a compact device that encodes every moment of a random variable into a single function. To see where it comes from, recall the Taylor series for e^u: e^u = 1 + u + u²/2! + u³/3! + ⋯ Substituting u = tX gives e^{tX} = 1 + tX + t²X²/2! + t³X³/3! + ⋯ Taking expectations term by term yields M(t) = E[e^{tX}] = 1 + tE[X] + t²E[X²]/2! + t³E[X³]/3! + ⋯ Every coefficient carries a moment. The MGF is literally the generating function of the sequence of moments — the name is apt.

The key computational payoff is that **differentiation at zero extracts moments**. Differentiating M(t) once and evaluating at t=0 gives M'(0) = E[X]. Differentiating twice gives M''(0) = E[X²]. You already know variance from prerequisites: Var(X) = E[X²] − (E[X])². The MGF lets you compute both quantities from a single function by taking derivatives, rather than computing integrals from scratch. For a Poisson(λ) random variable, for example, M(t) = e^{λ(e^t - 1)}, and two differentiations at zero confirm E[X] = Var(X) = λ.

MGFs also shine when working with **sums of independent random variables**. If X and Y are independent, then M_{X+Y}(t) = E[e^{t(X+Y)}] = E[e^{tX}]·E[e^{tY}] = M_X(t)·M_Y(t). Products of MGFs correspond to convolutions of distributions — a statement that would require integral calculations to prove directly. This multiplicative property is what allows the MGF proof of the Central Limit Theorem: as sums of independent copies are taken, their MGFs converge to the MGF of the normal distribution, and since MGFs uniquely determine distributions, the sum converges in distribution to normal.

The **uniqueness theorem** is what gives MGFs their real power: if two random variables have the same MGF on an open interval around zero, they have the same distribution. This means you can prove distributional equalities by comparing MGFs rather than density functions. There is one important caveat: the MGF does not always exist. If E[e^{tX}] = ∞ for all t ≠ 0 (as happens for heavy-tailed distributions like the Cauchy), the MGF fails to exist and one must use the **characteristic function** φ(t) = E[e^{itX}] instead, which always exists since |e^{itX}| = 1. Characteristic functions have analogous properties but require complex analysis — a reason to appreciate MGFs when they do exist.

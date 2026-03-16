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
- binomial-distribution-theory
- normal-distribution-theory
tags:
- mgf
- moments
stage: formal-systems
status: draft
---

# Moment Generating Functions

## Core Idea
MGF M(t)=E[e^{tX}] uniquely determines a distribution (when it exists). The n-th moment is M^{(n)}(0)=E[X^n]. MGFs simplify finding moments, proving distribution properties, and establishing convergence. Matching MGFs implies identical distributions.

## Explainer

A **moment generating function (MGF)** is a compact device that encodes every moment of a random variable into a single function. To see where it comes from, recall the Taylor series for e^u: e^u = 1 + u + u²/2! + u³/3! + ⋯ Substituting u = tX gives e^{tX} = 1 + tX + t²X²/2! + t³X³/3! + ⋯ Taking expectations term by term yields M(t) = E[e^{tX}] = 1 + tE[X] + t²E[X²]/2! + t³E[X³]/3! + ⋯ Every coefficient carries a moment. The MGF is literally the generating function of the sequence of moments — the name is apt.

The key computational payoff is that **differentiation at zero extracts moments**. Differentiating M(t) once and evaluating at t=0 gives M'(0) = E[X]. Differentiating twice gives M''(0) = E[X²]. You already know variance from prerequisites: Var(X) = E[X²] − (E[X])². The MGF lets you compute both quantities from a single function by taking derivatives, rather than computing integrals from scratch. For a Poisson(λ) random variable, for example, M(t) = e^{λ(e^t - 1)}, and two differentiations at zero confirm E[X] = Var(X) = λ.

MGFs also shine when working with **sums of independent random variables**. If X and Y are independent, then M_{X+Y}(t) = E[e^{t(X+Y)}] = E[e^{tX}]·E[e^{tY}] = M_X(t)·M_Y(t). Products of MGFs correspond to convolutions of distributions — a statement that would require integral calculations to prove directly. This multiplicative property is what allows the MGF proof of the Central Limit Theorem: as sums of independent copies are taken, their MGFs converge to the MGF of the normal distribution, and since MGFs uniquely determine distributions, the sum converges in distribution to normal.

The **uniqueness theorem** is what gives MGFs their real power: if two random variables have the same MGF on an open interval around zero, they have the same distribution. This means you can prove distributional equalities by comparing MGFs rather than density functions. There is one important caveat: the MGF does not always exist. If E[e^{tX}] = ∞ for all t ≠ 0 (as happens for heavy-tailed distributions like the Cauchy), the MGF fails to exist and one must use the **characteristic function** φ(t) = E[e^{itX}] instead, which always exists since |e^{itX}| = 1. Characteristic functions have analogous properties but require complex analysis — a reason to appreciate MGFs when they do exist.

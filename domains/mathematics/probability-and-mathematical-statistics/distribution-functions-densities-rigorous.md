---
id: distribution-functions-densities-rigorous
title: Distribution Functions and Densities (Rigorous)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: random-variables-as-measurable-functions
  type: hard
- id: riemann-integral-darboux-sums
  type: hard
builds-toward:
- expectation-measure-theoretic
- joint-distributions-marginals-rigorous
- characteristic-functions
tags:
- distributions
- densities
- measure-theory
stage: advanced
status: draft
---

# Distribution Functions and Densities (Rigorous)

## Core Idea
The cumulative distribution function (CDF) F(x) = P(X ≤ x) is right-continuous, non-decreasing, and uniquely determines the distribution of a random variable. A probability density function (pdf) is a measurable function f ≥ 0 where P(X ∈ A) = ∫ₐ f(x) dx with respect to Lebesgue measure. The Radon-Nikodym theorem guarantees densities exist when distributions are absolutely continuous with respect to Lebesgue measure.

## Explainer

You already know that a random variable X is a measurable function from a probability space (Ω, ℱ, P) to ℝ. The **cumulative distribution function** F(x) = P(X ≤ x) translates this abstract object into a concrete function on ℝ. Every probability about X can be recovered from F: P(a < X ≤ b) = F(b) − F(a), and P(X = a) = F(a) − F(a⁻), where F(a⁻) = lim_{x↑a} F(x) is the left-hand limit. Because X is a measurable function, the set {ω : X(ω) ≤ x} is always in ℱ and has a well-defined probability — so F(x) is well-defined for all x ∈ ℝ.

Three properties characterize every CDF. (1) F is **non-decreasing**: as x grows, the event {X ≤ x} can only get larger, so its probability can only stay the same or increase. (2) F has the correct limits: F(x) → 0 as x → −∞ (the event {X ≤ x} shrinks to the empty set) and F(x) → 1 as x → +∞ (the event approaches all of Ω). (3) F is **right-continuous**: F(x) = lim_{t↓x} F(t). Right-continuity is a convention choice — left-continuous CDFs would also work — but the right-continuous version aligns with the ≤ in the definition P(X ≤ x) and ensures point masses appear as jump discontinuities whose sizes equal P(X = a) = F(a) − F(a⁻). Any function satisfying these three properties is the CDF of some random variable.

A **probability density function (pdf)** is a non-negative measurable function f such that P(X ∈ A) = ∫_A f(x) dx for every measurable set A. When a density exists, F(x) = ∫_{−∞}^x f(t) dt, and the Darboux-sum integral you know from your prerequisites gives F'(x) = f(x) wherever f is continuous — the CDF and pdf are related by differentiation and integration. The rigorous question — when does a density exist? — is answered by the **Radon-Nikodym theorem**: a density exists if and only if the distribution of X is **absolutely continuous** with respect to Lebesgue measure, meaning P(X ∈ A) = 0 whenever A has Lebesgue measure zero. Intuitively, a continuous distribution spreads probability diffusely rather than concentrating it at isolated points.

Not all distributions have densities. The **Lebesgue decomposition theorem** states that any distribution decomposes uniquely into three parts: a **discrete** component (point masses, like a PMF), an **absolutely continuous** component (has a density), and a **singular continuous** component — distributed over a set of Lebesgue measure zero with no point masses and no density, like the Cantor distribution. This rigorous framework extends the intuitive "probability histogram" picture into a mathematically complete theory that handles pathological distributions and forms the foundation for measure-theoretic expectation, joint distributions, and characteristic functions.

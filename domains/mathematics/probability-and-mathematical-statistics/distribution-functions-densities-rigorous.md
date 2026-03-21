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

## Questions

```yaml
- question: "A random variable X has CDF F(x) satisfying F(3) = 0.7 and lim_{t↑3} F(t) = 0.5. What does this imply about X?"
  type: multiple-choice
  options:
    - "X has a probability density of 0.2 in a neighborhood of x = 3"
    - "X has a point mass of 0.2 at x = 3, meaning P(X = 3) = 0.2"
    - "The CDF is invalid because right-continuous CDFs cannot have jump discontinuities"
    - "The CDF is valid, but X cannot have a density anywhere because of this jump"
  answer: 1
  explanation: "P(X = a) = F(a) − F(a⁻), where F(a⁻) is the left-hand limit. Here, P(X = 3) = 0.7 − 0.5 = 0.2. Jump discontinuities in the CDF correspond exactly to point masses — this is not an error, it is the correct representation of a discrete component. Note that F is still right-continuous at x = 3 (F(3) = 0.7 = lim_{t↓3} F(t)), which is required. X can still have a density elsewhere if the rest of F is absolutely continuous."

- question: "A student argues: 'Since every continuous random variable has a continuous CDF, it must have a probability density function.' Which statement correctly identifies the flaw?"
  type: multiple-choice
  options:
    - "The student is correct — all continuous random variables have both a continuous CDF and a density by definition"
    - "A continuous CDF is necessary but not sufficient for a density to exist. The Cantor distribution has a continuous CDF but no density, because it is distributed over a set of Lebesgue measure zero — the correct condition is absolute continuity of the distribution with respect to Lebesgue measure"
    - "Continuous random variables can have densities only if their CDF is differentiable everywhere, not just continuous"
    - "The argument fails because CDFs are never continuous — they always have at least one jump"
  answer: 1
  explanation: "This is the key insight from the Radon-Nikodym theorem. A density f exists if and only if the distribution is absolutely continuous with respect to Lebesgue measure — meaning P(X ∈ A) = 0 whenever A has Lebesgue measure zero. The Cantor distribution is a counterexample: its CDF (the 'Devil's staircase') is continuous everywhere and increases only on a set of Lebesgue measure zero (the Cantor set). Yet no density exists, because all the probability is concentrated on that zero-measure set. Continuity of F ≠ absolute continuity of the distribution."

- question: "The CDF is defined using P(X ≤ x) rather than P(X < x), and this choice directly explains why CDFs are right-continuous rather than left-continuous."
  type: true-false
  answer: true
  explanation: "Using ≤ means F(x) captures the probability up to and including x. As we decrease t to x from above (t ↓ x), the event {X ≤ t} decreases to {X ≤ x}, so F(t) → F(x) — right-continuity. If we had used < in the definition, F(x) = P(X < x) would instead be left-continuous. The convention is a choice, but the ≤ version is standard because it aligns naturally with the CDF's role in characterizing distributions, where P(X = a) = F(a) − F(a⁻) gives jump sizes directly."

- question: "Any non-negative function f: ℝ → [0, ∞) that integrates to 1 (∫f(x) dx = 1) qualifies as a valid probability density function."
  type: true-false
  answer: false
  explanation: "The function must also be measurable (a technical but necessary condition), and more importantly, the existence of such an f does not mean a given random variable X has this density — that requires the distribution of X to be absolutely continuous with respect to Lebesgue measure (the Radon-Nikodym condition). For example, a discrete random variable X concentrated at finitely many points has no density, even though there exist non-negative functions integrating to 1. The density must satisfy P(X ∈ A) = ∫_A f(x) dx for every measurable set A, not just for A = ℝ."

- question: "The Lebesgue decomposition theorem says every probability distribution decomposes uniquely into three parts. Name these three components, and explain what a 'singular continuous' distribution is in intuitive terms."
  type: short-answer
  answer: "The three components are: (1) discrete — point masses at countably many points, like a PMF; (2) absolutely continuous — the part with a density, where probability is spread continuously over intervals; (3) singular continuous — continuous (no point masses) but concentrated entirely on a set of Lebesgue measure zero, with no density. The Cantor distribution is the canonical example: its probability is spread over the Cantor set, a closed set with measure zero that is 'dust-like' — nowhere dense but uncountably large. It has no atoms and no density, occupying a strange middle ground between discrete and continuous."
  explanation: "The singular continuous component is genuinely pathological and rarely appears in applied probability, but its existence shows that the discrete/continuous dichotomy is incomplete as a classification. Measure theory is necessary to give a complete account of what distributions can exist. In practice, the rigorous framework matters most when dealing with mixed distributions (part discrete, part continuous) and when proving theorems about convergence of distributions, where the full decomposition clarifies which assumptions are actually needed."
```

## Explainer

You already know that a random variable X is a measurable function from a probability space (Ω, ℱ, P) to ℝ. The **cumulative distribution function** F(x) = P(X ≤ x) translates this abstract object into a concrete function on ℝ. Every probability about X can be recovered from F: P(a < X ≤ b) = F(b) − F(a), and P(X = a) = F(a) − F(a⁻), where F(a⁻) = lim_{x↑a} F(x) is the left-hand limit. Because X is a measurable function, the set {ω : X(ω) ≤ x} is always in ℱ and has a well-defined probability — so F(x) is well-defined for all x ∈ ℝ.

Three properties characterize every CDF. (1) F is **non-decreasing**: as x grows, the event {X ≤ x} can only get larger, so its probability can only stay the same or increase. (2) F has the correct limits: F(x) → 0 as x → −∞ (the event {X ≤ x} shrinks to the empty set) and F(x) → 1 as x → +∞ (the event approaches all of Ω). (3) F is **right-continuous**: F(x) = lim_{t↓x} F(t). Right-continuity is a convention choice — left-continuous CDFs would also work — but the right-continuous version aligns with the ≤ in the definition P(X ≤ x) and ensures point masses appear as jump discontinuities whose sizes equal P(X = a) = F(a) − F(a⁻). Any function satisfying these three properties is the CDF of some random variable.

A **probability density function (pdf)** is a non-negative measurable function f such that P(X ∈ A) = ∫_A f(x) dx for every measurable set A. When a density exists, F(x) = ∫_{−∞}^x f(t) dt, and the Darboux-sum integral you know from your prerequisites gives F'(x) = f(x) wherever f is continuous — the CDF and pdf are related by differentiation and integration. The rigorous question — when does a density exist? — is answered by the **Radon-Nikodym theorem**: a density exists if and only if the distribution of X is **absolutely continuous** with respect to Lebesgue measure, meaning P(X ∈ A) = 0 whenever A has Lebesgue measure zero. Intuitively, a continuous distribution spreads probability diffusely rather than concentrating it at isolated points.

Not all distributions have densities. The **Lebesgue decomposition theorem** states that any distribution decomposes uniquely into three parts: a **discrete** component (point masses, like a PMF), an **absolutely continuous** component (has a density), and a **singular continuous** component — distributed over a set of Lebesgue measure zero with no point masses and no density, like the Cantor distribution. This rigorous framework extends the intuitive "probability histogram" picture into a mathematically complete theory that handles pathological distributions and forms the foundation for measure-theoretic expectation, joint distributions, and characteristic functions.

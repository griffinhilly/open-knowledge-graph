---
id: characteristic-functions
title: Characteristic Functions
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: moment-generating-functions
  type: soft
- id: variance-higher-moments-rigorous
  type: hard
- id: complex-exponential-function
  type: soft
builds-toward:
- central-limit-theorem-rigorous
- convergence-in-distribution
tags:
- characteristic-functions
- fourier-analysis
- moments
stage: advanced
status: draft
---

# Characteristic Functions

## Core Idea
The characteristic function is φ(t) = E[e^{itX}], which exists for all real t. Unlike the MGF, φ always exists, making it more versatile. The characteristic function is the Fourier transform of the probability distribution; inversion formulas recover the CDF from φ. Convergence of characteristic functions implies convergence of distributions.

## How It's Best Learned
Compute characteristic functions for standard distributions. Apply the inversion formula to recover CDFs. Use characteristic functions to prove the central limit theorem.

## Common Misconceptions
- Confusing characteristic and moment generating functions; use φ(t) = E[e^{itX}] for characteristic. - Thinking moment-generating functions always exist; MGFs may not, but characteristic functions always do. - Forgetting to use the complex exponential in the definition.

## Explainer

You've studied **moment-generating functions** (MGFs), which use the transform M(t) = E[e^{tX}]. The problem with MGFs is that e^{tX} can become unbounded for large X, so the expectation may not exist — for heavy-tailed distributions like the Cauchy, the MGF is infinite everywhere except t = 0. The **characteristic function** φ(t) = E[e^{itX}] fixes this by using a complex exponential: since |e^{itX}| = 1 for all real t and X (by Euler's formula, e^{itX} traces the unit circle in the complex plane), the integral ∫ e^{itx} dF(x) always converges absolutely. The characteristic function exists for every probability distribution, making it a universal tool where the MGF may fail.

The complex exponential e^{itX} = cos(tX) + i·sin(tX) transforms the probability distribution into the **frequency domain** — characteristic functions are exactly the **Fourier transform** of the probability measure. All the tools of Fourier analysis therefore apply. The transform is invertible: the **inversion formula** recovers F (and the density, if it exists) from φ, so different distributions cannot share the same characteristic function. Convolution of independent random variables corresponds to pointwise multiplication of characteristic functions: if X ⊥ Y, then φ_{X+Y}(t) = φ_X(t) · φ_Y(t). This multiplication property is why sums of independent random variables are tractable — adding random variables becomes multiplying two functions, a far simpler operation.

Computing moments from φ is analogous to using the MGF: the k-th derivative at 0 gives E[X^k] up to a factor of i, specifically E[X^k] = i^{−k} φ^{(k)}(0). The characteristic function of a standard normal is φ(t) = e^{−t²/2} — a Gaussian in the frequency domain. This is no coincidence: the normal distribution is its own Fourier transform (up to scaling), a reflection of the normal's special symmetry properties.

The deepest result connecting characteristic functions to probability theory is the **continuity theorem**: if φ_{Xₙ}(t) → φ(t) pointwise for every t, and φ is continuous at 0, then Xₙ converges in distribution to the random variable with characteristic function φ. This is the key tool for proving limit theorems. To prove the **central limit theorem** rigorously: (1) compute φ_{Xᵢ}(t/√n) by Taylor-expanding around 0, (2) show the n-fold product of these characteristic functions converges pointwise to e^{−t²/2} using the identity (1 + x/n)ⁿ → eˣ, (3) invoke the continuity theorem to conclude convergence in distribution to N(0,1). Each step is clean algebra; no heavy measure-theoretic machinery beyond dominated convergence is needed. Characteristic functions thus reduce distributional convergence questions to pointwise limits of complex-valued functions.

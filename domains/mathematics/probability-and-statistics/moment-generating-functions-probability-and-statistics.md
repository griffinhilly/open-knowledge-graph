---
id: moment-generating-functions-probability-and-statistics
title: Moment Generating Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- central-limit-theorem-theory
tags:
- mgf
- probability
- moments
stage: formal-systems
status: draft
---

# Moment Generating Functions

## Core Idea
The moment generating function is M(t) = E[e^{tX}]. Its derivatives at t=0 give moments: M^{(n)}(0) = E[X^n]. MGFs uniquely determine distributions and are useful for finding distributions of sums of random variables.

## How It's Best Learned
Calculate MGFs for simple distributions like Bernoulli and exponential. Use MGFs to find moments without direct integration. Compare MGFs of related distributions to understand relationships.

## Common Misconceptions
Forgetting that MGFs only exist for distributions with appropriate moment conditions. Confusing MGF with characteristic function. Not recognizing that MGF uniqueness determines uniqueness of distributions.

## Explainer

You already know that expected value compresses a distribution into a single number, and that exponential functions like e^x are well-behaved and differentiable everywhere. The moment generating function combines these ideas in a clever way: instead of computing E[X] directly, define M(t) = E[e^{tX}], a function of a new variable t. When t = 0, M(0) = E[e^0] = E[1] = 1. The power of this construction appears when you differentiate.

Because e^{tX} has the Taylor expansion 1 + tX + (t²X²)/2! + (t³X³)/3! + ···, its expected value is M(t) = 1 + tE[X] + (t²/2!)E[X²] + (t³/3!)E[X³] + ···. Differentiating once and evaluating at t = 0 picks out E[X]; differentiating twice gives E[X²]; the n-th derivative at t = 0 gives the **n-th moment** E[Xⁿ]. This is why the function is called a moment-generating function — it encodes all moments simultaneously. For example, variance can be recovered as E[X²] − (E[X])², which is M''(0) − (M'(0))².

The MGF is especially powerful for studying sums of independent random variables. If X and Y are independent, then M_{X+Y}(t) = E[e^{t(X+Y)}] = E[e^{tX}]·E[e^{tY}] = M_X(t)·M_Y(t). Multiplying MGFs corresponds to adding independent random variables — much cleaner than convolving their densities directly. This is the key mechanism behind many proofs, including the Central Limit Theorem, where you show that the MGF of the standardized sum converges to e^{t²/2}, the MGF of the standard normal.

The **uniqueness theorem** for MGFs says: if two distributions have the same MGF in a neighborhood of t = 0, they are identical. This makes the MGF an alternative characterization of a distribution — you can prove two random variables have the same distribution by showing their MGFs agree, without ever comparing their densities directly. The catch is that MGFs may not exist if E[e^{tX}] is infinite for all t ≠ 0, as can happen for heavy-tailed distributions. When the MGF fails, the closely related **characteristic function** E[e^{itX}] (with imaginary t) always exists, but that requires complex analysis to use.

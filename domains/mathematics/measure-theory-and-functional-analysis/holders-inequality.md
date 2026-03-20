---
id: holders-inequality
title: Hölder's Inequality
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lp-norm-metric
  type: hard
builds-toward:
- minkowski-inequality-lp
tags:
- lp-spaces
- inequalities
stage: advanced
status: draft
---

# Hölder's Inequality

## Core Idea
For 1 < p < ∞ with 1/p + 1/q = 1, Hölder's inequality states ∫|fg| ≤ ‖f‖_p ‖g‖_q. This is the key inequality enabling duality in L^p theory. When p = q = 2, it reduces to Cauchy–Schwarz.

## Explainer

You already know the **Lᵖ norm** ‖f‖_p = (∫|f|ᵖ)^(1/p), which measures the "size" of a function in a way that weights extreme values more heavily as p grows. Hölder's inequality answers the question: how large can the integral of the product |fg| be, given that you know ‖f‖_p and ‖g‖_q? The answer is the elegant bound ∫|fg| ≤ ‖f‖_p ‖g‖_q — and the condition 1/p + 1/q = 1 is precisely what makes this tight.

The pair (p, q) satisfying 1/p + 1/q = 1 are called **conjugate exponents**. When p = 2, we get q = 2 as well, and Hölder's inequality becomes the Cauchy–Schwarz inequality ∫|fg| ≤ ‖f‖₂ ‖g‖₂ — a fact you may recognize from inner product spaces. Hölder generalizes this: for p = 3 and q = 3/2, Hölder's inequality handles situations where f has L³ integrability but g is only in L^(3/2). The conjugate condition is not arbitrary; it emerges from the proof via **Young's inequality** (ab ≤ aᵖ/p + bq/q for a, b ≥ 0), which in turn follows from the convexity of the exponential function.

The proof strategy is instructive: normalize by replacing f with f/‖f‖_p and g with g/‖g‖_q, reducing to the case where both norms are 1 and you need to show ∫|fg| ≤ 1. Then apply Young's inequality pointwise to get |f(x)g(x)| ≤ |f(x)|ᵖ/p + |g(x)|^q/q, and integrate both sides. The right-hand side integrates to 1/p + 1/q = 1. This argument reveals why the conjugate condition is necessary: it is exactly what makes Young's inequality integrate to 1.

The deepest significance of Hölder's inequality is its role in **Lᵖ duality**. Every bounded linear functional on Lᵖ can be represented as integration against some function in Lq — written symbolically as (Lᵖ)* ≅ Lq. This duality underpins the Riesz representation theorem and is central to functional analysis. Hölder's inequality is what makes this identification *bounded*: without it, you couldn't control ∫fg by separate norms. It also immediately implies the Minkowski inequality (triangle inequality for Lᵖ norms), which is the next step in the theory.

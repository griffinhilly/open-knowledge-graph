---
id: weierstrass-m-test
title: Weierstrass M-Test
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-convergence-functions
  type: hard
- id: series-convergence-rigorous
  type: hard
builds-toward:
- uniform-convergence-power-series
tags:
- weierstrass-m-test
- uniform-convergence
- series
stage: advanced
status: draft
---

# Weierstrass M-Test

## Core Idea
If |fₙ(x)| ≤ Mₙ for all x in a set S and all n, and if ∑Mₙ converges, then ∑fₙ(x) converges uniformly on S. This is the workhorse for proving uniform convergence of series without explicit calculation. It applies to power series, Fourier series, and integral representations.

## Explainer

From your study of uniform convergence, you know that a series of functions ∑fₙ(x) converges uniformly if the partial sums can be made uniformly close to the limit — meaning the worst-case error over all x in S can be driven to zero by taking enough terms. The trouble with checking this directly is that you need to control a supremum over an infinite set. The **Weierstrass M-test** sidesteps this by replacing the x-dependent functions with x-independent constants: if you can bound each |fₙ(x)| above by a number Mₙ that does not depend on x, and if the series ∑Mₙ of constants converges, then you have uniform convergence for free.

The proof uses comparison with the tail of ∑Mₙ. For any ε > 0, the convergence of ∑Mₙ guarantees that the tail ∑_{n=N+1}^∞ Mₙ < ε for large enough N. But then the tail of the function series satisfies |∑_{n=N+1}^∞ fₙ(x)| ≤ ∑_{n=N+1}^∞ |fₙ(x)| ≤ ∑_{n=N+1}^∞ Mₙ < ε for *every* x in S simultaneously. That uniform bound is exactly what uniform convergence requires — the same N works everywhere, not just pointwise. This is why the test is so useful: you delegate the convergence question to a numerical series, where you already have many tools.

A standard application is the power series ∑xⁿ/n². On the closed interval [−1, 1], you have |xⁿ/n²| ≤ 1/n², and ∑1/n² = π²/6 converges. So the M-test immediately gives uniform convergence on [−1, 1]. You did not have to track how the partial sums behave as x varies — the constants did all the work. Once uniform convergence is established, you can swap limits with integration or pass differentiation through the sum, conclusions that would not be valid from mere pointwise convergence alone.

The test is sufficient but not necessary: a series can converge uniformly even when no suitable sequence of constants Mₙ exists with ∑Mₙ convergent. When the M-test fails, uniform convergence may still hold by more delicate arguments (Dirichlet's test, Abel's test). But in practice — especially for power series inside the radius of convergence, and for Fourier series with summable coefficient sequences — the M-test is almost always the first tool to reach for. Its elegance lies in translating a functional analysis problem (uniform convergence of functions) into a classical analysis problem (convergence of a numerical series) where comparison, ratio, and integral tests all apply.



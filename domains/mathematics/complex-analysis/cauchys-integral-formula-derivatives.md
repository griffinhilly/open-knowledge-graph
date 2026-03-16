---
id: cauchys-integral-formula-derivatives
title: Cauchy's Integral Formula for Derivatives
domain: mathematics
course: complex-analysis
prerequisites:
- id: cauchys-integral-formula
  type: hard
builds-toward:
- taylor-series-complex
- liouville-theorem
tags:
- derivatives
- integral-formula
- cauchy
stage: advanced
status: draft
---

# Cauchy's Integral Formula for Derivatives

## Core Idea
If f is holomorphic in a simply connected domain D and γ encloses z₀, then f^(n)(z₀) = (n!/2πi) ∮_γ f(z)/(z - z₀)^(n+1) dz for any positive integer n. This shows every holomorphic function is infinitely differentiable and all derivatives are also holomorphic. It is the gateway to Taylor series.

## Explainer

From Cauchy's Integral Formula you know that the value of a holomorphic function at any interior point is completely determined by its values on the boundary: f(z₀) = (1/2πi) ∮_γ f(z)/(z - z₀) dz. The generalization to derivatives extends this result: not just f(z₀) but every derivative f^(n)(z₀) is recoverable from the boundary integral, via f^(n)(z₀) = (n!/2πi) ∮_γ f(z)/(z - z₀)^(n+1) dz. Each successive derivative introduces one higher power of (z - z₀)^(−1) in the denominator and one factor of n! in the numerator.

The derivation follows by differentiating Cauchy's Integral Formula with respect to z₀ under the integral sign. Starting from f(z₀) = (1/2πi) ∮ f(z)/(z - z₀) dz, differentiate the integrand: d/dz₀[1/(z - z₀)] = 1/(z - z₀)². Differentiating n times: d^n/dz₀^n[1/(z - z₀)] = n!/(z - z₀)^(n+1). This is simply the power rule applied to the function of z₀. The formula for f^(n)(z₀) follows directly, with the factor n! appearing because differentiating 1/(z - z₀) exactly n times produces n! in the numerator.

The conceptual significance is profound. In real analysis, differentiability once does not imply differentiability twice — a function can have exactly one derivative and no more. In complex analysis, holomorphicity (complex differentiability) implies **infinite differentiability**: since the integral formula exists for every n, f^(n)(z₀) exists for every n, and each derivative is again holomorphic. This is one of the deepest asymmetries between real and complex analysis. Holomorphic functions form a far more rigid class than real-differentiable functions.

The practical payoff is in computing Taylor coefficients. If f has a Taylor series f(z) = Σ aₙ(z - z₀)ⁿ, the n-th coefficient is aₙ = f^(n)(z₀)/n!. Substituting the derivative formula gives aₙ = (1/2πi) ∮_γ f(z)/(z - z₀)^(n+1) dz. This bridges the integral representation of a holomorphic function and its power series expansion, and it is the key step in proving that every holomorphic function equals its Taylor series on its disk of convergence — the result you will encounter next.

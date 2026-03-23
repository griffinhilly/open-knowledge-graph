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
status: validated
---

# Cauchy's Integral Formula for Derivatives

## Core Idea
If f is holomorphic in a simply connected domain D and γ encloses z₀, then f^(n)(z₀) = (n!/2πi) ∮_γ f(z)/(z - z₀)^(n+1) dz for any positive integer n. This shows every holomorphic function is infinitely differentiable and all derivatives are also holomorphic. It is the gateway to Taylor series.

## Questions

```yaml
- question: "A function f is holomorphic on a domain D. Which statement correctly describes f's differentiability?"
  type: multiple-choice
  options:
    - "f may fail to have a second derivative at isolated points, as in real analysis"
    - "f must have derivatives of all orders, and each derivative is also holomorphic"
    - "f has at most finitely many derivatives, determined by its complexity"
    - "f has infinitely many derivatives, but they need not be holomorphic"
  answer: 1
  explanation: "Holomorphicity implies infinite differentiability — a fundamental asymmetry with real analysis. In real analysis, differentiability once does not imply differentiability twice. But since Cauchy's integral formula exists for every order n (just differentiate under the integral sign n times), f^(n)(z₀) exists for all n, and each derivative is again holomorphic. Option D is tempting but wrong: each derivative is also holomorphic, not merely differentiable."

- question: "You want to compute the n-th derivative of a holomorphic function f at z₀ using Cauchy's formula. Compared to the formula for f(z₀) itself, the formula for f^(n)(z₀):"
  type: multiple-choice
  options:
    - "Replaces the denominator (z − z₀) with (z − z₀)^n"
    - "Divides by n! to normalize for the repeated differentiation"
    - "Multiplies by n! and replaces (z − z₀) with (z − z₀)^(n+1) in the denominator"
    - "Is identical — you differentiate the result after evaluating the contour integral"
  answer: 2
  explanation: "Differentiating 1/(z − z₀) with respect to z₀ n times gives n!/(z − z₀)^(n+1) by the power rule. This factor of n! appears in the numerator and the denominator gains one extra power of (z − z₀) per differentiation. The full formula is f^(n)(z₀) = (n!/2πi) ∮ f(z)/(z − z₀)^(n+1) dz. Option A (wrong exponent) and option B (divides rather than multiplies) are the most common errors."

- question: "In real analysis, differentiability once implies differentiability infinitely many times, just as in complex analysis."
  type: true-false
  answer: false
  explanation: "This is one of the deepest asymmetries between real and complex analysis. In real analysis, a function can be differentiable exactly once (or any finite number of times) without being differentiable a second time. Complex differentiability (holomorphicity) is far more restrictive: the Cauchy integral formula allows recovery of every derivative from boundary values, so a holomorphic function is automatically infinitely differentiable. The rigidity of holomorphic functions — infinite differentiability, equality with their Taylor series — has no real-analysis counterpart."

- question: "Cauchy's integral formula for the n-th derivative can be derived by differentiating the original integral formula for f(z₀) with respect to z₀ under the integral sign."
  type: true-false
  answer: true
  explanation: "The derivation is exactly this: start from f(z₀) = (1/2πi) ∮ f(z)/(z − z₀) dz and differentiate the integrand with respect to z₀. Each differentiation applies the power rule to 1/(z − z₀), producing an extra power in the denominator and accumulating a factorial in the numerator. After n differentiations, d^n/dz₀^n[1/(z − z₀)] = n!/(z − z₀)^(n+1), giving the formula directly."

- question: "Why does holomorphicity in complex analysis imply infinite differentiability, while differentiability in real analysis does not?"
  type: short-answer
  answer: "In complex analysis, Cauchy's integral formula expresses f(z₀) as a contour integral over the boundary. Differentiating this formula with respect to z₀ under the integral sign produces a valid formula for f'(z₀), and there is no obstruction to repeating this process for any n — so all derivatives exist. In real analysis, there is no analogous integral representation that forces derivatives to exist beyond a given order; a function can have a derivative at every point without that derivative being itself differentiable."
  explanation: "The key is that the integral formula gives f^(n)(z₀) for every n without requiring additional assumptions. Holomorphicity is a single condition that turns out to entail the entire tower of derivatives. In real analysis, each level of differentiability is an independent condition — you must separately assume f', f'', etc. exist. This is why complex analysis has such a richer theory: one mild-seeming condition implies an enormous amount of structure."
```

## Explainer

From Cauchy's Integral Formula you know that the value of a holomorphic function at any interior point is completely determined by its values on the boundary: f(z₀) = (1/2πi) ∮_γ f(z)/(z - z₀) dz. The generalization to derivatives extends this result: not just f(z₀) but every derivative f^(n)(z₀) is recoverable from the boundary integral, via f^(n)(z₀) = (n!/2πi) ∮_γ f(z)/(z - z₀)^(n+1) dz. Each successive derivative introduces one higher power of (z - z₀)^(−1) in the denominator and one factor of n! in the numerator.

The derivation follows by differentiating Cauchy's Integral Formula with respect to z₀ under the integral sign. Starting from f(z₀) = (1/2πi) ∮ f(z)/(z - z₀) dz, differentiate the integrand: d/dz₀[1/(z - z₀)] = 1/(z - z₀)². Differentiating n times: d^n/dz₀^n[1/(z - z₀)] = n!/(z - z₀)^(n+1). This is simply the power rule applied to the function of z₀. The formula for f^(n)(z₀) follows directly, with the factor n! appearing because differentiating 1/(z - z₀) exactly n times produces n! in the numerator.

The conceptual significance is profound. In real analysis, differentiability once does not imply differentiability twice — a function can have exactly one derivative and no more. In complex analysis, holomorphicity (complex differentiability) implies **infinite differentiability**: since the integral formula exists for every n, f^(n)(z₀) exists for every n, and each derivative is again holomorphic. This is one of the deepest asymmetries between real and complex analysis. Holomorphic functions form a far more rigid class than real-differentiable functions.

The practical payoff is in computing Taylor coefficients. If f has a Taylor series f(z) = Σ aₙ(z - z₀)ⁿ, the n-th coefficient is aₙ = f^(n)(z₀)/n!. Substituting the derivative formula gives aₙ = (1/2πi) ∮_γ f(z)/(z - z₀)^(n+1) dz. This bridges the integral representation of a holomorphic function and its power series expansion, and it is the key step in proving that every holomorphic function equals its Taylor series on its disk of convergence — the result you will encounter next.

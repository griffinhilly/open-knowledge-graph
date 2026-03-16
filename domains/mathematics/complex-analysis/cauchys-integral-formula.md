---
id: cauchys-integral-formula
title: Cauchy's Integral Formula
domain: mathematics
course: complex-analysis
prerequisites:
- id: cauchys-theorem
  type: hard
builds-toward:
- cauchys-integral-formula-derivatives
- taylor-series-complex
tags:
- cauchys-integral-formula
- reconstruction
- values-from-boundary
stage: advanced
status: draft
---

# Cauchy's Integral Formula

## Core Idea
If f is holomorphic in a simply connected domain D and γ is a simple closed contour in D enclosing a point z₀, then f(z₀) = (1/2πi) ∮_γ f(z)/(z - z₀) dz. This formula says the value of an analytic function at an interior point is completely determined by its values on any surrounding contour — a rigidity that has no real analogue.

## How It's Best Learned
Apply this formula to f(z) = z² and a circle around z = 0 to verify it gives f(0) = 0. This may seem trivial, but the power comes when f is complicated and you can choose any contour.

## Common Misconceptions
Thinking this is just an integral formula; it reveals that analytic functions are completely rigid. Assuming the contour can be any curve; it must enclose z₀ and lie in the domain of analyticity.

## Explainer

**Cauchy's theorem** — your prerequisite — told you that if f is holomorphic everywhere inside and on a simple closed contour γ, then ∮_γ f(z) dz = 0. The key word is "everywhere": holomorphic with no exceptions. Now consider f(z)/(z − z₀) where z₀ is a point *inside* γ. This function is not holomorphic at z₀ (it blows up there), so Cauchy's theorem doesn't apply, and the integral need not be zero. Cauchy's integral formula tells you exactly what the integral *is*: it equals 2πi · f(z₀). Rearranged, this gives **f(z₀) = (1/2πi) ∮_γ f(z)/(z − z₀) dz**.

The formula is saying something philosophically extraordinary: the value of an analytic function at an *interior* point is completely determined by its values on *any surrounding contour*. Change f anywhere in the interior, and you automatically change f everywhere on the boundary (and vice versa). There is no real analogue of this. For a smooth real function f: ℝ → ℝ, you can change f on (0,1) without affecting f at x = 2. But for a holomorphic function, such surgery is impossible — the function's values are globally locked together by the condition of complex differentiability. The formula makes this rigidity explicit and quantitative.

To build intuition, observe what happens when f ≡ 1 (the constant function 1). The formula gives 1 = (1/2πi) ∮_γ 1/(z − z₀) dz, meaning ∮_γ dz/(z − z₀) = 2πi. You can verify this directly for a circle γ parameterized as z = z₀ + re^{iθ}: the integral becomes ∫₀^{2π} (ire^{iθ})/(re^{iθ}) dθ = ∫₀^{2π} i dθ = 2πi. The same 2πi appears for *any* simple closed contour enclosing z₀ — not just circles. This independence from contour shape (as long as z₀ is enclosed and the region is free of singularities) is precisely Cauchy's theorem protecting you.

The formula generalizes powerfully: by differentiating under the integral sign with respect to z₀, you get formulas for all higher derivatives — f^(n)(z₀) = (n!/2πi) ∮_γ f(z)/(z − z₀)^{n+1} dz. This shocking result means that a holomorphic function is infinitely differentiable — all derivatives exist automatically. Combined with Taylor series, it shows that every holomorphic function is locally a convergent power series. The Cauchy integral formula is the seed from which almost all of complex analysis grows.

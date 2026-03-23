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
status: validated
---

# Cauchy's Integral Formula

## Core Idea
If f is holomorphic in a simply connected domain D and γ is a simple closed contour in D enclosing a point z₀, then f(z₀) = (1/2πi) ∮_γ f(z)/(z - z₀) dz. This formula says the value of an analytic function at an interior point is completely determined by its values on any surrounding contour — a rigidity that has no real analogue.

## How It's Best Learned
Apply this formula to f(z) = z² and a circle around z = 0 to verify it gives f(0) = 0. This may seem trivial, but the power comes when f is complicated and you can choose any contour.

## Common Misconceptions
Thinking this is just an integral formula; it reveals that analytic functions are completely rigid. Assuming the contour can be any curve; it must enclose z₀ and lie in the domain of analyticity.

## Questions

```yaml
- question: "Cauchy's theorem states that ∮_γ f(z) dz = 0 when f is holomorphic everywhere inside and on γ. Why does this theorem NOT immediately give ∮_γ f(z)/(z − z₀) dz = 0 when z₀ is inside γ?"
  type: multiple-choice
  options:
    - "Because f(z)/(z − z₀) fails to be holomorphic at z₀, which lies inside γ"
    - "Because the contour γ must be a circle for Cauchy's theorem to apply"
    - "Because f(z)/(z − z₀) is not bounded on γ when z₀ is close to the contour"
    - "Because Cauchy's theorem requires the function to be real-valued on the contour"
  answer: 0
  explanation: "Cauchy's theorem requires holomorphicity everywhere *inside and on* the contour. The function g(z) = f(z)/(z − z₀) has a singularity at z = z₀, which sits inside γ. So g is not holomorphic everywhere inside γ, and Cauchy's theorem cannot be applied. Instead of giving zero, the integral gives 2πi·f(z₀) — precisely Cauchy's integral formula. This is the key: the formula arises because we are forced to handle a function with an interior singularity."

- question: "You want to compute f(i) for f(z) = z³ + 2z using Cauchy's integral formula. Which statement about the choice of contour is correct?"
  type: multiple-choice
  options:
    - "You must use a circle of radius 1 centered at i for the formula to be exact"
    - "You can use any simple closed contour that encloses i and stays within a simply connected region where f is holomorphic"
    - "Larger contours give better approximations, so you should use the largest feasible contour"
    - "The contour must not enclose any other points besides i for the formula to apply"
  answer: 1
  explanation: "Cauchy's integral formula gives f(z₀) = (1/2πi) ∮_γ f(z)/(z − z₀) dz for *any* simple closed contour enclosing z₀, as long as f is holomorphic in the simply connected region bounded by γ. Since f(z) = z³ + 2z is holomorphic everywhere (it's a polynomial), any simple closed contour enclosing i works — circle, square, ellipse, or any other shape. The result is always f(i) = i³ + 2i = −i + 2i = i. Independence from contour shape (within a holomorphic region) is a direct consequence of Cauchy's theorem."

- question: "Cauchy's integral formula implies that a holomorphic function is automatically infinitely differentiable — all derivatives of all orders exist."
  type: true-false
  answer: true
  explanation: "By differentiating both sides of Cauchy's integral formula with respect to z₀ (differentiating under the integral sign), you obtain formulas for all higher derivatives: f^(n)(z₀) = (n!/2πi) ∮_γ f(z)/(z − z₀)^{n+1} dz. Since the right side is well-defined whenever f is holomorphic and z₀ is inside γ, every derivative exists automatically. This is a striking contrast to real analysis, where a function can be once differentiable without being twice differentiable. Complex differentiability once is a much stronger condition — it entails differentiability infinitely many times."

- question: "A smooth real function f: ℝ → ℝ has the same 'boundary determines interior' property as a holomorphic function: knowing f on the boundary of an interval determines all its interior values."
  type: true-false
  answer: false
  explanation: "For real smooth functions, this is completely false. You can freely change f on the interior of [0,1] without affecting its values at the endpoints. For example, f(x) = x and g(x) = x + sin(πx) both satisfy f(0) = g(0) = 0 and f(1) = g(1) = 1, but differ everywhere in between. Holomorphic functions have a rigidity with no real analogue: complex differentiability locks the function's values together globally. Cauchy's integral formula makes this explicit — boundary values on *any* surrounding contour completely reconstruct interior values."

- question: "Why does Cauchy's integral formula represent something genuinely new about holomorphic functions that has no parallel in real analysis? What structural feature of complex differentiability makes it possible?"
  type: short-answer
  answer: "In real analysis, a function's values in the interior of a domain are independent of its boundary values — you can modify f on (0,1) without touching f(0) or f(1). Complex differentiability (holomorphicity) imposes a rigid global constraint: the Cauchy-Riemann equations couple the real and imaginary parts of f so tightly that no isolated local modification is possible. This coupling is encoded in Cauchy's theorem (∮ f dz = 0), which forces the integral of f(z)/(z−z₀) to equal exactly 2πi·f(z₀). The interior value is not just influenced by boundary values — it is completely reconstructed from them."
  explanation: "This rigidity explains why holomorphic functions are so well-behaved (analytic, infinitely differentiable, expressible as convergent power series) compared to smooth real functions. The formula is not a computational trick — it is the quantitative expression of a deep structural rigidity that has no real-variable analogue."
```

## Explainer

**Cauchy's theorem** — your prerequisite — told you that if f is holomorphic everywhere inside and on a simple closed contour γ, then ∮_γ f(z) dz = 0. The key word is "everywhere": holomorphic with no exceptions. Now consider f(z)/(z − z₀) where z₀ is a point *inside* γ. This function is not holomorphic at z₀ (it blows up there), so Cauchy's theorem doesn't apply, and the integral need not be zero. Cauchy's integral formula tells you exactly what the integral *is*: it equals 2πi · f(z₀). Rearranged, this gives **f(z₀) = (1/2πi) ∮_γ f(z)/(z − z₀) dz**.

The formula is saying something philosophically extraordinary: the value of an analytic function at an *interior* point is completely determined by its values on *any surrounding contour*. Change f anywhere in the interior, and you automatically change f everywhere on the boundary (and vice versa). There is no real analogue of this. For a smooth real function f: ℝ → ℝ, you can change f on (0,1) without affecting f at x = 2. But for a holomorphic function, such surgery is impossible — the function's values are globally locked together by the condition of complex differentiability. The formula makes this rigidity explicit and quantitative.

To build intuition, observe what happens when f ≡ 1 (the constant function 1). The formula gives 1 = (1/2πi) ∮_γ 1/(z − z₀) dz, meaning ∮_γ dz/(z − z₀) = 2πi. You can verify this directly for a circle γ parameterized as z = z₀ + re^{iθ}: the integral becomes ∫₀^{2π} (ire^{iθ})/(re^{iθ}) dθ = ∫₀^{2π} i dθ = 2πi. The same 2πi appears for *any* simple closed contour enclosing z₀ — not just circles. This independence from contour shape (as long as z₀ is enclosed and the region is free of singularities) is precisely Cauchy's theorem protecting you.

The formula generalizes powerfully: by differentiating under the integral sign with respect to z₀, you get formulas for all higher derivatives — f^(n)(z₀) = (n!/2πi) ∮_γ f(z)/(z − z₀)^{n+1} dz. This shocking result means that a holomorphic function is infinitely differentiable — all derivatives exist automatically. Combined with Taylor series, it shows that every holomorphic function is locally a convergent power series. The Cauchy integral formula is the seed from which almost all of complex analysis grows.

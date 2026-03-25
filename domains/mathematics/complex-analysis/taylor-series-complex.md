---
id: taylor-series-complex
title: Taylor Series for Complex Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: cauchys-integral-formula-derivatives
  type: hard
- id: taylor-series
  type: hard
- id: complex-trigonometric-functions
  type: soft
builds-toward:
- power-series-complex-plane
- laurent-series
tags:
- taylor-series
- power-series
- analytic
stage: advanced
status: validated
---
# Taylor Series for Complex Functions

## Core Idea
Every holomorphic function f on a disk |z - z₀| < R is equal to its Taylor series f(z) = Σ f^(n)(z₀)/n! (z - z₀)^n, which converges for |z - z₀| < R. The radius of convergence R is the distance to the nearest singularity. This makes complex analytic functions completely rigid: the Taylor coefficients encode all information.

## How It's Best Learned
Compute the Taylor series of f(z) = 1/(1-z) around z = 0 and verify the radius of convergence is 1. Understand why: the function has a singularity at z = 1, which is distance 1 from the center.

## Common Misconceptions
Assuming every power series converges everywhere or nowhere; the radius of convergence is finite for holomorphic functions with singularities. Confusing the radius of convergence with the domain of the function.

## Questions

```yaml
- question: "The function f(x) = 1/(1 + x²) is smooth and well-defined for all real x, yet its Taylor series around x = 0 converges only for |x| < 1. What is the correct explanation?"
  type: multiple-choice
  options:
    - "The function grows too steeply beyond x = 1 for polynomial approximation to keep up"
    - "The Taylor series converges only where the function is increasing, and 1/(1+x²) decreases for x > 0"
    - "In the complex plane, f has singularities at z = ±i, which are distance 1 from the origin — those singularities govern the radius of convergence"
    - "The function's Taylor coefficients become large enough at n = 1 to cause divergence"
  answer: 2
  explanation: "This is the key insight of complex Taylor series: the radius of convergence equals the distance to the nearest singularity *in the complex plane*, not on the real line. Real analysis gives no clue why convergence stops at |x| = 1 — the function is perfectly smooth there. Complex analysis reveals the hidden obstruction: f(z) = 1/(1+z²) has poles at z = i and z = -i, each exactly distance 1 from the origin. The singularities are invisible on the real axis but they control the real Taylor series."

- question: "Two holomorphic functions f and g agree on a small open disk D. What must be true on their shared domain?"
  type: multiple-choice
  options:
    - "f and g agree only within D; outside D their values may diverge"
    - "f and g agree everywhere on their entire shared domain"
    - "f and g agree provided they share the same singularities"
    - "f and g agree only if D contains a zero of f − g"
  answer: 1
  explanation: "This is the **identity theorem** for holomorphic functions. Because a holomorphic function is *equal* to its Taylor series on any disk (not merely approximated), the Taylor coefficients at any center point completely determine the function everywhere. Two functions agreeing on an open set must have identical Taylor coefficients there, so they are identical on their entire shared domain. There is no real-analysis analogue — two smooth functions can match on an interval while differing elsewhere, but holomorphic functions cannot."

- question: "In complex analysis, a holomorphic function equals its Taylor series exactly within the disk of convergence — not approximately, as in real analysis."
  type: true-false
  answer: true
  explanation: "This is the central distinction between real and complex power series. In real analysis, Taylor series are approximations — even smooth functions are only guaranteed to match their Taylor series in the limit, and the error can be nonzero at any finite order. In complex analysis, if f is holomorphic on |z − z₀| < R, then f(z) = Σ aₙ(z−z₀)ⁿ exactly, with zero error, everywhere on that disk. This follows from Cauchy's Integral Formula for derivatives and gives holomorphic functions their striking rigidity."

- question: "The radius of convergence of the Taylor series of a complex function is determined by the behavior of the function near the real expansion point."
  type: true-false
  answer: false
  explanation: "The radius of convergence is the distance from the expansion center to the nearest **singularity in the complex plane** — which may have no real manifestation at all. The function 1/(1+z²) is perfectly well-behaved on the real line everywhere, yet its Taylor series around z = 0 has radius of convergence 1 because its singularities z = ±i lie one unit away in the complex plane. Real-line behavior near the center is irrelevant; it is the global complex geometry (singularity locations) that governs convergence."

- question: "Explain why the Taylor series of 1/(1 + z²) around z = 0 has radius of convergence exactly 1, even though the real function 1/(1+x²) is smooth and bounded for all real x."
  type: short-answer
  answer: "The radius of convergence equals the distance from the expansion center to the nearest singularity in the complex plane. The function 1/(1+z²) has singularities where 1+z² = 0, i.e., at z = i and z = -i. Both are exactly distance 1 from the origin. The series converges on the disk |z| < 1 — the largest disk centered at 0 that contains no singularity. On the real line, z = ±i are invisible, which is why the real function seems to have no obstruction to convergence beyond |x| = 1. Complex analysis reveals that the apparent mystery of real Taylor series is always resolved by the singularity structure in the complex plane."
  explanation: "This is historically one of the great clarifying results of complex analysis. Before the complex plane was understood, mathematicians were puzzled by power series that 'stopped working' at points where the real function was smooth. Cauchy and Riemann's insight was that the complex plane is the natural domain for analytic functions, and convergence is determined by the complex geometry — not the real geometry alone."
```

## Explainer

In real analysis, Taylor series are an approximation tool: a smooth function is approximated by polynomials near a point, with an error that shrinks as you include more terms, but equality holds only in the limit and only under additional conditions. The complex case is different in kind: if f is holomorphic on a disk |z - z₀| < R, then f **equals** its Taylor series everywhere on that disk — not approximately, but exactly, with zero error. This equality is a theorem, not a hope, and it follows directly from Cauchy's Integral Formula for derivatives.

This rigidity has a striking implication. Because the Taylor coefficients aₙ = f^(n)(z₀)/n! are determined entirely by the behavior of f near z₀, two holomorphic functions that agree on any open set — even a tiny disk — must agree on their entire shared domain. You cannot patch together two different holomorphic functions smoothly the way you can with real functions. The function is "frozen" by its local behavior. This property is called the **identity theorem** and it has no real-analysis analogue.

The **radius of convergence** R is the distance from the center z₀ to the nearest **singularity** of f in the complex plane. This is one of the most clarifying results in all of analysis. For f(z) = 1/(1 + z²), the real function 1/(1 + x²) is perfectly smooth for all real x — it has no real singularity. Yet its Taylor series around x = 0 has radius of convergence 1, a fact that puzzled mathematicians before complex analysis was developed. The resolution: in the complex plane, f has singularities at z = ±i, which are distance 1 from the origin. The singularities are invisible on the real line but they govern the radius of convergence.

To find Taylor series in practice, you can either compute derivatives directly or manipulate known series algebraically. The geometric series 1/(1 - z) = Σ zⁿ for |z| < 1 is the most useful starting point. Substituting -z² for z gives 1/(1 + z²) = Σ (-1)ⁿ z²ⁿ for |z| < 1. Substituting z² for z gives 1/(1 - z²) = Σ z²ⁿ for |z| < 1. These substitution tricks are the same algebraic manipulations you know from real Taylor series — the complex setting adds no new algebraic rules, only a geometric interpretation (via singularity locations) of why the radius of convergence is what it is.

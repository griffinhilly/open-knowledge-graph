---
id: complex-trigonometric-functions
title: Complex Trigonometric Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-exponential-function
  type: hard
builds-toward:
- evaluating-integrals-residues
tags:
- trigonometric-functions
- entire-function
- periodicity
stage: advanced
status: draft
---

# Complex Trigonometric Functions

## Core Idea
Complex sine and cosine are defined by sin(z) = (e^(iz) - e^(-iz))/(2i) and cos(z) = (e^(iz) + e^(-iz))/2. They are entire, periodic with period 2π (on the real axis), but unlike their real counterparts, they grow exponentially in the imaginary direction: |sin(iy)| = sinh(y) → ∞ as |y| → ∞.

## Questions

```yaml
- question: "A student argues: 'Since sin(x) is bounded between −1 and 1 for all real x, and complex analysis is just an extension of real analysis, sin(z) must also be bounded for all complex z.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — sin(z) is indeed bounded on the complex plane, and the student is correct"
    - "Sin(z) is bounded, but only on the imaginary axis, not the real axis"
    - "Boundedness on the real axis is not preserved under analytic continuation; sin(z) grows exponentially in the imaginary direction: |sin(iy)| = sinh(y) → ∞"
    - "The student confuses sin(z) with cos(z); only cos(z) is bounded in the complex plane"
  answer: 2
  explanation: "This is the central surprise of complex trigonometric functions. When z = iy (purely imaginary), sin(iy) = i·sinh(y), so |sin(iy)| = sinh(y), which grows without bound as |y| → ∞. The real sine function is bounded because it oscillates around the unit circle as the angle increases. In the complex plane, moving in the imaginary direction instead 'stretches' the exponentials rather than rotating them, producing hyperbolic growth. Analytic continuation preserves algebraic identities and local behavior — but not global properties like boundedness."

- question: "Evaluating sin(z) at z = iy for large real y reveals |sin(iy)| = sinh(y) → ∞. Which of the following conclusions is correct?"
  type: multiple-choice
  options:
    - "This shows sin(z) has essential singularities in the imaginary direction, explaining the unbounded growth"
    - "This is consistent with Liouville's theorem: sin(z) is entire, and the only bounded entire functions are constants — so an entire function that is not constant must be unbounded"
    - "This means sin(z) violates the Cauchy-Riemann equations for purely imaginary inputs"
    - "Sin(z) is not actually entire; the unbounded growth reveals poles on the imaginary axis"
  answer: 1
  explanation: "Liouville's theorem states that a bounded entire function must be constant. Since sin(z) is entire (no singularities anywhere in ℂ) and clearly not constant, it follows that sin(z) must be unbounded. The fact that |sin(iy)| = sinh(y) → ∞ is not a contradiction — it is exactly what Liouville's theorem predicts. Far from being a pathology, the unbounded growth confirms that sin(z) is behaving as an entire non-constant function should. Sin(z) has no singularities at all; the growth is smooth exponential behavior, not a singularity."

- question: "Because sin(z) is an entire function (analytic everywhere in ℂ), Liouville's theorem implies it must be bounded — just as sin(x) is bounded on the real axis."
  type: true-false
  answer: false
  explanation: "This reverses Liouville's theorem. The theorem states: if an entire function IS bounded, then it must be constant. Equivalently: a non-constant entire function CANNOT be bounded. Since sin(z) is entire and non-constant, Liouville's theorem guarantees it is unbounded — consistent with |sin(iy)| = sinh(y) → ∞. The real-axis boundedness of sin(x) is a special property of the real line, not a consequence of analyticity that extends to all of ℂ."

- question: "The definition sin(z) = (e^(iz) − e^(−iz))/(2i) is not an arbitrary choice — it is the unique extension of real sine to the complex plane that is consistent with both the complex exponential and Euler's formula."
  type: true-false
  answer: true
  explanation: "Euler's formula gives e^(iθ) = cos(θ) + i·sin(θ) for real θ. From this: e^(iθ) + e^(−iθ) = 2cos(θ) and e^(iθ) − e^(−iθ) = 2i·sin(θ). The complex definitions of cos(z) and sin(z) simply promote these identities to hold for all complex z. There is no choice involved once you require (a) the functions agree with real sin and cos on the real axis and (b) they are analytic. Analytic continuation is unique, so this is the only definition that works."

- question: "Explain why |sin(z)| can become arbitrarily large for complex z, even though |sin(x)| ≤ 1 for all real x. What does this reveal about extending real functions to the complex plane?"
  type: short-answer
  answer: "For real x, sin(x) oscillates because e^(ix) and e^(−ix) both have modulus 1 — they rotate around the unit circle. When z = iy is purely imaginary, e^(i·iy) = e^(−y) and e^(−i·iy) = e^(y), so sin(iy) = i·sinh(y). As y grows, e^y dominates, and |sin(iy)| = sinh(y) grows exponentially without bound. The key insight is that real-axis properties — like boundedness — are properties of the real line specifically, not properties of the function's analytic structure. Analytic continuation extends the local structure (derivatives, algebraic identities) but cannot preserve global properties that were artifacts of restricting to the real axis."
  explanation: "This reveals a general principle: when extending real functions to ℂ, expect global behavior to change dramatically. Real exponential growth, real oscillation, and real boundedness are all special cases of complex behavior constrained to a line. Off that line, the complex function follows its own logic — and for trigonometric functions, the imaginary direction produces hyperbolic rather than oscillatory behavior, with unbounded exponential growth."
```

## Explainer

From your study of the complex exponential, you know Euler's formula: e^(iθ) = cos(θ) + i·sin(θ) for real θ. This gives a beautiful pair of identities: adding e^(iθ) and e^(−iθ) gives 2cos(θ), and subtracting gives 2i·sin(θ). The **complex trigonometric functions** simply promote these identities to a definition: for any complex number z, declare cos(z) = (e^(iz) + e^(−iz))/2 and sin(z) = (e^(iz) − e^(−iz))/(2i). This is not an extension by guesswork — it is the only definition consistent with the complex exponential and the familiar real values.

Because e^z is entire (analytic everywhere in ℂ), and the definitions are just linear combinations of entire functions, sin(z) and cos(z) are **entire functions** — no singularities anywhere in the complex plane. All the algebraic identities from real trigonometry carry over: sin²(z) + cos²(z) = 1, the addition formulas, the derivative formulas (d/dz sin(z) = cos(z)), and periodicity with period 2π. So far, complex trig feels like a smooth generalization.

The surprise comes when you plug in purely imaginary values. Set z = iy for real y. Then sin(iy) = (e^(i·iy) − e^(−i·iy))/(2i) = (e^(−y) − e^(y))/(2i) = i·(e^y − e^(−y))/2 = i·sinh(y). So |sin(iy)| = sinh(y), which grows exponentially as |y| increases. This is completely unlike real sine, which is forever bounded between −1 and 1. The complex sine function is **unbounded** — you can make |sin(z)| as large as you like by moving z far enough into the imaginary direction. This exposes a fundamental difference: boundedness is not preserved when you extend real functions to the complex plane.

This unboundedness is not a pathology; it is a consequence of how exponentials behave in the complex plane, and it has real consequences. In complex analysis, Liouville's theorem states that the only bounded entire functions are constants — so the fact that sin(z) is entire and unbounded is perfectly consistent. When you later evaluate integrals using residues, the behavior of trig functions along contours in the complex plane (where z has large imaginary part) determines whether certain integrals converge or diverge. Understanding that complex trig functions grow exponentially off the real axis is essential for choosing the right contour in those calculations.

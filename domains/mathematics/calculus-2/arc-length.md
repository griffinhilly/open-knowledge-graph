---
id: arc-length
title: Arc Length
domain: mathematics
course: calculus-2
prerequisites:
- id: fundamental-theorem-of-calculus-part-2
  type: hard
- id: u-substitution
  type: hard
- id: trigonometric-substitution
  type: soft
- id: central-angles-and-arcs
  type: soft
- id: circumference
  type: soft
builds-toward:
- arc-length-parametric
- surface-area-of-revolution
tags:
- integration
- applications
- arc-length
stage: formal-systems
status: validated
---
# Arc Length

## Core Idea
The length of a curve y = f(x) from x = a to x = b is L = integral from a to b of sqrt(1 + (f'(x))^2) dx. This formula comes from summing infinitesimal hypotenuses (sqrt(dx^2 + dy^2)) along the curve. Arc length integrals are often difficult or impossible to evaluate in closed form, making them good candidates for numerical methods.

## How It's Best Learned
Derive the formula from the Pythagorean theorem applied to infinitesimal segments. Compute arc length for functions where the integral simplifies nicely (e.g., y = x^(3/2), y = (x^2)/2 - ln(x)/4). Emphasize that most arc length integrals do not have neat answers.

## Common Misconceptions
- Forgetting the square root or the 1 inside it.
- Confusing arc length with the integral of |f(x)| (which gives area, not length).
- Expecting all arc length integrals to have closed-form solutions.

## Questions

```yaml
- question: "A student wants to find the length of the curve y = x² from x = 0 to x = 1. She sets up the integral ∫₀¹ x² dx and gets 1/3. What error has she made?"
  type: multiple-choice
  options:
    - "She computed the area under the curve rather than arc length; the correct setup is ∫₀¹ √(1 + (2x)²) dx"
    - "She used the wrong limits of integration; she should integrate from 0 to f(1) = 1"
    - "She forgot to multiply by 2π, which converts area integrals to length"
    - "She should integrate |f(x)| rather than f(x) to get path length"
  answer: 0
  explanation: "Integrating f(x) directly gives the signed area between the curve and the x-axis — not the curve's length. Arc length requires summing the lengths of infinitesimal hypotenuses √(dx² + dy²), which simplifies to ∫√(1 + [f′(x)]²) dx. For y = x², f′(x) = 2x, so the arc length integral is ∫₀¹ √(1 + 4x²) dx — quite different from ∫₀¹ x² dx."

- question: "In the arc length formula L = ∫ₐᵇ √(1 + [f′(x)]²) dx, where does the '1 +' inside the square root come from?"
  type: multiple-choice
  options:
    - "It represents the horizontal component dx of each infinitesimal segment, via the Pythagorean theorem applied to the tiny right triangle with legs dx and dy"
    - "It is a normalizing constant that ensures the integral converges for all continuous functions"
    - "It shifts the integrand upward to prevent the square root from taking a negative value"
    - "It represents the constant of integration absorbed into the formula during derivation"
  answer: 0
  explanation: "Each infinitesimal segment of the curve has horizontal run dx and vertical rise dy = f′(x)dx. By the Pythagorean theorem, the segment length is √(dx² + dy²) = √(dx² + [f′(x)]² dx²) = √(1 + [f′(x)]²) dx. The '1' comes from dx² / dx² = 1 after factoring out dx. It is always present because even a nearly horizontal curve still has a horizontal component."

- question: "Most arc length integrals that arise from natural functions cannot be evaluated in elementary closed form."
  type: true-false
  answer: true
  explanation: "True. For most functions — y = sin(x), y = x³, y = eˣ — the expression √(1 + [f′(x)]²) does not have an elementary antiderivative. The 'nice' examples in calculus textbooks (like y = x^(3/2)) are specially engineered so the algebra simplifies. Arc length is a natural context where numerical integration is often the only practical option."

- question: "The arc length formula is derived by summing the vertical changes dy along the curve from x = a to x = b."
  type: true-false
  answer: false
  explanation: "False. Arc length sums the lengths of infinitesimal hypotenuses — √(dx² + dy²) — not just the vertical changes. Summing only dy would give the total net vertical displacement (f(b) − f(a)), not the path length. The Pythagorean theorem is essential: both horizontal and vertical components must be included."

- question: "Explain in your own words why the arc length formula involves a square root, and what geometric idea that square root represents."
  type: short-answer
  answer: "The curve is cut into infinitely many tiny segments. Each segment is approximately a straight line with a horizontal component dx and a vertical component dy = f′(x) dx — a tiny right triangle. By the Pythagorean theorem, the length of that segment (the hypotenuse) is √(dx² + dy²). Factoring out dx gives √(1 + [f′(x)]²) dx. The square root is the hypotenuse of an infinitesimal right triangle; arc length is the integral (sum) of infinitely many such hypotenuses."
  explanation: "Recognizing the Pythagorean theorem as the source of the square root is what lets you adapt the formula to parametric curves and surfaces of revolution — the derivation is always the same geometric idea in a slightly different setting."
```

## Explainer

You already know how to use the Fundamental Theorem of Calculus to compute accumulations, and you know u-substitution for handling composite integrands. **Arc length** applies integration to a new question: instead of asking "how much area is under this curve?" you ask "how long is this curve?" The setup uses a trick from a prerequisite you may not expect — the Pythagorean theorem.

Picture the curve y = f(x) from x = a to x = b cut into thousands of tiny segments. Each segment has a horizontal run of dx and a vertical rise of dy = f′(x) dx. The straight-line length of that tiny segment, by the Pythagorean theorem, is √(dx² + dy²). Factor out dx: √(dx² + [f′(x) dx]²) = √(1 + [f′(x)]²) dx. Now integrate — sum these infinitesimal hypotenuses — to get the total arc length: L = ∫ₐᵇ √(1 + [f′(x)]²) dx. The "1 +" inside the square root accounts for the horizontal component that is always present, even along a nearly flat curve.

The formula has a clean three-step setup: differentiate f(x) to get f′(x), square it, add 1, take the square root, and integrate. The challenge is in that last step. Most of the time, √(1 + [f′(x)]²) does not have a nice antiderivative. For polynomials like y = x^(3/2), the derivative f′(x) = (3/2)x^(1/2), so [f′(x)]² = (9/4)x, and 1 + (9/4)x has an elementary antiderivative. These "nice" examples are engineered specifically to work out. For a curve like y = sin(x) or y = x³, the arc length integral has no elementary closed form.

This is an important conceptual checkpoint: arc length teaches you that not every naturally-arising integral can be computed symbolically. The setup and formula are always the same; the evaluation may require numerical integration. When you move to parametric curves (arc length parametric) and surfaces of revolution, the same Pythagorean-theorem derivation extends in a natural way. Understanding the derivation — not just memorizing the formula — is what lets you adapt it to those new settings.

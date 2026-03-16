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

## Explainer

You already know how to use the Fundamental Theorem of Calculus to compute accumulations, and you know u-substitution for handling composite integrands. **Arc length** applies integration to a new question: instead of asking "how much area is under this curve?" you ask "how long is this curve?" The setup uses a trick from a prerequisite you may not expect — the Pythagorean theorem.

Picture the curve y = f(x) from x = a to x = b cut into thousands of tiny segments. Each segment has a horizontal run of dx and a vertical rise of dy = f′(x) dx. The straight-line length of that tiny segment, by the Pythagorean theorem, is √(dx² + dy²). Factor out dx: √(dx² + [f′(x) dx]²) = √(1 + [f′(x)]²) dx. Now integrate — sum these infinitesimal hypotenuses — to get the total arc length: L = ∫ₐᵇ √(1 + [f′(x)]²) dx. The "1 +" inside the square root accounts for the horizontal component that is always present, even along a nearly flat curve.

The formula has a clean three-step setup: differentiate f(x) to get f′(x), square it, add 1, take the square root, and integrate. The challenge is in that last step. Most of the time, √(1 + [f′(x)]²) does not have a nice antiderivative. For polynomials like y = x^(3/2), the derivative f′(x) = (3/2)x^(1/2), so [f′(x)]² = (9/4)x, and 1 + (9/4)x has an elementary antiderivative. These "nice" examples are engineered specifically to work out. For a curve like y = sin(x) or y = x³, the arc length integral has no elementary closed form.

This is an important conceptual checkpoint: arc length teaches you that not every naturally-arising integral can be computed symbolically. The setup and formula are always the same; the evaluation may require numerical integration. When you move to parametric curves (arc length parametric) and surfaces of revolution, the same Pythagorean-theorem derivation extends in a natural way. Understanding the derivation — not just memorizing the formula — is what lets you adapt it to those new settings.

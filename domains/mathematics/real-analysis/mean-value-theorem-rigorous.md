---
id: mean-value-theorem-rigorous
title: Mean Value Theorem (Rigorous)
domain: mathematics
course: real-analysis
prerequisites:
- id: rigorous-derivative-definition
  type: hard
- id: extreme-value-theorem-rigorous
  type: soft
builds-toward:
- lhopitals-rule-rigorous
- taylors-theorem-remainder
tags:
- mean-value
- derivative
- intermediate-point
stage: advanced
status: draft
---

# Mean Value Theorem (Rigorous)

## Core Idea
If f is continuous on [a,b] and differentiable on (a,b), then there exists c ∈ (a,b) such that f'(c) = [f(b) - f(a)]/(b - a). This theorem links the derivative at a point to the average rate of change and is fundamental to bounding derivatives, proving monotonicity, and analyzing function behavior. Rolle's Theorem (f(a) = f(b) ⟹ f'(c) = 0) is a special case.

## Explainer

The Mean Value Theorem (MVT) captures a geometrically obvious fact in analytically usable form. Draw any smooth curve from (a, f(a)) to (b, f(b)) — the secant line connecting the endpoints has a definite slope [f(b) − f(a)]/(b − a). The MVT says there must be at least one interior point c where the tangent to the curve is exactly parallel to that secant line. In kinematic terms: if you drive 120 miles in 2 hours, your average speed is 60 mph — and the MVT guarantees you were traveling at *exactly* 60 mph at some instant, even if you sped and slowed throughout the trip.

The rigorous proof builds from your prerequisite — the **rigorous derivative definition** — and proceeds through **Rolle's Theorem**. Rolle's handles the special case f(a) = f(b): if a function starts and ends at the same height and is continuous on [a,b] and differentiable on (a,b), then f'(c) = 0 somewhere inside. This follows from the Extreme Value Theorem: f attains a maximum and minimum on [a,b]; if both occur at the endpoints, f is constant and f' ≡ 0 everywhere; otherwise an interior extremum exists, and at an interior extremum the derivative must be zero (by the first-derivative test from your derivative definition). To derive MVT from Rolle's, define g(x) = f(x) − [f(a) + ((f(b)−f(a))/(b−a))(x−a)], which subtracts the secant line, making g(a) = g(b) = 0. Rolle's applies to g, yielding g'(c) = 0, which translates directly to f'(c) = [f(b)−f(a)]/(b−a).

The MVT's primary analytical power is **bounding functions via their derivatives**. If |f'(x)| ≤ M on (a,b), then applying MVT gives |f(b) − f(a)| ≤ M|b − a|. This estimate — the function can change no faster than its maximum derivative rate — appears constantly: in error analysis for numerical integration, in proving continuity from differentiability, and in establishing that algorithms converge. The MVT also proves the fundamental uniqueness principle: if f'(x) = 0 everywhere on (a,b), then f is constant. This is the rigorous justification for the calculus claim that "antiderivatives of the same function differ only by a constant," which undergirds the whole theory of definite integration.

Monotonicity is another direct consequence: if f'(x) > 0 on (a,b), then for any x₁ < x₂ in (a,b), MVT gives f(x₂) − f(x₁) = f'(c)(x₂ − x₁) > 0, so f is strictly increasing. The MVT thus transforms the local information encoded in the derivative into global statements about the function's behavior. From this point, Taylor's Theorem and L'Hôpital's Rule both use MVT-style arguments to control remainder terms and indeterminate forms — so the proof technique you learn here recurs throughout the rest of real analysis.

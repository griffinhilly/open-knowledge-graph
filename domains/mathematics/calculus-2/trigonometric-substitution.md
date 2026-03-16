---
id: trigonometric-substitution
title: Trigonometric Substitution
domain: mathematics
course: calculus-2
prerequisites:
- id: trigonometric-integrals
  type: hard
- id: inverse-trigonometric-functions
  type: hard
- id: derivatives-of-inverse-trig-functions
  type: soft
- id: graphing-tangent-and-reciprocal-trig
  type: soft
builds-toward:
- arc-length
tags:
- integration
- techniques
- trig-substitution
stage: formal-systems
status: validated
---
# Trigonometric Substitution

## Core Idea
Trigonometric substitution handles integrands containing sqrt(a^2 - x^2), sqrt(a^2 + x^2), or sqrt(x^2 - a^2) by substituting x = a*sin(theta), x = a*tan(theta), or x = a*sec(theta) respectively. The substitution eliminates the square root using a Pythagorean identity. After integrating in theta, you convert back to x using a reference triangle.

## How It's Best Learned
Memorize the three cases and which substitution matches each radical form. Practice drawing the reference triangle to convert back. Work through complete examples for each case. Connect to completing the square when the expression under the radical is not in standard form.

## Common Misconceptions
- Using the wrong substitution for the given radical form.
- Forgetting to convert back from theta to x at the end.
- Not completing the square first when the quadratic under the radical is not in standard form (e.g., sqrt(2x - x^2)).

## Explainer

Ordinary u-substitution works when the integrand contains a function and its derivative together. But integrands containing expressions like √(1 − x²) or √(x² + 9) don't fit that pattern — the square roots of quadratics resist all algebraic simplification. Trigonometric substitution works by exploiting the Pythagorean identities you already know from trigonometric integrals to collapse those square roots into trig functions that can be integrated directly. The square root disappears; an integral in θ takes its place.

The three cases correspond one-to-one with the three Pythagorean identities. If the integrand contains **√(a² − x²)**, substitute x = a sin(θ): then a² − x² = a²(1 − sin²θ) = a²cos²θ, so the square root becomes a|cos θ|. If it contains **√(a² + x²)**, substitute x = a tan(θ): a² + x² = a²(1 + tan²θ) = a²sec²θ. If it contains **√(x² − a²)**, substitute x = a sec(θ): x² − a² = a²(sec²θ − 1) = a²tan²θ. Memorizing which substitution matches which radical form is the entire "table" for this technique — everything else follows mechanically.

The full procedure has three phases. First, apply the substitution: replace x by its trig expression and replace dx by differentiating (e.g., if x = a tan θ, then dx = a sec²θ dθ). Simplify the integrand completely into trig functions of θ, using the Pythagorean identity to eliminate the square root. Second, integrate in θ — this step often requires the techniques from trigonometric integrals (powers of sin and cos, products of sec and tan). Third, **convert back to x** using a reference triangle: draw a right triangle that encodes your substitution. For x = a tan θ, the opposite side is x, the adjacent side is a, and the hypotenuse is √(x² + a²). Any trig function of θ can then be read off the triangle as an algebraic expression in x.

A common variant requires one extra preparatory step: if the expression under the radical is not already in the form a² ± x² or x² − a², **complete the square** first. For example, √(2x − x²) = √(1 − (x−1)²) after completing the square, which now fits the first case with a = 1 and the substitution (x−1) = sin θ. The technique then proceeds as usual. Trigonometric substitution is a unification of several prerequisite skills — inverse trig functions, Pythagorean identities, trig integrals, and the reference triangle — all coordinated to handle one family of integrands that resist every simpler approach.

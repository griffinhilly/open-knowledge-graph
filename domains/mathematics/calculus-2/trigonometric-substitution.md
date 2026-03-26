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

## Questions

```yaml
- question: "To evaluate ∫ dx / √(x² + 16), which substitution should you use, and why?"
  type: multiple-choice
  options:
    - "x = 4 sin(θ), because the expression under the radical has the form a² − x²"
    - "x = 4 tan(θ), because the expression under the radical has the form a² + x²"
    - "x = 4 sec(θ), because the expression under the radical has the form x² − a²"
    - "x = 4 cos(θ), because cosine simplifies square roots of sums"
  answer: 1
  explanation: "The radical √(x² + 16) has the form √(x² + a²) with a = 4. This matches the second case: substitute x = a tan(θ), so that x² + a² = a²(1 + tan²θ) = a²sec²θ, and the square root becomes a|sec θ|. Using sin(θ) is the most common error — that substitution is for √(a² − x²), where the x² is subtracted. Each radical form maps to exactly one Pythagorean identity."

- question: "After completing a trigonometric substitution and integrating in θ, a student leaves the answer in terms of θ. What error has the student made?"
  type: multiple-choice
  options:
    - "No error — θ is a valid variable since the substitution replaced x with a trig function of θ"
    - "The student should have differentiated, not integrated, after substituting"
    - "The student forgot to convert the answer back to x using a reference triangle"
    - "The student should have used u-substitution instead, which doesn't require back-conversion"
  answer: 2
  explanation: "The original integral is a function of x, so the final answer must also be expressed in x. After integrating in θ, you must use a reference triangle to convert every trig function of θ back to an algebraic expression in x. For example, if x = a tan θ, then the reference triangle has opposite side x, adjacent side a, and hypotenuse √(x² + a²) — from which sin θ = x/√(x² + a²), cos θ = a/√(x² + a²), etc. Forgetting this step is one of the most common errors in applying trig substitution."

- question: "The substitution x = a sin(θ) works on the radical √(a² − x²) because it converts the expression under the radical into a²cos²θ via the Pythagorean identity sin²θ + cos²θ = 1."
  type: true-false
  answer: true
  explanation: "Substituting x = a sin θ gives a² − x² = a² − a²sin²θ = a²(1 − sin²θ) = a²cos²θ. So √(a² − x²) = a|cos θ|, eliminating the square root entirely. This is exactly why trigonometric substitution works: each radical form corresponds to one Pythagorean identity that collapses the square root into a trig function. The entire technique is built on this identity-matching."

- question: "If the expression under the radical is not already in the form a² ± x² or x² − a², trigonometric substitution can rarely be applied."
  type: true-false
  answer: false
  explanation: "When the quadratic under the radical is not in standard form, you complete the square first to put it into one of the three standard forms. For example, √(2x − x²) = √(1 − (x−1)²) after completing the square — now it fits the form √(a² − u²) with a = 1 and u = x − 1, and you substitute u = sin θ. Completing the square is a preparatory step, not a separate technique; trig substitution then proceeds normally."

- question: "Why does trigonometric substitution succeed at eliminating square roots of quadratic expressions, when ordinary algebraic methods and u-substitution fail?"
  type: short-answer
  answer: "Trigonometric substitution works by exploiting the Pythagorean identities (sin²θ + cos²θ = 1, 1 + tan²θ = sec²θ, sec²θ − 1 = tan²θ) to collapse the square root. By substituting x = a·trig(θ), the expression under the radical becomes a perfect square of a trig function, so the square root disappears. U-substitution requires the integrand to contain a function and its derivative simultaneously — a condition that square roots of quadratics don't satisfy. Only the Pythagorean identities provide the algebraic relationship needed to eliminate these radicals."
  explanation: "The key insight is that trig substitution is not guesswork — it is a deliberate exploitation of known identities. The three cases (sin, tan, sec) correspond exactly to the three Pythagorean identities, each designed to eliminate one of the three radical forms. No other substitution has this property. Once the radical is eliminated, the resulting trig integral — which may still require techniques from trig integrals — can be computed. The back-conversion via reference triangle then restores the answer to the original variable x."
```

## Explainer

Ordinary u-substitution works when the integrand contains a function and its derivative together. But integrands containing expressions like √(1 − x²) or √(x² + 9) don't fit that pattern — the square roots of quadratics resist all algebraic simplification. Trigonometric substitution works by exploiting the Pythagorean identities you already know from trigonometric integrals to collapse those square roots into trig functions that can be integrated directly. The square root disappears; an integral in θ takes its place.

The three cases correspond one-to-one with the three Pythagorean identities. If the integrand contains **√(a² − x²)**, substitute x = a sin(θ): then a² − x² = a²(1 − sin²θ) = a²cos²θ, so the square root becomes a|cos θ|. If it contains **√(a² + x²)**, substitute x = a tan(θ): a² + x² = a²(1 + tan²θ) = a²sec²θ. If it contains **√(x² − a²)**, substitute x = a sec(θ): x² − a² = a²(sec²θ − 1) = a²tan²θ. Memorizing which substitution matches which radical form is the entire "table" for this technique — everything else follows mechanically.

The full procedure has three phases. First, apply the substitution: replace x by its trig expression and replace dx by differentiating (e.g., if x = a tan θ, then dx = a sec²θ dθ). Simplify the integrand completely into trig functions of θ, using the Pythagorean identity to eliminate the square root. Second, integrate in θ — this step often requires the techniques from trigonometric integrals (powers of sin and cos, products of sec and tan). Third, **convert back to x** using a reference triangle: draw a right triangle that encodes your substitution. For x = a tan θ, the opposite side is x, the adjacent side is a, and the hypotenuse is √(x² + a²). Any trig function of θ can then be read off the triangle as an algebraic expression in x.

A common variant requires one extra preparatory step: if the expression under the radical is not already in the form a² ± x² or x² − a², **complete the square** first. For example, √(2x − x²) = √(1 − (x−1)²) after completing the square, which now fits the first case with a = 1 and the substitution (x−1) = sin θ. The technique then proceeds as usual. Trigonometric substitution is a unification of several prerequisite skills — inverse trig functions, Pythagorean identities, trig integrals, and the reference triangle — all coordinated to handle one family of integrands that resist every simpler approach.

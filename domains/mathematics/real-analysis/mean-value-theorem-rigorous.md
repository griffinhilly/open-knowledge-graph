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

## Questions

```yaml
- question: "You know that |f'(x)| ≤ 3 for all x in (2, 5). What can you conclude about |f(5) − f(2)|?"
  type: multiple-choice
  options:
    - "f(5) − f(2) = 9, since f' averages 3 over an interval of length 3"
    - "|f(5) − f(2)| ≤ 9, because MVT gives |f(b) − f(a)| ≤ M|b − a|"
    - "Nothing can be concluded without knowing f explicitly"
    - "|f(5) − f(2)| = 3, because f' must equal 3 at some interior point"
  answer: 1
  explanation: "By MVT, f(5) − f(2) = f'(c)(5 − 2) for some c ∈ (2, 5). Taking absolute values: |f(5) − f(2)| = |f'(c)| · 3 ≤ 3 · 3 = 9. The bound is an inequality, not an equality (option A), because f' need not be constantly 3. Option D confuses the existence of a point where f' equals the average rate of change with the value of the change itself. This derivative-bounding application is MVT's primary analytical power."

- question: "To derive the MVT from Rolle's Theorem, an auxiliary function g(x) is defined by subtracting the secant line from f. What property of g makes Rolle's Theorem applicable?"
  type: multiple-choice
  options:
    - "g is continuous and differentiable, satisfying Rolle's regularity conditions"
    - "g(a) = g(b) = 0, satisfying Rolle's requirement that the function starts and ends at the same height"
    - "g is strictly increasing on (a, b), guaranteeing an interior zero of g'"
    - "g'(x) = f'(x) for all x, so the derivative information is preserved"
  answer: 1
  explanation: "Rolle's Theorem requires f(a) = f(b). By subtracting the secant line — setting g(x) = f(x) − [f(a) + ((f(b)−f(a))/(b−a))(x−a)] — both g(a) and g(b) equal zero, satisfying this requirement. Option A is true but not novel (differentiability is inherited from f). Option D is wrong: g'(x) = f'(x) minus the secant slope, not equal to f'(x). Rolle's then guarantees g'(c) = 0, which translates back to f'(c) = [f(b)−f(a)]/(b−a)."

- question: "If f'(x) = 0 for all x in an open interval (a, b), then f is constant on (a, b)."
  type: true-false
  answer: true
  explanation: "This follows directly from MVT. For any two points x₁ < x₂ in (a, b), MVT gives f(x₂) − f(x₁) = f'(c)(x₂ − x₁) = 0. So f(x₂) = f(x₁) for any pair of points, meaning f is constant. This is the rigorous justification for the calculus claim that antiderivatives of the same function differ only by a constant — a fact that undergirds the entire theory of definite integration."

- question: "The Mean Value Theorem guarantees that the derivative equals the average rate of change at exactly one interior point."
  type: true-false
  answer: false
  explanation: "MVT guarantees existence of *at least one* such point c, not exactly one. A function could satisfy f'(c) = [f(b)−f(a)]/(b−a) at multiple interior points — for example, a horizontal line (f constant) satisfies f' = 0 = average rate of change everywhere on the interval. The theorem is an existence result, not a uniqueness result. Mistaking 'at least one' for 'exactly one' is a common misreading."

- question: "Explain why the Mean Value Theorem is more than a geometric observation and what analytical work it actually does."
  type: short-answer
  answer: "MVT converts local information (derivative values at individual points) into global information about the function's behavior over an interval. The geometric picture shows the result is plausible, but the analytical power is the inequality |f(b)−f(a)| ≤ M|b−a|: a function cannot change faster than its maximum derivative rate. This enables bounding functions in error analysis, proving monotonicity, and establishing uniqueness of antiderivatives."
  explanation: "The kinematic analogy (you were exactly at the average speed at some instant) makes MVT vivid but doesn't convey its usefulness. The analytical leverage comes from being able to *bound* how much a function changes given a bound on its derivative. This appears throughout analysis: proving convergence, bounding approximation errors, and establishing monotonicity all reduce to MVT-style arguments where derivative bounds translate into function-value bounds."
```

## Explainer

The Mean Value Theorem (MVT) captures a geometrically obvious fact in analytically usable form. Draw any smooth curve from (a, f(a)) to (b, f(b)) — the secant line connecting the endpoints has a definite slope [f(b) − f(a)]/(b − a). The MVT says there must be at least one interior point c where the tangent to the curve is exactly parallel to that secant line. In kinematic terms: if you drive 120 miles in 2 hours, your average speed is 60 mph — and the MVT guarantees you were traveling at *exactly* 60 mph at some instant, even if you sped and slowed throughout the trip.

The rigorous proof builds from your prerequisite — the **rigorous derivative definition** — and proceeds through **Rolle's Theorem**. Rolle's handles the special case f(a) = f(b): if a function starts and ends at the same height and is continuous on [a,b] and differentiable on (a,b), then f'(c) = 0 somewhere inside. This follows from the Extreme Value Theorem: f attains a maximum and minimum on [a,b]; if both occur at the endpoints, f is constant and f' ≡ 0 everywhere; otherwise an interior extremum exists, and at an interior extremum the derivative must be zero (by the first-derivative test from your derivative definition). To derive MVT from Rolle's, define g(x) = f(x) − [f(a) + ((f(b)−f(a))/(b−a))(x−a)], which subtracts the secant line, making g(a) = g(b) = 0. Rolle's applies to g, yielding g'(c) = 0, which translates directly to f'(c) = [f(b)−f(a)]/(b−a).

The MVT's primary analytical power is **bounding functions via their derivatives**. If |f'(x)| ≤ M on (a,b), then applying MVT gives |f(b) − f(a)| ≤ M|b − a|. This estimate — the function can change no faster than its maximum derivative rate — appears constantly: in error analysis for numerical integration, in proving continuity from differentiability, and in establishing that algorithms converge. The MVT also proves the fundamental uniqueness principle: if f'(x) = 0 everywhere on (a,b), then f is constant. This is the rigorous justification for the calculus claim that "antiderivatives of the same function differ only by a constant," which undergirds the whole theory of definite integration.

Monotonicity is another direct consequence: if f'(x) > 0 on (a,b), then for any x₁ < x₂ in (a,b), MVT gives f(x₂) − f(x₁) = f'(c)(x₂ − x₁) > 0, so f is strictly increasing. The MVT thus transforms the local information encoded in the derivative into global statements about the function's behavior. From this point, Taylor's Theorem and L'Hôpital's Rule both use MVT-style arguments to control remainder terms and indeterminate forms — so the proof technique you learn here recurs throughout the rest of real analysis.

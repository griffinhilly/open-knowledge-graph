---
id: differentials
title: Differentials
domain: mathematics
course: calculus-1
prerequisites:
  - id: linear-approximation
    type: hard
  - id: derivative-notation
    type: hard
builds-toward:
  - u-substitution
tags: [derivatives, differentials, approximation]
stage: formal-systems
status: validated
---

# Differentials

## Core Idea
If y = f(x), the differential dy = f'(x) dx represents the change in y along the tangent line for a small change dx in x. While the actual change in y is Delta_y = f(x + dx) - f(x), the differential dy approximates it: dy is approximately equal to Delta_y when dx is small. Differentials formalize the Leibniz notation and are used in error estimation, integration by substitution, and differential equations.

## How It's Best Learned
Compare Delta_y (actual change along the curve) with dy (change along the tangent line) graphically and numerically. Practice computing differentials: if y = x^3, then dy = 3x^2 dx. Apply to error propagation: if a measurement has error dx, estimate the error in a computed quantity.

## Common Misconceptions
- Confusing dy with Delta_y (dy is the linear approximation to the actual change).
- Treating dx as zero (it is small but nonzero).
- Not understanding the relationship between differentials and the chain rule / u-substitution.

## Questions

```yaml
- question: "A sphere's radius is measured as r = 10 cm with a measurement error of dr = 0.2 cm. Using differentials, what is the approximate error in the computed volume V = (4/3)πr³?"
  type: multiple-choice
  options:
    - "dV = (4/3)π(0.2)³ ≈ 0.034 cm³"
    - "dV = 4πr² dr = 4π(100)(0.2) ≈ 251.3 cm³"
    - "dV = (4/3)π(10.2)³ − (4/3)π(10)³ ≈ 257 cm³"
    - "dV = 4πr³ dr = 4π(1000)(0.2) ≈ 2513 cm³"
  answer: 1
  explanation: "The differential of V = (4/3)πr³ is dV = 4πr² dr. Substituting r = 10 and dr = 0.2 gives dV = 4π(100)(0.2) ≈ 251.3 cm³. This is the change along the tangent (the differential), which approximates the true change ΔV. Option C computes ΔV exactly — notice dV and ΔV are close but not identical; the differential is the approximation."

- question: "Which statement best describes the relationship between dy and Δy as dx approaches zero?"
  type: multiple-choice
  options:
    - "dy and Δy both approach zero, and their ratio dy/Δy approaches 1"
    - "dy approaches Δy exactly for sufficiently small dx, so they become equal"
    - "dy and Δy both approach zero, but they remain different quantities representing different geometric objects"
    - "dy approaches zero while Δy remains constant"
  answer: 0
  explanation: "As dx → 0, both dy and Δy → 0. The key fact is that their ratio dy/Δy → 1, meaning the differential is an ever-better proportional approximation to the actual change. But dy and Δy never become equal for any nonzero dx (unless the function is linear) — dy always follows the tangent line while Δy follows the curve. Option B is the classic confusion: 'sufficiently small' doesn't make them equal, only close in proportion."

- question: "In Leibniz notation, dy/dx should be understood as a limit of a ratio, not as an actual ratio of two quantities."
  type: true-false
  answer: false
  explanation: "Once differentials are properly defined, dy/dx IS a literal ratio of two differentials: dy = f′(x) dx, and dividing both sides by dx gives dy/dx = f′(x). This is precisely why Leibniz notation is so powerful — it lets the chain rule look like fraction cancellation (dy/du · du/dx = dy/dx) and makes substitution in integrals meaningful. The differential formalism vindicates the literal ratio interpretation that the limit definition initially discouraged."

- question: "If y = x³, then dy = 3x² dx gives the exact change in y for any nonzero value of dx."
  type: true-false
  answer: false
  explanation: "dy = 3x² dx is an approximation — it gives the change along the tangent line, not the actual change along the curve. The true change is Δy = (x + dx)³ − x³ = 3x² dx + 3x(dx)² + (dx)³. The terms 3x(dx)² + (dx)³ are the error: for small dx they are negligible, but for large dx they matter significantly. The differential approximation is exact only when f is linear."

- question: "Explain why the substitution step in u-substitution (writing du = f'(x) dx) is mathematically legitimate, not just a notational trick."
  type: short-answer
  answer: "When you write u = g(x) and compute du = g′(x) dx, you are computing a differential — a precise object defined as the rate of change of u times a change in x. This means du and dx are related as actual quantities, not just notation. When you substitute into an integral, replacing the integrand's x-expression with u and the 'dx' with 'du/g′(x)', you are performing a genuine change of variable using the differential relationship. The integral's value is preserved because the differential correctly captures how the infinitesimal element transforms under the substitution."
  explanation: "The legitimacy of u-substitution rests on the differential formalism: differentials obey the chain rule algebraically, so du = g′(x) dx can be rearranged and substituted. This is not a symbol-shuffling trick — it is a coherent change of variables where the differential of the new variable correctly accounts for the stretching or compressing of the integration variable. This is why the topic builds toward u-substitution: differentials are the conceptual foundation that makes the technique rigorous."
```

## Explainer

You already know how to use the tangent line to approximate a function near a point — that's linear approximation. Differentials give that idea a precise algebraic form. If y = f(x), then **dx** is any small (but nonzero) change in x, and **dy** is defined as f′(x) dx: the corresponding change along the tangent line. The actual change in the function value is Δy = f(x + dx) − f(x), which follows the curve. The differential dy follows the tangent line instead, and when dx is small, dy ≈ Δy.

To compute a differential in practice, differentiate as normal and then attach dx. If y = x³, then dy = 3x² dx. If y = sin(x), then dy = cos(x) dx. The dx is not decorative — it is a variable in its own right, representing an increment in x. You can think of the familiar derivative notation dy/dx as a literal ratio of two differentials: the ratio of how much y changes (along the tangent) to how much x changes.

This reframing makes **u-substitution** in integration make sense. When you write u = x² and then compute du = 2x dx, you are computing a differential. The substitution replaces not just u but the entire dx-expression, capturing how the substitution changes the variable of integration. Without differentials, this step would seem like a notational trick; with them, it is a coherent change of variables.

Differentials also formalize **error propagation**. If you measure x with a small error dx, then the induced error in y = f(x) is approximately dy = f′(x) dx. For example, if you measure the radius of a sphere as r = 5 cm with an error of ±0.1 cm, the error in the volume V = (4/3)πr³ is approximately dV = 4πr² dr = 4π(25)(0.1) ≈ 31.4 cm³. This is linear approximation in applied form, and it is why scientists routinely use differentials to estimate measurement uncertainty.

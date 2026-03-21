---
id: derivatives-of-inverse-trig-functions
title: Derivatives of Inverse Trigonometric Functions
domain: mathematics
course: calculus-1
prerequisites:
  - id: implicit-differentiation
    type: hard
  - id: inverse-trigonometric-functions
    type: hard
builds-toward:
  - trigonometric-substitution
tags: [derivatives, inverse-trig, arcsin, arctan]
stage: formal-systems
status: validated
---

# Derivatives of Inverse Trigonometric Functions

## Core Idea
The derivatives of the inverse trig functions produce algebraic expressions: d/dx[arcsin(x)] = 1/sqrt(1 - x^2), d/dx[arccos(x)] = -1/sqrt(1 - x^2), d/dx[arctan(x)] = 1/(1 + x^2). These are derived using implicit differentiation (e.g., if y = arcsin(x), then sin(y) = x, differentiate implicitly). These derivatives appear frequently as results of integration, making them important both for differentiation and for recognizing integral forms.

## How It's Best Learned
Derive each using implicit differentiation and Pythagorean identities. Practice with chain rule applications: d/dx[arctan(3x)], d/dx[arcsin(x^2)]. Recognize the integral forms: integral of 1/(1 + x^2) dx = arctan(x) + C.

## Common Misconceptions
- Confusing the derivative of arcsin with the derivative of arccos (they differ by a sign).
- Forgetting the chain rule when the argument is not simply x.
- Not recognizing 1/(1 + x^2) as the derivative of arctan in integration problems.

## Questions

```yaml
- question: "A student needs to find ∫1/(1 + 9x²) dx. She rewrites the denominator as 1 + (3x)². What is the correct antiderivative?"
  type: multiple-choice
  options:
    - "(1/3)arctan(3x) + C"
    - "arctan(3x) + C"
    - "(1/9)arctan(3x) + C"
    - "3·arctan(3x) + C"
  answer: 0
  explanation: "Use u = 3x, so du = 3dx, meaning dx = du/3. The integral becomes ∫1/(1 + u²) · (du/3) = (1/3)arctan(u) + C = (1/3)arctan(3x) + C. The factor of 1/3 comes from the substitution: when the argument of arctan is (3x) rather than x, the chain rule in reverse requires dividing by the inner derivative (3). Check by differentiating: d/dx[(1/3)arctan(3x)] = (1/3) · 1/(1+(3x)²) · 3 = 1/(1+9x²). ✓"

- question: "To derive d/dx[arcsin(x)], a student writes sin(y) = x and differentiates implicitly, obtaining cos(y)·(dy/dx) = 1. The correct next step is:"
  type: multiple-choice
  options:
    - "Use the Pythagorean identity to write cos(y) = √(1 − x²), accounting for the restricted domain of arcsin, then solve for dy/dx"
    - "Set cos(y) = x, since sin(y) = x implies cos(y) = x by symmetry"
    - "Apply the quotient rule to 1/cos(y) to get the final derivative"
    - "Substitute y = arcsin(x) back and leave the answer as 1/cos(arcsin(x))"
  answer: 0
  explanation: "After implicit differentiation, dy/dx = 1/cos(y), but the answer must be in terms of x. Since sin(y) = x, we have sin²(y) = x², and by the Pythagorean identity cos²(y) = 1 − x². Since the domain of arcsin is [−π/2, π/2] — where cosine is non-negative — cos(y) = +√(1 − x²). Therefore dy/dx = 1/√(1 − x²). The domain restriction is crucial: without it, we could not take the positive square root."

- question: "d/dx[arccos(x)] = 1/√(1 − x²), the same formula as d/dx[arcsin(x)]."
  type: true-false
  answer: false
  explanation: "d/dx[arccos(x)] = −1/√(1 − x²) — the same magnitude but with a minus sign. This follows from the identity arcsin(x) + arccos(x) = π/2 (a constant). Differentiating both sides: d/dx[arcsin(x)] + d/dx[arccos(x)] = 0, so d/dx[arccos(x)] = −d/dx[arcsin(x)] = −1/√(1 − x²). The minus sign is the most common error when recalling this formula."

- question: "d/dx[arctan(x²)] = 2x/(1 + x⁴), obtained by applying the arctan derivative formula to x² and multiplying by the derivative of x²."
  type: true-false
  answer: true
  explanation: "By the chain rule with u = x²: d/dx[arctan(x²)] = 1/(1 + (x²)²) · d/dx[x²] = 1/(1 + x⁴) · 2x = 2x/(1 + x⁴). The outer derivative is 1/(1 + u²) evaluated at u = x², giving 1/(1 + x⁴); the inner derivative is 2x. Their product is 2x/(1 + x⁴). The most common error is forgetting the inner derivative and writing 1/(1 + x⁴) alone."

- question: "Explain how implicit differentiation is used to derive d/dx[arctan(x)] = 1/(1 + x²). What role does a Pythagorean identity play in the derivation?"
  type: short-answer
  answer: "Let y = arctan(x), so tan(y) = x. Differentiate both sides with respect to x using the chain rule: sec²(y) · dy/dx = 1. Solve: dy/dx = 1/sec²(y). To express this in terms of x, use the identity sec²(y) = 1 + tan²(y) = 1 + x² (since tan(y) = x). Therefore dy/dx = 1/(1 + x²). The Pythagorean identity is the step that converts the expression from y-form to x-form, completing the derivation."
  explanation: "The same strategy applies to all inverse trig derivatives: (1) write the trig equation from the inverse function definition, (2) differentiate implicitly, (3) solve for dy/dx, (4) use a Pythagorean identity to re-express in terms of x. For arcsin: sin(y) = x → cos(y)·dy/dx = 1 → use cos²(y) = 1 − sin²(y) = 1 − x² → dy/dx = 1/√(1−x²). No new rules are needed — just implicit differentiation applied to a known inverse relationship, followed by an algebraic substitution using a trig identity."
```

## Explainer

To find the derivative of arcsin(x), you don't need a new rule — you need implicit differentiation, which you already know. Let y = arcsin(x). By definition of the inverse, this means sin(y) = x, where y ∈ [-π/2, π/2]. Differentiate both sides with respect to x using the chain rule: cos(y) · (dy/dx) = 1. Solve for dy/dx: dy/dx = 1/cos(y). The result should be in terms of x, not y, so substitute back. From the Pythagorean identity, cos²(y) = 1 - sin²(y) = 1 - x², and since y ∈ [-π/2, π/2] where cosine is non-negative, cos(y) = √(1 - x²). Therefore d/dx[arcsin(x)] = 1/√(1 - x²). The entire derivation is just implicit differentiation plus a Pythagorean identity substitution.

The same strategy yields the other derivatives. For arctan: let y = arctan(x), so tan(y) = x. Differentiating implicitly: sec²(y) · dy/dx = 1, so dy/dx = 1/sec²(y). Using the identity sec²(y) = 1 + tan²(y) = 1 + x², we get d/dx[arctan(x)] = 1/(1 + x²). For arccos, the derivation mirrors arcsin, but the derivative of cosine introduces a minus sign: d/dx[arccos(x)] = -1/√(1 - x²). Notice that arcsin(x) + arccos(x) = π/2 (a constant), so their derivatives must sum to zero — the two formulas are negatives of each other, which serves as a self-consistency check.

These algebraic-looking results are surprising at first — why does differentiating a trigonometric function produce something involving square roots? The answer is that the inverse functions "undo" the original trig functions, and the algebraic expressions encode the geometry of those functions' slopes at each point. But the key practical payoff is in integration: encountering 1/√(1 - x²) in an integral should immediately trigger recognition of arcsin. The antiderivatives ∫1/√(1 - x²)dx = arcsin(x) + C and ∫1/(1 + x²)dx = arctan(x) + C are among the most commonly occurring results in calculus, and they appear frequently as the answers to trigonometric substitution problems.

When the argument is a composite function, the chain rule applies as always. For d/dx[arctan(3x)]: the outer derivative formula gives 1/(1 + (3x)²) and the inner derivative of 3x is 3, so the answer is 3/(1 + 9x²). For d/dx[arcsin(x²)]: outer derivative is 1/√(1 - (x²)²) = 1/√(1 - x⁴), inner derivative is 2x, so the answer is 2x/√(1 - x⁴). The common error is applying the formula correctly but forgetting to multiply by the inner derivative — always check whether the argument is just x or something more complex.

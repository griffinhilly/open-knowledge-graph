---
id: linear-approximation
title: Linear Approximation
domain: mathematics
course: calculus-1
prerequisites:
  - id: derivative-as-slope-of-tangent
    type: hard
builds-toward:
  - differentials
  - taylor-polynomials
tags: [derivatives, applications, approximation, tangent-line]
stage: formal-systems
status: validated
---

# Linear Approximation

## Core Idea
Linear approximation uses the tangent line at a known point to estimate function values nearby: f(x) is approximately equal to L(x) = f(a) + f'(a)(x - a) for x near a. This is the simplest and most practical consequence of differentiability. It is the foundation for differentials, Newton's method, and Taylor polynomials. The quality of the approximation depends on how close x is to a and how curved the function is.

## How It's Best Learned
Approximate values like sqrt(4.1) by linearizing sqrt(x) at x = 4. Compare the approximation with the true value to see the error. Discuss when the approximation is good (f is nearly linear near a) vs. poor (high curvature).

## Common Misconceptions
- Using a tangent line centered at a point far from the target value.
- Forgetting that the approximation gets worse as you move further from a.
- Confusing linear approximation (one term) with higher-order Taylor approximation.

## Questions

```yaml
- question: "You want to approximate f(x) = sin(x) near a = 0 using a linear approximation. Which estimate will be least accurate?"
  type: multiple-choice
  options:
    - "sin(0.01)"
    - "sin(0.1)"
    - "sin(0.5)"
    - "sin(1.5)"
  answer: 3
  explanation: "Linear approximation L(x) = f(a) + f'(a)(x−a) gets less accurate as x moves farther from a. At a = 0, sin(x) ≈ x. The estimate for sin(1.5) is farthest from the center a = 0, where the function has curved significantly away from the tangent line. The error grows with both distance from a and the curvature of f near a."

- question: "A function has f(5) = 3 and f'(5) = 2. What is the linear approximation L(5.001)?"
  type: multiple-choice
  options:
    - "3.001 — because L(x) ≈ f(a) + (x − a)"
    - "3.002 — because L(x) = f(a) + f'(a)(x − a)"
    - "10.002 — because f'(5) × 5.001 ≈ 10"
    - "5.002 — because the tangent line passes through (a, f'(a))"
  answer: 1
  explanation: "L(x) = f(a) + f'(a)(x − a) = 3 + 2(5.001 − 5) = 3 + 2(0.001) = 3.002. The formula is the point-slope equation of the tangent line at (a, f(a)), evaluated at x. Option A confuses f'(a) with 1; options C and D misapply the formula entirely."

- question: "The linear approximation L(x) always overestimates the true value of a concave-down function (f'' < 0) near the base point a."
  type: true-false
  answer: true
  explanation: "When f''(a) < 0, the function curves downward — it bends below the tangent line on both sides of a. This means the tangent line lies above the curve, so L(x) ≥ f(x) near a, giving an overestimate. The second derivative reveals not just the magnitude of the error but its direction, even though f'' doesn't appear in the formula L(x) = f(a) + f'(a)(x − a) itself."

- question: "Linear approximation is only useful when the exact value of f(x) is completely unknown to the user."
  type: true-false
  answer: false
  explanation: "Linear approximation is valuable when exact computation is difficult, not merely when the value is unknown. Approximating √4.1 by linearizing at a = 4 provides a quick, accurate estimate without a calculator. But the technique's importance extends further: it is the foundation for differentials, Newton's root-finding method, and Taylor polynomials. Its value is computational convenience and conceptual generativity, not just filling gaps in knowledge."

- question: "Why does the accuracy of a linear approximation depend on f''(a), even though the formula L(x) = f(a) + f'(a)(x − a) contains no second derivative term?"
  type: short-answer
  answer: "f''(a) measures how sharply the function curves away from the tangent line. A large |f''(a)| means the function bends steeply, so the tangent diverges quickly from the curve as x moves away from a. A small |f''(a)| means the function is nearly linear near a, and the approximation stays accurate over a wider range. The leading error term in the Taylor expansion is (1/2)f''(a)(x−a)², so f'' directly governs the approximation error."
  explanation: "The linear approximation is the first-order Taylor polynomial. The 'missing' second-derivative term is precisely what makes it an approximation rather than the exact value. Understanding this reveals why L(x) works so well for √x at a = 4 (small f'' there) but would be less reliable for functions with large curvature — the formula doesn't include the error, but the error is always there, governed by f''."
```

## Explainer

You already know that the derivative f'(a) is the slope of the tangent line to y = f(x) at x = a. Linear approximation takes the next step: that tangent line is not just a line that touches the curve at one point — it is the best linear approximation to the function near that point. If you zoom in close enough to any differentiable function, the function and its tangent line become indistinguishable. Linear approximation exploits this fact to estimate function values that would otherwise require a calculator.

The formula is L(x) = f(a) + f'(a)(x − a). This is simply the point-slope equation of the tangent line at (a, f(a)), rearranged in a useful way. To approximate √4.1, choose a = 4, where you know the exact value: f(x) = √x, f(4) = 2, f'(x) = 1/(2√x), f'(4) = 1/4. The linear approximation is L(x) = 2 + (1/4)(x − 4). At x = 4.1: L(4.1) = 2 + (1/4)(0.1) = 2.025. The true value is approximately 2.02485 — the approximation is excellent because 4.1 is very close to 4, and √x is nearly linear in a small neighborhood of 4.

The quality of the approximation depends on two things: how far x is from a, and how curved the function is near a. The curvature is captured by the second derivative — a large |f''(a)| means the function bends sharply away from the tangent line, and the approximation degrades quickly. A small |f''(a)| means the function is nearly linear, and the tangent line stays close for a wider range of x. This is why L(x) works well for √x at a = 4 but would be less accurate at a = 0.01, where the function curves steeply.

Linear approximation is the foundation for several tools you'll encounter next. **Differentials** restate it using the notation df = f'(a)dx, emphasizing the infinitesimal change perspective. **Newton's method** for root-finding iteratively applies linear approximation: it replaces the curve with its tangent line, finds where the tangent crosses zero, and uses that as the next approximation. **Taylor polynomials** extend the idea by adding higher-degree correction terms, starting with the quadratic correction (1/2)f''(a)(x−a)². Linear approximation is the first-order Taylor polynomial — the foundation of a hierarchy of increasingly accurate polynomial approximations.

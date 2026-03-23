---
id: newtons-method-convergence-analysis
title: Newton's Method for Root-Finding (Convergence Analysis)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
builds-toward:
- order-of-convergence
tags:
- newtons-method
- root-finding
- quadratic-convergence
stage: formal-systems
status: draft
---

# Newton's Method for Root-Finding (Convergence Analysis)

## Core Idea
Newton's method approximates roots using x_{n+1} = x_n - f(x_n)/f'(x_n), derived by linearizing f around x_n via Taylor expansion. Near a simple root, the method exhibits quadratic convergence, roughly doubling the number of correct digits with each iteration. However, it requires derivative evaluation and convergence depends on the initial guess.

## Questions

```yaml
- question: "Newton's method is applied to a function with a simple root. After several iterations, the error is approximately 0.01. Roughly what will the error be after two more iterations?"
  type: multiple-choice
  options:
    - "About 0.005 — the method halves the error each step"
    - "About 0.000001 — the error is squared twice (0.01² = 0.0001, then 0.0001² = 0.00000001)"
    - "About 0.000001 — the error is squared twice (0.01² = 0.0001, 0.0001² ≈ 10⁻⁸)"
    - "About 0.000001 — the error drops by 10x each step"
  answer: 2
  explanation: "Quadratic convergence means εₙ₊₁ ≈ C·εₙ². Starting from ε ≈ 0.01: after one step, ε ≈ (0.01)² = 10⁻⁴; after another step, ε ≈ (10⁻⁴)² = 10⁻⁸. Option A describes linear (bisection-like) convergence. The key insight is that the error is *squared*, not halved — this is why Newton's method delivers roughly double the number of correct digits per iteration."

- question: "Newton's method is applied to f(x) = x² at the root x = 0 (a double root). Compared to its behavior at a simple root, the convergence is:"
  type: multiple-choice
  options:
    - "Still quadratic, but the constant C = |f″/2f′| is larger"
    - "Degraded to linear convergence, because f′(0) = 0 makes the constant C blow up"
    - "Faster than at a simple root, because the function is flatter near the root"
    - "Undefined — Newton's method cannot be applied when the function has a double root"
  answer: 1
  explanation: "The quadratic convergence constant is C = |f″(r)/2f′(r)|. At a double root, f′(r) = 0, so this constant blows up — the proof of quadratic convergence breaks down entirely. In practice, Newton's method on x² converges only linearly (each step cuts the error by a constant fraction, roughly 1/2). This is why the convergence proof requires f′(r) ≠ 0, the definition of a simple root."

- question: "Newton's method is guaranteed to converge to a root for any starting point, as long as the function is differentiable."
  type: true-false
  answer: false
  explanation: "Newton's method is only *locally* convergent: the guarantee of convergence applies only when the starting guess is already close enough to the root. Far from the root, the tangent-line approximation can send the iteration to a different region, into a cycle, or to infinity. This sensitivity to initial conditions is why Newton's method is often paired with a globally reliable method (e.g., bisection) to first get close, before switching to Newton for fast polishing."

- question: "Quadratic convergence means that each Newton iteration reduces the error by the same constant multiplicative factor."
  type: true-false
  answer: false
  explanation: "Quadratic convergence means the error is *squared* each step: εₙ₊₁ ≈ C·εₙ². Reducing the error by a constant factor each step is *linear* convergence (e.g., bisection). The distinction matters enormously in practice: linear convergence adds one correct digit per few iterations, while quadratic convergence doubles the number of correct digits per iteration — going from 2 correct digits to 4 to 8 to 16 in just four steps."

- question: "Why does Newton's method exhibit quadratic convergence near a simple root, and what property of the root makes this break down?"
  type: short-answer
  answer: "The Taylor expansion of f(r) = 0 around xₙ shows that the error in the next iterate is proportional to the *square* of the current error — the linear term cancels because Newton's update is designed to zero it, leaving only second-order terms. This gives εₙ₊₁ ≈ |f″(r)/2f′(r)| · εₙ². At a double root, f′(r) = 0, so the denominator of this constant vanishes and the quadratic rate breaks down, degrading to linear convergence."
  explanation: "The root cause of quadratic convergence is that Newton's step exactly cancels the first-order Taylor term; only the quadratic remainder survives. The condition f′(r) ≠ 0 (simple root) is what keeps the convergence constant finite and the analysis valid. Double roots violate this, and the performance penalty is severe: what was exponentially fast convergence becomes merely linear."
```

## Explainer

Newton's method is one of the most elegant applications of the **Taylor series** you already know. Suppose you want to solve f(x) = 0, and you have a current guess xₙ that is close to the true root r. Expanding f around xₙ: f(x) ≈ f(xₙ) + f′(xₙ)(x − xₙ). Setting this linear approximation to zero and solving for x gives x = xₙ − f(xₙ)/f′(xₙ). Call this xₙ₊₁. You've replaced f with its tangent line at xₙ and found where the tangent line crosses zero — geometrically, you're following the tangent until it hits the x-axis, then starting over. Each iteration uses the local linear approximation to improve the guess.

The remarkable property is **quadratic convergence**, which means the error roughly squares with each step. If the error at step n is εₙ = |xₙ − r|, then εₙ₊₁ ≈ C·εₙ² for some constant C. To see why, write the Taylor expansion of f(r) = 0 around xₙ: 0 = f(xₙ) + f′(xₙ)(r − xₙ) + (1/2)f″(xₙ)(r − xₙ)² + ... Rearranging, r − xₙ₊₁ ≈ −(f″(xₙ)/2f′(xₙ))(r − xₙ)², so εₙ₊₁ ≈ |f″(r)/2f′(r)| · εₙ². The quadratic dependence on the previous error is why Newton's method doubles the number of correct decimal digits with each step. Starting from an error of 0.01, you get 0.0001, then 10⁻⁸, then 10⁻¹⁶ — four iterations for 16 correct digits.

The constant C = |f″(r)/2f′(r)| reveals when the method is fast or slow. If f′(r) is small — meaning the root is near a local extremum — C blows up and convergence degrades or fails entirely. Indeed, at a double root where f′(r) = 0, Newton's method loses its quadratic rate and converges only linearly (each step cuts the error by a constant factor rather than squaring it). This is why the convergence proof requires f′(r) ≠ 0, the definition of a **simple root**.

The other crucial caveat is initial guess sensitivity. Newton's method is locally quadratically convergent: the guarantee only holds when xₙ is close enough to r. Far from the root, the tangent-line approximation can send the iteration to a completely different region, cycle, or diverge to infinity. Choosing a good starting point often requires a preliminary global search (e.g., bisection to isolate a root) followed by Newton's method to polish the result. This hybrid strategy — slow but globally reliable bisection to get close, then fast quadratically convergent Newton to finish — is a standard engineering pattern in root-finding software.

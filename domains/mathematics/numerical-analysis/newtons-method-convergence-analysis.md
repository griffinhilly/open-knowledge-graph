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
stage: advanced
status: draft
---

# Newton's Method for Root-Finding (Convergence Analysis)

## Core Idea
Newton's method approximates roots using x_{n+1} = x_n - f(x_n)/f'(x_n), derived by linearizing f around x_n via Taylor expansion. Near a simple root, the method exhibits quadratic convergence, roughly doubling the number of correct digits with each iteration. However, it requires derivative evaluation and convergence depends on the initial guess.

## Explainer

Newton's method is one of the most elegant applications of the **Taylor series** you already know. Suppose you want to solve f(x) = 0, and you have a current guess xₙ that is close to the true root r. Expanding f around xₙ: f(x) ≈ f(xₙ) + f′(xₙ)(x − xₙ). Setting this linear approximation to zero and solving for x gives x = xₙ − f(xₙ)/f′(xₙ). Call this xₙ₊₁. You've replaced f with its tangent line at xₙ and found where the tangent line crosses zero — geometrically, you're following the tangent until it hits the x-axis, then starting over. Each iteration uses the local linear approximation to improve the guess.

The remarkable property is **quadratic convergence**, which means the error roughly squares with each step. If the error at step n is εₙ = |xₙ − r|, then εₙ₊₁ ≈ C·εₙ² for some constant C. To see why, write the Taylor expansion of f(r) = 0 around xₙ: 0 = f(xₙ) + f′(xₙ)(r − xₙ) + (1/2)f″(xₙ)(r − xₙ)² + ... Rearranging, r − xₙ₊₁ ≈ −(f″(xₙ)/2f′(xₙ))(r − xₙ)², so εₙ₊₁ ≈ |f″(r)/2f′(r)| · εₙ². The quadratic dependence on the previous error is why Newton's method doubles the number of correct decimal digits with each step. Starting from an error of 0.01, you get 0.0001, then 10⁻⁸, then 10⁻¹⁶ — four iterations for 16 correct digits.

The constant C = |f″(r)/2f′(r)| reveals when the method is fast or slow. If f′(r) is small — meaning the root is near a local extremum — C blows up and convergence degrades or fails entirely. Indeed, at a double root where f′(r) = 0, Newton's method loses its quadratic rate and converges only linearly (each step cuts the error by a constant factor rather than squaring it). This is why the convergence proof requires f′(r) ≠ 0, the definition of a **simple root**.

The other crucial caveat is initial guess sensitivity. Newton's method is locally quadratically convergent: the guarantee only holds when xₙ is close enough to r. Far from the root, the tangent-line approximation can send the iteration to a completely different region, cycle, or diverge to infinity. Choosing a good starting point often requires a preliminary global search (e.g., bisection to isolate a root) followed by Newton's method to polish the result. This hybrid strategy — slow but globally reliable bisection to get close, then fast quadratically convergent Newton to finish — is a standard engineering pattern in root-finding software.

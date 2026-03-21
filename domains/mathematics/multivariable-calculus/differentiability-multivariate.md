---
id: differentiability-multivariate
title: Differentiability in Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: limits-continuity-multivariable
  type: hard
builds-toward:
- total-differential
- chain-rule-multivariable
- tangent-planes-linear-approximation
tags:
- differentiability
- continuity
- linear-approximation
stage: formal-systems
status: draft
---

# Differentiability in Multivariable Functions

## Core Idea
A function f(x, y) is differentiable at (a, b) if it can be well-approximated by a linear function; equivalently, if the error in the linear approximation vanishes faster than the distance to (a, b). Existence of continuous partial derivatives guarantees differentiability.

## Questions

```yaml
- question: "Function f has both partial derivatives fₓ(0,0) = 0 and f_y(0,0) = 0, yet f is not continuous at (0,0). What does this imply?"
  type: multiple-choice
  options:
    - "This is impossible — if both partial derivatives exist, continuity is guaranteed"
    - "f is differentiable at (0,0) because both partial derivatives exist"
    - "f is not differentiable at (0,0), since differentiability implies continuity and continuity fails"
    - "f is differentiable but the tangent plane formula does not apply"
  answer: 2
  explanation: "Differentiability is a strictly stronger condition than the existence of partial derivatives. The hierarchy is: differentiable ⟹ continuous ⟹ (partial derivatives may exist). Since differentiability implies continuity, if continuity fails at (0,0) then differentiability must also fail — regardless of whether partial derivatives exist. This example illustrates that partial derivatives only measure rates of change along the coordinate axes; they say nothing about behavior in diagonal or other directions."

- question: "Which of the following is a sufficient condition that guarantees a function f(x,y) is differentiable at (a,b)?"
  type: multiple-choice
  options:
    - "Both partial derivatives fₓ and f_y exist at (a,b)"
    - "f is continuous at (a,b)"
    - "Both partial derivatives fₓ and f_y exist and are continuous in a neighborhood of (a,b)"
    - "The gradient vector ∇f(a,b) is nonzero"
  answer: 2
  explanation: "Mere existence of partial derivatives (option A) does not guarantee differentiability — the function could behave badly in non-axis directions. Continuity alone (option B) doesn't imply differentiability either. The reliable sufficient condition is that the partial derivatives *exist and are continuous* in a neighborhood of (a,b). This guarantees the linear approximation works in all directions, not just along the axes."

- question: "If f(x,y) is differentiable at (a,b), then both partial derivatives fₓ(a,b) and f_y(a,b) exist."
  type: true-false
  answer: true
  explanation: "Differentiability implies the existence of partial derivatives. The formal definition of differentiability requires that there exist constants L₁ and L₂ such that the linear approximation using L₁h + L₂k vanishes faster than √(h²+k²). When this holds, restricting to h=0 or k=0 recovers the limit definitions of f_y and fₓ respectively — so both must exist and equal L₂ and L₁. The implication goes one way: differentiability ⟹ partial derivatives exist (but not conversely)."

- question: "If both partial derivatives of f(x,y) exist at every point in ℝ², then f is differentiable at every point in ℝ²."
  type: true-false
  answer: false
  explanation: "Existence of partial derivatives does not guarantee differentiability. A classic counterexample: f(x,y) = xy/√(x²+y²) for (x,y) ≠ (0,0) and f(0,0) = 0. Both fₓ(0,0) and f_y(0,0) exist (both equal 0), yet f is not differentiable at the origin because the linear approximation using 0·h + 0·k does not vanish faster than √(h²+k²) when approaching along the line y = x. The partial derivatives only measure axis-aligned rates of change, missing the function's behavior in other directions."

- question: "Why is the existence of partial derivatives not sufficient to guarantee differentiability in multivariable calculus, when the existence of a derivative is sufficient in single-variable calculus?"
  type: short-answer
  answer: "In single-variable calculus, there is only one direction to approach a point (from the left or right along the number line), so the derivative captures all approach directions. In multivariable calculus, a point in ℝ² can be approached from infinitely many directions. Partial derivatives only measure rates of change along the x-axis and y-axis directions. A function can have well-defined rates along both axes while behaving wildly in diagonal or other directions — for example, not even being continuous. Differentiability requires the linear approximation to work uniformly across all approach directions, which is a genuinely stronger condition."
  explanation: "The asymmetry between 1D and 2D differentiability is one of the deepest conceptual shifts in multivariable calculus. In 1D, 'differentiable' = 'has a derivative' = 'has a tangent line approximation.' In 2D, 'has partial derivatives' is far weaker than 'has a tangent plane approximation.' The definition of differentiability captures exactly what 'tangent plane' should mean: a linear function that approximates f well in *every* direction, not just north-south and east-west."
```

## Explainer

In single-variable calculus, differentiability at a point a meant the function had a tangent line — a linear function L(x) = f(a) + f'(a)(x − a) that approximated f so well that the relative error vanished: [f(x) − L(x)] / (x − a) → 0 as x → a. You learned from partial derivatives that f has well-defined rates of change in the x-direction and y-direction at any point. Differentiability in the multivariable setting asks for something stronger: a **tangent plane** that approximates f well from *every* direction, not just the coordinate directions.

Formally, f(x, y) is **differentiable** at (a, b) if there exist constants L₁ and L₂ such that the error in the linear approximation vanishes faster than the distance:

  lim₍h,k₎→(0,0) [f(a+h, b+k) − f(a,b) − L₁h − L₂k] / √(h² + k²) = 0

When differentiability holds, L₁ = fₓ(a, b) and L₂ = f_y(a, b) must be the partial derivatives. So differentiability does not introduce new numbers — it imposes a *quality condition* on the partial derivatives: the linear function built from them must approximate f well in all directions, not just along the axes.

The subtle point is that partial derivatives *alone* do not guarantee differentiability. You can construct functions where fₓ and f_y both exist at a point, yet the function is not even continuous there — the rates along the axes exist, but the function behaves wildly in diagonal directions. Differentiability is a genuinely stronger condition than the mere existence of partial derivatives because it constrains the function's behavior uniformly across all approaching directions.

The practical theorem you will use most: if fₓ and f_y exist and are **continuous** in a neighborhood of (a, b), then f is differentiable at (a, b). Continuous partial derivatives are the reliable sufficient condition. This guarantees the chain rule applies, the tangent plane formula is valid, and directional derivatives in every direction can be computed as the dot product of the gradient with the direction vector. The hierarchy is: continuous partial derivatives ⟹ differentiable ⟹ continuous, and each implication is strict — the converses fail in general.

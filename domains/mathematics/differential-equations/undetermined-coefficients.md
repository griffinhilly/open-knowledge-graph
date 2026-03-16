---
id: undetermined-coefficients
title: Method of Undetermined Coefficients
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: characteristic-equation-method
  type: hard
builds-toward:
- higher-order-linear-odes
tags:
- particular-solution
- undetermined-coefficients
- non-homogeneous
stage: formal-systems
status: draft
---

# Method of Undetermined Coefficients

## Core Idea
To solve y'' + py' + qy = f(x), find the homogeneous solution y_h, then guess the form of a particular solution y_p based on f(x). For f polynomial, exponential, sine, or cosine, use corresponding y_p forms with unknown coefficients. Substitute into the equation and solve for these coefficients. The general solution is y = y_h + y_p. This method is efficient when applicable.

## Explainer

You've already solved y″ + py′ + qy = 0 using the characteristic equation. The roots r₁, r₂ give the **homogeneous solution** y_h — for real distinct roots, y_h = C₁e^{r₁x} + C₂e^{r₂x}. Now add a forcing function f(x) on the right side. The equation is no longer asking "what decays to zero?" but "what produces exactly f(x) when differentiated and combined?" You need a **particular solution** y_p that satisfies the full equation, then combine: the **general solution** is y = y_h + y_p.

The insight behind undetermined coefficients is that differentiation preserves certain functional forms. Derivatives of polynomials are polynomials; derivatives of e^{αx} are multiples of e^{αx}; derivatives of sin(βx) and cos(βx) cycle back to sines and cosines. So if f(x) is built from these forms, a y_p of the same form has a chance of working. The strategy: **guess the form of y_p, substitute into the ODE, and solve for the unknown coefficients** by matching both sides.

The guessing rules: if f(x) = xⁿ (polynomial of degree n), try y_p = Aₙxⁿ + ··· + A₁x + A₀ (a full polynomial of degree n). If f(x) = e^{αx}, try y_p = Ae^{αx}. If f(x) = sin(βx) or cos(βx), always try y_p = A cos(βx) + B sin(βx) together — even if only sine or cosine appears in f, both terms are needed because differentiating introduces the other. Products combine: f(x) = x²e^{3x} calls for y_p = (Ax² + Bx + C)e^{3x}.

The critical exception is the **modification rule** (also called the resonance case). If your initial guess for y_p would duplicate a term already present in y_h, that guess will produce zero when substituted into the left side of the homogeneous part and can never match f(x). The fix: multiply the guess by x. If the duplication persists, multiply by x². For example, if y_h includes e^{2x} and f(x) = e^{2x}, the usual guess Ae^{2x} fails — use Axe^{2x} instead. This modification is analogous to the repeated-root adjustment in the characteristic equation method, and understanding why it's needed connects the algebra directly to the structure of the solution space.

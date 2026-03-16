---
id: fundamental-theorem-of-calculus-part-1
title: Fundamental Theorem of Calculus Part 1
domain: mathematics
course: calculus-1
prerequisites:
- id: definite-integral-definition
  type: hard
- id: continuity-definition
  type: hard
- id: antiderivatives
  type: soft
builds-toward:
- fundamental-theorem-of-calculus-part-2
tags:
- integration
- FTC
- fundamental-theorem
stage: formal-systems
status: validated
---
# Fundamental Theorem of Calculus Part 1

## Core Idea
FTC Part 1 states that if f is continuous on [a, b], then the function g(x) = integral from a to x of f(t) dt is an antiderivative of f: g'(x) = f(x). In other words, differentiation undoes integration. This theorem guarantees that every continuous function has an antiderivative and connects the two branches of calculus (differential and integral). With the chain rule, d/dx[integral from a to h(x) of f(t) dt] = f(h(x)) * h'(x).

## How It's Best Learned
Start with concrete examples: if g(x) = integral from 0 to x of t^2 dt, compute g(x) as x^3/3 and verify g'(x) = x^2. Then apply to functions defined by integrals whose antiderivatives are not elementary. Practice the chain rule extension. Emphasize the deep meaning: integration and differentiation are inverse processes.

## Common Misconceptions
- Confusing FTC Part 1 (derivative of an integral) with FTC Part 2 (evaluating a definite integral).
- Forgetting the chain rule when the upper limit is not simply x.
- Not recognizing that the variable of integration (t) is a dummy variable, distinct from x.

## Explainer

You know the definite integral as a limit of Riemann sums — a way of measuring accumulated area under a curve. Now define a new function by letting the upper limit of that integral vary: g(x) = ∫ from a to x of f(t) dt. This **accumulation function** g(x) records how much total area has piled up between a and x as x increases. FTC Part 1 says: if f is continuous, then g'(x) = f(x). Differentiating an accumulation function gives back the original integrand.

The intuition is direct. As x increases by a tiny amount Δx, the additional area accumulated is approximately f(x) · Δx — a thin rectangle of height f(x) and width Δx. So g(x + Δx) − g(x) ≈ f(x) · Δx, which gives [g(x + Δx) − g(x)] / Δx ≈ f(x). Taking the limit as Δx → 0 recovers the derivative definition exactly. Continuity of f ensures this approximation tightens to an equality in the limit.

This is a profound structural result: it says that **every continuous function has an antiderivative**, namely its own accumulation function. Before the FTC, you might have wondered whether every function could be "anti-differentiated" — the answer is yes, at least in principle, as long as continuity holds. The theorem also reveals that differentiation and integration are inverse operations: integrating f and then differentiating returns f, just as multiplying and then dividing returns the original number.

When the upper limit is a function h(x) rather than just x, the **chain rule** enters. Let g(x) = ∫ from a to h(x) of f(t) dt. Define G(u) = ∫ from a to u of f(t) dt, so g(x) = G(h(x)). By the chain rule, g'(x) = G'(h(x)) · h'(x) = f(h(x)) · h'(x). For example, if g(x) = ∫ from 1 to x² of sin(t³) dt, then g'(x) = sin((x²)³) · 2x = 2x sin(x⁶). Notice that t is a **dummy variable** — it labels the integration variable inside the integral but does not appear in the output g(x). The output depends only on x (the upper limit), not t.

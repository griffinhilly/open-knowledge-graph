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

## Questions

```yaml
- question: "If g(x) = ∫₀ˣ t² dt, what is g'(x)?"
  type: multiple-choice
  options:
    - "x³/3 — the antiderivative of t² evaluated at x"
    - "x² — the integrand evaluated at the upper limit x"
    - "2x — the derivative of x² applied to the upper limit"
    - "0 — differentiating a definite integral always gives zero"
  answer: 1
  explanation: "By FTC Part 1, differentiating an accumulation function g(x) = ∫ₐˣ f(t) dt returns the integrand: g'(x) = f(x). Here f(t) = t², so g'(x) = x². Option A (x³/3) is g(x) itself — the antiderivative, not its derivative. Option C confuses applying the power rule to x² with applying FTC. Option D reflects the false belief that definite integrals are constants, ignoring that the upper limit varies with x."

- question: "What is d/dx[∫₁^(x²) sin(t) dt]?"
  type: multiple-choice
  options:
    - "sin(x²) · 2x"
    - "sin(x²)"
    - "cos(x²) · 2x"
    - "sin(x) · 2x"
  answer: 0
  explanation: "When the upper limit is a function h(x) = x², apply the chain rule: d/dx[∫ₐ^(h(x)) f(t) dt] = f(h(x)) · h'(x). Here f(t) = sin(t) and h(x) = x², so the result is sin(x²) · 2x. Option B forgets the chain rule factor 2x. Option C mistakenly differentiates sin to get cos. Option D wrongly substitutes x into the integrand instead of h(x) = x²."

- question: "The function g(x) = ∫₀ˣ e^(t²) dt has no closed-form antiderivative formula, yet it is still a valid function with a well-defined derivative."
  type: true-false
  answer: true
  explanation: "FTC Part 1 guarantees that g'(x) = e^(x²) — this holds regardless of whether g(x) can be expressed using elementary functions. The theorem proves that every continuous function has an antiderivative (namely its own accumulation function), even when no formula exists. The existence of an antiderivative and the existence of a closed-form expression for it are separate questions."

- question: "In the expression ∫₀ˣ f(t) dt, the variable t affects the final output g(x), so substituting a different dummy variable would change the function."
  type: true-false
  answer: false
  explanation: "The variable t is a dummy variable — it labels positions inside the integral but disappears in the output. The expression ∫₀ˣ f(t) dt is identical to ∫₀ˣ f(u) du or ∫₀ˣ f(s) ds. The output depends only on x (the upper limit), not on whatever letter is used inside. Changing the dummy variable is purely notational and has no effect on g(x)."

- question: "Why does FTC Part 1 imply that every continuous function has an antiderivative, and why is this significant?"
  type: short-answer
  answer: "FTC Part 1 states that if f is continuous on [a, b], then g(x) = ∫ₐˣ f(t) dt is differentiable and g'(x) = f(x) — meaning g is an antiderivative of f, constructed explicitly as an accumulation function. Since this construction works for any continuous f, every continuous function has an antiderivative. The significance is that antiderivatives exist even when no elementary formula can express them (e.g., e^(x²) or sin(x)/x), and that integration and differentiation are inverse operations."
  explanation: "Before FTC, there was no guarantee that every continuous function could be anti-differentiated. The theorem resolves this by constructing the antiderivative directly as an accumulation function. This also reveals the deep structural unity of calculus: differentiation and integration undo each other, just as multiplication and division do in arithmetic."
```

## Explainer

You know the definite integral as a limit of Riemann sums — a way of measuring accumulated area under a curve. Now define a new function by letting the upper limit of that integral vary: g(x) = ∫ from a to x of f(t) dt. This **accumulation function** g(x) records how much total area has piled up between a and x as x increases. FTC Part 1 says: if f is continuous, then g'(x) = f(x). Differentiating an accumulation function gives back the original integrand.

The intuition is direct. As x increases by a tiny amount Δx, the additional area accumulated is approximately f(x) · Δx — a thin rectangle of height f(x) and width Δx. So g(x + Δx) − g(x) ≈ f(x) · Δx, which gives [g(x + Δx) − g(x)] / Δx ≈ f(x). Taking the limit as Δx → 0 recovers the derivative definition exactly. Continuity of f ensures this approximation tightens to an equality in the limit.

This is a profound structural result: it says that **every continuous function has an antiderivative**, namely its own accumulation function. Before the FTC, you might have wondered whether every function could be "anti-differentiated" — the answer is yes, at least in principle, as long as continuity holds. The theorem also reveals that differentiation and integration are inverse operations: integrating f and then differentiating returns f, just as multiplying and then dividing returns the original number.

When the upper limit is a function h(x) rather than just x, the **chain rule** enters. Let g(x) = ∫ from a to h(x) of f(t) dt. Define G(u) = ∫ from a to u of f(t) dt, so g(x) = G(h(x)). By the chain rule, g'(x) = G'(h(x)) · h'(x) = f(h(x)) · h'(x). For example, if g(x) = ∫ from 1 to x² of sin(t³) dt, then g'(x) = sin((x²)³) · 2x = 2x sin(x⁶). Notice that t is a **dummy variable** — it labels the integration variable inside the integral but does not appear in the output g(x). The output depends only on x (the upper limit), not t.

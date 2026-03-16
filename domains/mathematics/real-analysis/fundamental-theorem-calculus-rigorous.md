---
id: fundamental-theorem-calculus-rigorous
title: Fundamental Theorem of Calculus (Rigorous)
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-integral-properties
  type: hard
- id: rigorous-derivative-definition
  type: hard
tags:
- fundamental-theorem
- differentiation
- integration
stage: advanced
status: draft
---

# Fundamental Theorem of Calculus (Rigorous)

## Core Idea
The Fundamental Theorem has two parts: (1) if f is continuous on [a,b] and F(x) = ∫ₐˣ f, then F'(x) = f(x); (2) if F is continuous on [a,b], differentiable on (a,b), and F' is integrable, then ∫ₐᵇ F'(x) dx = F(b) - F(a). Together, they formalize that differentiation and integration are inverse operations. The rigorous proof requires uniform continuity and Darboux integrability.

## Explainer

From your study of the Riemann integral, you know that ∫_a^b f(x)dx is defined as a limit of Riemann sums — a purely geometric object measuring signed area. From your work on rigorous derivatives, you know that f'(x) = lim_{h→0}(f(x+h)−f(x))/h is defined through careful ε-δ limit arguments. The Fundamental Theorem of Calculus (FTC) reveals that these two constructions, developed independently through separate limit processes, are inverse operations of each other.

**Part 1** is the more surprising half. Define the **accumulation function** F(x) = ∫_a^x f(t)dt, measuring the signed area under f from a fixed point a to a variable endpoint x. If f is continuous on [a,b], then F is differentiable and F'(x) = f(x). The proof uses continuity directly: for small h, ∫_x^{x+h} f(t)dt ≈ f(x)·h because continuity forces f to stay near f(x) on a short interval. More precisely, by continuity, for any ε > 0 you can find δ so that |f(t) − f(x)| < ε whenever |t − x| < δ. This bounds the difference quotient (F(x+h)−F(x))/h within ε of f(x), establishing the derivative. The continuity hypothesis is doing essential work here — drop it and F can still exist (integrability is weaker than continuity) but need not be differentiable.

**Part 2** is the computational workhorse: if F is a continuous antiderivative of f on [a,b], then ∫_a^b f(x)dx = F(b) − F(a). The proof links Part 1 to the Mean Value Theorem (which you know from rigorous derivative theory). Let G(x) = ∫_a^x f(t)dt be the accumulation function. By Part 1, G'(x) = f(x). By hypothesis, F'(x) = f(x) too, so F' = G' everywhere on (a,b). The MVT implies F − G is constant on [a,b]. Evaluating at x = a: F(a) − G(a) = F(a) − 0 = F(a). So G(x) = F(x) − F(a) for all x, and G(b) = F(b) − F(a).

The rigorous treatment clarifies exactly which hypotheses each part requires and why. Part 2 only needs f to be Riemann integrable (not continuous) and F to be a continuous antiderivative — strictly weaker than Part 1's continuity hypothesis for f. Counterexamples exist for both parts when hypotheses are violated: without continuity in Part 1, the accumulation function can fail to be differentiable at specific points; without integrability in Part 2, the antiderivative evaluation formula breaks down. The theorem doesn't just assert that differentiation and integration undo each other — it precisely characterizes the conditions under which they do, which is why the rigorous version is more powerful than the informal version you may have seen in a first calculus course.

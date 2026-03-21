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

## Questions

```yaml
- question: "Let f be Riemann integrable but discontinuous on [0,1], with a jump at x = 1/2 (f(x) = 0 for x < 1/2, f(x) = 1 for x ≥ 1/2). Define F(x) = ∫₀ˣ f(t) dt. Which statement is correct?"
  type: multiple-choice
  options:
    - "F'(x) = f(x) for all x ∈ [0,1] by FTC Part 1"
    - "F is differentiable at every point where f is continuous; at x = 1/2, F may not be differentiable (or F'(1/2) may not equal f(1/2))"
    - "F is not well-defined because f is not continuous"
    - "F'(x) = f(x) everywhere because integration smooths out the discontinuity"
  answer: 1
  explanation: "FTC Part 1 requires f to be *continuous* at x to conclude F'(x) = f(x). The proof works by showing f stays near f(x) on a short interval — exactly what continuity guarantees. At a jump discontinuity x = 1/2, f makes a sudden jump no matter how small the interval, breaking the proof. F is still well-defined (f is integrable) and in fact continuous — but need not be differentiable at the jump point, or if it is, the derivative need not equal f(1/2). Option D is the common misconception: continuity is required, not bypassed by integration."

- question: "FTC Part 2 states that ∫ₐᵇ F'(x) dx = F(b) − F(a). Which hypothesis is required by Part 2 but NOT by Part 1?"
  type: multiple-choice
  options:
    - "f = F' must be continuous on [a,b]"
    - "F must be a known antiderivative — Part 2 starts from a given F with F' = f, rather than constructing F from the integral"
    - "The interval [a,b] must be bounded"
    - "F must be differentiable at the endpoints a and b"
  answer: 1
  explanation: "Parts 1 and 2 answer different questions. Part 1 constructs an antiderivative: given integrable f, define F(x) = ∫ₐˣ f(t)dt and prove F' = f when f is continuous. Part 2 evaluates an integral: given a function F that you already know is an antiderivative of f (with F' integrable), conclude ∫ₐᵇ f = F(b) − F(a). Part 2 has *weaker* hypotheses for f (integrability suffices; continuity is not required) but presupposes you have already found an antiderivative F. The two parts together link the analytic construction of antiderivatives to the geometric computation of area."

- question: "FTC Part 1 proves that every continuous function on [a,b] has an antiderivative, constructed explicitly as the accumulation function F(x) = ∫ₐˣ f(t) dt."
  type: true-false
  answer: true
  explanation: "This is precisely what Part 1 establishes: if f is continuous, then F(x) = ∫_a^x f(t)dt is differentiable and F'(x) = f(x). In other words, F is an explicit antiderivative. This is a non-trivial existence theorem: it guarantees that continuous functions always have antiderivatives, even when no closed-form expression exists. The antiderivative need not be expressible in elementary functions — but existence is guaranteed by the integral construction."

- question: "FTC Part 2 requires f to be continuous — the same hypothesis as Part 1 — because the evaluation formula F(b) − F(a) breaks down without continuity."
  type: true-false
  answer: false
  explanation: "Part 2 has strictly weaker hypotheses than Part 1. Part 1 requires continuity of f (to ensure the accumulation function is differentiable at each point). Part 2 only requires that F is a continuous antiderivative of f and that F' is Riemann integrable — f itself need not be continuous. The proof of Part 2 uses the MVT applied to F and the accumulation function G, not the continuity of f. The two parts have different hypotheses, different proofs, and serve different purposes."

- question: "Explain intuitively why Part 1 of the FTC requires continuity of f, and what breaks down in the proof if f has a jump discontinuity at x."
  type: short-answer
  answer: "Part 1 proves (F(x+h)−F(x))/h → f(x) by showing the average value of f on [x, x+h] approaches f(x) as h → 0. This relies on f staying near f(x) on a shrinking interval — precisely what continuity guarantees. If f has a jump discontinuity at x, then on any interval [x, x+h], f takes values far from f(x) on a portion that doesn't shrink away. The mean value of f on [x, x+h] does not converge to f(x), so the difference quotient fails to converge to f(x). Continuity is not just a convenient assumption — it is exactly the hypothesis that makes the average-value argument work."
  explanation: "The precise statement is: for any ε > 0, continuity gives δ such that |f(t) − f(x)| < ε for |t − x| < δ. This bounds |(F(x+h)−F(x))/h − f(x)| < ε. At a jump, no such δ exists, so no such bound can be made, and the limit may fail or yield the wrong value."
```

## Explainer

From your study of the Riemann integral, you know that ∫_a^b f(x)dx is defined as a limit of Riemann sums — a purely geometric object measuring signed area. From your work on rigorous derivatives, you know that f'(x) = lim_{h→0}(f(x+h)−f(x))/h is defined through careful ε-δ limit arguments. The Fundamental Theorem of Calculus (FTC) reveals that these two constructions, developed independently through separate limit processes, are inverse operations of each other.

**Part 1** is the more surprising half. Define the **accumulation function** F(x) = ∫_a^x f(t)dt, measuring the signed area under f from a fixed point a to a variable endpoint x. If f is continuous on [a,b], then F is differentiable and F'(x) = f(x). The proof uses continuity directly: for small h, ∫_x^{x+h} f(t)dt ≈ f(x)·h because continuity forces f to stay near f(x) on a short interval. More precisely, by continuity, for any ε > 0 you can find δ so that |f(t) − f(x)| < ε whenever |t − x| < δ. This bounds the difference quotient (F(x+h)−F(x))/h within ε of f(x), establishing the derivative. The continuity hypothesis is doing essential work here — drop it and F can still exist (integrability is weaker than continuity) but need not be differentiable.

**Part 2** is the computational workhorse: if F is a continuous antiderivative of f on [a,b], then ∫_a^b f(x)dx = F(b) − F(a). The proof links Part 1 to the Mean Value Theorem (which you know from rigorous derivative theory). Let G(x) = ∫_a^x f(t)dt be the accumulation function. By Part 1, G'(x) = f(x). By hypothesis, F'(x) = f(x) too, so F' = G' everywhere on (a,b). The MVT implies F − G is constant on [a,b]. Evaluating at x = a: F(a) − G(a) = F(a) − 0 = F(a). So G(x) = F(x) − F(a) for all x, and G(b) = F(b) − F(a).

The rigorous treatment clarifies exactly which hypotheses each part requires and why. Part 2 only needs f to be Riemann integrable (not continuous) and F to be a continuous antiderivative — strictly weaker than Part 1's continuity hypothesis for f. Counterexamples exist for both parts when hypotheses are violated: without continuity in Part 1, the accumulation function can fail to be differentiable at specific points; without integrability in Part 2, the antiderivative evaluation formula breaks down. The theorem doesn't just assert that differentiation and integration undo each other — it precisely characterizes the conditions under which they do, which is why the rigorous version is more powerful than the informal version you may have seen in a first calculus course.

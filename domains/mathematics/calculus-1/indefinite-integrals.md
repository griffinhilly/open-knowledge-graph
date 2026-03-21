---
id: indefinite-integrals
title: Indefinite Integrals
domain: mathematics
course: calculus-1
prerequisites:
  - id: antiderivatives
    type: hard
builds-toward:
  - basic-integration-rules
  - fundamental-theorem-of-calculus-part-2
tags: [integration, indefinite, notation]
stage: formal-systems
status: validated
---

# Indefinite Integrals

## Core Idea
The indefinite integral of f(x), written as the integral of f(x) dx, represents the family of all antiderivatives of f(x): F(x) + C. The integral sign, the integrand f(x), the differential dx, and the constant C are the key components of the notation. The indefinite integral is not a number but a family of functions. It provides the notation framework for all integration.

## How It's Best Learned
Connect the notation to antiderivatives: the integral of f(x) dx = F(x) + C means F'(x) = f(x). Practice computing basic indefinite integrals using known antiderivative rules. Verify by differentiating the result.

## Common Misconceptions
- Omitting the dx (it indicates the variable of integration and is essential for substitution).
- Forgetting +C.
- Confusing indefinite integrals (functions) with definite integrals (numbers).

## Questions

```yaml
- question: "A student computes ∫6x² dx = 2x³ and considers the problem finished. What is wrong with this answer?"
  type: multiple-choice
  options:
    - "Nothing — 2x³ is the correct and complete antiderivative of 6x²"
    - "The constant of integration +C is missing; without it, only one antiderivative is named instead of the entire family"
    - "The dx should appear in the answer alongside the result"
    - "The integral sign should be retained in the answer to show the operation is ongoing"
  answer: 1
  explanation: "Differentiation destroys any constant: (F(x) + C)' = F'(x) for any constant C. This means if F'(x) = f(x), then (F(x) + C)' = f(x) as well, for every value of C. The family 2x³ + C represents ALL antiderivatives of 6x². Writing just 2x³ implicitly claims there is only one antiderivative, which is false. Omitting +C is an incomplete answer, not merely a notational preference."

- question: "What is the key difference between the indefinite integral ∫f(x) dx and the definite integral ∫ₐᵇ f(x) dx?"
  type: multiple-choice
  options:
    - "Both produce functions of x, but the definite integral restricts the domain to [a, b]"
    - "The indefinite integral produces a family of functions; the definite integral produces a specific number"
    - "They produce the same result — the definite integral just adds evaluation at the bounds"
    - "The indefinite integral includes +C while the definite integral does not, but otherwise they are equivalent objects"
  answer: 1
  explanation: "The indefinite integral ∫f(x) dx = F(x) + C is a function (or family of functions). The definite integral ∫ₐᵇ f(x) dx = F(b) − F(a) is a number — the net signed area under f between a and b. Option D is the most tempting wrong answer: while it's true that the +C cancels in F(b) − F(a), the objects themselves are fundamentally different in kind (function vs. number), not merely differing by a constant."

- question: "The dx in ∫f(x) dx is optional notation that can be omitted without affecting the mathematical meaning."
  type: true-false
  answer: false
  explanation: "The dx identifies the variable of integration — essential when the integrand involves multiple variables, and critical when performing substitution. In u-substitution, the differential itself transforms: if u = g(x), then du = g'(x) dx, and the dx in the original integral becomes part of the substitution. Omitting dx makes this transformation impossible to execute. It is a structural part of the notation, not decorative."

- question: "The indefinite integral of a function f(x) represents the family of all functions that differentiate to f(x)."
  type: true-false
  answer: true
  explanation: "This is the definition. If F'(x) = f(x), then every function of the form F(x) + C (for any constant C) also differentiates to f(x). The indefinite integral names this entire family. The +C encodes the fact that constants vanish under differentiation, so the antiderivative is not unique — it is determined only up to an additive constant."

- question: "How do you verify that an indefinite integral is correct, and why does this method always work?"
  type: short-answer
  answer: "Differentiate the result and check whether you recover the original integrand. If ∫f(x) dx = F(x) + C, compute d/dx[F(x) + C] and confirm it equals f(x). This always works because integration and differentiation are inverse operations — the derivative of an antiderivative of f must return f. The +C disappears in differentiation (the derivative of any constant is zero), so it doesn't affect the check."
  explanation: "This verification strategy is available for every indefinite integral and should become automatic. If d/dx[your answer] ≠ f(x), the integral is wrong. The method works because the Fundamental Theorem of Calculus guarantees that differentiation undoes integration: d/dx ∫f(x) dx = f(x). The check exploits this inverse relationship directly."
```

## Explainer

You already know what an antiderivative is: a function F is an antiderivative of f if F'(x) = f(x). The indefinite integral is simply a notation for "give me all the antiderivatives of f." Writing ∫f(x) dx = F(x) + C is a compact statement: F is one antiderivative of f, and every other antiderivative differs from F by at most a constant C. The "indefinite" in the name signals that the answer is not a specific number — it is a whole family of functions, differing from each other by vertical shifts.

The notation has four components, each meaningful. The **integral sign** ∫ is an elongated S, originally standing for "sum" — it hints at the connection to Riemann sums that you'll formalize with the Fundamental Theorem. The **integrand** f(x) is the function you're integrating. The **differential** dx identifies the variable of integration; it tells you which variable is "moving" and becomes critical when you perform substitution, where the differential itself changes. The **constant of integration** +C encodes the fact that differentiation destroys constant terms, so any constant could have been present in the original function. Omitting C gives an incomplete answer — you've named one antiderivative instead of the whole family.

The way to verify an indefinite integral is always to differentiate the answer. If ∫3x² dx = x³ + C, check: d/dx(x³ + C) = 3x² + 0 = 3x². The derivative recovers the integrand, confirming the integral is correct. This is the inverse relationship between differentiation and integration, and it is the central fact of calculus. You can always check your work this way: differentiate the result and see if you get back what you started with.

The most important distinction to carry forward is between indefinite and definite integrals. An indefinite integral is a **function** (or family of functions). A definite integral ∫ₐᵇ f(x) dx is a **number** — the net area under f between x = a and x = b. The Fundamental Theorem of Calculus, which you'll encounter next, is precisely the bridge connecting these two: it says you can evaluate the definite integral using an antiderivative. But for now, practice the notation and the basic antiderivative rules until the +C and the dx feel like natural parts of the language rather than afterthoughts to remember.

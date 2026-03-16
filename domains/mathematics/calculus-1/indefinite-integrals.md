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

## Explainer

You already know what an antiderivative is: a function F is an antiderivative of f if F'(x) = f(x). The indefinite integral is simply a notation for "give me all the antiderivatives of f." Writing ∫f(x) dx = F(x) + C is a compact statement: F is one antiderivative of f, and every other antiderivative differs from F by at most a constant C. The "indefinite" in the name signals that the answer is not a specific number — it is a whole family of functions, differing from each other by vertical shifts.

The notation has four components, each meaningful. The **integral sign** ∫ is an elongated S, originally standing for "sum" — it hints at the connection to Riemann sums that you'll formalize with the Fundamental Theorem. The **integrand** f(x) is the function you're integrating. The **differential** dx identifies the variable of integration; it tells you which variable is "moving" and becomes critical when you perform substitution, where the differential itself changes. The **constant of integration** +C encodes the fact that differentiation destroys constant terms, so any constant could have been present in the original function. Omitting C gives an incomplete answer — you've named one antiderivative instead of the whole family.

The way to verify an indefinite integral is always to differentiate the answer. If ∫3x² dx = x³ + C, check: d/dx(x³ + C) = 3x² + 0 = 3x². The derivative recovers the integrand, confirming the integral is correct. This is the inverse relationship between differentiation and integration, and it is the central fact of calculus. You can always check your work this way: differentiate the result and see if you get back what you started with.

The most important distinction to carry forward is between indefinite and definite integrals. An indefinite integral is a **function** (or family of functions). A definite integral ∫ₐᵇ f(x) dx is a **number** — the net area under f between x = a and x = b. The Fundamental Theorem of Calculus, which you'll encounter next, is precisely the bridge connecting these two: it says you can evaluate the definite integral using an antiderivative. But for now, practice the notation and the basic antiderivative rules until the +C and the dx feel like natural parts of the language rather than afterthoughts to remember.

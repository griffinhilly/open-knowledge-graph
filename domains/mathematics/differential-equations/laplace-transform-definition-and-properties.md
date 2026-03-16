---
id: laplace-transform-definition-and-properties
title: 'Laplace Transform: Definition and Properties'
domain: mathematics
course: differential-equations
prerequisites:
- id: integration-by-parts
  type: hard
- id: improper-integrals-convergence
  type: hard
builds-toward:
- common-laplace-transforms
- inverse-laplace-transform
- laplace-transform-of-derivatives
tags:
- laplace-transform
- integral-transform
- definition
stage: formal-systems
status: draft
---

# Laplace Transform: Definition and Properties

## Core Idea
The Laplace transform of f(t) is F(s) = ∫₀^∞ e^{-st}·f(t) dt (for Re(s) > some threshold). It converts ODEs in the t-domain to algebraic equations in the s-domain, simplifying IVP solution. Key properties: linearity, shifting, scaling, and the derivative rule L{f'} = s·F(s) - f(0).

## How It's Best Learned
Compute Laplace transforms directly from the definition for simple functions like e^{at}, sin(bt), cos(bt). Use property tables to extend to more complex functions.

## Common Misconceptions
- Confusing the Laplace transform with Fourier transform; Laplace includes e^{-st} decay ensuring convergence for larger class of functions. - Forgetting the lower limit is 0, not -∞. - Not paying attention to convergence regions (s > σ, the abscissa of convergence).

## Explainer

The Laplace transform is an **integral transform**: it takes a function of time t and produces a function of a new variable s. The definition is F(s) = ∫₀^∞ e^{−st} f(t) dt. This integral is improper — it runs to infinity — and your prerequisite study of improper integrals tells you it converges only when s is large enough that the decaying exponential e^{−st} damps out any growth in f(t). For most functions of interest, convergence holds for all s greater than some threshold, called the **abscissa of convergence**.

Why would anyone define such a thing? The motivation becomes clear when you differentiate. If you apply the Laplace transform to f'(t) and integrate by parts (your other prerequisite), you get: L{f'(t)} = s·F(s) − f(0). This is the key property. A derivative in the t-domain becomes **multiplication by s** in the s-domain, adjusted by the initial condition f(0). Second derivatives give s²F(s) − sf(0) − f'(0). Higher derivatives give higher powers of s. The practical consequence: a differential equation in t — which involves derivatives — becomes an **algebraic equation** in s, which involves only multiplication. Algebra is easier to solve than calculus.

The transform is **linear**: L{af + bg} = aL{f} + bL{g}. This means it handles the superposition principle naturally, just as the differential equations you've studied are linear. There are also **shifting properties**: multiplying f(t) by e^{at} shifts F(s) to F(s−a), and shifting the input f(t−c)u(t−c) by c units multiplies F(s) by e^{−cs}. These shifting rules let you handle non-zero initial conditions and piecewise-defined forcing functions systematically, which were difficult to handle with direct integration methods.

The full solve-by-Laplace strategy has three steps: (1) transform both sides of the ODE, turning it into an algebraic equation in F(s); (2) solve for F(s) algebraically; (3) **invert** the transform to recover the solution f(t). Step 3 relies on a table of known transforms, partial fraction decomposition to match table entries, and the inverse Laplace transform — topics you will build in the next topics. But the key conceptual move is already visible in the definition and the derivative rule: by encoding initial conditions directly into F(s) at the moment of transformation, you never have to impose initial conditions separately at the end.

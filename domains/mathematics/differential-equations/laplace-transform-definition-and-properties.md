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
status: validated
---

# Laplace Transform: Definition and Properties

## Core Idea
The Laplace transform of f(t) is F(s) = ∫₀^∞ e^{-st}·f(t) dt (for Re(s) > some threshold). It converts ODEs in the t-domain to algebraic equations in the s-domain, simplifying IVP solution. Key properties: linearity, shifting, scaling, and the derivative rule L{f'} = s·F(s) - f(0).

## How It's Best Learned
Compute Laplace transforms directly from the definition for simple functions like e^{at}, sin(bt), cos(bt). Use property tables to extend to more complex functions.

## Common Misconceptions
- Confusing the Laplace transform with Fourier transform; Laplace includes e^{-st} decay ensuring convergence for larger class of functions. - Forgetting the lower limit is 0, not -∞. - Not paying attention to convergence regions (s > σ, the abscissa of convergence).

## Questions

```yaml
- question: "You apply the Laplace transform to f''(t) + 3f'(t) + 2f(t) = 0 with initial conditions f(0) = 1, f'(0) = 0. What does the transformed equation look like?"
  type: multiple-choice
  options:
    - "A simpler differential equation with fewer derivative terms"
    - "An algebraic equation (s² + 3s + 2)F(s) = s + 3, solvable for F(s) by ordinary algebra"
    - "An integral equation involving ∫F(s) ds"
    - "The same equation with t replaced by s throughout"
  answer: 1
  explanation: "Applying L{f''} = s²F(s) − sf(0) − f'(0) and L{f'} = sF(s) − f(0) gives (s²F(s) − s) + 3(sF(s) − 1) + 2F(s) = 0, which simplifies to (s² + 3s + 2)F(s) = s + 3. This is a purely algebraic equation in F(s). Initial conditions are absorbed automatically during the transform step. Calculus (differentiation) has become algebra (multiplication by powers of s) — that is the transform's central payoff."

- question: "A student says: 'The Laplace and Fourier transforms do the same job — I can use whichever I prefer when solving an ODE with initial conditions.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The Fourier transform only works on periodic functions"
    - "The Laplace transform uses a one-sided integral from 0 to ∞, naturally encoding initial conditions at t = 0; the Fourier transform is two-sided and does not"
    - "Both transforms work, but the Fourier version always produces more complicated algebra"
    - "The Laplace transform requires convergence conditions that the Fourier transform avoids"
  answer: 1
  explanation: "The Laplace transform integrates from 0 to ∞. The lower limit of 0 is the feature — not a limitation — that makes initial conditions at t = 0 appear naturally in the derivative rule as f(0), f'(0), etc. The Fourier transform integrates from −∞ to ∞, ignores initial conditions, and assumes the function exists for all time. For initial value problems, the one-sided nature of the Laplace transform is what makes the method clean."

- question: "When solving an ODE using the Laplace transform, initial conditions are encoded into the transformed equation automatically during the transform step and do not need to be applied separately at the end."
  type: true-false
  answer: true
  explanation: "True. The derivative rule L{f'} = sF(s) − f(0) incorporates f(0) directly. L{f''} = s²F(s) − sf(0) − f'(0) incorporates both f(0) and f'(0). By the time you write down the algebraic equation for F(s), all initial conditions are already embedded. This contrasts with classical methods (undetermined coefficients, variation of parameters) where you find a general solution first and impose initial conditions as a separate step at the end."

- question: "The Laplace transform is less efficient than direct methods for solving ODEs because computing the integral F(s) = ∫₀^∞ e^{−st}f(t) dt from scratch is harder than differentiating."
  type: true-false
  answer: false
  explanation: "False. The point is not to compute F(s) from scratch each time — it is to use a pre-built table of known transforms and apply algebraic manipulations. Once standard transforms (for e^{at}, sin(bt), t^n, etc.) are tabulated, any reasonable ODE is solved by table lookup, algebraic manipulation, and partial fractions. The transform turns a calculus problem into an algebra problem, which is far more routine, especially for higher-order equations or non-zero initial conditions."

- question: "What is the key conceptual step that makes the Laplace transform useful for solving initial value problems, and why is this different from simply integrating both sides of the ODE?"
  type: short-answer
  answer: "The key step is the derivative rule: L{f'(t)} = sF(s) − f(0). Differentiation in the t-domain becomes multiplication by s in the s-domain, with the initial condition subtracted. This converts a differential equation — which requires finding an unknown function — into an algebraic equation for F(s), solvable by arithmetic. Simply integrating both sides of an ODE does not achieve this: integration introduces new unknowns and does not separate the function from its derivatives in a useful way."
  explanation: "The transform exploits a structural coincidence: the operation of differentiation maps to multiplication under the Laplace integral. This is analogous to how logarithms turn multiplication into addition — a domain change that converts a harder operation into an easier one. The extra benefit for IVPs is that initial conditions appear naturally as constants in the algebraic equation, embedded at the moment of transformation rather than imposed at the end."
```

## Explainer

The Laplace transform is an **integral transform**: it takes a function of time t and produces a function of a new variable s. The definition is F(s) = ∫₀^∞ e^{−st} f(t) dt. This integral is improper — it runs to infinity — and your prerequisite study of improper integrals tells you it converges only when s is large enough that the decaying exponential e^{−st} damps out any growth in f(t). For most functions of interest, convergence holds for all s greater than some threshold, called the **abscissa of convergence**.

Why would anyone define such a thing? The motivation becomes clear when you differentiate. If you apply the Laplace transform to f'(t) and integrate by parts (your other prerequisite), you get: L{f'(t)} = s·F(s) − f(0). This is the key property. A derivative in the t-domain becomes **multiplication by s** in the s-domain, adjusted by the initial condition f(0). Second derivatives give s²F(s) − sf(0) − f'(0). Higher derivatives give higher powers of s. The practical consequence: a differential equation in t — which involves derivatives — becomes an **algebraic equation** in s, which involves only multiplication. Algebra is easier to solve than calculus.

The transform is **linear**: L{af + bg} = aL{f} + bL{g}. This means it handles the superposition principle naturally, just as the differential equations you've studied are linear. There are also **shifting properties**: multiplying f(t) by e^{at} shifts F(s) to F(s−a), and shifting the input f(t−c)u(t−c) by c units multiplies F(s) by e^{−cs}. These shifting rules let you handle non-zero initial conditions and piecewise-defined forcing functions systematically, which were difficult to handle with direct integration methods.

The full solve-by-Laplace strategy has three steps: (1) transform both sides of the ODE, turning it into an algebraic equation in F(s); (2) solve for F(s) algebraically; (3) **invert** the transform to recover the solution f(t). Step 3 relies on a table of known transforms, partial fraction decomposition to match table entries, and the inverse Laplace transform — topics you will build in the next topics. But the key conceptual move is already visible in the definition and the derivative rule: by encoding initial conditions directly into F(s) at the moment of transformation, you never have to impose initial conditions separately at the end.

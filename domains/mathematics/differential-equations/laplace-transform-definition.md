---
id: laplace-transform-definition
title: 'Laplace Transform: Definition and Properties'
domain: mathematics
course: differential-equations
prerequisites:
- id: improper-integrals-convergence
  type: hard
- id: exponential-functions-and-graphs
  type: hard
builds-toward:
- common-laplace-transforms
- inverse-laplace-transform
tags:
- laplace-transform
- integral-transform
- definition
stage: formal-systems
status: draft
---

# Laplace Transform: Definition and Properties

## Core Idea
The Laplace transform converts f(t) to F(s) = ∫₀^∞ e^(-st)f(t)dt, mapping time-domain differential equations to frequency-domain algebra. Key properties: linearity, the derivative rule L[f'(t)] = sF(s) - f(0), and shifting theorems. These transform initial conditions into the equation automatically, making Laplace transforms powerful for solving IVPs, especially with discontinuous forcing functions.

## Questions

```yaml
- question: "What does the Laplace transform derivative rule L{f'(t)} = sF(s) - f(0) accomplish that makes it powerful for solving initial value problems?"
  type: multiple-choice
  options:
    - "It eliminates the need to find F(s) by directly computing the answer in the time domain"
    - "It converts differentiation in t into multiplication by s, incorporating the initial condition algebraically so the ODE becomes an algebraic equation in s"
    - "It shows that all derivatives have the same Laplace transform, simplifying the computation"
    - "It converts an algebraic equation back into a differential equation so it can be solved by standard methods"
  answer: 1
  explanation: "The derivative rule's entire power is in this conversion: instead of solving a differential equation, you solve an algebraic equation in F(s). The initial condition f(0) appears as part of the algebra — you don't need to impose it as a separate step after solving. This is why Laplace transforms are especially valuable for IVPs: initial conditions are baked in automatically."

- question: "A student has the ODE f'' + 4f' + 3f = e^{-2t} with f(0) = 1, f'(0) = 0. After applying the Laplace transform, what kind of equation does she need to solve?"
  type: multiple-choice
  options:
    - "A new second-order ODE in F(s)"
    - "An algebraic equation in F(s) where the initial conditions already appear as constants"
    - "An integral equation that requires numerical methods"
    - "The same ODE, now written in the s-variable instead of t"
  answer: 1
  explanation: "Applying the transform converts every derivative into multiplication by s (with initial conditions as constants) and every function into its transform. The result is a purely algebraic equation in F(s) — no differential equation remains, just algebra. The initial conditions f(0)=1 and f'(0)=0 appear in the algebra automatically, without any separate step to impose them."

- question: "The Laplace transform L{e^{at}f(t)} = F(s - a) means that multiplying a function by an exponential in t shifts the argument of its transform in s."
  type: true-false
  answer: true
  explanation: "This is the s-shifting (first shifting) theorem. Multiplying f(t) by e^{at} in the time domain shifts the argument of F(s) from s to s - a in the frequency domain. This is useful for handling forcing functions with exponential growth or decay — you can use a known transform F(s) and simply replace s with s - a. The reverse direction (t-shifting) handles functions that switch on at some time c via the unit step function."

- question: "The Laplace transform method is most advantageous over direct methods when the forcing function in an ODE is a smooth, continuous function like a polynomial."
  type: true-false
  answer: false
  explanation: "The Laplace transform's greatest advantage over direct methods (variation of parameters, undetermined coefficients) appears with discontinuous forcing functions like step functions and impulses. For smooth forcing functions, direct methods often work just as easily. The t-shifting theorem and the Heaviside step function make the Laplace transform the natural tool when a forcing function 'switches on' at some time c — a case that is awkward and messy to handle any other way."

- question: "Explain why the Laplace transform converts a differential equation with initial conditions into an algebraic equation, and why this is more than just a computational shortcut."
  type: short-answer
  answer: "The derivative rule L{f'(t)} = sF(s) - f(0) replaces differentiation with multiplication by s (plus an algebraic term from the initial condition). A second derivative L{f''(t)} = s²F(s) - sf(0) - f'(0) reduces the order again. Applying the transform to a whole ODE converts every term into an algebraic expression in F(s), including the initial conditions, which appear as constants rather than side conditions. The result is an algebraic equation solvable for F(s), after which inversion recovers f(t)."
  explanation: "This is conceptually important because it changes the mathematical domain of the problem. Rather than searching for a function f(t) that satisfies a differential equation, you search for an algebraic function F(s), then recover f(t) via inverse transform. Initial conditions are absorbed into the algebra — they don't need to be imposed after finding a general solution, which eliminates an entire step and handles discontinuous forcing functions cleanly."
```

## Explainer

You've already studied improper integrals and know that ∫₀^∞ e^(−at) dt converges for a > 0. The **Laplace transform** wraps that convergence trick into a machine for solving differential equations. Given a function f(t) defined for t ≥ 0, the transform is ℒ{f}(s) = F(s) = ∫₀^∞ e^(−st) f(t) dt. The exponential e^(−st) acts as a damping factor: for large enough s, it forces the integral to converge even if f(t) grows (as long as f doesn't grow faster than some exponential). The output F(s) is a new function of the parameter s.

The whole point of the transform is the **derivative rule**: ℒ{f′(t)} = sF(s) − f(0). Differentiation in t becomes multiplication by s in the s-domain, with the initial condition f(0) appearing algebraically. For a second derivative: ℒ{f″(t)} = s²F(s) − sf(0) − f′(0). Every derivative lowers the problem by one degree. So a second-order ODE like f″ + 3f′ + 2f = g(t) with initial conditions f(0) = a, f′(0) = b transforms into a purely algebraic equation in F(s) and G(s) = ℒ{g}. Solve for F(s), then transform back. The initial conditions are absorbed automatically — no separate step needed to impose them.

**Linearity** ℒ{αf + βg} = αF + βG follows directly from linearity of integration and lets you handle sums of functions term by term. The **s-shifting theorem** says ℒ{e^(at)f(t)} = F(s − a): multiplying by an exponential in t shifts the argument in s. This handles forcing functions with exponential growth or decay. The **t-shifting theorem** ℒ{u_c(t)f(t − c)} = e^(−cs)F(s) handles functions that "switch on" at time t = c, where u_c is the unit step function. This is where the Laplace transform genuinely outperforms variation of parameters — discontinuous forcing functions like step functions and impulses are handled with almost no extra complexity.

The Laplace transform establishes convergence for Re(s) > some abscissa of convergence. For polynomials, ℒ{tⁿ} = n!/s^(n+1) for s > 0; for exponentials, ℒ{e^(at)} = 1/(s − a) for s > a. These basic transforms, combined with the linearity and shifting properties, form a table that covers almost every forcing function you'll encounter. The transform method's procedure is always the same: transform the ODE → solve the algebraic equation for F(s) → apply partial fractions and the table → invert back to f(t).

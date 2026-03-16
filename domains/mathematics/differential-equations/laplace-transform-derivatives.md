---
id: laplace-transform-derivatives
title: Laplace Transform of Derivatives and Initial Values
domain: mathematics
course: differential-equations
prerequisites:
- id: inverse-laplace-transform
  type: hard
- id: integration-by-parts
  type: hard
builds-toward:
- solving-ivps-laplace-transform
tags:
- derivatives
- initial-values
- transform-properties
stage: formal-systems
status: draft
---

# Laplace Transform of Derivatives and Initial Values

## Core Idea
The Laplace transform converts derivatives to multiplication: L[f'(t)] = sF(s) - f(0) and L[f''(t)] = s²F(s) - sf(0) - f'(0). This property directly incorporates initial conditions into the transformed equation, converting an IVP into an algebraic problem in F(s). This is the key advantage of Laplace transforms for solving initial value problems.

## Explainer

The Laplace transform turns a differential equation into an algebraic equation — that is its entire purpose. The derivative property is the mechanism that makes this happen. The key formula L[f'(t)] = sF(s) - f(0) says: differentiation in the time domain (which is hard, because it involves limits) becomes multiplication by s in the frequency domain (which is easy). And the initial condition f(0) enters automatically as a constant, baked into the transformed equation from the start.

The derivation uses integration by parts, which you already know. Starting from the definition: L[f'(t)] = ∫₀^∞ e^(-st) f'(t) dt. Apply integration by parts with u = e^(-st) and dv = f'(t)dt, giving du = -se^(-st)dt and v = f(t): the result is [e^(-st)f(t)]₀^∞ + s∫₀^∞ e^(-st)f(t) dt. The boundary term evaluates to 0 - f(0) = -f(0) (assuming f grows slowly enough that the t → ∞ term vanishes), and the remaining integral is sF(s). So L[f'(t)] = sF(s) - f(0). Applying the rule again to f''(t) treated as the derivative of f'(t): L[f''(t)] = sL[f'(t)] - f'(0) = s(sF(s) - f(0)) - f'(0) = s²F(s) - sf(0) - f'(0). The pattern extends naturally: each additional derivative introduces one more power of s and one more initial condition term.

To see the payoff, consider the IVP y'' + 3y' + 2y = 0 with y(0) = 1, y'(0) = 0. Applying the transform to each term: L[y''] + 3L[y'] + 2L[y] = 0 becomes (s²Y - s·1 - 0) + 3(sY - 1) + 2Y = 0. Collecting: Y(s)(s² + 3s + 2) = s + 3. Solve algebraically: Y(s) = (s + 3)/((s+1)(s+2)). Then partial fractions and the inverse Laplace transform recover y(t). The ODE has been completely replaced by algebra.

The key conceptual shift is that the initial conditions are no longer "applied after solving" — they are **embedded in the algebraic equation** from the moment you take the transform. This differs from methods like undetermined coefficients, where you find a general solution first and then solve for constants. This embedding makes the Laplace method particularly well-suited for piecewise-defined forcing functions and for systems where the forcing switches on at a specific time — situations where the initial conditions determine the entire solution trajectory in a natural, transparent way.

---
id: laplace-transform-of-derivatives
title: Laplace Transform of Derivatives and Integrals
domain: mathematics
course: differential-equations
prerequisites:
- id: laplace-transform-definition-and-properties
  type: hard
- id: integration-by-parts
  type: soft
builds-toward:
- solving-ivps-with-laplace-transforms
tags:
- laplace-transform
- derivative
- integral
stage: formal-systems
status: draft
---

# Laplace Transform of Derivatives and Integrals

## Core Idea
The key property L{f'(t)} = sF(s) - f(0) (and generalizations for higher derivatives) converts ODE initial value problems into algebraic problems. Similarly, L{∫₀ᵗ f(τ) dτ} = F(s)/s, converting integro-differential equations to algebraic form.

## Explainer

From your study of the Laplace transform definition, you know that L{f(t)} = ∫₀^∞ f(t)e^{−st} dt = F(s). The transform converts a function of time t into a function of the complex parameter s. What you now need is: what happens when you apply the Laplace transform to a *derivative*? The answer, derived from **integration by parts** (your soft prerequisite), is the formula that makes Laplace transforms the workhorse of ODE solving.

Apply integration by parts to L{f'(t)} = ∫₀^∞ f'(t)e^{−st} dt, with u = e^{−st} and dv = f'(t) dt. Then du = −se^{−st} dt and v = f(t), giving: [f(t)e^{−st}]₀^∞ + s∫₀^∞ f(t)e^{−st} dt. The boundary term evaluates to 0 − f(0) (assuming f(t) doesn't grow too fast), and the integral is exactly F(s). Result: **L{f'(t)} = sF(s) − f(0)**. Differentiation in the time domain becomes multiplication by s in the s-domain, with an initial condition subtracted. Applying this formula a second time to f''(t) = (f')'(t) gives **L{f''(t)} = s²F(s) − sf(0) − f'(0)**, and the pattern continues: each differentiation adds a factor of s and "peels off" one more initial condition.

This is the core reason Laplace transforms are powerful for initial value problems. An ODE like y'' + 3y' + 2y = eˡ with y(0) = 0, y'(0) = 1 transforms into (s²Y − s·0 − 1) + 3(sY − 0) + 2Y = 1/(s−1). The left side, after collecting terms, is (s² + 3s + 2)Y − 1. Solving for Y(s) is now purely **algebra**: Y(s) = (1 + 1/(s−1)) / (s² + 3s + 2). Partial fraction decomposition followed by inverse transform gives the solution. The differential equation — previously requiring the method of undetermined coefficients or variation of parameters — reduces to polynomial arithmetic.

The integration formula L{∫₀ᵗ f(τ) dτ} = F(s)/s is the symmetric partner. Just as differentiation multiplies by s, integration divides by s. This duality (s ↔ multiplication, 1/s ↔ integration) is a formal parallel to the derivative/integral relationship from calculus, but now entirely algebraic in the s-domain. Together these formulas make the Laplace transform a full **operational calculus**: the operations of differentiation and integration on functions become multiplication and division on their transforms, letting you manipulate ODEs as if they were ordinary equations.

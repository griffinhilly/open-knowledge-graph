---
id: complex-roots-oscillatory-solutions
title: Complex Roots and Oscillatory Solutions
domain: mathematics
course: differential-equations
prerequisites:
- id: characteristic-equation-method
  type: hard
- id: complex-numbers-intro
  type: hard
builds-toward:
- undetermined-coefficients
tags:
- complex-roots
- oscillation
- trigonometric
stage: formal-systems
status: draft
---

# Complex Roots and Oscillatory Solutions

## Core Idea
When the characteristic equation has complex conjugate roots r = α ± iβ, the general solution is y = e^(αx)(c₁cos(βx) + c₂sin(βx)). The real part α controls exponential growth or decay of the amplitude; β controls the oscillation frequency. This form naturally captures all oscillatory behavior in physical systems with damping, making complex roots essential for understanding vibrations.

## Explainer

From the characteristic equation method, you know that for a second-order linear ODE with constant coefficients, substituting y = e^(rx) reduces the differential equation to a polynomial in r. When the discriminant is negative, the characteristic equation has no real roots — instead it yields a **conjugate pair** r = α ± iβ. The formal solutions e^((α+iβ)x) and e^((α−iβ)x) involve complex exponentials, which seem abstract until you apply Euler's formula.

Euler's formula says e^(iβx) = cos(βx) + i·sin(βx). So e^((α+iβ)x) = e^(αx)·e^(iβx) = e^(αx)[cos(βx) + i·sin(βx)]. By taking the real and imaginary parts separately, you get two real-valued solutions: e^(αx)cos(βx) and e^(αx)sin(βx). These are linearly independent, so the general real solution is y = e^(αx)(c₁cos(βx) + c₂sin(βx)). This is the **real form** of the solution, derived from the complex exponentials but expressed entirely in terms of real functions.

The two parameters in the exponent do distinct physical jobs. The **real part α** determines whether the oscillation grows, decays, or stays constant. If α < 0, the factor e^(αx) decays exponentially — this is a **damped oscillation**, where amplitude shrinks over time, like a pendulum with friction. If α = 0, the amplitude is constant — **pure oscillation**, like an ideal spring. If α > 0, the amplitude grows exponentially — **unstable oscillation**, rare in passive physical systems but important in electronics. The **imaginary part β** sets the **angular frequency** of oscillation — how many complete cycles occur per unit of x (or time). Larger β means faster oscillation.

To find the arbitrary constants c₁ and c₂, you apply initial conditions, just as with real roots. Typically you're given y(0) and y'(0). Plugging in x = 0 gives y(0) = c₁ (since e^0 = 1 and sin(0) = 0, cos(0) = 1). Differentiating and plugging in x = 0 gives a second equation involving both c₁ and c₂. The result is a specific oscillatory trajectory through the initial state. This process — characteristic roots, Euler's formula, real form, initial conditions — is the complete recipe for solving any undamped or damped oscillatory system with constant coefficients, and it underlies the analysis of vibrations, circuits, and wave motion throughout physics and engineering.

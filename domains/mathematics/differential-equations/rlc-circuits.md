---
id: rlc-circuits
title: RLC Circuit Applications of Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: damping-and-resonance
  type: soft
builds-toward:
- laplace-transform-of-derivatives
tags:
- application
- electrical-circuits
- modeling
stage: advanced
status: draft
---

# RLC Circuit Applications of Differential Equations

## Core Idea
In an RLC circuit with resistance R, inductance L, and capacitance C, Kirchhoff's voltage law gives L·i'' + R·i' + i/C = V'(t), analogous to the damped spring-mass equation. Solving this ODE predicts transient currents and steady-state response to AC sources.

## How It's Best Learned
Derive the circuit equation from Kirchhoff's laws: V_R + V_L + V_C = V_applied. Identify analogies with mechanical systems: L↔m, R↔c, 1/C↔k. Solve for underdamped and overdamped responses.

## Common Misconceptions
- Confusing voltage across the capacitor (∫i dt / C) with current; the signs matter. - Forgetting the R·i term or misinterpreting its role as energy dissipation. - Not recognizing the mechanical-electrical duality, missing intuition from one domain to the other.

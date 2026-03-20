---
id: system-type-error-constant-steady-state
title: System Type and Steady-State Error Constants
domain: engineering
course: control-systems
prerequisites:
- id: steady-state-error-analysis
  type: hard
- id: transfer-functions-control
  type: hard
builds-toward:
- control-loop-design-via-bode-plots
tags:
- system-type
- error-constant
- zero-steady-state-error
- tracking
- regulation
stage: advanced
status: draft
---

# System Type and Steady-State Error Constants

## Core Idea
System type is the number of free integrators in the open-loop transfer function. Type 0 systems cannot track ramps with zero error; Type 1 can track ramps; Type 2 can track parabolas. Error constants Kₚ, Kᵥ, and Kₐ (position, velocity, acceleration) determine steady-state error to reference inputs.

## Explainer

You already know from steady-state error analysis that tracking a reference perfectly requires the closed-loop system to cancel the error signal. The key question is: what kind of reference can the system track with zero error? That question is answered entirely by counting the integrators in the open-loop transfer function — a number called the **system type**.

The intuition is that an integrator in the forward path is a memory element that can build up a correction to a persistent error. A **Type 0** system has no free integrators. When you command a constant position (step input), the system can settle to a finite but nonzero error determined by the **position error constant** Kₚ = lim(s→0) G(s). The steady-state error is e∞ = 1/(1+Kₚ). If you ask a Type 0 system to track a ramp, the error grows without bound — the system can't keep up because it has no inherent integration to generate a linearly growing output. A **Type 1** system has one integrator. Its Kₚ is infinite (zero step error), and its **velocity error constant** Kᵥ = lim(s→0) s·G(s) is finite. For a ramp input of slope R, the steady-state tracking error is e∞ = R/Kᵥ — a constant lag. A **Type 2** system adds another integrator: both Kₚ and Kᵥ are infinite, and only the **acceleration error constant** Kₐ = lim(s→0) s²·G(s) governs tracking of parabolic inputs.

The error constants are computed directly from the open-loop transfer function without closing the loop. Given G(s) = K·(s+z₁)(s+z₂)…/[sⁿ·(s+p₁)(s+p₂)…], the system type is n (the exponent on the bare s in the denominator). The error constants fall out by taking limits: Kₚ = lim G(s) as s→0, Kᵥ = lim s·G(s), Kₐ = lim s²·G(s). For a Type 1 system, Kₚ = ∞, Kᵥ is finite, and Kₐ = 0. The zero-error conditions for lower-order inputs are not coincidences — each integrator exactly cancels one power of s in the denominator of the error transfer function.

A practical implication: if your application demands zero position error under a constant disturbance or ramp command, the open-loop must contain at least one integrator. Many controllers (PID, PI) deliberately add an integrator via the integral term precisely to achieve Type 1 behavior. The tradeoff is that more integrators improve steady-state tracking but can destabilize the loop by adding phase lag — which connects directly to the Bode plot and phase margin analysis you will study next.

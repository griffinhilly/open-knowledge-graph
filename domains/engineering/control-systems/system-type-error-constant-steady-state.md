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
stage: expert
status: validated
---

# System Type and Steady-State Error Constants

## Core Idea
System type is the number of free integrators in the open-loop transfer function. Type 0 systems cannot track ramps with zero error; Type 1 can track ramps; Type 2 can track parabolas. Error constants Kₚ, Kᵥ, and Kₐ (position, velocity, acceleration) determine steady-state error to reference inputs.

## Questions

```yaml
- question: "A Type 1 closed-loop control system tracks a ramp input r(t) = 2t. The open-loop velocity error constant is Kᵥ = 4. What is the steady-state tracking error?"
  type: multiple-choice
  options:
    - "0 — Type 1 systems track all ramp inputs with zero steady-state error"
    - "0.5 — from e∞ = R/Kᵥ = 2/4"
    - "2 — the steady-state error equals the ramp slope"
    - "Infinite — Type 1 systems cannot track ramp inputs at all"
  answer: 1
  explanation: "Type 1 systems track ramps with a constant finite error, not zero error. The formula is e∞ = R/Kᵥ, where R is the ramp slope and Kᵥ = lim(s→0) s·G(s). Here, e∞ = 2/4 = 0.5. Zero ramp error requires Type 2. A Type 0 system would have infinite ramp error (grows without bound). The common misconception is that 'Type 1 tracks ramps' means zero error — it means bounded, finite error."

- question: "A designer adds an integral term to a proportional controller, converting a Type 0 system into a Type 1 system. What is the primary benefit of this change?"
  type: multiple-choice
  options:
    - "Faster transient response — the integrator speeds up rise time"
    - "Zero steady-state error for constant (step) reference inputs"
    - "Increased phase margin — the integral term improves stability"
    - "The ability to track parabolic inputs with finite error"
  answer: 1
  explanation: "Adding one integrator upgrades the system from Type 0 to Type 1. For a Type 0 system, the step error is e∞ = 1/(1+Kₚ) — finite and nonzero regardless of gain. The integrator makes Kₚ = ∞, reducing step error to zero. The tradeoff is that the integrator adds 90° of phase lag, which typically reduces phase margin and can destabilize the loop — the opposite of option C. Parabolic tracking with finite error requires Type 2 (two integrators)."

- question: "A Type 0 feedback control system will always achieve zero steady-state error for a constant step reference input if the open-loop gain is made sufficiently large."
  type: true-false
  answer: false
  explanation: "For a Type 0 system, the position error constant Kₚ = lim(s→0) G(s) is finite, giving e∞ = 1/(1+Kₚ). Increasing the gain increases Kₚ and reduces the error, but e∞ approaches zero only as Kₚ → ∞, which is never achieved with finite gain. No finite gain makes e∞ exactly zero for a Type 0 system. Zero step error requires a free integrator (Type 1 or higher), which makes Kₚ truly infinite."

- question: "Each free integrator added to the open-loop transfer function increases the system type by 1, allowing the system to track the next higher-order reference input (step, ramp, parabola) with zero steady-state error."
  type: true-false
  answer: true
  explanation: "This is the fundamental structure of system type theory. Type 0: zero integrators → finite step error. Type 1: one integrator → zero step error, finite ramp error. Type 2: two integrators → zero step error, zero ramp error, finite parabolic error. Each integrator cancels one power of s in the error transfer function's denominator, eliminating the error for one class of inputs. The cost is increasing phase lag with each added integrator, which must be managed through compensator design."

- question: "Why does a free integrator in the open-loop transfer function allow a closed-loop system to track a constant reference input with zero steady-state error, when a system with no integrators cannot?"
  type: short-answer
  answer: "An integrator in the forward path generates an output that grows without bound in response to any persistent nonzero input (its output is the integral of its input). If a constant reference tracking error persists, the integrator accumulates that error over time, increasing the control signal until the error is driven to zero. At steady state, the only way the integrator's output can be constant (not growing) is if its input — the error — is exactly zero. A proportional-only (Type 0) system has no such accumulation mechanism: it produces a control signal proportional to the current error and can settle at a nonzero steady-state error where the control signal exactly balances the plant's needs."
  explanation: "Mathematically, the integrator term 1/s in G(s) means the position error constant Kₚ = lim(s→0) G(s) → ∞, giving e∞ = 1/(1+Kₚ) → 0. The tradeoff is that the integrator adds 90° of phase lag at all frequencies, reducing phase margin and potentially causing instability — which is why integral terms in PID controllers must be paired with careful gain tuning."
```

## Explainer

You already know from steady-state error analysis that tracking a reference perfectly requires the closed-loop system to cancel the error signal. The key question is: what kind of reference can the system track with zero error? That question is answered entirely by counting the integrators in the open-loop transfer function — a number called the **system type**.

The intuition is that an integrator in the forward path is a memory element that can build up a correction to a persistent error. A **Type 0** system has no free integrators. When you command a constant position (step input), the system can settle to a finite but nonzero error determined by the **position error constant** Kₚ = lim(s→0) G(s). The steady-state error is e∞ = 1/(1+Kₚ). If you ask a Type 0 system to track a ramp, the error grows without bound — the system can't keep up because it has no inherent integration to generate a linearly growing output. A **Type 1** system has one integrator. Its Kₚ is infinite (zero step error), and its **velocity error constant** Kᵥ = lim(s→0) s·G(s) is finite. For a ramp input of slope R, the steady-state tracking error is e∞ = R/Kᵥ — a constant lag. A **Type 2** system adds another integrator: both Kₚ and Kᵥ are infinite, and only the **acceleration error constant** Kₐ = lim(s→0) s²·G(s) governs tracking of parabolic inputs.

The error constants are computed directly from the open-loop transfer function without closing the loop. Given G(s) = K·(s+z₁)(s+z₂)…/[sⁿ·(s+p₁)(s+p₂)…], the system type is n (the exponent on the bare s in the denominator). The error constants fall out by taking limits: Kₚ = lim G(s) as s→0, Kᵥ = lim s·G(s), Kₐ = lim s²·G(s). For a Type 1 system, Kₚ = ∞, Kᵥ is finite, and Kₐ = 0. The zero-error conditions for lower-order inputs are not coincidences — each integrator exactly cancels one power of s in the denominator of the error transfer function.

A practical implication: if your application demands zero position error under a constant disturbance or ramp command, the open-loop must contain at least one integrator. Many controllers (PID, PI) deliberately add an integrator via the integral term precisely to achieve Type 1 behavior. The tradeoff is that more integrators improve steady-state tracking but can destabilize the loop by adding phase lag — which connects directly to the Bode plot and phase margin analysis you will study next.

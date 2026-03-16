---
id: steady-state-error-analysis
title: Steady-State Error Analysis
domain: engineering
course: control-systems
prerequisites:
- id: block-diagram-algebra
  type: hard
- id: time-domain-response-first-order
  type: hard
- id: time-domain-response-second-order
  type: soft
builds-toward:
- pid-control
- root-locus-controller-design
tags:
- steady-state-error
- system-type
- error-constants
- position-error
- velocity-error
stage: advanced
status: validated
---
# Steady-State Error Analysis

## Core Idea
Steady-state error quantifies how closely a stable control system tracks its reference input after transients die out, determined by the number of free integrators in the open-loop forward path (system type). A Type 0 system has finite position constant Kp and nonzero steady-state error to a step; a Type 1 system (one integrator) tracks steps perfectly but has finite velocity constant Kv and error to a ramp; a Type 2 system tracks ramps perfectly but has finite acceleration constant Ka. Errors are given by ess = R/(1+Kp), ess = R/Kv, and ess = R/Ka respectively, derived using the final value theorem applied to E(s) = R(s)/(1 + G(s)).

## How It's Best Learned
Apply error constant formulas to example open-loop transfer functions with varying numbers of origin poles. Verify using the final value theorem on the closed-loop error transfer function — the two approaches must agree for a stable closed-loop system.

## Common Misconceptions
- Steady-state error formulas only apply to stable closed-loop systems; an unstable system does not have a meaningful steady-state.
- High gain reduces steady-state error but does not change system type — only adding integrators changes the fundamental error to polynomial inputs.
- Disturbance rejection steady-state error and reference tracking error have different expressions and should not be confused.

## Explainer

From your work with block-diagram algebra, you know how to compute a closed-loop transfer function by reducing feedback loops, and from time-domain analysis you know that a stable system eventually settles to a final value. Steady-state error analysis asks: once all the transients die away, how close does that final value get to the reference? The answer depends almost entirely on one structural feature of the open-loop path — how many pure integrators it contains. This count is the **system type**.

To see why integrators matter, think about what an integrator does in the s-domain: it contributes a factor of 1/s to G(s), which means infinite DC gain. The **closed-loop error signal** E(s) = R(s) / (1 + G(s)). When G(s) has no integrators (Type 0), G(0) is a finite number — call it Kp, the **position error constant**. The steady-state error to a unit step is then 1/(1+Kp): always nonzero unless Kp → ∞. But when G(s) contains one integrator, G(s) → ∞ as s → 0, which forces E(0) → 0. A Type 1 system tracks constant references perfectly, because the integrator continuously corrects any persistent error until it vanishes.

The pattern repeats for higher-order inputs. A ramp input R(s) = 1/s² demands that G(s) → ∞ faster than 1/s to achieve zero error — that requires at least two integrators. This is the **velocity error constant** Kv = lim[s→0] s·G(s); for a Type 1 system Kv is finite and the ramp error is 1/Kv. For a Type 2 system with two integrators, Kv → ∞ and ramp error is zero, but the system can still have finite error to a parabolic (acceleration) input, characterized by **Ka**. The three error constants Kp, Kv, Ka live in a precise hierarchy: each higher system type eliminates error to one more class of polynomial input.

The right tool for computing these errors is the **final value theorem**: the steady-state value of a signal f(t) equals lim[s→0] s·F(s), provided the closed-loop system is stable and the limit exists. Apply this to the error: ess = lim[s→0] s · E(s) = lim[s→0] s · R(s)/(1+G(s)). For a step R(s) = 1/s, this gives ess = 1/(1+lim G(s)) = 1/(1+Kp). Always verify stability first — the final value theorem gives a finite number even for unstable systems, but that number is meaningless.

One critical subtlety: high loop gain reduces steady-state error but does not change system type. You can drive Kp very large (making step error small) without adding any integrators, but you cannot make step error exactly zero without one. Conversely, adding an integrator changes the system's fundamental character — it now tracks steps perfectly regardless of gain, but requires careful stability analysis because each integrator contributes −90° of phase at all frequencies, eating into your phase margin. Steady-state error and stability are in tension, and the system type is the fulcrum between them.


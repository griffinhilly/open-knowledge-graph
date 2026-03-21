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

## Questions

```yaml
- question: "A control engineer wants zero steady-state error tracking a constant step input. She has a stable Type 0 system with gain K = 10. She increases gain to K = 10,000. What happens to the steady-state error?"
  type: multiple-choice
  options:
    - "It becomes exactly zero — very high gain forces the system to track perfectly"
    - "It decreases substantially but remains a small positive nonzero value"
    - "It stays unchanged because gain has no effect on steady-state error"
    - "It becomes negative because the system permanently overshoots the reference"
  answer: 1
  explanation: "For a Type 0 system, ess = R/(1+Kp) where Kp = lim[s→0] G(s), which equals K times other finite terms. Increasing K raises Kp, which reduces ess — but ess = R/(1+Kp) approaches zero only as Kp → ∞. At any finite K, Kp is finite and ess is a small but nonzero value. To achieve exactly zero steady-state error to a step, you need at least one integrator in the open-loop path (Type 1 system). No amount of finite gain can substitute for the structural property of having an integrator. High gain reduces error; system type determines whether error can reach zero."

- question: "A stable Type 1 system has velocity error constant Kv = 4 and is tracking a ramp input with slope R = 12 units/sec. What is the steady-state tracking error?"
  type: multiple-choice
  options:
    - "0, because a Type 1 system tracks all polynomial inputs without error"
    - "12 units, because the error equals the ramp slope for any Type 1 system"
    - "3 units, computed as ess = R/Kv = 12/4"
    - "Cannot be determined without knowing the closed-loop pole locations"
  answer: 2
  explanation: "A Type 1 system tracks step inputs with zero error (because one integrator makes G(0) → ∞), but it has finite steady-state error to a ramp input, given by ess = R/Kv. With R = 12 and Kv = 4, ess = 3. Option A is the critical misconception: Type 1 eliminates step error but NOT ramp error — you need Type 2 (two integrators) for zero ramp tracking error. The hierarchy is exact: each system type eliminates steady-state error to one more class of polynomial input, but not to the next."

- question: "A stable Type 2 control system will track both step and ramp reference inputs with zero steady-state error."
  type: true-false
  answer: true
  explanation: "A Type 2 system has two integrators in the open-loop forward path. Each integrator contributes a factor of 1/s to G(s), and together they make G(s) → ∞ faster than s² as s → 0. Applying the final value theorem to E(s) = R(s)/(1+G(s)) for both a step (R(s) = 1/s) and a ramp (R(s) = 1/s²) yields ess = 0 in both cases. However, two integrators contribute −180° of cumulative phase lag, making stability analysis critical — zero steady-state error is achieved at the cost of substantially reduced phase margin."

- question: "Adding an integrator to the open-loop forward path increases system type and reduces steady-state error without affecting the system's stability."
  type: true-false
  answer: false
  explanation: "Each integrator contributes −90° of phase lag at all frequencies, directly eroding the phase margin that measures stability robustness. A system with 60° of phase margin may become marginally stable or oscillatory after adding an integrator without compensating for the phase loss. This is the fundamental tension in control design: integrators reduce steady-state error but threaten stability. This is precisely why PID controllers include a derivative term — to add phase lead that compensates for the phase lag introduced by the integral term."

- question: "Explain why system type — the number of integrators in the open-loop path — rather than loop gain determines whether a control system can achieve exactly zero steady-state error to a given class of input."
  type: short-answer
  answer: "System type determines the structural ability to eliminate steady-state error because each integrator contributes a factor of 1/s to G(s), making G(s) → ∞ as s → 0. The closed-loop steady-state error is ess = lim[s→0] s·R(s)/(1+G(s)). For this limit to reach zero, G(0) must be infinite — and only an integrator (a pole at the origin) achieves that. Loop gain K scales G(s) by a finite constant: it can make G(0) very large for a Type 0 system, making ess very small, but ess = R/(1+K·finite) never reaches exactly zero for finite K. An integrator makes the denominator literally infinite at DC, forcing ess = 0. You cannot substitute quantity of gain for the qualitative structural property of having a pole at the origin."
  explanation: "This distinction between 'reduces error' and 'eliminates error' is the insight that separates genuine understanding from surface familiarity with the formulas. Students who confuse high gain with system type will make design errors — thinking they've solved a tracking problem with gain when only an integrator can actually solve it."
```

## Explainer

From your work with block-diagram algebra, you know how to compute a closed-loop transfer function by reducing feedback loops, and from time-domain analysis you know that a stable system eventually settles to a final value. Steady-state error analysis asks: once all the transients die away, how close does that final value get to the reference? The answer depends almost entirely on one structural feature of the open-loop path — how many pure integrators it contains. This count is the **system type**.

To see why integrators matter, think about what an integrator does in the s-domain: it contributes a factor of 1/s to G(s), which means infinite DC gain. The **closed-loop error signal** E(s) = R(s) / (1 + G(s)). When G(s) has no integrators (Type 0), G(0) is a finite number — call it Kp, the **position error constant**. The steady-state error to a unit step is then 1/(1+Kp): always nonzero unless Kp → ∞. But when G(s) contains one integrator, G(s) → ∞ as s → 0, which forces E(0) → 0. A Type 1 system tracks constant references perfectly, because the integrator continuously corrects any persistent error until it vanishes.

The pattern repeats for higher-order inputs. A ramp input R(s) = 1/s² demands that G(s) → ∞ faster than 1/s to achieve zero error — that requires at least two integrators. This is the **velocity error constant** Kv = lim[s→0] s·G(s); for a Type 1 system Kv is finite and the ramp error is 1/Kv. For a Type 2 system with two integrators, Kv → ∞ and ramp error is zero, but the system can still have finite error to a parabolic (acceleration) input, characterized by **Ka**. The three error constants Kp, Kv, Ka live in a precise hierarchy: each higher system type eliminates error to one more class of polynomial input.

The right tool for computing these errors is the **final value theorem**: the steady-state value of a signal f(t) equals lim[s→0] s·F(s), provided the closed-loop system is stable and the limit exists. Apply this to the error: ess = lim[s→0] s · E(s) = lim[s→0] s · R(s)/(1+G(s)). For a step R(s) = 1/s, this gives ess = 1/(1+lim G(s)) = 1/(1+Kp). Always verify stability first — the final value theorem gives a finite number even for unstable systems, but that number is meaningless.

One critical subtlety: high loop gain reduces steady-state error but does not change system type. You can drive Kp very large (making step error small) without adding any integrators, but you cannot make step error exactly zero without one. Conversely, adding an integrator changes the system's fundamental character — it now tracks steps perfectly regardless of gain, but requires careful stability analysis because each integrator contributes −90° of phase at all frequencies, eating into your phase margin. Steady-state error and stability are in tension, and the system type is the fulcrum between them.


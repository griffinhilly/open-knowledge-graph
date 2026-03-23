---
id: jet-impact-force-momentum-buckets
title: Jet Impact Force and Momentum Analysis
domain: engineering
course: fluid-mechanics
prerequisites:
- id: control-volume-momentum
  type: hard
- id: bernoullis-equation
  type: soft
tags:
- momentum
- jet
- force
stage: formal-systems
status: validated
---

# Jet Impact Force and Momentum Analysis

## Core Idea
The momentum equation applied to a control volume surrounding an impacting jet yields the force on a surface: F = ṁ(V_exit - V_inlet) = ρQ(V_exit - V_inlet). When a jet deflects by 180° on a flat plate, the force is F = 2ρQV; when deflected by θ, F = ρQV(1 - cosθ). This principle governs Pelton wheel bucket design, rocket control systems, and hydraulic actuators.

## Questions

```yaml
- question: "A jet of water strikes a flat plate perpendicularly, exerting force F on the plate. The plate is replaced by a curved bucket that deflects the same jet exactly 180°. With identical jet velocity and flow rate, the force on the bucket is:"
  type: multiple-choice
  options:
    - "The same force F — mass flow rate and inlet velocity are unchanged"
    - "Half of F — only the component of velocity parallel to the jet axis contributes"
    - "Twice F — the jet momentum completely reverses, doubling the total change in momentum"
    - "Four times F — force depends on velocity squared, and reversing velocity is equivalent to doubling it"
  answer: 2
  explanation: "For a flat plate perpendicular to the jet, the flow exits sideways with zero x-momentum, so the force equals the incoming momentum flux: F = ṁV = ρAV². For a 180° deflecting bucket, the jet exits in the reverse direction with x-momentum −ṁV, giving a total momentum change of 2ṁV and force 2ρAV² — exactly twice as large. The general formula is F = ρAV²(1 − cosθ), which gives 2ρAV² at θ = 180°. Option D confuses the squaring from the momentum flux formula (ρAV²) with what changes when deflection angle changes."

- question: "A Pelton wheel bucket moves at speed u = 10 m/s and intercepts a water jet with absolute velocity V = 30 m/s. What velocity governs the momentum exchange between the jet and the bucket?"
  type: multiple-choice
  options:
    - "V = 30 m/s, the absolute jet velocity, because momentum is always measured in a fixed frame"
    - "V − u = 20 m/s, the relative jet velocity, because the bucket only intercepts momentum not already matched by its own motion"
    - "V + u = 40 m/s, the sum of both velocities, because the bucket moves toward the oncoming jet"
    - "u = 10 m/s, the bucket velocity, because power equals force times velocity and only bucket speed matters for power"
  answer: 1
  explanation: "When a surface moves, the momentum exchange depends on the relative velocity between the jet and the surface. The bucket receives fluid at relative velocity (V − u) and must redirect it. Substituting into the force formula: F = ρA(V − u)²(1 − cosθ). When u = 0 (stationary), the full jet velocity applies. When u = V (bucket moving at jet speed), the relative velocity is zero and no force is exerted — the jet just touches the bucket without exchanging momentum. Only the relative motion drives momentum transfer, just as with any impact problem in classical mechanics."

- question: "For a curved vane deflecting a jet by angle θ, the force on the vane increases monotonically as θ increases from 0° to 180°, reaching its maximum when the jet is fully reversed."
  type: true-false
  answer: true
  explanation: "The force formula F = ρQV(1 − cosθ) confirms this directly. At θ = 0° (no deflection), cos 0° = 1 and F = 0 — the jet passes through unchanged. At θ = 90° (perpendicular deflection), cos 90° = 0 and F = ρQV. At θ = 180° (full reversal), cos 180° = −1 and F = 2ρQV — the maximum possible force. Since (1 − cosθ) is monotonically increasing on [0°, 180°], the force increases continuously with deflection angle."

- question: "A flat plate perpendicular to a water jet exerts the same force as a curved bucket that deflects the same jet by 180°, because in both cases the jet's kinetic energy is fully removed."
  type: true-false
  answer: false
  explanation: "The forces are not equal — the 180° bucket exerts twice the force of the flat plate. For the flat plate, the jet exits sideways with zero axial momentum, so the axial force equals ṁV. For the 180° bucket, the jet exits in the reverse direction with axial momentum −ṁV, so the total change in axial momentum is 2ṁV — double the force. Force depends on momentum change, not energy removal. (The flat plate also removes kinetic energy but does so by redirecting it sideways, not reversing it.)"

- question: "Why are Pelton wheel buckets designed to deflect the incoming water jet as close to 180° as possible, rather than using flat plates or smaller deflection angles?"
  type: short-answer
  answer: "The force exerted on a surface by a jet equals the rate of change of momentum of the fluid. For a flat plate (perpendicular impact), the jet exits sideways with zero axial momentum, so the force equals ṁV. For a 180° deflection, the jet reverses direction and the total axial momentum change is 2ṁV — twice as large. Maximum force means maximum torque on the wheel and maximum power extracted from the water. Pelton buckets approach hemispherical shapes to reverse the jet as completely as possible, with a slight opening to prevent the exiting water from striking the next bucket."
  explanation: "In practice, buckets are designed with a deflection angle slightly less than 180° (typically about 165°–170°) to prevent interference between the exiting flow and the next bucket in line. The small deviation from 180° causes only a small reduction in force (since cos 165° ≈ −0.97, giving F ≈ 1.97ρAV² instead of 2ρAV²), so the design target remains as close to full reversal as mechanically feasible."
```

## Explainer

A jet of water striking a surface is one of the cleanest applications of the control volume momentum equation you already know. Draw the control volume enclosing the region where the jet meets the surface. Continuity demands that whatever mass flow enters must exit (neglecting splashing). The force the jet exerts on the surface is then entirely determined by the change in momentum flux between inlet and outlet — you do not need to know the pressure or velocity anywhere inside the control volume.

For a **flat plate perpendicular to the jet**, the flow arrives with velocity V in the x-direction and exits sideways with zero x-momentum. Applying the x-momentum equation: F = ṁV_in - ṁV_out,x = ṁV - 0 = ρAV². The force on the plate equals the incoming momentum flux. Now consider a **curved vane that deflects the jet 180°** — a bucket that turns the flow back on itself. The exit velocity is −V (in the x-direction), so F = ṁV - ṁ(−V) = 2ṁV = 2ρAV². Doubling the deflection angle doubles the force. For an arbitrary deflection angle θ, the x-component of exit velocity is V·cosθ, giving F = ρAV²(1 − cosθ), which ranges from zero at θ = 0° (the jet passes straight through, unchanged) to 2ρAV² at θ = 180°.

This is exactly why **Pelton wheel buckets** are designed as hemispherical cups that turn the jet nearly 180°. Each bucket catches the jet and reverses its momentum, extracting the maximum possible force and therefore maximum work from the water. In practice the angle is slightly less than 180° to prevent the exiting water from interfering with the next bucket, but the design target is always as close to 180° as mechanically feasible.

When the vane is **moving** at velocity u (as on a real Pelton wheel or turbine blade), the analysis still applies but the relative velocity of the jet with respect to the vane determines the momentum exchange: the effective jet velocity becomes (V − u), so F = ρA(V−u)²(1 − cosθ). The power delivered is F·u = ρA(V−u)²(1−cosθ)·u, which reaches a maximum when u = V/3 for a flat plate (θ = 90°) or u = V/3 for the general case — an important result for turbomachinery optimization.

The key discipline in these problems is careful sign convention. Choose a positive x-direction, write V_exit as a signed vector component, and let the algebra work out the direction of the force. A negative result simply means the force acts in the direction opposite to your assumed positive. Once you can confidently set up the control volume, identify all momentum fluxes with correct signs, and apply continuity, jet impact problems become straightforward and satisfying — a direct application of Newton's second law to a practical engineering system.

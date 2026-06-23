---
id: flow-measurement-methods
title: 'Flow Measurement: Venturi, Orifice, and Pitot Tube'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: bernoullis-equation
  type: hard
- id: continuity-equation-fluid
  type: hard
- id: manometry-and-pressure-measurement
  type: soft
- id: pitot-tube-velocity-measurement
  type: soft
- id: differential-manometer-types
  type: soft
tags:
- venturi meter
- orifice plate
- Pitot tube
- flow rate measurement
- discharge coefficient
stage: expert
status: validated
---
# Flow Measurement: Venturi, Orifice, and Pitot Tube

## Core Idea
Flow meters exploit the Bernoulli-continuity relationship between pressure and velocity. The venturi meter uses a gradual contraction and expansion to minimize losses; flow rate Q = C_d·A₂·√(2ΔP/ρ(1−(A₂/A₁)²)). The orifice plate is simpler but causes higher pressure loss. The Pitot tube measures stagnation pressure and, combined with a static tap, yields local velocity: V = √(2(P_stag − P_static)/ρ). A discharge coefficient C_d corrects for real-fluid effects.

## How It's Best Learned
Compare all three devices: which has lowest cost, lowest pressure loss, highest accuracy? Calibrate a venturi or orifice by measuring flow with a weighing tank and plotting C_d vs. Re. Use a Pitot traverse to measure velocity profile across a duct and integrate to find Q.

## Common Misconceptions
- The Pitot tube measures stagnation pressure, not static pressure — the two pressure taps must be distinguished carefully.
- The theoretical (ideal) flow rate overestimates actual flow; C_d < 1 corrects for vena contracta and friction effects.
- Venturi and orifice meters measure volumetric flow rate indirectly through pressure difference, not directly.

## Questions

```yaml
- question: "An engineer places a Pitot tube at the centerline of a circular pipe and uses the measured pressure to compute V = √(2ΔP/ρ), then multiplies by the pipe cross-section area to get flow rate Q. What is the primary error in this procedure?"
  type: multiple-choice
  options:
    - "The Pitot tube formula requires the discharge coefficient C_d to be applied before computing velocity"
    - "The Pitot tube measures velocity at one point; because velocity varies across the cross-section (lower near the walls), a single centerline measurement overestimates the cross-sectional average velocity and thus overestimates flow rate"
    - "A Pitot tube measures static pressure, not stagnation pressure, so the formula V = √(2ΔP/ρ) is inapplicable"
    - "The Pitot tube is only valid in open channels; in pipes the static port is obstructed"
  answer: 1
  explanation: "A Pitot tube measures the local velocity at the specific point where it is positioned. In a pipe, velocity is highest at the centerline and falls to zero at the wall (no-slip condition). Using the centerline velocity as a proxy for average velocity overestimates Q. The correct approach is a Pitot traverse — measuring velocity at multiple radial positions across the cross-section and integrating the velocity profile to find the true average. The engineer should either perform the traverse or use a venturi/orifice meter that inherently measures total flow rate."

- question: "A venturi meter and an orifice plate are installed in the same pipeline with identical throat-to-pipe area ratios. For the same volumetric flow rate, how do their permanent pressure losses compare?"
  type: multiple-choice
  options:
    - "Both produce identical permanent pressure losses because they have the same area ratio and thus the same Bernoulli pressure drop"
    - "The venturi has far lower permanent pressure loss because its gradual expansion recovers most of the kinetic energy; the orifice plate's abrupt geometry creates large separation and permanent energy dissipation"
    - "The orifice plate has lower permanent pressure loss because its sharp edge reduces contact area with the fluid"
    - "The venturi has higher permanent pressure loss because the longer throat creates more wall friction"
  answer: 1
  explanation: "Both devices produce similar measured pressure drops (the differential ΔP used to compute flow rate). However, permanent pressure loss — energy that cannot be recovered — differs dramatically. The venturi's gradual expansion converts most of the kinetic energy at the throat back into pressure, so permanent loss is small (a few percent of ΔP). The orifice plate's abrupt geometry causes massive flow separation and turbulent dissipation downstream, so permanent loss is a large fraction of ΔP (about 60-80% for a typical orifice). This energy difference has real operating costs in large industrial pipelines."

- question: "A Pitot tube measures the static pressure of the flowing fluid at the point where it is inserted."
  type: true-false
  answer: false
  explanation: "A forward-facing Pitot tube brings the flow to rest (stagnates it) at its opening, measuring stagnation pressure P_stag = P_static + ½ρV². This is always greater than static pressure by the dynamic pressure ½ρV². Static pressure is measured separately through a port perpendicular to the flow, where no stagnation occurs. The velocity is extracted from the difference: V = √(2(P_stag − P_static)/ρ). Confusing the two pressure taps leads to a velocity reading of zero — one of the most common Pitot tube errors in practice."

- question: "The theoretical flow rate calculated from the ideal Bernoulli-continuity equation overestimates the actual flow through a venturi or orifice meter, which is why the discharge coefficient C_d is always less than 1."
  type: true-false
  answer: true
  explanation: "The ideal Bernoulli derivation assumes no viscous losses, a uniform velocity profile, and exact geometric areas. Real flows experience wall friction, non-uniform velocity profiles, and — in the case of the orifice — a vena contracta where the actual minimum flow area is smaller than the physical hole area. All of these effects reduce actual flow below the ideal prediction. The discharge coefficient C_d (typically 0.98 for well-designed venturis, 0.61 for orifices) is an empirical correction factor that brings the theoretical formula into agreement with measured flow rates."

- question: "Explain what stagnation pressure is and why a Pitot tube measures it rather than static pressure, then describe what additional measurement is needed to extract flow velocity."
  type: short-answer
  answer: "Stagnation pressure is the pressure that would be measured if the fluid were brought to rest isentropically — it equals static pressure plus dynamic pressure (½ρV²). A Pitot tube faces directly into the flow, so the moving fluid decelerates to zero velocity at the tube opening; all kinetic energy converts to pressure according to Bernoulli's equation, producing the stagnation pressure. To extract velocity, you also need static pressure, measured through a port oriented perpendicular to the flow where the fluid is not decelerated. The velocity follows from V = √(2(P_stag − P_static)/ρ), where the difference is the dynamic pressure."
  explanation: "The Pitot tube is essentially a kinetic-energy-to-pressure converter: it turns the invisible kinetic energy of the moving fluid into a measurable pressure surplus. The static port provides the baseline, and the difference gives the dynamic pressure. In a Pitot-static tube (the standard aircraft airspeed indicator), both pressures are measured by the same probe: the forward-facing hole for stagnation, and side holes for static. Without both measurements, you cannot separate the two contributions to stagnation pressure."
```

## Explainer

You already know Bernoulli's equation: along a streamline, pressure drops when velocity increases, and vice versa. You also know continuity: for an incompressible fluid in a pipe, A₁V₁ = A₂V₂, so a narrower section means higher velocity. Flow measurement devices exploit both of these principles simultaneously. The core idea is that you force the fluid through a constriction, which guarantees a velocity increase; that velocity increase produces a predictable pressure drop; and that pressure drop is easy to measure. From the measured pressure drop, you work backwards to find the velocity and then the volumetric flow rate.

The **venturi meter** is the most accurate version of this idea. It uses a smooth, gradual contraction to accelerate the flow to a throat, then a gradual expansion to recover most of the pressure. Because the geometry is smooth, viscous losses are minimal and the measured pressure difference between upstream and throat closely approximates the ideal Bernoulli prediction. The **orifice plate** does the same thing more cheaply — a plate with a hole is simply inserted into the pipe — but the abrupt geometry creates a **vena contracta** (the actual minimum flow area is smaller than the hole area) and significant permanent pressure loss. Both devices use the same working equation Q = C_d · A₂ · √(2ΔP / ρ(1−(A₂/A₁)²)), where the **discharge coefficient** C_d corrects the theoretical (ideal) answer for real-fluid effects. For a well-designed venturi, C_d ≈ 0.98; for an orifice plate, C_d ≈ 0.61.

The **Pitot tube** works differently: instead of measuring flow rate through a constriction, it measures the local velocity at a point by converting kinetic energy to pressure. A forward-facing tube traps the flow and brings it to rest — creating **stagnation pressure** P_stag = P_static + ½ρV². A separate static tap measures P_static through a port perpendicular to the flow, where the fluid is not decelerated. The velocity follows from the pressure difference: V = √(2(P_stag − P_static)/ρ). A Pitot tube measures velocity at one point, not average flow rate; to get total flow rate you need a Pitot traverse — measuring across the full cross-section and integrating the velocity profile.

The practical choice between devices hinges on cost, accuracy, and pressure loss. Venturi meters have low permanent pressure loss (important for energy efficiency in large pipelines) but are expensive to manufacture. Orifice plates are cheap and easy to replace, but waste energy through the large permanent pressure drop. Pitot tubes are ideal for large ducts and gas flows where inserting a venturi would be impractical. In all cases, the discharge coefficient must be determined — either from published correlations as a function of Reynolds number, or by direct calibration against a weighing tank or other primary standard.

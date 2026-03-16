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
tags:
- venturi meter
- orifice plate
- Pitot tube
- flow rate measurement
- discharge coefficient
stage: formal-systems
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

## Explainer

You already know Bernoulli's equation: along a streamline, pressure drops when velocity increases, and vice versa. You also know continuity: for an incompressible fluid in a pipe, A₁V₁ = A₂V₂, so a narrower section means higher velocity. Flow measurement devices exploit both of these principles simultaneously. The core idea is that you force the fluid through a constriction, which guarantees a velocity increase; that velocity increase produces a predictable pressure drop; and that pressure drop is easy to measure. From the measured pressure drop, you work backwards to find the velocity and then the volumetric flow rate.

The **venturi meter** is the most accurate version of this idea. It uses a smooth, gradual contraction to accelerate the flow to a throat, then a gradual expansion to recover most of the pressure. Because the geometry is smooth, viscous losses are minimal and the measured pressure difference between upstream and throat closely approximates the ideal Bernoulli prediction. The **orifice plate** does the same thing more cheaply — a plate with a hole is simply inserted into the pipe — but the abrupt geometry creates a **vena contracta** (the actual minimum flow area is smaller than the hole area) and significant permanent pressure loss. Both devices use the same working equation Q = C_d · A₂ · √(2ΔP / ρ(1−(A₂/A₁)²)), where the **discharge coefficient** C_d corrects the theoretical (ideal) answer for real-fluid effects. For a well-designed venturi, C_d ≈ 0.98; for an orifice plate, C_d ≈ 0.61.

The **Pitot tube** works differently: instead of measuring flow rate through a constriction, it measures the local velocity at a point by converting kinetic energy to pressure. A forward-facing tube traps the flow and brings it to rest — creating **stagnation pressure** P_stag = P_static + ½ρV². A separate static tap measures P_static through a port perpendicular to the flow, where the fluid is not decelerated. The velocity follows from the pressure difference: V = √(2(P_stag − P_static)/ρ). A Pitot tube measures velocity at one point, not average flow rate; to get total flow rate you need a Pitot traverse — measuring across the full cross-section and integrating the velocity profile.

The practical choice between devices hinges on cost, accuracy, and pressure loss. Venturi meters have low permanent pressure loss (important for energy efficiency in large pipelines) but are expensive to manufacture. Orifice plates are cheap and easy to replace, but waste energy through the large permanent pressure drop. Pitot tubes are ideal for large ducts and gas flows where inserting a venturi would be impractical. In all cases, the discharge coefficient must be determined — either from published correlations as a function of Reynolds number, or by direct calibration against a weighing tank or other primary standard.

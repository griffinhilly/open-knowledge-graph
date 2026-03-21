---
id: hagen-poiseuille-flow
title: Hagen-Poiseuille Flow
domain: engineering
course: fluid-mechanics
prerequisites:
- id: laminar-pipe-flow
  type: hard
- id: navier-stokes-equations
  type: soft
tags:
- Hagen-Poiseuille
- laminar pipe flow
- parabolic velocity profile
- pressure drop
- viscous flow
stage: advanced
status: draft
---
# Hagen-Poiseuille Flow

## Core Idea
Hagen-Poiseuille flow is the exact analytical solution for fully developed, steady, incompressible, laminar flow in a circular pipe. The Navier-Stokes equations reduce to a simple ODE when the flow is axisymmetric, unidirectional, and fully developed (∂u/∂x = 0 for the axial velocity profile shape). The resulting velocity profile is parabolic: u(r) = (ΔP/4μL)(R² − r²), with maximum velocity at the centerline equal to twice the mean velocity. The volumetric flow rate is Q = πR⁴ΔP/(8μL), showing the dramatic fourth-power dependence on radius — halving the pipe diameter requires 16 times the pressure drop for the same flow rate. This solution is valid only for Re_D < ~2100 and in the fully developed region downstream of the entrance length.

## How It's Best Learned
Derive the parabolic profile from the cylindrical Navier-Stokes equations step by step, applying no-slip and symmetry boundary conditions. Verify that the wall shear stress τ_w = 8μV_avg/D matches the Darcy friction factor f = 64/Re. Then solve practical problems: compute the pressure drop for oil flowing through a long capillary tube, or estimate the flow rate through a medical catheter given a pressure difference. Compare predictions against the Moody diagram in the laminar regime.

## Common Misconceptions
- The Q ∝ R⁴ relationship (Poiseuille's law) applies only to laminar flow. In turbulent flow, Q depends on R to a power closer to 2.5, mediated by the friction factor.
- Hagen-Poiseuille flow assumes the pipe is long enough for the flow to be fully developed. In short pipes or near inlets, the velocity profile is still developing and the pressure drop per unit length is higher.
- The parabolic profile means the fluid at the wall is stationary (no-slip) while the centerline fluid moves at twice the average velocity. This velocity non-uniformity is critical for understanding residence time distributions in chemical reactors and blood flow in arteries.

## Questions

```yaml
- question: "Atherosclerotic plaque reduces the effective radius of a coronary artery by 50%. Assuming laminar flow conditions hold, by what factor does flow resistance increase?"
  type: multiple-choice
  options:
    - "2× — resistance doubles because the cross-sectional area is halved"
    - "4× — resistance quadruples because area depends on radius squared"
    - "8× — resistance increases with the cube of radius reduction"
    - "16× — resistance increases by the fourth power of the radius ratio"
  answer: 3
  explanation: "From Q = πR⁴ΔP/(8μL), flow resistance (ΔP/Q) ∝ 1/R⁴. Reducing R by half means R⁴ decreases by (1/2)⁴ = 1/16, so resistance increases 16-fold. This is why a 50% stenosis is medically critical — the heart cannot compensate for a 16-fold increase in resistance. The R⁴ relationship governs pipe flow because both the available flow area and the velocity profile (shaped by the no-slip condition and viscous resistance) change with radius."

- question: "Water flows through a long straight pipe at Re = 800 (well within the laminar regime). If the pipe radius is doubled while keeping pressure drop ΔP, fluid viscosity μ, and pipe length L constant, by what factor does volumetric flow rate increase?"
  type: multiple-choice
  options:
    - "2× — flow rate is proportional to radius"
    - "4× — flow rate is proportional to cross-sectional area (R²)"
    - "8× — flow rate is proportional to R³"
    - "16× — flow rate is proportional to R⁴"
  answer: 3
  explanation: "Q = πR⁴ΔP/(8μL) shows Q ∝ R⁴ when ΔP, μ, and L are held constant. Doubling R gives Q increases by 2⁴ = 16. This fourth-power sensitivity makes Hagen-Poiseuille flow very responsive to small changes in pipe radius — the reason it dominates design considerations in microfluidics, biomedical devices, and any viscous-flow application where pipe geometry must be precisely controlled."

- question: "In fully developed Hagen-Poiseuille flow, the fluid velocity at the pipe centerline equals the average (mean) velocity across the entire cross-section."
  type: true-false
  answer: false
  explanation: "The parabolic velocity profile has its maximum at the centerline (r = 0): u_max = ΔPR²/(4μL). Integrating over the cross-section gives the mean velocity V_avg = u_max/2. The centerline velocity is exactly twice the mean velocity, not equal to it. This factor of two has practical consequences: in chemical reactors, the fastest fluid elements spend half as much time in the reactor as the average, leading to non-uniform conversion and residence time distributions."

- question: "The Hagen-Poiseuille equation accurately predicts pressure drop in the region immediately downstream of a pipe entrance, before the velocity profile has fully developed."
  type: true-false
  answer: false
  explanation: "The Hagen-Poiseuille solution assumes fully developed flow — the velocity profile shape is unchanged along the pipe length (∂u/∂x = 0). Near the pipe entrance, the flow transitions from a flat entry profile to the parabolic profile, and pressure drop per unit length is higher than the fully-developed prediction during this entrance region. The entrance length L_e ≈ 0.06 Re·D can extend many pipe diameters. Applying Hagen-Poiseuille to a short pipe or entrance region overestimates flow rate for a given pressure drop."

- question: "Why does volumetric flow rate in a pipe depend on the fourth power of radius rather than the second power (cross-sectional area), and what physical mechanism explains this?"
  type: short-answer
  answer: "The fourth-power dependence comes from two contributing R² factors. First, a larger radius provides more cross-sectional area for flow (∝ R²). Second, a larger radius means the parabolic velocity profile spans a wider range — the centerline (maximum) velocity increases with R² because viscous resistance over a longer radial distance is less, allowing faster fluid. Integrating this wider, faster parabolic profile over the larger cross-section gives Q ∝ R² × R² = R⁴."
  explanation: "This is why the R⁴ law is so dramatic in practice: a modest change in radius changes both how much fluid the pipe can hold and how fast that fluid moves, compounding the effect. In turbulent flow the relationship is weaker (closer to R^2.5) because turbulent mixing flattens the velocity profile, eliminating the velocity-amplification component of the R⁴ scaling."
```

## Explainer

From your study of laminar pipe flow and viscosity, you know that fluid near a pipe wall is held stationary by the no-slip condition while fluid near the center moves fastest. Viscosity resists the relative sliding between fluid layers, and the applied pressure drop along the pipe provides the driving force to overcome that resistance. Hagen-Poiseuille flow is what results when these two effects reach a precise, steady balance — it is one of the rare exact analytical solutions in fluid mechanics, valid under conditions strict enough to be enforced but common enough to be routinely useful.

The derivation reduces the cylindrical Navier-Stokes equations to a simple radial ODE by applying three conditions: the flow is axisymmetric (nothing varies with angular position), it is fully developed (the velocity profile shape does not change along the pipe length, so the axial velocity gradient ∂u/∂x = 0), and it is steady and incompressible. Applying no-slip at the wall (u = 0 at r = R) and symmetry at the centerline (du/dr = 0 at r = 0) yields the **parabolic velocity profile**: u(r) = (ΔP/4μL)(R² − r²). The profile is a paraboloid of revolution: zero at the wall, maximum at the centerline, with the centerline velocity equal to exactly twice the cross-sectional average velocity. Integrating over the pipe cross-section gives the Hagen-Poiseuille equation: Q = πR⁴ΔP/(8μL).

The **R⁴ dependence** is the most practically significant result. Double the pipe radius while keeping all else fixed, and flow rate increases 16-fold. Equivalently, pushing the same flow rate through a pipe half the diameter requires 16 times the pressure drop. This extreme sensitivity to radius governs a wide range of physical systems. In medicine: atherosclerotic plaque reducing an artery's radius by 50% increases flow resistance by a factor of 16 — the heart cannot compensate, and blood flow drops severely. In microfluidics: channels machined at 10 μm diameter instead of 20 μm require 16-fold higher driving pressure for the same throughput. In IV therapy: a catheter selected one French size smaller dramatically reduces maximum flow rate. The R⁴ law demands respect in any system where small geometric changes have large hydraulic consequences.

The solution is exact, but its assumptions must all hold. Re < ~2100 is required for laminar flow; above that, turbulence destroys the parabolic profile and the linear Q–ΔP relationship. The flow must be **fully developed**: near the pipe entrance, the velocity profile is still transitioning from the flat entry profile to the parabola, and the entrance length L_e ≈ 0.06 Re·D can be many pipe diameters long for high Reynolds number laminar flows. During this entrance region, pressure drop per unit length is higher than the fully-developed value, which matters for short pipes. The pipe must also be straight and circular; bends, non-circular cross-sections, and wall roughness all invalidate the solution. When these conditions hold — as they commonly do in viscous flow applications — Hagen-Poiseuille provides exact, reliable predictions without numerical approximation.

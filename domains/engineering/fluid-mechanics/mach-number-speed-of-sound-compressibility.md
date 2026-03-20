---
id: mach-number-speed-of-sound-compressibility
title: 'Mach Number and Speed of Sound: Compressibility Effects'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: compressible-flow-basics
  type: hard
- id: fluid-properties-and-continuum
  type: soft
builds-toward:
- isentropic-nozzle-flow-choked-conditions
- rayleigh-line-flow-stagnation-conditions
tags:
- mach
- compressibility
- sound
stage: advanced
status: draft
---

# Mach Number and Speed of Sound: Compressibility Effects

## Core Idea
The Mach number M = V/a is the ratio of fluid velocity to local speed of sound a = √(γRT) for an ideal gas. For M < 0.3, compressibility effects are typically negligible and incompressible flow assumptions apply. As M increases, density variations become significant and require modification to continuity, momentum, and energy equations. Subsonic (M < 1), transonic (M ≈ 1), and supersonic (M > 1) regimes exhibit qualitatively different behavior.

## How It's Best Learned
Calculate Mach numbers for air flows at different velocities (sea-level and altitude) to understand the speeds at which compressibility becomes important. Solve subsonic and supersonic nozzle problems to see how area, Mach, and pressure relate differently in each regime.

## Explainer

In most of the fluid problems you have solved so far, density has been a constant. Water is incompressible for all practical purposes, and slow-moving air behaves the same way — the pressures involved are small compared to atmospheric pressure, so density barely changes. The Mach number is the ratio that tells you when to abandon this assumption. It does not measure absolute speed; it measures how fast the flow is moving relative to the medium's own ability to transmit pressure disturbances.

The **speed of sound** a = √(γRT) is a property of the gas, not of the flow. It is the speed at which a small pressure disturbance — a tap on a drum, a conversation, an airplane's pressure wave — propagates through the medium. For air at sea level (T ≈ 293 K, γ = 1.4), a ≈ 343 m/s. At altitude where air is colder, a is lower, which is why aircraft reach supersonic flight more easily at altitude even at the same airspeed. The **Mach number** M = V/a measures whether the flow is slower or faster than this information-propagation speed.

When M < 1, pressure disturbances can run upstream ahead of the flow and warn the fluid that an obstacle is coming. The gas has time to adjust — diverting smoothly around wings and through nozzles. When M > 1, the flow outpaces its own pressure signals. No upstream warning is possible. Information piles up at the nose of an obstacle, forming a **shock wave** — an extremely thin region of near-discontinuous property changes. Across a shock, pressure, temperature, and density jump abruptly while velocity drops. This is a qualitatively different regime, not just a quantitative extension of subsonic behavior.

The threshold M < 0.3 for "incompressible" comes from the isentropic relation for density change: at M = 0.3, density varies by about 5% compared to the stagnation condition — usually acceptable engineering error. As M increases toward 1.0, density variations grow rapidly, and the incompressible Bernoulli equation gives increasingly wrong answers. The **area-velocity relation** for isentropic flow is dA/A = (M² − 1) dV/V. For M < 1, this is negative — a converging nozzle accelerates flow. For M > 1, it is positive — a *diverging* section accelerates supersonic flow. This counterintuitive reversal is the key result of compressible nozzle theory.

Near M = 1.0 (the transonic regime), the flow becomes especially sensitive to geometry. Supersonic patches form locally on airfoils at freestream speeds well below Mach 1 — one reason commercial aircraft are designed to cruise at M ≈ 0.82–0.85 rather than pushing to 0.95. The governing equations change mathematical type (from elliptic to hyperbolic) at M = 1, which is why a new set of analytical tools — method of characteristics, shock relations, isentropic flow tables — is needed for supersonic design. Mach number is the single parameter that determines which regime governs, and every result in compressible flow ultimately branches on whether M is below, at, or above unity.

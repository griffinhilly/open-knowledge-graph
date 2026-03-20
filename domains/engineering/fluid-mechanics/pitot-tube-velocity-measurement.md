---
id: pitot-tube-velocity-measurement
title: Pitot Tube and Velocity Measurement
domain: engineering
course: fluid-mechanics
prerequisites:
- id: absolute-gauge-atmospheric-pressure
  type: hard
- id: bernoullis-equation
  type: hard
builds-toward:
- streamlines-and-flow-visualization
tags:
- measurement
- instruments
- flow
stage: advanced
status: draft
---

# Pitot Tube and Velocity Measurement

## Core Idea
A Pitot tube measures flow velocity by converting dynamic pressure into a height difference in a manometer. The stagnation pressure (total pressure where flow stops) minus static pressure equals the dynamic pressure: q = ½ρV². Pitot tubes are widely used for measuring airspeed in aircraft and water velocity in open channels because they cause minimal flow disturbance.

## Explainer

Bernoulli's equation, which you know from prerequisites, states that along a streamline in steady, inviscid, incompressible flow: P + ½ρV² + ρgz = constant. This is an energy statement — the sum of pressure energy, kinetic energy, and potential energy per unit volume is conserved. The **dynamic pressure** ½ρV² represents the kinetic energy of the moving fluid. A Pitot tube exploits this relationship by creating a controlled stagnation point: a small hole facing directly into the flow brings the fluid momentarily to rest, converting all of its kinetic energy into a measurable pressure increase.

The device in practice consists of two pressure ports. The **stagnation port** faces upstream and measures total pressure P_total = P_static + ½ρV². The **static port** is flush with the tube wall and measures P_static, the ambient pressure at that location. The difference is exactly the dynamic pressure: P_total − P_static = ½ρV². Solving for velocity gives V = √(2(P_total − P_static)/ρ). You only need to measure a pressure difference and know the fluid density — no other information about the flow is required.

From your understanding of pressure measurement, you know that pressure differences can be read directly with a manometer or differential pressure transducer. In a water-filled manometer connected to the two ports, the height difference Δh satisfies ΔP = ρ_fluid · g · Δh. Substituting back gives V = √(2gΔh) for the special case where the manometer fluid is the same as the flowing fluid. This clean result is why Pitot tubes are popular in introductory lab courses — the velocity comes directly from a ruler measurement of liquid height.

On aircraft, the **Pitot-static system** connects one probe facing the airstream (for stagnation pressure) and one set of flush ports on the fuselage (for static pressure). The difference drives the airspeed indicator. One critical limitation: the classical Bernoulli derivation assumes incompressible flow. At low aircraft speeds this is fine, but above roughly Mach 0.3 the compressibility correction becomes important. For subsonic aircraft the correction is a modest factor; for supersonic flight, a normal shock forms ahead of the probe and the analysis must account for the entropy rise across the shock — the Rayleigh Pitot tube formula applies instead. But the core physical idea — measure the pressure rise from stagnating a moving fluid — remains unchanged across all these regimes.

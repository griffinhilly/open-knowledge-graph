---
id: cavitation-pressure-vapor-dynamics
title: Cavitation and Vapor Pressure Dynamics
domain: engineering
course: fluid-mechanics
prerequisites:
- id: absolute-gauge-atmospheric-pressure
  type: hard
tags:
- cavitation
- vapor
- pressure
- damage
stage: advanced
status: draft
---

# Cavitation and Vapor Pressure Dynamics

## Core Idea
Cavitation occurs when pressure in a flowing liquid drops below the vapor pressure, causing liquid to vaporize and form bubbles. These bubbles collapse when they reach high-pressure regions, creating pressure spikes that can damage surfaces. Cavitation is a concern in pumps, turbines, and behind propellers; it is avoided by maintaining minimum pressure or reducing fluid temperature, and its onset is predicted using the cavitation number σ = (P − P_v)/(½ρV²).

## Explainer

From your work with absolute and gauge pressure, you know that every liquid has a **vapor pressure** P_v — the pressure at which it transitions from liquid to vapor at a given temperature. At sea level and room temperature, water's vapor pressure is only about 2,300 Pa (much less than atmospheric 101,325 Pa), so you don't normally worry about it. But in high-speed flows, local pressure can drop dramatically. By Bernoulli's equation, regions of high velocity correspond to low pressure. When that local pressure falls below P_v, the liquid instantaneously vaporizes, forming vapor-filled voids called **cavitation bubbles**.

The damage comes not from the bubble's formation but from its collapse. As a cavitation bubble travels downstream into a region of higher pressure, it implodes asymmetrically and violently — the surrounding liquid rushes inward faster than the speed of sound in the liquid, generating a focused **microjet** and pressure pulses reaching thousands of atmospheres. These repeated impacts erode metal surfaces, pitting pump impellers, propeller blades, and turbine runner faces even in hardened steel. The damage looks like the surface has been sand-blasted from the inside. In extreme cases, cavitation destroys impellers within months of installation.

Engineers quantify cavitation tendency with the dimensionless **cavitation number** σ = (P − P_v)/(½ρV²). The numerator is how far the local pressure exceeds vapor pressure — the margin before vaporization. The denominator is the dynamic pressure associated with flow velocity. A small σ means cavitation is likely; a large σ means the flow is safely above vapor pressure. For pump systems, this becomes the **Net Positive Suction Head (NPSH)**: the minimum head at the pump inlet that prevents cavitation. If NPSH available (from system geometry and fluid pressure) falls below NPSH required (from the pump manufacturer), cavitation occurs.

Prevention strategies all work by raising local pressure relative to vapor pressure: lower the fluid temperature (reducing P_v), increase the static pressure at the problem location (raise inlet pressure, shorten the suction pipe, add head), reduce flow velocity (operate away from peak flow), or use materials and coatings that resist pitting. Inducer impellers placed upstream of the main impeller are specifically designed to raise local pressure before the main rotor, buying margin against cavitation. Understanding that cavitation is fundamentally a **pressure-relative-to-vapor-pressure** problem — not simply a boiling problem — is the key to diagnosing and preventing it.

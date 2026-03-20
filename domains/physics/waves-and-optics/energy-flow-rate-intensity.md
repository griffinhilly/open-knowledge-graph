---
id: energy-flow-rate-intensity
title: Energy Transport and Wave Intensity
domain: physics
course: waves-and-optics
prerequisites:
- id: particle-velocity-oscillating-motion
  type: hard
- id: power-and-work-rate
  type: soft
builds-toward:
- sound-level-logarithmic-scale
- wave-energy-and-intensity
tags:
- waves
- energy
- power
stage: advanced
status: draft
---

# Energy Transport and Wave Intensity

## Core Idea
Intensity is the average power per unit area carried by a wave (I ∝ A² f²), proportional to the square of amplitude and frequency. Energy flows at the group velocity in dispersive media. The Poynting vector describes energy flow direction and magnitude in electromagnetic waves.

## Explainer

You already know from oscillating motion that the energy stored in a vibrating particle scales with the square of its amplitude — a particle displaced twice as far has four times the potential energy. Waves carry energy by passing that oscillation from particle to particle, so it follows directly that **wave intensity** — the rate at which energy passes through a unit area — also scales with amplitude squared: I ∝ A². Double the amplitude and you quadruple the power delivered to any surface the wave passes through. Frequency matters too: higher frequency means more oscillation cycles per second, each carrying energy, giving the I ∝ f² dependence.

From your work on power and work rate, you know power is energy per unit time. Intensity simply divides that further by the area over which the power is spread. Think of a speaker: it radiates sound power outward in all directions. As you move away, that same total power is spread over an ever-larger spherical surface (area = 4πr²). Since the power is conserved but the area grows as r², intensity falls as 1/r² — the **inverse square law** for point sources. This is why sound seems four times quieter when you double your distance from a loudspeaker.

For electromagnetic waves, the concept needs a vector treatment. The **Poynting vector** S = E × B / μ₀ points in the direction the wave is traveling and has magnitude equal to the instantaneous intensity. The cross product of the electric and magnetic fields gives the direction of energy flow — always perpendicular to both fields — which is exactly the direction of wave propagation. For a plane wave traveling in one direction, the time-averaged Poynting vector magnitude gives the average intensity that you'd measure with a light meter or power sensor.

The key insight connecting all these cases is that energy does not "travel with" the medium. The medium oscillates back and forth while the energy pattern advances steadily forward. The particles you studied in oscillating motion stay roughly in place; what moves is the organized disturbance. Intensity measures how much of that organized energy flux passes through a cross-section per second — whether the wave is sound, light, seismic, or electromagnetic, the same dimensional relationship (power per area) captures how concentrated or diffuse that energy flow is.

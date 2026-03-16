---
id: sound-waves-longitudinal
title: Sound Waves and Longitudinal Propagation
domain: physics
course: waves-and-optics
prerequisites:
- id: transverse-and-longitudinal-waves
  type: hard
- id: wavelength-frequency-speed-relationship
  type: hard
builds-toward:
- doppler-shift-observer-motion
- acoustic-resonance-pipes
tags:
- sound
- longitudinal
- compression
stage: formal-systems
status: draft
---

# Sound Waves and Longitudinal Propagation

## Core Idea
Sound travels as longitudinal pressure waves, with particles oscillating parallel to the direction of wave propagation. Sound speed depends on the medium's properties (density and elasticity), not on frequency or amplitude. In air at 20°C, sound travels at ~343 m/s; in water it's ~1480 m/s due to higher elasticity.

## Explainer

From your study of wave types, you know the key distinction: in a **transverse** wave, the medium oscillates perpendicular to the wave's travel direction (like a rope wave), while in a **longitudinal** wave, the medium oscillates parallel to the travel direction. Sound is longitudinal. A vibrating speaker cone pushes on the air molecules directly in front of it, creating a region of slightly higher pressure — a **compression**. Those molecules then push on their neighbors, which push on their neighbors, and so on. Behind the initial compression, molecules spread apart into a **rarefaction** (lower pressure). The result is a pressure disturbance that propagates outward even though no individual air molecule travels the full distance — each one just oscillates back and forth around its equilibrium position.

You also know from the wave equation v = fλ that wave speed, frequency, and wavelength are linked. For sound, this relationship holds, but the speed v is set entirely by the **medium** — not by the frequency or amplitude of the source. Sound speed depends on two competing properties: the **bulk modulus** (how strongly the medium resists compression — a higher modulus means faster transmission) and the **density** (how much mass must be accelerated — higher density slows transmission). Mathematically, v = √(B/ρ), where B is the bulk modulus and ρ is density. Water has both higher bulk modulus and higher density than air, but the modulus effect dominates, which is why sound travels about four times faster in water (~1480 m/s) than in air (~343 m/s).

Temperature affects sound speed because it affects the bulk modulus of a gas. Warmer air has faster-moving molecules and resists compression more elastically, so sound travels faster: in air, roughly +0.6 m/s per degree Celsius rise. This explains a familiar experience: you see a lightning bolt essentially instantaneously (light arrives in microseconds), but you hear the thunder about 3 seconds later per kilometer of distance. The delay is pure sound travel time, and knowing the speed of sound lets you estimate how far away the storm is. Frequency and amplitude change what you hear (pitch and loudness), but they don't change the propagation speed — that is entirely a property of the medium.


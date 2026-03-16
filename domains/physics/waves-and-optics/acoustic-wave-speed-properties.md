---
id: acoustic-wave-speed-properties
title: Sound Wave Speed and Temperature Dependence
domain: physics
course: waves-and-optics
prerequisites:
- id: wavelength-frequency-speed-relation
  type: hard
- id: kinetic-theory-of-gases
  type: soft
builds-toward:
- vibrating-string-normal-modes
- vibrating-air-column-modes
tags:
- sound
- acoustics
- temperature
stage: formal-systems
status: draft
---

# Sound Wave Speed and Temperature Dependence

## Core Idea
Sound speed in an ideal gas is v = √(γRT/M), depending on the gas's adiabatic index γ, temperature T, and molar mass M. In air at 20°C, v ≈ 343 m/s. Speed is independent of pressure but increases with temperature (≈ 0.6 m/s per °C in air). Sound travels faster in solids and liquids due to stronger intermolecular forces.

## Explainer

From your study of the wavelength-frequency-speed relation, you know that v = fλ — wave speed connects how rapidly a pattern oscillates in time (frequency) with how it stretches in space (wavelength). But what sets the speed itself? For mechanical waves, the answer is always the same in form: speed depends on how stiff or elastic the medium is relative to how massive it is. A stiffer medium responds faster, and a lighter medium accelerates more readily. For sound in an ideal gas, this gives v = √(γRT/M), where the numerator captures the elastic restoring force (via the adiabatic index γ and thermal energy RT) and the denominator M captures the inertia of the gas molecules.

The kinetic theory of gases you've encountered provides the intuition here. Temperature measures the average kinetic energy of gas molecules. Higher temperature means molecules are moving faster on average, which means they collide and transmit pressure disturbances — sound pulses — more quickly. This is why the sound speed in air rises by roughly 0.6 m/s for every 1°C increase in temperature. On a hot summer day (35°C), sound travels about 351 m/s; on a cold winter morning (−10°C), it falls to about 325 m/s. The speed depends on molecular activity, not on how compressed the air is — doubling the pressure also roughly doubles the density, and the two effects cancel exactly for an ideal gas.

A surprising consequence is medium dependence. Steel is far stiffer than air — its elastic modulus is roughly a million times larger — and while it is also denser, the stiffness wins decisively. Sound in steel travels at about 5,100 m/s, nearly 15 times faster than in air. In water, sound travels at about 1,480 m/s. This is why you can hear a distant train before you feel the vibration in the rails: the rails deliver the sound in a fraction of the time the air does. In all cases, the underlying mechanism is the same — elastic restoring forces transmit the disturbance, and **wave speed** is determined by the ratio of stiffness to inertia in the medium.

Understanding acoustic speed is foundational for the vibrating string and air column problems you will encounter next. In those contexts, the medium's sound speed sets the natural frequencies — the normal modes. A longer column of air or a longer string has lower-frequency resonances not because of any change in wave speed, but because the wavelengths of standing waves scale with the physical dimensions. You will apply v = fλ in those situations with the wave speed fixed by the medium's properties — the groundwork you've established here.


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
stage: formal-systems
status: draft
---

# Mach Number and Speed of Sound: Compressibility Effects

## Core Idea
The Mach number M = V/a is the ratio of fluid velocity to local speed of sound a = √(γRT) for an ideal gas. For M < 0.3, compressibility effects are typically negligible and incompressible flow assumptions apply. As M increases, density variations become significant and require modification to continuity, momentum, and energy equations. Subsonic (M < 1), transonic (M ≈ 1), and supersonic (M > 1) regimes exhibit qualitatively different behavior.

## How It's Best Learned
Calculate Mach numbers for air flows at different velocities (sea-level and altitude) to understand the speeds at which compressibility becomes important. Solve subsonic and supersonic nozzle problems to see how area, Mach, and pressure relate differently in each regime.

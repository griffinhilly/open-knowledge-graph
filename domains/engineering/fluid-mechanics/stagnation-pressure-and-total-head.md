---
id: stagnation-pressure-and-total-head
title: Stagnation Pressure and Total Head
domain: engineering
course: fluid-mechanics
prerequisites:
- id: bernoullis-equation
  type: hard
- id: fluid-kinematics
  type: soft
builds-toward:
- isentropic-nozzle-flow-choked-conditions
- rayleigh-line-flow-stagnation-conditions
tags:
- pressure
- energy
- compressible-flow
stage: formal-systems
status: draft
---

# Stagnation Pressure and Total Head

## Core Idea
Stagnation pressure (total pressure) represents the pressure a moving fluid would reach if brought to rest isentropically. It equals static pressure plus dynamic pressure: P₀ = P + (1/2)ρV². The stagnation temperature similarly combines thermal and kinetic energy, remaining constant along streamlines in adiabatic flows. This concept is fundamental for understanding energy transformations in pumps, compressors, and jet flows.

## How It's Best Learned
Measure pressure at a stagnation point on a Pitot tube and compare to static pressure measured in the free stream. Verify Bernoulli's equation by showing the sum is constant. Then apply to subsonic nozzles where stagnation conditions are set by inlet state.

## Common Misconceptions
Stagnation pressure is not a 'real' pressure at every point—it is the pressure the fluid would have if brought to rest. Static pressure and dynamic pressure are not added linearly in compressible flows; you must use isentropic relations to convert between them.

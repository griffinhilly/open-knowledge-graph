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
stage: advanced
status: draft
---

# Stagnation Pressure and Total Head

## Core Idea
Stagnation pressure (total pressure) represents the pressure a moving fluid would reach if brought to rest isentropically. It equals static pressure plus dynamic pressure: P₀ = P + (1/2)ρV². The stagnation temperature similarly combines thermal and kinetic energy, remaining constant along streamlines in adiabatic flows. This concept is fundamental for understanding energy transformations in pumps, compressors, and jet flows.

## How It's Best Learned
Measure pressure at a stagnation point on a Pitot tube and compare to static pressure measured in the free stream. Verify Bernoulli's equation by showing the sum is constant. Then apply to subsonic nozzles where stagnation conditions are set by inlet state.

## Common Misconceptions
Stagnation pressure is not a 'real' pressure at every point—it is the pressure the fluid would have if brought to rest. Static pressure and dynamic pressure are not added linearly in compressible flows; you must use isentropic relations to convert between them.

## Explainer

Bernoulli's equation — your core prerequisite — states that along a streamline in steady, inviscid, incompressible flow, P + ½ρV² + ρgz is constant. Each term represents energy per unit volume: pressure energy, kinetic energy, and gravitational potential energy. **Stagnation pressure** P₀ is what you get when all the kinetic energy is converted to pressure energy: P₀ = P + ½ρV². It represents the pressure a moving fluid parcel would have if brought to rest **isentropically** — without friction or heat transfer, so that no energy is lost in the conversion. Stagnation pressure does not exist as a local property everywhere in the flow; it is a hypothetical thermodynamic bookkeeping value that encodes the total mechanical energy the fluid carries.

The place where the flow actually reaches stagnation is the **stagnation point** — the tip of a Pitot tube, the leading edge of an airfoil, the nose of a blunt body. Here the velocity is literally zero and P = P₀. Every other location in the flow has V > 0 and therefore P < P₀. A **Pitot tube** exploits this directly: its open stagnation port measures P₀ while a nearby static port measures P. Velocity follows from V = √(2(P₀ − P)/ρ). This is how aircraft airspeed indicators work, and it is why Pitot tubes are the universal velocity sensor for any flow where you can make a stagnation point.

**Total head** H = P₀/(ρg) = P/(ρg) + V²/(2g) + z rewrites Bernoulli's equation in units of length — meters of fluid column — rather than pressure. Hydraulic engineers prefer head because they want to track energy budgets through systems with pumps, turbines, valves, and friction losses. A pump adds total head; a turbine extracts it; pipe friction dissipates it irreversibly. The hydraulic grade line (plotting P/(ρg) + z) and the energy grade line (plotting H) provide visual maps of how pressure and velocity energy are distributed and lost along a pipeline.

The stagnation concept becomes especially powerful — and qualitatively different — in compressible (high-speed) flows. In incompressible flow, P₀ = P + ½ρV² is exact. In compressible flow, density changes with velocity, and the correct relation is the isentropic stagnation formula: P₀/P = (1 + (γ−1)/2 × M²)^(γ/(γ−1)), where M is the Mach number. At low M this reduces to the incompressible result, but at M = 1 (sonic flow), P₀/P = 1.893 for air — the static pressure is only 53% of the stagnation pressure. In compressible nozzles and diffusers, **stagnation conditions** (P₀, T₀) remain constant through an isentropic process even as static pressure and temperature vary dramatically. They are the natural reference state for the entire flow field — the "energy bank account" that the fluid draws from as it accelerates through a nozzle.

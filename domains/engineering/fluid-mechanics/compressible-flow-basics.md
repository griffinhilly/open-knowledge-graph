---
id: compressible-flow-basics
title: Compressible Flow Basics
domain: engineering
course: fluid-mechanics
prerequisites:
- id: bernoullis-equation
  type: hard
- id: fluid-properties-and-continuum
  type: hard
tags:
- compressible flow
- Mach number
- speed of sound
- isentropic relations
- compressibility effects
- stagnation properties
stage: formal-systems
status: draft
---
# Compressible Flow Basics

## Core Idea
When a gas flows at speeds comparable to the local speed of sound a = √(γRT), density changes become significant and the incompressible assumption breaks down. The Mach number Ma = V/a is the key parameter: flows are classified as subsonic (Ma < 1), transonic (Ma ≈ 0.8–1.2), supersonic (Ma > 1), and hypersonic (Ma > 5). For isentropic (reversible, adiabatic) flow of an ideal gas, stagnation (total) properties — T₀, P₀, ρ₀ — relate to static properties through Ma: T₀/T = 1 + (γ−1)/2·Ma², with analogous relations for pressure and density using the isentropic exponents. Compressibility effects are generally negligible below Ma ≈ 0.3 (density changes less than 5%), which is why most liquid flows and low-speed gas flows can be treated as incompressible. Above Ma = 0.3, the energy equation must be coupled with the momentum and continuity equations, and Bernoulli's equation in its incompressible form is no longer valid.

## How It's Best Learned
Compute stagnation temperature and pressure for air at several Mach numbers (0.3, 0.8, 1.0, 2.0, 3.0) to build intuition for how dramatically compressibility effects grow. Use isentropic flow tables or the area-velocity relation (A/A* as a function of Ma) to analyze converging-diverging nozzle flows. Compare the incompressible Bernoulli prediction for dynamic pressure (½ρV²) against the compressible stagnation pressure to see the error grow with Mach number.

## Common Misconceptions
- The speed of sound is not a fixed number — it depends on temperature (a = √(γRT) for an ideal gas). At high altitude where temperature drops, the speed of sound decreases, so an aircraft can be at a higher Mach number at the same airspeed.
- Compressible does not mean turbulent. Compressibility refers to density variation with pressure; turbulence refers to chaotic velocity fluctuations. A laminar supersonic flow in a nozzle is compressible but not turbulent.
- Bernoulli's equation can be extended to compressible isentropic flow, but the form changes: it becomes an integral involving density as a function of pressure, not the simple ½ρV² + P = const form. Using the incompressible form at high Mach numbers yields significant errors in pressure prediction.

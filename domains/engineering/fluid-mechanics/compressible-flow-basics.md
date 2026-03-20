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
stage: advanced
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

## Explainer

You already know Bernoulli's equation: along a streamline, P + ½ρV² + ρgz = constant. This derivation assumed density is fixed — a safe assumption for liquids and for air moving well below the speed of sound. But as a gas accelerates toward and beyond the speed of sound, it no longer has time to "get out of the way" without compressing. The pressure waves that ordinarily allow fluid to rearrange itself travel at the speed of sound; once the flow matches that speed, the upstream fluid receives no warning that something is coming. The **Mach number** Ma = V/a, where a = √(γRT) is the local speed of sound, is the single parameter that captures how far into this regime you've traveled.

The speed of sound itself is not a fixed constant — it depends on temperature. At sea level on a standard day, a ≈ 340 m/s, but at 12 km altitude where temperature drops to about −57°C, a ≈ 295 m/s. This is why aircraft can experience compressibility effects at altitudes lower than you might expect, and why Mach number is a more meaningful speed measure than airspeed alone in high-altitude aerodynamics. Below Ma ≈ 0.3, density changes are less than 5% and the incompressible Bernoulli equation is accurate enough for most purposes. Above that threshold, you must account for the coupling between the momentum, continuity, and energy equations.

For **isentropic flow** — reversible and adiabatic, which is a good model for flow through nozzles and diffusers away from shocks — temperature, pressure, and density all relate to Mach number through elegant closed-form expressions. The **stagnation temperature** T₀ = T(1 + (γ−1)/2 · Ma²) represents what temperature a moving parcel of gas would reach if you slowed it to rest without heat transfer. This is what a pitot tube (which brings flow to rest at its stagnation point) actually measures. Pressure and density scale with higher powers of the same factor. At Ma = 1, the static pressure has already fallen to about 52.8% of stagnation pressure for air (γ = 1.4), illustrating just how dramatic the compressibility corrections become even at relatively modest supersonic speeds.

The practical consequence is that using incompressible Bernoulli at Mach 0.8 underestimates the stagnation pressure by roughly 6% — an error that matters enormously for aircraft speed measurement, nozzle design, and turbomachinery. As a rule of thumb: if Ma < 0.3, use incompressible Bernoulli; if Ma > 0.3, use isentropic relations; if a normal shock is present, add the Rankine-Hugoniot shock relations. The isentropic framework built here is the foundation for all of these extensions.

---
id: normal-shock-waves
title: Normal Shock Waves
domain: engineering
course: fluid-mechanics
prerequisites:
- id: compressible-flow-basics
  type: hard
tags:
- normal shock
- Rankine-Hugoniot
- shock relations
- total pressure loss
- supersonic to subsonic
stage: formal-systems
status: draft
---
# Normal Shock Waves

## Core Idea
A normal shock wave is an extremely thin (~micrometers), stationary discontinuity perpendicular to the flow direction across which a supersonic flow abruptly decelerates to subsonic. Conservation of mass, momentum, and energy across the shock — the Rankine-Hugoniot relations — uniquely determine the downstream conditions given the upstream Mach number. Across a normal shock: static pressure, temperature, density, and entropy all increase, while velocity, Mach number, and total (stagnation) pressure all decrease. The total temperature remains constant (adiabatic process), but the process is irreversible, so total pressure is permanently lost. The strength of these jumps increases with upstream Mach number — at Ma₁ = 1 the shock vanishes (no discontinuity), while at Ma₁ = 2 in air (γ = 1.4), the pressure ratio is 4.5 and the downstream Mach number is 0.577. Normal shocks appear in supersonic inlets, at the exit of overexpanded nozzles, and ahead of blunt bodies in supersonic flight.

## How It's Best Learned
Use the normal shock tables (or derive them from the Rankine-Hugoniot relations) to compute downstream conditions for several upstream Mach numbers. Plot pressure ratio, temperature ratio, and total pressure ratio vs. Ma₁ to see the nonlinear growth. Analyze a converging-diverging nozzle at an intermediate back pressure where a normal shock stands in the diverging section: locate the shock position, compute conditions on each side, and verify that the exit pressure matches the imposed back pressure.

## Common Misconceptions
- A normal shock is not isentropic — entropy increases across the shock. This means total pressure decreases, which is why shock waves in engine inlets degrade performance and engineers design inlets to minimize or oblique the shocks.
- The flow downstream of a normal shock is always subsonic (Ma₂ < 1), regardless of how strong the upstream supersonic flow is. This is a mathematical consequence of the conservation equations, not an assumption.
- Normal shocks cannot exist in subsonic flow. If Ma₁ < 1, the Rankine-Hugoniot relations would require entropy to decrease, violating the second law of thermodynamics. Compression in subsonic flow occurs smoothly through pressure waves, not shocks.

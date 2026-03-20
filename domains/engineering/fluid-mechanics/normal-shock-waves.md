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
stage: advanced
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

## Explainer

From your prerequisite study of compressible flow basics, you know that the character of a flow changes fundamentally at Mach 1. In subsonic flow, pressure disturbances propagate as sound waves in all directions — including upstream — so the flow can sense and adjust to obstacles ahead. In supersonic flow, disturbances propagate only downstream; the flow has no advance warning of what is coming. When a supersonic flow must decelerate to match a downstream boundary condition — the stagnation pressure at a blunt body's nose, a subsonic nozzle exit, or the back pressure in a duct — it cannot do so gradually by sending information upstream. Instead it adjusts instantaneously, in an extraordinarily thin region called a **normal shock wave**.

Across the shock, conservation of mass, momentum, and energy — the **Rankine-Hugoniot relations** — uniquely determine all downstream conditions given only the upstream Mach number Ma₁. The results are sharp and counter-intuitive: static pressure, temperature, and density all jump upward, while velocity and Mach number drop. The downstream flow is always subsonic, with a Mach number Ma₂ that depends only on Ma₁ and the specific heat ratio γ. At Ma₁ = 2 in air (γ = 1.4), Ma₂ = 0.577, the static pressure ratio is 4.5, and the temperature ratio is 1.69. As Ma₁ → 1 from above, the shock weakens to zero; as Ma₁ → ∞, Ma₂ approaches a finite lower limit ((γ−1)/(2γ))^(1/2) ≈ 0.378 for air. The conservation equations determine the outcome completely — there is no choice.

The most important thermodynamic fact about a normal shock is its irreversibility. **Total temperature** T₀ is conserved — the process is adiabatic, with no heat transfer across the thin shock. But **total pressure** P₀ decreases, and it does so irreversibly: entropy increases across every shock, consistent with the second law. The total pressure ratio P₀₂/P₀₁ < 1 is a direct measure of the shock's entropy generation, and it decreases rapidly as Ma₁ increases above 1. This total pressure loss is the central performance penalty in propulsion systems. A jet engine ingesting a Mach 2 flow through a single normal shock loses about 27% of its total pressure before the air even reaches the compressor — an enormous efficiency hit. Supersonic inlet design is largely the art of replacing one strong normal shock with a sequence of weaker oblique shocks, each generating less entropy, collectively achieving higher total pressure recovery.

Normal shocks appear wherever supersonic flow must match a subsonic exit condition. In a converging-diverging nozzle operated at an intermediate back pressure, a normal shock stands in the diverging section, converting the supersonic core to subsonic. As back pressure decreases toward the design exit pressure, the shock moves toward the nozzle exit and weakens; at the design condition the shock disappears. Ahead of a blunt body in supersonic flight, a detached **bow shock** forms: it curves from nearly normal at the stagnation streamline (where the full deceleration to zero velocity occurs) to increasingly oblique off to the sides (where the deceleration is partial and the entropy rise is smaller). The stagnation point streamline, which crosses the normal portion of the bow shock, experiences the largest total pressure loss — this is why streamlining and pointed noses reduce supersonic drag.

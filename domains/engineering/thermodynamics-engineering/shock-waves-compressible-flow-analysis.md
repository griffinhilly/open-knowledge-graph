---
id: shock-waves-compressible-flow-analysis
title: Normal Shock Waves and Shock Analysis
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: normal-shock-waves
  type: hard
- id: isentropic-flow-with-area-change
  type: soft
tags:
- shock-waves
- compressible-flow
- entropy-generation
stage: advanced
status: draft
---

# Normal Shock Waves and Shock Analysis

## Core Idea
Normal shock waves are thin regions where supersonic flow decelerates to subsonic with large irreversible entropy increase. Rankine-Hugoniot relations govern pressure, temperature, and velocity jumps across the shock. Stagnation pressure always drops; entropy always increases. Shock location and strength significantly affect inlet pressure recovery in supersonic vehicles and compressor inlet conditions.

## Explainer

From your study of isentropic flow with area change, you know that supersonic flow in a converging-diverging nozzle accelerates smoothly so long as boundary conditions are favorable. But what happens when supersonic flow encounters an abrupt obstacle or a back pressure that the flow cannot accommodate isentropically? The answer is a **shock wave** — a nearly discontinuous jump in flow properties that happens across a layer only a few mean-free-paths thick. Understanding shocks means understanding what the conservation equations demand when isentropic adjustment is impossible.

A **normal shock** stands perpendicular to the flow direction. Across it, three conservation laws apply simultaneously: conservation of mass (ρ₁V₁ = ρ₂V₂), conservation of momentum (p₁ + ρ₁V₁² = p₂ + ρ₂V₂²), and conservation of energy (h₁ + V₁²/2 = h₂ + V₂²/2). These three equations, combined with the equation of state for a perfect gas, give the **Rankine-Hugoniot relations** that express all downstream conditions purely as functions of the upstream Mach number M₁. The key results: pressure, temperature, and density all jump upward across the shock; velocity drops sharply; and M₂ < 1 always (supersonic flow always exits a normal shock as subsonic). You can look up these ratios in normal shock tables indexed by M₁.

The thermodynamics of the shock is what distinguishes it from isentropic flow. Because the process is irreversible — violent viscous and thermal mixing in an extremely thin region — **entropy increases** across the shock. On the h-s diagram, the downstream state lies to the right of the upstream state on the same stagnation enthalpy line (total enthalpy is conserved since the flow is adiabatic). Stagnation temperature is conserved, but **stagnation pressure drops** — this is the key performance penalty. Stagnation pressure represents the maximum pressure recoverable if the flow were decelerated isentropically; losing it means you cannot fully recover the flow's kinetic energy, which directly reduces thrust in a jet engine inlet or nozzle efficiency in a wind tunnel.

The strength of the shock is entirely determined by the upstream Mach number. At M₁ = 1, the shock degenerates to a vanishingly weak disturbance with zero entropy rise — this is the limit connecting shock analysis back to isentropic flow. As M₁ increases, pressure ratio and entropy rise grow rapidly. This is why supersonic inlet design tries to decelerate flow through a series of weaker oblique shocks rather than one strong normal shock: the entropy penalty of multiple weak shocks is lower than the penalty of a single strong one, preserving more stagnation pressure for the engine.

When working shock problems numerically, the approach is: identify M₁ from upstream conditions, use normal shock tables (or Mach-specific formulas) to find all property ratios across the shock, then apply isentropic flow relations separately on each side if the regions before and after the shock are themselves isentropic. Shocks are not isentropic, but the flow approaching the shock and the flow downstream of the shock (if no further shocks occur) may each be treated as isentropic within their respective regions.

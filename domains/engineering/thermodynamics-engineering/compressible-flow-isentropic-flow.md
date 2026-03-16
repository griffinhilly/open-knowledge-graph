---
id: compressible-flow-isentropic-flow
title: Compressible Flow and Isentropic Flow Analysis
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: control-volume-steady-flow
  type: hard
- id: isentropic-process-reversible
  type: hard
tags:
- compressible-flow
- isentropic-flow
- sonic-conditions
stage: advanced
status: draft
---

# Compressible Flow and Isentropic Flow Analysis

## Core Idea
Compressible flow accounts for density changes due to pressure variations; the sonic condition (Mach = 1) becomes relevant when flow speeds approach the local speed of sound. Isentropic flow relations give velocity and temperature as functions of pressure ratio and Mach number, enabling choked-flow analysis and nozzle design. Normal shock waves (sudden property jumps) occur when supersonic flow is decelerated below sonic speed, dissipating energy irreversibly.

## How It's Best Learned
Use isentropic flow relations (T₀/T = 1 + (γ-1)/2 * M², P₀/P = (1 + (γ-1)/2 * M²)^(γ/(γ-1))) to relate stagnation properties, static properties, and Mach number. Understand that choked flow (Mach = 1 at minimum area) limits mass flow rate regardless of downstream pressure. Calculate normal shock properties to quantify entropy generation and irreversibility across the shock.

## Common Misconceptions
- Sonic conditions are only relevant to very high speeds (jet engines); they occur in any high-speed flow, including compressors and turbine blade passages.
- Compressible flow effects are always small; they become significant when Mach number exceeds ~0.3 (roughly 100 m/s in air).
- A nozzle (converging passage) always accelerates flow; a converging nozzle accelerates subsonic flow but decelerates supersonic flow; a converging-diverging nozzle is required for supersonic exit flow.

## Explainer

From your study of isentropic processes, you know that reversible adiabatic compression and expansion leave entropy unchanged while changing temperature and pressure together in a fixed ratio. From control-volume analysis, you know how to track energy and mass across a flow boundary. Compressible flow welds these together by adding one new variable: the **Mach number** M = V/a, where a = √(γRT) is the local speed of sound. Mach number matters because it measures how fast the flow is moving relative to the speed at which pressure disturbances propagate — and when M approaches 1, that propagation speed can no longer carry information upstream.

The **stagnation state** is the anchor of isentropic flow analysis. If you were to bring the flow to rest isentropically (no friction, no heat transfer), it would reach the stagnation temperature T₀ = T(1 + (γ−1)/2 · M²) and stagnation pressure P₀ = P(1 + (γ−1)/2 · M²)^(γ/(γ−1)). The stagnation state is a reference — it does not require actually stopping the flow. In isentropic flow, T₀ and P₀ are constant throughout, so any change in local temperature and pressure is a pure conversion between thermal energy and kinetic energy. A flow that speeds up loses temperature; a flow that slows down gains it. This is why the leading edge of a hypersonic vehicle glows — it stagnates the air and dumps all that kinetic energy into heat.

The **area-velocity relationship** in compressible flow is counterintuitive: for subsonic flow (M < 1), a converging passage accelerates the gas, exactly as you would expect from the incompressible continuity equation. But for supersonic flow (M > 1), a converging passage *decelerates* the gas. The reason is that at supersonic speeds, density drops so rapidly with velocity that you actually need more area, not less, to keep the same mass flow rate. The **sonic condition** (M = 1) is a critical point that can only exist at a throat — the minimum area. To accelerate flow from subsonic to supersonic, you need a **converging-diverging nozzle**: converge to accelerate to M = 1 at the throat, then diverge to accelerate further into the supersonic regime. **Choked flow** occurs when the throat reaches M = 1; from that point, reducing downstream pressure cannot increase mass flow rate — the throat is already delivering the maximum.

A **normal shock wave** is what happens when supersonic flow encounters an obstruction or an adverse pressure gradient severe enough to decelerate it below sonic speed in a short distance. The shock is nearly discontinuous: pressure, temperature, and density jump sharply upward while velocity drops. Unlike isentropic flow, the shock is irreversible — entropy increases and stagnation pressure decreases across it. You can quantify the losses from the Rankine-Hugoniot jump conditions, which use conservation of mass, momentum, and energy across the shock front. The stagnation temperature is unchanged (energy is conserved), but stagnation pressure drops, meaning the downstream flow has less work-producing capacity. This is why aircraft inlets are designed to avoid strong normal shocks: the stagnation pressure recovery determines how efficiently the engine can extract energy from the captured air.

---
id: steady-flow-energy-equation-engineering
title: Steady-Flow Energy Equation
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-open-systems
  type: hard
- id: control-volume-steady-flow
  type: hard
builds-toward:
- turbine-compressor-efficiency-definitions
- heat-exchanger-effectiveness-ntu
- throttling-expansion-isenthalpic-process
tags:
- first-law
- control-volume
- steady-flow
- enthalpy
stage: advanced
status: draft
---

# Steady-Flow Energy Equation

## Core Idea
For steady-flow control volumes with inlet and outlet streams: Q̇ - Ẇ = Σṁ_out(h + ke + pe) - Σṁ_in(h + ke + pe). Enthalpy h = u + Pv naturally appears from flow work at boundaries. This equation is fundamental for analyzing turbines, compressors, pumps, heat exchangers, and nozzles in power and refrigeration cycles.

## Explainer

For a closed system you wrote dU = δQ - δW, tracking the energy of a fixed mass. Open systems change this accounting: mass enters and exits the control volume, and each parcel of mass carries energy with it. From your study of control volume thermodynamics, you know that a fluid element crossing a boundary does two things: it carries its internal energy u into the control volume, and it does work pushing against the pressure at the inlet (the fluid behind it must push it in). This **flow work** per unit mass is Pv, where v is specific volume. The total energy carried per unit mass is therefore u + Pv — which is precisely **enthalpy** h = u + Pv. This is why enthalpy, not internal energy, is the natural energy variable for open systems: it bundles together stored energy and the mechanical work of moving mass across a boundary.

Adding kinetic and gravitational potential energy per unit mass, the total energy transported by a mass flow is h + V²/2 + gz. The **steady-flow energy equation** (SFEE) balances all contributions: Q̇ - Ẇ_shaft = Σṁ_out(h + V²/2 + gz) - Σṁ_in(h + V²/2 + gz). For most thermal devices, kinetic and potential energy terms are small compared to enthalpy changes and are dropped. But for nozzles — which exist precisely to convert enthalpy into kinetic energy — the V²/2 term is the entire point, and enthalpy drop equals kinetic energy gain: V²_out/2 - V²_in/2 = h_in - h_out.

Each device type simplifies the SFEE in a characteristic way. A **turbine** operates adiabatically (Q̇ ≈ 0) and extracts shaft work: Ẇ = ṁ(h_in - h_out). A **heat exchanger** involves no shaft work and negligible kinetic or potential energy changes: Q̇ = ṁ(h_out - h_in). A **throttle** has no work, no heat, and negligible kinetic/potential changes — so h_in = h_out, meaning throttling is an isenthalpic process. These simplifications are not approximations pulled from thin air; they follow directly from which terms the device's function requires and which it makes negligible.

The SFEE is the master equation for analyzing power plant and refrigeration cycles. A Rankine cycle consists of a boiler, turbine, condenser, and pump — each analyzed separately with its simplified SFEE, linked by mass flow continuity. The net work output is turbine work minus pump work; the heat input is boiler duty; cycle efficiency is their ratio. Every state point in the cycle is defined by two independent properties (pressure and enthalpy, or pressure and entropy), read from steam tables, and every energy quantity follows from substituting into the SFEE. The equation is straightforward in form; the engineering skill lies in applying it consistently across each component and tracking state points through the cycle.

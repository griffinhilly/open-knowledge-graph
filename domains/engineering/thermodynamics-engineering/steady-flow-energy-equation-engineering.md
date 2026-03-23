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
stage: formal-systems
status: validated
---

# Steady-Flow Energy Equation

## Core Idea
For steady-flow control volumes with inlet and outlet streams: Q̇ - Ẇ = Σṁ_out(h + ke + pe) - Σṁ_in(h + ke + pe). Enthalpy h = u + Pv naturally appears from flow work at boundaries. This equation is fundamental for analyzing turbines, compressors, pumps, heat exchangers, and nozzles in power and refrigeration cycles.

## Questions

```yaml
- question: "A turbine operates adiabatically with a single inlet and single outlet. Which correctly applies the SFEE to find shaft work per unit mass flow?"
  type: multiple-choice
  options:
    - "ẇ = h_out − h_in, because the fluid gains enthalpy as it does work"
    - "ẇ = h_in − h_out, because the fluid loses enthalpy and that energy becomes shaft work"
    - "q̇ = h_out − h_in, because energy is conserved through heat transfer"
    - "ẇ = u_in − u_out, because internal energy is the relevant energy variable for work calculations"
  answer: 1
  explanation: "For an adiabatic turbine, Q̇ = 0, so the SFEE simplifies to Ẇ = ṁ(h_in − h_out). The fluid's enthalpy drops as it expands, and that energy is extracted as shaft work. Option D is the classic error: internal energy u is the energy variable for closed systems. In open systems, mass crossing the boundary also carries flow work Pv, so enthalpy h = u + Pv is the correct energy variable — and replacing h with u would miss this contribution entirely."

- question: "Why does enthalpy (h = u + Pv) rather than internal energy (u) appear in the steady-flow energy equation?"
  type: multiple-choice
  options:
    - "Internal energy cannot be measured directly, while enthalpy is tabulated in steam tables"
    - "Enthalpy includes the flow work (Pv) done to push fluid parcels across the control volume boundary"
    - "Enthalpy is a more general form of energy that reduces to internal energy when velocities are low"
    - "The SFEE uses enthalpy by convention; either variable gives the same answer if applied consistently"
  answer: 1
  explanation: "When a fluid parcel crosses a control volume boundary, the fluid behind it must do work to push it across against the local pressure — this is flow work, equal to Pv per unit mass. The total energy transported per unit mass is therefore u (stored energy) + Pv (work of entry) = h. Internal energy alone would undercount the energy transfer. Enthalpy is not a convention or a measurement convenience — it arises necessarily from the physics of mass crossing a boundary."

- question: "A throttle valve (like a pressure-reducing valve) operates with no shaft work, no heat transfer, and negligible kinetic and potential energy changes. Therefore, the fluid's enthalpy is the same at inlet and outlet."
  type: true-false
  answer: true
  explanation: "This follows directly from the SFEE with all terms set to zero except the enthalpy terms: 0 − 0 = ṁ(h_out − h_in), so h_in = h_out. Throttling is isenthalpic. Note that pressure and temperature can both change dramatically across the throttle — but enthalpy is conserved. For real gases with Joule-Thomson cooling, this isenthalpic process produces a temperature drop that is exploited in refrigeration systems."

- question: "For a nozzle, the kinetic energy terms in the SFEE can be neglected because nozzles are small and flow velocities are modest."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. A nozzle exists precisely to convert enthalpy into kinetic energy — the velocity increase is the entire purpose. The SFEE for a nozzle (adiabatic, no shaft work) is V²_out/2 − V²_in/2 = h_in − h_out. The kinetic energy term is not small; it is the output. In contrast, for devices like boilers and heat exchangers, kinetic and potential terms are genuinely negligible compared to enthalpy changes, but nozzles are the canonical exception."

- question: "Explain in your own words why enthalpy (h = u + Pv) rather than internal energy appears in the steady-flow energy equation. What does the Pv term represent physically?"
  type: short-answer
  answer: "When a parcel of fluid enters a control volume, the fluid behind it must exert pressure to push it across the boundary. This pushing requires mechanical work equal to P × v per unit mass (force per unit area times volume per unit mass = work per unit mass). This 'flow work' Pv is delivered to the control volume along with the parcel's stored internal energy u. The total energy arriving per unit mass is therefore u + Pv = h. Internal energy alone misses this mechanical contribution. For closed systems (fixed boundaries, no mass crossing), no flow work occurs and dU = Q − W is correct. Open systems require the enthalpy formulation precisely because mass — and the work of moving it — crosses the boundary continuously."
```

## Explainer

For a closed system you wrote dU = δQ - δW, tracking the energy of a fixed mass. Open systems change this accounting: mass enters and exits the control volume, and each parcel of mass carries energy with it. From your study of control volume thermodynamics, you know that a fluid element crossing a boundary does two things: it carries its internal energy u into the control volume, and it does work pushing against the pressure at the inlet (the fluid behind it must push it in). This **flow work** per unit mass is Pv, where v is specific volume. The total energy carried per unit mass is therefore u + Pv — which is precisely **enthalpy** h = u + Pv. This is why enthalpy, not internal energy, is the natural energy variable for open systems: it bundles together stored energy and the mechanical work of moving mass across a boundary.

Adding kinetic and gravitational potential energy per unit mass, the total energy transported by a mass flow is h + V²/2 + gz. The **steady-flow energy equation** (SFEE) balances all contributions: Q̇ - Ẇ_shaft = Σṁ_out(h + V²/2 + gz) - Σṁ_in(h + V²/2 + gz). For most thermal devices, kinetic and potential energy terms are small compared to enthalpy changes and are dropped. But for nozzles — which exist precisely to convert enthalpy into kinetic energy — the V²/2 term is the entire point, and enthalpy drop equals kinetic energy gain: V²_out/2 - V²_in/2 = h_in - h_out.

Each device type simplifies the SFEE in a characteristic way. A **turbine** operates adiabatically (Q̇ ≈ 0) and extracts shaft work: Ẇ = ṁ(h_in - h_out). A **heat exchanger** involves no shaft work and negligible kinetic or potential energy changes: Q̇ = ṁ(h_out - h_in). A **throttle** has no work, no heat, and negligible kinetic/potential changes — so h_in = h_out, meaning throttling is an isenthalpic process. These simplifications are not approximations pulled from thin air; they follow directly from which terms the device's function requires and which it makes negligible.

The SFEE is the master equation for analyzing power plant and refrigeration cycles. A Rankine cycle consists of a boiler, turbine, condenser, and pump — each analyzed separately with its simplified SFEE, linked by mass flow continuity. The net work output is turbine work minus pump work; the heat input is boiler duty; cycle efficiency is their ratio. Every state point in the cycle is defined by two independent properties (pressure and enthalpy, or pressure and entropy), read from steam tables, and every energy quantity follows from substituting into the SFEE. The equation is straightforward in form; the engineering skill lies in applying it consistently across each component and tracking state points through the cycle.

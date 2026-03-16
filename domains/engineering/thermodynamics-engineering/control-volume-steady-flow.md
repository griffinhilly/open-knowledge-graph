---
id: control-volume-steady-flow
title: Control Volume Analysis and Steady-Flow Devices
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-open-systems
  type: hard
- id: energy-conservation-applications
  type: hard
builds-toward:
- kinetic-potential-energy-flow
- compressible-flow-isentropic-flow
tags:
- control-volume
- steady-flow
- engineering-devices
stage: advanced
status: draft
---

# Control Volume Analysis and Steady-Flow Devices

## Core Idea
A control volume is a fixed region in space through which fluid flows; the steady-flow assumption means properties at each point don't change with time, though they may vary spatially. The control volume energy equation balances inlet and outlet enthalpy, kinetic energy, and potential energy with heat and shaft work. This is the dominant approach in engineering practice for analyzing most flow devices.

## Explainer

From your study of the first law for open systems, you know that energy can enter a control volume not just as heat and work, but also carried by mass flowing across the boundary. The **control volume** framework formalizes this: draw an imaginary boundary around a device (a turbine, a compressor, a nozzle, a heat exchanger), then account for every form of energy crossing that boundary per unit time. The **steady-flow assumption** is the key simplification — properties at any fixed point inside the boundary don't change with time, so there is no accumulation of internal energy inside the control volume. Whatever energy enters per second must equal whatever leaves per second.

Under steady-flow, the energy rate balance reduces to: Q̇ - Ẇ_shaft = ṁ [(h₂ - h₁) + ½(V₂² - V₁²) + g(z₂ - z₁)]. Read this term by term. Q̇ is the heat transfer rate into the control volume (positive in). Ẇ_shaft is the shaft work rate out (positive out — a turbine outputs positive shaft work; a pump or compressor inputs work, so Ẇ_shaft is negative). On the right, ṁ is the mass flow rate and h is specific **enthalpy**, which already bundles together internal energy and the flow work (Pv) that the fluid does pushing itself through the inlet and outlet. Kinetic energy ½V² and gravitational potential gz round out the mechanical contributions.

Different devices activate different terms. In a **nozzle** or **diffuser**, there is no shaft work and negligible heat transfer, so the equation reduces to a trade between enthalpy and kinetic energy: a nozzle converts enthalpy (pressure and temperature) into high-velocity flow, while a diffuser does the reverse. In a **turbine**, kinetic and potential energy changes are usually small, so nearly all the enthalpy drop appears as shaft work output. In a **pump or compressor**, shaft work drives the enthalpy rise. In a **heat exchanger**, no shaft work crosses the boundary, and kinetic/potential changes are negligible — enthalpy simply transfers from the hot stream to the cold stream. Recognizing which terms dominate in which device is the core engineering judgment skill.

The reason engineers use enthalpy rather than internal energy in this equation is precisely the flow work term. Every kilogram of fluid that enters the control volume must push the fluid ahead of it to make room — that work is P·v per unit mass and is absorbed into h = u + Pv. Using enthalpy means you never have to separately track this boundary-pushing work; it is already accounted for in the fluid's state. This is why steam tables list h so prominently: turbines, boilers, and condensers are all control volumes where enthalpy differences directly equal the heat or work per unit mass transferred.

The mass flow rate ṁ must satisfy **conservation of mass** (continuity) at steady state: ṁ_in = ṁ_out for a single-inlet, single-outlet device. For devices with multiple inlets or outlets (mixing chambers, splitting headers), mass must balance across all streams simultaneously. Applying continuity before the energy equation often reveals which velocities or state properties are constrained, narrowing the problem to a straightforward substitution into the energy balance.


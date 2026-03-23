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
stage: formal-systems
status: validated
---

# Control Volume Analysis and Steady-Flow Devices

## Core Idea
A control volume is a fixed region in space through which fluid flows; the steady-flow assumption means properties at each point don't change with time, though they may vary spatially. The control volume energy equation balances inlet and outlet enthalpy, kinetic energy, and potential energy with heat and shaft work. This is the dominant approach in engineering practice for analyzing most flow devices.

## Questions

```yaml
- question: "Steam enters a well-insulated turbine at high enthalpy h₁ and exits at lower enthalpy h₂. Kinetic and potential energy changes are negligible. What is the physical interpretation of the enthalpy drop (h₁ − h₂) per unit mass?"
  type: multiple-choice
  options:
    - "It equals the heat lost through the turbine's insulation to the surroundings"
    - "It equals the shaft work output per unit mass of steam flowing through the turbine"
    - "It represents the increase in the steam's internal energy while it is inside the turbine"
    - "It equals the kinetic energy the steam gains as it expands through the blades"
  answer: 1
  explanation: "For a steady-flow turbine with Q̇ ≈ 0 and negligible kinetic/potential changes, the energy equation simplifies to Ẇ_shaft = ṁ(h₁ − h₂), so the specific shaft work out equals h₁ − h₂. The turbine converts the enthalpy difference entirely into mechanical shaft output. Option A is wrong because the turbine is insulated (Q̇ = 0 by assumption). Option C is wrong because under steady-flow, there is no accumulation of internal energy inside the device — whatever enters must leave. Option D mistakes the nozzle case for the turbine case."

- question: "Why does the steady-flow energy equation use specific enthalpy h = u + Pv rather than specific internal energy u to represent the energy carried by each stream?"
  type: multiple-choice
  options:
    - "Enthalpy is always larger than internal energy, making engineering calculations more conservative"
    - "Enthalpy accounts for both the fluid's internal energy and the flow work (Pv) required to push each parcel of fluid through the inlet or outlet against the local pressure"
    - "Internal energy changes are negligible in most engineering devices, so enthalpy serves as a convenient approximation"
    - "Enthalpy is easier to measure directly with sensors than internal energy"
  answer: 1
  explanation: "Every kilogram of fluid entering a control volume must push the fluid ahead of it to make room — that work is exactly Pv per unit mass (pressure times specific volume). Using h = u + Pv bundles this 'flow work' term into the enthalpy so you never have to track it separately. This is why steam tables list h so prominently: turbines, boilers, condensers, and compressors are all open systems where the enthalpy differences directly represent the net energy exchange. Using u instead would give the wrong answer unless you separately added Pv at each boundary."

- question: "Under the steady-flow assumption, the thermodynamic properties (temperature, pressure, enthalpy) at any fixed point inside a control volume change continuously over time as fluid flows through."
  type: true-false
  answer: false
  explanation: "The steady-flow assumption means precisely the opposite: properties at any fixed spatial location inside the control volume do NOT change with time. Fluid is flowing and properties may vary from point to point spatially, but any given point maintains a constant state. This is what allows the energy balance to be written as a simple rate equation without accumulation terms. If properties were changing with time at fixed points, the system would be unsteady and the accumulation term d(E_cv)/dt would be nonzero, significantly complicating the analysis."

- question: "In a well-insulated converging nozzle, a drop in fluid enthalpy (due to falling pressure and temperature) must be accompanied by an increase in fluid velocity, because the steady-flow energy equation requires total energy to be conserved across the device."
  type: true-false
  answer: true
  explanation: "For a nozzle with Q̇ = 0, Ẇ_shaft = 0, and negligible elevation change, the energy equation reduces to h₁ + ½V₁² = h₂ + ½V₂². If h falls (h₂ < h₁), then ½V₂² must rise — the enthalpy decrease is exactly converted to kinetic energy increase. This is the design purpose of a nozzle: trade pressure/temperature for velocity. A diffuser does the reverse. The principle follows directly from energy conservation applied to a steady-flow open system."

- question: "Explain why engineers use enthalpy rather than internal energy in the steady-flow energy equation, and what physical quantity the Pv term represents."
  type: short-answer
  answer: "Pv represents 'flow work' — the work per unit mass that fluid at the inlet does pushing itself into the control volume against the existing pressure, and the work per unit mass the control volume does pushing fluid out at the outlet. Every kilogram crossing a boundary must displace its own volume against the local pressure. Using enthalpy h = u + Pv automatically accounts for this boundary-pushing work, so the energy balance only needs to track enthalpy differences between streams rather than separately computing internal energy plus two Pv terms at each port."
  explanation: "This is why open-system (control volume) analysis looks different from closed-system analysis even though both apply the first law. In a closed system, no mass crosses the boundary, so internal energy and heat/work are sufficient. In an open system, mass carries energy in two forms: its internal energy u and the flow work Pv needed to push it through the boundary. Enthalpy packages these together. The insight that 'flow work is already in h' is what makes steam tables so useful — you look up h at inlet and outlet conditions, subtract, and you have the work or heat per unit mass directly."
```

## Explainer

From your study of the first law for open systems, you know that energy can enter a control volume not just as heat and work, but also carried by mass flowing across the boundary. The **control volume** framework formalizes this: draw an imaginary boundary around a device (a turbine, a compressor, a nozzle, a heat exchanger), then account for every form of energy crossing that boundary per unit time. The **steady-flow assumption** is the key simplification — properties at any fixed point inside the boundary don't change with time, so there is no accumulation of internal energy inside the control volume. Whatever energy enters per second must equal whatever leaves per second.

Under steady-flow, the energy rate balance reduces to: Q̇ - Ẇ_shaft = ṁ [(h₂ - h₁) + ½(V₂² - V₁²) + g(z₂ - z₁)]. Read this term by term. Q̇ is the heat transfer rate into the control volume (positive in). Ẇ_shaft is the shaft work rate out (positive out — a turbine outputs positive shaft work; a pump or compressor inputs work, so Ẇ_shaft is negative). On the right, ṁ is the mass flow rate and h is specific **enthalpy**, which already bundles together internal energy and the flow work (Pv) that the fluid does pushing itself through the inlet and outlet. Kinetic energy ½V² and gravitational potential gz round out the mechanical contributions.

Different devices activate different terms. In a **nozzle** or **diffuser**, there is no shaft work and negligible heat transfer, so the equation reduces to a trade between enthalpy and kinetic energy: a nozzle converts enthalpy (pressure and temperature) into high-velocity flow, while a diffuser does the reverse. In a **turbine**, kinetic and potential energy changes are usually small, so nearly all the enthalpy drop appears as shaft work output. In a **pump or compressor**, shaft work drives the enthalpy rise. In a **heat exchanger**, no shaft work crosses the boundary, and kinetic/potential changes are negligible — enthalpy simply transfers from the hot stream to the cold stream. Recognizing which terms dominate in which device is the core engineering judgment skill.

The reason engineers use enthalpy rather than internal energy in this equation is precisely the flow work term. Every kilogram of fluid that enters the control volume must push the fluid ahead of it to make room — that work is P·v per unit mass and is absorbed into h = u + Pv. Using enthalpy means you never have to separately track this boundary-pushing work; it is already accounted for in the fluid's state. This is why steam tables list h so prominently: turbines, boilers, and condensers are all control volumes where enthalpy differences directly equal the heat or work per unit mass transferred.

The mass flow rate ṁ must satisfy **conservation of mass** (continuity) at steady state: ṁ_in = ṁ_out for a single-inlet, single-outlet device. For devices with multiple inlets or outlets (mixing chambers, splitting headers), mass must balance across all streams simultaneously. Applying continuity before the energy equation often reveals which velocities or state properties are constrained, narrowing the problem to a straightforward substitution into the energy balance.


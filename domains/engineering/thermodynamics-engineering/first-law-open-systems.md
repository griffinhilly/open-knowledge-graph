---
id: first-law-open-systems
title: First Law for Open Systems and Control Volumes
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-closed-systems
  type: hard
- id: thermodynamic-systems-engineering
  type: hard
- id: control-mass-first-law-applications
  type: soft
builds-toward:
- control-volume-steady-flow
- combustion-thermodynamic-analysis
tags:
- first-law
- open-systems
- control-volume
stage: formal-systems
status: validated
---
# First Law for Open Systems and Control Volumes

## Core Idea
The first law for open systems (control volumes) extends closed-system analysis by accounting for mass flow across boundaries, leading to the steady-flow energy equation. Each unit of mass carries enthalpy h with it into and out of the device, in addition to kinetic and potential energy. This framework enables analysis of pumps, turbines, compressors, and piping systems where fluid moves continuously through a device.

## How It's Best Learned
Derive the steady-flow energy equation from first principles by tracking mass and energy entering and leaving a control volume. Practice with devices where kinetic energy effects are small (turbines, compressors, heat exchangers) before tackling high-velocity flow. Recognize that enthalpy h = u + Pv naturally appears because flowing fluid must do flow work Pv to enter and exit the device.

## Common Misconceptions
- Internal energy u is relevant only to closed systems; enthalpy h = u + Pv combines internal and flow work for open systems.
- The steady-flow equation applies only to single-inlet, single-outlet devices; it generalizes to multiple inlets and outlets by summing mass and energy flows.
- Enthalpy is always greater than internal energy; at very low pressures, Pv becomes negligible and h ≈ u.

## Questions

```yaml
- question: "Why does enthalpy h = u + Pv appear in the steady-flow energy equation for open systems instead of internal energy u alone?"
  type: multiple-choice
  options:
    - "Enthalpy is easier to look up in steam tables than internal energy"
    - "Fluid crossing the control volume boundary must do flow work Pv to push against boundary pressure, so total energy transported per unit mass is u + Pv = h"
    - "The pressure and volume terms cancel with each other in the derivation, leaving only u"
    - "Enthalpy replaces internal energy only for incompressible liquids"
  answer: 1
  explanation: "Each parcel of fluid entering a control volume carries internal energy u but also does work Pv pushing the fluid column behind it across the boundary (flow work). Similarly, fluid leaving does flow work on what follows it. The total energy transported per unit mass is therefore u + Pv = h. This is a fundamental consequence of the open-system formulation, not merely a convenience."

- question: "For any steady-flow device, the kinetic and potential energy terms in the energy equation can always be safely neglected."
  type: true-false
  answer: false
  explanation: "Kinetic and potential energy terms are often small compared to enthalpy and heat/work terms in turbines and compressors, and neglecting them is a reasonable approximation there. But for nozzles and diffusers — designed specifically to convert enthalpy to kinetic energy or vice versa — the kinetic energy change is the entire point and cannot be neglected. Similarly, large elevation changes in hydraulic turbines make the potential energy term significant."

- question: "At steady state, what is the rate of change of energy stored inside a control volume, and what does this imply about the energy balance?"
  type: short-answer
  answer: "At steady state, dE_cv/dt = 0 — the energy stored inside the control volume does not change with time. This means energy in (via mass flow and heat transfer) exactly equals energy out (via mass flow and work output), reducing the first law to a balance of boundary flows rather than a storage equation."
  explanation: "The full open-system first law is dE_cv/dt = Q̇ − Ẇ + Σ(ṁh)_in − Σ(ṁh)_out. Setting dE_cv/dt = 0 for steady state eliminates the storage term and yields Q̇ − Ẇ = Σ(ṁh)_out − Σ(ṁh)_in (plus kinetic and potential terms). This steady-flow energy equation is the working tool for analyzing turbines, compressors, heat exchangers, and nozzles."
```

## Explainer

The first law for closed systems — ΔU = Q − W — tracks energy for a fixed mass of substance with no material crossing the boundary. Most real engineering devices (turbines, pumps, compressors, boilers) operate differently: fluid flows continuously in and out while the device itself reaches a steady operating state. Analyzing these requires extending the first law to open systems, or control volumes, where mass crosses the boundary.

The crucial difference from closed systems is that flowing mass carries energy with it. A parcel of fluid entering a device has internal energy u per unit mass, but it also does work pushing the fluid column behind it into the device — this is called flow work, and its magnitude is Pv per unit mass (pressure times specific volume). The total energy that each unit of mass transports across the boundary is therefore u + Pv, which is the definition of specific enthalpy h. This is not a coincidence or a definition of convenience; it is a direct consequence of writing the first law for a control volume with moving boundaries. Enthalpy h naturally replaces internal energy u in open-system analysis for exactly this reason.

For a single-inlet, single-outlet device at steady state, the energy equation becomes Q̇ − Ẇ_s = ṁ[(h₂ − h₁) + ½(V₂² − V₁²) + g(z₂ − z₁)], where Q̇ is the rate of heat transfer, Ẇ_s is shaft work (turbine output or pump input), and ṁ is the mass flow rate. The terms involving kinetic and potential energy can often be dropped for devices like turbines and compressors, where enthalpy changes dominate. But for nozzles and diffusers — designed specifically to exchange enthalpy for kinetic energy — those terms are the entire purpose and cannot be neglected.

The steady-state assumption (dE_cv/dt = 0) is what makes this equation algebraic rather than differential: the energy inventory inside the device does not change over time, so every joule flowing in must flow out in some form. In practice, "steady" means the device has reached its operating condition — temperature and pressure at each point are stable, and mass flow rate is constant. Startup transients, where the device heats up or pressurizes, require the full unsteady form of the control-volume energy equation. Most engineering analysis focuses on the steady-state operating point, making the steady-flow energy equation one of the most widely used tools in thermodynamic analysis.

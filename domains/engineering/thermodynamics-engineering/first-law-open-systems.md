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
builds-toward:
- control-volume-steady-flow
- combustion-thermodynamic-analysis
tags:
- first-law
- open-systems
- control-volume
stage: advanced
status: draft
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

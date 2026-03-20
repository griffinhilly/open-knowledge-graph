---
id: maxwell-stress-tensor
title: Maxwell Stress Tensor and Radiation Pressure
domain: physics
course: electrodynamics
prerequisites:
- id: poynting-vector-and-energy-flux
  type: hard
- id: maxwells-equations-integral-form
  type: soft
builds-toward:
- radiation-from-accelerated-charges
tags:
- stress
- momentum
- radiation-pressure
stage: advanced
status: draft
---

# Maxwell Stress Tensor and Radiation Pressure

## Core Idea
The Maxwell stress tensor T_ij encodes electromagnetic momentum density g = ε₀(E × B) and represents stresses exerted by fields. Radiation carries momentum and exerts pressure on absorbing surfaces. This provides a unified view of electromagnetic forces through momentum conservation.

## Explainer

You already know from the Poynting vector that electromagnetic fields carry energy flowing at rate S = (1/μ₀)E × B per unit area. A natural question follows: if electromagnetic waves carry energy, do they also carry momentum? The answer is yes — and the **Maxwell stress tensor** is the mathematical tool that makes momentum conservation in electromagnetic systems precise in exactly the same way that Poynting's theorem made energy conservation precise.

The **electromagnetic momentum density** is g = ε₀(E × B) = S/c², meaning the momentum stored per unit volume in the field is proportional to the energy flux divided by c². This is not merely an analogy to mechanical momentum — it is real momentum that can be transferred to matter. When a light wave hits an absorbing surface, it deposits momentum, producing a measurable **radiation pressure**: P = I/c for a perfectly absorbing surface (intensity divided by the speed of light) and P = 2I/c for a perfect reflector. The force from sunlight on a square meter of surface is tiny (about 5 micronewtons), but it is real — solar sail spacecraft use it for propulsion.

The **Maxwell stress tensor** T_ij is the object that systematizes this. Just as a mechanical stress tensor tells you the force per unit area exerted across a surface in a material, T_ij tells you the flux of the i-th component of electromagnetic momentum in the j-th direction. The total electromagnetic force on all matter inside a volume V can be written as a surface integral of T over the boundary: F_i = ∮ T_ij dAⱼ − d/dt ∫ gᵢ dV. The first term is the momentum flowing in through the surface; the second term is the rate of change of momentum stored in the fields inside. In steady state, the surface integral alone gives the force — you can calculate the force on any object (conductor, dielectric, current loop) by integrating the stress tensor over a surface enclosing it, without needing to know the microscopic charge distribution.

The conceptual payoff is unification: mechanical force, radiation pressure, and electromagnetic momentum are all aspects of a single conservation law for total (mechanical + field) momentum. Just as energy is conserved locally by Poynting's theorem, momentum is conserved locally by the stress tensor formulation. This framework extends naturally to radiation from accelerating charges and to the momentum carried by photons in quantum electrodynamics, where each photon carries momentum p = ħk = E/c — the macroscopic radiation pressure is just the classical average of countless photon impacts.

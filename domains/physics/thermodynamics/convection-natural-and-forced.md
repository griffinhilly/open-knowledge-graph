---
id: convection-natural-and-forced
title: 'Convective Heat Transfer: Natural and Forced'
domain: physics
course: thermodynamics
prerequisites:
- id: heat-transfer-conduction-fourier
  type: soft
tags:
- heat-transfer
- convection
- fluid-motion
stage: formal-systems
status: draft
---

# Convective Heat Transfer: Natural and Forced

## Core Idea
Convection transfers heat through the motion of a fluid (liquid or gas). Natural convection arises from density differences due to heating; forced convection uses external means (fans, pumps). The heat transfer rate is proportional to surface area and temperature difference, characterized by a convection coefficient h.

## Explainer

From your study of conduction, you know that heat flows through stationary matter by molecular diffusion — governed by Fourier's law, Q̇ = −kA(dT/dx). Convection is fundamentally different: heat is carried not by molecular diffusion alone but by the **bulk motion of the fluid itself**. Warm fluid near a hot surface expands, becomes less dense, rises (or moves), and is replaced by cooler fluid — this continuous renewal is what makes convection so much more efficient than conduction for most engineering applications.

In **forced convection**, an external agent drives the flow: a pump moves coolant through a pipe, a fan blows air over a circuit board, or a car moves through air. The heat transfer rate obeys **Newton's law of cooling**: Q̇ = hA(T_s − T_∞), where T_s is the surface temperature, T_∞ is the bulk fluid temperature far from the surface, A is the surface area, and h is the **convection coefficient** (also called the heat transfer coefficient). The coefficient h is the key quantity — it encodes everything about the fluid flow pattern, fluid properties, and geometry. It is not a material property like thermal conductivity; it depends on velocity, fluid viscosity, density, specific heat, and the geometry of the surface. Typical values range from ~10 W/(m²·K) for free air to ~10,000 W/(m²·K) for boiling water.

In **natural (free) convection**, the fluid motion is driven entirely by buoyancy — the density variation caused by the temperature difference itself. Heated fluid near the surface expands and rises; cooler, denser fluid sinks to take its place. The driving force is the buoyancy force ρgβΔT (where β is the thermal expansion coefficient), balanced by viscous drag. The characteristic dimensionless number is the **Grashof number** Gr = gβΔTL³/ν², the ratio of buoyancy to viscous forces. Compare this to forced convection's Reynolds number Re = ρVL/μ. When Gr/Re² ≫ 1, natural convection dominates; when Gr/Re² ≪ 1, forced convection dominates; when they are comparable, both matter and the situation is mixed.

The convection coefficient h is typically determined experimentally or via dimensional analysis using the **Nusselt number** Nu = hL/k_fluid — the ratio of total heat transfer to what conduction alone would give. Empirical correlations express Nu as a function of the relevant dimensionless groups: Nu = C Re^m Pr^n for forced convection, or Nu = C (Gr·Pr)^n for natural convection, where **Prandtl number** Pr = ν/α = (viscous diffusivity)/(thermal diffusivity) characterizes the fluid. Water has Pr ≈ 7 (thermal boundary layer thinner than velocity boundary layer), air has Pr ≈ 0.7, oils can have Pr > 100. These correlations are the engineer's practical tool: measure or estimate the flow conditions, look up the correlation, compute h, and Newton's law of cooling gives you the heat transfer rate.

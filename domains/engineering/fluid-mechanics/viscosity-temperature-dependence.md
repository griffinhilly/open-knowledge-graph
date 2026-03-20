---
id: viscosity-temperature-dependence
title: Viscosity-Temperature Dependence
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-properties-and-continuum
  type: hard
builds-toward:
- laminar-turbulent-transition-critical-reynolds
- darcy-weisbach-equation-application
tags:
- viscosity
- temperature
- thermophysical-properties
stage: advanced
status: draft
---

# Viscosity-Temperature Dependence

## Core Idea
Viscosity depends strongly on temperature and changes differently for liquids versus gases. For liquids, viscosity decreases exponentially as temperature increases due to reduced intermolecular forces. For gases, viscosity increases with temperature because higher molecular velocities increase momentum transfer. Accurate prediction of viscosity across operating temperature ranges is essential for design calculations.

## Explainer

From your study of fluid properties, you know that **dynamic viscosity** μ is the fluid's resistance to shearing — it is the proportionality constant between shear stress and velocity gradient (Newton's law of viscosity: τ = μ du/dy). But viscosity is not a fixed number; it is a thermophysical property that changes substantially with temperature. The direction and magnitude of that change depends on the molecular mechanism responsible for viscosity, and liquids and gases behave in completely opposite ways.

In a **liquid**, molecules are densely packed and viscosity arises primarily from intermolecular cohesive forces — the short-range attractions that try to hold neighboring molecules together and resist their sliding past one another. When temperature rises, molecules gain kinetic energy and can overcome these attractive forces more easily. The cohesive resistance weakens, and the fluid flows more readily. The viscosity of a liquid typically follows an Arrhenius-type relationship: μ = A exp(B/T), where T is absolute temperature. The result is a steep, roughly exponential decrease. Engine oil at 20°C is perhaps 50 times more viscous than at 100°C — a factor-of-50 change over the operating range of a car engine. This is why oil must be matched to operating temperatures and why cold-start lubrication is a design challenge.

In a **gas**, molecules are widely separated and intermolecular forces are negligible. Gas viscosity arises from a different mechanism: the **momentum transfer** between adjacent fluid layers by molecules randomly crossing from one layer to the other. A molecule moving from a fast layer to a slow one carries extra momentum, which it imparts through collisions — effectively dragging the slow layer forward. Higher temperature means faster molecules moving more frequently and carrying more momentum per crossing. Therefore gas viscosity **increases** with temperature, following Sutherland's correlation: μ/μ_ref = (T/T_ref)^(3/2) × (T_ref + S)/(T + S), where S is the Sutherland constant. The effect is modest — air at 300 K has viscosity about 1.5× higher than at 100 K — and far smaller in magnitude than the liquid-phase changes.

These opposing behaviors have direct engineering consequences. When you calculate Reynolds number Re = ρVD/μ for a gas flowing through a heated duct, rising temperature increases μ, which decreases Re — the flow is less turbulent than a naive constant-viscosity estimate would predict. For a liquid-cooled system, falling liquid viscosity at higher temperatures means lower pumping power but also changes heat transfer coefficients. In both cases, using the correct temperature-dependent viscosity — evaluated at the local fluid temperature, not a nominal inlet value — is essential for accurate friction factor calculations, flow distribution predictions, and sizing of pumps and compressors.

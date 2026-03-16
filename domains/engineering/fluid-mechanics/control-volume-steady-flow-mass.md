---
id: control-volume-steady-flow-mass
title: 'Control Volume Analysis: Mass Balance'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: continuity-equation-fluid
  type: hard
builds-toward:
- control-volume-momentum-applications
- mechanical-energy-balance-pump-turbine
tags:
- control-volume
- conservation
- continuity
- mass-flow
stage: formal-systems
status: draft
---

# Control Volume Analysis: Mass Balance

## Core Idea
The continuity equation for steady flow states that mass flow rate in equals mass flow rate out for a control volume. Extended to multiple inlets and outlets, Σ(ṁ_in) = Σ(ṁ_out). This fundamental conservation principle applies to all fluid systems regardless of complexity and forms the basis for solving incompressible flow problems with varying areas and velocities.

## Explainer

The **control volume** method is an accounting framework. You draw an imaginary boundary around any region of space — a pipe section, a pump, a valve, the interior of a nozzle — and then track what crosses that boundary. You already know from the continuity equation that mass is conserved everywhere in a flow field. The control volume approach takes that local statement and turns it into a global accounting tool: instead of tracking every fluid particle, you only watch what enters and exits the boundary you chose.

For **steady flow**, the key simplification is that nothing accumulates inside the control volume. The density and velocity fields inside are frozen in time. Whatever mass flows in must flow out at exactly the same rate. This gives you Σ(ṁ_in) = Σ(ṁ_out), where **mass flow rate** ṁ = ρAV at each port: density times cross-sectional area times average velocity. If the geometry is simple — one inlet, one outlet — this reduces to ρ₁A₁V₁ = ρ₂A₂V₂.

The real power appears when the geometry is complex. Consider a T-junction where one inlet pipe splits into two outlet branches. You don't need to solve the flow field inside the junction. You only need to know that ṁ_in = ṁ_out,1 + ṁ_out,2. You can solve for an unknown velocity or area in one branch given the other quantities. The interior of the control volume is a black box — only the boundary values matter for the mass balance.

For **incompressible** flows (liquids, and gases at low Mach number), density is constant, so mass conservation becomes **volume flow rate** conservation: Q_in = Q_out, where Q = AV. This is why a pipe that narrows must have higher velocity at the narrow section: A decreases, so V must increase to keep Q constant. The nozzle accelerates flow and the diffuser decelerates it — both follow directly from this single conservation statement. Most hydraulic engineering problems reduce to applying this principle systematically at each junction and section in a network.

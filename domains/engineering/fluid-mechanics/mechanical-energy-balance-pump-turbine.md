---
id: mechanical-energy-balance-pump-turbine
title: Mechanical Energy Balance with Pump and Turbine Work
domain: engineering
course: fluid-mechanics
prerequisites:
- id: first-law-open-systems
  type: hard
- id: bernoulli-real-fluid-limitations
  type: hard
builds-toward:
- centrifugal-pump-curves-selection
- pipe-network-solutions-hardy-cross
tags:
- energy-equation
- pump-work
- turbine-work
- head
stage: advanced
status: draft
---

# Mechanical Energy Balance with Pump and Turbine Work

## Core Idea
The steady-flow mechanical energy equation (p₁/ρg + v₁²/2g + z₁ + H_pump = p₂/ρg + v₂²/2g + z₂ + H_turbine + H_loss) extends Bernoulli to include work interactions and irreversibilities. Pump head and turbine head represent useful work transfer; head loss represents energy dissipated as heat by viscous friction. This equation is the foundation for all piping system design.

## Explainer

You already know that Bernoulli's equation is an energy balance along a streamline for an ideal, inviscid fluid: pressure energy, kinetic energy, and potential energy trade off while their sum stays constant. But Bernoulli breaks down when the fluid passes through a machine (pump or turbine) or when friction is significant. The mechanical energy equation is the corrected version: it adds terms for work added by pumps, work extracted by turbines, and energy destroyed by friction — all expressed in the same units of length called **head**.

**Head** is the most important concept here. By dividing each energy term by ρg, you convert joules per kilogram into meters — a "height equivalent" of energy. Pressure head (P/ρg) is the height a column of fluid would reach if all pressure energy were converted to elevation. Velocity head (V²/2g) is the equivalent height for kinetic energy. Elevation head z is the actual height. **Pump head** H_pump is the mechanical energy added to the fluid per unit weight of fluid — it increases the total head at the pump discharge. **Turbine head** H_turbine is the energy extracted. **Head loss** H_loss is energy permanently destroyed by viscous friction and converted to heat; it always appears on the right side of the equation because you always lose it, regardless of which way you write the balance.

The equation p₁/ρg + V₁²/2g + z₁ + H_pump = p₂/ρg + V₂²/2g + z₂ + H_turbine + H_loss reads as: total head at inlet, plus any head added by a pump, equals total head at outlet, plus any head extracted by a turbine, plus all head losses in between. This is an accounting statement: every joule of energy that enters a control volume must go somewhere. To use it in a piping system problem, pick two points (usually where conditions are known, like tank surfaces), write the equation, and solve for the unknown — typically pump head, flow rate, or pressure at some point.

The power required by or delivered by a machine follows directly from the head: P = ρgQH, where Q is volumetric flow rate. This connects the hydraulic head concept back to the first-law open-system analysis you learned earlier — power is the rate of energy transfer. Real pumps and turbines have efficiencies less than 1, so the shaft power input to a pump is P_shaft = ρgQH_pump/η_pump, and the shaft power output from a turbine is P_shaft = η_turbine · ρgQH_turbine. Correctly applying this equation is what allows engineers to size pumps for water distribution systems, calculate hydroelectric power output, or determine whether a pipe network can deliver the required flow rate.

---
id: heat-transfer-convection
title: 'Heat Transfer: Convection'
domain: physics
course: thermodynamics
prerequisites:
- id: heat-transfer-conduction
  type: soft
tags:
- convection
- heat-transfer
- fluid-flow
- natural-convection
- forced-convection
stage: concrete-operations
status: validated
---

# Heat Transfer: Convection

## Core Idea
Convection is heat transfer by the bulk movement of a fluid (liquid or gas). In natural convection, temperature-driven density differences cause fluid to circulate — warm fluid rises and cool fluid sinks. In forced convection, a pump or fan drives the flow, enhancing transfer rates. The convective heat transfer rate is approximately P = hAΔT, where h is the convection coefficient depending on fluid properties and flow conditions.

## Common Misconceptions
- Convection requires a fluid medium — it cannot occur in a solid or in a vacuum.
- Hot air rising is often described as the primary mechanism, but the driving force is pressure differences caused by density gradients, not simply 'lightness'.

## Explainer

From your study of heat conduction, you know that conduction transfers heat through a material by molecular collisions, without bulk movement of the material itself — the molecules vibrate in place and pass energy to neighbors. Convection is categorically different: the fluid itself moves, carrying thermal energy with it as bulk flow. A warm parcel of water rising in a pot, or a warm air mass circulating in a room, transports enthalpy bodily from hot regions to cold ones. This makes convection far more effective than conduction in fluids, because the thermal conductivity of gases and liquids is generally low, but their capacity to carry energy by flow is high.

**Natural (free) convection** is driven by buoyancy — the tendency of less-dense fluid to rise relative to denser fluid. When a fluid is heated, it expands and its density decreases. Gravity pulls denser fluid downward, displacing lighter fluid upward. This sets up a circulation pattern: near a hot surface, fluid heats up, becomes less dense, rises, carries heat away, cools, becomes denser, and descends to repeat the cycle. The driving force is not simply that "hot air is light" — it is that a density gradient in a gravitational field creates a pressure gradient that drives flow. The strength of natural convection depends on the temperature difference ΔT, the gravitational acceleration g, the coefficient of thermal expansion β, and the fluid's kinematic viscosity and thermal diffusivity, combined into the dimensionless **Rayleigh number** Ra = gβΔT L³/(νκ). When Ra exceeds a critical threshold (~10³), convection becomes vigorous; below it, conduction dominates.

**Forced convection** uses a pump, fan, or external flow to drive fluid over a surface, regardless of buoyancy effects. A cooling fan on a computer chip blows air over the hot surface; the chip heats that thin boundary layer of air, which is swept away and replaced by fresh cool air. Forced convection is far more controllable and typically more powerful than natural convection. The governing equation in both cases is **Newton's law of cooling**: Q̇ = h A ΔT, where Q̇ is the heat transfer rate, A is the surface area, ΔT is the temperature difference between surface and fluid, and h is the **convection coefficient** (W/m²·K). The deceptively simple appearance of this equation hides all the complexity in h, which depends on fluid properties (viscosity, conductivity, density, specific heat), flow geometry, and flow velocity. Doubling the fan speed does not simply double h — h scales roughly as flow velocity to some fractional power, typically 0.5–0.8, depending on the geometry and flow regime.

The convection coefficient h is determined by the thin **boundary layer** of fluid immediately adjacent to the surface, where viscous effects slow the flow and heat must cross by conduction to reach the bulk fluid. Fast external flow thins the boundary layer and steepens the temperature gradient within it, increasing the local heat flux even though the bulk temperature difference ΔT is unchanged. This is why a breeze feels cooling even when air temperature is constant: faster flow thins the boundary layer, increasing h and hence Q̇. In engineering heat transfer, correlations between dimensionless numbers (Nusselt, Reynolds, Prandtl numbers) tabulate h for standard geometries, allowing engineers to predict cooling performance without solving the full fluid dynamics equations. These correlations are the practical legacy of convection physics: the physical picture of boundary layers and flow-driven heat transport translated into design-ready formulas.

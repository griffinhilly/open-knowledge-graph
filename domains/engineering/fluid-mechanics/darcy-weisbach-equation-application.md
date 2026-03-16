---
id: darcy-weisbach-equation-application
title: 'Darcy-Weisbach Equation: Major Head Loss Calculation'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: laminar-pipe-flow
  type: hard
- id: turbulent-pipe-flow
  type: hard
- id: mechanical-energy-balance-pump-turbine
  type: hard
builds-toward:
- friction-factor-determination-methods
- pipe-network-solutions-hardy-cross
tags:
- head-loss
- friction
- pipe-flow
- energy
stage: formal-systems
status: draft
---

# Darcy-Weisbach Equation: Major Head Loss Calculation

## Core Idea
The Darcy-Weisbach equation, H_loss = f(L/D)(V²/2g), quantifies major (friction) head loss in pipes. The friction factor f depends on Reynolds number and relative roughness. This equation is universal for all pipe diameters, lengths, and flow velocities, making it the standard tool for piping system calculations in industry and engineering practice.

## Explainer

When real fluid flows through a pipe, some of the mechanical energy is permanently lost to viscous friction and turbulent dissipation — this is **major head loss**, or friction head loss. Your prerequisite on the mechanical energy balance extended the Bernoulli equation for real fluids by adding a head loss term H_loss on the right side: energy added by pumps minus energy extracted by turbines minus friction losses equals the net change in fluid mechanical energy. The Darcy-Weisbach equation gives you the precise value to substitute for H_loss.

The equation H_loss = f(L/D)(V²/2g) has a clear physical structure. The term V²/2g is the **velocity head** — the kinetic energy per unit weight of fluid, measured in meters of fluid column. The ratio L/D counts how many pipe diameters the fluid has traveled; a 5 m pipe with a 25 mm diameter has L/D = 200, meaning the fluid has traversed 200 pipe diameters of frictional surface. The **Darcy friction factor** f scales these together and encapsulates the effect of flow regime and pipe roughness. Head loss grows linearly with pipe length and inversely with diameter — a pipe twice as long loses twice the head, and a pipe twice as wide at the same velocity loses half the head.

The friction factor f is where your prerequisites on laminar and turbulent pipe flow become essential. For laminar flow (Re < 2300), theory yields f = 64/Re exactly — the smoother the laminar layers, the less friction, regardless of pipe wall roughness. For turbulent flow (Re > 4000), you must use the **Moody diagram** (or the Colebrook equation it represents), which shows f as a function of both Reynolds number and **relative roughness** ε/D, where ε is the average wall roughness height. At moderate Reynolds numbers, viscous effects damp out roughness contributions; at very high Reynolds numbers, f flattens to a constant set by ε/D alone — the "fully rough" regime where the roughness peaks protrude through the viscous sublayer and dominate friction.

The universality of Darcy-Weisbach is what makes it the engineering standard. Whether the fluid is water or crude oil, the pipe is 12 mm or 1.2 m in diameter, flow is laminar or fully turbulent — the same equation applies. You simply look up or calculate the appropriate f. Because head loss is expressed in meters of fluid rather than pascals, it is independent of fluid density and adds directly to the Bernoulli terms. A piping network calculation — sizing pumps, checking if flow rates are achievable, comparing parallel and series pipe branches — reduces to writing energy equations between nodes with Darcy-Weisbach supplying each pipe's friction term.

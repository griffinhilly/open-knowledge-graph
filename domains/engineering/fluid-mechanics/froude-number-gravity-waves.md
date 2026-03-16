---
id: froude-number-gravity-waves
title: Froude Number and Gravity Wave Propagation
domain: engineering
course: fluid-mechanics
prerequisites:
- id: dimensional-analysis-and-similarity
  type: hard
- id: open-channel-flow
  type: hard
tags:
- froude-number
- surface-waves
- open-channel
stage: formal-systems
status: draft
---

# Froude Number and Gravity Wave Propagation

## Core Idea
The Froude number, Fr = V/√(gh), compares flow velocity to surface wave speed. For Fr < 1 (subcritical), gravity waves propagate upstream and control upstream boundary conditions. For Fr > 1 (supercritical), waves cannot propagate upstream and flow is controlled by downstream conditions. The transition at Fr = 1 produces a hydraulic jump—essential concepts for spillway design and open channel flow control.

## Explainer

From your study of dimensional analysis, you know that dimensionless groups compress the relevant physics of a problem into a single ratio. The **Froude number** Fr = V/√(gD) is the group that governs free-surface flows — rivers, spillways, canals, and any flow with an air-water interface. It compares the local flow velocity V to the speed at which small gravity waves propagate on the surface, c = √(gD), where D is the depth. This ratio controls everything about open-channel hydraulics: which boundary conditions matter, whether disturbances can travel upstream, and whether flow transitions occur smoothly or violently.

Think of it this way: a gravity wave is information. When you throw a pebble into still water, ripples propagate outward in all directions at speed c. In a moving stream, those ripples still propagate at speed c relative to the water, but the water itself is moving at speed V. If V < c (Fr < 1), ripples can still move upstream relative to the ground — the flow is **subcritical** (also called tranquil). Downstream conditions can send signals upstream and influence the flow. If V > c (Fr > 1), ripples are swept downstream faster than they can propagate upstream — the flow is **supercritical** (also called rapid). Downstream conditions have no upstream influence. The boundary Fr = 1 is called **critical flow**, the condition at which a small wave is stationary relative to the ground. This is precisely analogous to the Mach number in compressible flow: in subsonic flow pressure disturbances propagate upstream; in supersonic flow they cannot.

The most dramatic consequence of this physics is the **hydraulic jump**: when a supercritical flow is forced to transition to subcritical — for example, when a high-velocity jet off a spillway meets the deeper, slower-moving water downstream — the transition cannot occur smoothly because no gradual upstream information exchange is possible. Instead, the flow undergoes an abrupt, turbulent jump in which depth increases sharply, velocity drops, and a significant fraction of kinetic energy is dissipated as heat and turbulence. Hydraulic jumps are deliberately designed into stilling basins below dams to dissipate energy harmlessly before flow re-enters a downstream channel. The Froude number of the incoming supercritical flow determines how strong the jump is and how much energy is dissipated.

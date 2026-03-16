---
id: isentropic-nozzle-flow-choked-conditions
title: Isentropic Nozzle Flow and Choked Conditions
domain: engineering
course: fluid-mechanics
prerequisites:
- id: compressible-flow-isentropic-flow
  type: hard
- id: continuity-equation-fluid
  type: hard
- id: mach-number-speed-of-sound-compressibility
  type: soft
tags:
- nozzle
- choked
- sonic
stage: formal-systems
status: draft
---

# Isentropic Nozzle Flow and Choked Conditions

## Core Idea
In isentropic nozzle flow, the area-Mach relation governs acceleration: smaller area accelerates subsonic flow to higher M; beyond sonic conditions at the throat, a diverging section further accelerates supersonic flow. Choked flow occurs when the throat reaches sonic conditions (M = 1), after which downstream pressure changes do not affect the mass flow rate. This principle limits the thrust of rockets and the delivery rate of compressed gases.

## How It's Best Learned
Analyze converging-only nozzles where choked flow limits mass flow versus converging-diverging nozzles where supersonic flow is achieved. Calculate throat area, exit Mach number, and pressure for given inlet stagnation conditions and back-pressures to observe the transition to choked behavior.

## Explainer

From your study of isentropic flow, you know that the relationship between flow velocity and cross-sectional area is not the same in compressible flow as in the incompressible flows you may have encountered earlier. For subsonic compressible flow, contracting the duct still accelerates the fluid — as you'd expect from continuity. But the governing area-Mach relation, A/A* = (1/M)[(2/(γ+1))(1 + (γ−1)/2 · M²)]^((γ+1)/(2(γ−1))}, reveals a critical feature: the area reaches its minimum when M = 1, the **sonic condition**. Below that Mach number, decreasing area increases velocity. Above it, increasing area is required to continue accelerating the flow. This counterintuitive behavior in the supersonic regime follows from the fact that at high speeds, density drops faster than the area decreases, so the duct must widen to carry the same mass flow.

This geometry constraint defines the **converging-diverging nozzle**. A converging section accelerates subsonic flow toward sonic conditions at the minimum area location — the **throat**. If conditions are right, a diverging section then continues accelerating the flow into the supersonic regime. The key word is "if." Whether supersonic flow actually occurs downstream depends on the **back pressure** — the pressure at the nozzle exit imposed by the downstream environment. If the back pressure is above a critical value, the flow remains subsonic throughout and the nozzle behaves like a venturi. Only when the back pressure is sufficiently reduced does a supersonic solution appear downstream of the throat.

**Choked flow** occurs when the throat velocity reaches exactly M = 1. At this point, the mass flow rate through the nozzle has reached its maximum possible value for the given inlet stagnation conditions and throat area. Physically, information in a compressible fluid propagates at the local speed of sound. Once the throat is sonic, no pressure disturbance from the downstream environment can propagate upstream against the sonic flow — the upstream flow is effectively isolated from what happens downstream. This is why reducing back pressure further, below the choking threshold, does not increase mass flow: the throat is already at its maximum delivery rate.

The practical consequences are significant. Aircraft engine inlet design, rocket nozzles, and pressure-relief valves all depend on choked flow for predictable performance. In a rocket, the throat area and inlet stagnation temperature and pressure set the mass flow and therefore the thrust, regardless of ambient conditions at altitude. For industrial gas systems, a choked orifice acts as a metering device: mass flow is set by upstream pressure and temperature alone, decoupled from downstream variations. The converging-diverging geometry is thus not just a way to reach supersonic speed — it is a mechanism for flow control through geometric design.

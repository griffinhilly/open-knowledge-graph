---
id: isentropic-flow-with-area-change
title: Isentropic Flow with Area Change and Nozzles
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: compressible-flow-isentropic-flow
  type: hard
- id: compressible-flow-thermodynamic-relations
  type: hard
builds-toward:
- shock-waves-compressible-flow-analysis
tags:
- isentropic-flow
- area-change
- mach-number
- nozzles
stage: advanced
status: draft
---

# Isentropic Flow with Area Change and Nozzles

## Core Idea
For isentropic flow, the area-Mach relationship dA/A = -(1 - M²) dV/V determines flow behavior: converging sections accelerate subsonic flow and decelerate supersonic flow; diverging sections do the opposite. Sonic condition (M = 1) occurs only at a throat. This principle is fundamental in jet engines, compressor design, and supersonic wind tunnels.

## Explainer

From your study of isentropic flow relations, you know that for an ideal compressible flow with no heat transfer or friction, total pressure and total temperature are conserved. Introducing a changing cross-sectional area creates a coupling between geometry and Mach number that produces one of the most counterintuitive results in engineering: **a converging duct accelerates subsonic flow but decelerates supersonic flow, while a diverging duct does the opposite.** This contradicts everyday intuition shaped by low-speed (incompressible) flows, where a narrowing always speeds up the fluid.

The explanation comes from the governing area-velocity relation derived from continuity and the momentum equation: dA/A = (M² − 1) · dV/V. At subsonic speeds (M < 1), the factor (M² − 1) is negative, so area and velocity change in opposite directions — narrowing accelerates, widening decelerates. Exactly as you expect from a garden hose. But at supersonic speeds (M > 1), (M² − 1) is positive, so area and velocity change in the *same* direction — widening accelerates, narrowing decelerates. The physics is that at supersonic speeds, density drops so fast with increasing velocity that the flow must spread into a larger area to maintain mass continuity. The density effect dominates over the velocity effect.

The **throat** — the minimum-area cross-section — is where sonic conditions (M = 1) can occur. At M = 1, the factor (M² − 1) = 0, which requires dA = 0: sonic flow can only exist at a location where the area is at a local minimum or maximum. In practice, this means M = 1 occurs at a throat, and it can only be achieved there if the pressure ratio across the nozzle is large enough to "choke" the flow. A **converging-diverging nozzle** (de Laval nozzle) exploits this: subsonic flow in the converging section reaches M = 1 at the throat, then the diverging section accelerates it to supersonic speeds. This is exactly the geometry of rocket nozzles and supersonic wind tunnel test sections.

The isentropic area-Mach relation A/A* = f(M) — derived from the isentropic flow equations you already know — gives the required area ratio to reach any Mach number. Here A* is the throat area (the area at M = 1). Notice that A/A* > 1 for both subsonic and supersonic flow: a given area ratio corresponds to *two* possible Mach numbers, one below and one above 1. Which solution applies depends on the pressure boundary conditions. This duality is not a mathematical quirk — it reflects two physically distinct flow regimes that a nozzle can operate in depending on the downstream pressure, and selecting the right solution is a critical design step for any compressible flow device.

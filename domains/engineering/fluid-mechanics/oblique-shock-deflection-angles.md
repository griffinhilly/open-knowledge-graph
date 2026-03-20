---
id: oblique-shock-deflection-angles
title: 'Oblique Shock Waves: Deflection Angle Relations'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: normal-shock-pressure-temperature-relations
  type: hard
tags:
- shocks
- deflection
- supersonic
stage: advanced
status: draft
---

# Oblique Shock Waves: Deflection Angle Relations

## Core Idea
Oblique shocks form when supersonic flow encounters a corner or deflection, with shock angle θ and flow deflection angle δ related through the θ-β-M relation. For a given Mach number and deflection angle, two solutions (weak and strong shocks) may exist. Understanding oblique shock behavior is essential for designing supersonic inlets, nozzles, and control surfaces where flow deflection is unavoidable.

## Explainer

From your study of normal shocks, you know what happens when supersonic flow hits a wall head-on: a strong discontinuity forms, and the flow decelerates to subsonic speed with large pressure, temperature, and entropy increases. But in practice, supersonic flow rarely meets a perfectly perpendicular wall. When a flat surface is inclined — a wedge nose, a deflected control surface, a supersonic inlet ramp — the shock tilts at an angle and much of the Mach number survives. This is the **oblique shock**, and the key insight is that it reduces to a normal shock problem once you decompose the velocity correctly.

Let the oblique shock be inclined at **wave angle** β to the incoming flow (M_1). Decompose the upstream velocity into a component normal to the shock (M_{n1} = M_1 sin β) and a component tangential to the shock (M_t = M_1 cos β). The tangential component is unchanged across the shock — there is no pressure gradient driving it. Only the normal component experiences the shock. So apply all the normal shock relations you already know, but using M_{n1} instead of M_1: you get the normal Mach number downstream M_{n2}, and the corresponding pressure, temperature, and density ratios. The downstream Mach number is then reconstructed as M_2 = M_{n2} / sin(β − δ), where **deflection angle** δ is how much the flow turns toward the wall.

The θ-β-M relation connects the three: tan(δ) = 2 cot(β) [M_1² sin²(β) − 1] / [M_1²(γ + cos 2β) + 2]. For a given M_1 and required flow deflection δ, this equation typically has two solutions: a **weak shock** (smaller β, flow may remain supersonic) and a **strong shock** (larger β, flow is subsonic downstream). In practice, nature selects the weak shock unless a downstream boundary condition forces the strong solution. There is also a **maximum deflection angle** δ_max for each M_1 — if the wall turns more sharply than this, no attached oblique shock can form and a detached **bow shock** stands off the body, with a normal shock at the centerline and increasingly oblique portions away from the axis.

This framework is indispensable for supersonic inlet design. Rather than accepting one strong normal shock (maximum total pressure loss), engineers use a series of oblique shocks to decelerate the flow incrementally, each one weaker than the last. Each oblique shock carries less entropy rise than an equivalent normal shock. The theoretical optimum — infinitely many infinitely weak oblique shocks — is the **isentropic compression**, approximated in practice by curved ramps. Understanding the β-δ-M geometry lets you calculate exactly how much total pressure recovery each ramp configuration provides and how to prevent the flow from detaching.

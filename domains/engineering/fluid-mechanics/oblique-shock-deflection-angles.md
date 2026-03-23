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
stage: formal-systems
status: validated
---

# Oblique Shock Waves: Deflection Angle Relations

## Core Idea
Oblique shocks form when supersonic flow encounters a corner or deflection, with shock angle θ and flow deflection angle δ related through the θ-β-M relation. For a given Mach number and deflection angle, two solutions (weak and strong shocks) may exist. Understanding oblique shock behavior is essential for designing supersonic inlets, nozzles, and control surfaces where flow deflection is unavoidable.

## Questions

```yaml
- question: "Supersonic flow at M = 3.0 encounters a wedge. The θ-β-M relation yields two mathematically valid shock angles for the given deflection. In the absence of a downstream constraint forcing a specific solution, which shock will form?"
  type: multiple-choice
  options:
    - "The strong shock, because stronger shocks are more stable under supersonic conditions"
    - "The weak shock, because nature minimizes entropy production wherever possible"
    - "A standing normal shock, since the wedge geometry forces the flow to decelerate fully"
    - "Neither solution is stable; a detached bow shock always forms at M = 3.0"
  answer: 1
  explanation: "Nature selects the weak shock (smaller wave angle β) in the vast majority of practical cases. The weak shock leaves the downstream flow closer to (or at) supersonic speed and corresponds to a lower entropy rise. A strong shock solution exists mathematically but requires a specific downstream pressure condition — such as a closed duct — to be forced. Detached bow shocks only form when the deflection angle exceeds the maximum possible for the given Mach number (δ > δ_max), not for all wedge geometries."

- question: "In an oblique shock analysis, how is the pressure ratio across the shock calculated?"
  type: multiple-choice
  options:
    - "Use normal shock tables directly with the full upstream Mach number M₁"
    - "Decompose M₁ into normal and tangential components; apply normal shock relations to the normal component M_{n1} = M₁ sin β"
    - "The pressure ratio across an oblique shock equals one, since the tangential component dominates"
    - "Multiply the normal shock pressure ratio by cos²β to account for the oblique geometry"
  answer: 1
  explanation: "This is the key insight: the tangential velocity component is unchanged across the shock (no pressure gradient drives it), so only the normal component experiences the shock transition. By substituting M_{n1} = M₁ sin β into the standard normal shock pressure ratio formula, you recover the correct oblique shock result. This decomposition reduces the oblique shock problem to a normal shock problem — all the normal shock relations and tables you already know apply directly to the normal Mach number."

- question: "Flow through an oblique shock always decelerates to subsonic speed, just as flow through a normal shock does."
  type: true-false
  answer: false
  explanation: "This is a critical distinction between normal and oblique shocks. A normal shock always decelerates supersonic flow to subsonic speed. An oblique shock (specifically the weak solution) often leaves the downstream flow supersonic — it merely reduces the Mach number. The downstream Mach number M₂ = M_{n2} / sin(β − δ) can be greater than 1 for weak shocks. This is why oblique shocks are useful in inlet design: a series of oblique shocks can gradually decelerate supersonic flow while keeping it supersonic throughout, until a final, weaker shock transitions to subsonic."

- question: "An oblique shock can be fully analyzed using normal shock relations by substituting the component of the upstream Mach number normal to the shock wave."
  type: true-false
  answer: true
  explanation: "Yes — this is the fundamental insight of oblique shock analysis. Because the tangential velocity is unchanged across the shock (no tangential pressure gradient), the shock only 'sees' the normal component of the incoming flow. All normal shock relations (pressure ratio, temperature ratio, density ratio, downstream Mach number) hold exactly when M₁ is replaced by M_{n1} = M₁ sin β. The downstream quantities are then reconstructed using the geometry of the deflection angle δ. This decomposition makes oblique shocks tractable with only normal shock theory."

- question: "Why do supersonic inlet designers use multiple oblique shocks to decelerate flow rather than a single normal shock, and what is the theoretical optimum?"
  type: short-answer
  answer: "Each oblique shock produces less entropy rise (less total pressure loss) than a normal shock decelerating flow by the same total amount. By using a series of increasingly weaker oblique shocks, each one carries a smaller entropy penalty, so the total pressure recovery is higher than from a single strong normal shock. The theoretical optimum is infinitely many infinitely weak shocks — isentropic compression — which approaches zero entropy production. In practice, engineers use two to four oblique ramps to approximate this, balancing total pressure recovery against mechanical complexity."
  explanation: "Total pressure recovery (p₀_exit / p₀_inlet) is a key performance metric for supersonic inlets; every point of recovery translates to more thrust from the engine. A single normal shock at M = 2.5 recovers roughly 50–60% of total pressure. A two-shock oblique system can recover 80–90%. This is why supersonic military jets and supersonic transports use variable-geometry inlet ramps rather than flat perpendicular inlets — the aerodynamic efficiency gain is substantial."
```

## Explainer

From your study of normal shocks, you know what happens when supersonic flow hits a wall head-on: a strong discontinuity forms, and the flow decelerates to subsonic speed with large pressure, temperature, and entropy increases. But in practice, supersonic flow rarely meets a perfectly perpendicular wall. When a flat surface is inclined — a wedge nose, a deflected control surface, a supersonic inlet ramp — the shock tilts at an angle and much of the Mach number survives. This is the **oblique shock**, and the key insight is that it reduces to a normal shock problem once you decompose the velocity correctly.

Let the oblique shock be inclined at **wave angle** β to the incoming flow (M_1). Decompose the upstream velocity into a component normal to the shock (M_{n1} = M_1 sin β) and a component tangential to the shock (M_t = M_1 cos β). The tangential component is unchanged across the shock — there is no pressure gradient driving it. Only the normal component experiences the shock. So apply all the normal shock relations you already know, but using M_{n1} instead of M_1: you get the normal Mach number downstream M_{n2}, and the corresponding pressure, temperature, and density ratios. The downstream Mach number is then reconstructed as M_2 = M_{n2} / sin(β − δ), where **deflection angle** δ is how much the flow turns toward the wall.

The θ-β-M relation connects the three: tan(δ) = 2 cot(β) [M_1² sin²(β) − 1] / [M_1²(γ + cos 2β) + 2]. For a given M_1 and required flow deflection δ, this equation typically has two solutions: a **weak shock** (smaller β, flow may remain supersonic) and a **strong shock** (larger β, flow is subsonic downstream). In practice, nature selects the weak shock unless a downstream boundary condition forces the strong solution. There is also a **maximum deflection angle** δ_max for each M_1 — if the wall turns more sharply than this, no attached oblique shock can form and a detached **bow shock** stands off the body, with a normal shock at the centerline and increasingly oblique portions away from the axis.

This framework is indispensable for supersonic inlet design. Rather than accepting one strong normal shock (maximum total pressure loss), engineers use a series of oblique shocks to decelerate the flow incrementally, each one weaker than the last. Each oblique shock carries less entropy rise than an equivalent normal shock. The theoretical optimum — infinitely many infinitely weak oblique shocks — is the **isentropic compression**, approximated in practice by curved ramps. Understanding the β-δ-M geometry lets you calculate exactly how much total pressure recovery each ramp configuration provides and how to prevent the flow from detaching.

---
id: root-locus-controller-design
title: Controller Design via Root Locus
domain: engineering
course: control-systems
prerequisites:
- id: root-locus-method
  type: hard
- id: steady-state-error-analysis
  type: soft
builds-toward:
- lead-lag-compensators
tags:
- compensator-design
- root-locus
- dominant-poles
- angle-condition
- design-specs
stage: advanced
status: validated
---

# Controller Design via Root Locus

## Core Idea
Controller design via root locus involves adding compensator poles and zeros to reshape the locus so it passes through desired closed-loop pole locations corresponding to performance specifications. The design maps specifications (settling time, overshoot) to a desired dominant pole location in the s-plane, then determines the phase angle contribution the compensator must provide to satisfy the angle condition at that point. Lead compensators (zero closer to imaginary axis than pole) add phase to increase speed; lag compensators improve steady-state accuracy by adding low-frequency gain. The dominant pole assumption — that poles closest to the imaginary axis govern the step response — underpins the method but must be verified post-design.

## How It's Best Learned
Calculate the required angle contribution at the desired pole location before determining compensator zero and pole placement. Always verify the dominant pole assumption by checking that non-dominant poles are at least 5× further left in the s-plane, and simulate the full response.

## Common Misconceptions
- Satisfying the angle condition ensures the desired poles lie on the locus, but the gain K must then be set separately to place them at the exact desired locations.
- The dominant pole approximation fails when non-dominant poles create closed-loop zeros that nearly cancel them — always simulate the full closed-loop response.
- Lead and lag compensators serve fundamentally different purposes and are not interchangeable in terms of their effect on the locus shape.

## Explainer

From your prerequisite on the root locus method, you know how to sketch the locus — the set of all possible closed-loop pole locations as gain K varies from 0 to ∞. Controller design via root locus reverses this question: instead of asking "where do the poles go as K increases?", you ask "what compensator do I need to make the locus pass through the pole locations I want?" The starting point is always translating time-domain **performance specifications** into a desired closed-loop pole location in the s-plane.

The mapping from specs to s-plane is concrete. For a second-order system, **percent overshoot** maps to a minimum **damping ratio** ζ via %OS = 100·exp(−πζ/√(1−ζ²)), which corresponds to a wedge-shaped region in the left-half s-plane centered on the real axis. **Settling time** maps to a minimum distance from the imaginary axis: the real part of the desired pole σ = −4/T_s (for a 2% criterion). Where these constraints intersect — a specific complex location s* — is your **desired dominant pole**. If the uncompensated locus does not pass through s*, a compensator is needed to reshape it.

The **angle condition** is the mechanism. A point s* is on the root locus if and only if the phase angle of the open-loop transfer function G(s)H(s) evaluated at s* equals ±180° (an odd multiple). You evaluate the phase contribution of all existing poles and zeros at s* and compute the **angle deficiency** — how many degrees short of 180° the current system is. A **lead compensator** C(s) = (s + z)/(s + p) with z < p (zero closer to the origin than the pole) contributes positive phase at s*. You place the compensator zero and pole geometrically — often by bisecting angles — to contribute exactly the required angle deficiency. Once the angle condition is satisfied, the locus passes through s*, and you set gain K to place the closed-loop poles exactly at s*.

**Lag compensators** work differently and serve a different purpose. A lag compensator C(s) = (s + z)/(s + p) with z > p (pole closer to origin) contributes negative phase but adds low-frequency gain without significantly changing the locus shape near the desired poles. This improves **steady-state accuracy** — reducing position or velocity error — without substantially affecting transient performance. The **dominant pole assumption** that underpins all of this must be verified: if any non-dominant closed-loop poles are within 5× the real-part magnitude of the dominant poles, they will significantly affect the response and the design requires iteration. Always simulate the full closed-loop response to confirm the design meets specs before considering the job done.

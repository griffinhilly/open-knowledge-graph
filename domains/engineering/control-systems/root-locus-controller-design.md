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
- id: root-locus-gain-design
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

## Questions

```yaml
- question: "A lead compensator has been designed so that its zero and pole satisfy the angle condition at the desired closed-loop pole location s*. What additional step is required to complete the design?"
  type: multiple-choice
  options:
    - "The design is complete — satisfying the angle condition places the closed-loop pole at s* for all values of gain K"
    - "Gain K must be set separately using the magnitude condition to place the closed-loop pole exactly at s*"
    - "A lag compensator must be added to cancel the phase contribution of the lead compensator"
    - "The plant transfer function must be re-linearized around the new operating point defined by s*"
  answer: 1
  explanation: "Satisfying the angle condition means s* lies on the root locus — it is a *possible* closed-loop pole location. But the root locus contains infinitely many points, one for each value of K. To place the closed-loop pole exactly at s*, gain K must be set using the magnitude condition: K = 1/|G(s*)H(s*)|. Satisfying the angle condition and setting K are two separate steps; confusing them is the most common design error."

- question: "A control engineer needs to improve a system's steady-state tracking accuracy (reduce position error) without significantly changing its transient response speed or overshoot. Which compensator is appropriate?"
  type: multiple-choice
  options:
    - "Lead compensator — adds phase near the desired pole to increase response speed"
    - "Lag compensator — adds low-frequency gain to reduce steady-state error without substantially reshaping the locus near the desired poles"
    - "Both lead and lag simultaneously to address both transient and steady-state performance"
    - "Neither — steady-state accuracy can only be improved by increasing plant gain K directly"
  answer: 1
  explanation: "Lead and lag compensators serve fundamentally different purposes. A lead compensator (zero closer to imaginary axis than pole) adds phase near the desired closed-loop poles, improving speed and damping. A lag compensator (pole closer to origin than zero) places its pole and zero very close together near the origin, contributing nearly zero phase near the desired poles but adding significant low-frequency gain — exactly what is needed to reduce steady-state error. Using a lead compensator for steady-state accuracy (or a lag compensator for speed) conflates two distinct design objectives."

- question: "A lead compensator improves both transient response speed and steady-state accuracy, making it the preferred choice over a lag compensator in most control design scenarios."
  type: true-false
  answer: false
  explanation: "Lead and lag compensators address different objectives and are not substitutes. A lead compensator adds phase at the desired closed-loop pole location, improving speed and damping — transient performance. It does not significantly improve steady-state accuracy. A lag compensator adds low-frequency gain (improving steady-state error) without substantially adding or removing phase near the desired poles. Claiming a lead compensator improves steady-state accuracy conflates the two and ignores the distinct mechanics of each compensator type."

- question: "The dominant pole assumption is considered valid when non-dominant closed-loop poles are at least 5 times further to the left in the s-plane than the dominant poles."
  type: true-false
  answer: true
  explanation: "The 5× rule-of-thumb ensures that non-dominant poles produce transient terms that decay roughly 5× faster than the dominant pole terms, making their contribution negligible in the step response within a fraction of the dominant settling time. If non-dominant poles are closer to the imaginary axis — especially if they nearly cancel with closed-loop zeros — their contribution can significantly alter the response and the second-order approximation breaks down. Always verify this condition and simulate the full response."

- question: "Why is the angle condition central to root locus controller design, and what does it mean geometrically?"
  type: short-answer
  answer: "The angle condition states that a point s* lies on the root locus if and only if the total phase angle of the open-loop transfer function evaluated at s* equals ±180° (an odd multiple). Geometrically, you draw vectors from every open-loop pole and zero to s*, measure each vector's angle, and sum them (subtracting pole angles, adding zero angles). If the sum equals 180°, s* is on the locus. If it does not, the angle deficiency tells you exactly how many degrees of phase a compensator must contribute. The compensator's zero and pole are then positioned so that their angular contributions make up the deficiency — reshaping the locus to pass through the desired closed-loop pole location."
  explanation: "This geometric interpretation is what makes root locus design tractable: instead of solving for compensator parameters algebraically, you graphically determine the phase contribution needed and use simple angle geometry (often bisecting angles or using circular arcs) to place the compensator elements."
```

## Explainer

From your prerequisite on the root locus method, you know how to sketch the locus — the set of all possible closed-loop pole locations as gain K varies from 0 to ∞. Controller design via root locus reverses this question: instead of asking "where do the poles go as K increases?", you ask "what compensator do I need to make the locus pass through the pole locations I want?" The starting point is always translating time-domain **performance specifications** into a desired closed-loop pole location in the s-plane.

The mapping from specs to s-plane is concrete. For a second-order system, **percent overshoot** maps to a minimum **damping ratio** ζ via %OS = 100·exp(−πζ/√(1−ζ²)), which corresponds to a wedge-shaped region in the left-half s-plane centered on the real axis. **Settling time** maps to a minimum distance from the imaginary axis: the real part of the desired pole σ = −4/T_s (for a 2% criterion). Where these constraints intersect — a specific complex location s* — is your **desired dominant pole**. If the uncompensated locus does not pass through s*, a compensator is needed to reshape it.

The **angle condition** is the mechanism. A point s* is on the root locus if and only if the phase angle of the open-loop transfer function G(s)H(s) evaluated at s* equals ±180° (an odd multiple). You evaluate the phase contribution of all existing poles and zeros at s* and compute the **angle deficiency** — how many degrees short of 180° the current system is. A **lead compensator** C(s) = (s + z)/(s + p) with z < p (zero closer to the origin than the pole) contributes positive phase at s*. You place the compensator zero and pole geometrically — often by bisecting angles — to contribute exactly the required angle deficiency. Once the angle condition is satisfied, the locus passes through s*, and you set gain K to place the closed-loop poles exactly at s*.

**Lag compensators** work differently and serve a different purpose. A lag compensator C(s) = (s + z)/(s + p) with z > p (pole closer to origin) contributes negative phase but adds low-frequency gain without significantly changing the locus shape near the desired poles. This improves **steady-state accuracy** — reducing position or velocity error — without substantially affecting transient performance. The **dominant pole assumption** that underpins all of this must be verified: if any non-dominant closed-loop poles are within 5× the real-part magnitude of the dominant poles, they will significantly affect the response and the design requires iteration. Always simulate the full closed-loop response to confirm the design meets specs before considering the job done.

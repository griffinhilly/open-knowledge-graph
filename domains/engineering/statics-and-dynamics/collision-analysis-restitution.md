---
id: collision-analysis-restitution
title: Collision Analysis and Coefficient of Restitution
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: impulse-momentum-particles
  type: hard
- id: impact-and-restitution
  type: hard
- id: conservation-of-linear-momentum
  type: hard
tags:
- collision
- restitution
- elastic
- inelastic
- impact
stage: formal-systems
status: validated
---

# Collision Analysis and Coefficient of Restitution

## Core Idea
The coefficient of restitution e relates velocities before and after collision for particles along the collision line: e = -(v₂' - v₁')/(v₂ - v₁). Values range from e = 0 (perfectly inelastic) to e = 1 (perfectly elastic). Both momentum and the restitution equation are used to solve collision problems. Energy is lost in collisions when e < 1.

## Questions

```yaml
- question: "Two objects of known mass collide. You know all pre-collision velocities. What additional information is needed to determine both post-collision velocities?"
  type: multiple-choice
  options:
    - "Nothing — conservation of momentum alone fully determines both post-collision velocities"
    - "Conservation of kinetic energy — this provides the second equation needed"
    - "The coefficient of restitution — this provides the second equation linking relative velocities"
    - "The contact impulse force — once you know the contact force, post-collision velocities are determined"
  answer: 2
  explanation: "Momentum conservation gives one equation (m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂') with two unknowns (v₁' and v₂') — the system is underdetermined. The coefficient of restitution e = −(v₂' − v₁')/(v₂ − v₁) provides the second equation. Option B is incorrect: kinetic energy is only conserved in perfectly elastic collisions (e = 1), so it cannot be assumed in general. Option D is circular — impulse is typically what you derive from post-collision velocities, not a given input."

- question: "A 4 kg ball moving at 5 m/s strikes a stationary 4 kg ball with e = 0. What are the post-collision velocities?"
  type: multiple-choice
  options:
    - "v₁' = 5 m/s, v₂' = 0 m/s — the first ball passes through unchanged"
    - "v₁' = 0 m/s, v₂' = 5 m/s — the first ball stops and all momentum transfers"
    - "v₁' = 2.5 m/s, v₂' = 2.5 m/s — both balls move at half the original speed"
    - "v₁' = −5 m/s, v₂' = 5 m/s — the first ball bounces back with equal speed"
  answer: 2
  explanation: "With e = 0, the restitution equation gives v₂' − v₁' = 0, so both objects have the same post-collision velocity (perfectly inelastic). Momentum conservation: 4(5) + 4(0) = (4 + 4)v', giving v' = 2.5 m/s for both. Option B (v₁' = 0, v₂' = 5) is the result for e = 1 (elastic) with equal masses — a common but incorrect answer for e = 0. For e = 0, objects stick together; they do not undergo a clean exchange of velocities."

- question: "Momentum is conserved in all collisions, so kinetic energy must also be conserved in all collisions."
  type: true-false
  answer: false
  explanation: "Momentum and kinetic energy are governed by different principles. Momentum conservation follows from Newton's third law and holds for all collisions (any value of e), requiring only that no net external force acts during impact. Kinetic energy conservation requires e = 1 (perfectly elastic) — energy stored as deformation is fully recovered. For e < 1, kinetic energy is converted to heat, sound, and permanent deformation. A clay-ball collision conserves momentum exactly while dissipating essentially all kinetic energy. They are independent conditions."

- question: "In a perfectly inelastic collision (e = 0), the two objects always stick together and move with a single common post-collision velocity."
  type: true-false
  answer: true
  explanation: "e = 0 means the relative separation velocity after the collision is zero: v₂' − v₁' = 0. If the relative velocity is zero, both objects have the same post-collision velocity — they move together as a single unit. The common velocity is found from momentum conservation alone: v' = (m₁v₁ + m₂v₂)/(m₁ + m₂). This is the formal definition of a perfectly inelastic collision: maximum kinetic energy loss consistent with momentum conservation."

- question: "Why is conservation of momentum alone insufficient to solve a two-body collision, and what role does the coefficient of restitution play?"
  type: short-answer
  answer: "Momentum conservation gives one equation with two unknowns (v₁' and v₂'), leaving infinitely many valid solutions. The coefficient of restitution provides the second equation by characterizing how bouncy the collision is: e = −(v₂' − v₁')/(v₂ − v₁) specifies that the relative separation speed is a fixed fraction e of the relative approach speed. Together, the two equations form a 2×2 linear system that uniquely determines both post-collision velocities."
  explanation: "This underdetermination is fundamental, not incidental: the same two objects with the same initial velocities could in principle collide with any e from 0 to 1, and each would conserve momentum while producing different outcomes. The coefficient of restitution is a material property — it encodes how much of the approach kinetic energy is stored as elastic deformation and recovered versus dissipated. Engineers exploit this: crash barriers target low e to absorb energy, billiard balls target high e to preserve speed, and vehicle crumple zones are designed with specific e values to control energy transfer to occupants."
```

## Explainer

Conservation of linear momentum — your core prerequisite — tells you that the total momentum of an isolated two-particle system is unchanged by a collision: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'. This gives you one equation with two unknowns (the post-collision velocities v₁' and v₂'). The momentum equation alone is underdetermined; you need a second relationship that characterizes the collision itself. That's where the **coefficient of restitution** e enters.

The coefficient of restitution is defined along the line of impact as e = -(v₂' - v₁')/(v₂ - v₁), or equivalently, the relative separation velocity equals e times the relative approach velocity. When e = 1, the particles bounce apart as fast as they came together — a **perfectly elastic collision** — and kinetic energy is fully conserved. When e = 0, the particles stick together and move as one mass — a **perfectly inelastic collision** — and the maximum kinetic energy is lost. Real collisions fall between these extremes; a rubber ball on concrete might have e ≈ 0.8, a lump of clay e ≈ 0.

The standard solution procedure for a **direct central impact** (1D, particles moving along the same line) is to write the momentum equation and the restitution equation as a 2×2 linear system in v₁' and v₂', then solve simultaneously. The kinetic energy lost in the collision is ΔKE = ½m₁v₁² + ½m₂v₂² - ½m₁v₁'² - ½m₂v₂'², and this can be verified to vanish only when e = 1. For an **oblique impact** (particles approaching at an angle), resolve velocities into components along the line of impact and perpendicular to it. The impulse acts only along the line of impact, so components perpendicular to it are unchanged; apply momentum conservation and the restitution equation only to the impact-line components.

The impulse-momentum framework you already know connects naturally here: the entire velocity change is caused by the impulsive contact force, which acts for a very short time. The ratio e fundamentally reflects how much of the approach kinetic energy is stored as elastic deformation and recovered, versus dissipated as heat, sound, or permanent deformation. Engineering applications range from designing protective packaging (low e absorbs energy) to billiard ball dynamics (e near 1 preserves speed) to vehicle crash analysis (where e governs how energy is transferred to occupants).

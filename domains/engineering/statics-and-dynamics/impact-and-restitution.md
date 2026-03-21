---
id: impact-and-restitution
title: Impact and Coefficient of Restitution
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: impulse-momentum-particles
  type: hard
- id: collisions-elastic-inelastic
  type: soft
tags:
- dynamics
- impact
- collision
- coefficient of restitution
- energy loss
stage: formal-systems
status: validated
---

# Impact and Coefficient of Restitution

## Core Idea
Impact between two particles is analyzed using the coefficient of restitution e, defined as e = (v'_B − v'_A) / (v_A − v_B) along the line of impact (common normal at contact). For perfectly elastic impact e = 1 (no kinetic energy loss); for perfectly plastic impact e = 0 (maximum energy loss, particles stick together). Combined with conservation of linear momentum along the line of impact, the two equations determine post-impact velocities. For oblique impacts, tangential velocity components of smooth spheres are unchanged, and restitution applies only along the line of impact.

## How It's Best Learned
Always identify the line of impact first (direction of common normal at contact). Write conservation of momentum and the restitution equation as a two-equation system and solve simultaneously. Verify that kinetic energy is not gained.

## Common Misconceptions
- Applying the restitution equation in the tangential direction instead of along the line of impact.
- Confusing e = 1 (elastic, no energy loss) with a special case requiring equal masses.
- In oblique impacts, incorrectly changing the tangential velocity components of smooth particles during contact.

## Questions

```yaml
- question: "Two smooth spheres collide obliquely (not head-on). Sphere A's velocity has components v_An = 4 m/s (normal to contact) and v_At = 3 m/s (tangential). After impact, what happens to v_At?"
  type: multiple-choice
  options:
    - "v_At changes according to the restitution equation applied in the tangential direction"
    - "v_At = 0 after impact, since all tangential momentum is lost during contact"
    - "v_At remains 3 m/s unchanged, because smooth spheres exert no friction force tangentially"
    - "v_At changes based on conservation of momentum in the tangential direction"
  answer: 2
  explanation: "For smooth (frictionless) spheres, the contact force acts only along the line of impact — the normal direction at the contact point. There is no tangential force to change the tangential velocity component. Therefore v_At is completely unchanged by the impact. This is a direct consequence of Newton's second law: no tangential force means no tangential impulse, so no change in tangential momentum. Applying restitution in the tangential direction (option A) is the most common error in oblique impact problems."

- question: "Two spheres collide with coefficient of restitution e = 1. Which statement is correct?"
  type: multiple-choice
  options:
    - "The spheres must have equal mass for e = 1 to hold"
    - "The collision is perfectly plastic and the spheres stick together"
    - "The relative separation speed equals the relative approach speed — no kinetic energy is lost"
    - "Each sphere bounces back at the same speed it had before, regardless of mass ratio"
  answer: 2
  explanation: "e = 1 means (v'_B − v'_A)/(v_A − v_B) = 1, i.e., the separation speed equals the approach speed. This is the perfectly elastic case: kinetic energy is conserved. Equal mass is not required — in a perfectly elastic collision between unequal masses, the spheres exchange some fraction of velocity depending on the mass ratio. Option D is only true for equal-mass elastic collisions. Option B describes e = 0 (perfectly plastic)."

- question: "The coefficient of restitution equation, combined with linear momentum conservation, provides exactly the two equations needed to determine both post-impact velocities along the line of impact."
  type: true-false
  answer: true
  explanation: "Momentum conservation alone yields one equation with two unknowns (v'_A and v'_B along the line of impact). The restitution equation provides a second independent relationship between those same two unknowns. Together, the two equations form a solvable 2×2 system. This is the entire analytical framework for central impact — one momentum equation plus one restitution equation."

- question: "A coefficient of restitution of e = 1 indicates that the two colliding objects have equal mass."
  type: true-false
  answer: false
  explanation: "The coefficient of restitution characterizes the material properties and deformation behavior of the collision, not the mass ratio. e = 1 means no kinetic energy is lost — a property of how the objects deform and rebound, related to material elasticity. It applies to any mass ratio. You can have e = 1 for a ping-pong ball hitting a bowling ball (approximately), and e < 1 for two equal-mass clay balls that stick together."

- question: "Why is it necessary to identify the 'line of impact' before applying the restitution equation, and what defines this line geometrically?"
  type: short-answer
  answer: "The coefficient of restitution is defined specifically as the ratio of separation speed to approach speed *along the line of impact* — the direction in which the contact force acts. For two spheres, this is the line connecting their centers at the moment of contact (the common normal). Applying the restitution equation in any other direction gives physically incorrect results because the contact force has no component in the tangential direction. Identifying the line of impact also separates the problem: restitution + momentum apply in the normal direction, while tangential velocity components (for smooth bodies) are simply unchanged."
  explanation: "This is the procedural core of impact analysis. The line of impact is the direction of the impulsive force, which is the only force large enough to change velocities during the brief collision. The geometry of contact (sphere centers, flat surface normal) determines this direction. Once identified, the problem decomposes cleanly: normal direction (two equations, two unknowns), tangential direction (unchanged — zero equations needed). Without this decomposition, oblique impact problems become unsolvable."
```

## Explainer

From your work with impulse-momentum and collisions, you know that a collision is a brief, high-force interaction and that linear momentum is conserved across it. The problem with stopping there is that momentum conservation alone gives you one equation and two unknowns (the two post-impact velocities along the line of contact). You need a second equation — and that is where the **coefficient of restitution** e comes in.

The coefficient of restitution is defined along the **line of impact** (the common normal at the contact point, which is the line connecting the centers of two spheres or the normal to a flat surface): e = (v'_B − v'_A) / (v_A − v_B). Read it as a ratio of separation speed to approach speed. When e = 1, the particles separate exactly as fast as they approached — no kinetic energy is lost, which is the **perfectly elastic** case. When e = 0, v'_A = v'_B — the particles stick together and move as one, which is the **perfectly plastic** case with maximum energy loss. All real impacts fall somewhere between 0 and 1; a rubber ball on concrete might have e ≈ 0.8, a lump of clay on steel might have e ≈ 0.1.

With these two equations — conservation of momentum and the restitution relationship — you can always solve for both post-impact velocities along the line of impact. The procedure is: (1) identify the line of impact, (2) write the scalar momentum equation m_A*v_A + m_B*v_B = m_A*v'_A + m_B*v'_B, (3) write the restitution equation, (4) solve the system. You should always check that kinetic energy does not increase in the result — that would violate physics.

Oblique impacts add a layer of geometry but no new physics. When two smooth spheres collide at an angle, the contact force acts only along the line of impact (the normal direction) — there is no friction force in the tangential direction. This means the momentum equation and restitution equation apply only in the normal direction, and the tangential velocity components of each particle are completely unchanged by the impact. The key move is to decompose each particle's velocity into normal and tangential components at the start, apply impact analysis in the normal direction only, and then reassemble the post-impact velocity from the new normal component and the unchanged tangential component. Many students forget this decomposition and incorrectly try to apply restitution in the tangential direction, producing nonsensical results.

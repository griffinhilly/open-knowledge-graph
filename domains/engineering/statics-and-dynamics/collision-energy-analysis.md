---
id: collision-energy-analysis
title: Collision Analysis and Energy
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: linear-momentum-impulse-systems
  type: hard
- id: impact-and-restitution
  type: soft
tags:
- collision
- restitution
- elastic
- inelastic
- energy dissipation
- impact velocity
stage: formal-systems
status: draft
---

# Collision Analysis and Energy

## Core Idea
Collisions are classified by the coefficient of restitution e, which relates relative velocities before and after impact: e = (v₂' - v₁') / (v₁ - v₂). Elastic collisions (e = 1) conserve kinetic energy; inelastic collisions (0 ≤ e < 1) dissipate energy through deformation and heat. Momentum is always conserved, enabling calculation of post-impact velocities and energy loss.

## Questions

```yaml
- question: "A 2 kg ball moving at 6 m/s strikes a stationary 2 kg ball in a perfectly inelastic collision. Which principle correctly determines the post-collision velocity?"
  type: multiple-choice
  options:
    - "Kinetic energy conservation: ½(2)(6²) = ½(4)v², so v = 4.24 m/s"
    - "Momentum conservation: (2)(6) = (4)v, so v = 3 m/s"
    - "The coefficient of restitution alone: e = 0 means v = 0 m/s"
    - "Both momentum and energy conservation must hold simultaneously: v = 6 m/s"
  answer: 1
  explanation: "In a perfectly inelastic collision (e = 0), the objects move together after impact. Momentum conservation gives (2)(6) + 0 = (2+2)v, so v = 3 m/s. Option A incorrectly applies kinetic energy conservation — kinetic energy is NOT conserved in inelastic collisions. Option C misapplies e = 0 alone; you still need momentum conservation to find the actual velocity. Option D is wrong because energy conservation cannot be applied to kinetic energy here. The kinetic energy loss is ½(2)(6²) − ½(4)(3²) = 36 − 18 = 18 J, converted to heat, sound, and deformation."

- question: "Two objects collide with coefficient of restitution e = 0.6. The relative velocity of approach was 10 m/s. What is the relative velocity of separation after impact?"
  type: multiple-choice
  options:
    - "10 m/s — momentum conservation requires equal approach and separation speeds"
    - "6 m/s — the coefficient of restitution gives e × (relative approach) = relative separation"
    - "4 m/s — the kinetic energy lost equals (1−e) of the initial kinetic energy"
    - "0.6 m/s — the restitution coefficient directly gives the post-impact velocity"
  answer: 1
  explanation: "The coefficient of restitution is defined as e = (relative velocity of separation) / (relative velocity of approach) = (v₂' − v₁') / (v₁ − v₂). With e = 0.6 and approach speed 10 m/s, the relative separation speed is 0.6 × 10 = 6 m/s. This is the second equation needed alongside momentum conservation to solve for both post-impact velocities. Option A would only be true for a perfectly elastic collision (e = 1)."

- question: "Momentum is conserved in all collisions, regardless of whether the collision is elastic or inelastic."
  type: true-false
  answer: true
  explanation: "Momentum conservation applies to ALL collisions because the internal forces between colliding objects are equal and opposite (Newton's third law), contributing zero net impulse to the system. External forces (gravity, friction) also act during a collision, but the collision duration is so brief that their impulse is negligible. Momentum conservation is exact and universal for collisions. Kinetic energy conservation, by contrast, only holds for perfectly elastic collisions (e = 1) — it is the special case, not the rule."

- question: "In a perfectly inelastic collision, all kinetic energy is lost."
  type: true-false
  answer: false
  explanation: "A perfectly inelastic collision (e = 0) means the objects move together after impact — maximum deformation and maximum kinetic energy loss for given initial conditions. However, unless one object was already stationary in the center of mass frame, the combined mass is still moving, and some kinetic energy remains. Total energy is conserved (thermodynamics), but it's redistributed: the kinetic energy that disappears becomes heat, sound, and deformation energy. Only in the special case where both objects have equal mass and one is initially stationary does all kinetic energy convert to other forms."

- question: "Why is the coefficient of restitution needed in addition to momentum conservation to solve a two-body collision problem?"
  type: short-answer
  answer: "A two-body collision has two unknown post-impact velocities. Momentum conservation provides one equation: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'. This alone is underdetermined — infinitely many pairs (v₁', v₂') satisfy it. The coefficient of restitution provides a second independent equation: e = (v₂' − v₁') / (v₁ − v₂), constraining the relative velocity of separation. Together, the two equations uniquely determine both post-impact velocities. The restitution coefficient encodes the material's elastic properties — how 'bouncy' the contact surfaces are — and this physical property is what closes the system."
  explanation: "Without the restitution equation, you know total momentum but cannot determine how it is distributed between the two objects. Any distribution that conserves momentum is mathematically valid; the physics of the materials determines which one actually occurs."
```

## Explainer

From your prerequisite study of linear momentum and impulse, you know that the total momentum of a system is conserved whenever the net external impulse is zero. In a collision, the internal forces between the colliding objects are enormous but exactly equal and opposite — they contribute zero net impulse to the system. External forces like gravity act during the collision too, but the collision duration is so short that their impulse is negligible. The result: **momentum conservation is exact** for all collisions, regardless of how violent or how much energy is lost.

Momentum conservation alone gives you one equation for two unknowns (the two post-collision velocities). To close the problem you need a second equation — and this is where the **coefficient of restitution** e comes in. The coefficient of restitution relates the relative velocity of separation after impact to the relative velocity of approach before impact: e = (v₂' − v₁')/(v₁ − v₂). It is a material property that captures how much the contact surfaces elastically "bounce back." A perfectly elastic collision has e = 1, meaning the objects separate with exactly the same relative speed they approached. A perfectly inelastic collision has e = 0, meaning the objects end up moving together (zero relative velocity after impact) — maximum deformation, maximum energy loss. Real collisions fall somewhere between: a tennis ball on concrete might have e ≈ 0.75, while a lead ball might have e ≈ 0.2.

With momentum conservation and the restitution equation, you have two equations and two unknowns. Solving them gives both post-impact velocities. The **kinetic energy lost** can then be computed directly: ΔKE = ½m₁v₁² + ½m₂v₂² − ½m₁v₁'² − ½m₂v₂'². For an elastic collision (e = 1) this is zero by construction — you can verify algebraically. For an inelastic collision, the lost kinetic energy has gone into deformation, heat, sound, and vibration. A useful result: for two masses with a perfectly inelastic collision (e = 0), the energy loss depends only on the reduced mass and the relative velocity of approach — larger mass ratio means more energy survives.

The hardest conceptual step for most students is accepting that momentum is always conserved while energy is not. Momentum is a vector quantity tied to a symmetry law (spatial translation invariance) and always conserved in an isolated system. Kinetic energy is not separately conserved in inelastic collisions because energy transforms into other forms — but total energy is still conserved. The coefficient of restitution is the bridge: it tells you exactly how much relative velocity survives the collision, from which you can quantify exactly how much kinetic energy was converted into other forms.

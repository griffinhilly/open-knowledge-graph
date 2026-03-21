---
id: conservation-of-angular-momentum-mechanics
title: Conservation of Angular Momentum
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: angular-impulse-momentum
  type: hard
- id: torque-angular-acceleration
  type: soft
- id: conservation-of-angular-momentum
  type: hard
builds-toward:
- rigid-body-rotation-theory
- gyroscopic-motion-and-stability
tags:
- angular-momentum
- conservation-laws
- torque
stage: formal-systems
status: draft
---

# Conservation of Angular Momentum

## Core Idea
Angular momentum L = r × p (or L = Iω for rotation) is conserved in systems with zero net external torque. This explains why spinning ice skaters accelerate when pulling in their arms, and why rotating systems exhibit remarkable stability—it is the rotational analog of linear momentum conservation and equally fundamental.

## Questions

```yaml
- question: "An ice skater spins at ω = 4 rad/s with arms extended (I = 3 kg·m²). She pulls her arms in, reducing her moment of inertia to I = 1 kg·m². What is her new angular velocity, and why?"
  type: multiple-choice
  options:
    - "ω = 4 rad/s — angular velocity is conserved just like linear velocity in the absence of forces"
    - "ω = 12 rad/s — because angular momentum L = Iω must stay constant, so halving I triples ω"
    - "ω = 12 rad/s — because the skater did work by pulling her arms in, adding kinetic energy"
    - "ω = 1.33 rad/s — because total kinetic energy (½Iω²) must be conserved"
  answer: 1
  explanation: "With no external torque acting, angular momentum L = Iω is conserved: L = 3·4 = 12 kg·m²/s. When I drops to 1, ω must rise to 12 to maintain L = 12. Option A is wrong because angular velocity is NOT conserved — angular momentum is. Option C has the right numerical answer but wrong reasoning: the skater does do internal work (muscle work pulling arms in), so kinetic energy is not conserved — it actually increases. Option D applies energy conservation incorrectly. The key insight is that the conserved quantity is the product Iω, not either factor alone."

- question: "A planet orbits the Sun in an elliptical orbit. It moves faster when closer to the Sun and slower when farther away. Which principle directly explains this?"
  type: multiple-choice
  options:
    - "Conservation of energy — the planet trades potential energy for kinetic energy as it falls toward the Sun"
    - "Newton's second law — the stronger gravitational force when close to the Sun directly accelerates the planet"
    - "Conservation of angular momentum — gravity produces no torque about the Sun, so L = r × p stays constant"
    - "Conservation of linear momentum — the Sun and planet exchange momentum as the orbit varies"
  answer: 2
  explanation: "This is Kepler's second law (equal areas in equal times) as a direct consequence of angular momentum conservation. Gravity always points from the planet toward the Sun — directly through the pivot point — so it produces zero torque about the Sun. With no torque, angular momentum L = r × p = m·r·v_perp is conserved. When the planet is close to the Sun (small r), v_perp must be large to keep r·v_perp constant. When far away (large r), v_perp is small. Option A is also true (energy is conserved) and also explains the speed variation, but it does not directly explain the equal-areas law. Conservation of angular momentum is the more direct and fundamental explanation for the orbital speed variation."

- question: "When an ice skater pulls her arms inward and spins faster, her angular momentum increases because she is doing internal work on her body."
  type: true-false
  answer: false
  explanation: "Angular momentum is conserved — it does NOT change. The skater pulls her arms in, reducing her moment of inertia I, and her angular velocity ω increases proportionally so that the product Iω stays constant. She has not added any angular momentum to the system; she has merely redistributed mass relative to the spin axis. Her kinetic energy (½Iω²) actually does increase — the internal work of pulling her arms against centrifugal effect converts chemical energy to rotational kinetic energy — but angular momentum remains constant throughout. Conservation of angular momentum says nothing about kinetic energy."

- question: "Conservation of angular momentum requires that both the moment of inertia I and the angular velocity ω remain individually constant when no external torque acts."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about angular momentum conservation. What is conserved is the PRODUCT L = Iω — not either factor individually. I can change (because moment of inertia depends on mass distribution, which can shift internally), and ω can change accordingly, as long as their product stays constant. This is the entire point of the ice skater example: I decreases, ω increases, L remains fixed. Conservation of angular momentum only requires L = Iω = constant, not I = constant or ω = constant separately. A system can undergo dramatic internal rearrangements (changing both I and ω) while perfectly conserving angular momentum."

- question: "Explain why an ice skater spins faster when pulling her arms inward, using the concept of angular momentum conservation. What is actually conserved, and why doesn't the skater 'create' new rotation?"
  type: short-answer
  answer: "Angular momentum L = Iω is conserved because no external torque acts on the skater (ice friction is negligible and acts through the contact point, producing little torque). When she pulls her arms inward, the mass distribution shifts closer to the spin axis, reducing the moment of inertia I. Since L = Iω must remain constant and I decreased, ω must increase proportionally. She doesn't create new angular momentum — she started spinning with some L and merely traded a larger I for a smaller I while ω compensated."
  explanation: "The deeper point is that I is not fixed — it is a property of how mass is spatially arranged, which can change through internal forces. Angular momentum conservation governs the product Iω, not either variable alone. This is precisely why it is more useful to think in terms of conserved quantities than forces when analyzing such systems: you don't need to know the internal forces (muscle tension, contact forces between body parts), just the initial and final moments of inertia. The conservation law gives you the answer directly."
```

## Explainer

You already know from angular impulse-momentum that net torque causes angular momentum to change: ΣM = dL/dt. Conservation of angular momentum is simply the case where ΣM = 0, so dL/dt = 0, meaning **L = constant**. The logic mirrors linear momentum conservation exactly — just as a net force is required to change linear momentum, a net external torque is required to change angular momentum. If no torque acts, the rotational state of the system cannot change.

For a rigid body spinning about a fixed axis, this takes the compact form L = Iω = constant. The critical insight is that the **moment of inertia** I is not fixed — it depends on how mass is distributed relative to the spin axis. When an ice skater pulls their arms inward, they reduce their moment of inertia. Because Iω must stay constant, ω must increase proportionally. The total angular momentum (the product Iω) is conserved; the skater hasn't done any external work on angular momentum — they've merely redistributed mass to change I and ω simultaneously. This is why conservation calculations often proceed differently from torque-based ones: you don't need to know the internal forces, just the initial and final moments of inertia.

For particles and systems where the position vector matters, the vector form L = r × p becomes important. Angular momentum depends on both the speed of the particle *and* its perpendicular distance from the rotation axis (the moment arm). A planet in an elliptical orbit conserves angular momentum because gravity always points through the Sun (zero torque about the Sun), so it moves faster when close to the Sun (small r) and slower when far away (large r) — this is Kepler's second law as a direct consequence of angular momentum conservation.

Conservation of angular momentum also underlies **gyroscopic stability**: a spinning gyroscope resists changes to its orientation because any torque produces a change in the direction of L, not a change in its magnitude. A fast-spinning top doesn't fall because gravity's torque causes L to precess (rotate) rather than tip over. This counterintuitive behavior — where a torque produces motion perpendicular to itself — follows directly from the vector nature of L = r × p and the fact that torque is dL/dt. Recognizing when angular momentum is conserved (isolated system or zero net torque) and when it is not (net external torque present) is the fundamental skill this topic develops, and it is the rotational counterpart of the same judgment call you already make for linear momentum.

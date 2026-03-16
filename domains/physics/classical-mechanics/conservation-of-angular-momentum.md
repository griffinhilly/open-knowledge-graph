---
id: conservation-of-angular-momentum
title: Conservation of Angular Momentum
domain: physics
course: classical-mechanics
prerequisites:
- id: angular-momentum
  type: hard
- id: cross-product-3d
  type: soft
builds-toward:
- keplers-laws
tags:
- conservation-of-angular-momentum
- isolated-rotation
- spin
stage: formal-systems
status: validated
---

# Conservation of Angular Momentum

## Core Idea
When the net external torque on a system is zero, its total angular momentum is conserved: L_i = L_f. This is the rotational analog of conservation of linear momentum. Classic examples: a figure skater pulling in arms to spin faster (I decreases, ω increases to maintain L); a planet moving faster when closer to the sun (Kepler's second law). Angular momentum conservation is a consequence of rotational symmetry in physics.

## How It's Best Learned
Solve problems where a person on a rotating platform catches or drops a spinning wheel. The key is computing I·ω before and after a change in mass distribution and setting them equal.

## Common Misconceptions
- Confusing conservation of angular momentum with conservation of energy: they are independent conservation laws and both can apply simultaneously.
- Thinking angular momentum is conserved only for spinning objects: it applies to any system with zero net torque, including orbiting planets.

## Questions

```yaml
- question: "A figure skater spinning with arms extended pulls her arms in close to her body, halving her moment of inertia. What happens to her angular velocity?"
  type: multiple-choice
  options: ["It halves", "It stays the same", "It doubles", "It quadruples"]
  answer: 2
  explanation: "Angular momentum L = Iω is conserved because no external torque acts on the skater. If I decreases by half and L is constant, ω must double: L = I₁ω₁ = I₂ω₂ → ω₂ = (I₁/I₂)ω₁ = 2ω₁. The skater spins faster, but her total angular momentum is unchanged."

- question: "When a figure skater pulls in her arms and spins faster, her angular momentum has increased."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Angular momentum is conserved — it does not change. What changes is how that fixed angular momentum is distributed: a smaller moment of inertia (arms in) requires a larger angular velocity to maintain the same L = Iω. The skater spins faster, but her total angular momentum is unchanged."

- question: "What condition must be satisfied for the total angular momentum of a system to be conserved?"
  type: short-answer
  answer: "The net external torque on the system must be zero."
  explanation: "This follows from Newton's second law for rotation: dL/dt = τ_net. If net external torque is zero, dL/dt = 0, so L is constant. Internal torques (forces between parts of the system) always come in equal and opposite pairs and cannot change the total angular momentum — only external torques can."
```

## Explainer

You already know that angular momentum L = Iω, where I is the moment of inertia and ω is the angular velocity. From linear mechanics, you know that momentum is conserved when no net external force acts. Conservation of angular momentum is the exact rotational analog: when no net external *torque* acts on a system, its total angular momentum remains constant. This follows directly from Newton's second law for rotation, τ_net = dL/dt: if the left side is zero, L cannot change.

The classic demonstration is the figure skater. Standing on frictionless ice with arms outstretched, she spins at some initial angular velocity ω₁ with moment of inertia I₁. When she pulls her arms in, her moment of inertia decreases to I₂ < I₁. No external torque acts, so L = Iω is conserved: I₁ω₁ = I₂ω₂. Since I₂ is smaller, ω₂ must be larger — she spins faster. This is not free energy: as she pulls her arms in, she does positive work against the tendency of her arms to fly outward, converting chemical energy into rotational kinetic energy. Angular momentum is conserved; kinetic energy is not.

There are two misconceptions to address carefully. First, the skater's angular momentum does *not* increase when she spins faster — it is conserved. The increase in ω exactly compensates the decrease in I. Second, conservation of angular momentum is independent of conservation of energy. Both laws apply simultaneously, but they govern different quantities. In the skater example, L is constant and kinetic energy increases. In an inelastic collision, linear momentum is conserved but kinetic energy is not. Always identify which conservation law applies to which quantity.

The second major application is planetary orbits. A planet orbiting the Sun traces an ellipse. As it approaches the Sun, its distance from the axis of rotation decreases — effectively reducing its rotational moment of inertia — so it speeds up. As it recedes, it slows down. Kepler observed this empirically (his second law: a planet sweeps out equal areas in equal times) centuries before Newton explained it as a direct consequence of angular momentum conservation under a central gravitational force that exerts no torque about the Sun.

Angular momentum conservation is ultimately a deep consequence of rotational symmetry in the laws of physics. Noether's theorem establishes that every symmetry of the laws corresponds to a conservation law: translational symmetry → linear momentum conservation; time symmetry → energy conservation; rotational symmetry → angular momentum conservation. This makes angular momentum one of the most fundamental quantities in all of physics, appearing everywhere from atomic electron orbitals to neutron star spin-ups.

---
id: work-and-energy
title: Work Done by a Force
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: dot-product
  type: soft
- id: work-as-integral
  type: soft
- id: definite-integral-definition
  type: soft
- id: friction-forces
  type: soft
- id: applications-integrals-area-mass
  type: soft
- id: work-as-force-times-distance
  type: soft
builds-toward:
- kinetic-energy
- potential-energy
- work-energy-theorem
tags:
- work
- energy
- dot-product
- force-displacement
stage: formal-systems
status: validated
---
# Work Done by a Force

## Core Idea
Work is the transfer of energy by a force acting over a displacement: W = F · d = Fd cosθ, where θ is the angle between the force and displacement vectors. Only the component of force along the direction of motion does work. For a variable force, work is the integral of force over displacement: W = ∫F dx. Work is a scalar measured in joules (N·m).

## How It's Best Learned
Start with constant forces at various angles and use the dot product formula. Then move to variable forces and compute work as the area under an F-x graph. Pay careful attention to sign: negative work means the force removes energy from the object.

## Common Misconceptions
- Thinking a large force always does a lot of work — if the object does not move or the force is perpendicular to motion, work is zero.
- Confusing work with effort: holding a heavy box stationary requires effort but does zero work in physics.
- Forgetting that work depends on displacement, not distance, when forces vary in direction.

## Questions

```yaml
- question: "A person carries a heavy box horizontally across a room at constant velocity. What is the net work done on the box?"
  type: multiple-choice
  options:
    - "Positive, equal to the carrying force times the distance"
    - "Equal to the weight of the box times the distance"
    - "Zero, because the kinetic energy does not change"
    - "Negative, because friction opposes the motion"
  answer: 2
  explanation: "Net work equals the change in kinetic energy (work-energy theorem). Since velocity is constant, ΔKE = 0, so net work = 0. The person's horizontal force does positive work, but friction does equal negative work, summing to zero. Note also that the person's upward supporting force and gravity act perpendicular to the horizontal displacement, contributing no work."

- question: "A force that is typically perpendicular to an object's velocity can do positive work on that object."
  type: true-false
  answer: false
  explanation: "Work is W = F·d·cosθ where θ is the angle between the force and displacement. When force is perpendicular to motion, θ = 90° and cos90° = 0, so W = 0 regardless of the force's magnitude. This is why gravity does no work on a horizontally moving object, and why the centripetal force in circular motion never changes the object's speed — it can change direction but cannot transfer energy."

- question: "A spring compressed by distance x is released and pushes a block until the block leaves the spring. How is the work done by the spring force calculated, and why can't you simply use W = Fd?"
  type: short-answer
  answer: "Work must be computed as the integral W = ∫F dx (the area under the force-displacement graph). For a spring, F = kx varies with position, so the simple product Fd applies only to constant forces. For a spring obeying Hooke's law, this integral gives W = ½kx²."
  explanation: "The formula W = Fd assumes a constant force in the direction of motion. Because the spring force changes continuously as it extends (F = kx decreasing from kx to 0), you must sum infinitesimal contributions — which is the definite integral. This connects directly to why calculus enters mechanics: real forces are rarely constant."
```

## Explainer

In everyday language, "work" means effort — a person straining to hold a heavy weight overhead is clearly working hard. But in physics, the word is defined precisely and the result can be counterintuitive: that same person holding the weight stationary does *zero* work on it. Physics defines work as the transfer of energy by a force acting over a displacement, and the crucial word is *displacement*. No displacement, no work — regardless of how much effort is involved.

The quantitative definition is W = F · d · cosθ, where θ is the angle between the applied force and the direction of motion. This dot product captures the insight that only the component of force *along* the direction of motion contributes to energy transfer. A force perpendicular to motion — like gravity on a horizontal projectile, or the centripetal force keeping a satellite in orbit — does no work at all. The satellite doesn't speed up or slow down because the force is always sideways to its path. You already know the dot product from mathematics; here it plays a concrete physical role.

The sign of work matters. When the force has a component in the same direction as displacement, W > 0: the force adds energy to the object. When the force opposes motion (like friction), W < 0: the force removes energy. This sign convention makes the work-energy theorem clean: the *net* work done on an object by all forces equals the change in its kinetic energy (ΔKE). Constant velocity means ΔKE = 0, so net work is always zero — useful as a check.

For variable forces, the definition generalizes to the integral W = ∫F dx: the area under the force-displacement curve. A spring is the standard example — the restoring force F = kx grows linearly with compression, so you cannot use the simple product formula. Integrating gives W = ½kx², the familiar spring energy expression. Graphically, this area is a triangle under the F-x line, which is a clean way to see why the factor of ½ appears.

Work is the bridge into the broader energy framework you will build next: kinetic energy, potential energy, and the work-energy theorem. The reason physicists care about work is precisely that it quantifies energy exchange between agents and objects, turning dynamics problems that would require tracking forces through every instant into accounting problems about energy before and after.

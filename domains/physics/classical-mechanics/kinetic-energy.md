---
id: kinetic-energy
title: Kinetic Energy
domain: physics
course: classical-mechanics
prerequisites:
- id: work-and-energy
  type: hard
- id: kinetic-energy-formula
  type: soft
- id: kinetic-energy-intro
  type: soft
- id: what-is-energy
  type: soft
builds-toward:
- work-energy-theorem
- conservation-of-energy
- collisions-elastic-inelastic
tags:
- kinetic-energy
- energy
- speed
- mass
stage: formal-systems
status: validated
---

# Kinetic Energy

## Core Idea
Kinetic energy is the energy an object possesses due to its motion: KE = ½mv². It is a scalar that depends on mass and the square of speed. Doubling speed quadruples kinetic energy. Kinetic energy is always non-negative and is measured in joules. It is the quantity that changes when work is done on a moving object.

## How It's Best Learned
Derive KE from the work-energy theorem: compute the net work done on an object starting from rest and show it equals ½mv². Then use KE in energy conservation problems to track how energy converts between kinetic and potential forms.

## Common Misconceptions
- Thinking KE is proportional to speed rather than speed squared — this is a critical error in energy comparisons.
- Treating KE as a vector: it is entirely a scalar and has no direction.

## Questions

```yaml
- question: "A car traveling at 30 m/s has a certain kinetic energy. If it speeds up to 60 m/s, what happens to its kinetic energy?"
  type: multiple-choice
  options: ["It doubles", "It triples", "It quadruples", "It increases by 30 m/s worth"]
  answer: 2
  explanation: "KE = ½mv². When speed doubles (30 → 60), speed² quadruples (900 → 3600), so KE quadruples. This is the critical difference between KE and momentum: momentum doubles when speed doubles, but KE quadruples."

- question: "Kinetic energy is a vector quantity because a moving object has a direction of motion."
  type: true-false
  answer: false
  explanation: "KE = ½mv² is entirely a scalar. The speed v in the formula is the magnitude of velocity, not velocity itself. Two objects moving in opposite directions at the same speed have identical kinetic energies. Direction matters for momentum (mv), not kinetic energy."

- question: "An object initially at rest has work W done on it by a net force. Explain why the object's resulting kinetic energy equals W."
  type: short-answer
  answer: "By the work-energy theorem, the net work done on an object equals its change in kinetic energy. Starting from rest (KE = 0), all the work goes into building kinetic energy: W = ΔKE = ½mv² - 0 = ½mv²."
  explanation: "This is the work-energy theorem in action. Work and kinetic energy are both measured in joules because work is the mechanism by which kinetic energy changes. Deriving KE from this relationship (rather than memorizing the formula) builds deep understanding of why the ½ and the v² appear."
```

## Explainer

You already know from studying work and energy that work is done when a force acts through a displacement. Kinetic energy is the payoff: it is what an object accumulates as work is done on it. If you start with an object at rest and push it with a constant net force over a distance d, you can use Newton's second law and kinematics to calculate how fast it ends up moving — and the work you did (F × d) turns out to equal exactly ½mv². This derivation is why the formula looks the way it does; the ½ and the v² are not arbitrary, they fall out of combining F = ma with kinematics.

The most important thing to internalize about kinetic energy is the squared relationship with speed. Doubling speed does not double KE — it quadruples it. This has dramatic real-world consequences: a car traveling 60 mph in a crash releases four times the kinetic energy of the same car at 30 mph, not twice. Engineers designing crumple zones, safety ratings, and speed limits take this nonlinearity seriously. Whenever you see a comparison involving speeds, ask yourself: am I comparing speeds or energies? The answers can look very different.

Kinetic energy is a scalar, not a vector. It has magnitude but no direction. A ball rolling north at 5 m/s and a ball rolling south at 5 m/s have identical kinetic energies. This is in sharp contrast to momentum (mv), which is a vector and does depend on direction. The distinction matters when you move on to collisions: in elastic collisions you conserve both momentum (a vector equation) and kinetic energy (a scalar equation), giving you two independent equations to work with.

Finally, note that KE is always non-negative. Because v² ≥ 0 and mass is always positive, an object either has positive kinetic energy (if moving) or zero kinetic energy (if at rest). There is no such thing as negative kinetic energy. This makes it a natural quantity to track in energy conservation problems: when KE decreases, that energy must have gone somewhere (into potential energy, heat, or work done on something else), and when it increases, energy must have come from somewhere.

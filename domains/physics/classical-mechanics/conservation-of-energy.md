---
id: conservation-of-energy
title: Conservation of Mechanical Energy
domain: physics
course: classical-mechanics
prerequisites:
- id: kinetic-energy
  type: hard
- id: potential-energy
  type: hard
- id: work-energy-theorem
  type: hard
- id: friction-forces
  type: soft
builds-toward:
- collisions-elastic-inelastic
- spring-mass-system
- orbital-mechanics
tags:
- conservation-of-energy
- mechanical-energy
- conservative-forces
stage: formal-systems
status: validated
---
# Conservation of Mechanical Energy

## Core Idea
When only conservative forces (gravity, spring) do work, the total mechanical energy E = KE + PE remains constant: KE_i + PE_i = KE_f + PE_f. Nonconservative forces like friction convert mechanical energy to thermal energy, so the conservation law must be modified: ΔKE + ΔPE = W_nc, where W_nc is the work done by nonconservative forces. Energy conservation is often the fastest route to finding speeds and heights in complex scenarios.

## How It's Best Learned
Identify initial and final states, then write the full energy equation including any nonconservative work. Practice roller-coaster and pendulum problems to build intuition for energy conversion between kinetic and potential forms.

## Common Misconceptions
- Applying the no-friction form of energy conservation when friction is present.
- Choosing an inconsistent height reference between initial and final states.
- Thinking energy is 'lost' in inelastic collisions — it converts to thermal/internal energy, not destroyed.

## Questions

```yaml
- question: "A 3 kg ball is released from rest at a height of 5 m (g = 10 m/s²). Assuming no air resistance, what is its speed just before it hits the ground?"
  type: multiple-choice
  options: ["5 m/s", "10 m/s", "15 m/s", "50 m/s"]
  answer: 1
  explanation: "Setting PE_i = KE_f: mgh = ½mv². The mass cancels, giving v = sqrt(2gh) = sqrt(2 × 10 × 5) = sqrt(100) = 10 m/s. Note that the mass does not matter — all objects dropped from the same height reach the same speed in the absence of air resistance."

- question: "When a block slides down a ramp with friction, the total mechanical energy (KE + PE) of the block is conserved."
  type: true-false
  answer: false
  explanation: "Friction is a nonconservative force that converts mechanical energy into thermal energy. The block's KE + PE decreases as it slides. The correct statement is that the *total energy* of the system (mechanical + thermal) is conserved — but mechanical energy alone is not."

- question: "A roller coaster car starts from rest at a height of 20 m. Using energy conservation (no friction), explain why its speed at the bottom does not depend on its mass."
  type: short-answer
  answer: "Setting initial PE equal to final KE: mgh = ½mv². When you solve for v, the mass m appears on both sides and cancels, giving v = sqrt(2gh). Speed at the bottom depends only on the height drop and gravitational acceleration, not on the mass of the car."
  explanation: "This is a direct consequence of both kinetic energy (½mv²) and gravitational potential energy (mgh) being proportional to mass. The mass factor cancels algebraically, so energy conservation predicts the same final speed for any mass dropped from the same height — consistent with Galileo's observation that objects of different mass fall at the same rate."
```

## Explainer

The work-energy theorem you studied earlier tells you that the net work done on an object equals its change in kinetic energy. Conservation of energy takes this further by splitting forces into two categories: *conservative* forces (like gravity and springs) that store energy in a way that can be fully recovered, and *nonconservative* forces (like friction and air resistance) that convert mechanical energy into forms — heat, sound — that can't be recovered as motion.

When only conservative forces act, something remarkable happens: the sum of kinetic and potential energy stays constant throughout the motion. A ball thrown upward slows down, but the kinetic energy it loses is exactly stored as gravitational potential energy. When it falls back down, that stored energy returns as kinetic energy. At any point along the path: KE + PE = constant. This lets you solve for speeds and heights at any point without tracking the detailed path — just identify the starting and ending states.

The height you choose as your reference for potential energy (PE = 0) is arbitrary, because only *differences* in PE matter. What's critical is using the *same* reference throughout a problem. If you set the ground as PE = 0 at the start of a calculation, it must remain the ground for all subsequent states. A common mistake is implicitly shifting the reference partway through, which produces wrong answers without any obvious algebraic error.

When friction is present, you have to account for the work it does. Friction converts mechanical energy to thermal energy, so KE_f + PE_f = KE_i + PE_i − |W_friction|. The mechanical energy of the sliding object decreases, but the thermal energy of the surfaces increases by the same amount. Total energy is always conserved — the first law of thermodynamics — but in physics problems involving friction, that thermal energy is usually outside the scope of what you are tracking. The practical rule: before applying the simple KE + PE = constant form, always check whether friction or other nonconservative forces are present.

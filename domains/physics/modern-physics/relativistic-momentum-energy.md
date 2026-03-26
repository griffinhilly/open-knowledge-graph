---
id: relativistic-momentum-energy
title: Relativistic Momentum and Energy
domain: physics
course: modern-physics
prerequisites:
- id: lorentz-transformation
  type: hard
- id: momentum-and-impulse
  type: hard
- id: kinetic-energy
  type: hard
- id: relativistic-velocity-addition
  type: soft
builds-toward:
- mass-energy-equivalence
- pair-production-annihilation
tags:
- relativity
- momentum
- energy
- four-vector
stage: advanced
status: validated
---
# Relativistic Momentum and Energy

## Core Idea
In special relativity, momentum is redefined as p = γmv so that it is conserved in all inertial frames. The total relativistic energy is E = γmc², which includes both the kinetic energy and the rest energy mc². The kinetic energy is K = (γ−1)mc², recovering ½mv² in the low-speed limit. These quantities form a four-vector (E/c, p), whose invariant magnitude is (mc²)² = E² − (pc)², a relation that holds for massless photons as well.

## How It's Best Learned
Work through elastic collisions in two frames to see why the classical p = mv fails, then verify γmv is conserved. Expand γ in a Taylor series to recover the Newtonian limit. Use the energy-momentum relation E²=(pc)²+(mc²)² to solve problems without picking a frame.

## Common Misconceptions
- Mass increases with velocity — it is more precise to say relativistic momentum grows with γ; rest mass m is a Lorentz invariant.
- Kinetic energy is still ½mv² — that formula fails badly at high speeds; the correct expression is (γ−1)mc².

## Questions

```yaml
- question: "An electron is accelerated to 99% of the speed of light (v = 0.99c, γ ≈ 7). A student says 'the electron's mass has increased by a factor of 7.' What is the most precise modern assessment of this statement?"
  type: multiple-choice
  options:
    - "Correct — relativistic mass increases with velocity, so the electron is effectively about 7 times heavier."
    - "Incorrect — the electron's rest mass m is a Lorentz invariant unchanged by its speed. What increases by γ is the electron's momentum, not its mass."
    - "Incorrect — at 0.99c, quantum effects dominate and the classical concept of mass no longer applies."
    - "Partially correct — the electron's inertia increases, meaning it behaves like it has 7 times more mass for practical purposes."
  answer: 1
  explanation: "Rest mass m is a Lorentz invariant — it has the same value in every reference frame and does not change with velocity. The notion of 'relativistic mass' γm is an outdated framing. What does increase with γ is the momentum: p = γmv grows dramatically as v approaches c. The practical consequence (the electron is increasingly hard to accelerate further) is real, but it arises because momentum and energy grow, not because mass increases. Modern physics reserves 'mass' for the invariant rest mass."

- question: "A photon has zero rest mass. According to the energy-momentum relation E² = (pc)² + (mc²)², what does this imply about a photon's energy and momentum?"
  type: multiple-choice
  options:
    - "A photon has zero energy since E² = (pc)² gives E = pc = 0 for a massless particle."
    - "A photon has energy E = pc, so it carries momentum proportional to its energy despite having no rest mass."
    - "The energy-momentum relation does not apply to photons, which must be treated using quantum mechanics instead."
    - "A photon has only rest energy mc² = 0, confirming it has no energy at all."
  answer: 1
  explanation: "Setting m = 0 gives E² = (pc)², so E = pc. Photons carry momentum p = E/c despite having no rest mass — a purely relativistic result with no Newtonian analogue, and the reason light exerts radiation pressure. The energy-momentum relation is universally valid for all particles, massive or massless, in any reference frame. This frame-independence is precisely why it is so useful: you never need to pick a specific frame to apply it."

- question: "At low velocities (v << c), the relativistic kinetic energy formula K = (γ−1)mc² reduces to the familiar Newtonian expression ½mv²."
  type: true-false
  answer: true
  explanation: "At low speeds, γ = 1/√(1 − v²/c²) ≈ 1 + v²/2c² (first-order Taylor expansion). Therefore K = (γ − 1)mc² ≈ (v²/2c²)mc² = ½mv². This is the required correspondence principle: any correct relativistic formula must reduce to the Newtonian result at everyday speeds. Relativistic mechanics is not a replacement for Newtonian mechanics — it is a generalization that contains Newton's laws as a special case in the low-velocity limit."

- question: "In special relativity, the rest mass of a particle increases as it moves faster, which is why it becomes very difficult to accelerate a massive particle to the speed of light."
  type: true-false
  answer: false
  explanation: "Rest mass is a Lorentz invariant — it does not change with velocity. The reason a massive particle cannot reach the speed of light is that its momentum p = γmv diverges as v → c (because γ → ∞), requiring infinite energy to continue accelerating. The barrier is not growing mass but growing momentum: each additional increment of speed toward c requires exponentially more energy. 'Mass increases' is an old pedagogical shorthand that conflates invariant rest mass with the γ-factor in momentum."

- question: "Why must relativistic momentum be defined as p = γmv rather than the classical p = mv?"
  type: short-answer
  answer: "Because classical momentum p = mv is not conserved in all inertial frames. When two observers apply conservation of momentum to a collision using p = mv, they disagree on whether momentum was conserved. Defining momentum using proper time — p = m(dx/dτ) = γmv — produces a quantity that is conserved in every inertial frame, as required by the principle of relativity."
  explanation: "The motivation is physical necessity, not mathematical convenience. Proper time τ is the time measured in the particle's own rest frame — a Lorentz-invariant quantity. Differentiating position with respect to proper time (rather than coordinate time) automatically builds in the γ factor. The result is a momentum that all inertial observers agree is conserved in collisions, which is the foundational requirement for the concept of momentum to be physically meaningful."
```

## Explainer

Classical mechanics works beautifully at everyday speeds, but it breaks down when objects approach the speed of light. You already know from the Lorentz transformation that space and time mix together in special relativity — lengths contract and clocks dilate depending on your reference frame. The same logic forces us to revise momentum. If two observers in different inertial frames apply conservation of momentum using the classical formula p = mv, they find it isn't conserved. The fix is to replace time with **proper time** τ (the time measured in the object's own rest frame), defining relativistic momentum as **p = m(dx/dτ) = γmv**, where γ = 1/√(1 − v²/c²) is the Lorentz factor. With this redefinition, momentum is conserved in every inertial frame.

Energy follows from the same logic. The relativistic kinetic energy isn't ½mv² — it's the work done accelerating a particle from rest to speed v using the relativistic force law. Working through this integral yields **K = (γ − 1)mc²**. The extra term mc² doesn't vanish when v = 0; it is the **rest energy**, the energy a particle has simply by virtue of having mass. The total relativistic energy is therefore **E = γmc²**, which includes both the kinetic energy of motion and the rest-mass energy. At low speeds, γ ≈ 1 + v²/2c², so K ≈ ½mv² exactly recovers Newton's formula — a necessary sanity check.

The deepest structure here is the **energy-momentum four-vector**. Just as position and time form the spacetime four-vector (ct, x, y, z), energy and momentum form the four-vector (E/c, pₓ, pᵧ, p_z). The invariant magnitude of this four-vector — the quantity that all observers agree on regardless of their frame — is (mc²)². Working it out gives the **energy-momentum relation**: E² = (pc)² + (mc²)². This single equation is enormously useful: it works for massive particles, and it also works for massless photons (where m = 0), giving E = pc. You never need to pick a specific reference frame to use it.

One common conceptual trap: it is sometimes said that mass "increases" with velocity. This framing is outdated. The rest mass m is a Lorentz invariant — every observer measures the same value. What grows with speed is the momentum (because γ grows), not the mass itself. Keeping this straight matters when you get to pair production and annihilation, where rest-mass energy converts to kinetic energy and radiation. The invariant E² − (pc)² = (mc²)² is the rigorous statement of what is actually conserved and frame-independent.

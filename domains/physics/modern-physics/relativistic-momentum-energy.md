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

## Explainer

Classical mechanics works beautifully at everyday speeds, but it breaks down when objects approach the speed of light. You already know from the Lorentz transformation that space and time mix together in special relativity — lengths contract and clocks dilate depending on your reference frame. The same logic forces us to revise momentum. If two observers in different inertial frames apply conservation of momentum using the classical formula p = mv, they find it isn't conserved. The fix is to replace time with **proper time** τ (the time measured in the object's own rest frame), defining relativistic momentum as **p = m(dx/dτ) = γmv**, where γ = 1/√(1 − v²/c²) is the Lorentz factor. With this redefinition, momentum is conserved in every inertial frame.

Energy follows from the same logic. The relativistic kinetic energy isn't ½mv² — it's the work done accelerating a particle from rest to speed v using the relativistic force law. Working through this integral yields **K = (γ − 1)mc²**. The extra term mc² doesn't vanish when v = 0; it is the **rest energy**, the energy a particle has simply by virtue of having mass. The total relativistic energy is therefore **E = γmc²**, which includes both the kinetic energy of motion and the rest-mass energy. At low speeds, γ ≈ 1 + v²/2c², so K ≈ ½mv² exactly recovers Newton's formula — a necessary sanity check.

The deepest structure here is the **energy-momentum four-vector**. Just as position and time form the spacetime four-vector (ct, x, y, z), energy and momentum form the four-vector (E/c, pₓ, pᵧ, p_z). The invariant magnitude of this four-vector — the quantity that all observers agree on regardless of their frame — is (mc²)². Working it out gives the **energy-momentum relation**: E² = (pc)² + (mc²)². This single equation is enormously useful: it works for massive particles, and it also works for massless photons (where m = 0), giving E = pc. You never need to pick a specific reference frame to use it.

One common conceptual trap: it is sometimes said that mass "increases" with velocity. This framing is outdated. The rest mass m is a Lorentz invariant — every observer measures the same value. What grows with speed is the momentum (because γ grows), not the mass itself. Keeping this straight matters when you get to pair production and annihilation, where rest-mass energy converts to kinetic energy and radiation. The invariant E² − (pc)² = (mc²)² is the rigorous statement of what is actually conserved and frame-independent.

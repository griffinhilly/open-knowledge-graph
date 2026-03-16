---
id: four-momentum-energy-conservation
title: Four-Momentum and Energy-Momentum Conservation
domain: physics
course: modern-physics
prerequisites:
- id: relativistic-dynamics-acceleration
  type: hard
- id: relativistic-momentum-energy
  type: soft
builds-toward:
- invariant-mass-rest-frame
- pair-annihilation-creation-threshold
tags:
- special-relativity
- four-vectors
- conservation-laws
stage: advanced
status: draft
---

# Four-Momentum and Energy-Momentum Conservation

## Core Idea
Four-momentum combines energy and three-momentum into a single four-vector: p_μ = (E/c, p⃗). The magnitude p·p is an invariant equal to (mc)². Conservation of four-momentum in particle interactions automatically enforces conservation of both energy and 3-momentum, and provides a powerful relativistic approach to collision and decay problems.

## How It's Best Learned
Work with specific examples: elastic collisions, particle decay, and pair production. Use four-momentum conservation to derive threshold energies. Recognize that invariant mass M of a system satisfies M²c⁴ = (Σp_μ)·(Σp_μ).

## Common Misconceptions
Four-momentum is not simply (E, pc⃗) with factors of c inconsistently applied. The fourth component must be E/c or γmc depending on your metric convention.

## Explainer

From your study of relativistic dynamics, you know that the energy of a particle is E = γmc² and its relativistic momentum is p⃗ = γmv⃗. These two quantities are no longer independent in special relativity — they are linked by the relation E² = (pc)² + (mc²)². This is not a coincidence but reflects a deep structure: energy and momentum are the time and space components of a single geometric object called the **four-momentum** p_μ = (E/c, p_x, p_y, p_z).

The power of combining energy and momentum into a four-vector lies in what happens when you compute its "length" using the spacetime metric. Just as the spacetime interval s² = c²t² − x² − y² − z² is invariant under Lorentz boosts, the "length squared" of the four-momentum is p_μp^μ = (E/c)² − |p⃗|² = (mc)². This is the **invariant mass relation** — it is the same number in every reference frame. In the rest frame, p⃗ = 0 and E = mc², so the invariant reduces trivially to (mc)². In any boosted frame, E and |p⃗| both change, but they change in exactly the right way to keep (E/c)² − p² constant. The invariant mass m is a frame-independent property of the particle.

Conservation of four-momentum in a collision means both energy and three-momentum are conserved simultaneously — you do not need to apply two separate conservation laws. For a reaction A + B → C + D, you write p_A^μ + p_B^μ = p_C^μ + p_D^μ as a single four-vector equation. The real payoff comes from working in strategically chosen reference frames. To find a **threshold energy** (the minimum energy to create new particles), work in the center-of-momentum frame where the total three-momentum is zero and all the kinetic energy goes into creating rest mass. The invariant (Σp_μ)·(Σp_μ) = M²c² where M is the total invariant mass of the system is the same in every frame, so you can compute it in the lab frame (where you know the projectile's energy) and set it equal to the minimum rest-mass energy in the CM frame.

As a concrete example, consider a proton colliding with a stationary proton to create a new proton-antiproton pair (p + p → p + p + p + p̄). The four-momentum of the incoming system has invariant mass-squared M²c⁴ = (E_lab + mc²)² − (p_lab c)² = 2mc²(E_lab + mc²). At threshold, all four final particles are produced at rest in the CM frame, giving M²c⁴ = (4mc²)² = 16m²c⁴. Setting these equal and solving gives E_lab = 7mc² — the projectile must have kinetic energy T = 6mc² ≈ 5.6 GeV. This calculation, which would be extremely awkward using three-momentum and energy conservation separately in the lab frame, takes just two lines with four-momentum invariants. This is why every particle physicist works fluently with four-vectors.

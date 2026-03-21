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

## Questions

```yaml
- question: "A particle physicist wants to find the threshold energy for a proton to produce a proton-antiproton pair colliding with a stationary proton. What is the strategic advantage of computing the four-momentum invariant?"
  type: multiple-choice
  options:
    - "It allows working in the lab frame where the calculations are simplest"
    - "The invariant p_μp^μ is the same in all frames, so it can be computed in the convenient lab frame and set equal to the minimum rest-mass energy in the center-of-momentum frame"
    - "It replaces the need for energy conservation, leaving only momentum to track"
    - "It converts the relativistic problem into a Newtonian approximation valid near threshold"
  answer: 1
  explanation: "The power of the four-momentum invariant is frame independence. In the lab frame, you know the projectile energy, so you can compute (Σp_μ)·(Σp_μ) easily. In the CM frame, threshold corresponds to all final particles at rest, giving M²c⁴ = (sum of rest masses × c²)². Setting these equal across frames — possible because the invariant is the same in all frames — yields the threshold energy in just two lines. The common misconception (option A) reverses the logic: the lab frame is where you know the givens, not where calculations are simplest; you equate invariants across frames."

- question: "A student calculates the threshold for p + p → p + p + p + p̄ by setting total kinetic energy equal to 2mc² (the rest mass of the new pair) and gets T = 2mc². What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "She should use four-momentum, not kinetic energy, as the conserved quantity"
    - "In the lab frame, the threshold requires T = 6mc² — not 2mc² — because in the lab frame significant kinetic energy must remain in the final-state particles; only in the CM frame can all energy go into rest mass"
    - "She forgot that the antiproton has negative energy in the lab frame, requiring an additional mc² correction"
    - "Kinetic energy and rest mass energy cannot be equated because they have different units in relativity"
  answer: 1
  explanation: "The student is conflating the lab-frame threshold with the CM-frame argument. In the CM frame, at threshold all four final particles are at rest, so M²c⁴ = (4mc²)². Computing this invariant in the lab frame (one proton stationary, one with energy E) gives M²c⁴ = 2mc²(E + mc²). Setting these equal gives E = 7mc², meaning the projectile kinetic energy T = E − mc² = 6mc². The error of setting T = 2mc² assumes you can dump all kinetic energy into new rest mass from the lab frame, ignoring that the final system must still have center-of-mass motion."

- question: "The invariant p_μp^μ = (mc)² has the same value in all inertial reference frames, so its value computed in the lab frame equals its value in the center-of-momentum frame."
  type: true-false
  answer: true
  explanation: "Frame invariance is the defining property of a Lorentz scalar, and p_μp^μ = (E/c)² − |p⃗|² is precisely such a scalar. In the rest frame, p⃗ = 0 and E = mc², giving (mc)². In any boosted frame, E and |p⃗| each change but change in exactly the right way to keep the combination constant. This invariance is what makes the 'compute in one frame, equate in another' strategy for threshold calculations valid."

- question: "When four-momentum is conserved in a particle collision, energy conservation and three-momentum conservation are separate, independent conditions that must each be checked."
  type: true-false
  answer: false
  explanation: "Conservation of four-momentum is a single four-vector equation p_A^μ + p_B^μ = p_C^μ + p_D^μ, which simultaneously enforces both energy conservation (the time component) and three-momentum conservation (the three spatial components). They are not independent conditions to verify separately — they are components of the same unified law. This unity is one of the main reasons four-vector notation is used: what would otherwise be four separate equations is expressed as one."

- question: "Explain why the invariant mass of the four-momentum is useful for solving relativistic collision problems. What does it allow you to do that treating energy and momentum separately does not?"
  type: short-answer
  answer: "The invariant mass is the same in every reference frame, so you can compute it in whichever frame is most convenient and then apply the result in any other frame. For threshold problems, you compute the invariant in the lab frame (where you know the energies and momenta) and set it equal to the minimum rest-mass energy in the CM frame (where the threshold condition is simplest to state). Treating energy and momentum separately locks you into one frame and forces you to track all components simultaneously."
  explanation: "The strategy is: (1) compute the Lorentz-invariant (Σp_μ)² in the lab frame using known quantities, (2) set it equal to its value in the CM frame where the threshold condition is easy to state, (3) solve. This cross-frame equating is impossible when working with energy and momentum as separate non-invariant quantities. The invariant mass is the 'currency' that converts cleanly between frames, which is why particle physicists call it one of the most useful tools in relativistic kinematics."
```

## Explainer

From your study of relativistic dynamics, you know that the energy of a particle is E = γmc² and its relativistic momentum is p⃗ = γmv⃗. These two quantities are no longer independent in special relativity — they are linked by the relation E² = (pc)² + (mc²)². This is not a coincidence but reflects a deep structure: energy and momentum are the time and space components of a single geometric object called the **four-momentum** p_μ = (E/c, p_x, p_y, p_z).

The power of combining energy and momentum into a four-vector lies in what happens when you compute its "length" using the spacetime metric. Just as the spacetime interval s² = c²t² − x² − y² − z² is invariant under Lorentz boosts, the "length squared" of the four-momentum is p_μp^μ = (E/c)² − |p⃗|² = (mc)². This is the **invariant mass relation** — it is the same number in every reference frame. In the rest frame, p⃗ = 0 and E = mc², so the invariant reduces trivially to (mc)². In any boosted frame, E and |p⃗| both change, but they change in exactly the right way to keep (E/c)² − p² constant. The invariant mass m is a frame-independent property of the particle.

Conservation of four-momentum in a collision means both energy and three-momentum are conserved simultaneously — you do not need to apply two separate conservation laws. For a reaction A + B → C + D, you write p_A^μ + p_B^μ = p_C^μ + p_D^μ as a single four-vector equation. The real payoff comes from working in strategically chosen reference frames. To find a **threshold energy** (the minimum energy to create new particles), work in the center-of-momentum frame where the total three-momentum is zero and all the kinetic energy goes into creating rest mass. The invariant (Σp_μ)·(Σp_μ) = M²c² where M is the total invariant mass of the system is the same in every frame, so you can compute it in the lab frame (where you know the projectile's energy) and set it equal to the minimum rest-mass energy in the CM frame.

As a concrete example, consider a proton colliding with a stationary proton to create a new proton-antiproton pair (p + p → p + p + p + p̄). The four-momentum of the incoming system has invariant mass-squared M²c⁴ = (E_lab + mc²)² − (p_lab c)² = 2mc²(E_lab + mc²). At threshold, all four final particles are produced at rest in the CM frame, giving M²c⁴ = (4mc²)² = 16m²c⁴. Setting these equal and solving gives E_lab = 7mc² — the projectile must have kinetic energy T = 6mc² ≈ 5.6 GeV. This calculation, which would be extremely awkward using three-momentum and energy conservation separately in the lab frame, takes just two lines with four-momentum invariants. This is why every particle physicist works fluently with four-vectors.

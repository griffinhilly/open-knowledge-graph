---
id: born-oppenheimer-approximation
title: The Born-Oppenheimer Approximation
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: partial-derivatives
  type: soft
- id: schrodinger-equation-intro
  type: soft
- id: wave-particle-duality
  type: soft
builds-toward:
- molecular-orbital-theory-advanced
- potential-energy-surfaces
- vibrational-spectroscopy-theory
tags:
- approximation
- nuclear-motion
- electronic-structure
- potential-energy-surface
stage: advanced
status: validated
---

# The Born-Oppenheimer Approximation

## Core Idea
The Born-Oppenheimer (BO) approximation separates nuclear and electronic motion by exploiting the large mass difference between electrons and nuclei: nuclei move so slowly relative to electrons that electrons instantaneously adjust to any nuclear configuration. This allows the total molecular wavefunction to be factored into an electronic part (solved for fixed nuclear positions) and a nuclear part (moving on the electronic potential energy surface). The BO approximation is the conceptual foundation for potential energy surfaces, molecular geometry, and most of computational chemistry. It breaks down in cases of closely spaced electronic states (conical intersections) or very fast nuclear dynamics.

## How It's Best Learned
Understand the physical reasoning first — electrons move ~1000× faster than nuclei — before tackling the mathematical separation of the Hamiltonian. Then see how the electronic energy as a function of geometry becomes the potential for nuclear motion.

## Common Misconceptions
- Thinking BO is exact; it is an approximation that fails near conical intersections.
- Confusing 'fixed nuclei' with 'stationary nuclei' — the approximation is about timescales, not that nuclei don't move.

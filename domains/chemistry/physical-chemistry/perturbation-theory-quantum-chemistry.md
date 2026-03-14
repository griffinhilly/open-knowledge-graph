---
id: perturbation-theory-quantum-chemistry
title: Perturbation Theory in Quantum Chemistry
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: born-oppenheimer-approximation
  type: hard
builds-toward:
- post-hartree-fock-methods
- configuration-interaction-methods
tags:
- quantum
- perturbation
- approximation
- computational
stage: advanced
status: draft
---

# Perturbation Theory in Quantum Chemistry

## Core Idea
Perturbation theory systematically improves upon an initial quantum solution by treating small deviations as perturbations. In chemistry, first- and second-order perturbation theory (MP1, MP2) provide accurate estimates of correlation energy by expanding electron-electron interactions beyond mean-field approximations. This approach bridges the computational gap between simple Hartree-Fock and full configuration interaction.

## How It's Best Learned
Derive first-order energy correction from electron-electron repulsion using perturbation formalism; implement MP2 calculations on water and benzene; compare MP2 results to experimental bond energies and compare computational cost (order N⁵) to other methods.

## Common Misconceptions
- Assuming perturbation order directly corresponds to accuracy; MP2 is excellent for correlation energy but sometimes worse than Hartree-Fock for geometries. - Forgetting that perturbation theory assumes a good zeroth-order approximation; it fails if the unperturbed solution is qualitatively wrong.

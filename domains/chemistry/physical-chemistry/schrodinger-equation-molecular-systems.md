---
id: schrodinger-equation-molecular-systems
title: Schrödinger Equation for Molecular Systems
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: hydrogen-atom-wavefunctions
  type: hard
builds-toward:
- variational-principle-quantum-chemistry
- molecular-orbital-theory-advanced
tags:
- quantum
- molecular
- wavefunctions
- schrodinger
stage: advanced
status: draft
---

# Schrödinger Equation for Molecular Systems

## Core Idea
The time-independent Schrödinger equation describes molecular systems by relating the Hamiltonian operator (kinetic + potential energy) to molecular wavefunctions. For molecules, the Born-Oppenheimer approximation separates electronic and nuclear motion, allowing us to solve for electronic structure at fixed nuclear positions. This equation is the foundation for understanding bonding, spectroscopy, and reaction mechanisms.

## How It's Best Learned
Start with H₂⁺ ion as the simplest molecular system, compare results to hydrogen atom. Then progress to more complex molecules using variational methods and basis set approximations. Numerical solvers and visualization tools help understand the meaning of molecular wavefunctions.

## Common Misconceptions
- Thinking the wavefunction itself is observable (it's the probability density that matters).
- Assuming the Born-Oppenheimer approximation works equally well for all molecules (fails for light nuclei or very fast nuclear motion).

---
id: ising-model-statmech
title: The Ising Model and Magnetic Transitions
domain: physics
course: statistical-mechanics
prerequisites:
- id: canonical-ensemble
  type: hard
- id: phase-transition-equilibrium
  type: soft
builds-toward:
- mean-field-theory-statmech
- monte-carlo-statistical-mechanics
tags:
- ising-model
- magnetism
- phase-transition
stage: advanced
status: draft
---

# The Ising Model and Magnetic Transitions

## Core Idea
The Ising model represents a magnetic system as a lattice of spins σ_i = ±1 coupled by nearest-neighbor interactions. The Hamiltonian is H = -J Σ σ_i σ_j - h Σ σ_i. It exhibits a ferromagnetic phase transition at T_c in d ≥ 2. The 2D Ising model is exactly solvable (Onsager); in higher dimensions, it reveals universal critical behavior.

---
id: quantum-numbers
title: Quantum Numbers
domain: physics
course: modern-physics
prerequisites:
- id: bohr-model
  type: hard
- id: schrodinger-equation-intro
  type: soft
- id: particle-in-a-box
  type: soft
builds-toward:
- atomic-orbitals
- spin-quantum-number
tags:
- quantum
- hydrogen
- principal
- angular-momentum
- magnetic
- quantum-numbers
stage: advanced
status: validated
---
# Quantum Numbers

## Core Idea
The full quantum mechanical treatment of the hydrogen atom yields four quantum numbers. The principal quantum number n = 1, 2, 3, … determines the energy level. The orbital angular momentum quantum number ℓ = 0, 1, …, n−1 determines the shape of the orbital. The magnetic quantum number m_ℓ = −ℓ, …, +ℓ determines the orientation of the orbital in a magnetic field. The spin quantum number m_s = ±½ describes the intrinsic angular momentum of the electron. Together they uniquely label each quantum state of a hydrogen electron.

## How It's Best Learned
Build up from Bohr (n only) to include ℓ (angular momentum quantization from solving the 3D Schrödinger equation) and m_ℓ (projection). Introduce spin separately as an experimental fact (Stern–Gerlach) before showing it requires a relativistic treatment (Dirac equation) for its full explanation.

## Common Misconceptions
- n alone determines everything about the state — n gives the energy (for hydrogen), but ℓ and m_ℓ specify the orbital shape and orientation; all four numbers are needed to specify the state.
- ℓ can equal n — ℓ ranges from 0 to n−1; ℓ = n is not allowed.

---
id: angular-momentum-quantum
title: Quantum Angular Momentum
domain: physics
course: quantum-mechanics
prerequisites:
- id: commutation-relations
  type: hard
- id: conservation-of-angular-momentum
  type: soft
- id: eigenvalues-eigenvectors
  type: hard
builds-toward:
- orbital-angular-momentum-quantum
- spin-angular-momentum
tags:
- angular-momentum
- rotation
- symmetry
stage: advanced
status: draft
---

# Quantum Angular Momentum

## Core Idea
Quantum angular momentum operators L̂ₓ, L̂ᵧ, L̂ᵧ satisfy canonical commutation relations [L̂ᵢ, L̂ⱼ] = iℏεᵢⱼₖL̂ₖ. The total angular momentum squared L̂² commutes with each component, so L̂² and one component (typically L̂ᵧ) can be simultaneously diagonalized. Eigenvalues of L̂ᵧ are mℏ where m = -l, -l+1, …, l-1, l and l is the angular momentum quantum number.

## Explainer

In classical mechanics you already know, angular momentum is a continuous vector L = r × p that can point in any direction and take any magnitude. Quantum mechanics replaces this with operators, and the commutation relations you studied tell you something profound: you cannot simultaneously know all three components of angular momentum. Specifically, [L̂ₓ, L̂ᵧ] = iℏL̂_z means measuring L̂ₓ disturbs L̂ᵧ. This is a direct consequence of the algebra, not an experimental accident.

The way out is to find what you *can* measure simultaneously. The total angular momentum squared L̂² = L̂ₓ² + L̂ᵧ² + L̂_z² commutes with each component: [L̂², L̂_z] = 0. This means you can simultaneously have definite values for the *magnitude* of angular momentum and *one* component (conventionally chosen as L̂_z). The shared eigenstates |l, m⟩ are labeled by two quantum numbers: **l** (the angular momentum quantum number, a non-negative integer or half-integer) and **m** (the magnetic quantum number, ranging from −l to +l in integer steps). The eigenvalue equations are L̂²|l,m⟩ = ℏ²l(l+1)|l,m⟩ and L̂_z|l,m⟩ = mℏ|l,m⟩.

The quantization of l to integer steps is not imposed by hand — it falls out of the algebra. The key argument uses **ladder operators** L̂₊ = L̂ₓ + iL̂ᵧ and L̂₋ = L̂ₓ − iL̂ᵧ, which raise and lower the m quantum number by 1. Since m must be bounded (you cannot have a component larger than the total magnitude), the ladder must terminate. The requirement that the ladder terminates at both ends — L̂₊|l,l⟩ = 0 and L̂₋|l,−l⟩ = 0 — forces l to be a non-negative integer or half-integer and restricts m to the 2l + 1 values from −l to +l.

The physical picture that helps: think of the angular momentum vector as having a fixed magnitude ℏ√(l(l+1)) and a definite projection mℏ onto the z-axis, but its orientation in the x-y plane is completely uncertain. The vector "precesses" around the z-axis in a way you cannot track — which is exactly what the uncertainty principle between L̂ₓ and L̂ᵧ enforces. This structure is the foundation for everything that follows: orbital angular momentum gives the l = 0, 1, 2, … states of the hydrogen atom, while spin angular momentum extends the framework to half-integer l, leading to the electron spin states you will study next.

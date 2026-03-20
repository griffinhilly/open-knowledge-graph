---
id: angular-momentum-quantization
title: Angular Momentum Quantization
domain: physics
course: quantum-mechanics
prerequisites:
- id: operators-and-observables
  type: hard
- id: commutation-relations
  type: hard
builds-toward:
- spin-half-systems
- angular-momentum-addition
- hydrogen-atom-solution
tags:
- angular-momentum
- quantization
stage: advanced
status: draft
---

# Angular Momentum Quantization

## Core Idea
Angular momentum operators satisfy [Lᵢ, Lⱼ] = iℏεᵢⱼₖLₖ, implying L² and Lz have eigenvalues ℏ²ℓ(ℓ+1) and mℏ respectively, where ℓ = 0,½,1,... and m = -ℓ,...,ℓ. This quantization emerges from commutation relations, not boundary conditions.

## Explainer

From your work on operators and observables, you know that compatible observables share a common eigenbasis (they commute), while incompatible ones do not. Angular momentum components Lx, Ly, Lz are pairwise incompatible: [Lx, Ly] = iℏLz, and its cyclic permutations. This means you cannot simultaneously assign sharp values to all three components. What you *can* do is find the simultaneous eigenstates of L² (the total squared angular momentum) and any one component, conventionally Lz, since [L², Lᵢ] = 0 for all i.

The derivation of allowed values is purely algebraic — it is one of the most elegant results in quantum mechanics. You define **ladder operators** L± = Lx ± iLy and use the commutation relations to show that L± raises or lowers the Lz eigenvalue by ℏ. Since L² has a fixed eigenvalue for a given state, the eigenvalues of Lz must be bounded above and below (you cannot have a component larger than the magnitude). For the ladder to terminate at both ends, the eigenvalues of Lz must be of the form mℏ where m steps in integer increments between −ℓ and +ℓ. The total L² eigenvalue is then ℏ²ℓ(ℓ+1), not ℏ²ℓ² — a subtle but important distinction arising from the non-commutativity.

The striking feature is that ℓ can be either an integer (0, 1, 2, ...) or a half-integer (½, 3/2, ...). Integer values appear for **orbital angular momentum** (motion of a particle in space), which you can also derive from the spatial wavefunction using boundary conditions. Half-integer values have no classical analog — they describe **spin**, an intrinsic angular momentum that cannot be represented as spatial rotation. The existence of half-integer representations is forced by the algebra alone, which is why spin-½ particles (electrons, quarks) fit naturally into the same quantum mechanical framework as orbital angular momentum, even though spin is not literally spinning.

Physically, the quantum number ℓ tells you the magnitude of angular momentum (√(ℓ(ℓ+1)) ℏ), while m tells you the projection onto the quantization axis. For a given ℓ there are 2ℓ+1 values of m, corresponding to the 2ℓ+1 degenerate states that differ only in the orientation of the angular momentum vector. This degeneracy is broken by external fields — a fact that drives the Zeeman effect and underpins the structure of the periodic table. Angular momentum quantization connects directly to the hydrogen atom solution, where the quantum numbers ℓ and m label the orbitals (s, p, d, f) you may recognize from chemistry.

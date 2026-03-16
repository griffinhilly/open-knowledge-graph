---
id: orbital-angular-momentum-quantum
title: Orbital Angular Momentum in Quantum Mechanics
domain: physics
course: quantum-mechanics
prerequisites:
- id: commutation-relations
  type: hard
- id: differential-equations
  type: hard
builds-toward:
- total-angular-momentum
- hydrogen-atom-solution
tags:
- angular-momentum
- quantum-mechanics
stage: formal-systems
status: draft
---

# Orbital Angular Momentum in Quantum Mechanics

## Core Idea
Orbital angular momentum L⃗ = r⃗ × p⃗ is quantized with [L̂_i, L̂_j] = iℏ ε_{ijk} L̂_k. Only one component and magnitude are simultaneously measurable with eigenvalues ℏm_l and ℏ²l(l+1).

## Explainer

Classically, angular momentum is the vector L⃗ = r⃗ × p⃗: it has three components L_x, L_y, L_z, all of which you can know simultaneously. In quantum mechanics you can write the same formula using the corresponding operators, but the commutation relations your prerequisites introduced change everything. The key result is [L̂_x, L̂_y] = iℏL̂_z, and cyclically for the other pairs. Because no two components commute, only *one* component can have a definite value at a time. The conventional choice is L̂_z, measured in units of ℏ.

The magnitude-squared operator L̂² = L̂_x² + L̂_y² + L̂_z² does commute with each individual component: [L̂², L̂_z] = 0. This is what allows you to simultaneously know the total magnitude and one component. The eigenvalues work out to |L|² = ℏ²l(l+1) and L_z = ℏm_l, where **l** (the orbital quantum number) is a non-negative integer and **m_l** (the magnetic quantum number) runs from −l to +l in integer steps, giving 2l+1 possible values. Notice that even when m_l = l (the "maximum alignment" case), L_z = ℏl is always less than |L| = ℏ√(l(l+1)): the angular momentum vector can never be fully aligned with any axis, a purely quantum effect.

The eigenfunctions of L̂² and L̂_z are the **spherical harmonics** Y_l^{m_l}(θ,φ). These arise naturally when you solve the angular part of the Schrödinger equation in spherical coordinates using your differential equations prerequisite — specifically, separation of variables in Laplace's equation on the sphere. The azimuthal dependence is always e^{im_lφ}, which enforces single-valuedness when you go around the full circle: φ → φ + 2π must reproduce the same wavefunction, which forces m_l to be an integer. The polar-angle dependence involves **associated Legendre polynomials**, whose normalizability forces l to be a non-negative integer and |m_l| ≤ l.

This structure of quantum numbers (l, m_l) is the foundation for understanding the hydrogen atom and multi-electron atoms. The orbital quantum number l corresponds to the shape labels you may have encountered (s for l=0, p for l=1, d for l=2, etc.), and m_l describes the orientation of the orbital in space. When a magnetic field is applied, it breaks the 2l+1 degeneracy among the m_l states — different orientations now have different energies — which is the origin of the Zeeman effect. All of this flows from the algebra of the commutators you already know.

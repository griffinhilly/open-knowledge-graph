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

## Questions

```yaml
- question: "A quantum particle is in the state l = 2, m_l = 2 — the maximum m_l for this l value. A student concludes the angular momentum vector points exactly along the z-axis since m_l is at its maximum. What is wrong?"
  type: multiple-choice
  options:
    - "Nothing is wrong — when m_l = l, the angular momentum is fully aligned with the z-axis"
    - "The student forgot that L_z = ℏm_l is negative for positive m_l values"
    - "Even at maximum m_l, L_z = ℏl is always strictly less than |L| = ℏ√(l(l+1)), so the vector cannot be fully z-aligned"
    - "The angular momentum vector doesn't exist as a geometric object in quantum mechanics; only eigenvalues exist"
  answer: 2
  explanation: "For l = 2, m_l = 2: L_z = ℏ·2 = 2ℏ, but |L| = ℏ√(2·3) = ℏ√6 ≈ 2.45ℏ. Since L_z < |L|, the vector cannot be fully along the z-axis — there must be components in x and y directions, which are genuinely indeterminate. This is a purely quantum effect with no classical counterpart. Classically, you could align a spinning object precisely with any axis; quantum mechanically, the non-commutativity of components prevents this."

- question: "Why can only ONE component of the angular momentum vector be known precisely at a time in quantum mechanics?"
  type: multiple-choice
  options:
    - "Only L_z has a well-defined mathematical operator; L_x and L_y are undefined"
    - "The Heisenberg uncertainty principle prohibits simultaneously knowing both position and momentum"
    - "The angular momentum components do not commute: [L̂_x, L̂_y] = iℏL̂_z, so measuring one component disturbs the others"
    - "Electron spin interferes with orbital angular momentum measurement for all but the z-component"
  answer: 2
  explanation: "The non-commutativity of L̂_x, L̂_y, L̂_z is the direct cause: [L̂_x, L̂_y] = iℏL̂_z (and cyclically). Two operators that don't commute cannot share a complete set of simultaneous eigenstates — so you cannot have a state where both L_x and L_y have definite values simultaneously. By contrast, L̂² commutes with each component ([L̂², L̂_z] = 0), so you CAN simultaneously know the total magnitude squared and one component."

- question: "When l = 0, all three components L_x, L_y, and L_z are simultaneously zero and thus simultaneously well-defined, which is the only case where all components are simultaneously measurable."
  type: true-false
  answer: true
  explanation: "When l = 0, the only allowed value is m_l = 0, giving L_z = 0 and |L|² = ℏ²·0·1 = 0, so all components are zero. A vector that is identically zero has no directional ambiguity — L_x = L_y = L_z = 0 is simultaneously definite. This is consistent with the commutation relations: if [L̂_x, L̂_y] = iℏL̂_z and L_z = 0, the uncertainty relation allows both L_x and L_y to be zero simultaneously. The l = 0 (s-orbital) state is spherically symmetric for exactly this reason."

- question: "The orbital quantum number l can take any non-negative real value, including fractions, as long as |m_l| ≤ l."
  type: true-false
  answer: false
  explanation: "Both l and m_l must be non-negative integers (l = 0, 1, 2, ...) and integers (m_l = -l, ..., 0, ..., +l) respectively. The quantization to integers arises from the requirement that the wavefunction be single-valued: the azimuthal dependence e^{im_lφ} must return to the same value after a full rotation φ → φ + 2π, which forces m_l to be an integer. The normalizability of the polar part then forces l to be a non-negative integer with |m_l| ≤ l."

- question: "Explain the key difference between knowing L_z and knowing the full angular momentum vector L⃗ for a quantum particle, and why this difference has no classical counterpart."
  type: short-answer
  answer: "Knowing L_z gives you the projection of angular momentum along the z-axis (ℏm_l) and the total magnitude (ℏ√(l(l+1))), but the x and y components are genuinely indeterminate — not merely unknown, but without definite values. The angular momentum vector cannot be fully specified in any direction simultaneously because the components don't commute. Classically, L⃗ has definite components in all three directions at once; quantum mechanically, this is forbidden by the algebra of the operators."
  explanation: "This is a genuine departure from classical intuition, not just a measurement limitation. It's not that L_x and L_y are hidden from us — it's that the particle doesn't have simultaneous definite values for them. The angular momentum vector 'points' in an indeterminate direction within a cone around the z-axis, which is why the vector model of atomic orbitals shows L⃗ precessing around the z-axis rather than sitting still."
```

## Explainer

Classically, angular momentum is the vector L⃗ = r⃗ × p⃗: it has three components L_x, L_y, L_z, all of which you can know simultaneously. In quantum mechanics you can write the same formula using the corresponding operators, but the commutation relations your prerequisites introduced change everything. The key result is [L̂_x, L̂_y] = iℏL̂_z, and cyclically for the other pairs. Because no two components commute, only *one* component can have a definite value at a time. The conventional choice is L̂_z, measured in units of ℏ.

The magnitude-squared operator L̂² = L̂_x² + L̂_y² + L̂_z² does commute with each individual component: [L̂², L̂_z] = 0. This is what allows you to simultaneously know the total magnitude and one component. The eigenvalues work out to |L|² = ℏ²l(l+1) and L_z = ℏm_l, where **l** (the orbital quantum number) is a non-negative integer and **m_l** (the magnetic quantum number) runs from −l to +l in integer steps, giving 2l+1 possible values. Notice that even when m_l = l (the "maximum alignment" case), L_z = ℏl is always less than |L| = ℏ√(l(l+1)): the angular momentum vector can never be fully aligned with any axis, a purely quantum effect.

The eigenfunctions of L̂² and L̂_z are the **spherical harmonics** Y_l^{m_l}(θ,φ). These arise naturally when you solve the angular part of the Schrödinger equation in spherical coordinates using your differential equations prerequisite — specifically, separation of variables in Laplace's equation on the sphere. The azimuthal dependence is always e^{im_lφ}, which enforces single-valuedness when you go around the full circle: φ → φ + 2π must reproduce the same wavefunction, which forces m_l to be an integer. The polar-angle dependence involves **associated Legendre polynomials**, whose normalizability forces l to be a non-negative integer and |m_l| ≤ l.

This structure of quantum numbers (l, m_l) is the foundation for understanding the hydrogen atom and multi-electron atoms. The orbital quantum number l corresponds to the shape labels you may have encountered (s for l=0, p for l=1, d for l=2, etc.), and m_l describes the orientation of the orbital in space. When a magnetic field is applied, it breaks the 2l+1 degeneracy among the m_l states — different orientations now have different energies — which is the origin of the Zeeman effect. All of this flows from the algebra of the commutators you already know.

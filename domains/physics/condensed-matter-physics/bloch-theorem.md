---
id: bloch-theorem
title: Bloch's Theorem
domain: physics
course: condensed-matter-physics
prerequisites:
- id: reciprocal-lattice-brillouin-zones
  type: hard
- id: schrodinger-equation-intro
  type: hard
- id: quantum-superposition
  type: soft
tags:
- bloch-theorem
- bloch-wave
- crystal-momentum
- periodic-potential
stage: expert
status: validated
---

# Bloch's Theorem

## Core Idea
Bloch's theorem states that the eigenstates of an electron in a periodic potential V(r) = V(r + R) for all lattice vectors R take the form psi_{nk}(r) = e^{ik·r} u_{nk}(r), where u_{nk}(r) has the periodicity of the lattice. The quantum number k (crystal momentum) lives in the first Brillouin zone, and n is the band index. This theorem is the foundation of electronic band theory: it reduces the problem of an electron in an infinite crystal to solving for u_{nk} within a single unit cell, and it explains why electronic states organize into continuous energy bands separated by gaps.

## Questions

```yaml
- question: "A Bloch state psi_k(r) = e^{ik·r} u_k(r) is NOT a plane wave, even though it contains the factor e^{ik·r}. What makes it different?"
  type: multiple-choice
  options:
    - "The factor e^{ik·r} oscillates but u_k(r) is constant, so it is actually a plane wave"
    - "The function u_k(r) is periodic with the lattice periodicity, so the Bloch state is a plane wave modulated by a periodic function — it has the lattice symmetry built into it"
    - "Bloch states have discrete k values while plane waves have continuous k"
    - "Bloch states only exist in one dimension; plane waves exist in three dimensions"
  answer: 1
  explanation: "A pure plane wave e^{ik·r} has uniform amplitude everywhere. A Bloch state multiplies this by u_k(r), which oscillates with the periodicity of the crystal lattice — it is large near atomic cores and small between them (or vice versa). The result is a wave that propagates through the crystal but whose amplitude is modulated to reflect the atomic arrangement. This modulation is what produces energy bands and gaps: the electron 'knows' about the crystal structure through u_k(r)."

- question: "Crystal momentum ħk for a Bloch electron is not true momentum. What does it actually represent?"
  type: multiple-choice
  options:
    - "The kinetic energy of the electron divided by its velocity"
    - "The quantum number labeling translational symmetry of the crystal — it is conserved modulo reciprocal lattice vectors G, and determines how the electron responds to external fields via ħ dk/dt = F_ext"
    - "The average momentum of the electron, identical to ħk for a free particle"
    - "A classical quantity that has no quantum mechanical significance"
  answer: 1
  explanation: "True momentum ħk would require a state that is an eigenstate of the momentum operator, which Bloch states are not (the periodic part u_k breaks pure translational symmetry). Crystal momentum is the quantum number associated with discrete translational symmetry — it is defined modulo G and is conserved in that sense. Its physical importance is in semiclassical dynamics: an external force changes crystal momentum as ħ dk/dt = F_ext, and the electron's velocity is v = (1/ħ) ∂E/∂k. These equations govern electrical transport."

- question: "Bloch's theorem implies that an electron in a perfect crystal moves without scattering — the periodic potential alone does not cause resistance."
  type: true-false
  answer: true
  explanation: "This is a profound consequence. A Bloch state is a stationary state of the periodic Hamiltonian, meaning the electron propagates indefinitely through the perfect lattice without scattering. Electrical resistance in real metals comes entirely from deviations from perfect periodicity: thermal vibrations (phonons), impurities, defects, and grain boundaries. A perfect crystal at zero temperature would have zero resistance even without superconductivity — it simply would have no mechanism to scatter Bloch electrons."

- question: "Explain why Bloch's theorem reduces an infinite-crystal problem to a unit-cell problem."
  type: short-answer
  answer: "The Bloch form psi_k(r) = e^{ik·r} u_k(r) means that once you know u_k(r) within one unit cell, you know the wavefunction everywhere — the factor e^{ik·r} provides the phase relationship between cells. Substituting the Bloch form into the Schrodinger equation gives an equation for u_k(r) alone, with periodic boundary conditions on the unit cell. Instead of solving for psi in all of infinite space, you solve for u_k in a finite volume (one unit cell) for each k in the Brillouin zone. This is computationally tractable and is the basis of all band structure calculations."
  explanation: "This dimensional reduction is what makes solid-state physics possible. An infinite crystal has ~10^23 atoms, but Bloch's theorem says you only need to understand one unit cell (plus how k labels the states). The k-dependence of the eigenvalues E_n(k) gives the band structure."
```

## Explainer

Bloch's theorem is the single most important result in the quantum theory of solids. It answers the question: what do electron wavefunctions look like in a crystal, where the potential repeats periodically? The answer is elegant — they are **Bloch waves** of the form psi_{nk}(r) = e^{ik·r} u_{nk}(r), where the exponential is a plane-wave envelope and u_{nk}(r) is a function with the full periodicity of the lattice. The theorem follows directly from the commutation of the Hamiltonian with lattice translation operators: since [H, T_R] = 0 for any lattice vector R, energy eigenstates can be chosen as simultaneous eigenstates of all T_R, and the eigenvalues of T_R must be phases e^{ik·R}.

The quantum number **k** is called the crystal momentum (up to a factor of hbar) and lives in the first Brillouin zone. It labels how the wavefunction's phase evolves from one unit cell to the next. For each k, the Schrodinger equation becomes an eigenvalue problem for u_{nk} within a single unit cell with periodic boundary conditions, yielding a discrete set of eigenvalues E_n(k) indexed by the band index n. As k varies continuously across the Brillouin zone, each E_n(k) traces out an **energy band**. The collection of all bands E_n(k) is the band structure of the crystal — the central object of solid-state physics.

Two features of Bloch's theorem have far-reaching consequences. First, k is defined only modulo reciprocal lattice vectors G, meaning psi_{n,k+G} and psi_{nk} describe the same physics. This is why the first Brillouin zone suffices. Second, a Bloch electron in a perfect periodic potential experiences no scattering — the wavefunction is a stationary state that propagates indefinitely. Electrical resistance comes entirely from departures from perfect periodicity: phonons, impurities, surfaces, and defects. This insight, which seems counterintuitive (how can an electron move freely through a dense array of atoms?), is the starting point for understanding metallic conduction.

The practical power of Bloch's theorem is that it reduces a many-body problem in infinite space to a tractable eigenvalue problem in a single unit cell, parameterized by k. Modern band structure calculations — whether using nearly free electron models, tight-binding, or density functional theory — all begin with this reduction. The resulting band structure E_n(k) determines whether a material is a metal, semiconductor, or insulator, governs optical absorption, dictates transport properties, and is the foundation on which all of condensed matter physics is built.

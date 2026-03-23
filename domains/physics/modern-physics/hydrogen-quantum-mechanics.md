---
id: hydrogen-quantum-mechanics
title: Hydrogen Atom in Quantum Mechanics
domain: physics
course: modern-physics
prerequisites:
- id: schrodinger-eigenvalue-problem
  type: hard
- id: bohr-model
  type: soft
builds-toward:
- spectral-lines-transitions-wavelength
tags:
- quantum
- atoms
- hydrogen
stage: advanced
status: validated
---

# Hydrogen Atom in Quantum Mechanics

## Core Idea
The quantum mechanical hydrogen atom reproduces Bohr's energy levels En = −13.6 eV/n² without assuming circular orbits. Solutions yield three quantum numbers: n (principal, determines energy), ℓ (orbital angular momentum), and mℓ (z-component of angular momentum). Wavefunctions describe probability clouds (orbitals), not trajectories. This approach extends naturally to multi-electron atoms and molecules.

## Questions

```yaml
- question: "Hydrogen's 2s state (n=2, ℓ=0) and 2p states (n=2, ℓ=1) have the same energy. What accounts for this degeneracy?"
  type: multiple-choice
  options:
    - "Both states have ℓ = 0, so their angular momenta are identical"
    - "Both states have the same magnetic quantum number mℓ = 0"
    - "Energy depends only on n in the Coulomb potential, so all n=2 states are degenerate regardless of ℓ"
    - "The spherical harmonics Y_ℓ^m are energy eigenstates with the same eigenvalue for all ℓ"
  answer: 2
  explanation: "In the hydrogen atom, energy depends only on the principal quantum number n: E_n = −13.6 eV/n². States with different ℓ but the same n share the same energy — this is the n²-fold degeneracy. The 2s (ℓ=0) and all three 2p (ℓ=1, mℓ = −1, 0, +1) states all have energy −3.4 eV. This degeneracy is a special property of the 1/r Coulomb potential, reflecting a hidden SO(4) symmetry. It is lifted by perturbations such as spin-orbit coupling."

- question: "How many distinct quantum states (ignoring spin) share the energy E_3 = −13.6/9 eV?"
  type: multiple-choice
  options:
    - "3, because mℓ can take values −1, 0, +1"
    - "5, because the largest ℓ is 2 and mℓ has 5 values for ℓ=2"
    - "9, because for n=3, summing 2ℓ+1 over ℓ = 0, 1, 2 gives 1+3+5 = 9"
    - "6, because there are 3 possible ℓ values each with 2 mℓ values"
  answer: 2
  explanation: "For n=3, ℓ can be 0, 1, or 2. For ℓ=0: mℓ=0 only → 1 state. For ℓ=1: mℓ = −1, 0, +1 → 3 states. For ℓ=2: mℓ = −2, −1, 0, +1, +2 → 5 states. Total: 1+3+5 = 9 = n² = 9. The general formula is n² distinct states per energy level (ignoring spin). This is the n²-fold degeneracy specific to the Coulomb potential."

- question: "In the quantum mechanical hydrogen atom, the electron follows a definite circular orbit whose radius is given by a₀n², just as the Bohr model describes."
  type: true-false
  answer: false
  explanation: "This is the Bohr model's picture, which quantum mechanics replaces. In quantum mechanics, the electron has no definite position or trajectory; it exists in a state described by a wavefunction ψ(r,θ,φ), and |ψ|² gives a probability density for finding the electron at each point. Orbitals are probability clouds, not paths. The most probable radius for the 1s state equals the Bohr radius a₀ — a coincidence of the most probable value — but the electron can be found at any radius."

- question: "The three quantum numbers n, ℓ, and mℓ emerge from three separate equations when the hydrogen Schrödinger equation is solved by separating variables in spherical coordinates."
  type: true-false
  answer: true
  explanation: "Separation of variables splits the hydrogen Schrödinger equation into three independent equations: a radial equation (yielding n and constraining ℓ ≤ n−1), a polar angle equation (yielding ℓ), and an azimuthal equation (yielding mℓ, constrained to |mℓ| ≤ ℓ). Each quantum number is defined by the boundary conditions on its equation. They are not independent in the sense that n constrains ℓ, which constrains mℓ — but each number arises from its own separated equation."

- question: "The Bohr model correctly predicts hydrogen's energy levels but is said to give 'the right answer for the wrong reason.' What did Bohr assume that quantum mechanics corrects, and what does quantum mechanics actually say about where the electron is?"
  type: short-answer
  answer: "Bohr assumed electrons travel on well-defined circular orbits at specific radii (a₀n²), with angular momentum quantized as nℏ. Quantum mechanics shows there are no definite orbits: the electron has a wavefunction ψ(r,θ,φ) whose square gives a probability density. The electron has no trajectory — its position is fundamentally indeterminate between measurements. The most probable radius for the ground state coincidentally equals the Bohr radius a₀, but the electron can be found at any radius. Quantum mechanics also introduces ℓ and mℓ absent from the Bohr model, and gives the 1s state zero angular momentum (ℓ=0), contradicting Bohr's requirement of one unit."
  explanation: "The Bohr model's success was partly accidental — the Coulomb potential and orbit quantization happen to give correct energies. But the model fails for multi-electron atoms, cannot predict spectral intensities or selection rules, and gives incorrect angular momenta. Quantum mechanics provides the correct framework by replacing deterministic trajectories with probabilistic wavefunctions and grounding the energy formula in a rigorous eigenvalue equation."
```

## Explainer

Your prerequisite — the Schrödinger eigenvalue problem — taught you to find quantum states as solutions to Ĥψ = Eψ. For hydrogen, the Hamiltonian is Ĥ = −(ℏ²/2m)∇² − e²/(4πε₀r), combining kinetic energy with the Coulomb attraction between electron and proton. Because the potential depends only on r (it is spherically symmetric), the solutions separate: ψ(r,θ,φ) = R(r)·Y_ℓ^m(θ,φ), where R(r) satisfies a radial equation and Y_ℓ^m are the spherical harmonics governing the angular dependence. This separation is what makes hydrogen exactly solvable, and the three quantum numbers emerge naturally — one from each separated equation.

The **principal quantum number** n = 1, 2, 3, ... determines the energy: E_n = −13.6 eV/n². This is Bohr's formula, recovered without assuming circular orbits. The **orbital angular momentum quantum number** ℓ = 0, 1, ..., n−1 quantifies the magnitude of angular momentum: |L⃗| = ℏ√(ℓ(ℓ+1)). The **magnetic quantum number** m_ℓ = −ℓ, ..., 0, ..., +ℓ quantifies the z-component: L_z = m_ℓℏ. Notice how n constrains ℓ, which constrains m_ℓ — the three quantum numbers are linked because they come from three nested separation equations. For a given n, there are n² distinct states (one for ℓ = 0, three for ℓ = 1, five for ℓ = 2, and so on), all sharing the same energy. This **degeneracy** is a special property of the 1/r Coulomb potential.

The Bohr model gave correct energies by assuming electrons travel on circular orbits of radius a₀n². The quantum mechanical picture replaces orbits with **probability clouds** (orbitals). The quantity |ψ(r,θ,φ)|² gives the probability density for finding the electron at position (r,θ,φ). For the 1s ground state (n=1, ℓ=0, m_ℓ=0), this is spherically symmetric and peaks at the nucleus, decaying exponentially outward. The most probable radius — the peak of the radial probability distribution r²|R(r)|² — is exactly the Bohr radius a₀ ≈ 0.053 nm. Bohr got the right radius but for the wrong reason; quantum mechanics justifies it rigorously.

The n²-fold degeneracy of each energy level is deeper than spherical symmetry alone would predict. A merely spherically symmetric problem would have only a (2ℓ+1)-fold degeneracy in m_ℓ for each ℓ; the additional degeneracy across different ℓ values sharing the same n reflects a hidden SO(4) symmetry of the Coulomb potential — an extra conserved quantity called the Laplace-Runge-Lenz vector. This degeneracy is lifted by perturbations: spin-orbit coupling, relativistic corrections, and external fields all split the n-levels into distinct sub-levels, producing the **fine structure** and **hyperfine structure** observed in high-resolution hydrogen spectra and predicted by the deeper theory.

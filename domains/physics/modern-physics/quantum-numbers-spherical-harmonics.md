---
id: quantum-numbers-spherical-harmonics
title: Quantum Numbers and Spherical Harmonics
domain: physics
course: modern-physics
prerequisites:
- id: atomic-orbitals-shapes-nodes
  type: hard
- id: quantum-numbers
  type: soft
builds-toward:
- periodic-table-filling-orbitals
tags:
- atomic-physics
- quantum-numbers
stage: advanced
status: validated
---

# Quantum Numbers and Spherical Harmonics

## Core Idea
Three quantum numbers label hydrogen atom states: n (principal, energy), ℓ (orbital angular momentum, shape), and m_ℓ (magnetic, orientation). Additionally, m_s = ±1/2 describes electron spin. Angular parts of wavefunctions are spherical harmonics Y_ℓ^m_ℓ(θ,φ), which determine orbital shapes. The quantum number n ranges from 1 to ∞, ℓ from 0 to n−1, and m_ℓ from −ℓ to +ℓ, giving multiple degenerate states at each energy level.

## Questions

```yaml
- question: "Why are there exactly five d orbitals at any given energy level?"
  type: multiple-choice
  options:
    - "Because d is the fourth type of orbital and 4 + 1 = 5 by a conventional counting rule"
    - "Because d orbitals have a pentagonal symmetry that requires five distinct spatial orientations"
    - "Because d orbitals have ℓ = 2, giving magnetic quantum number values m_ℓ = −2, −1, 0, +1, +2 — five distinct quantum states"
    - "Because five d orbitals are needed to accommodate the 10 electrons that fill the d subshell"
  answer: 2
  explanation: "The number of orbitals for a given ℓ is always 2ℓ + 1, one for each allowed value of m_ℓ. For d orbitals (ℓ = 2), m_ℓ ranges from −2 to +2: five values, five orbitals. Option D reverses the causation — the 10-electron capacity follows from having 5 orbitals × 2 spins, not the other way around."

- question: "Which physical constraint gives rise to the magnetic quantum number m_ℓ?"
  type: multiple-choice
  options:
    - "The requirement that the radial wavefunction approach zero at large distances from the nucleus"
    - "The requirement that the wavefunction be single-valued — returning to the same value after a full 2π rotation in the azimuthal (φ) direction"
    - "The requirement that the total energy of the electron be negative (bound state)"
    - "The requirement that the angular momentum magnitude be an integer multiple of ℏ"
  answer: 1
  explanation: "The φ-dependence of the wavefunction has the form e^{im_ℓφ}. For this to be single-valued — ψ(φ) = ψ(φ + 2π) — we need e^{im_ℓ·2π} = 1, which requires m_ℓ to be an integer. Option D describes a consequence of quantization rather than the mathematical constraint that generates it. Option A constrains the radial quantum number n, not m_ℓ."

- question: "All hydrogen atom states with the same principal quantum number n have the same energy, regardless of their ℓ and m_ℓ values."
  type: true-false
  answer: true
  explanation: "In the ideal hydrogen atom, energy depends only on n: Eₙ = −13.6 eV/n². States with the same n but different ℓ and m_ℓ are degenerate. This n-degeneracy is a special feature of the 1/r Coulomb potential and is broken in multi-electron atoms, where electron-electron repulsion makes energy depend on ℓ as well (which is why the 2s and 2p orbitals have different energies in helium and heavier elements)."

- question: "The electron's spin quantum number m_s = ±1/2 arises naturally from solving the Schrödinger equation in spherical coordinates, just as n, ℓ, and m_ℓ do."
  type: true-false
  answer: false
  explanation: "Spin does not emerge from the non-relativistic Schrödinger equation. It must be added as an independent degree of freedom — a two-component spinor describing intrinsic angular momentum with no classical analog. It arises naturally from the Dirac equation (relativistic quantum mechanics) but must be grafted onto the Schrödinger framework by hand. This is why it is described separately from the three spatial quantum numbers."

- question: "How do the four quantum numbers (n, ℓ, m_ℓ, m_s) together with the Pauli exclusion principle produce the shell structure of the periodic table?"
  type: short-answer
  answer: "For each n, ℓ can range from 0 to n−1 (n values). For each ℓ, m_ℓ ranges from −ℓ to +ℓ (2ℓ+1 values). Summing over all ℓ gives n² spatial states per shell. With two spin states (m_s = ±1/2), each shell holds 2n² electrons. Pauli forbids any two electrons from sharing all four quantum numbers, so electrons fill these distinct slots sequentially. This yields 2 for n=1, 8 for n=2, 18 for n=3 — directly matching the periods of the periodic table."
  explanation: "The counting is not arbitrary: it follows necessarily from the mathematical constraints that generate each quantum number. Understanding the derivation makes the periodic table's structure predictable from first principles rather than a memorized pattern."
```

## Explainer

From your study of atomic orbitals — the s, p, d, f shapes and their nodes — you already know the visual vocabulary of quantum states. The **quantum numbers** are the systematic labeling scheme that connects those pictures to the mathematics of solving the hydrogen atom's Schrödinger equation in spherical coordinates. Solving the equation involves separation of variables: the wavefunction ψ(r, θ, φ) = R(r)·Y(θ, φ), where R(r) is a radial function and Y(θ, φ) is an angular function. Each separation introduces a quantum number that must take specific discrete values for the solution to be physically acceptable (normalizable and single-valued).

The **principal quantum number** n = 1, 2, 3, … comes from the radial equation and determines the energy: Eₙ = −13.6 eV/n². All states with the same n are **degenerate** in hydrogen — they share the same energy. The **orbital angular momentum quantum number** ℓ = 0, 1, 2, …, n−1 comes from requiring the angular solution to be well-behaved (square-integrable on the sphere). It determines the magnitude of the electron's orbital angular momentum: |L⃗| = ℏ√(ℓ(ℓ+1)). This is the quantum number you are really labeling when you say s (ℓ=0), p (ℓ=1), d (ℓ=2), f (ℓ=3). Finally, the **magnetic quantum number** m_ℓ = −ℓ, −ℓ+1, …, 0, …, ℓ comes from requiring the φ-dependence to be single-valued (the wavefunction must return to the same value after rotating 2π). It determines the component of angular momentum along any chosen axis: L_z = m_ℓ ℏ. A state with ℓ = 2 can have m_ℓ = −2, −1, 0, 1, or 2 — five choices, hence five d orbitals.

The angular functions Y_ℓ^{m_ℓ}(θ,φ) are the **spherical harmonics** — a complete, orthonormal basis for functions on a sphere. You can think of them as the "Fourier modes" of the sphere: just as sinusoids are the natural modes of a periodic line, spherical harmonics are the natural modes of a spherical surface. Their shapes directly give the orbital geometries you visualized earlier. Y₀⁰ is a constant (s orbital: spherically symmetric). Y₁⁰ ∝ cos θ (p_z: a lobe along the z-axis). Y₂⁰ ∝ 3cos²θ − 1 (d_z²: the double-lobe plus torus shape). The number of angular nodes equals ℓ, which is why higher-ℓ orbitals have more complex angular shapes. The real combinations of Y_ℓ^{m_ℓ} and Y_ℓ^{−m_ℓ} give the familiar d_{xy}, d_{xz} etc. orientations.

The electron's **spin quantum number** m_s = ±1/2 has no classical analog and does not come from the spatial Schrödinger equation — it arises from the intrinsic angular momentum (spin) of the electron, described by a separate two-component spinor. Combining all four quantum numbers (n, ℓ, m_ℓ, m_s), the number of distinct states at principal quantum number n is 2n² — two spin states for each of the n² spatial states. This counting, combined with the **Pauli exclusion principle** (no two electrons can share all four quantum numbers), directly produces the periodic table's shell structure: 2 electrons in n=1, 8 in n=2, 18 in n=3, each shell filling in the order you will study when you learn about orbital filling and the Aufbau principle.

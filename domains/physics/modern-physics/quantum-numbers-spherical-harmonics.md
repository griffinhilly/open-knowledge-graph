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
status: draft
---

# Quantum Numbers and Spherical Harmonics

## Core Idea
Three quantum numbers label hydrogen atom states: n (principal, energy), ℓ (orbital angular momentum, shape), and m_ℓ (magnetic, orientation). Additionally, m_s = ±1/2 describes electron spin. Angular parts of wavefunctions are spherical harmonics Y_ℓ^m_ℓ(θ,φ), which determine orbital shapes. The quantum number n ranges from 1 to ∞, ℓ from 0 to n−1, and m_ℓ from −ℓ to +ℓ, giving multiple degenerate states at each energy level.

## Explainer

From your study of atomic orbitals — the s, p, d, f shapes and their nodes — you already know the visual vocabulary of quantum states. The **quantum numbers** are the systematic labeling scheme that connects those pictures to the mathematics of solving the hydrogen atom's Schrödinger equation in spherical coordinates. Solving the equation involves separation of variables: the wavefunction ψ(r, θ, φ) = R(r)·Y(θ, φ), where R(r) is a radial function and Y(θ, φ) is an angular function. Each separation introduces a quantum number that must take specific discrete values for the solution to be physically acceptable (normalizable and single-valued).

The **principal quantum number** n = 1, 2, 3, … comes from the radial equation and determines the energy: Eₙ = −13.6 eV/n². All states with the same n are **degenerate** in hydrogen — they share the same energy. The **orbital angular momentum quantum number** ℓ = 0, 1, 2, …, n−1 comes from requiring the angular solution to be well-behaved (square-integrable on the sphere). It determines the magnitude of the electron's orbital angular momentum: |L⃗| = ℏ√(ℓ(ℓ+1)). This is the quantum number you are really labeling when you say s (ℓ=0), p (ℓ=1), d (ℓ=2), f (ℓ=3). Finally, the **magnetic quantum number** m_ℓ = −ℓ, −ℓ+1, …, 0, …, ℓ comes from requiring the φ-dependence to be single-valued (the wavefunction must return to the same value after rotating 2π). It determines the component of angular momentum along any chosen axis: L_z = m_ℓ ℏ. A state with ℓ = 2 can have m_ℓ = −2, −1, 0, 1, or 2 — five choices, hence five d orbitals.

The angular functions Y_ℓ^{m_ℓ}(θ,φ) are the **spherical harmonics** — a complete, orthonormal basis for functions on a sphere. You can think of them as the "Fourier modes" of the sphere: just as sinusoids are the natural modes of a periodic line, spherical harmonics are the natural modes of a spherical surface. Their shapes directly give the orbital geometries you visualized earlier. Y₀⁰ is a constant (s orbital: spherically symmetric). Y₁⁰ ∝ cos θ (p_z: a lobe along the z-axis). Y₂⁰ ∝ 3cos²θ − 1 (d_z²: the double-lobe plus torus shape). The number of angular nodes equals ℓ, which is why higher-ℓ orbitals have more complex angular shapes. The real combinations of Y_ℓ^{m_ℓ} and Y_ℓ^{−m_ℓ} give the familiar d_{xy}, d_{xz} etc. orientations.

The electron's **spin quantum number** m_s = ±1/2 has no classical analog and does not come from the spatial Schrödinger equation — it arises from the intrinsic angular momentum (spin) of the electron, described by a separate two-component spinor. Combining all four quantum numbers (n, ℓ, m_ℓ, m_s), the number of distinct states at principal quantum number n is 2n² — two spin states for each of the n² spatial states. This counting, combined with the **Pauli exclusion principle** (no two electrons can share all four quantum numbers), directly produces the periodic table's shell structure: 2 electrons in n=1, 8 in n=2, 18 in n=3, each shell filling in the order you will study when you learn about orbital filling and the Aufbau principle.

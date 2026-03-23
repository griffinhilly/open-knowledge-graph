---
id: principal-angular-magnetic-quantum-numbers
title: Principal, Angular, and Magnetic Quantum Numbers in Atoms
domain: physics
course: modern-physics
prerequisites:
- id: quantum-numbers
  type: hard
- id: hydrogen-atom-schrodinger-solution
  type: hard
builds-toward:
- atomic-term-symbols-ls-coupling
tags:
- quantum-numbers
- atomic-physics
- quantum-mechanics
stage: advanced
status: validated
---

# Principal, Angular, and Magnetic Quantum Numbers in Atoms

## Core Idea
The principal quantum number n determines the energy level and orbital size. The orbital angular momentum quantum number ℓ (ranging from 0 to n−1) sets |L| = ℏ√(ℓ(ℓ+1)) and determines orbital shape (s, p, d, f, ...). The magnetic quantum number m_ℓ (ranging from −ℓ to +ℓ) specifies the z-component L_z = m_ℏ and determines orbital orientation. Each (n,ℓ,m_ℓ) triplet labels a unique orbital.

## How It's Best Learned
List all valid combinations of (n,ℓ,m_ℓ) for n=1,2,3. Relate quantum numbers to measurable quantities: energy, angular momentum magnitude, and z-component. Use selection rules ℓ → ℓ±1 and Δm_ℓ = 0,±1 to predict allowed transitions.

## Common Misconceptions
m_ℓ does not represent the magnitude of angular momentum in any direction (it is specifically the z-component). The z-axis is not special in free atoms; it only gains meaning in an applied magnetic field.

## Questions

```yaml
- question: "Two electrons both have n=2 and ℓ=1, but one has m_ℓ = +1 and the other has m_ℓ = 0. In a hydrogen atom with no applied magnetic field, which electron has higher energy?"
  type: multiple-choice
  options:
    - "m_ℓ = +1 has higher energy because its z-component of angular momentum is larger"
    - "m_ℓ = 0 has higher energy because it corresponds to the 'central' orbital orientation"
    - "They have the same energy — without an applied field, all m_ℓ states with the same n and ℓ are degenerate"
    - "Energy depends on m_ℓ but the calculation requires knowing the spin quantum number too"
  answer: 2
  explanation: "In a free hydrogen atom with no external field, the energy depends only on n (E_n = −13.6 eV/n²). All states with the same n are degenerate — the 2p subshell's three m_ℓ = −1, 0, +1 states all have the same energy. The z-axis has no physical preferred status in the absence of a field; only when a magnetic field defines a preferred direction do the m_ℓ states acquire different energies via the Zeeman effect. The common misconception is treating m_ℓ as directly connected to energy."

- question: "What is the magnitude of the orbital angular momentum for an electron with ℓ = 2?"
  type: multiple-choice
  options:
    - "2ℏ"
    - "4ℏ"
    - "ℏ√6"
    - "ℏ√4 = 2ℏ (same as answer A)"
  answer: 2
  explanation: "|L| = ℏ√(ℓ(ℓ+1)) = ℏ√(2·3) = ℏ√6 ≈ 2.45ℏ. This is a key formula to internalize: the angular momentum magnitude is NOT ℓℏ. The extra term in √(ℓ(ℓ+1)) versus √(ℓ²) = ℓ comes from quantum mechanics — the uncertainty principle prevents all three angular momentum components from being sharp simultaneously, so the magnitude must exceed the maximum z-component (m_ℓ·ℏ = 2ℏ at most for ℓ=2). The formula |L| = ℏ√(ℓ(ℓ+1)) encodes this."

- question: "For an electron with ℓ = 1 and m_ℓ = 1, the total orbital angular momentum magnitude is ℏ, since L_z = m_ℓ·ℏ = ℏ implies the full angular momentum is ℏ."
  type: true-false
  answer: false
  explanation: "m_ℓ gives only the z-component: L_z = m_ℓ·ℏ = ℏ. The total magnitude is |L| = ℏ√(ℓ(ℓ+1)) = ℏ√(1·2) = ℏ√2 ≈ 1.41ℏ, which is larger than L_z. The total angular momentum always exceeds its z-component (unless ℓ = 0) because the uncertainty principle requires L_x and L_y to have nonzero expectation of their squares. Setting |L| = L_z = m_ℓ·ℏ confuses the component with the magnitude — the most common error with magnetic quantum numbers."

- question: "In a hydrogen atom with no applied magnetic field, an electron in the 2p subshell (n=2, ℓ=1) exists in one of three distinct energy levels corresponding to m_ℓ = −1, 0, +1."
  type: true-false
  answer: false
  explanation: "Without an applied field, the three m_ℓ states of the 2p subshell are energetically degenerate — they all have the same energy E_2 = −3.4 eV. The z-axis is only meaningful when a magnetic field defines a preferred spatial direction; in a free atom, all orientations are equivalent. It is the Zeeman effect — the splitting of degenerate m_ℓ levels in an applied field — that makes the magnetic quantum number experimentally accessible."

- question: "Why can we simultaneously know |L|² (the squared magnitude of orbital angular momentum) and L_z (one component), but not all three components L_x, L_y, L_z simultaneously? What physical principle prevents this?"
  type: short-answer
  answer: "The angular momentum components satisfy the commutation relations [L_x, L_y] = iℏL_z (and cyclic permutations). By the Heisenberg uncertainty principle, two observables can be simultaneously sharp only if they commute. L_x and L_y do not commute, so they cannot both have definite values at once. However, L² = L_x² + L_y² + L_z² commutes with each component individually, so L² and one component (conventionally L_z) can be simultaneously sharp. This is why quantum numbers ℓ (giving |L|²) and m_ℓ (giving L_z) can both be well-defined, while L_x and L_y remain inherently indefinite."
  explanation: "This is not a measurement limitation but a fundamental feature of the quantum state. An eigenstate of L² and L_z genuinely has indefinite L_x and L_y — not merely unknown. The consequence is that the angular momentum vector cannot 'point' in a definite direction; it precesses around the z-axis, with fixed |L| and L_z but uncertain transverse components."
```

## Explainer

When you solved the Schrödinger equation for hydrogen, three separation constants appeared naturally — one for each spatial coordinate in spherical coordinates. These constants are the quantum numbers n, ℓ, and m_ℓ. They are not arbitrary labels; they emerge from the mathematical requirement that the wavefunction be well-behaved (normalizable, single-valued, continuous). Understanding what each one physically means requires connecting the separation constants to observable quantities.

The **principal quantum number** n (n = 1, 2, 3, …) controls the energy: E_n = −13.6 eV / n². It also determines the average distance of the electron from the nucleus — higher n means larger, more diffuse orbitals. The name "principal" reflects its role as the primary determinant of orbital energy in hydrogen (though in multi-electron atoms, shielding breaks this simple dependence). Think of n as the "shell" — the main energy level.

The **orbital angular momentum quantum number** ℓ (0, 1, 2, … up to n−1) controls the shape of the orbital. It tells you the magnitude of the electron's orbital angular momentum: |L| = ℏ√(ℓ(ℓ+1)). For ℓ = 0 (s orbitals), the angular wavefunction is spherically symmetric — no preferred direction, no angular nodes. For ℓ = 1 (p orbitals), there is one angular node and the orbital is dumbbell-shaped. For ℓ = 2 (d orbitals), there are two angular nodes and more complex shapes. The letters s, p, d, f are historical spectroscopic names (sharp, principal, diffuse, fundamental) that map to ℓ = 0, 1, 2, 3. The constraint ℓ ≤ n−1 is not arbitrary: it follows from the requirement that the radial wavefunction be normalizable.

The **magnetic quantum number** m_ℓ (−ℓ, −ℓ+1, …, 0, …, ℓ−1, ℓ) controls the orientation of the orbital in space. Specifically, it gives the z-component of angular momentum: L_z = m_ℓ·ℏ. For a p orbital (ℓ = 1), there are three possible orientations (m_ℓ = −1, 0, +1), corresponding to the familiar p_x, p_y, p_z orbitals (or rather, their complex linear combinations). The reason the magnitude |L| is quantized separately from L_z is the uncertainty principle: L_x, L_y, and L_z satisfy commutation relations that forbid them from all being sharp simultaneously. You can know |L|² and one component (by convention L_z), but the other two components are inherently indefinite. A free atom in the absence of a magnetic field is degenerate over all m_ℓ values — all orientations are equally valid and physically equivalent. It is only when a field defines a preferred axis that the m_ℓ states acquire different energies (the Zeeman effect), making the quantum number measurable directly.

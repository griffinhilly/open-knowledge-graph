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
status: draft
---

# Principal, Angular, and Magnetic Quantum Numbers in Atoms

## Core Idea
The principal quantum number n determines the energy level and orbital size. The orbital angular momentum quantum number ℓ (ranging from 0 to n−1) sets |L| = ℏ√(ℓ(ℓ+1)) and determines orbital shape (s, p, d, f, ...). The magnetic quantum number m_ℓ (ranging from −ℓ to +ℓ) specifies the z-component L_z = m_ℏ and determines orbital orientation. Each (n,ℓ,m_ℓ) triplet labels a unique orbital.

## How It's Best Learned
List all valid combinations of (n,ℓ,m_ℓ) for n=1,2,3. Relate quantum numbers to measurable quantities: energy, angular momentum magnitude, and z-component. Use selection rules ℓ → ℓ±1 and Δm_ℓ = 0,±1 to predict allowed transitions.

## Common Misconceptions
m_ℓ does not represent the magnitude of angular momentum in any direction (it is specifically the z-component). The z-axis is not special in free atoms; it only gains meaning in an applied magnetic field.

## Explainer

When you solved the Schrödinger equation for hydrogen, three separation constants appeared naturally — one for each spatial coordinate in spherical coordinates. These constants are the quantum numbers n, ℓ, and m_ℓ. They are not arbitrary labels; they emerge from the mathematical requirement that the wavefunction be well-behaved (normalizable, single-valued, continuous). Understanding what each one physically means requires connecting the separation constants to observable quantities.

The **principal quantum number** n (n = 1, 2, 3, …) controls the energy: E_n = −13.6 eV / n². It also determines the average distance of the electron from the nucleus — higher n means larger, more diffuse orbitals. The name "principal" reflects its role as the primary determinant of orbital energy in hydrogen (though in multi-electron atoms, shielding breaks this simple dependence). Think of n as the "shell" — the main energy level.

The **orbital angular momentum quantum number** ℓ (0, 1, 2, … up to n−1) controls the shape of the orbital. It tells you the magnitude of the electron's orbital angular momentum: |L| = ℏ√(ℓ(ℓ+1)). For ℓ = 0 (s orbitals), the angular wavefunction is spherically symmetric — no preferred direction, no angular nodes. For ℓ = 1 (p orbitals), there is one angular node and the orbital is dumbbell-shaped. For ℓ = 2 (d orbitals), there are two angular nodes and more complex shapes. The letters s, p, d, f are historical spectroscopic names (sharp, principal, diffuse, fundamental) that map to ℓ = 0, 1, 2, 3. The constraint ℓ ≤ n−1 is not arbitrary: it follows from the requirement that the radial wavefunction be normalizable.

The **magnetic quantum number** m_ℓ (−ℓ, −ℓ+1, …, 0, …, ℓ−1, ℓ) controls the orientation of the orbital in space. Specifically, it gives the z-component of angular momentum: L_z = m_ℓ·ℏ. For a p orbital (ℓ = 1), there are three possible orientations (m_ℓ = −1, 0, +1), corresponding to the familiar p_x, p_y, p_z orbitals (or rather, their complex linear combinations). The reason the magnitude |L| is quantized separately from L_z is the uncertainty principle: L_x, L_y, and L_z satisfy commutation relations that forbid them from all being sharp simultaneously. You can know |L|² and one component (by convention L_z), but the other two components are inherently indefinite. A free atom in the absence of a magnetic field is degenerate over all m_ℓ values — all orientations are equally valid and physically equivalent. It is only when a field defines a preferred axis that the m_ℓ states acquire different energies (the Zeeman effect), making the quantum number measurable directly.

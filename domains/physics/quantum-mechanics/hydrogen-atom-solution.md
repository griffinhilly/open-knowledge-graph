---
id: hydrogen-atom-solution
title: Solution of the Hydrogen Atom
domain: physics
course: quantum-mechanics
prerequisites:
- id: schrodinger-equation-intro
  type: hard
- id: orbital-angular-momentum-quantum
  type: hard
builds-toward:
- hydrogen-energy-levels
- fine-structure-hydrogen
tags:
- hydrogen-atom
- solvable-systems
stage: advanced
status: draft
---

# Solution of the Hydrogen Atom

## Core Idea
The Coulomb potential V(r) = −e²/4πε₀r yields exact solutions via separation of variables: angular parts are spherical harmonics; radial equations give R_{nl}(r) depending on n (principal) and l (orbital).

## Explainer

You already know how to write down and solve the Schrödinger equation for simple systems like the infinite square well, and you know that orbital angular momentum in quantum mechanics is quantized with quantum numbers l and m_l. The hydrogen atom brings these threads together: it is the first physically realistic problem with a three-dimensional, spherically symmetric potential that yields an exact analytic solution.

The key move is **separation of variables**. Because the Coulomb potential V(r) = −e²/4πε₀r depends only on the radial distance r from the nucleus, the wavefunction factors as ψ(r, θ, φ) = R(r) · Y_l^m(θ, φ). The angular part Y_l^m are the **spherical harmonics** — you've seen these from your work on orbital angular momentum. They are the eigenfunctions of L² and L_z, carrying quantum numbers l (orbital quantum number, l = 0, 1, 2, …) and m_l (magnetic quantum number, −l ≤ m_l ≤ l). The spherical harmonics encode the shape of the orbital: s-orbitals are spherically symmetric (l=0), p-orbitals have one nodal plane (l=1), d-orbitals have more complex shapes (l=2), and so on.

The radial equation is trickier. Substituting the Coulomb potential and requiring normalizable solutions forces the energy to be quantized. The allowed energies are E_n = −13.6 eV / n², where n = 1, 2, 3, … is the **principal quantum number**. This matches what was known empirically from spectroscopy (the Rydberg formula), but quantum mechanics derives it from first principles. The corresponding radial wavefunctions R_{nl}(r) are products of an exponential decay and an associated Laguerre polynomial. They depend on both n and l, with the constraint that l = 0, 1, …, n−1. Larger n means the electron is more likely to be found farther from the nucleus, and the energy is closer to zero (less tightly bound).

The complete **hydrogen wavefunction** ψ_{nlm}(r, θ, φ) is labeled by three quantum numbers: n determines the energy, l determines the magnitude of angular momentum, and m_l determines the component of angular momentum along a chosen axis. The ground state (n=1, l=0, m_l=0) is spherically symmetric, purely exponential, and has the smallest possible spatial extent. Each energy level n has n² degenerate states (ignoring spin). This degeneracy is partly accidental — a consequence of the special 1/r form of the Coulomb potential — and it is partially lifted by relativistic corrections and spin effects, which give rise to the fine structure of hydrogen spectral lines.

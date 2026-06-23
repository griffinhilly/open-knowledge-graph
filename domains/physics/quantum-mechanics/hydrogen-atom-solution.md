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
- id: angular-momentum-quantization
  type: hard
builds-toward:
- hydrogen-energy-levels
- fine-structure-hydrogen
tags:
- hydrogen-atom
- solvable-systems
stage: advanced
status: validated
---

# Solution of the Hydrogen Atom

## Core Idea
The Coulomb potential V(r) = −e²/4πε₀r yields exact solutions via separation of variables: angular parts are spherical harmonics; radial equations give R_{nl}(r) depending on n (principal) and l (orbital).

## Questions

```yaml
- question: "A hydrogen electron is in a state with principal quantum number n = 3. Which of the following correctly lists all allowed values of the orbital quantum number l?"
  type: multiple-choice
  options:
    - "l = 0, 1, 2, 3 — l can take any non-negative integer up to n"
    - "l = 0, 1, 2 — l ranges from 0 to n − 1"
    - "l = 1, 2, 3 — l starts at 1 for excited states"
    - "l = 0 only — all n = 3 states are s-states"
  answer: 1
  explanation: "The constraint from solving the radial Schrödinger equation is l = 0, 1, 2, …, n − 1. For n = 3, this gives l = 0, 1, or 2 (the 3s, 3p, and 3d subshells). Option A is wrong by one — l cannot equal n. The constraint l ≤ n − 1 arises from requiring the radial wavefunction to be normalizable: trying to construct a solution with l ≥ n forces the power series in the associated Laguerre polynomial to diverge. The l values are not an independent postulate — they fall out of the mathematics of the radial equation."

- question: "How many distinct quantum states does the n = 2 energy level of hydrogen contain, ignoring electron spin?"
  type: multiple-choice
  options:
    - "1 — there is only one n = 2 state"
    - "2 — one for each allowed value of l"
    - "4 — one 2s state and three 2p states (m_l = −1, 0, +1)"
    - "8 — including all spin states"
  answer: 2
  explanation: "For n = 2, l can be 0 or 1. For l = 0: only m_l = 0 (one state, the 2s orbital). For l = 1: m_l = −1, 0, +1 (three states, the 2p orbitals). Total ignoring spin: 1 + 3 = 4 states. This equals n² = 2² = 4, confirming the general formula. The degeneracy (all four states having the same energy) is a special feature of the 1/r Coulomb potential. Option D of 8 would be correct if spin were included (2 spin states per orbital)."

- question: "The principal quantum number n in hydrogen comes from the angular part of the wavefunction — specifically, from the spherical harmonics."
  type: true-false
  answer: false
  explanation: "False. The principal quantum number n emerges from solving the *radial* part of the Schrödinger equation, not the angular part. The angular part gives the spherical harmonics, which are labeled by l (orbital angular momentum quantum number) and m_l (magnetic quantum number). When the Coulomb potential is substituted into the radial equation and normalizable solutions are required, the energy is forced to take discrete values — only specific values of n produce solutions that don't blow up at large r. So n is fundamentally a radial quantum number, determining both the energy and the overall spatial scale of the orbital."

- question: "In hydrogen, two states with the same principal quantum number n but different orbital quantum numbers l have exactly the same energy (ignoring relativistic corrections and spin effects)."
  type: true-false
  answer: true
  explanation: "True. The energy of a hydrogen eigenstate depends only on n: E_n = −13.6 eV / n². This means all states within a given n — regardless of l and m_l — are degenerate (have the same energy). For example, the 2s (n=2, l=0) and 2p (n=2, l=1) states all have energy −3.4 eV. This 'accidental' degeneracy is a special consequence of the 1/r form of the Coulomb potential. In atoms with more than one electron, electron-electron repulsion breaks this degeneracy, making 2s and 2p have different energies. Fine structure (relativistic effects and spin-orbit coupling) partially lifts it even in hydrogen."

- question: "The hydrogen atom wavefunction requires three quantum numbers n, l, and m_l. Where does each come from, and what physical quantity does each determine?"
  type: short-answer
  answer: "The three quantum numbers arise from the three spatial degrees of freedom in the Schrödinger equation after separation of variables. The φ (azimuthal) equation yields m_l, the magnetic quantum number, which determines the z-component of angular momentum: L_z = m_l ℏ, with m_l = −l, …, +l. The θ (polar) equation yields l, the orbital quantum number, which determines the total angular momentum magnitude: |L| = √(l(l+1)) ℏ, with l = 0, 1, 2, …. The radial equation yields n, the principal quantum number, which determines the energy: E_n = −13.6 eV / n², with n = 1, 2, 3, … and the constraint l ≤ n − 1."
  explanation: "This question tests whether students understand where the quantum numbers come from rather than just knowing their names and ranges. The key insight is that three quantum numbers emerge naturally because the wavefunction depends on three coordinates (r, θ, φ), and separation of variables produces an independent equation for each. Each equation, when solved with physical boundary conditions (normalizability, single-valuedness), produces one quantum number. The quantum numbers are not postulated — they are forced by the mathematics."
```

## Explainer

You already know how to write down and solve the Schrödinger equation for simple systems like the infinite square well, and you know that orbital angular momentum in quantum mechanics is quantized with quantum numbers l and m_l. The hydrogen atom brings these threads together: it is the first physically realistic problem with a three-dimensional, spherically symmetric potential that yields an exact analytic solution.

The key move is **separation of variables**. Because the Coulomb potential V(r) = −e²/4πε₀r depends only on the radial distance r from the nucleus, the wavefunction factors as ψ(r, θ, φ) = R(r) · Y_l^m(θ, φ). The angular part Y_l^m are the **spherical harmonics** — you've seen these from your work on orbital angular momentum. They are the eigenfunctions of L² and L_z, carrying quantum numbers l (orbital quantum number, l = 0, 1, 2, …) and m_l (magnetic quantum number, −l ≤ m_l ≤ l). The spherical harmonics encode the shape of the orbital: s-orbitals are spherically symmetric (l=0), p-orbitals have one nodal plane (l=1), d-orbitals have more complex shapes (l=2), and so on.

The radial equation is trickier. Substituting the Coulomb potential and requiring normalizable solutions forces the energy to be quantized. The allowed energies are E_n = −13.6 eV / n², where n = 1, 2, 3, … is the **principal quantum number**. This matches what was known empirically from spectroscopy (the Rydberg formula), but quantum mechanics derives it from first principles. The corresponding radial wavefunctions R_{nl}(r) are products of an exponential decay and an associated Laguerre polynomial. They depend on both n and l, with the constraint that l = 0, 1, …, n−1. Larger n means the electron is more likely to be found farther from the nucleus, and the energy is closer to zero (less tightly bound).

The complete **hydrogen wavefunction** ψ_{nlm}(r, θ, φ) is labeled by three quantum numbers: n determines the energy, l determines the magnitude of angular momentum, and m_l determines the component of angular momentum along a chosen axis. The ground state (n=1, l=0, m_l=0) is spherically symmetric, purely exponential, and has the smallest possible spatial extent. Each energy level n has n² degenerate states (ignoring spin). This degeneracy is partly accidental — a consequence of the special 1/r form of the Coulomb potential — and it is partially lifted by relativistic corrections and spin effects, which give rise to the fine structure of hydrogen spectral lines.

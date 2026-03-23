---
id: hydrogen-atom-quantum
title: Quantum Mechanical Treatment of Hydrogen
domain: physics
course: quantum-mechanics
prerequisites:
- id: quantum-postulates
  type: hard
- id: angular-momentum-quantum
  type: hard
- id: eigenvalues-eigenvectors
  type: hard
builds-toward:
- hydrogen-atom-spectrum
- fine-structure-splitting
tags:
- hydrogen-atom
- coulomb-potential
- solvable-systems
stage: advanced
status: validated
---

# Quantum Mechanical Treatment of Hydrogen

## Core Idea
The hydrogen atom with Coulomb potential V(r) = -ke²/r is solved in spherical coordinates. Energy levels depend only on principal quantum number n: En = -13.6 eV / n². Wavefunctions ψ_{nlm}(r,θ,φ) are products of radial functions R_{nl}(r) and spherical harmonics Y_l^m(θ,φ). This exactly solvable system marks the triumph of quantum mechanics over classical theory.

## Questions

```yaml
- question: "The hydrogen atom has states labeled by quantum numbers n, l, and m. A student claims that the n=2, l=1, m=0 state has higher energy than the n=2, l=0, m=0 state because it has greater angular momentum. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — higher angular momentum means higher rotational kinetic energy"
    - "No — energy depends only on n; both states are degenerate with energy E₂ = −13.6/4 eV"
    - "Yes — the l=1 state has a node structure that pushes the electron further from the nucleus, raising energy"
    - "No — the l=0 state actually has higher energy because the electron spends more time near the nucleus"
  answer: 1
  explanation: "The energy eigenvalues E_n = −13.6 eV / n² depend only on the principal quantum number n, not on l or m. This is a special feature of the 1/r Coulomb potential. Both the (n=2, l=0, m=0) and (n=2, l=1, m=0) states have exactly the same energy −3.4 eV. For a given n, all states with l ranging from 0 to n−1 and m ranging from −l to l are degenerate — giving n² degenerate states per energy level. Small corrections (spin-orbit coupling, relativistic effects) lift this degeneracy."

- question: "A student describes the hydrogen atom's ground state by saying: 'The electron orbits the proton at a fixed distance of one Bohr radius, a₀.' What is the fundamental error in this description?"
  type: multiple-choice
  options:
    - "The ground state electron orbits at twice the Bohr radius, not one"
    - "The electron does not follow a definite orbital path; the wavefunction gives a probability distribution, and the Bohr radius marks the most probable radial distance"
    - "The description is correct — the Bohr model gives the exact ground state behavior"
    - "The error is that the electron is stationary in the ground state, not orbiting"
  answer: 1
  explanation: "The ground state wavefunction ψ₁₀₀ is a probability amplitude, not a trajectory. The electron has no definite position between measurements — |ψ₁₀₀|² gives the probability density for finding it at any point in space. The Bohr radius a₀ ≈ 0.053 nm marks the peak of the radial probability distribution (the most probable distance), not a fixed orbital radius. The electron can be found anywhere from r=0 to r→∞ with varying probability. This replaces the Bohr model's definite circular orbit with a genuine quantum probability cloud."

- question: "In the hydrogen atom, changing the orbital quantum number l while keeping n fixed does not change the electron's energy."
  type: true-false
  answer: true
  explanation: "The energy E_n = −13.6 eV / n² depends only on n. For n=3, for example, the states l=0, l=1, and l=2 all have energy −13.6/9 ≈ −1.51 eV. This degeneracy in l (and m) is a special property of the pure Coulomb potential. In multielectron atoms, electron-electron repulsion and screening break this degeneracy, making different l values at the same n have different energies — which is why s, p, d, f orbitals fill in the order seen in the periodic table."

- question: "The quantization of hydrogen's energy levels (E_n = −13.6 eV/n²) is an additional postulate imposed on the Schrödinger equation by hand, not derived from it."
  type: true-false
  answer: false
  explanation: "This is false — quantization emerges from the mathematics of the Schrödinger equation itself. The requirement that the wavefunction be normalizable (square-integrable, finite at r=0, decaying to zero as r→∞) forces a quantization condition on the radial solutions. Only specific discrete values of energy allow normalizable solutions; all other energies lead to wavefunctions that diverge at infinity. Quantization is a consequence of boundary conditions, not an assumption — which is why this result was such a triumph over the ad hoc quantization rules of the old Bohr model."

- question: "Why does the hydrogen atom have exactly n² degenerate energy eigenstates for each principal quantum number n?"
  type: short-answer
  answer: "For a given n, the orbital quantum number l can range from 0 to n−1 (giving n possible values). For each l, the magnetic quantum number m ranges from −l to l, giving 2l+1 states. Summing over all l: Σ(l=0 to n−1) (2l+1) = n². This n²-fold degeneracy arises because the Coulomb potential energy depends only on r, not on angular direction, so states with different angular momentum quantum numbers l and m have the same energy."
  explanation: "The degeneracy in m (−l to l) follows directly from the spherical symmetry of the potential — no spatial direction is preferred. The additional degeneracy in l (all l values at a given n have the same energy) is a deeper, accidental symmetry of the 1/r Coulomb potential specifically, sometimes called the SO(4) symmetry. It is lifted by any correction that breaks this special symmetry, such as fine-structure effects. The total n² degeneracy per level is what produces the structure of the periodic table through Aufbau filling."
```

## Explainer

The hydrogen atom is the first and most important exactly solvable system in quantum mechanics. It serves as the foundation for atomic physics, spectroscopy, and ultimately the periodic table. The goal is to find the energy levels and wavefunctions of a single electron bound to a proton by the Coulomb potential V(r) = −ke²/r — attractive, spherically symmetric, and falling off as 1/r.

From your study of eigenvalues and eigenvectors, you know that the time-independent Schrödinger equation is an eigenvalue equation: Ĥψ = Eψ. Because the potential depends only on distance r (spherically symmetric), it is natural to work in **spherical coordinates** (r, θ, φ). From your study of quantum angular momentum, you know the eigenfunctions of L² and Lz are the **spherical harmonics** Y_l^m(θ, φ). The spherical symmetry allows the full wavefunction to separate: ψ_{nlm}(r, θ, φ) = R_{nl}(r) × Y_l^m(θ, φ). The angular part is fully determined by angular momentum theory; what remains is solving for the radial functions R_{nl}(r) subject to the boundary conditions that ψ be normalizable (finite at r = 0 and decaying to zero as r → ∞).

The energy eigenvalues emerge from the normalizability requirement, which forces a quantization condition on the radial solution. This gives **E_n = −13.6 eV / n²**, where n = 1, 2, 3, … is the **principal quantum number**. Three quantum numbers label each state: n (principal, sets the energy), l (orbital angular momentum, 0 to n−1), and m (magnetic, −l to l). The ground state (n=1, l=0, m=0) has energy −13.6 eV — the ionization energy of hydrogen. Excited states have higher (less negative) energy, and the degeneracy grows as n²: for a given n, there are n² distinct states with the same energy because E depends only on n, not on l or m.

The physical picture built by the wavefunctions is rich. For the ground state, the probability density is a simple exponential decay characterized by the **Bohr radius** a₀ ≈ 0.053 nm. For higher n, the radial probability density spreads outward and develops n−l−1 radial nodes. The angular parts give the familiar "orbital shapes" — s orbitals (l=0) are spherically symmetric, p orbitals (l=1) have lobes along the coordinate axes. This is not a circular orbit in any classical sense; it is a genuine probability distribution for where the electron will be found. The true triumph is quantitative: the energy differences E_n − E_{n'} exactly predict the frequencies of hydrogen's spectral lines — the Balmer, Lyman, and Paschen series — explaining with a single formula what decades of empirical spectroscopy had catalogued but not understood.

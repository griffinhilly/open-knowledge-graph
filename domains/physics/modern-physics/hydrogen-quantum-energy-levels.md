---
id: hydrogen-quantum-energy-levels
title: 'Hydrogen Atom: Quantum Energy Levels and Orbitals'
domain: physics
course: modern-physics
prerequisites:
- id: hydrogen-atom-quantum
  type: hard
- id: schrodinger-equation-intro
  type: soft
- id: eigenvalues-and-eigenvectors
  type: hard
- id: spherical-harmonics-electrostatics
  type: soft
builds-toward:
- atomic-orbitals-shapes-nodes
tags:
- atomic-physics
- hydrogen
stage: advanced
status: draft
---

# Hydrogen Atom: Quantum Energy Levels and Orbitals

## Core Idea
Solutions to the Schrödinger equation for hydrogen give energy levels E_n = −13.6 eV/n², matching Bohr's prediction and explaining spectral lines. Each level is labeled by principal quantum number n. Unlike Bohr's orbits, quantum mechanics gives probability densities (orbitals) for finding the electron at various distances from the nucleus, with characteristic spatial shapes determined by angular momentum quantum numbers.

## Explainer

Solving the Schrödinger equation for hydrogen is the quantum mechanical analogue of solving Newton's equations for a planet orbiting the sun — both are two-body inverse-square-law problems. From your prerequisite on the hydrogen atom and Schrödinger equation, you know that the wavefunction ψ(r, θ, φ) must satisfy −(ℏ²/2m)∇²ψ + V(r)ψ = Eψ with V(r) = −e²/(4πε₀r). Separation of variables in spherical coordinates breaks this into a radial equation and an angular equation. The angular equation produces **spherical harmonics** Y_l^m(θ, φ), which your spherical harmonics prerequisite introduced. The radial equation produces quantized energy eigenvalues and associated Laguerre polynomials for the radial part.

The energy eigenvalues E_n = −13.6 eV/n² depend only on the **principal quantum number** n = 1, 2, 3, .... The negative sign reflects that the electron is bound (lower energy than a free electron at infinity). The spacing between levels decreases rapidly: the n=1 to n=2 gap is 10.2 eV, while n=10 to n=11 is only about 0.03 eV. This is why the Lyman series (transitions to n=1) produces ultraviolet photons while the Balmer series (transitions to n=2) produces visible light — those famous red, blue-green, and violet lines in hydrogen's spectrum. Each spectral line corresponds to a photon with energy exactly equal to the difference between two energy levels, E_photon = E_n2 − E_n1 = 13.6 eV × (1/n₁² − 1/n₂²).

The full description of each quantum state requires three quantum numbers. The **principal quantum number** n sets the energy and the overall scale of the orbital. The **angular momentum quantum number** l (ranging from 0 to n−1) sets the total orbital angular momentum: L = √(l(l+1))ℏ. States with l=0 are called s orbitals, l=1 are p, l=2 are d. The **magnetic quantum number** m_l (ranging from −l to +l) sets the z-component of angular momentum. Each (n, l, m_l) triple specifies a distinct orbital with a distinct probability density shape. The 1s orbital (n=1, l=0) is spherically symmetric with maximum electron density at the nucleus. The 2p orbitals (n=2, l=1) have dumbbell shapes with a nodal plane through the nucleus.

The critical conceptual shift from Bohr to quantum mechanics is replacing definite orbits with **probability densities**. There is no trajectory for the electron — only |ψ(r)|² giving the probability per unit volume of finding the electron near point r. The average radius ⟨r⟩ for the 1s orbital is 1.5 times the Bohr radius a₀, and the most probable radius is exactly a₀ ≈ 0.053 nm — so Bohr's model gets the right scale but for the wrong reason. Nodes in the wavefunction (surfaces where |ψ|² = 0) have no classical analogue. The number of radial nodes is n − l − 1 and the number of angular nodes is l, giving a total of n−1 nodes — which is why higher-n states have more oscillatory wavefunctions and more complex spatial structure.

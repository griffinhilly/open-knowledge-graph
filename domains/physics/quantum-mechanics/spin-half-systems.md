---
id: spin-half-systems
title: Spin-1/2 Systems
domain: physics
course: quantum-mechanics
prerequisites:
- id: angular-momentum-quantization
  type: hard
- id: quantum-numbers
  type: soft
builds-toward:
- pauli-matrices
- spin-orbit-coupling
tags:
- spin
- two-level-systems
stage: abstract-reasoning
status: draft
---

# Spin-1/2 Systems

## Core Idea
Electrons and nucleons have intrinsic angular momentum (spin) with s = ½, giving two possible z-components: m_s = ±½. The spin-½ system is the simplest nontrivial quantum system with a 2-dimensional Hilbert space.

## Explainer

You already know from angular momentum quantization that quantum angular momentum is discrete: a particle with angular momentum quantum number j has 2j + 1 possible z-projections, ranging from −j to +j in integer steps. For j = 1 there are three states; for j = 2, five states. For j = ½, there are exactly two states: m = +½ and m = −½. The spin-½ system is the minimal nontrivial quantum system — two states, a 2-dimensional Hilbert space — and it is the proving ground for almost everything interesting in quantum mechanics.

The two basis states are written |↑⟩ = |+½⟩ and |↓⟩ = |−½⟩, called **spin-up** and **spin-down** (relative to whatever axis you designate as z). A general spin state is a **spinor**: |χ⟩ = α|↑⟩ + β|↓⟩ with |α|² + |β|² = 1. The coefficients α and β are complex numbers, and a convenient way to visualize all pure states is the **Bloch sphere**: every normalized spin state corresponds to a point on a unit sphere, where the north pole is |↑⟩ and the south pole is |↓⟩. States on the equator are equal superpositions with different relative phases. Measurement of S_z always yields ±ℏ/2; the probabilities are |α|² and |β|² respectively.

The operators acting on this 2-dimensional space are 2×2 matrices. The spin operators S_x, S_y, S_z are each (ℏ/2) times the corresponding **Pauli matrix** σ_x, σ_y, σ_z — the topic this builds toward. What makes the spin-½ algebra so elegant is the commutation relation [S_x, S_y] = iℏS_z and cyclic permutations, the same algebra as orbital angular momentum, but now realized entirely in a 2-dimensional space with no spatial wavefunction. The eigenstates of S_x and S_y are superpositions of the S_z eigenstates, reflecting the quantum uncertainty between different components of angular momentum.

The spin-½ system is not just a mathematical curiosity — it is the physical description of every electron, every proton, and every neutron. The behavior of atomic spectra, the structure of the periodic table, the stability of matter, and the technology of magnetic resonance imaging (MRI) all depend on getting spin-½ right. When two spin-½ particles are combined, their spin states combine according to Clebsch-Gordan rules, yielding a spin-1 triplet and a spin-0 singlet. When spin is coupled to orbital angular momentum — the next major step toward spin-orbit coupling — the spin-½ structure is what creates the fine structure of spectral lines.

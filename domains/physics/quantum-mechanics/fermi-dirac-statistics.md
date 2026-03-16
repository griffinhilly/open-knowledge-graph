---
id: fermi-dirac-statistics
title: Fermi-Dirac Statistics
domain: physics
course: quantum-mechanics
prerequisites:
- id: bosons-and-fermions
  type: hard
tags:
- fermi-dirac
- fermions
- statistical-mechanics
stage: advanced
status: draft
---

# Fermi-Dirac Statistics

## Core Idea
Fermi-Dirac statistics describe systems of indistinguishable fermions with no two particles in the same single-particle state. The Fermi-Dirac distribution f(E) = 1/(e^{(E-μ)/k_BT} + 1) gives the probability that energy level E is occupied. At T=0, all levels up to the Fermi energy E_F are filled. Electrons cannot be compressed into lower energy states, explaining conductivity and stability of matter.

## Explainer

From your study of bosons and fermions, you know the defining rule for fermions: no two identical fermions can occupy the same quantum state — the Pauli exclusion principle. For bosons, any number can pile into the same state, leading to Bose-Einstein condensation. Fermions must spread out. Fermi-Dirac statistics is simply the systematic accounting of how fermions distribute themselves across available energy levels when subject to this constraint.

Start at absolute zero, T = 0. Imagine filling energy levels from the bottom up, one fermion per state (two electrons per level if you count spin-up and spin-down as distinct). You add fermions until you've placed all N of them. The energy of the topmost occupied state is the **Fermi energy** E_F. Below E_F, every state is occupied with probability 1; above E_F, every state is empty with probability 0. The distribution is a perfect step function. This is entirely unlike classical particles, which would all crowd into the lowest available state. Fermions are forced by quantum statistics to occupy a wide range of energies — the lowest energy a Fermi gas can have is not zero but a substantial fraction of NE_F. This energy is called the **zero-point kinetic energy** of the Fermi gas and is the origin of electron degeneracy pressure in white dwarf stars.

Now turn on temperature. Thermal energy kT gives particles near the Fermi energy the chance to jump to unfilled states above E_F. But electrons deep below E_F have nowhere to jump — all nearby states are already occupied — so they remain frozen in place. Only electrons within roughly kT of E_F can be thermally excited. The sharp step function smooths into the **Fermi-Dirac distribution** f(E) = 1/(e^{(E−μ)/k_BT} + 1). This S-shaped curve transitions from 1 at low energies to 0 at high energies, with the transition centered at the **chemical potential** μ, which is the energy at which the occupation probability is exactly 1/2. At T = 0, μ = E_F exactly. At finite T, μ decreases very slightly as E_F is approached from different directions by thermal excitations and depletions.

The shape of the Fermi-Dirac distribution has a built-in check: at E = μ, the exponent is zero and f = 1/(1+1) = 1/2 regardless of temperature. This means the chemical potential is always the energy at which a state has a 50% chance of being occupied. For typical metals, E_F is on the order of several electron-volts, while room-temperature kT ≈ 0.025 eV. The ratio kT/E_F ≈ 0.01 means temperature is a tiny perturbation — metals at room temperature are nearly as "cold" as they are at absolute zero in a quantum sense. This is why metals have far smaller heat capacities than classical theory predicts.

The physical consequences of Fermi-Dirac statistics extend throughout condensed matter physics. The rigidity of ordinary matter against compression comes partly from electron degeneracy pressure — electrons resist being squeezed together because the Pauli principle forces them into ever-higher energy states. In conductors, electrical current is carried almost entirely by electrons within kT of E_F, and the sharpness of the Fermi surface controls conductivity. In semiconductors, the gap between a filled valence band and an empty conduction band is the Fermi-Dirac picture with μ sitting in a forbidden region. Every time you use an electronic device, Fermi-Dirac statistics is running in the background, governing which electrons can move and which cannot.



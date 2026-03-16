---
id: boltzmann-distribution-molecular-populations
title: Boltzmann Distribution and Molecular Populations
domain: chemistry
course: physical-chemistry
prerequisites:
- id: statistical-mechanics-foundations
  type: hard
- id: kinetic-molecular-theory-overview
  type: hard
- id: exponential-distribution
  type: soft
builds-toward:
- partition-function-thermodynamic-properties
tags:
- statistical-mechanics
- population-distribution
- thermodynamics
stage: advanced
status: draft
---

# Boltzmann Distribution and Molecular Populations

## Core Idea
At thermal equilibrium, the population of energy state i follows N_i/N_total ∝ e^(-E_i/k_B T), the Boltzmann distribution. This fundamental relation connects molecular-level energy spacing to macroscopic observables: at low T, only ground state is populated; at high T, many excited states are occupied. The exponential factor reflects how thermal energy k_B T compares to level spacing.

## How It's Best Learned
Calculate population distributions for simple systems (two-level atoms, harmonic oscillators, rotors) at various temperatures. Observe how distributions broaden and shift as temperature increases.

## Explainer

From kinetic molecular theory, you know that molecules in a gas have a distribution of speeds and energies — not all molecules move at the same velocity. From statistical mechanics foundations, you understand that macroscopic properties emerge from averaging over enormous numbers of microstates. The **Boltzmann distribution** gives the precise mathematical form of this averaging: it tells you exactly what fraction of molecules occupy each available energy level at a given temperature.

The central equation is deceptively simple: the probability of finding a molecule in energy state i is proportional to **e^(−Eᵢ/k_BT)**, where Eᵢ is the energy of that state, k_B is Boltzmann's constant, and T is absolute temperature. The exponential function does all the work. When an energy level is much higher than k_BT (the "thermal energy"), the exponential becomes vanishingly small — almost no molecules occupy that state. When an energy level is comparable to or less than k_BT, the exponential is close to 1 — that state is well-populated. The ratio k_BT acts as a yardstick: it sets the energy scale that separates "accessible" from "inaccessible" states at a given temperature.

Consider the simplest case: a two-level system with a ground state at energy 0 and an excited state at energy ε. At very low temperature (k_BT ≪ ε), the exponential factor e^(−ε/k_BT) is essentially zero, and virtually all molecules sit in the ground state. As temperature rises, k_BT approaches ε, and the excited state begins to populate. At very high temperature (k_BT ≫ ε), both states approach equal population — the exponential factor approaches 1, and thermal energy is so abundant that the energy gap hardly matters. This behavior generalizes to any number of levels: raising temperature always broadens the population distribution, spreading molecules across more states.

The Boltzmann distribution has far-reaching consequences you will encounter repeatedly. It explains why reaction rates increase with temperature (more molecules have enough energy to surmount activation barriers), why spectral line intensities depend on temperature (the population of the absorbing state changes), and why heat capacities vary with temperature (new degrees of freedom "turn on" as k_BT exceeds their energy spacing). The **partition function** — the sum of Boltzmann factors over all states — normalizes this distribution and becomes the central object in statistical thermodynamics, connecting molecular energy levels directly to macroscopic quantities like entropy, free energy, and equilibrium constants.

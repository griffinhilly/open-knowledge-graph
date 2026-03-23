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
status: validated
---

# Boltzmann Distribution and Molecular Populations

## Core Idea
At thermal equilibrium, the population of energy state i follows N_i/N_total ∝ e^(-E_i/k_B T), the Boltzmann distribution. This fundamental relation connects molecular-level energy spacing to macroscopic observables: at low T, only ground state is populated; at high T, many excited states are occupied. The exponential factor reflects how thermal energy k_B T compares to level spacing.

## How It's Best Learned
Calculate population distributions for simple systems (two-level atoms, harmonic oscillators, rotors) at various temperatures. Observe how distributions broaden and shift as temperature increases.

## Questions

```yaml
- question: "A molecule has a ground state at E=0 and an excited state at energy ε. At temperature T where k_BT = ε/4, approximately what fraction of molecules occupy the excited state?"
  type: multiple-choice
  options:
    - "About 50%, because both states are available"
    - "Very small (close to 0), because k_BT is much less than ε"
    - "About 25%, equal to the ratio k_BT/ε"
    - "Exactly ε/(2k_BT), from the Boltzmann formula"
  answer: 1
  explanation: "When k_BT = ε/4, the ratio ε/k_BT = 4, so the Boltzmann factor is e^(-4) ≈ 0.018 — very small. The excited state population is proportional to e^(-ε/k_BT), which becomes vanishingly small when thermal energy is much less than the level spacing. Option A is wrong because availability does not equal equal population; option C mistakes a linear ratio for an exponential one."

- question: "A spectroscopist observes that at room temperature a vibrational spectral band has very low intensity, but the intensity increases dramatically when the sample is heated. What does this tell us about the energy spacing of the vibrational levels?"
  type: multiple-choice
  options:
    - "The vibrational spacing is much smaller than k_BT at room temperature"
    - "The vibrational spacing is much larger than k_BT at room temperature"
    - "Heating increases the number of molecules, increasing intensity"
    - "The energy spacing increases with temperature"
  answer: 1
  explanation: "Low intensity at room temperature means the absorbing state (excited vibrational level) has very low population — the Boltzmann factor e^(-E/k_BT) is small, meaning E ≫ k_BT. As temperature rises, k_BT approaches the level spacing and more molecules populate the excited state, increasing absorption intensity. Option A would predict high population (and high intensity) at room temperature. Heating does not create molecules (C), and energy spacings are fixed by molecular structure (D)."

- question: "At very high temperatures, all energy levels in a multi-level system approach equal population."
  type: true-false
  answer: true
  explanation: "As T → ∞, k_BT becomes arbitrarily large compared to any finite energy spacing. Every Boltzmann factor e^(-E_i/k_BT) approaches e^0 = 1 regardless of E_i, so all levels carry equal weight. This is the high-temperature limit where thermal energy completely overwhelms energy level differences, and the distribution becomes uniform."

- question: "In a two-level system, raising the temperature always increases the fraction of molecules in the ground state."
  type: true-false
  answer: false
  explanation: "Raising temperature increases the population of excited states and *decreases* the fraction in the ground state. The Boltzmann distribution spreads population across more states as temperature rises. At very low T, nearly all molecules are in the ground state; as T increases, population flows into excited states. The ground state fraction N₀/N_total = 1/(1 + e^(-ε/k_BT)) decreases monotonically as T increases."

- question: "Why does the Boltzmann distribution predict that reaction rates increase with temperature, even when the reaction's overall energy change is unchanged?"
  type: short-answer
  answer: "Reaction rates increase with temperature because the Boltzmann distribution shifts more molecules into high-energy states as T rises. The fraction of molecules with enough energy to surmount the activation barrier E_a is proportional to e^(-E_a/k_BT). As T increases, k_BT grows, the exponential factor becomes larger, and more molecules have enough energy to react. The activation energy has not changed — but the fraction of the population above it has."
  explanation: "This is the physical content of the Arrhenius equation k = A·e^(-E_a/RT), which is a direct consequence of the Boltzmann distribution. Temperature is the knob that controls which states are thermally accessible — it shifts the population distribution, not the energy levels themselves."
```

## Explainer

From kinetic molecular theory, you know that molecules in a gas have a distribution of speeds and energies — not all molecules move at the same velocity. From statistical mechanics foundations, you understand that macroscopic properties emerge from averaging over enormous numbers of microstates. The **Boltzmann distribution** gives the precise mathematical form of this averaging: it tells you exactly what fraction of molecules occupy each available energy level at a given temperature.

The central equation is deceptively simple: the probability of finding a molecule in energy state i is proportional to **e^(−Eᵢ/k_BT)**, where Eᵢ is the energy of that state, k_B is Boltzmann's constant, and T is absolute temperature. The exponential function does all the work. When an energy level is much higher than k_BT (the "thermal energy"), the exponential becomes vanishingly small — almost no molecules occupy that state. When an energy level is comparable to or less than k_BT, the exponential is close to 1 — that state is well-populated. The ratio k_BT acts as a yardstick: it sets the energy scale that separates "accessible" from "inaccessible" states at a given temperature.

Consider the simplest case: a two-level system with a ground state at energy 0 and an excited state at energy ε. At very low temperature (k_BT ≪ ε), the exponential factor e^(−ε/k_BT) is essentially zero, and virtually all molecules sit in the ground state. As temperature rises, k_BT approaches ε, and the excited state begins to populate. At very high temperature (k_BT ≫ ε), both states approach equal population — the exponential factor approaches 1, and thermal energy is so abundant that the energy gap hardly matters. This behavior generalizes to any number of levels: raising temperature always broadens the population distribution, spreading molecules across more states.

The Boltzmann distribution has far-reaching consequences you will encounter repeatedly. It explains why reaction rates increase with temperature (more molecules have enough energy to surmount activation barriers), why spectral line intensities depend on temperature (the population of the absorbing state changes), and why heat capacities vary with temperature (new degrees of freedom "turn on" as k_BT exceeds their energy spacing). The **partition function** — the sum of Boltzmann factors over all states — normalizes this distribution and becomes the central object in statistical thermodynamics, connecting molecular energy levels directly to macroscopic quantities like entropy, free energy, and equilibrium constants.

---
id: density-of-states-fermi-gas
title: Density of States in Fermi Gas
domain: physics
course: statistical-mechanics
prerequisites:
- id: ideal-fermi-gas-t-equals-zero
  type: hard
builds-toward:
- fermi-gas-finite-temperature
tags:
- fermi-gas
- density-of-states
- dispersion
stage: expert
status: validated
---

# Density of States in Fermi Gas

## Core Idea
The density of states g(E) counts the number of states per unit energy interval. For a 3D free-electron Fermi gas, g(E) ∝ √E. At the Fermi surface, g(E_F) = 3N/(2E_F), which relates the jump in the Fermi-Dirac distribution to the density of states and determines the linear heat capacity coefficient.

## Questions

```yaml
- question: "The classical (Boltzmann) prediction for the heat capacity of a gas of electrons is about 100 times larger than what is actually measured in metals at room temperature. The correct quantum explanation is:"
  type: multiple-choice
  options:
    - "Electrons in metals move more slowly than the classical model predicts, so they carry less thermal energy"
    - "Pauli exclusion prevents all electrons except those within ~k_BT of the Fermi energy from absorbing thermal energy — the vast majority are 'frozen' in filled states with no available nearby states to transition into"
    - "The Fermi gas model overestimates the number of electrons by including core electrons that don't move freely"
    - "Electrons lose most of their thermal energy to the lattice before it can be measured as heat capacity"
  answer: 1
  explanation: "In a classical gas, every particle can absorb ~k_BT of thermal energy when temperature rises. In a Fermi gas, Pauli exclusion blocks this for all electrons except those within ~k_BT of the Fermi surface — roughly k_BT/E_F ≈ 1% of electrons at room temperature. Each of these electrons gains ~k_BT, giving C_V ∝ (k_BT/E_F) × Nk_B × T ∝ T, much smaller than the classical Nk_B. The enormous depth of filled states means almost all electrons cannot change their energy at all — there are simply no empty states nearby for them to move into."

- question: "The density of states g(E) ∝ √E in a 3D free-electron gas arises because:"
  type: multiple-choice
  options:
    - "Higher-energy electrons are more likely to be thermally excited, creating more available states near the top"
    - "The Pauli exclusion principle forces states to spread out more at higher energies"
    - "States are uniformly distributed in k-space, and the volume of a spherical shell at radius k grows as k² — which, since E ∝ k², means the number of states per unit energy grows as √E"
    - "Electrons at higher energies have longer de Broglie wavelengths, allowing more standing wave modes"
  answer: 2
  explanation: "The √E dependence is purely geometric. In k-space, each allowed wavevector occupies the same tiny volume (2π/L)³. The number of states with energy below E equals the volume of a sphere of radius k(E) ∝ √E in k-space, giving N(E) ∝ E^(3/2). The density of states g(E) = dN/dE ∝ E^(1/2) = √E. More states are packed per unit energy at higher energies simply because the spherical shell in k-space has larger area (∝ k² ∝ E). Option D has the wavelength relationship backwards — higher energy means shorter de Broglie wavelength (λ = h/p)."

- question: "In a Fermi gas at low temperature, the electronic heat capacity is small because only electrons near the Fermi energy can be thermally excited. At absolute zero, this contribution is exactly zero."
  type: true-false
  answer: true
  explanation: "At T = 0, the Fermi-Dirac distribution is a perfect step function: all states below E_F are filled, all above are empty. No electron can change its energy without violating Pauli exclusion (there are no nearby empty states). When T > 0, only electrons within ~k_BT of E_F have access to empty states just above them and can absorb thermal energy. As T → 0, k_BT → 0 and the fraction of excitable electrons vanishes, making C_V → 0. The linear-T electronic heat capacity C_V = γT with γ ∝ g(E_F) reflects this: at T = 0, C_V = 0."

- question: "The density of states at the Fermi energy g(E_F) is the key quantity determining the electronic heat capacity of a metal, with C_V proportional to g(E_F) × T."
  type: true-false
  answer: true
  explanation: "g(E_F) determines how many electrons can be thermally excited at a given temperature — it counts the states available within ~k_BT of E_F. The number of excitable electrons is ∝ g(E_F) × k_BT, and each gains ~k_BT energy, giving C_V ∝ g(E_F) k_B² T. The formula g(E_F) = 3N/(2E_F) makes this quantitative. This is why materials with high densities of states at the Fermi level (transition metals, superconductors near their transition temperature) have enhanced heat capacities — and why engineering the density of states via band structure is central to materials design."

- question: "Why does only a small fraction of electrons in a metal contribute to its heat capacity, and how does the density of states g(E_F) quantify this fraction?"
  type: short-answer
  answer: "Pauli exclusion means that for an electron to absorb thermal energy, there must be an empty state at slightly higher energy for it to move into. At low temperature, all states up to E_F are filled and all above are empty. Only electrons within ~k_BT of E_F have nearby empty states and can be thermally excited. The fraction of excitable electrons is ∝ k_BT/E_F — at room temperature in copper (~0.025 eV vs. E_F ~ 7 eV) this is about 0.4%. The density of states g(E_F) counts how many states per unit energy are available at the Fermi surface, so the number of excitable electrons is g(E_F) × k_BT, and C_V = (dU/dT) ∝ g(E_F) k_B² T."
  explanation: "The contrast with a classical gas is stark: classically every electron contributes ~k_B/2 per degree of freedom. In the Fermi gas, only those within k_BT of E_F contribute — roughly 1% at room temperature. This explains why metals have much lower electronic heat capacities than naive classical models predict, a puzzle that was resolved only after Fermi-Dirac statistics were developed."
```

## Explainer

From the ideal Fermi gas at zero temperature, you know that electrons fill all states up to the Fermi energy E_F, with every state below occupied and every state above empty. But how many states are available near any given energy? The **density of states** g(E) answers this question: it is the number of quantum states per unit energy per unit volume, telling you how densely packed the available energy levels are at each energy.

To derive g(E) for free electrons in 3D, think of momentum space. Each allowed wavevector **k** occupies a volume (2π/L)³ in k-space for a box of side L. The number of states with energy below E is proportional to the volume of a sphere of radius k(E) = √(2mE)/ℏ in k-space, giving N(E) ∝ E^(3/2). Differentiating: g(E) = dN/dE ∝ √E. The **√E dependence** is the fundamental result for a 3D parabolic dispersion. More states are available at higher energies, which is a purely geometric consequence of the spherical shell in k-space growing as its radius increases.

At the Fermi surface specifically, g(E_F) = 3N/(2E_F), where N is the total number of electrons. This formula appears repeatedly because the Fermi surface is where almost all interesting physics happens. When temperature is raised slightly above zero, only electrons within ~k_BT of E_F can be thermally excited — all others are locked in place by the Pauli exclusion principle. The number of excitable electrons is proportional to g(E_F) × k_BT, and each gains roughly k_BT in energy, giving an electronic heat capacity C_V ∝ g(E_F) k_B² T. This is the famous linear-T electronic heat capacity, and g(E_F) is its coefficient.

The broader lesson is that g(E) acts as a weight function for all thermal averages. The average energy, total particle number, and any equilibrium observable are integrals of the form ∫ (quantity) × g(E) × f(E) dE, where f(E) is the Fermi-Dirac distribution. Changing the material — say, going from a 3D free gas to a 2D electron gas or to a material with a different dispersion relation — changes g(E) and can dramatically alter thermal, electrical, and magnetic properties. This is why engineering the density of states through band structure is central to semiconductor and material design.

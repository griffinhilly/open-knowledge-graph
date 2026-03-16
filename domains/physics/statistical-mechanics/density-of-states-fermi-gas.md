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
stage: advanced
status: draft
---

# Density of States in Fermi Gas

## Core Idea
The density of states g(E) counts the number of states per unit energy interval. For a 3D free-electron Fermi gas, g(E) ∝ √E. At the Fermi surface, g(E_F) = 3N/(2E_F), which relates the jump in the Fermi-Dirac distribution to the density of states and determines the linear heat capacity coefficient.

## Explainer

From the ideal Fermi gas at zero temperature, you know that electrons fill all states up to the Fermi energy E_F, with every state below occupied and every state above empty. But how many states are available near any given energy? The **density of states** g(E) answers this question: it is the number of quantum states per unit energy per unit volume, telling you how densely packed the available energy levels are at each energy.

To derive g(E) for free electrons in 3D, think of momentum space. Each allowed wavevector **k** occupies a volume (2π/L)³ in k-space for a box of side L. The number of states with energy below E is proportional to the volume of a sphere of radius k(E) = √(2mE)/ℏ in k-space, giving N(E) ∝ E^(3/2). Differentiating: g(E) = dN/dE ∝ √E. The **√E dependence** is the fundamental result for a 3D parabolic dispersion. More states are available at higher energies, which is a purely geometric consequence of the spherical shell in k-space growing as its radius increases.

At the Fermi surface specifically, g(E_F) = 3N/(2E_F), where N is the total number of electrons. This formula appears repeatedly because the Fermi surface is where almost all interesting physics happens. When temperature is raised slightly above zero, only electrons within ~k_BT of E_F can be thermally excited — all others are locked in place by the Pauli exclusion principle. The number of excitable electrons is proportional to g(E_F) × k_BT, and each gains roughly k_BT in energy, giving an electronic heat capacity C_V ∝ g(E_F) k_B² T. This is the famous linear-T electronic heat capacity, and g(E_F) is its coefficient.

The broader lesson is that g(E) acts as a weight function for all thermal averages. The average energy, total particle number, and any equilibrium observable are integrals of the form ∫ (quantity) × g(E) × f(E) dE, where f(E) is the Fermi-Dirac distribution. Changing the material — say, going from a 3D free gas to a 2D electron gas or to a material with a different dispersion relation — changes g(E) and can dramatically alter thermal, electrical, and magnetic properties. This is why engineering the density of states through band structure is central to semiconductor and material design.

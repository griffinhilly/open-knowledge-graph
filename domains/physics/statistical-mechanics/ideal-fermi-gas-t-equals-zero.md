---
id: ideal-fermi-gas-t-equals-zero
title: Ideal Fermi Gas at T=0
domain: physics
course: statistical-mechanics
prerequisites:
- id: fermi-dirac-statistics
  type: hard
builds-toward:
- fermi-energy-fermi-surface
- fermi-gas-finite-temperature
tags:
- fermi-gas
- degenerate
- ground-state
stage: advanced
status: draft
---

# Ideal Fermi Gas at T=0

## Core Idea
At T=0, all states with energy E < E_F (Fermi energy) are filled, all above are empty. The Fermi energy for a 3D gas is E_F = (ℏ^2/2m)(3π^2 n)^{2/3}, where n = N/V is the number density. The ground-state energy U_0 = (3/5)NE_F and pressure P = (2/5)n E_F arise from quantum degeneracy, not thermal motion.

## Explainer

From Fermi-Dirac statistics, you know that the average occupancy of a single-particle state with energy ε is f(ε) = 1/(e^{(ε−μ)/k_BT} + 1). At absolute zero, this step function becomes perfectly sharp: f(ε) = 1 for ε < μ and f(ε) = 0 for ε > μ. The chemical potential at T = 0 is called the **Fermi energy** E_F. Every state below E_F is exactly full; every state above is exactly empty. This filled-up-to-a-sharp-cutoff structure is called the **Fermi sea**, and its surface in momentum space is the **Fermi surface**.

To find E_F, count how many states fit below it. For a 3D ideal gas in a box of volume V, the density of states is g(ε) = (V/2π²)(2m/ℏ²)^{3/2} √ε. Setting the integral ∫₀^{E_F} g(ε)dε = N (with a factor of 2 for spin) and solving gives E_F = (ℏ²/2m)(3π²n)^{2/3}. This is a purely quantum result — it depends only on the number density n = N/V and the particle mass, with no temperature anywhere. For electrons in copper, E_F ≈ 7 eV, corresponding to an equivalent temperature T_F = E_F/k_B ≈ 80,000 K. The electrons are deeply quantum degenerate at any laboratory temperature.

The ground-state energy is not zero. Even at T = 0, fermions cannot all sit in the lowest state — the Pauli principle distributes them across levels from 0 up to E_F. Integrating ε × g(ε) from 0 to E_F gives U₀ = (3/5)NE_F. This is roughly 60% of the classical equipartition expectation (3/2)Nk_BT_F, reflecting the filled distribution below E_F. The resulting **degeneracy pressure** P = (2/3)(U₀/V) = (2/5)nE_F is what holds up a white dwarf star against gravity — the electrons are so densely packed that quantum pressure alone resists gravitational collapse, with no thermal contribution needed.

This T = 0 picture is the starting point for understanding real metals. At room temperature k_BT ≈ 0.025 eV ≪ E_F ≈ 7 eV, so only electrons within roughly k_BT of the Fermi surface can be thermally excited — the vast interior of the Fermi sea is frozen by the Pauli principle. This explains why metals have far smaller electronic heat capacities than classical theory predicts (the Drude model's failure), and why the heat capacity is linear in T at low temperatures rather than constant.

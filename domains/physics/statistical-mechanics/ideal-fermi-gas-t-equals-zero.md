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
stage: expert
status: draft
---

# Ideal Fermi Gas at T=0

## Core Idea
At T=0, all states with energy E < E_F (Fermi energy) are filled, all above are empty. The Fermi energy for a 3D gas is E_F = (ℏ^2/2m)(3π^2 n)^{2/3}, where n = N/V is the number density. The ground-state energy U_0 = (3/5)NE_F and pressure P = (2/5)n E_F arise from quantum degeneracy, not thermal motion.

## Questions

```yaml
- question: "The number density of conduction electrons in metal A is twice that of metal B. How does the Fermi energy of A compare to that of B?"
  type: multiple-choice
  options:
    - "It is twice as large, since twice as many electrons need to be accommodated"
    - "It is about 1.59 times larger, since E_F ∝ n^{2/3} and 2^{2/3} ≈ 1.587"
    - "It is the same, since Fermi energy depends on temperature, which is zero for both"
    - "It is four times larger, since packing twice the electrons requires twice the momentum in each dimension"
  answer: 1
  explanation: "The Fermi energy formula E_F = (ℏ²/2m)(3π²n)^{2/3} gives E_F ∝ n^{2/3}. Doubling n gives 2^{2/3} ≈ 1.587, not 2. Option A would be true if E_F were proportional to n; option C is wrong because E_F is explicitly independent of temperature; option D would require a linear momentum dependence, but the kinetic energy goes as p²/2m."

- question: "A white dwarf star is supported against gravitational collapse. At its core temperature of ~10⁷ K, the Fermi temperature of the electrons is ~10¹⁰ K. What primarily provides the supporting pressure?"
  type: multiple-choice
  options:
    - "Thermal pressure from hot electrons colliding with the star's walls"
    - "Radiation pressure from photons trapped in the dense core"
    - "Degeneracy pressure arising from the Pauli exclusion principle, independent of temperature"
    - "Electrostatic repulsion between negatively charged electrons"
  answer: 2
  explanation: "Because T ≪ T_F, the electrons are deeply quantum degenerate — the vast majority cannot be thermally excited above the Fermi sea. The pressure P = (2/5)nE_F is a quantum mechanical result with no temperature dependence; it persists even as the star cools toward absolute zero. This is why white dwarfs don't collapse: the degeneracy pressure is not thermal and cannot be 'turned off' by cooling."

- question: "At T=0, the ground-state energy per particle of an ideal Fermi gas equals (3/5)E_F, which is about 60% of the Fermi energy."
  type: true-false
  answer: true
  explanation: "This follows directly from integrating ε × g(ε) from 0 to E_F: U₀ = ∫₀^{E_F} ε g(ε) dε = (3/5)NE_F, giving an average energy per particle of (3/5)E_F. The result is not zero because the Pauli exclusion principle forces fermions to fill all states from the ground state up to E_F — they cannot all sit at the lowest energy level."

- question: "At T=0, all fermions in an ideal Fermi gas occupy the single lowest-energy quantum state."
  type: true-false
  answer: false
  explanation: "This is the key misconception to avoid. The Pauli exclusion principle forbids two identical fermions from occupying the same quantum state. At T=0, fermions fill states one by one from the ground state upward, forming the Fermi sea: every state with energy below E_F is exactly filled, every state above is exactly empty. The zero-temperature state is not a Bose-Einstein condensate — it is a fully filled band up to the Fermi energy, which is why the ground-state energy is large and nonzero."

- question: "Why does the Fermi energy of a metal depend on electron number density but not on temperature?"
  type: short-answer
  answer: "The Fermi energy is determined by counting: you fill available quantum states (each holding at most one electron per spin state, by the Pauli principle) until all N electrons are accommodated. This counting depends only on how many electrons there are per unit volume (the density n) and on the density of states g(ε), which is set by mass and the box geometry. Temperature controls how sharply the occupation function cuts off at E_F, but at T=0 the cutoff is a perfect step function and E_F is exactly the energy of the last filled state — a purely combinatorial, not thermal, quantity."
  explanation: "The classical ideal gas has energy that grows linearly with T because particles can explore all energies freely. In the Fermi gas, the Pauli principle forces a fixed 'stacking' of electrons into states regardless of temperature. As long as k_BT ≪ E_F (true for metals at all laboratory temperatures), the Fermi energy is essentially temperature-independent. This is why the electronic heat capacity of metals is far smaller than the classical prediction — most electrons are frozen deep in the Fermi sea and cannot absorb thermal energy."
```

## Explainer

From Fermi-Dirac statistics, you know that the average occupancy of a single-particle state with energy ε is f(ε) = 1/(e^{(ε−μ)/k_BT} + 1). At absolute zero, this step function becomes perfectly sharp: f(ε) = 1 for ε < μ and f(ε) = 0 for ε > μ. The chemical potential at T = 0 is called the **Fermi energy** E_F. Every state below E_F is exactly full; every state above is exactly empty. This filled-up-to-a-sharp-cutoff structure is called the **Fermi sea**, and its surface in momentum space is the **Fermi surface**.

To find E_F, count how many states fit below it. For a 3D ideal gas in a box of volume V, the density of states is g(ε) = (V/2π²)(2m/ℏ²)^{3/2} √ε. Setting the integral ∫₀^{E_F} g(ε)dε = N (with a factor of 2 for spin) and solving gives E_F = (ℏ²/2m)(3π²n)^{2/3}. This is a purely quantum result — it depends only on the number density n = N/V and the particle mass, with no temperature anywhere. For electrons in copper, E_F ≈ 7 eV, corresponding to an equivalent temperature T_F = E_F/k_B ≈ 80,000 K. The electrons are deeply quantum degenerate at any laboratory temperature.

The ground-state energy is not zero. Even at T = 0, fermions cannot all sit in the lowest state — the Pauli principle distributes them across levels from 0 up to E_F. Integrating ε × g(ε) from 0 to E_F gives U₀ = (3/5)NE_F. This is roughly 60% of the classical equipartition expectation (3/2)Nk_BT_F, reflecting the filled distribution below E_F. The resulting **degeneracy pressure** P = (2/3)(U₀/V) = (2/5)nE_F is what holds up a white dwarf star against gravity — the electrons are so densely packed that quantum pressure alone resists gravitational collapse, with no thermal contribution needed.

This T = 0 picture is the starting point for understanding real metals. At room temperature k_BT ≈ 0.025 eV ≪ E_F ≈ 7 eV, so only electrons within roughly k_BT of the Fermi surface can be thermally excited — the vast interior of the Fermi sea is frozen by the Pauli principle. This explains why metals have far smaller electronic heat capacities than classical theory predicts (the Drude model's failure), and why the heat capacity is linear in T at low temperatures rather than constant.

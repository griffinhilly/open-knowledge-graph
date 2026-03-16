---
id: fermi-gas-finite-temperature
title: Fermi Gas at Finite Temperature
domain: physics
course: statistical-mechanics
prerequisites:
- id: fermi-energy-fermi-surface
  type: hard
- id: canonical-ensemble
  type: soft
tags:
- fermi-gas
- thermal-effects
- thermodynamic-quantities
stage: advanced
status: draft
---

# Fermi Gas at Finite Temperature

## Core Idea
For kT ≪ E_F, the Fermi-Dirac distribution n(E) ≈ 1 for E < μ(T), ≈ 0 for E > μ(T), smoothing over a width ~kT. Chemical potential μ(T) ≈ E_F [1 − π^2(kT/E_F)^2/12 + ...]. Heat capacity C_V ≈ (π^2 k_B^2 T / 3) g(E_F) is linear in T, a signature of Fermi liquid behavior.

## Explainer

From your study of the Fermi energy and Fermi surface, you have the T = 0 picture: a sharp step function in the occupation number, with all states filled below E_F and all states empty above it. The Fermi surface in k-space is the boundary between occupied and empty states — for a free electron gas it's a perfect sphere, and for real metals it's a complex shape that controls nearly every electronic property. The question at finite temperature is: what happens to this sharp boundary when thermal energy becomes available?

The key insight is that only electrons within roughly kT of the Fermi energy can be affected by temperature. An electron deep in the Fermi sea, say 1 eV below E_F, cannot absorb a thermal fluctuation of 0.025 eV (room temperature) because every neighboring state it might jump into is already occupied. Only electrons close to E_F have access to empty states just above. The result is that the sharp step at E_F smears out over a width of about 4kT, with electrons just below E_F having slightly less than full occupation and electrons just above E_F having slightly more than zero occupation. Everywhere far from E_F, the distribution is essentially unchanged from the T = 0 result.

This thermal smearing also shifts the **chemical potential** μ(T) slightly below E_F. The reason is asymmetric: the density of states g(E) typically increases with energy (in 3D, g(E) ∝ √E), so there are more states just above E_F than just below it. When temperature smears the distribution, slightly more electrons are promoted above E_F than are removed from below, which means the system has "too many" electrons at high energies relative to the symmetric case. To keep the total electron count fixed, μ must shift downward to re-balance. The leading correction is μ(T) ≈ E_F[1 − (π²/12)(kT/E_F)²], a quadratic suppression that is tiny for metals at room temperature.

The linear heat capacity is the most experimentally important prediction. Classical statistical mechanics predicts each electron should contribute (3/2)k_B to the heat capacity — a result that dramatically overestimates the measured heat capacity of metals. The resolution is that only the fraction ~kT/E_F of electrons near the Fermi surface can absorb thermal energy. Each of these electrons picks up energy of order kT, giving an electronic contribution to heat capacity of C_V^{el} ∝ Nk_B(kT/E_F) ∝ T. This linear T dependence is a characteristic signature of **Fermi liquid behavior** and has been confirmed in countless metals. At very low temperatures where lattice vibrations (which contribute C_V ∝ T³) are frozen out, the linear electronic term dominates, allowing direct measurement of g(E_F).

The Sommerfeld expansion — expanding thermodynamic quantities in powers of (kT/E_F) — is the systematic framework for computing all finite-temperature corrections. The same framework predicts the **Wiedemann-Franz law**: the ratio of thermal to electrical conductivity is proportional to T, with a universal coefficient. Both heat and charge are carried by electrons near the Fermi surface, and the ratio of these two transport coefficients depends only on fundamental constants and T. This law, confirmed across a wide range of metals, is another consequence of the Fermi-Dirac distribution applied to a nearly-free electron gas. Deviations from it signal that electron-electron or electron-phonon scattering is breaking the simple Fermi liquid picture.



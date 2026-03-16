---
id: photon-gas-thermodynamics
title: Photon Gas Thermodynamics
domain: physics
course: statistical-mechanics
prerequisites:
- id: planck-distribution-blackbody
  type: hard
- id: partition-function-definition
  type: soft
tags:
- photon-gas
- radiation-thermodynamics
- blackbody
stage: advanced
status: draft
---

# Photon Gas Thermodynamics

## Core Idea
Photon gas is a Bose gas with zero chemical potential (photons created/destroyed freely). Average energy U = (π^2 k_B^4 T^4 V)/(15 ℏ^3 c^3), pressure P = U/(3V) = (π^2 k_B^4 T^4)/(45 ℏ^3 c^3), and entropy S = (4π^2 k_B^4 T^3 V)/(45 ℏ^3 c^3). Radiation pressure P ∝ T^4 is significant in stellar interiors and early universe.

## Explainer

You already know the Planck distribution for blackbody radiation: the mean number of photons in a mode of frequency ω is n̄ = 1/(e^{ℏω/k_BT} − 1). This is the Bose-Einstein distribution with **chemical potential μ = 0**. The reason μ = 0 is that photons are not conserved — a cavity wall can absorb or emit photons freely, so there is no constraint fixing the total photon number, and the Lagrange multiplier that enforces a number constraint (the chemical potential) is therefore zero. This is the key distinction from a gas of atoms: atoms have a conserved number and nonzero μ; photons in thermal equilibrium do not.

To get thermodynamic quantities, sum the energy over all modes. Each mode has two polarization states, wavevector k = ω/c, and energy ℏω per photon. The energy density is an integral over the Planck distribution weighted by the density of modes. This integral evaluates to U/V = (π²k_B⁴T⁴)/(15ℏ³c³), proportional to T⁴. The heat capacity is C_V = dU/dT ∝ T³, and the entropy S ∝ T³ as well. These power laws all trace back to a single feature: photons are massless bosons with a linear dispersion ω = ck and μ = 0, so the only energy scale is k_BT.

The **Stefan-Boltzmann law** for the power radiated per unit area by a blackbody, P/A = σT⁴ with σ = (π²k_B⁴)/(60ℏ³c²), emerges directly from U ∝ T⁴V. The radiation pressure P_rad = U/(3V) is a consequence of the photon gas having the same equation of state as any ultrarelativistic gas: P = u/3 where u is energy density. For ordinary gases you learned P = (2/3)(kinetic energy density), but photons travel at c and the factor becomes 1/3 instead. This radiation pressure is negligible on Earth but dominant in the interior of massive stars (where T ~ 10⁷ K) and was the dominant pressure in the early universe when temperatures exceeded 10⁹ K.

The connection to your partition function work is immediate: the photon gas grand canonical partition function factors into independent mode contributions because μ = 0 eliminates the coupling between modes imposed by total-number conservation. Each mode is a simple quantum harmonic oscillator, and the grand potential is Ω = −k_BT Σ_k ln(1 − e^{−ℏω_k/k_BT}). Converting the sum to an integral and evaluating gives all the T⁴ results above. The photon gas is thus one of the cleanest examples of a fully quantum statistical mechanical system — solvable exactly, physically transparent, and experimentally verified to high precision via measurements of the cosmic microwave background.

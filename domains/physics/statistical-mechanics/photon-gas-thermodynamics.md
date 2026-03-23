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
stage: expert
status: validated
---

# Photon Gas Thermodynamics

## Core Idea
Photon gas is a Bose gas with zero chemical potential (photons created/destroyed freely). Average energy U = (π^2 k_B^4 T^4 V)/(15 ℏ^3 c^3), pressure P = U/(3V) = (π^2 k_B^4 T^4)/(45 ℏ^3 c^3), and entropy S = (4π^2 k_B^4 T^3 V)/(45 ℏ^3 c^3). Radiation pressure P ∝ T^4 is significant in stellar interiors and early universe.

## Questions

```yaml
- question: "Why does a photon gas in thermal equilibrium have zero chemical potential (μ = 0)?"
  type: multiple-choice
  options:
    - "Because photons are massless, so they carry no rest-mass energy to assign a chemical potential to"
    - "Because photons are bosons, and all bosons have zero chemical potential at thermal equilibrium"
    - "Because photon number is not conserved — cavity walls freely emit and absorb photons, so there is no constraint on total photon number and thus no Lagrange multiplier for number"
    - "Because photons travel at the speed of light, making their chemical potential undefined in the non-relativistic limit"
  answer: 2
  explanation: "Chemical potential is the Lagrange multiplier that enforces conservation of particle number. For atoms or electrons, particle number is conserved, so μ ≠ 0 in general. But photons are freely created and destroyed by cavity walls at thermal equilibrium — there is no conservation law fixing the total photon count. With no number constraint, there is no Lagrange multiplier and μ = 0. This is the key physical distinction between a photon gas and an ordinary gas. Photons being massless or bosonic are true facts but not the reason for μ = 0."

- question: "The energy density of a photon gas scales as T⁴. If the temperature of a radiation cavity is doubled from T to 2T, by what factor does the total energy in the cavity increase?"
  type: multiple-choice
  options:
    - "2 — energy doubles when temperature doubles"
    - "4 — energy scales as T² for ultrarelativistic particles"
    - "8 — energy scales as T³ for bosons"
    - "16 — energy density scales as T⁴, so total energy (density × fixed volume) scales as T⁴ = 2⁴ = 16"
  answer: 3
  explanation: "U/V ∝ T⁴, so total energy U = (U/V)·V ∝ T⁴ at fixed volume. Doubling T multiplies energy by 2⁴ = 16. This is the Stefan-Boltzmann T⁴ dependence at work. The T⁴ scaling traces back to μ = 0 and the massless (linear) dispersion ω = ck of photons: with no energy scale other than k_BT, dimensional analysis forces U/V ∝ (k_BT)⁴/(ℏc)³. This dramatic T-dependence is why radiation pressure dominates in stellar interiors and the early universe at high temperatures."

- question: "A photon gas in thermal equilibrium obeys the same equation of state as an ordinary ideal gas: P = nkT."
  type: true-false
  answer: false
  explanation: "The photon gas obeys P = U/(3V) = u/3, where u is energy density — the equation of state of an ultrarelativistic gas. This is fundamentally different from an ordinary ideal gas (P = nkT = (2/3) × kinetic energy density). The factor of 1/3 rather than 2/3 arises because photons travel at c: for ultrarelativistic particles, momentum = energy/c, whereas for non-relativistic particles, momentum = mv with KE = ½mv². Radiation pressure scales as T⁴, not T, making it negligible at ordinary temperatures but dominant in extreme astrophysical environments."

- question: "In a photon gas, the chemical potential μ = 0 because photons carry no electric charge and therefore have no electrochemical interactions."
  type: true-false
  answer: false
  explanation: "Chemical potential has nothing to do with electric charge — it is the thermodynamic variable conjugate to particle number. μ = 0 for the photon gas because photon number is not conserved: a cavity wall can absorb or emit photons freely, so the total photon count fluctuates without constraint. Electric charge conservation would affect the chemical potential of charged particles (electrons, ions) but has no direct bearing on photons, which are electrically neutral by a completely separate fact."

- question: "Why does μ = 0 for a photon gas, and what physical fact about photons makes this true? Why is this different from an ordinary gas of atoms?"
  type: short-answer
  answer: "Chemical potential is the thermodynamic cost of adding one particle to a system — equivalently, the Lagrange multiplier enforcing conservation of particle number. For atoms, particle number is strictly conserved, so μ ≠ 0 and encodes the free energy change per particle added. For photons in a thermal cavity, cavity walls continuously absorb and re-emit photons at a rate that equilibrates the distribution — the photon number is not fixed by any conservation law. With no number constraint, there is no Lagrange multiplier and μ = 0. This has profound consequences: the Planck distribution n̄ = 1/(e^{ℏω/kT} − 1) follows from μ = 0 in the Bose-Einstein formula, and all T⁴ thermodynamic results follow from this single fact."
  explanation: "The μ = 0 condition is not an approximation or a special case — it is exact and fundamental to photon thermodynamics. It is why the grand partition function factors cleanly into independent mode contributions, why the Stefan-Boltzmann law takes its T⁴ form, and why radiation is fully described by temperature alone (no separate chemical potential needed). The contrast with ordinary gases is sharp: for atoms, specifying temperature T and chemical potential μ (or equivalently, number density n) is needed to determine the state; for the photon gas, T alone suffices."
```

## Explainer

You already know the Planck distribution for blackbody radiation: the mean number of photons in a mode of frequency ω is n̄ = 1/(e^{ℏω/k_BT} − 1). This is the Bose-Einstein distribution with **chemical potential μ = 0**. The reason μ = 0 is that photons are not conserved — a cavity wall can absorb or emit photons freely, so there is no constraint fixing the total photon number, and the Lagrange multiplier that enforces a number constraint (the chemical potential) is therefore zero. This is the key distinction from a gas of atoms: atoms have a conserved number and nonzero μ; photons in thermal equilibrium do not.

To get thermodynamic quantities, sum the energy over all modes. Each mode has two polarization states, wavevector k = ω/c, and energy ℏω per photon. The energy density is an integral over the Planck distribution weighted by the density of modes. This integral evaluates to U/V = (π²k_B⁴T⁴)/(15ℏ³c³), proportional to T⁴. The heat capacity is C_V = dU/dT ∝ T³, and the entropy S ∝ T³ as well. These power laws all trace back to a single feature: photons are massless bosons with a linear dispersion ω = ck and μ = 0, so the only energy scale is k_BT.

The **Stefan-Boltzmann law** for the power radiated per unit area by a blackbody, P/A = σT⁴ with σ = (π²k_B⁴)/(60ℏ³c²), emerges directly from U ∝ T⁴V. The radiation pressure P_rad = U/(3V) is a consequence of the photon gas having the same equation of state as any ultrarelativistic gas: P = u/3 where u is energy density. For ordinary gases you learned P = (2/3)(kinetic energy density), but photons travel at c and the factor becomes 1/3 instead. This radiation pressure is negligible on Earth but dominant in the interior of massive stars (where T ~ 10⁷ K) and was the dominant pressure in the early universe when temperatures exceeded 10⁹ K.

The connection to your partition function work is immediate: the photon gas grand canonical partition function factors into independent mode contributions because μ = 0 eliminates the coupling between modes imposed by total-number conservation. Each mode is a simple quantum harmonic oscillator, and the grand potential is Ω = −k_BT Σ_k ln(1 − e^{−ℏω_k/k_BT}). Converting the sum to an integral and evaluating gives all the T⁴ results above. The photon gas is thus one of the cleanest examples of a fully quantum statistical mechanical system — solvable exactly, physically transparent, and experimentally verified to high precision via measurements of the cosmic microwave background.

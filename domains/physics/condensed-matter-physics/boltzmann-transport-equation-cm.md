---
id: boltzmann-transport-equation-cm
title: Boltzmann Transport Equation
domain: physics
course: condensed-matter-physics
prerequisites:
- id: drude-sommerfeld-models
  type: hard
- id: boltzmann-transport-equation
  type: soft
tags:
- boltzmann-transport
- conductivity
- scattering
- relaxation-time
stage: expert
status: validated
---

# Boltzmann Transport Equation

## Core Idea
The Boltzmann transport equation (BTE) governs the distribution function f(r, k, t) of electrons in a solid subject to external fields and scattering. In steady state, the balance between the driving term (electric and magnetic fields changing k, temperature gradients changing the local equilibrium) and the collision integral (scattering returning the distribution toward equilibrium) determines transport coefficients: electrical conductivity, thermal conductivity, thermoelectric power, and magnetoresistance. The relaxation-time approximation replaces the full collision integral with -(f - f_0)/tau, making the BTE analytically solvable and recovering the Drude formula as a special case.

## Questions

```yaml
- question: "The Boltzmann transport equation in the relaxation-time approximation gives σ = e²τ ∫ v_k v_k (-∂f₀/∂E) g(E) dE. Why does the derivative -∂f₀/∂E appear, rather than f₀ itself?"
  type: multiple-choice
  options:
    - "It's a mathematical convenience with no physical significance"
    - "Only electrons near the Fermi surface contribute to transport — the factor -∂f₀/∂E is sharply peaked at E_F (width ~k_BT), selecting precisely these electrons from the integral"
    - "The derivative accounts for the change in electron mass near the Fermi level"
    - "It corrects for the spin degeneracy of electrons"
  answer: 1
  explanation: "At low temperature, f₀ is nearly a step function and -∂f₀/∂E approximates a delta function at E_F. This mathematically enforces the physical principle that only electrons near E_F carry current: deep electrons are frozen by Pauli exclusion (no empty states to scatter into) and high-energy states are empty. The width of the peak is ~k_BT, giving the thermal broadening of transport. This factor appears universally in transport integrals — conductivity, thermopower, Hall effect, thermal conductivity — and is why g(E_F) and v_F dominate metallic properties."

- question: "The Boltzmann transport equation treats electrons as semiclassical particles with well-defined position and momentum. Under what conditions does this semiclassical approach fail?"
  type: multiple-choice
  options:
    - "It always fails because electrons are quantum mechanical"
    - "When the mean free path becomes comparable to the Fermi wavelength (λ_F ~ 1/k_F), or when quantum coherence effects (weak localization, Anderson localization, quantum oscillations) become important — typically at low temperatures and in disordered or low-dimensional systems"
    - "It only fails in insulators"
    - "It fails whenever magnetic fields are present"
  answer: 1
  explanation: "The BTE requires that electrons behave as well-defined wavepackets that scatter incoherently — each scattering event randomizes the phase. This breaks down when: (1) the mean free path ℓ ≈ λ_F, so the electron cannot be localized to a wavepacket (Anderson localization regime); (2) quantum interference between scattering paths is important (weak localization, universal conductance fluctuations); (3) magnetic fields quantize the orbits (Landau levels, quantum Hall effect). In these regimes, the full quantum mechanical (Kubo formula) treatment is needed."

- question: "Why does the Boltzmann equation predict that the thermoelectric power (Seebeck coefficient) of a simple metal is much smaller than that of a semiconductor?"
  type: short-answer
  answer: "The Seebeck coefficient S is proportional to the energy derivative of the conductivity at E_F: S ∝ (1/σ)(dσ/dE)|_{E_F}, which measures the asymmetry of transport above and below E_F. In a metal, the density of states and scattering rate vary slowly near E_F (they are smooth functions of energy), so this derivative is small — typically S ~ k_BT/E_F ~ μV/K. In a semiconductor, the carrier concentration changes exponentially with energy near the band edges, creating a huge energy asymmetry and Seebeck coefficients of ~mV/K, orders of magnitude larger. This is why thermoelectric devices use semiconductors, not metals."
  explanation: "The Mott formula for the thermopower, S = -(π²k_B²T/3e)(d ln σ(E)/dE)|_{E_F}, makes this explicit. For a free-electron metal, d ln σ/dE ~ 1/E_F, giving S of order μV/K. The Boltzmann framework naturally captures both limits."
```

## Explainer

The Drude and Sommerfeld models provide the qualitative picture of metallic transport, but to calculate transport coefficients quantitatively — especially when scattering rates depend on energy, when temperature gradients or magnetic fields are present, or when the Fermi surface is anisotropic — you need the **Boltzmann transport equation**. The BTE tracks the non-equilibrium distribution function f(r, k, t), which gives the probability of finding an electron at position r with crystal momentum k at time t. In equilibrium, f = f_0 (the Fermi-Dirac distribution). External perturbations drive f away from f_0, and scattering processes push it back.

The BTE in its general form is df/dt + v_k · nabla_r f + (F/hbar) · nabla_k f = I_coll{f}, where v_k = (1/hbar) nabla_k E(k) is the group velocity, F is the external force (electric and magnetic), and I_coll is the collision integral encoding all scattering mechanisms. The **relaxation-time approximation** simplifies I_coll to -(f - f_0)/tau, asserting that scattering restores equilibrium exponentially with time constant tau. This approximation, while crude, captures the essential physics of most transport phenomena and is analytically tractable.

For electrical conductivity in the relaxation-time approximation, the BTE yields sigma = e^2 integral tau(k) v_k v_k (-df_0/dE) [d^3k/(2pi)^3]. The crucial factor -df_0/dE is a sharply peaked function at E_F (width ~k_BT at low temperature), enforcing that only Fermi-surface electrons contribute. For an isotropic metal this reduces to sigma = (1/3) e^2 v_F^2 tau g(E_F), recovering the Drude formula with the correct Sommerfeld modifications. For anisotropic Fermi surfaces, the tensor character of the conductivity emerges naturally from the k-dependent velocity and scattering rate.

The BTE framework extends to all transport phenomena: **thermal conductivity** (response to a temperature gradient), **thermoelectric effects** (coupling between heat and charge currents, giving the Seebeck and Peltier coefficients), and **magnetotransport** (Hall effect, magnetoresistance, de Haas-van Alphen oscillations in the semiclassical regime). The Mott formula for thermopower, the Wiedemann-Franz law, and the Kohler rule for magnetoresistance all emerge as special cases. The BTE remains the workhorse of transport theory in condensed matter, succeeded by the Kubo formula only when quantum coherence effects become important.

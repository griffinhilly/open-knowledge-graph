---
id: legendre-transformations-thermodynamics
title: Legendre Transformations and Thermodynamic Potentials
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: thermodynamic-systems-engineering
  type: hard
- id: first-law-closed-systems
  type: hard
builds-toward:
- helmholtz-gibbs-free-energy
- maxwell-relations-thermodynamics
tags:
- legendre
- transformation
- potential
- natural-variables
- conjugate
stage: advanced
status: draft
---

# Legendre Transformations and Thermodynamic Potentials

## Core Idea
Legendre transformations convert extensive state functions between different sets of natural variables. Internal energy U(S,V) transforms to enthalpy H(S,P), Helmholtz free energy A(T,V), and Gibbs free energy G(T,P). Each potential is useful for different constraints: U for isolated systems, H for constant-pressure processes, G for systems at fixed T and P in contact with surroundings.

## Questions

```yaml
- question: "A chemist studying a reaction at constant temperature and pressure wants a single criterion to determine whether the reaction is spontaneous. Which thermodynamic potential should she use, and why?"
  type: multiple-choice
  options:
    - "Internal energy U, because it accounts for all energy stored in the system and drives all physical processes"
    - "Gibbs free energy G, because its natural variables are T and P — the conditions held constant — so dG directly indicates whether the process is spontaneous at those conditions"
    - "Helmholtz free energy A, because it measures the maximum work available at constant temperature"
    - "Enthalpy H, because constant-pressure conditions make H the most relevant energy measure"
  answer: 1
  explanation: "The Legendre transformation framework reveals that each potential is 'natural' for specific constraints — meaning its differential is expressed purely in terms of the variables being held constant. G(T,P) has dG = −S dT + V dP, so at constant T and P, dG = 0 at equilibrium and dG < 0 for spontaneous processes. Using U at constant T and P would be inconvenient: U(S,V) is natural in S and V, and at constant T and P you would need to track entropy changes and volume changes separately. The choice of potential is not arbitrary — it is determined by the experimental constraints."

- question: "The Legendre transformation converting U(S,V) to H(S,P) involves which mathematical operation, and what is the logic?"
  type: multiple-choice
  options:
    - "H = U − PV; the negative sign reflects that expansion at constant pressure does negative work on the system"
    - "H = U + PV; this swaps the natural variable V for P by subtracting the product of the conjugate pair (−P) and V, so dH is naturally expressed in S and P"
    - "H = U/PV; dividing by the PV product normalizes energy per unit of pressure-volume work"
    - "H = U − TS; this removes entropy dependence to give a temperature-independent potential"
  answer: 1
  explanation: "The Legendre transformation recipe to swap a natural variable x for its conjugate y (where y = ∂U/∂x) is: new function = old function − y·x. Here we want to swap V for its conjugate −P (since (∂U/∂V)_S = −P). The transformation gives H = U − (−P)·V = U + PV. Then dH = dU + PdV + VdP = T dS − P dV + P dV + V dP = T dS + V dP, which is naturally expressed in S and P. The key insight is that the '+PV' term is not chosen arbitrarily — it is forced by the requirement that the new differential contain only dS and dP."

- question: "Helmholtz free energy A, Gibbs free energy G, and enthalpy H are simply renamed versions of internal energy U, and they contain no thermodynamic information beyond what U already encodes."
  type: true-false
  answer: false
  explanation: "Each potential contains *all* the same thermodynamic information as U — they are mathematically equivalent descriptions of the same system. What differs is the natural variable set in which each is expressed. G(T,P) makes temperature and pressure derivatives immediately accessible; U(S,V) does not. This matters practically because differentiation of G directly yields entropy (−∂G/∂T)_P = S and volume (∂G/∂P)_T = V, while working with U at constant T and P requires awkward substitutions. The Legendre framework is not renaming but reorganizing — each potential is a different 'view' of the same information, optimized for different experimental conditions."

- question: "Maxwell relations — which connect entropy changes to measurable PVT properties — arise because each thermodynamic potential is an exact differential, requiring its mixed second partial derivatives to be equal."
  type: true-false
  answer: true
  explanation: "An exact differential dZ = M dx + N dy requires (∂M/∂y) = (∂N/∂x) (Schwarz's theorem on equality of mixed partials). For dG = −S dT + V dP, this gives (∂(−S)/∂P)_T = (∂V/∂T)_P, or (∂S/∂P)_T = −(∂V/∂T)_P. The left side involves entropy change with pressure — not directly measurable — while the right side involves thermal expansion — directly measurable from PVT data. Each of the four Legendre potentials generates one Maxwell relation, providing a network of cross-relations that allow engineers and scientists to determine thermodynamic quantities (entropy, free energy) from quantities they can actually measure in the lab."

- question: "Why does the choice of thermodynamic potential matter in practice? Explain why a chemist working at constant T and P should use Gibbs free energy rather than internal energy, even though both encode the same thermodynamic information."
  type: short-answer
  answer: "The thermodynamic potentials encode the same information but organize it differently — each is expressed in terms of its own set of natural variables, and those variables are the ones held constant in specific experimental conditions. Internal energy U(S,V) is most useful when entropy and volume are the controlled variables (isolated adiabatic systems). But chemical reactions in open labs happen at constant temperature (set by a thermostat) and constant pressure (atmospheric), not constant entropy and volume. For a constant-T, constant-P process, dG = −S dT + V dP = 0, so G is stationary at equilibrium and decreasing for spontaneous processes. Working with U at constant T and P would require tracking entropy and volume changes separately and connecting them through additional equations of state — much more work for the same result. Gibbs free energy does the bookkeeping automatically because T and P are already its natural variables."
  explanation: "Practically, the Legendre transformation framework means chemists can calculate whether a reaction is spontaneous using ΔG = ΔH − TΔS, where ΔH and ΔS can be measured calorimetrically and with heat capacity data. They do not need to track entropy of the system separately from work done against atmospheric pressure — G absorbs both corrections."
```

## Explainer

From the first law and the definition of entropy, the **fundamental relation** for a closed system is dU = T dS − P dV. This compact equation says that internal energy U is naturally a function of S and V: if you know how U depends on S and V, you can recover all thermodynamic information by differentiation — (∂U/∂S)_V = T and (∂U/∂V)_S = −P. The pair (S, T) and the pair (V, −P) are **conjugate variables**: each intensive variable (T, P) is the derivative of U with respect to its conjugate extensive variable (S, V).

The problem is experimental: entropy S is not directly measurable, and controlling S (adiabatic conditions) is often impractical. Most engineering processes happen at constant pressure (open systems exchanging heat with atmosphere) or constant temperature and pressure (chemical reactions in a lab). The Legendre transformation is the mathematical surgery that swaps a natural variable for its conjugate partner, producing a new function with more convenient natural variables. The recipe for swapping (V, −P) for (P, −V) is: define H = U − (−P)·V = U + PV. The differential is dH = dU + P dV + V dP = T dS + V dP. Now H is naturally a function of S and P — exactly the variables controlled in constant-pressure processes. Enthalpy H is not new to you; what the Legendre construction reveals is *why* H is the right function for constant-pressure problems.

Applying the same logic to swap (S, T) instead gives the **Helmholtz free energy** A = U − TS, with dA = −S dT − P dV. Helmholtz free energy is natural in (T, V): it is the relevant potential for constant-temperature, constant-volume processes (e.g., isothermal compression in a rigid container). Swapping both conjugate pairs at once gives **Gibbs free energy** G = U + PV − TS = H − TS, with dG = −S dT + V dP. Gibbs free energy is natural in (T, P) — the conditions of most chemical reactions and phase transitions. At constant T and P, the equilibrium state minimizes G, which is why ΔG < 0 is the criterion for spontaneity in chemistry.

The deeper payoff of this framework is the **Maxwell relations**: because each potential is an exact differential, its mixed second partial derivatives must be equal. From dG = −S dT + V dP, we get (∂S/∂P)_T = −(∂V/∂T)_P — relating entropy change with pressure to volume change with temperature, quantities that are actually measurable. The Legendre transformation thus turns a set of abstract thermodynamic potentials into a network of cross-relations among measurable properties, which is how engineers and scientists extract entropy and free energy data from equations of state and PVT measurements.

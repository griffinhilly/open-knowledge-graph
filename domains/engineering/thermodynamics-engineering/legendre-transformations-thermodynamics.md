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

## Explainer

From the first law and the definition of entropy, the **fundamental relation** for a closed system is dU = T dS − P dV. This compact equation says that internal energy U is naturally a function of S and V: if you know how U depends on S and V, you can recover all thermodynamic information by differentiation — (∂U/∂S)_V = T and (∂U/∂V)_S = −P. The pair (S, T) and the pair (V, −P) are **conjugate variables**: each intensive variable (T, P) is the derivative of U with respect to its conjugate extensive variable (S, V).

The problem is experimental: entropy S is not directly measurable, and controlling S (adiabatic conditions) is often impractical. Most engineering processes happen at constant pressure (open systems exchanging heat with atmosphere) or constant temperature and pressure (chemical reactions in a lab). The Legendre transformation is the mathematical surgery that swaps a natural variable for its conjugate partner, producing a new function with more convenient natural variables. The recipe for swapping (V, −P) for (P, −V) is: define H = U − (−P)·V = U + PV. The differential is dH = dU + P dV + V dP = T dS + V dP. Now H is naturally a function of S and P — exactly the variables controlled in constant-pressure processes. Enthalpy H is not new to you; what the Legendre construction reveals is *why* H is the right function for constant-pressure problems.

Applying the same logic to swap (S, T) instead gives the **Helmholtz free energy** A = U − TS, with dA = −S dT − P dV. Helmholtz free energy is natural in (T, V): it is the relevant potential for constant-temperature, constant-volume processes (e.g., isothermal compression in a rigid container). Swapping both conjugate pairs at once gives **Gibbs free energy** G = U + PV − TS = H − TS, with dG = −S dT + V dP. Gibbs free energy is natural in (T, P) — the conditions of most chemical reactions and phase transitions. At constant T and P, the equilibrium state minimizes G, which is why ΔG < 0 is the criterion for spontaneity in chemistry.

The deeper payoff of this framework is the **Maxwell relations**: because each potential is an exact differential, its mixed second partial derivatives must be equal. From dG = −S dT + V dP, we get (∂S/∂P)_T = −(∂V/∂T)_P — relating entropy change with pressure to volume change with temperature, quantities that are actually measurable. The Legendre transformation thus turns a set of abstract thermodynamic potentials into a network of cross-relations among measurable properties, which is how engineers and scientists extract entropy and free energy data from equations of state and PVT measurements.

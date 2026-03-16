---
id: thermodynamic-property-relations-maxwell
title: Maxwell Relations and Thermodynamic Property Derivations
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: second-law-thermodynamics-entropy
  type: hard
- id: differential-equations
  type: hard
tags:
- maxwell-relations
- property-relations
- thermodynamic-identities
stage: advanced
status: draft
---

# Maxwell Relations and Thermodynamic Property Derivations

## Core Idea
Maxwell relations are derived from the equality of mixed partial derivatives of thermodynamic potentials (U, H, F, G), linking different properties without direct measurement. For example, (∂S/∂V)_T = (∂P/∂T)_V enables calculation of entropy from P-T-V data. These relations form the theoretical foundation for property tables and reduced-variable equations of state used throughout engineering.

## Explainer

Your prerequisite on the second law established the fundamental thermodynamic relation: dU = TdS − PdV. This tells you that internal energy U is a natural function of entropy S and volume V, with the partial derivatives (∂U/∂S)_V = T and (∂U/∂V)_S = −P. Your calculus prerequisite on differential equations established the **Schwarz (Clairaut) symmetry condition**: for any function f(x, y) with continuous second partial derivatives, ∂²f/∂x∂y = ∂²f/∂y∂x. Thermodynamic potentials are exact differentials, so this symmetry must hold. The **Maxwell relations** are what you get when you apply this symmetry to each of the four thermodynamic potentials.

Starting with U(S, V): the symmetry of mixed partials gives (∂T/∂V)_S = −(∂P/∂S)_V. For the **enthalpy** H = U + PV, the differential is dH = TdS + VdP, so H is natural in (S, P), and the relation is (∂T/∂P)_S = (∂V/∂S)_P. For the **Helmholtz free energy** A = U − TS, the differential is dA = −SdT − PdV, natural in (T, V), giving (∂S/∂V)_T = (∂P/∂T)_V. For the **Gibbs free energy** G = U + PV − TS, the differential is dG = −SdT + VdP, natural in (T, P), giving (∂S/∂P)_T = −(∂V/∂T)_P. These four are the Maxwell relations.

The practical importance is that **entropy is not directly measurable**, but pressure, volume, and temperature are. The Helmholtz relation (∂S/∂V)_T = (∂P/∂T)_V allows you to compute entropy changes from PVT data: measuring how pressure changes with temperature at constant volume gives you how entropy changes with volume at constant temperature. For an ideal gas, (∂P/∂T)_V = nR/V, so (∂S/∂V)_T = nR/V — consistent with what you know. For a real gas described by a van der Waals or Peng-Robinson equation of state, the same procedure yields entropy corrections to the ideal-gas value. This is how steam tables and refrigerant tables are constructed: experimental PVT data and specific heat measurements feed into Maxwell relations and other thermodynamic identities to derive the tabulated entropy, enthalpy, and internal energy values.

More broadly, Maxwell relations are instances of a pattern: whenever you have an exact differential dZ = M dx + N dy, the relation (∂M/∂y)_x = (∂N/∂x)_y holds. This pattern appears throughout thermodynamics — in Gibbs-Duhem relations, in the Clausius-Clapeyron equation, in chemical potential relations — making the mathematical technique as important as any specific relation. Recognizing that a thermodynamic identity follows from the symmetry of mixed partials is a key skill for deriving unfamiliar relations from first principles.

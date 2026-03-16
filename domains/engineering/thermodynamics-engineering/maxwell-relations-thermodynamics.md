---
id: maxwell-relations-thermodynamics
title: Maxwell Relations and Thermodynamic Consistency
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: legendre-transformations-thermodynamics
  type: hard
- id: thermodynamic-property-relations-maxwell
  type: soft
tags:
- maxwell-relations
- partial-derivatives
- consistency
- cross-derivatives
stage: advanced
status: draft
---

# Maxwell Relations and Thermodynamic Consistency

## Core Idea
Maxwell relations arise from the exactness of thermodynamic potentials; cross-partial derivatives are equal. Examples: (∂T/∂V)_S = -(∂P/∂S)_V and (∂S/∂P)_T = -(∂V/∂T)_P. These relations enable determination of unmeasurable properties (entropy changes) from measurable ones (P, V, T, C_p). They provide consistency checks for equation-of-state data and property correlations.

## Explainer

From your work with Legendre transformations, you know that the four thermodynamic potentials — internal energy U, enthalpy H, Helmholtz free energy A, and Gibbs free energy G — are related by swapping natural variables among S, T, P, and V. Each potential has an exact differential. For example, dU = T dS − P dV tells you that T = (∂U/∂S)_V and −P = (∂U/∂V)_S. These are just definitions of the partial derivatives of U.

Now apply **Schwarz's theorem** (equality of mixed partial derivatives): for any smooth function Z with exact differential dZ = M dx + N dy, we must have ∂M/∂y = ∂N/∂x. Applied to dU = T dS − P dV, we set M = T (coefficient of dS) and N = −P (coefficient of dV), then equate their cross-partials: (∂T/∂V)_S = (∂(−P)/∂S)_V = −(∂P/∂S)_V. This is one **Maxwell relation**. Applying the same logic to dH, dA, and dG yields the other three. There are exactly four, one per thermodynamic potential, each arising automatically from the exactness of an exact differential.

The engineering value is immediate: Maxwell relations translate entropy derivatives — which cannot be measured directly — into P, V, T derivatives, which can be measured or read from tables. The relation (∂S/∂P)_T = −(∂V/∂T)_P is especially useful. The left side involves how entropy changes with pressure at constant temperature, which is not directly measurable. The right side is the negative of the isobaric thermal expansion coefficient — a quantity that can be determined from volumetric measurements or equation-of-state data. This is how engineers build complete thermodynamic property tables: start from P-V-T measurements, use Maxwell relations to derive entropy and enthalpy changes, and integrate to construct tabulated properties.

Beyond calculation, Maxwell relations serve as **thermodynamic consistency checks**. If two independent experimental datasets — say, calorimetric Cₚ measurements and volumetric V(T,P) data — are combined into a property correlation, the Maxwell relations must be satisfied for the correlation to be physically self-consistent. Violations signal measurement error, ill-fitting equations of state, or incorrect correlation forms. This is why all serious thermodynamic property software tests its correlations against Maxwell consistency before deploying them for engineering calculations.

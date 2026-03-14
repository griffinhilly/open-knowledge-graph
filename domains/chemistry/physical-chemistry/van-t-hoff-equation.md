---
id: van-t-hoff-equation
title: "The van't Hoff Equation: Temperature Dependence of Equilibrium"
domain: chemistry
course: physical-chemistry
prerequisites:
- id: statistical-thermodynamics-applications
  type: hard
builds-toward: []
tags:
- van-t-Hoff
- equilibrium-constant
- temperature-dependence
- Le-Chatelier
- enthalpy-of-reaction
- thermodynamic-equilibrium
stage: advanced
status: draft
---

# The van't Hoff Equation: Temperature Dependence of Equilibrium

## Core Idea
The van't Hoff equation d(ln K)/dT = Delta_H_std/(R*T^2) quantifies how the equilibrium constant K changes with temperature, providing the quantitative foundation for Le Chatelier's principle. For an endothermic reaction (Delta_H > 0), K increases with temperature; for exothermic (Delta_H < 0), K decreases. The integrated form ln(K2/K1) = -(Delta_H/R)(1/T2 - 1/T1) assumes Delta_H is approximately constant over the temperature range and enables prediction of K at any temperature from a single measured value. A van't Hoff plot of ln K vs 1/T yields a straight line with slope -Delta_H/R when enthalpy is temperature-independent; curvature indicates significant Delta_Cp, requiring the Kirchhoff equation correction. This relationship connects macroscopic equilibrium measurements directly to molecular-level energetics.

## How It's Best Learned
Collect or look up equilibrium constant data for a reaction at multiple temperatures (e.g., the dissociation of N2O4 or the solubility of a sparingly soluble salt). Construct the van't Hoff plot, extract Delta_H from the slope, and verify consistency with calorimetric measurements.

## Common Misconceptions
- Assuming Delta_H is always temperature-independent; for reactions with large Delta_Cp (heat capacity changes), the van't Hoff plot curves and the simple two-point integrated form becomes inaccurate.
- Confusing the van't Hoff equation with the Arrhenius equation; the former relates K (equilibrium) to temperature while the latter relates k (rate constant) to temperature -- they have similar mathematical forms but describe fundamentally different quantities.

---
id: electrochemistry-nernst-equation
title: Electrochemistry and the Nernst Equation
domain: chemistry
course: physical-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: thermochemistry-enthalpy
  type: soft
tags:
- electrochemistry
- nernst
- potential
- cell
stage: advanced
status: draft
---

# Electrochemistry and the Nernst Equation

## Core Idea
The Nernst equation E = E° - (RT/nF) ln(Q) relates electrochemical cell potential to the reaction quotient Q, showing how electrode potential varies with concentration. Standard cell potentials (E°) are linked to Gibbs free energy through ΔG° = -nFE°, connecting electrochemistry to thermodynamics. At equilibrium (E = 0), the equation determines the equilibrium constant. The Nernst equation explains how battery voltage drops under load and how pH affects redox potentials.

## Explainer

From electrochemistry basics, you know that a galvanic cell generates voltage by separating oxidation and reduction into two half-cells, and that standard reduction potentials (E°) measured under standard conditions (1 M, 1 atm, 25°C) let you predict which direction electrons flow. But real cells rarely operate at standard conditions — concentrations change as the cell discharges, temperatures vary, and pH shifts. The **Nernst equation** tells you the actual cell potential under any set of conditions.

The equation is E = E° − (RT/nF) ln Q, where R is the gas constant, T is absolute temperature, n is the number of electrons transferred, F is Faraday's constant (96,485 C/mol), and Q is the **reaction quotient** — the same ratio of product to reactant activities you use in equilibrium thermodynamics. At 25°C, the prefactor RT/F simplifies to 0.02569 V, giving the common form E = E° − (0.02569/n) ln Q, or equivalently E = E° − (0.05916/n) log Q when using base-10 logarithms. The equation says that as products accumulate (Q increases), the driving force for the reaction decreases and the cell potential drops — exactly what you observe as a battery discharges.

The deep connection here is thermodynamic: the Nernst equation is really just **ΔG = ΔG° + RT ln Q** rewritten in electrical terms, using the relationship ΔG = −nFE. At standard conditions (Q = 1), E equals E° and ΔG equals ΔG°. At equilibrium (Q = K), E = 0 and ΔG = 0, which gives the powerful result E° = (RT/nF) ln K — the standard cell potential directly determines the equilibrium constant. A cell with E° = +0.50 V and n = 2 has K ≈ 10¹⁷, meaning the reaction overwhelmingly favors products. This bridges the gap between the voltage you measure with a multimeter and the thermodynamic favorability of the underlying chemistry.

A particularly important application is pH-dependent electrochemistry. Many half-reactions involve H⁺ ions, so their potentials shift with pH. The hydrogen electrode potential, for instance, changes by −0.05916 V per unit increase in pH at 25°C. This is the basis of pH meters — they are simply electrochemical cells whose voltage varies linearly with hydrogen ion concentration. The Nernst equation also explains concentration cells, where two identical electrodes dipped in solutions of different concentration generate a voltage purely from the concentration difference, with no net chemical change at standard conditions.

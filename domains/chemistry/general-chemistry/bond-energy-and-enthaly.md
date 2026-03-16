---
id: bond-energy-and-enthaly
title: Bond Energy and Enthalpy Change
domain: chemistry
course: general-chemistry
prerequisites:
- id: covalent-bonding
  type: hard
- id: thermochemistry-enthalpy
  type: hard
builds-toward:
- hess-law-of-enthalpy
- reaction-coordinate-diagrams
tags:
- bond energy
- bond breaking
- bond formation
stage: formal-systems
status: draft
---

# Bond Energy and Enthalpy Change

## Core Idea
Bond energy is the energy required to break a bond. ΔH for a reaction equals energy required to break bonds minus energy released when forming new bonds.

## How It's Best Learned
Use bond energy tables to calculate ΔH; compare with other methods like Hess's Law.

## Explainer

You already know that covalent bonds form when atoms share electrons, and from thermochemistry you know that enthalpy change (ΔH) measures the heat absorbed or released during a reaction at constant pressure. Bond energy connects these two ideas: it tells you exactly how much energy is stored in each bond, which lets you estimate ΔH for any reaction directly from its structural formula.

**Bond energy** (also called bond dissociation energy) is the energy required to break one mole of a particular bond in the gas phase, producing separated atoms. For example, breaking one mole of H–H bonds requires 436 kJ — that's the bond energy of H–H. Breaking bonds always requires energy input (endothermic), while forming bonds always releases energy (exothermic). This is the fundamental bookkeeping principle: a chemical reaction is essentially a process of breaking old bonds and forming new ones, and ΔH is the net energy balance.

The calculation follows a simple formula: **ΔH ≈ Σ(bond energies broken) − Σ(bond energies formed)**. Consider the combustion of methane: CH₄ + 2O₂ → CO₂ + 2H₂O. You break four C–H bonds and two O=O bonds (energy input), then form two C=O bonds and four O–H bonds (energy output). Plugging in table values: breaking costs 4(413) + 2(498) = 2648 kJ; forming releases 2(799) + 4(463) = 3450 kJ. The difference is 2648 − 3450 = −802 kJ/mol — negative because more energy is released forming bonds than consumed breaking them, confirming that combustion is exothermic, which matches your everyday experience of fire producing heat.

One important caveat: bond energies are averages across many different molecules. The C–H bond energy of 413 kJ/mol is an average — the actual C–H bond strength in methane differs slightly from that in ethanol or chloroform because the surrounding atoms influence electron distribution. This means bond energy calculations give estimates of ΔH, not exact values. For precise thermodynamic calculations, you would use Hess's Law with standard enthalpies of formation. But bond energies are powerful for quick predictions and for building intuition about why some reactions are energetically favorable: reactions tend to be exothermic when they form stronger bonds than they break.

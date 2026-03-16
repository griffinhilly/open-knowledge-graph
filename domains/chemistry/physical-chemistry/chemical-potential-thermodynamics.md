---
id: chemical-potential-thermodynamics
title: Chemical Potential and Thermodynamic Equilibrium
domain: chemistry
course: physical-chemistry
prerequisites:
- id: gibbs-free-energy-spontaneity
  type: hard
- id: phase-diagrams-clausius-clapeyron
  type: soft
tags:
- chemical-potential
- equilibrium
- thermodynamics
- phase-equilibrium
stage: advanced
status: draft
---

# Chemical Potential and Thermodynamic Equilibrium

## Core Idea
Chemical potential μᵢ represents the partial molar free energy of component i and determines the direction and extent of chemical reactions and phase changes. At equilibrium, chemical potentials of a substance in different phases are equal. Chemical potentials also explain colligative properties, osmotic pressure, and ion distribution in ionic solutions. The fundamental thermodynamic equilibrium condition is that the total chemical potential must be minimized.

## Explainer

You already know from Gibbs free energy that a process is spontaneous when ΔG < 0, and that equilibrium occurs at the minimum of G. Chemical potential extends this idea from pure substances to mixtures. In a pure system, the molar Gibbs energy tells you everything. But in a mixture — say, salt dissolved in water, or ethanol vapor above a liquid solution — you need to know how the total free energy changes when you add a tiny amount of one specific component while holding everything else constant. That quantity is the **chemical potential**, μᵢ = (∂G/∂nᵢ)_{T,P,nⱼ}. It answers the question: if I add one more mole of component i to this mixture, how much does the total free energy change?

The power of chemical potential lies in its role as the **driving force for all transfer processes**. Matter spontaneously flows from regions of high chemical potential to regions of low chemical potential — just as heat flows from high temperature to low temperature, or charge flows from high electrical potential to low electrical potential. When liquid water and water vapor coexist in a sealed container, equilibrium is reached when μ_water(liquid) = μ_water(vapor). If the chemical potential of water in the liquid phase were higher, molecules would spontaneously escape into the vapor phase until the potentials equalize. This single principle — equality of chemical potentials at equilibrium — unifies phase equilibria, chemical reaction equilibria, and membrane transport under one framework.

For an **ideal mixture**, the chemical potential of each component is μᵢ = μᵢ° + RT ln xᵢ, where μᵢ° is the chemical potential of the pure substance and xᵢ is its mole fraction. The RT ln xᵢ term is always negative (since xᵢ < 1 in a mixture), meaning that mixing always lowers the chemical potential of each component. This is why mixing is spontaneous for ideal solutions. It also explains **colligative properties**: adding a solute lowers the chemical potential of the solvent, which shifts phase boundaries. The solvent's vapor pressure drops (Raoult's law), its boiling point rises, and its freezing point falls — all because the solute reduced the solvent's chemical potential relative to the pure liquid.

Chemical potential also provides the bridge to **chemical reaction equilibrium**. The condition ΔG = 0 at equilibrium can be rewritten as Σνᵢμᵢ = 0, where νᵢ are stoichiometric coefficients (negative for reactants, positive for products). Substituting the ideal expression for each μᵢ recovers the familiar relationship ΔG° = −RT ln K. But the chemical potential formulation is more general: it applies to non-ideal solutions, to electrochemical cells (where electrical work modifies μ), and to biological systems where concentration gradients across membranes drive transport. Whenever you need to predict the direction of spontaneous change in a system with multiple components, chemical potential is the quantity to examine.

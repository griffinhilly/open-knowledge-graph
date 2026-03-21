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

## Questions

```yaml
- question: "A sealed container holds liquid water and water vapor in equilibrium at 25°C. The pressure is then slightly increased, compressing the vapor. In what direction will molecules spontaneously move, and why?"
  type: multiple-choice
  options:
    - "Vapor condenses into liquid, because compression raises the chemical potential of the vapor above that of the liquid"
    - "Liquid evaporates into vapor, because compression increases the energy of the liquid phase"
    - "No net transfer occurs, because the system was already at equilibrium and pressure does not affect chemical potential"
    - "Molecules transfer from liquid to vapor to restore the original pressure"
  answer: 0
  explanation: "Matter spontaneously flows from high chemical potential to low chemical potential — exactly as heat flows from hot to cold. Compressing the vapor raises its chemical potential above that of the liquid, so molecules condense until the potentials re-equalize. This is why the equilibrium condition is μ_liquid = μ_vapor, not equal numbers of molecules or equal pressures on each side. Option C is wrong because the perturbation broke the equality; the system must respond."

- question: "A student dissolves table salt in water and observes that the boiling point rises. Which explanation correctly uses chemical potential?"
  type: multiple-choice
  options:
    - "Salt raises the chemical potential of water vapor, making it harder for vapor to escape the liquid"
    - "Salt lowers the chemical potential of liquid water (via the RT ln x term), so a higher temperature is needed to make μ_liquid equal μ_vapor"
    - "Salt increases the kinetic energy of water molecules, so more heat is needed before they can escape"
    - "Salt forms hydrogen bonds with water that must be broken before boiling can occur"
  answer: 1
  explanation: "Dissolving a solute lowers the chemical potential of the solvent: μ_water(solution) = μ_water° + RT ln x_water, and since x_water < 1, the RT ln x term is negative. The liquid's chemical potential is now lower than the pure liquid's. For boiling to occur, the liquid and vapor chemical potentials must be equal — but the vapor hasn't changed, so you must heat the solution to raise the liquid's chemical potential until it matches the vapor's. That is why the boiling point rises. Options C and D describe incorrect physical mechanisms."

- question: "At thermodynamic equilibrium, the chemical potential of a substance is equal in all phases it occupies."
  type: true-false
  answer: true
  explanation: "This is the fundamental equilibrium condition. If chemical potential were higher in one phase, molecules would spontaneously transfer to the lower-potential phase — by definition, not equilibrium. The equality μ_liquid = μ_vapor = μ_solid (for coexisting phases) is the thermodynamic expression of phase equilibrium. It unifies ice melting, evaporation, osmotic equilibrium, and chemical reaction equilibrium under one principle: the system reaches its minimum total free energy when all chemical potentials are equalized."

- question: "Adding a non-volatile solute to a solvent raises the chemical potential of the solvent, which is why the solvent needs a higher temperature to boil."
  type: true-false
  answer: false
  explanation: "Dissolving a solute LOWERS the chemical potential of the solvent. In an ideal solution, μ_solvent = μ_solvent° + RT ln x_solvent. Since the mole fraction of solvent x_solvent < 1 in a solution, the logarithm is negative, reducing the chemical potential. This lowering is what causes all colligative properties: reduced vapor pressure, elevated boiling point, depressed freezing point, and osmotic pressure. The boiling point rises not because the solvent needs more energy, but because the lower chemical potential of the liquid means a higher temperature is needed for the liquid and vapor potentials to equalize."

- question: "Why does dissolving any solute in a solvent lower the solvent's vapor pressure, raise its boiling point, and depress its freezing point — all from the same underlying cause?"
  type: short-answer
  answer: "All three colligative properties arise because the solute lowers the chemical potential of the solvent. The mole fraction of the solvent is less than 1 in any solution, so μ_solvent = μ_solvent° + RT ln x_solvent is reduced below the pure solvent's value. Vapor pressure drops because equilibrium between liquid and vapor requires equal chemical potentials — the lower liquid μ is matched at a lower vapor pressure (Raoult's law). Boiling point rises because you must heat the solution to bring the liquid μ back up to meet the vapor's μ. Freezing point drops because the liquid's lower μ now falls below the solid's μ at the normal freezing point, so cooling is needed to bring the solid's μ down to match. The solute's specific identity doesn't matter — only how much it lowers x_solvent."
  explanation: "This is the power of the chemical potential framework: one equation (μᵢ = μᵢ° + RT ln xᵢ for ideal solutions) explains an entire class of phenomena without invoking different physical mechanisms for each. The chemical potential is the thermodynamic 'pressure' driving all spontaneous transfer, and its modification by concentration is the single upstream cause of all colligative effects."
```

## Explainer

You already know from Gibbs free energy that a process is spontaneous when ΔG < 0, and that equilibrium occurs at the minimum of G. Chemical potential extends this idea from pure substances to mixtures. In a pure system, the molar Gibbs energy tells you everything. But in a mixture — say, salt dissolved in water, or ethanol vapor above a liquid solution — you need to know how the total free energy changes when you add a tiny amount of one specific component while holding everything else constant. That quantity is the **chemical potential**, μᵢ = (∂G/∂nᵢ)_{T,P,nⱼ}. It answers the question: if I add one more mole of component i to this mixture, how much does the total free energy change?

The power of chemical potential lies in its role as the **driving force for all transfer processes**. Matter spontaneously flows from regions of high chemical potential to regions of low chemical potential — just as heat flows from high temperature to low temperature, or charge flows from high electrical potential to low electrical potential. When liquid water and water vapor coexist in a sealed container, equilibrium is reached when μ_water(liquid) = μ_water(vapor). If the chemical potential of water in the liquid phase were higher, molecules would spontaneously escape into the vapor phase until the potentials equalize. This single principle — equality of chemical potentials at equilibrium — unifies phase equilibria, chemical reaction equilibria, and membrane transport under one framework.

For an **ideal mixture**, the chemical potential of each component is μᵢ = μᵢ° + RT ln xᵢ, where μᵢ° is the chemical potential of the pure substance and xᵢ is its mole fraction. The RT ln xᵢ term is always negative (since xᵢ < 1 in a mixture), meaning that mixing always lowers the chemical potential of each component. This is why mixing is spontaneous for ideal solutions. It also explains **colligative properties**: adding a solute lowers the chemical potential of the solvent, which shifts phase boundaries. The solvent's vapor pressure drops (Raoult's law), its boiling point rises, and its freezing point falls — all because the solute reduced the solvent's chemical potential relative to the pure liquid.

Chemical potential also provides the bridge to **chemical reaction equilibrium**. The condition ΔG = 0 at equilibrium can be rewritten as Σνᵢμᵢ = 0, where νᵢ are stoichiometric coefficients (negative for reactants, positive for products). Substituting the ideal expression for each μᵢ recovers the familiar relationship ΔG° = −RT ln K. But the chemical potential formulation is more general: it applies to non-ideal solutions, to electrochemical cells (where electrical work modifies μ), and to biological systems where concentration gradients across membranes drive transport. Whenever you need to predict the direction of spontaneous change in a system with multiple components, chemical potential is the quantity to examine.

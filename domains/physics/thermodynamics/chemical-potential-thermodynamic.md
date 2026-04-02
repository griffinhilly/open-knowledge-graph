---
id: chemical-potential-thermodynamic
title: Chemical Potential and Partial Molar Properties
domain: physics
course: thermodynamics
prerequisites:
- id: gibbs-free-energy
  type: hard
- id: legendre-transformations-potentials
  type: hard
builds-toward:
- phase-equilibrium-coexistence
tags:
- chemical-potential
- mixtures
stage: expert
status: validated
---

# Chemical Potential and Partial Molar Properties

## Core Idea
Chemical potential μ = (∂G/∂n)_{T,P} is the molar Gibbs free energy of adding one mole to a large system. In equilibrium, chemical potentials of a substance in different phases are equal. Partial molar properties generalize intensive properties to mixtures: V̄ = (∂V/∂n)_{T,P}, H̄ = (∂H/∂n)_{T,P}.

## Questions

```yaml
- question: "Two regions at the same temperature and pressure contain water vapor and liquid water respectively. The chemical potential of water is higher in the liquid phase. What will happen?"
  type: multiple-choice
  options:
    - "Water will transfer from vapor to liquid until chemical potentials equalize"
    - "Water will transfer from liquid to vapor until chemical potentials equalize"
    - "No transfer occurs because the system is already at the same T and P"
    - "Transfer direction depends on which phase has higher entropy"
  answer: 1
  explanation: "Matter flows spontaneously from high chemical potential to low chemical potential, exactly as heat flows from high temperature to low temperature. If the liquid has higher μ, the system lowers its total Gibbs free energy by transferring matter from liquid (high μ) to vapor (low μ). Equilibrium is reached when μ_liquid = μ_vapor. The common error is option C — equal T and P are necessary but not sufficient for equilibrium; chemical potentials must also be equal for a system that can exchange matter between phases."

- question: "For a pure substance at constant temperature and pressure, the chemical potential μ is equal to which of the following?"
  type: multiple-choice
  options:
    - "The total Gibbs free energy G of the system"
    - "The molar Gibbs free energy G/n"
    - "The partial derivative of entropy with respect to particle number"
    - "The Helmholtz free energy per mole"
  answer: 1
  explanation: "For a pure substance, μ = G/n — the Gibbs free energy per mole. This follows directly from the definition μ = (∂G/∂n)_{T,P}: for a pure substance, adding one mole to a large reservoir at constant T and P increases G by exactly G/n. For mixtures, each component i has its own μᵢ = (∂G/∂nᵢ)_{T,P,nⱼ≠i} and the total G = Σᵢ nᵢμᵢ, which is why μᵢ and G/n diverge in the presence of other components."

- question: "At equilibrium between liquid and vapor phases of a substance, the chemical potential of the substance in both phases must be equal, even if the concentration (moles per liter) differs significantly between phases."
  type: true-false
  answer: true
  explanation: "True. The equilibrium condition for phase coexistence is μ_α = μ_β — chemical potentials must be equal, not concentrations. In a liquid-vapor system, the concentration of the substance in the liquid is typically orders of magnitude higher than in the vapor, yet equilibrium requires equal μ. This is the key insight: chemical potential, not concentration, is the driving force for mass transfer. Equal chemical potentials mean there is no net thermodynamic incentive for matter to flow from one phase to the other."

- question: "The partial molar volume of ethanol in a water-ethanol mixture is equal to the molar volume of pure ethanol."
  type: true-false
  answer: false
  explanation: "False. The partial molar volume V̄ᵢ = (∂V/∂nᵢ)_{T,P,nⱼ≠i} measures how the total volume changes when a small amount of component i is added to the mixture — and this is not the same as the molar volume of pure i. Intermolecular interactions between different species change volumes upon mixing. In water-ethanol mixtures, partial molar volumes are less than pure-component molar volumes, making the mixture denser than a simple additive calculation would predict. This is precisely why partial molar properties are needed: to account for mixing effects."

- question: "Explain why matter flows spontaneously from regions of high chemical potential to regions of low chemical potential, using an analogy to other thermodynamic driving forces."
  type: short-answer
  answer: "Chemical potential μ is the intensive variable conjugate to particle number N in the same way that temperature T is conjugate to entropy S and pressure P is conjugate to volume V. Just as heat flows from high T to low T (to maximize entropy) and mechanical systems do work from high P to low P (to minimize energy), matter flows from high μ to low μ because this reduces the total Gibbs free energy of the system. At constant T and P, the spontaneous direction of any process is decreasing G, and when matter can redistribute, the way to decrease G is to move particles from where each particle 'costs' more Gibbs free energy (high μ) to where each particle costs less (low μ). Equilibrium is reached when there is no further reduction possible — i.e., when μ is equal everywhere the substance can be found."
  explanation: "The analogy is mathematically exact: from the fundamental relation dG = -SdT + VdP + μdN, we see that μ, T, and P each drive flows of their conjugate extensive variable (N, S, V). The common misconception is to think concentration or density drives mass transfer, but osmosis dramatically demonstrates this is wrong: water flows from low solute concentration (high μ_water) to high solute concentration (low μ_water) across a semipermeable membrane, against the concentration gradient but in the direction of decreasing chemical potential."
```

## Explainer

From your work on Gibbs free energy, you know that processes at constant temperature and pressure proceed spontaneously in the direction of decreasing G, and equilibrium is where G is minimized. But G as you've used it describes a closed system with a fixed amount of material. The **chemical potential** extends this framework to open systems — systems that can exchange matter with their surroundings, or systems where material redistributes between phases or components. It answers the question: what is the thermodynamic "pressure" that drives matter to flow from one place to another?

The definition μ = (∂G/∂n)_{T,P} is the change in Gibbs free energy when one mole is added to a large reservoir at constant T and P. Think of it as the "price" in free energy units of adding one more particle to the system. If you connect two regions at the same T and P but different μ, matter will spontaneously flow from high μ to low μ — just as heat flows from high T to low T, and mechanical work is done from high P to low P. This analogy is precise: μ is the intensive variable conjugate to particle number N, exactly as T is conjugate to entropy S and P is conjugate to volume V. The condition for chemical equilibrium between two phases α and β is μ_α = μ_β; the driving force for mass transfer vanishes when potentials equalize.

From Legendre transformations, you know that G is the natural potential for constant-T, constant-P processes. Writing the fundamental relation dG = −SdT + VdP + μdN makes the chemical potential appear naturally: G already has (T, P, N) as its natural variables. For a pure substance, μ is simply the molar Gibbs free energy: μ = G/n. For **mixtures**, each component i has its own chemical potential μᵢ = (∂G/∂nᵢ)_{T,P,nⱼ≠i}, and the total G = Σᵢ nᵢμᵢ. The **Gibbs-Duhem equation** SdT − VdP + Σᵢ nᵢdμᵢ = 0 follows from this and constrains how the chemical potentials of mixture components can vary together.

**Partial molar properties** generalize this idea to any extensive property. The partial molar volume V̄ᵢ = (∂V/∂nᵢ)_{T,P,nⱼ≠i} is how much the total volume changes when a small amount of component i is added. This is not simply the molar volume of pure i — mixing changes volumes due to intermolecular interactions. In water-ethanol mixtures, for instance, partial molar volumes are less than the pure-component molar volumes, meaning the mixture is denser than expected. The partial molar enthalpy H̄ᵢ captures the heat of mixing in the same way. These quantities allow thermodynamic analysis of real mixtures, chemical reactions in solution, and phase equilibria — the foundation of chemical engineering separations, materials processing, and biological membrane thermodynamics.

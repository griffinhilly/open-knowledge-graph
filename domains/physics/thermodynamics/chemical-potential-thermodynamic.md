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
stage: formal-systems
status: draft
---

# Chemical Potential and Partial Molar Properties

## Core Idea
Chemical potential μ = (∂G/∂n)_{T,P} is the molar Gibbs free energy of adding one mole to a large system. In equilibrium, chemical potentials of a substance in different phases are equal. Partial molar properties generalize intensive properties to mixtures: V̄ = (∂V/∂n)_{T,P}, H̄ = (∂H/∂n)_{T,P}.

## Explainer

From your work on Gibbs free energy, you know that processes at constant temperature and pressure proceed spontaneously in the direction of decreasing G, and equilibrium is where G is minimized. But G as you've used it describes a closed system with a fixed amount of material. The **chemical potential** extends this framework to open systems — systems that can exchange matter with their surroundings, or systems where material redistributes between phases or components. It answers the question: what is the thermodynamic "pressure" that drives matter to flow from one place to another?

The definition μ = (∂G/∂n)_{T,P} is the change in Gibbs free energy when one mole is added to a large reservoir at constant T and P. Think of it as the "price" in free energy units of adding one more particle to the system. If you connect two regions at the same T and P but different μ, matter will spontaneously flow from high μ to low μ — just as heat flows from high T to low T, and mechanical work is done from high P to low P. This analogy is precise: μ is the intensive variable conjugate to particle number N, exactly as T is conjugate to entropy S and P is conjugate to volume V. The condition for chemical equilibrium between two phases α and β is μ_α = μ_β; the driving force for mass transfer vanishes when potentials equalize.

From Legendre transformations, you know that G is the natural potential for constant-T, constant-P processes. Writing the fundamental relation dG = −SdT + VdP + μdN makes the chemical potential appear naturally: G already has (T, P, N) as its natural variables. For a pure substance, μ is simply the molar Gibbs free energy: μ = G/n. For **mixtures**, each component i has its own chemical potential μᵢ = (∂G/∂nᵢ)_{T,P,nⱼ≠i}, and the total G = Σᵢ nᵢμᵢ. The **Gibbs-Duhem equation** SdT − VdP + Σᵢ nᵢdμᵢ = 0 follows from this and constrains how the chemical potentials of mixture components can vary together.

**Partial molar properties** generalize this idea to any extensive property. The partial molar volume V̄ᵢ = (∂V/∂nᵢ)_{T,P,nⱼ≠i} is how much the total volume changes when a small amount of component i is added. This is not simply the molar volume of pure i — mixing changes volumes due to intermolecular interactions. In water-ethanol mixtures, for instance, partial molar volumes are less than the pure-component molar volumes, meaning the mixture is denser than expected. The partial molar enthalpy H̄ᵢ captures the heat of mixing in the same way. These quantities allow thermodynamic analysis of real mixtures, chemical reactions in solution, and phase equilibria — the foundation of chemical engineering separations, materials processing, and biological membrane thermodynamics.

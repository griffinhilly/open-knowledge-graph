---
id: thermodynamic-equilibrium-mechanical-chemical
title: 'Thermodynamic Equilibrium: Mechanical, Thermal, and Chemical'
domain: physics
course: thermodynamics
prerequisites:
- id: zeroth-law-of-thermodynamics
  type: hard
- id: temperature-and-thermal-equilibrium
  type: hard
builds-toward:
- state-variables-and-functions
- phase-equilibrium-coexistence
tags:
- equilibrium
- stability
- conditions
stage: formal-systems
status: validated
---

# Thermodynamic Equilibrium: Mechanical, Thermal, and Chemical

## Core Idea
Thermodynamic equilibrium occurs when a system has no tendency to change its properties and is simultaneously in mechanical, thermal, and chemical equilibrium. Mechanical equilibrium requires uniform pressure; thermal equilibrium requires uniform temperature; chemical equilibrium requires uniform chemical potential throughout. A system at true thermodynamic equilibrium will not spontaneously undergo any changes in macroscopic properties.

## How It's Best Learned
Examine systems approaching equilibrium from non-equilibrium states: gas diffusion, temperature gradients, pressure imbalances. Identify which driving forces vanish at equilibrium.

## Common Misconceptions
- Thinking equilibrium means no motion at the molecular level.
- Confusing static equilibrium (mechanics) with thermodynamic equilibrium.
- Assuming any single criterion (e.g., constant T) guarantees full equilibrium.

## Questions

```yaml
- question: "A rigid, thermally insulated container holds a mixture of H₂ and O₂ at perfectly uniform temperature and pressure. Has the system reached thermodynamic equilibrium?"
  type: multiple-choice
  options:
    - "Yes — uniform temperature and pressure satisfy all equilibrium conditions."
    - "Not necessarily — chemical equilibrium also requires Σνᵢμᵢ = 0 for all reactions, which may not yet hold."
    - "Yes — rigidity guarantees mechanical equilibrium and insulation guarantees thermal equilibrium."
    - "No — thermodynamic equilibrium is impossible in a rigid container because boundaries always transmit some energy."
  answer: 1
  explanation: "Uniform T satisfies thermal equilibrium; rigidity with uniform P satisfies mechanical equilibrium. But thermodynamic equilibrium requires all three conditions simultaneously. H₂ and O₂ can react (2H₂ + O₂ → 2H₂O), and if this reaction has not reached its equilibrium composition, chemical potentials are unbalanced and the system will spontaneously evolve. Uniform T and P are necessary but not sufficient; without verifying Σνᵢμᵢ = 0 for all reactions, full thermodynamic equilibrium cannot be assumed."

- question: "What drives particles to flow between two regions, and what condition is satisfied when chemical equilibrium is reached?"
  type: multiple-choice
  options:
    - "Particles flow from low to high chemical potential, like water flowing uphill; equilibrium requires equal pressure."
    - "Particles flow from high to low chemical potential; equilibrium requires chemical potential to be uniform throughout for each species."
    - "Particles flow due to temperature gradients; chemical equilibrium requires equal temperatures everywhere."
    - "Particles move randomly with no directional tendency; equilibrium is reached when all molecular motion ceases."
  answer: 1
  explanation: "Chemical potential μ = (∂G/∂N)_{T,P} is the Gibbs free energy per particle. Just as heat flows from high T to low T and pressure drives volume change, particles flow from high μ to low μ — from regions where adding a particle is energetically costly to regions where it is cheap. Chemical equilibrium requires μ to be uniform for each species throughout the system: no gradient, no net flow. For chemical reactions, equilibrium requires Σνᵢμᵢ = 0, meaning the chemical potentials of reactants and products are exactly balanced."

- question: "A system can be in thermal and mechanical equilibrium while still not being in full thermodynamic equilibrium."
  type: true-false
  answer: true
  explanation: "Thermodynamic equilibrium requires three simultaneous conditions: thermal (uniform T), mechanical (uniform P, no net forces on movable boundaries), and chemical (uniform μ for each species, no net reaction). A system satisfying the first two can still be undergoing chemical reaction. A rigid insulated container with a slow-reacting mixture is in thermal and mechanical equilibrium throughout the reaction — but not thermodynamic equilibrium until the reaction reaches completion (Σνᵢμᵢ = 0). Partial equilibrium is common in practice and is often exploited as a useful approximation."

- question: "A gas mixture at uniform temperature and pressure should be at thermodynamic equilibrium, since no driving forces remain for heat flow or mechanical work."
  type: true-false
  answer: false
  explanation: "Uniform T eliminates the driving force for heat flow, and uniform P eliminates the driving force for volume work. But these two conditions say nothing about whether chemical reactions are proceeding or whether species are diffusing due to chemical potential gradients. A mixture at uniform T and P can be far from chemical equilibrium — for example, H₂ + Cl₂ → 2HCl proceeds at uniform T and P until the equilibrium composition is reached. Thermodynamic equilibrium requires all three driving forces (thermal, mechanical, chemical) to vanish simultaneously."

- question: "Explain why thermodynamic equilibrium requires three simultaneous conditions rather than just thermal equilibrium (uniform temperature)."
  type: short-answer
  answer: "Temperature uniform throughout means heat will not flow spontaneously — thermal equilibrium is satisfied. But a system can have uniform T while still having pressure gradients that drive mechanical work, or chemical potential gradients that drive diffusion and reaction. Each condition corresponds to a different mode of spontaneous change: thermal gradients drive heat flow, pressure gradients drive volume change, and chemical potential gradients drive matter flow and chemical reactions. Thermodynamic equilibrium means all spontaneous processes have ceased simultaneously — all three driving forces must vanish at once."
  explanation: "This is why thermodynamic equilibrium is a richer concept than mechanical equilibrium. In mechanics, equilibrium means no net force. In thermodynamics, 'forces' include temperature differences (driving heat flow), pressure imbalances (driving mechanical work), and chemical potential differences (driving diffusion and reaction). A system is truly at rest — at thermodynamic equilibrium — only when none of these thermodynamic driving forces remain. Partial equilibrium (thermal + mechanical, but not chemical) is common when reactions are slow and is often the appropriate approximation for thermodynamic analysis."
```

## Explainer

The zeroth law gave you thermal equilibrium: two systems in contact with no heat flow have the same temperature. Temperature-and-thermal-equilibrium deepened this by connecting temperature to the tendency of energy to distribute among microstates. Thermodynamic equilibrium extends this logic to *all* the ways a system can exchange things across its boundary — not just heat, but also mechanical work (volume exchange) and matter (particle exchange). Full equilibrium requires all three driving forces to vanish simultaneously.

**Mechanical equilibrium** means the pressure is uniform throughout the system and equal across any boundary. If a piston separates two regions at different pressures, it accelerates — work is done, the system changes, equilibrium is absent. At mechanical equilibrium, pressure gradients vanish: there is no net force on any movable boundary. In a column of fluid in a gravitational field, the pressure gradient dp/dh = −ρg *is* the mechanical equilibrium condition (balancing gravity against the pressure gradient), so equilibrium does not require pressure to be spatially uniform if external fields are present — it requires the net force on every fluid element to vanish.

**Chemical equilibrium** introduces the concept of **chemical potential** μ. For a pure substance, μ = (∂G/∂N)_{T,P} — the Gibbs free energy per particle, or equivalently the energy cost of adding one more particle at constant temperature and pressure. Particles flow from high μ to low μ, just as heat flows from high T to low T and volume contracts to equalize P. Chemical equilibrium requires μ to be uniform for each species throughout the system. This is why a solute distributes itself equally between two connected chambers at equilibrium (if the chambers are identical) — any μ gradient drives net diffusion. For chemical reactions, equilibrium requires that the sum of reactant chemical potentials equals the sum of product chemical potentials: Σ νᵢμᵢ = 0, which is the microscopic origin of the equilibrium constant K.

The crucial point is that all three conditions must hold *simultaneously* for true thermodynamic equilibrium. A system can be thermally equilibrated (uniform T) but still have a pressure gradient driving flow — it is in thermal but not mechanical equilibrium. A mixture might be at uniform T and P but still react — it is not in chemical equilibrium. Real systems are often in partial or approximate equilibrium: a gas in a thermally insulated rigid container is in thermal and mechanical equilibrium, but if two reactive species are present and the reaction is slow, chemical equilibrium may take centuries. Thermodynamics describes the *final* state; kinetics governs how fast (or whether) the system gets there. Recognizing which equilibrium conditions are satisfied — and which are not — is the first step in any thermodynamic analysis.

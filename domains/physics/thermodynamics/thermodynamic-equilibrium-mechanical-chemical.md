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
status: draft
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

## Explainer

The zeroth law gave you thermal equilibrium: two systems in contact with no heat flow have the same temperature. Temperature-and-thermal-equilibrium deepened this by connecting temperature to the tendency of energy to distribute among microstates. Thermodynamic equilibrium extends this logic to *all* the ways a system can exchange things across its boundary — not just heat, but also mechanical work (volume exchange) and matter (particle exchange). Full equilibrium requires all three driving forces to vanish simultaneously.

**Mechanical equilibrium** means the pressure is uniform throughout the system and equal across any boundary. If a piston separates two regions at different pressures, it accelerates — work is done, the system changes, equilibrium is absent. At mechanical equilibrium, pressure gradients vanish: there is no net force on any movable boundary. In a column of fluid in a gravitational field, the pressure gradient dp/dh = −ρg *is* the mechanical equilibrium condition (balancing gravity against the pressure gradient), so equilibrium does not require pressure to be spatially uniform if external fields are present — it requires the net force on every fluid element to vanish.

**Chemical equilibrium** introduces the concept of **chemical potential** μ. For a pure substance, μ = (∂G/∂N)_{T,P} — the Gibbs free energy per particle, or equivalently the energy cost of adding one more particle at constant temperature and pressure. Particles flow from high μ to low μ, just as heat flows from high T to low T and volume contracts to equalize P. Chemical equilibrium requires μ to be uniform for each species throughout the system. This is why a solute distributes itself equally between two connected chambers at equilibrium (if the chambers are identical) — any μ gradient drives net diffusion. For chemical reactions, equilibrium requires that the sum of reactant chemical potentials equals the sum of product chemical potentials: Σ νᵢμᵢ = 0, which is the microscopic origin of the equilibrium constant K.

The crucial point is that all three conditions must hold *simultaneously* for true thermodynamic equilibrium. A system can be thermally equilibrated (uniform T) but still have a pressure gradient driving flow — it is in thermal but not mechanical equilibrium. A mixture might be at uniform T and P but still react — it is not in chemical equilibrium. Real systems are often in partial or approximate equilibrium: a gas in a thermally insulated rigid container is in thermal and mechanical equilibrium, but if two reactive species are present and the reaction is slow, chemical equilibrium may take centuries. Thermodynamics describes the *final* state; kinetics governs how fast (or whether) the system gets there. Recognizing which equilibrium conditions are satisfied — and which are not — is the first step in any thermodynamic analysis.

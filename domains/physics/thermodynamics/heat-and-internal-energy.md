---
id: heat-and-internal-energy
title: Heat and Internal Energy
domain: physics
course: thermodynamics
prerequisites:
- id: temperature-and-thermal-equilibrium
  type: hard
- id: kinetic-energy
  type: hard
builds-toward:
- specific-heat-capacity
- first-law-of-thermodynamics
- phase-transitions
tags:
- heat
- internal-energy
- thermal-energy
- energy-transfer
stage: concrete-operations
status: validated
---

# Heat and Internal Energy

## Core Idea
Internal energy (U) is the total microscopic energy of a system — the kinetic energies of its atoms/molecules plus the potential energies of their interactions. Heat (Q) is energy that flows between systems due to a temperature difference; it is energy in transit, not a property stored in a body. Work is another way energy can be transferred, but heat flows spontaneously from higher to lower temperature until equilibrium is reached.

## How It's Best Learned
Contrast the 'caloric' historical model (heat as a fluid) with the modern mechanical view. Trace energy accounting in simple scenarios: rubbing hands transfers work into internal energy; touching ice transfers heat out. Always ask: is energy flowing as heat or as work?

## Common Misconceptions
- 'Heat content' is a misleading phrase — objects don't store heat, they store internal energy; heat only exists as a process of energy transfer.
- A high temperature does not imply high internal energy — a small flame is hotter than a warm lake, but the lake stores far more energy.

## Explainer

You already know from your study of kinetic energy that moving objects carry energy. **Internal energy** (U) extends this idea to the microscopic scale: it is the sum of all kinetic energies of the atoms and molecules inside a system, plus the potential energies of their interactions. In an ideal monatomic gas, molecules barely interact, so internal energy is almost entirely translational kinetic energy — (3/2)nRT for n moles. In a liquid or solid, intermolecular potential energy contributes significantly because molecules are close together and interact strongly. When ice melts at 0°C, you add energy without changing temperature because the energy goes into breaking intermolecular bonds, not into kinetic energy. This is why internal energy and temperature, though related, are not the same thing.

**Heat** (Q) is not a property of a system — it is a mode of energy transfer. The distinction matters deeply. You do not say a glass of water "contains heat"; you say it has internal energy U. Heat is the name for energy crossing a system boundary driven by a temperature difference. When you touch an ice cube, energy flows from your hand to the ice as heat — because your hand is warmer. When the ice reaches your body temperature, the flow stops. This spontaneous, temperature-driven transfer is what distinguishes heat from work. Work is energy transfer by a macroscopic force through displacement (a piston compressing a gas); heat is energy transfer by molecular collisions across a thermal boundary.

The magnitude of heat transferred depends on the material and how much temperature changes. But you must be careful about the scenario: if a substance changes phase (liquid → gas) at constant temperature, heat is added without any temperature change. This is **latent heat** — the energy goes entirely into changing the arrangement of molecules (internal potential energy), not their speed (temperature). Conversely, rubbing your hands together converts work into internal energy via friction — internal energy rises, temperature rises — without any heat flowing. Both work and heat are ways to change U, but they involve different physical processes.

The accounting rule that ties all this together is the first law of thermodynamics (which builds directly on this topic): ΔU = Q + W, where Q is heat added to the system and W is work done on the system. Every change in internal energy must be accounted for by heat flow or work — energy is conserved. Understanding that U is a state function (it depends only on the current state, not on the path taken to get there), while Q and W are path-dependent transfers, is the conceptual foundation for everything in classical thermodynamics.

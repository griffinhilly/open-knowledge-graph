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
stage: formal-systems
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

## Questions

```yaml
- question: "A cup of coffee cools from 80°C to 20°C sitting on a table. Which statement correctly describes this process?"
  type: multiple-choice
  options:
    - "The coffee lost heat, so it now contains less heat than room-temperature coffee"
    - "Heat was transferred from the coffee to its surroundings; the coffee's internal energy decreased"
    - "The coffee's temperature fell, but its internal energy stayed the same because the atoms didn't disappear"
    - "Heat flowed into the coffee from the room, since the room is at lower temperature"
  answer: 1
  explanation: "Heat is not a substance stored in the coffee — it is the transfer of energy from a hotter to a cooler body. When the coffee cools, its internal energy decreases as heat flows to the surroundings. Option A commits the key misconception: objects don't 'contain heat,' they contain internal energy. Option D reverses the direction — heat flows from hot to cold, not from cold to hot."

- question: "A lit birthday candle burns at 600°C. A warm bathtub holds water at 40°C. Which contains more internal energy?"
  type: multiple-choice
  options:
    - "The candle, because its temperature is much higher"
    - "The bathtub, because it contains vastly more matter with thermal energy"
    - "They contain the same internal energy, because thermal equilibrium will eventually equalize them"
    - "Temperature and internal energy are unrelated, so neither can be compared"
  answer: 1
  explanation: "Internal energy depends on both temperature and the amount of matter. The bathtub contains billions of times more molecules than the candle flame, each carrying kinetic energy. Even at lower temperature, the total internal energy of the water vastly exceeds that of the tiny candle flame. This scenario illustrates why high temperature does not imply high internal energy — a classic misconception noted in the Common Misconceptions section."

- question: "When ice melts at 0°C, it absorbs energy without any change in temperature because the energy goes into breaking intermolecular bonds rather than increasing molecular speeds."
  type: true-false
  answer: true
  explanation: "This is latent heat of fusion. At 0°C, the ice and water are in equilibrium — added energy goes entirely into the phase transition (breaking the hydrogen bond network of the crystal lattice), not into raising kinetic energy. Since temperature measures average kinetic energy of molecules, and kinetic energy isn't changing here, temperature stays constant while internal potential energy increases. This directly shows that internal energy and temperature are distinct quantities."

- question: "A body with a higher te
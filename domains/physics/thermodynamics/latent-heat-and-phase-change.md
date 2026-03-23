---
id: latent-heat-and-phase-change
title: Latent Heat and Phase Changes
domain: physics
course: thermodynamics
prerequisites:
- id: phase-transitions
  type: hard
- id: enthalpy-definition-and-significance
  type: soft
tags:
- latent-heat
- phase-change
- vaporization
- condensation
stage: formal-systems
status: validated
---

# Latent Heat and Phase Changes

## Core Idea
Latent heat is energy absorbed or released during a phase transition without temperature change. The heat of vaporization (L_v) is energy to convert liquid to gas; the heat of fusion (L_f) is energy to convert solid to liquid. These are intensive properties (per unit mass) and critically important in calorimetry and engineering.

## Questions

```yaml
- question: "You are heating 100 g of water that has just reached 100°C at standard pressure. You add 10,000 J of heat. What happens?"
  type: multiple-choice
  options:
    - "The temperature rises to about 124°C as the water absorbs sensible heat"
    - "The water remains at 100°C while approximately 4.4 g vaporizes; the remaining ~95.6 g stays as liquid"
    - "All 100 g instantly vaporizes because it is already at the boiling point"
    - "Temperature rises and vaporization occur simultaneously in equal proportions"
  answer: 1
  explanation: "At the boiling point, added heat goes into latent heat of vaporization (L_v ≈ 2260 J/g for water), not into raising temperature. 10,000 J can vaporize about 10,000/2260 ≈ 4.4 g; the remaining liquid stays at 100°C. Temperature will not rise until all liquid is vaporized. Temperature is constant during a phase transition — this is the defining property of latent heat."

- question: "Which requires more energy per gram: melting ice at 0°C, or vaporizing water at 100°C?"
  type: multiple-choice
  options:
    - "Melting ice — overcoming a rigid crystal lattice requires the most energy"
    - "They require equal energy — both occur at fixed temperatures, so the energy input is the same"
    - "Vaporizing water — molecules must be completely separated from all neighbors, requiring far more energy than disrupting long-range lattice order"
    - "Melting ice — because it starts at a lower temperature and must absorb more energy to change state"
  answer: 2
  explanation: "L_v ≈ 2260 J/g vs. L_f ≈ 334 J/g for water — vaporization requires about 6.8 times as much energy as melting. Melting only disrupts long-range lattice order; liquid molecules still attract one another at short range. Vaporization must overcome all short-range attractions, fully separating each molecule from all neighbors. This requires far more energy, even though both transitions occur at constant temperature."

- question: "During a phase transition, adding heat to a system does not cause its temperature to rise."
  type: true-false
  answer: true
  explanation: "This is the defining property of latent heat. During a phase change — melting, boiling, sublimation — added energy goes into breaking or forming intermolecular bonds and reorganizing matter, not into increasing molecular kinetic energy. Since temperature measures average kinetic energy, it remains constant until the entire sample has transitioned. Temperature resumes rising only after the phase change is complete."

- question: "To calculate the total heat needed to convert 50 g of ice at −10°C to steam at 120°C, you can use a single equation Q = mcΔT with ΔT = 130°C."
  type: true-false
  answer: false
  explanation: "This is the classic calorimetry error — treating a phase change as just another temperature step. The process requires five separate calculations: (1) warming ice from −10°C to 0°C; (2) melting ice at 0°C (q = mL_f); (3) warming water from 0°C to 100°C; (4) vaporizing water at 100°C (q = mL_v); (5) warming steam from 100°C to 120°C. No single q = mcΔT captures the full process, because latent heat operates at constant temperature with a different equation."

- question: "Explain at the molecular level why temperature stays constant during a phase change, and give one practical example that demonstrates the importance of this effect."
  type: short-answer
  answer: "Temperature reflects average molecular kinetic energy. During a phase change, added energy goes into overcoming intermolecular attractive forces — breaking lattice bonds in melting, or fully separating molecules in vaporization — rather than increasing molecular speed. Until the structural reorganization is complete, no energy is available to increase kinetic energy, so temperature stays flat. Practically: sweating exploits water's large latent heat of vaporization (≈2260 J/g). Each gram of water evaporating from skin carries away 2260 J without any temperature rise — far more cooling per gram than any sensible-heat mechanism over a few degrees."
  explanation: "The plateau on a heating curve is a direct experimental signature of latent heat. If you plot temperature vs. time for a constant heat input, you will see a flat line at the melting point and another at the boiling point — the energy is being absorbed without any temperature change during both phase transitions."
```

## Explainer

When you heat a solid, you add energy and its temperature rises — this is the familiar behavior governed by heat capacity. But when the solid reaches its melting point, something qualitatively different happens: you continue adding energy and the temperature *stops rising* until the entire sample has melted. The energy added during this plateau goes into restructuring intermolecular bonds and changing the organization of matter, not into increasing molecular kinetic energy. This energy absorbed or released during a phase transition without temperature change is **latent heat** — "latent" from the Latin for hidden, because it does not manifest as a temperature change visible on a thermometer.

The molecular picture makes the mechanism clear. In a solid, molecules are locked in a lattice by attractive interactions and vibrate around fixed positions. Melting requires enough energy input to liberate molecules from these lattice positions so they can flow past one another. The **latent heat of fusion** L_f is this energy per unit mass. Vaporization requires even more: molecules in a liquid still attract each other at short range and must be completely separated to enter the gas phase. The **latent heat of vaporization** L_v is always much larger than L_f for the same substance — for water, L_f ≈ 334 J/g while L_v ≈ 2260 J/g — because complete separation from all neighbors requires far more energy than simply disrupting long-range lattice order while keeping neighbors nearby.

Your prerequisite on phase transitions established that phase boundaries represent thermodynamic equilibrium between two coexisting phases. At the melting or boiling point, adding heat converts one phase into the other at constant temperature while both phases coexist. If you have studied enthalpy, the connection is immediate: at constant pressure, latent heat equals the enthalpy change of the transition, ΔH_fus or ΔH_vap. The enthalpy perspective clarifies why the temperature is constant: all the heat input at constant pressure goes into changing the system's enthalpy (bond energy and PV work against atmospheric pressure), with no increase in internal kinetic energy and therefore no temperature rise.

Calorimetry problems involving phase changes require careful bookkeeping that distinguishes two types of heat transfer. **Sensible heat** (q = mcΔT) describes heat that changes temperature within a single phase. **Latent heat** (q = mL) describes heat exchanged at a phase boundary at constant temperature. When a substance passes through a phase transition, both contributions must be added: for example, converting 50 g of ice at −10°C to steam at 120°C requires heat for warming the ice, melting it, warming the liquid, vaporizing it, and then superheating the steam — five separate terms. Treating the phase transition as just another temperature step is the most common calorimetry error. Practically, water's enormous L_v is why sweating cools so effectively: each gram of water that evaporates from skin carries away 2260 J, far more than any sensible-heat mechanism over a few degrees of temperature difference.

---
id: states-of-matter-properties-and-transitions
title: States of Matter and Phase Transitions
domain: chemistry
course: general-chemistry
prerequisites:
- id: intermolecular-forces
  type: hard
- id: heat-capacity-calorimetry
  type: soft
builds-toward:
- phase-changes-and-diagrams
- solution-concentration
tags:
- states
- phase
- gas
- liquid
- solid
stage: advanced
status: draft
---

# States of Matter and Phase Transitions

## Core Idea
Matter exists in three main states—solid, liquid, and gas—distinguished by how closely particles are packed and how freely they move. Phase transitions occur when energy addition or removal overcomes intermolecular forces. Melting, vaporization, sublimation, and their reverses are endothermic or exothermic processes.

## Questions

```yaml
- question: "A beaker of water is boiling steadily at 100°C at atmospheric pressure. You turn up the burner to add heat faster. What happens to the temperature of the boiling water?"
  type: multiple-choice
  options:
    - "It rises above 100°C because more energy is being added per second"
    - "It stays at 100°C because all added energy goes into the phase transition, not into increasing molecular speed"
    - "It drops slightly below 100°C because faster evaporation absorbs heat from the remaining liquid"
    - "It fluctuates between 95°C and 105°C due to increased turbulence from faster boiling"
  answer: 1
  explanation: "This is the defining feature of phase transitions: temperature remains constant during the transition because energy is absorbed to break intermolecular forces (enthalpy of vaporization) rather than to increase kinetic energy. The extra heat just makes water evaporate faster, not hotter. Temperature only rises again once all the liquid has converted to gas."

- question: "For the same substance, the enthalpy of vaporization is always larger than the enthalpy of fusion. What is the best physical explanation?"
  type: multiple-choice
  options:
    - "Vaporization requires the substance to first melt, so it includes the fusion energy as a subset"
    - "The gas phase is hotter than the liquid phase and requires additional thermal energy to maintain that temperature"
    - "Vaporization must fully separate molecules from all remaining intermolecular contact, while melting only disrupts the fixed lattice while molecules remain in close proximity"
    - "Vaporization requires more energy because the gas phase has greater gravitational potential energy than the liquid phase"
  answer: 2
  explanation: "In melting, molecules gain enough energy to slide past their neighbors, but they remain in close contact — intermolecular forces still act. In vaporization, molecules must be fully separated from the bulk liquid so that intermolecular forces become negligible. This requires overcoming all remaining attractive interactions, not just the lattice structure, which demands far more energy."

- question: "During a phase transition, the temperature of a substance remains constant because no energy is actually being transferred into or out of the substance."
  type: true-false
  answer: false
  explanation: "Energy IS being transferred — it just isn't going into kinetic energy (which would raise temperature). Instead, it breaks intermolecular bonds (during melting or vaporization) or releases energy from forming bonds (during freezing or condensation). The constant temperature reflects that all energy input is consumed by the phase change itself, not that energy transfer has stopped."

- question: "A substance with stronger intermolecular forces will generally have a higher boiling point than a similarly sized substance with weaker intermolecular forces."
  type: true-false
  answer: true
  explanation: "Boiling point is determined by how much kinetic energy molecules need to escape the liquid phase. Stronger intermolecular forces (e.g., hydrogen bonds vs. London dispersion forces) hold molecules together more tightly, requiring higher temperature — and thus greater kinetic energy — to achieve separation. This is why water (strong hydrogen bonds) boils at 100°C while methane (only weak London forces) boils at −161°C, despite methane having a higher molecular mass."

- question: "Why doesn't the temperature of water rise above 100°C while it is actively boiling at atmospheric pressure, even if you increase the heat input?"
  type: short-answer
  answer: "During boiling, all added energy goes into breaking the remaining intermolecular forces holding water molecules in the liquid phase (the enthalpy of vaporization), rather than increasing the kinetic energy of the molecules. Temperature is a measure of average kinetic energy, so if energy goes into bond-breaking instead, temperature stays constant. Only once all the liquid has vaporized can additional energy raise the temperature of the steam."
  explanation: "This constant-temperature behavior is the experimental signature of a first-order phase transition. The enthalpy of vaporization for water (40.7 kJ/mol) must be supplied to every mole of water converted to steam. Until that energetic 'debt' is paid for all the liquid present, the temperature cannot rise. Increasing heat input just pays off that debt faster — the water boils away more quickly at the same 100°C."
```

## Explainer

From your study of intermolecular forces, you know that molecules attract each other through dipole-dipole interactions, hydrogen bonds, and London dispersion forces. The state of matter a substance adopts is essentially a contest between these attractive forces pulling molecules together and the kinetic energy of the molecules trying to fly apart. In a **solid**, intermolecular forces win decisively — particles are locked into fixed positions, vibrating in place but unable to move past their neighbors. In a **liquid**, kinetic energy is high enough that particles slide past one another while remaining in close contact. In a **gas**, kinetic energy overwhelms the attractive forces entirely, and particles move independently with large spaces between them.

**Phase transitions** happen when the balance tips. When you heat a solid, you are adding kinetic energy to the particles. At the **melting point**, the added energy is just enough to overcome the forces holding particles in their fixed lattice positions, and the solid becomes a liquid. Crucially, during the transition itself, the temperature does not rise — all the energy being added goes into breaking intermolecular attractions rather than increasing particle speed. This is the **enthalpy of fusion**. The same principle applies at the **boiling point**, where the **enthalpy of vaporization** represents the energy needed to fully separate liquid-phase particles into the gas phase. Because vaporization requires overcoming all remaining intermolecular contact, it always demands more energy than melting.

The reverse processes release energy. **Condensation** (gas to liquid) and **freezing** (liquid to solid) are exothermic — the formation of intermolecular attractions releases the same energy that was required to break them. **Sublimation** is the direct transition from solid to gas, skipping the liquid phase entirely, and it requires energy equal to the sum of fusion and vaporization enthalpies. Dry ice (solid CO₂) sublimes at atmospheric pressure because CO₂'s weak London dispersion forces and low molecular symmetry make the liquid phase unstable under normal conditions.

The strength of a substance's intermolecular forces directly predicts its phase behavior. Water, with its extensive hydrogen bonding network, has an unusually high boiling point for its molecular weight. Methane, relying only on weak London forces, is a gas at room temperature. Comparing boiling points across a series of molecules is really comparing the strength of their intermolecular forces — a principle that connects this topic directly to everything you learned about molecular polarity and intermolecular attractions.

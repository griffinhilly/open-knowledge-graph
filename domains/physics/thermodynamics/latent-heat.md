---
id: latent-heat
title: Latent Heat
domain: physics
course: thermodynamics
prerequisites:
- id: phase-transitions
  type: hard
- id: specific-heat-capacity
  type: hard
builds-toward:
  - phase-diagrams
tags:
- latent-heat
- heat-of-fusion
- heat-of-vaporization
- phase-change
- Q=mL
stage: abstract-reasoning
status: validated
---
# Latent Heat

## Core Idea
Latent heat (L) is the heat per unit mass absorbed or released during a phase transition at constant temperature: Q = mL. The latent heat of fusion (L_f) applies to melting/freezing; the latent heat of vaporization (L_v) applies to boiling/condensation. For water: L_f = 334 kJ/kg and L_v = 2260 kJ/kg — vaporization requires about 7 times more energy than melting. The large L_v of water makes steam burns far more severe than boiling-water burns of equal mass.

## How It's Best Learned
Include latent heat in calorimetry problems: calculate the heat needed to convert 100 g of ice at −10°C to steam at 110°C, accounting for three temperature ramps (Q = mcΔT) and two phase transitions (Q = mL).

## Common Misconceptions
- Latent heat is not 'hidden' in a mysterious sense — the energy goes into breaking intermolecular bonds, increasing potential energy rather than kinetic energy.
- Condensation releases latent heat — when steam condenses on skin, it releases L_v ≈ 2260 kJ/kg, which is why steam scalds are so dangerous.

## Questions

```yaml
- question: "You are heating 1 kg of water. You add heat steadily to raise it from 10°C to 100°C. You continue adding heat at the same rate once it reaches 100°C. What happens to the water's temperature while it is actively boiling?"
  type: multiple-choice
  options:
    - "It continues rising at the same rate, since the same amount of heat is being added"
    - "It rises more slowly because steam has a lower specific heat than liquid water"
    - "It stays at 100°C until all the water has vaporized, then resumes rising"
    - "It drops slightly as the water expands into steam"
  answer: 2
  explanation: "During a phase transition, all added energy goes into breaking intermolecular bonds (increasing potential energy), not into raising molecular kinetic energy. Since temperature measures average kinetic energy, it doesn't change while the phase change is occurring. The temperature is locked at 100°C until all the water has vaporized; only then does adding heat raise the temperature of the steam. This plateau — not a rise or fall — is the defining signature of latent heat."

- question: "A cook is burned by 50 g of steam at 100°C, and a coworker is burned by 50 g of boiling water also at 100°C. Both burns cover the same skin area. Which burn is more severe?"
  type: multiple-choice
  options:
    - "The boiling water burn — liquid transfers heat to skin more efficiently than gas"
    - "They are equally severe, since both are at 100°C and have the same mass"
    - "The steam burn — steam is hotter than 100°C when it first leaves the pot"
    - "The steam burn — the steam must first condense on the skin, releasing ~113 kJ of latent heat before the resulting water even begins to cool"
  answer: 3
  explanation: "Steam and boiling water are at the same temperature, so intuition suggests equal burns. But when steam contacts skin, it first condenses into liquid water, releasing L_v ≈ 2260 kJ/kg — for 50 g, that's about 113 kJ deposited instantly, before any cooling begins. Boiling water starts cooling immediately without any phase-change energy release. The latent heat of condensation is a massive one-time energy dump that dwarfs the sensible heat both substances carry. This is why steam scalds are disproportionately dangerous."

- question: "Adding heat to water that is actively boiling at 100°C will cause its temperature to rise above 100°C."
  type: true-false
  answer: false
  explanation: "While water undergoes a phase transition, all added heat goes into breaking intermolecular bonds (latent heat of vaporization) rather than increasing molecular kinetic energy. Temperature measures average kinetic energy, so it cannot rise during the phase change. The temperature stays locked at 100°C (at standard pressure) until all the liquid has vaporized; only then does further heating raise the steam's temperature above 100°C. The temperature plateau, not a continued rise, is what defines latent heat."

- question: "The temperature of a substance can remain constant while it absorbs heat, because the energy is being stored as potential energy in changed molecular arrangements rather than as kinetic energy."
  type: true-false
  answer: true
  explanation: "This is the essential physics of latent heat. The temperature plateau during a phase transition is not a violation of energy conservation — the energy is still being absorbed, but it goes into potential energy (breaking bonds, separating molecules) rather than kinetic energy (faster molecular motion). Temperature only measures the kinetic part, so it doesn't change until the phase transition is complete. This is why latent heat was historically called 'hidden' — it didn't register on a thermometer, yet the energy was genuinely stored in the changed molecular configuration."

- question: "Why does steam at 100°C cause more severe burns than boiling water at 100°C, given that both are at the same temperature?"
  type: short-answer
  answer: "When steam contacts skin, it first undergoes a phase transition — condensing from gas to liquid — and releases the latent heat of vaporization (L_v ≈ 2260 kJ/kg) before any temperature change occurs. For a given mass, this condensation alone deposits far more energy than the sensible heat carried by the same mass of boiling water. Boiling water begins cooling immediately without any phase-change energy release. The steam therefore delivers much more total energy per kilogram, causing more severe tissue damage despite starting at the same temperature."
  explanation: "The key is recognizing that temperature alone does not capture the total thermal energy content of a substance. Steam at 100°C and water at 100°C carry very different energy because steam stores the latent heat of vaporization in its molecular configuration. When steam condenses, that energy is released as additional heat — on top of whatever sensible heat the resulting water then transfers. Understanding this asymmetry requires grasping that latent heat is real energy stored in phase, not merely a temperature reading."
```

## Explainer

From specific heat capacity you know that adding heat to a substance normally raises its temperature via Q = mcΔT. Latent heat is what happens at the *boundary* between two phases: you add heat but the temperature does not change. This seems paradoxical until you remember what temperature measures — the average kinetic energy of molecules. During a phase transition, the energy you add goes entirely into overcoming intermolecular forces (potential energy), not into speeding molecules up. The temperature is stuck at the transition point until the phase change is complete, then resumes rising once all the material has transformed.

The word "latent" comes from Latin for "hidden" — the energy is stored in the changed molecular configuration and is not visible as temperature. When ice melts, you supply L_f = 334 kJ/kg to break the rigid hydrogen-bond lattice of ice into the more disordered liquid structure. When water boils, you supply a far larger L_v = 2260 kJ/kg to completely separate molecules from the liquid into gas phase — you are not just disrupting close-range order but pulling molecules far enough apart that intermolecular attractions become negligible. The seven-fold difference between L_v and L_f reflects how much more dramatically vaporization disrupts molecular arrangements compared to melting.

The formula Q = mL is deceptively simple to use once you have it, but the real skill is integrating it correctly into multi-stage calorimetry problems. Consider converting 100 g of ice at −10°C to steam at 110°C. There are five stages: (1) warming ice from −10°C to 0°C (Q = mcΔT with c_ice ≈ 2.09 kJ/kg·K), (2) melting at 0°C (Q = mL_f), (3) warming water from 0°C to 100°C (Q = mcΔT with c_water ≈ 4.18 kJ/kg·K), (4) vaporizing at 100°C (Q = mL_v), and (5) warming steam from 100°C to 110°C (Q = mcΔT with c_steam ≈ 2.01 kJ/kg·K). The vaporization step alone (226 kJ) accounts for nearly 80% of the total energy — dwarfing all the temperature-change stages combined.

The reverse process is equally important. Condensation releases L_v; freezing releases L_f. This is why steam burns are so much worse than boiling-water burns of equal mass: the steam condenses on your skin and instantly deposits 2260 kJ/kg *before* the resulting water even begins to cool. It is also why humid air feels so cold when wet: evaporation from your skin absorbs latent heat. Phase transitions are enormous energy stores and releases — a fact that drives weather (thunderstorms release latent heat of condensation that powers convection), engineering (steam engines, refrigerators, heat pumps all work by cycling a substance through phase transitions), and biology (sweating cools by latent heat of vaporization).

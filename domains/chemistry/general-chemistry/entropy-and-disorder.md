---
id: entropy-and-disorder
title: Entropy and Molecular Disorder
domain: chemistry
course: general-chemistry
prerequisites:
- id: thermochemistry-enthalpy
  type: hard
- id: heat-capacity-calorimetry
  type: soft
builds-toward:
- entropy-and-gibbs-free-energy
- gibbs-free-energy-spontaneity
tags:
- entropy
- disorder
- second law
stage: formal-systems
status: validated
---

# Entropy and Molecular Disorder

## Core Idea
Entropy quantifies the disorder or number of possible microstates in a system. The second law of thermodynamics states that entropy of an isolated system always increases for spontaneous processes.

## How It's Best Learned
Compare entropy values for different states (gas > liquid > solid) and predict entropy changes qualitatively.

## Common Misconceptions
Confusing entropy with enthalpy; thinking entropy always increases even in non-isolated systems.

## Questions

```yaml
- question: "A chemist observes a reaction that proceeds spontaneously even though the products are more ordered than the reactants — the system's entropy decreases. Is this a violation of the second law of thermodynamics?"
  type: multiple-choice
  options:
    - "Yes — the second law requires entropy to increase for all spontaneous processes"
    - "No — the second law requires only that total entropy of the universe (system plus surroundings) increases; if the reaction releases heat, the surroundings' entropy can increase by more than the system's entropy decreases"
    - "No — the second law applies only to isolated systems, and laboratory reactions are never truly isolated"
    - "Yes — any decrease in system entropy prevents spontaneity regardless of what happens in the surroundings"
  answer: 1
  explanation: "The second law governs the entropy of the universe (ΔS_universe = ΔS_system + ΔS_surroundings ≥ 0), not the system alone. An exothermic reaction releases heat to the surroundings. That heat increases the surroundings' entropy by q/T, which can exceed the decrease in system entropy. Water freezing at −10°C is the canonical example: the liquid becomes a more ordered solid (system entropy decreases), but the heat released to the cold surroundings increases surroundings' entropy by a larger amount, so ΔS_universe > 0 and the process is spontaneous. Options A and D confuse 'the universe' with 'the system.'"

- question: "Which of the following processes results in the LARGEST increase in entropy?"
  type: multiple-choice
  options:
    - "Dissolving a small amount of table salt in water at room temperature"
    - "Compressing a gas to half its volume at constant temperature"
    - "The thermal decomposition of a solid carbonate into a metal oxide and multiple moles of CO₂ gas"
    - "Cooling a liquid to crystallize it into a highly ordered solid"
  answer: 2
  explanation: "The largest entropy increase occurs when a solid decomposes into multiple gas molecules — this combines a phase change from solid to gas (enormous increase in microstates) with an increase in the number of particles. Gas molecules occupy vastly more positions and have a much wider range of velocities than solid or liquid particles; producing several moles of CO₂ from one mole of solid represents an enormous increase in W (number of microstates). Dissolving salt (option A) does increase entropy but modestly. Compressing gas (option B) decreases entropy. Crystallization (option D) decreases entropy."

- question: "The second law of thermodynamics states that the entropy of any system should typically increase during a spontaneous process."
  type: true-false
  answer: false
  explanation: "This is the most common misstatement of the second law. The second law states that the total entropy of the UNIVERSE (system plus surroundings) increases for spontaneous processes. A system's entropy can decrease — as when water freezes, ice forms, or proteins fold — as long as the surroundings' entropy increases by at least as much. The second law without qualification applies to isolated systems (no exchange of matter or energy), where ΔS_system = ΔS_universe. In open or closed systems that exchange heat with surroundings, only ΔS_universe is always ≥ 0."

- question: "Water freezing at −10°C is consistent with the second law of thermodynamics even though the water molecules become more ordered during the process."
  type: true-false
  answer: true
  explanation: "System entropy decreases when water freezes (liquid → ordered solid crystal). But freezing releases heat to the cold surroundings (at −10°C = 263 K). The surroundings' entropy change is +q/T_surroundings — positive and large, because the temperature is low (making q/T large). This increase in surroundings' entropy exceeds the decrease in system entropy, so ΔS_universe > 0 and the process is thermodynamically spontaneous. At exactly 0°C, ΔS_universe = 0 (equilibrium — ice and water coexist). Below 0°C, freezing is spontaneous; above 0°C, melting is spontaneous."

- question: "Why must entropy changes in both the system AND the surroundings be tracked to apply the second law? Give an example where the system's entropy decreases but the process still occurs spontaneously."
  type: short-answer
  answer: "The second law governs the total entropy of the universe, not the system alone. A system can reduce its internal disorder by expelling heat or performing work on its surroundings — transferring disorder outward. The surroundings absorb that heat at some temperature T, gaining entropy q/T. If this gain exceeds the system's entropy loss, ΔS_universe > 0 and the process is spontaneous. Example: protein folding. A protein in solution adopts a compact, highly ordered native structure (system entropy decreases), but the folding releases structured water molecules that were surrounding the unfolded chain — those water molecules gain rotational and translational freedom (surroundings entropy increases significantly), making the total ΔS_universe positive."
  explanation: "The Gibbs free energy equation ΔG = ΔH − TΔS encodes exactly this bookkeeping: the TΔS term accounts for the entropy exchanged with surroundings via heat (ΔH = −q_surroundings at constant pressure), so ΔG < 0 is equivalent to ΔS_universe > 0. This is why ΔG is the practical criterion for spontaneity at constant temperature and pressure — it bundles the two-step entropy accounting into a single system-level quantity."
```

## Explainer

From your study of enthalpy and calorimetry, you know how to track energy flowing into and out of a system as heat. But energy alone does not determine whether a process happens spontaneously. Ice melts at room temperature even though melting is endothermic — it absorbs heat from the surroundings. Something beyond enthalpy is driving the process, and that something is **entropy**.

Entropy measures the number of ways a system's energy and particles can be arranged — its **microstates**. A gas has enormously more microstates than a liquid, which has more than a solid, because gas molecules can occupy many more positions and have a wider range of velocities. The Boltzmann equation, S = k ln W, makes this precise: entropy (S) is proportional to the natural log of the number of microstates (W). A system with more possible arrangements has higher entropy. This is why gases have higher entropy than liquids, why dissolving a solid in a solvent increases entropy, and why a reaction that produces more gas molecules than it consumes tends to increase entropy.

The **second law of thermodynamics** states that for any spontaneous process, the total entropy of the universe (system plus surroundings) increases. Notice the word "total" — a system's entropy can decrease, as long as the surroundings' entropy increases by a greater amount. When water freezes at −10°C, the water molecules become more ordered (system entropy decreases), but the heat released into the surroundings increases the surroundings' entropy by a larger amount, so the total entropy still increases. This is why the second law applies to isolated systems without qualification — there are no surroundings to compensate — but requires careful bookkeeping when the system exchanges heat with its environment.

You can predict the sign of entropy change (ΔS) qualitatively in many cases. Processes that increase the number of particles, increase volume, increase temperature, or change from solid to liquid to gas all tend to increase entropy. Conversely, processes that reduce particle count, compress gases, or form ordered crystals decrease the system's entropy. These qualitative predictions become quantitatively powerful when combined with enthalpy through the Gibbs free energy equation (ΔG = ΔH − TΔS), which you will encounter next — the framework that finally unifies the energy and entropy perspectives into a single criterion for spontaneity.

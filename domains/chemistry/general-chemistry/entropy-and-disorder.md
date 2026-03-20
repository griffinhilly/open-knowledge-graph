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
stage: advanced
status: draft
---

# Entropy and Molecular Disorder

## Core Idea
Entropy quantifies the disorder or number of possible microstates in a system. The second law of thermodynamics states that entropy of an isolated system always increases for spontaneous processes.

## How It's Best Learned
Compare entropy values for different states (gas > liquid > solid) and predict entropy changes qualitatively.

## Common Misconceptions
Confusing entropy with enthalpy; thinking entropy always increases even in non-isolated systems.

## Explainer

From your study of enthalpy and calorimetry, you know how to track energy flowing into and out of a system as heat. But energy alone does not determine whether a process happens spontaneously. Ice melts at room temperature even though melting is endothermic — it absorbs heat from the surroundings. Something beyond enthalpy is driving the process, and that something is **entropy**.

Entropy measures the number of ways a system's energy and particles can be arranged — its **microstates**. A gas has enormously more microstates than a liquid, which has more than a solid, because gas molecules can occupy many more positions and have a wider range of velocities. The Boltzmann equation, S = k ln W, makes this precise: entropy (S) is proportional to the natural log of the number of microstates (W). A system with more possible arrangements has higher entropy. This is why gases have higher entropy than liquids, why dissolving a solid in a solvent increases entropy, and why a reaction that produces more gas molecules than it consumes tends to increase entropy.

The **second law of thermodynamics** states that for any spontaneous process, the total entropy of the universe (system plus surroundings) increases. Notice the word "total" — a system's entropy can decrease, as long as the surroundings' entropy increases by a greater amount. When water freezes at −10°C, the water molecules become more ordered (system entropy decreases), but the heat released into the surroundings increases the surroundings' entropy by a larger amount, so the total entropy still increases. This is why the second law applies to isolated systems without qualification — there are no surroundings to compensate — but requires careful bookkeeping when the system exchanges heat with its environment.

You can predict the sign of entropy change (ΔS) qualitatively in many cases. Processes that increase the number of particles, increase volume, increase temperature, or change from solid to liquid to gas all tend to increase entropy. Conversely, processes that reduce particle count, compress gases, or form ordered crystals decrease the system's entropy. These qualitative predictions become quantitatively powerful when combined with enthalpy through the Gibbs free energy equation (ΔG = ΔH − TΔS), which you will encounter next — the framework that finally unifies the energy and entropy perspectives into a single criterion for spontaneity.

---
id: photochemical-processes-excited-states
title: Photochemistry and Photochemical Reaction Pathways
domain: chemistry
course: physical-chemistry
prerequisites:
- id: electronic-transitions-excited-states
  type: hard
- id: activation-energy-catalysis-reaction-pathways
  type: soft
tags:
- photochemistry
- photons
- excited-states
- reactions
stage: advanced
status: draft
---

# Photochemistry and Photochemical Reaction Pathways

## Core Idea
Photochemical reactions are initiated when molecules absorb photons and reach excited electronic states with different chemical properties than ground states. Excited states can undergo unimolecular decomposition, bimolecular reactions, or isomerization with rate constants often orders of magnitude different from ground state. Key photochemical processes include photosynthesis, vision, photopolymerization, and atmospheric chemistry. Understanding excited state reactivity requires knowledge of potential energy surfaces and radiationless decay pathways.

## Explainer

From your study of electronic transitions, you know that a molecule can absorb a photon and jump from its ground electronic state to an excited state. In photochemistry, the key insight is that this excited molecule is effectively a *different chemical species* — it has a different electron configuration, different bond strengths, and different reactivity. A molecule that is perfectly stable in its ground state may spontaneously break apart, rearrange, or react with neighbors once it absorbs a photon. This is why photochemistry opens reaction pathways that thermal chemistry cannot access.

The fate of an excited molecule is governed by a competition between several processes. **Radiative decay** returns the molecule to the ground state by emitting a photon (fluorescence from singlet states, phosphorescence from triplet states). **Internal conversion** and **intersystem crossing** are radiationless transitions that dissipate electronic energy as heat or transfer the molecule between singlet and triplet manifolds. **Photochemical reaction** occurs when the excited state follows a pathway on its potential energy surface that leads to bond breaking, bond formation, or isomerization before the molecule can relax back down. The Jablonski diagram organizes all of these competing pathways and their typical timescales — fluorescence happens in nanoseconds, phosphorescence in milliseconds to seconds, and photochemical reactions can occur on femtosecond to microsecond timescales depending on the barrier heights involved.

Two foundational laws frame all photochemistry. The **Grotthuss-Draper law** states that only absorbed light can cause a chemical change — photons that pass through or scatter off a sample do nothing. The **Stark-Einstein law** (the law of photochemical equivalence) states that each molecule that undergoes a photochemical primary process absorbs exactly one photon. The **quantum yield** then measures efficiency: it is the number of molecules that undergo a particular process divided by the number of photons absorbed. Quantum yields can exceed 1.0 for chain reactions (where one photon-initiated radical triggers many subsequent thermal reactions) but the primary photochemical step itself consumes exactly one photon per molecule.

Consider a concrete example: the photodissociation of ozone in the atmosphere. An O₃ molecule absorbs an ultraviolet photon, reaching an excited state where the O–O bond is dramatically weakened compared to the ground state. The excited molecule slides along a repulsive potential energy surface and dissociates into O₂ and an oxygen atom — a reaction that would require enormous thermal energy but happens readily with UV light. This single process is responsible for the protective function of the ozone layer. Similar logic applies to vision (photoisomerization of retinal), photosynthesis (charge separation in chlorophyll), and photopolymerization (radical generation from photoinitiators). In each case, the photon provides not just energy but *access to an entirely different potential energy surface* where new chemistry becomes possible.

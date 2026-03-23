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
status: validated
---

# Photochemistry and Photochemical Reaction Pathways

## Core Idea
Photochemical reactions are initiated when molecules absorb photons and reach excited electronic states with different chemical properties than ground states. Excited states can undergo unimolecular decomposition, bimolecular reactions, or isomerization with rate constants often orders of magnitude different from ground state. Key photochemical processes include photosynthesis, vision, photopolymerization, and atmospheric chemistry. Understanding excited state reactivity requires knowledge of potential energy surfaces and radiationless decay pathways.

## Questions

```yaml
- question: "A molecule is chemically stable at high temperatures but decomposes rapidly when irradiated with UV light of the appropriate wavelength. What is the best explanation?"
  type: multiple-choice
  options:
    - "UV light delivers more total energy than thermal heating can at those temperatures"
    - "Absorption of a photon places the molecule on an excited-state potential energy surface where decomposition proceeds without a barrier"
    - "UV photons mechanically break covalent bonds by direct impact"
    - "UV irradiation raises the local temperature of individual molecules beyond the thermal decomposition threshold"
  answer: 1
  explanation: "The key insight is that excited states are different chemical species on different potential energy surfaces — not just 'hotter' ground-state molecules. The ground-state molecule is stable because its potential energy surface has a high barrier to decomposition. After absorbing a photon, the molecule is on an excited-state surface where the bond may be repulsive with no barrier, allowing immediate dissociation. Thermal chemistry cannot access this pathway regardless of temperature, because heating only moves molecules along the ground-state surface."

- question: "The quantum yield of a photochemical chain reaction is measured as 1,000. What does this mean?"
  type: multiple-choice
  options:
    - "Each molecule absorbs 1,000 photons before reacting"
    - "One absorbed photon initiates a radical chain reaction in which 1,000 product molecules are ultimately formed"
    - "The measurement overcounts photon absorption by a factor of 1,000 due to scattering"
    - "The reaction rate is 1,000 times faster than predicted from activation energy alone"
  answer: 1
  explanation: "Quantum yield = (number of molecules undergoing a process) / (number of photons absorbed). A value greater than 1.0 is possible only for chain reactions: the primary photochemical step consumes exactly one photon per molecule (Stark-Einstein law), but that one event can initiate a cascade of thermal chain reactions. Quantum yields in the hundreds to thousands are observed in photoinitiated radical chain reactions like HCl synthesis from H₂ and Cl₂."

- question: "According to the Stark-Einstein law, the primary photochemical step requires exactly one photon per molecule that undergoes the primary process."
  type: true-false
  answer: true
  explanation: "The law of photochemical equivalence states that each molecule activated in the primary photochemical step absorbs exactly one photon. This is consistent with the quantization of light: a single electronic transition is triggered by a single photon. Quantum yields above 1.0 arise from secondary thermal reactions downstream of the primary event, not from multi-photon absorption in the primary step (which requires extremely high light intensity and is a separate phenomenon)."

- question: "A photochemical reaction and a thermal reaction that produce the same product must proceed through the same transition state."
  type: true-false
  answer: false
  explanation: "Photochemical reactions access excited-state potential energy surfaces that thermal reactions cannot reach. The pathways, transition states, and intermediates are fundamentally different. For example, photochemical and thermal cycloadditions follow opposite stereochemical rules (Woodward-Hoffmann rules), precisely because they proceed via different electronic surfaces. Producing the same final product does not mean the same route was taken."

- question: "Why can a photon sometimes enable a chemical reaction that high temperatures cannot bring about, even when the thermal energy available would be comparable in magnitude?"
  type: short-answer
  answer: "Temperature determines the energy distribution of molecules on the ground-state potential energy surface. No matter how high the temperature, molecules remain on that same surface — they simply have more kinetic energy along it. A photon does something different: it promotes the molecule to a completely different excited-state potential energy surface where the bonding structure, barrier heights, and reaction pathways are entirely different. A reaction that has a prohibitive barrier on the ground-state surface may have no barrier at all on the excited-state surface, making the reaction spontaneous once the photon is absorbed."
  explanation: "This is the core insight of photochemistry: photons provide access to new potential energy surfaces, not just more energy on the old one. The ozone photodissociation example illustrates it clearly — O₃ is thermally stable but photodissociates readily under UV because the excited state lands on a repulsive surface with no barrier to dissociation. Heating O₃ does not achieve the same result because the ground-state surface has a significant dissociation barrier."
```

## Explainer

From your study of electronic transitions, you know that a molecule can absorb a photon and jump from its ground electronic state to an excited state. In photochemistry, the key insight is that this excited molecule is effectively a *different chemical species* — it has a different electron configuration, different bond strengths, and different reactivity. A molecule that is perfectly stable in its ground state may spontaneously break apart, rearrange, or react with neighbors once it absorbs a photon. This is why photochemistry opens reaction pathways that thermal chemistry cannot access.

The fate of an excited molecule is governed by a competition between several processes. **Radiative decay** returns the molecule to the ground state by emitting a photon (fluorescence from singlet states, phosphorescence from triplet states). **Internal conversion** and **intersystem crossing** are radiationless transitions that dissipate electronic energy as heat or transfer the molecule between singlet and triplet manifolds. **Photochemical reaction** occurs when the excited state follows a pathway on its potential energy surface that leads to bond breaking, bond formation, or isomerization before the molecule can relax back down. The Jablonski diagram organizes all of these competing pathways and their typical timescales — fluorescence happens in nanoseconds, phosphorescence in milliseconds to seconds, and photochemical reactions can occur on femtosecond to microsecond timescales depending on the barrier heights involved.

Two foundational laws frame all photochemistry. The **Grotthuss-Draper law** states that only absorbed light can cause a chemical change — photons that pass through or scatter off a sample do nothing. The **Stark-Einstein law** (the law of photochemical equivalence) states that each molecule that undergoes a photochemical primary process absorbs exactly one photon. The **quantum yield** then measures efficiency: it is the number of molecules that undergo a particular process divided by the number of photons absorbed. Quantum yields can exceed 1.0 for chain reactions (where one photon-initiated radical triggers many subsequent thermal reactions) but the primary photochemical step itself consumes exactly one photon per molecule.

Consider a concrete example: the photodissociation of ozone in the atmosphere. An O₃ molecule absorbs an ultraviolet photon, reaching an excited state where the O–O bond is dramatically weakened compared to the ground state. The excited molecule slides along a repulsive potential energy surface and dissociates into O₂ and an oxygen atom — a reaction that would require enormous thermal energy but happens readily with UV light. This single process is responsible for the protective function of the ozone layer. Similar logic applies to vision (photoisomerization of retinal), photosynthesis (charge separation in chlorophyll), and photopolymerization (radical generation from photoinitiators). In each case, the photon provides not just energy but *access to an entirely different potential energy surface* where new chemistry becomes possible.

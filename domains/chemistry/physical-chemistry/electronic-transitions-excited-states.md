---
id: electronic-transitions-excited-states
title: Electronic Transitions and Excited State Behavior
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-spectroscopy-selection-rules
  type: hard
- id: energy-level-transitions
  type: hard
builds-toward:
- photochemical-processes-excited-states
tags:
- electronic
- excitation
- absorption
- emission
stage: advanced
status: draft
---

# Electronic Transitions and Excited State Behavior

## Core Idea
When molecules absorb photons, electrons transition from lower to higher energy levels, creating excited states with different electronic configurations. Excited states have different geometries, polarities, and chemical reactivity compared to ground states. Relaxation occurs through radiative (fluorescence, phosphorescence) or non-radiative (internal conversion, intersystem crossing) pathways. Understanding excited state dynamics is essential for photochemistry, photosynthesis, and photovoltaics.

## Explainer

From your study of energy level transitions and selection rules, you know that molecules absorb light only at specific wavelengths corresponding to energy differences between quantized levels, and that selection rules determine which transitions are allowed. Electronic transitions extend this framework to the highest-energy absorptions a molecule can undergo: an electron is promoted from one molecular orbital to another, fundamentally changing the molecule's electronic configuration. The most common transition is **HOMO → LUMO**, which requires the least energy and determines the absorption onset in UV-Vis spectroscopy.

What makes electronic transitions conceptually different from vibrational or rotational transitions is that the excited state is effectively a **different molecule**. When an electron is promoted from a bonding or non-bonding orbital into an antibonding orbital, the electron density distribution changes — bonds may lengthen or shorten, the dipole moment may shift, and the molecule may adopt a completely different equilibrium geometry. For example, formaldehyde's n→π* transition removes electron density from an oxygen lone pair and places it into a C=O antibonding orbital, weakening the C=O bond and making the molecule bend out of plane. The excited state is more reactive than the ground state precisely because its electronic structure is different.

Once a molecule reaches an excited state, it must eventually return to the ground state, and the pathway it takes determines what you observe experimentally. The **Jablonski diagram** maps these pathways. Absorption is nearly instantaneous (~10⁻¹⁵ s). The excited molecule typically relaxes first by **vibrational relaxation** within the same electronic state (losing energy as heat to the solvent, ~10⁻¹² s). From the lowest vibrational level of the excited state, it can emit a photon and drop back to the ground state — this is **fluorescence** (~10⁻⁹ to 10⁻⁷ s). Alternatively, **internal conversion** provides a non-radiative path between states of the same spin multiplicity, and **intersystem crossing** is the non-radiative jump between states of different spin (typically singlet → triplet).

The triplet state deserves special attention. In the ground state, most organic molecules are singlets (all electrons paired). The first excited singlet state S₁ can undergo intersystem crossing to the first excited triplet state T₁, where the promoted electron has flipped its spin. Because the T₁ → S₀ transition is spin-forbidden, the triplet state is long-lived (microseconds to seconds). Emission from this state is called **phosphorescence**, and it occurs at longer wavelengths than fluorescence because T₁ is lower in energy than S₁. The long lifetime of triplet states makes them central to photochemistry — they live long enough to undergo bimolecular reactions, energy transfer, and electron transfer that drive processes from photosynthesis to organic photovoltaics. Understanding the competition between radiative and non-radiative pathways — and how molecular structure, solvent, and temperature influence each rate — is the key to designing fluorescent probes, photocatalysts, and light-harvesting systems.

---
id: inorganic-photochemistry
title: Inorganic Photochemistry
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: electron-transfer-reactions
  type: hard
- id: color-spectroscopy-coordination-compounds
  type: hard
builds-toward: []
tags:
- photochemistry
- excited states
- charge transfer
- luminescence
- photocatalysis
- solar energy
stage: expert
status: validated
---

# Inorganic Photochemistry

## Core Idea
Inorganic photochemistry studies the reactions and properties of coordination compounds in electronically excited states. Light absorption promotes electrons to higher-energy orbitals, creating species with dramatically different redox potentials, bond strengths, and reactivities compared to their ground states. The excited-state properties of Ru(bipy)₃²⁺ and related complexes form the basis for photocatalysis, dye-sensitized solar cells, photodynamic therapy, and artificial photosynthesis.

## Questions

```yaml
- question: "[Ru(bipy)₃]²⁺ absorbs visible light and produces a long-lived excited state (τ ≈ 600 ns). This excited state is both a better oxidant AND a better reductant than the ground state. How is this possible?"
  type: multiple-choice
  options:
    - "The excited state has more electrons available for donation and acceptance simultaneously"
    - "Light absorption creates an MLCT excited state where an electron has been promoted from a metal-based orbital to a ligand-based orbital — the metal center is now effectively Ru(III) (a better oxidant) while the ligand carries an extra electron (a better reductant)"
    - "The excited state simply has more energy, which makes all reactions more favorable"
    - "Spin-orbit coupling in the excited state changes the selection rules for redox reactions"
  answer: 1
  explanation: "The MLCT (metal-to-ligand charge transfer) excited state of [Ru(bipy)₃]²⁺ is best described as [Ru³⁺(bipy)₂(bipy⁻)]²⁺* — one electron has moved from a metal d-orbital to a bipy π* orbital. The metal center, now effectively Ru(III), is electron-poor and a good oxidant (it wants to gain an electron to return to Ru(II)). The reduced bipyridine ligand is electron-rich and a good reductant (it wants to lose its extra electron). The excited state stores ~2.1 eV of energy, which provides the thermodynamic driving force for redox reactions that the ground state cannot achieve."

- question: "The Marcus inverted region is particularly relevant in inorganic photochemistry because excited-state electron transfer reactions often have very large driving forces."
  type: true-false
  answer: true
  explanation: "Excited states store substantial energy (1-3 eV for visible-light absorbers). This energy is available as thermodynamic driving force for electron transfer. When the driving force |ΔG°| exceeds the reorganization energy λ, Marcus theory predicts the reaction enters the inverted region — the rate actually decreases with increasing driving force. In photochemical systems, where |ΔG°| can easily reach 1-2 eV, the inverted region is frequently encountered. This has practical consequences for solar energy conversion: the rate of wasteful charge recombination (which has a large driving force) can be slowed by designing systems where recombination falls in the Marcus inverted region."

- question: "Phosphorescence in inorganic complexes involves emission from a triplet excited state and is typically longer-lived than fluorescence because the transition to the singlet ground state is spin-forbidden."
  type: true-false
  answer: true
  explanation: "In heavy-metal complexes like Ru²⁺, Ir³⁺, and Os²⁺, strong spin-orbit coupling facilitates intersystem crossing from the initially formed singlet excited state to a lower-energy triplet state. Emission from this triplet state (phosphorescence) is formally spin-forbidden (triplet → singlet), making it slow (microsecond to millisecond lifetimes) compared to fluorescence (nanosecond). However, the same spin-orbit coupling that enables intersystem crossing also partially relaxes the spin-selection rule for emission, making phosphorescence observable (though still slower than fluorescence). The long lifetime of the triplet state is advantageous for photochemistry because it provides time for bimolecular reactions to occur."

- question: "Explain how [Ru(bipy)₃]²⁺ can be used as a photocatalyst for water splitting, describing the role of sacrificial reagents and the connection to artificial photosynthesis."
  type: short-answer
  answer: "Upon visible light absorption, [Ru(bipy)₃]²⁺ enters the ³MLCT excited state with E° ≈ −0.86 V (as a reductant) and +0.84 V (as an oxidant). For water oxidation: the excited Ru²⁺* oxidizes water (with a catalyst like IrO₂ to lower the kinetic barrier), generating O₂ and H⁺ while being reduced to Ru⁺. A sacrificial oxidant regenerates Ru²⁺. For hydrogen evolution: the excited Ru²⁺* transfers an electron to a proton-reduction catalyst (like colloidal Pt), generating H₂, while a sacrificial reductant regenerates Ru²⁺. In a complete artificial photosynthesis system, both half-reactions run simultaneously without sacrificial reagents — but this requires solving the challenging problem of coupling the oxidative and reductive cycles through a common intermediate."
  explanation: "This approach mimics natural photosynthesis, where chlorophyll absorbs light and drives charge separation that powers water oxidation (O₂ evolution) and CO₂ reduction. Replacing chlorophyll with more robust synthetic photosensitizers like Ru and Ir complexes is a major research direction in sustainable energy."
```

## Explainer

Most coordination chemistry concerns ground-state properties — structures, spectra, and reactivity under thermal conditions. Photochemistry adds a new dimension by creating excited-state species with fundamentally different electronic configurations. A photon of visible light carries 1.5-3 eV of energy — comparable to the strength of chemical bonds. Depositing this energy into a coordination compound through light absorption creates an excited state that can drive reactions thermodynamically impossible for the ground state.

The prototypical inorganic photosensitizer is [Ru(bipy)₃]²⁺. Ground-state Ru(II) absorbs visible light (λ_max ≈ 450 nm), promoting an electron from a metal-based t₂g orbital to a bipyridine π* orbital — a metal-to-ligand charge transfer (MLCT) transition. Rapid intersystem crossing (facilitated by the heavy ruthenium atom's strong spin-orbit coupling) produces a triplet MLCT state with a remarkably long lifetime (~600 ns in water). This excited state stores 2.1 eV of energy and is simultaneously a better oxidant (by 2.1 V) and a better reductant (by 2.1 V) than the ground state. It can therefore initiate both oxidative and reductive electron transfer reactions that the ground state cannot drive.

The long excited-state lifetime of Ru(bipy)₃²⁺ and its relatives (Ir(ppy)₃, Os(bipy)₃²⁺) is the key to their photochemical utility. A nanosecond fluorescent lifetime is too short for most bimolecular reactions in solution — the excited molecule decays before encountering a reaction partner. The microsecond phosphorescent lifetimes of heavy-metal complexes provide ample time for diffusion-controlled bimolecular quenching. This is why transition metal photosensitizers have largely displaced organic dyes in photocatalysis research.

Applications span energy, medicine, and synthesis. In dye-sensitized solar cells (Gratzel cells), ruthenium complexes absorb sunlight and inject electrons into a TiO₂ semiconductor, generating electricity. In artificial photosynthesis, the same complexes drive water splitting into H₂ and O₂ — the holy grail of solar fuel production. In photodynamic therapy, Ru and Ir complexes generate reactive oxygen species upon light activation, selectively destroying cancer cells. In photoredox catalysis (a revolution in organic synthesis over the past decade), Ir(ppy)₃ and Ru(bipy)₃²⁺ replace harsh stoichiometric oxidants and reductants with catalytic amounts of a photosensitizer activated by visible light. Each application exploits the same fundamental property: the excited-state redox potential differs dramatically from the ground state.

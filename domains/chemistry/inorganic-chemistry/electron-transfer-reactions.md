---
id: electron-transfer-reactions
title: Electron Transfer Reactions (Inner and Outer Sphere)
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: reaction-mechanisms-coordination-compounds
  type: hard
- id: electrochemical-cells
  type: soft
- id: oxidation-reduction-reactions
  type: soft
builds-toward:
- bioinorganic-chemistry-metalloenzymes
- inorganic-photochemistry
tags:
- inner sphere
- outer sphere
- Marcus theory
- electron transfer
- Taube
stage: advanced
status: validated
---

# Electron Transfer Reactions (Inner and Outer Sphere)

## Core Idea
Electron transfer between metal complexes proceeds by two fundamentally different mechanisms. In outer-sphere transfer, the coordination shells of both metal ions remain intact — the electron tunnels through the ligand shells without any bridging ligand being shared. In inner-sphere transfer (the Taube mechanism), a bridging ligand connects the two metal centers, creating a direct pathway for electron flow. Marcus theory provides the quantitative framework for outer-sphere reactions, predicting rates from thermodynamic driving forces and reorganization energies.

## Questions

```yaml
- question: "In Taube's classic experiment, [Co(NH₃)₅Cl]²⁺ + [Cr(H₂O)₆]²⁺ → [Co(H₂O)₆]²⁺ + [Cr(H₂O)₅Cl]²⁺, the chloride transfers from cobalt to chromium. This proves the reaction proceeds by an inner-sphere mechanism. Why?"
  type: multiple-choice
  options:
    - "Because electron transfer always requires direct orbital overlap between two metal centers"
    - "Because the chloride bridges both metals in the transition state, mediating electron transfer, and ends up on chromium — which is possible only if chloride was simultaneously bonded to both metals during the reaction"
    - "Because outer-sphere reactions cannot involve any ligand changes"
    - "Because Co(III) and Cr(II) are both inert complexes that cannot exchange ligands without a bridging mechanism"
  answer: 1
  explanation: "The key evidence is the transfer of the chloride ligand from Co to Cr. In an outer-sphere mechanism, coordination shells remain intact — no ligand transfer would occur. The fact that Cl⁻ moves from one metal to another proves it must have been simultaneously bonded to both (bridging) during the electron transfer step. The precursor complex [Co-Cl-Cr] forms first, electron transfer occurs through the bridging Cl⁻, and then the successor complex dissociates with Cl⁻ remaining on Cr³⁺ (which is now inert due to its d³ configuration). This was Henry Taube's Nobel Prize-winning demonstration of the inner-sphere mechanism."

- question: "Marcus theory predicts that the rate of outer-sphere electron transfer depends on both the thermodynamic driving force (ΔG°) and the reorganization energy (λ). Increasing |ΔG°| always increases the rate."
  type: true-false
  answer: false
  explanation: "Marcus theory predicts that the rate increases as |ΔG°| increases — but only up to a point. When |ΔG°| exceeds the reorganization energy λ, the rate actually decreases. This counterintuitive prediction (the 'Marcus inverted region') occurs because the reaction coordinate and product energy surfaces intersect at progressively higher points when the driving force is too large. The inverted region was controversial when first predicted but has been experimentally confirmed, particularly in photochemical and biological electron transfer systems. For most ground-state inorganic reactions, |ΔG°| < λ and the rate does increase with driving force — the inverted region is more relevant in photoinduced processes."

- question: "In outer-sphere electron transfer, the rate depends on the reorganization energy λ, which includes both inner-sphere (bond length changes) and outer-sphere (solvent reorganization) contributions."
  type: true-false
  answer: true
  explanation: "Reorganization energy λ is the energy cost of distorting the reactant geometry to match the product geometry without actually transferring the electron. The inner-sphere component (λ_inner) reflects changes in metal-ligand bond lengths — for example, Fe²⁺ has longer Fe-O bonds than Fe³⁺, so the [Fe(H₂O)₆]²⁺/³⁺ self-exchange requires bond compression/extension. The outer-sphere component (λ_outer) reflects solvent reorientation — polar solvent molecules must reorganize around the changed charges. Both contribute to the activation barrier. Self-exchange reactions with small geometry changes (like [Ru(bipy)₃]²⁺/³⁺, where the rigid ligands minimize structural change) have small λ and fast rates."

- question: "Explain why the [Fe(H₂O)₆]²⁺/³⁺ self-exchange reaction is much slower than the [Fe(phen)₃]²⁺/³⁺ self-exchange reaction, despite involving the same metal couple."
  type: short-answer
  answer: "The rate difference arises from the reorganization energy λ. In [Fe(H₂O)₆]²⁺/³⁺, the Fe-O bond lengths change significantly between oxidation states (Fe²⁺ has longer bonds than Fe³⁺), contributing a large inner-sphere reorganization energy. The aqua complex also has small, labile ligands that allow substantial solvent access and a large outer-sphere reorganization term. In [Fe(phen)₃]²⁺/³⁺, the rigid phenanthroline ligands constrain the metal-ligand geometry, minimizing bond length changes between oxidation states (small λ_inner). The large aromatic ligands also shield the metal from solvent, reducing λ_outer. The combined effect gives [Fe(phen)₃] a much smaller total λ, lower activation barrier, and faster self-exchange rate."
  explanation: "This example illustrates a design principle for efficient electron transfer: minimize reorganization energy by using rigid ligands that accommodate both oxidation states with minimal structural change. Nature exploits this in electron transfer proteins, where the protein environment tunes λ for efficient electron flow."
```

## Explainer

Redox reactions between metal complexes are fundamental to chemistry and biology — from rusting to cellular respiration to photosynthesis. Unlike simple ion-electron reactions at electrodes, solution-phase electron transfer between two metal complexes must overcome the challenge of moving an electron between two separate coordination shells. The two mechanisms for achieving this — outer-sphere and inner-sphere transfer — represent fundamentally different solutions to this problem.

In outer-sphere electron transfer, the two complexes approach each other closely but their coordination shells remain intact. The electron tunnels from one metal through the intervening ligand shells to the other metal without any ligand being shared or transferred. This mechanism is identified experimentally by the absence of ligand transfer between the two metals and by rates that are consistent with Marcus theory predictions. The quintessential example is the [Fe(CN)₆]⁴⁻/[IrCl₆]²⁻ reaction, where no cyanide or chloride is transferred, and both product complexes retain their original ligand sets.

In inner-sphere electron transfer (Taube's mechanism), a bridging ligand connects the two metal centers, creating a direct orbital pathway for electron flow. The sequence is: formation of a precursor complex with a bridging ligand, electron transfer through the bridge, and dissociation of the successor complex. Taube's classic experiment with [Co(NH₃)₅Cl]²⁺ and [Cr(H₂O)₆]²⁺ proved this mechanism definitively: the chloride transferred from cobalt to chromium, which is impossible unless chloride bridged both metals simultaneously. Good bridging ligands (Cl⁻, N₃⁻, NCS⁻) have lone pairs on multiple atoms that can coordinate to two metals at once.

Marcus theory provides the quantitative framework for outer-sphere rates. The key insight is that before the electron can transfer, the nuclear coordinates of both reactant and solvent must reorganize to a configuration where the electron can move without violating energy conservation (the Franck-Condon principle). The reorganization energy λ measures this distortion cost, and the Marcus equation relates the rate to both λ and the thermodynamic driving force ΔG°. When the driving force is moderate, increasing it accelerates the reaction. But when the driving force exceeds λ, the theory predicts a rate decrease — the Marcus inverted region — a counterintuitive prediction that took decades to confirm experimentally and won Marcus the Nobel Prize.

---
id: mass-spectrometry-fragmentation-analysis
title: 'Mass Spectrometry: Fragmentation Patterns and Structure Elucidation'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: mass-spectrometry-organic
  type: hard
- id: ion-formation-from-electron-transfer
  type: soft
tags:
- mass-spectrometry
- fragmentation
- ion
- analysis
stage: advanced
status: draft
---

# Mass Spectrometry: Fragmentation Patterns and Structure Elucidation

## Core Idea
Mass spectrometry ionizes molecules and measures mass-to-charge ratios of resulting fragments. Fragmentation patterns reflect molecular structure and bonding through preferential cleavage at weak bonds. The molecular ion peak (M⁺) provides molecular weight; fragment peaks reveal functional groups and connectivity. Understanding fragmentation mechanisms allows prediction of MS patterns and vice versa—structure determination from spectra.

## Explainer

From your earlier study of mass spectrometry, you know the basic workflow: molecules are ionized (typically by electron impact, EI), the resulting ions are separated by mass-to-charge ratio (m/z), and a detector records the abundance of each m/z value. The spectrum is a bar graph of relative abundance versus m/z. The **molecular ion peak** (M⁺•) — formed when the molecule loses one electron without breaking any bonds — gives you the molecular weight directly. But the real structural information lies in how the molecular ion breaks apart.

**Fragmentation** occurs because the molecular ion has excess internal energy from the ionization process. This energy redistributes through the molecule's vibrational modes, and bonds break at the weakest points. The resulting fragment ions are detected (neutral fragments are not), and their m/z values tell you the masses of the pieces. The key analytical tool is the **mass difference**: if you see the molecular ion at m/z 120 and a prominent fragment at m/z 105, the difference of 15 mass units corresponds to loss of a CH₃ group. Common neutral losses are diagnostic: loss of 18 = H₂O (alcohols, carboxylic acids), loss of 28 = CO (carbonyls, phenols) or C₂H₄ (ethyl groups), loss of 31 = OCH₃ (methyl esters), loss of 45 = OC₂H₅ (ethyl esters).

The fragmentation of a molecule follows predictable rules rooted in thermodynamic stability and radical cation chemistry. **Alpha-cleavage** (cleavage of the bond adjacent to the radical cation site) is the most common mechanism — it produces a resonance-stabilized cation. For example, ketones fragment by alpha-cleavage on either side of the carbonyl, producing acylium ions (RC≡O⁺, which appear as strong peaks). **McLafferty rearrangement** is a six-membered transition state process where a gamma hydrogen transfers to the radical cation site with simultaneous beta-cleavage, producing a neutral alkene and a radical cation fragment. This rearrangement is diagnostic for carbonyl compounds with a gamma hydrogen and produces characteristic even-mass fragments from odd-mass molecular ions.

The **nitrogen rule** is a powerful shortcut: molecules with an even number of nitrogen atoms (including zero) have even molecular weights, while those with an odd number have odd molecular weights. This applies to molecular ions and can help you decide whether a fragment has retained or lost a nitrogen atom. Similarly, the **isotope pattern** at the molecular ion reveals elements like chlorine (M and M+2 in roughly 3:1 ratio) and bromine (M and M+2 in roughly 1:1 ratio).

Putting this together, structure elucidation from a mass spectrum proceeds as follows: (1) identify the molecular ion and determine the molecular weight; (2) check the isotope pattern for halogens and the nitrogen rule; (3) identify major fragment ions and calculate mass losses; (4) match losses and fragment masses to known functional group signatures; (5) propose candidate structures and verify that they predict the observed fragmentation. With practice, you begin to read a mass spectrum almost like a structural formula — each peak is a piece of the molecule, and the pattern of losses maps its connectivity.

---
id: molecular-spectroscopy-structure-determination
title: Molecular Spectroscopy for Structure Determination
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: uv-vis-spectroscopy-analytical
  type: hard
- id: ir-spectroscopy-analytical
  type: hard
- id: nmr-spectroscopy-analytical
  type: hard
- id: structure-elucidation-using-ir-nmr-and-ms
  type: soft
tags:
- structure elucidation
- spectroscopy
- IR
- NMR
- UV-Vis
stage: advanced
status: validated
---

# Molecular Spectroscopy for Structure Determination

## Core Idea
Combined IR, NMR, and UV-Vis spectroscopy enables unambiguous structural determination of organic compounds through functional group identification, connectivity mapping, and confirmation of conjugation and aromatic character.

## Questions

```yaml
- question: "A compound shows a strong C=O stretch at 1715 cm⁻¹ in IR and a singlet at ~9.5 ppm in ¹H NMR. Which structural feature do these two observations together establish?"
  type: multiple-choice
  options:
    - "An ester functional group, because the carbonyl stretch and the singlet indicate O-C=O"
    - "A ketone flanked by two alkyl groups, because 1715 cm⁻¹ is the classic ketone carbonyl"
    - "An aldehyde (CHO group), because the ~9.5 ppm singlet is the diagnostic aldehyde C–H signal"
    - "A carboxylic acid, because the broad O–H and the carbonyl together indicate COOH"
  answer: 2
  explanation: "Both ketones and aldehydes absorb near 1715 cm⁻¹, so IR alone cannot distinguish them. The ~9.5 ppm singlet in ¹H NMR is the definitive aldehyde C–H signal, which is absent in ketones (which have no H on the carbonyl carbon). This is a classic example of why combining techniques is essential: IR narrowed the candidates to carbonyl-containing compounds, and NMR resolved the ambiguity."

- question: "A compound shows no significant UV-Vis absorption above 220 nm. What can be concluded about its electronic structure?"
  type: multiple-choice
  options:
    - "It likely contains an extended conjugated π system spanning several double bonds"
    - "It must contain an aromatic ring with strong electron-withdrawing substituents"
    - "It contains little or no conjugation — probably only isolated double bonds or fully saturated bonds"
    - "It is a protein, since the absence of UV absorption is characteristic of biological macromolecules"
  answer: 2
  explanation: "Extended conjugation (multiple conjugated double bonds, aromatic rings, carbonyl-alkene systems) shifts UV absorption to longer wavelengths and higher intensities. Absorption only below 220 nm is characteristic of molecules with no significant conjugation — isolated C=C bonds absorb around 170–190 nm (often inaccessible in solution), and saturated bonds absorb even further into the vacuum UV. The absence of absorption above 220 nm essentially rules out extended π systems."

- question: "UV-Vis spectroscopy can determine the complete connectivity of atoms in an organic molecule."
  type: true-false
  answer: false
  explanation: "UV-Vis reports only on the electronic structure — specifically how electrons are delocalized through conjugated or aromatic systems. It cannot reveal the sequence of atoms, the number of distinct chemical environments, or the arrangement of saturated portions of the molecule. Connectivity mapping requires NMR spectroscopy (through chemical shifts, integration, and coupling patterns). UV-Vis is useful for confirming conjugation and aromatic character, but it is structurally silent about the rest of the molecule."

- question: "IR spectroscopy identifies functional groups by detecting characteristic vibrational frequencies of specific bonds."
  type: true-false
  answer: true
  explanation: "Different types of bonds vibrate at characteristic frequencies because bond strength (force constant) and atomic masses determine the vibrational frequency. A C=O bond vibrates near 1715 cm⁻¹, an O–H near 3200–3550 cm⁻¹, a C–H near 2850–3000 cm⁻¹, and so on. The IR spectrum is essentially a fingerprint of which bond types — and therefore which functional groups — are present in the molecule."

- question: "Why must IR, NMR, and UV-Vis spectroscopy be used together rather than relying on just one technique for unambiguous structure determination?"
  type: short-answer
  answer: "Each technique reveals a different and complementary aspect of molecular structure. IR identifies which functional groups are present (what types of bonds exist) but says little about connectivity. NMR maps the carbon-hydrogen framework — how many distinct environments exist, how many protons are in each, and which atoms are neighbors — but may not uniquely distinguish certain functional groups. UV-Vis reveals the electronic structure (the extent of conjugation and aromatic character) but is silent about saturated parts of the molecule. Only when all three data sets are consistent with a single proposed structure can you be confident in the determination."
  explanation: "The analogy in the Explainer is apt: each spectrum is a witness with partial testimony. IR may tell you a carbonyl is present and NMR may tell you there is no aldehyde proton, together ruling out an aldehyde and supporting a ketone or ester. UV-Vis can then confirm whether that carbonyl is conjugated with a double bond (an enone absorbs near 250 nm) or isolated (a simple ketone absorbs weakly near 280 nm). The convergence of all three is what transforms spectroscopic data into a definitive structural assignment."
```

## Explainer

You have already studied IR, NMR, and UV-Vis spectroscopy as individual techniques, each providing a different window into molecular structure. The power of this topic lies in learning to combine all three into a systematic workflow that converges on a single structural answer. Think of it as detective work: each spectrum is a witness providing partial testimony, and your job is to reconcile all the evidence into one consistent story. No single technique is sufficient alone — IR tells you what functional groups are present but not how they connect, NMR tells you about the carbon-hydrogen framework and connectivity but may not distinguish certain functional groups, and UV-Vis reveals conjugation patterns but says little about saturated portions of the molecule.

A practical structure determination typically begins with **IR spectroscopy** because it provides the fastest survey of functional groups. You scan the spectrum looking for diagnostic absorptions: a broad O–H stretch around 2500–3300 cm⁻¹ for carboxylic acids, a sharp C=O stretch near 1715 cm⁻¹ for ketones, N–H stretches around 3300–3500 cm⁻¹ for amines, and so on. This first pass narrows the candidate structures dramatically — knowing whether the compound contains a carbonyl, a hydroxyl, an amine, or an aromatic ring eliminates entire classes of possibilities before you even look at the NMR.

**NMR spectroscopy** then provides the connectivity map. ¹H NMR reveals how many distinct hydrogen environments exist (number of peaks), how many hydrogens are in each environment (integration), and which hydrogens are neighbors (splitting patterns from J-coupling). ¹³C NMR and DEPT experiments distinguish CH₃, CH₂, CH, and quaternary carbons. Two-dimensional experiments like COSY (which hydrogens couple to each other) and HSQC (which hydrogens attach to which carbons) can resolve ambiguities in complex molecules. If IR told you a carbonyl is present, NMR tells you whether it is an aldehyde (with a distinctive ~9.5 ppm ¹H signal), a ketone (no aldehyde proton, flanked by alkyl groups), an ester (with an oxygen-bearing carbon nearby), or an amide.

**UV-Vis spectroscopy** completes the picture by reporting on the electronic structure — specifically, the extent of conjugation and aromatic character. A compound absorbing at 250 nm has a different conjugated system than one absorbing at 350 nm, and the wavelength and intensity of absorption can distinguish between isolated double bonds, extended conjugation, and aromatic rings with various substituents. In practice, UV-Vis often serves as a confirmation step: after IR and NMR have suggested a structure, the UV-Vis absorption maximum should match what you predict for that structure's chromophore. When all three techniques point to the same answer — the functional groups from IR, the connectivity from NMR, and the electronic structure from UV-Vis all consistent with one structure — you have achieved an unambiguous determination.

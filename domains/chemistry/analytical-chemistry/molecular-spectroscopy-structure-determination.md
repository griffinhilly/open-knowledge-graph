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
status: draft
---

# Molecular Spectroscopy for Structure Determination

## Core Idea
Combined IR, NMR, and UV-Vis spectroscopy enables unambiguous structural determination of organic compounds through functional group identification, connectivity mapping, and confirmation of conjugation and aromatic character.

## Explainer

You have already studied IR, NMR, and UV-Vis spectroscopy as individual techniques, each providing a different window into molecular structure. The power of this topic lies in learning to combine all three into a systematic workflow that converges on a single structural answer. Think of it as detective work: each spectrum is a witness providing partial testimony, and your job is to reconcile all the evidence into one consistent story. No single technique is sufficient alone — IR tells you what functional groups are present but not how they connect, NMR tells you about the carbon-hydrogen framework and connectivity but may not distinguish certain functional groups, and UV-Vis reveals conjugation patterns but says little about saturated portions of the molecule.

A practical structure determination typically begins with **IR spectroscopy** because it provides the fastest survey of functional groups. You scan the spectrum looking for diagnostic absorptions: a broad O–H stretch around 2500–3300 cm⁻¹ for carboxylic acids, a sharp C=O stretch near 1715 cm⁻¹ for ketones, N–H stretches around 3300–3500 cm⁻¹ for amines, and so on. This first pass narrows the candidate structures dramatically — knowing whether the compound contains a carbonyl, a hydroxyl, an amine, or an aromatic ring eliminates entire classes of possibilities before you even look at the NMR.

**NMR spectroscopy** then provides the connectivity map. ¹H NMR reveals how many distinct hydrogen environments exist (number of peaks), how many hydrogens are in each environment (integration), and which hydrogens are neighbors (splitting patterns from J-coupling). ¹³C NMR and DEPT experiments distinguish CH₃, CH₂, CH, and quaternary carbons. Two-dimensional experiments like COSY (which hydrogens couple to each other) and HSQC (which hydrogens attach to which carbons) can resolve ambiguities in complex molecules. If IR told you a carbonyl is present, NMR tells you whether it is an aldehyde (with a distinctive ~9.5 ppm ¹H signal), a ketone (no aldehyde proton, flanked by alkyl groups), an ester (with an oxygen-bearing carbon nearby), or an amide.

**UV-Vis spectroscopy** completes the picture by reporting on the electronic structure — specifically, the extent of conjugation and aromatic character. A compound absorbing at 250 nm has a different conjugated system than one absorbing at 350 nm, and the wavelength and intensity of absorption can distinguish between isolated double bonds, extended conjugation, and aromatic rings with various substituents. In practice, UV-Vis often serves as a confirmation step: after IR and NMR have suggested a structure, the UV-Vis absorption maximum should match what you predict for that structure's chromophore. When all three techniques point to the same answer — the functional groups from IR, the connectivity from NMR, and the electronic structure from UV-Vis all consistent with one structure — you have achieved an unambiguous determination.

---
id: ir-spectroscopy-organic
title: 'Infrared Spectroscopy: Functional Group Identification'
domain: chemistry
course: organic-chemistry
prerequisites:
- id: ir-spectroscopy-basics
  type: hard
- id: electromagnetic-waves
  type: soft
- id: electromagnetic-spectrum
  type: soft
- id: wave-properties-intro
  type: soft
builds-toward:
- nmr-spectroscopy-organic
tags:
- ir
- spectroscopy
- functional-groups
- carbonyl
- hydroxyl
- amine
stage: formal-systems
status: draft
---

# Infrared Spectroscopy: Functional Group Identification

## Core Idea
Infrared spectroscopy measures molecular vibrations. Characteristic bands identify functional groups: O-H and N-H stretch at 3200–3600 cm⁻¹, C=O stretch at 1600–1750 cm⁻¹ (position depends on substituents), C=C at 1600–1680 cm⁻¹, and C-H stretches at 2850–3000 cm⁻¹. The fingerprint region (500–1500 cm⁻¹) contains complex absorptions unique to each molecule. IR is best used alongside NMR and MS to determine structure.

## How It's Best Learned
Identify functional group bands on actual IR spectra. Compare carbonyl stretches across different carbonyls (ketone, aldehyde, acid, ester) and note the shifts. Use reference IR correlation tables.

## Common Misconceptions
IR alone cannot determine structure uniquely—different compounds can have overlapping bands. The fingerprint region is not 'unknown'—it contains predictable patterns from substitution and geometry. Hydrogen bonding shifts O-H stretches to lower frequency (broader bands).

## Explainer

From your introduction to IR spectroscopy, you know that infrared light has the right energy to excite molecular vibrations — stretching and bending of bonds. Different bonds absorb at different frequencies because they have different strengths (spring constants) and connect atoms of different masses. The core skill in organic IR interpretation is learning to read a spectrum like a checklist: scan for the presence or absence of characteristic functional group absorptions, and use them to narrow down the structure.

Start at the high-frequency end of the spectrum (around 3500 cm⁻¹) and work downward. A **broad absorption between 3200 and 3600 cm⁻¹** signals O–H or N–H bonds. Alcohol O–H stretches are characteristically broad and rounded due to hydrogen bonding — the more hydrogen bonding, the broader and more shifted to lower frequency. Carboxylic acid O–H is even broader, often spanning 2500–3300 cm⁻¹ as a very wide, flat absorption. N–H stretches (amines and amides) appear in the same region but are sharper: primary amines show two peaks (symmetric and asymmetric stretch), secondary amines show one, and tertiary amines show none. Just below this, **C–H stretches** appear at 2850–3000 cm⁻¹ for sp³ C–H and just above 3000 cm⁻¹ for sp² C–H (alkenes, aromatics) — a quick way to detect unsaturation.

The most diagnostically powerful region is **1600–1800 cm⁻¹**, home of the **carbonyl stretch**. Nearly every carbonyl-containing functional group absorbs here, but each at a slightly different frequency: acid chlorides near 1800 cm⁻¹, anhydrides show two peaks around 1800 and 1760, esters near 1735–1750, carboxylic acids near 1710, ketones near 1715, aldehydes near 1725, and amides near 1650 (lowered by nitrogen lone pair donation into the C=O). Learning these approximate positions lets you distinguish between functional groups that might otherwise look similar. Conjugation with a double bond or aromatic ring lowers the carbonyl frequency by about 20–30 cm⁻¹ because electron delocalization weakens the C=O bond.

Below 1500 cm⁻¹ lies the **fingerprint region**, a complex pattern of C–C, C–O, and C–N stretches plus various bending modes. While individual peaks here are hard to assign, the overall pattern is unique to each molecule — like a fingerprint. In practice, you use the fingerprint region to confirm identity by comparing to a reference spectrum rather than trying to interpret every peak. The practical workflow for structure determination combines IR with other techniques: IR tells you which functional groups are present (or absent), then NMR and mass spectrometry fill in the carbon skeleton and molecular formula. An IR spectrum showing no broad O–H, no carbonyl, and C–H stretches only below 3000 cm⁻¹ immediately tells you the compound is likely a simple alkane or ether — narrowing the possibilities before you even look at the NMR.

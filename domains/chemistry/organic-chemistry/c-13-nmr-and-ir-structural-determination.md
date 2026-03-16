---
id: c-13-nmr-and-ir-structural-determination
title: ¹³C NMR and IR Spectroscopy for Structure Determination
domain: chemistry
course: organic-chemistry
prerequisites:
- id: proton-nmr-interpretation-coupling-patterns
  type: hard
- id: ir-spectroscopy-basics
  type: soft
- id: electromagnetic-waves
  type: soft
builds-toward:
- retrosynthetic-analysis
tags:
- nmr
- carbon-nmr
- ir
- spectroscopy
- structure-determination
stage: formal-systems
status: draft
---

# ¹³C NMR and IR Spectroscopy for Structure Determination

## Core Idea
¹³C NMR reveals the carbon skeleton: the number of peaks indicates the number of unique carbons; chemical shifts reflect environment (aliphatic ~0–50 ppm, aromatic/sp² ~100–150 ppm, carbonyl ~150–220 ppm). DEPT distinguishes CH₃, CH₂, CH, and quaternary carbons. IR spectroscopy identifies functional groups through characteristic absorptions: C=O (1650–1850 cm⁻¹), C-O (1000–1300 cm⁻¹), N-H, O-H, aromatic C=C (1400–1600 cm⁻¹).

## How It's Best Learned
Combine ¹H NMR, ¹³C NMR, and IR data to determine structures. Use molecular formula and degree of unsaturation to guide structure proposals.

## Common Misconceptions
- Over-interpreting exact ¹³C chemical shift values; they are approximate guides and shift with solvent and temperature.
- Using IR alone for functional group assignment without supporting NMR or MS data; IR is most informative when combined with other techniques.

## Explainer

From proton NMR, you learned to read hydrogen environments — chemical shifts, splitting patterns, and integration tell you about the electronic surroundings, neighboring hydrogens, and relative numbers of equivalent protons. **¹³C NMR** does the analogous job for the carbon skeleton. Each chemically distinct carbon in a molecule produces one peak, so the number of peaks immediately tells you how many unique carbon environments exist. A molecule with high symmetry (like para-xylene) will show fewer peaks than its molecular formula might suggest, because symmetry-equivalent carbons give a single signal.

The chemical shift ranges in ¹³C NMR are more spread out than in ¹H NMR (0–220 ppm vs. 0–12 ppm), which makes peaks easier to distinguish. Alkyl carbons (sp³, no electronegative neighbors) appear near 0–50 ppm. Carbons bonded to oxygen or nitrogen shift downfield to 50–100 ppm. Aromatic and alkene carbons (sp²) appear at 100–150 ppm. Carbonyl carbons are the most deshielded, ranging from about 150 ppm (carboxylic acids, esters) to 220 ppm (ketones, aldehydes). The **DEPT experiment** (Distortionless Enhancement by Polarization Transfer) adds another layer: it distinguishes CH₃, CH₂, CH, and quaternary carbons by running the spectrum under different conditions and comparing which peaks point up, down, or vanish.

**IR spectroscopy** complements NMR by identifying functional groups through the frequencies at which bonds vibrate. Each bond type absorbs infrared light at a characteristic frequency — the carbonyl C=O stretch near 1700 cm⁻¹ is one of the strongest and most recognizable absorptions in organic chemistry. A broad O-H stretch between 2500–3300 cm⁻¹ screams "carboxylic acid." A sharp N-H absorption near 3300–3500 cm⁻¹ indicates an amine or amide. The fingerprint region below 1500 cm⁻¹ is unique to each molecule but difficult to interpret peak-by-peak — it is most useful for confirming identity against a reference spectrum rather than for de novo structure determination.

The real power emerges when you combine all three techniques. Start with the molecular formula to calculate the **degree of unsaturation** (also called the index of hydrogen deficiency), which tells you the total number of rings plus double bonds. Then use IR to identify functional groups — is there a carbonyl? An O-H? An N-H? Next, use ¹³C NMR (with DEPT) to count unique carbons and classify them by hybridization and environment. Finally, use your ¹H NMR data for detailed connectivity information — splitting patterns reveal which hydrogens are neighbors, and integration confirms ratios. Each technique constrains the possibilities, and together they typically narrow the structure down to one candidate. This multi-technique approach is the standard workflow for structure determination in organic chemistry, and mastering it prepares you for tackling unknown compounds in both coursework and research.

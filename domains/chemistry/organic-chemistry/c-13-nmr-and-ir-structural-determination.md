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
status: validated
---

# ¹³C NMR and IR Spectroscopy for Structure Determination

## Core Idea
¹³C NMR reveals the carbon skeleton: the number of peaks indicates the number of unique carbons; chemical shifts reflect environment (aliphatic ~0–50 ppm, aromatic/sp² ~100–150 ppm, carbonyl ~150–220 ppm). DEPT distinguishes CH₃, CH₂, CH, and quaternary carbons. IR spectroscopy identifies functional groups through characteristic absorptions: C=O (1650–1850 cm⁻¹), C-O (1000–1300 cm⁻¹), N-H, O-H, aromatic C=C (1400–1600 cm⁻¹).

## How It's Best Learned
Combine ¹H NMR, ¹³C NMR, and IR data to determine structures. Use molecular formula and degree of unsaturation to guide structure proposals.

## Common Misconceptions
- Over-interpreting exact ¹³C chemical shift values; they are approximate guides and shift with solvent and temperature.
- Using IR alone for functional group assignment without supporting NMR or MS data; IR is most informative when combined with other techniques.

## Questions

```yaml
- question: "A compound with molecular formula C₈H₈ gives only 4 peaks in its ¹³C NMR spectrum. What is the most chemically reasonable interpretation?"
  type: multiple-choice
  options:
    - "The instrument malfunctioned — a compound with 8 carbons must produce 8 peaks"
    - "The compound has 4 unique carbon environments; the other 4 carbons are symmetry-equivalent to existing peaks"
    - "Only carbons bearing hydrogen atoms appear in standard ¹³C NMR spectra"
    - "The compound contains 4 carbon-13 atoms and 4 carbon-12 atoms; only ¹³C is detected"
  answer: 1
  explanation: "In ¹³C NMR, each chemically distinct carbon environment produces exactly one peak, but symmetry-equivalent carbons give only one signal. A compound with high symmetry (like styrene or cyclooctatetraene derivatives) can have far fewer peaks than total carbons. The number of peaks tells you the number of unique carbon environments, not the total carbon count. Option C is wrong because quaternary carbons (no attached H) appear in standard ¹³C NMR, though not in DEPT."

- question: "An IR spectrum shows a broad absorption from 2500–3300 cm⁻¹ and a strong carbonyl peak at 1710 cm⁻¹. What functional group is most consistent with both absorptions together?"
  type: multiple-choice
  options:
    - "Ketone — ketone C=O stretches appear near 1715 cm⁻¹ and no other absorptions are needed"
    - "Aldehyde — the broad absorption is the characteristic aldehyde C-H stretch"
    - "Carboxylic acid — the very broad O-H stretch (2500–3300 cm⁻¹) combined with a carbonyl near 1710 cm⁻¹ is diagnostic for -COOH"
    - "Ester — esters show strong carbonyl peaks near 1735 cm⁻¹ and a broad O-H"
  answer: 2
  explanation: "The combination of a very broad O-H stretch from 2500–3300 cm⁻¹ (caused by strong hydrogen bonding in the carboxylic acid dimer) and a C=O stretch near 1710 cm⁻¹ is characteristic of a carboxylic acid. A ketone would lack the broad O-H absorption; an aldehyde would show a distinctive pair of weak C-H stretches near 2720 and 2820 cm⁻¹; an ester C=O would be higher (1735 cm⁻¹) and lacks the O-H stretch."

- question: "Fewer peaks in a ¹³C NMR spectrum generally indicate that a molecule has fewer total carbon atoms."
  type: true-false
  answer: false
  explanation: "The number of ¹³C peaks equals the number of *chemically distinct* carbon environments, not the total carbon count. A highly symmetric molecule like benzene (C₆H₆) gives only one ¹³C peak because all 6 carbons are equivalent. Para-xylene (C₈H₁₀) gives only 4 peaks despite 8 carbons. Fewer peaks mean higher molecular symmetry, not fewer atoms."

- question: "Calculating the degree of unsaturation from the molecular formula before interpreting spectral data is good practice because it constrains what structural features are possible."
  type: true-false
  answer: true
  explanation: "Degree of unsaturation (= rings + double bonds + 2× triple bonds, calculated from the molecular formula) provides an independent structural constraint before any spectral interpretation. If DoU = 4, you know the structure must contain exactly 4 degrees of unsaturation in total — for example, one benzene ring (DoU = 4) accounts for all of them, ruling out additional carbonyl groups or rings. This prevents proposing structures that contradict the molecular formula."

- question: "What additional structural information does DEPT provide that a standard ¹³C NMR spectrum alone cannot, and why is this important for structure determination?"
  type: short-answer
  answer: "Standard ¹³C NMR shows the chemical shift and number of unique carbon environments but cannot distinguish how many hydrogens are attached to each carbon. DEPT uses different pulse angles to create subspectra where CH₃ and CH point upward, CH₂ points downward, and quaternary carbons (C with no H) disappear entirely. This tells you the substitution pattern of each carbon — methyl, methylene, methine, or quaternary — which is essential for assembling the connectivity of the molecule and distinguishing, for example, a CH₂ at 40 ppm from a quaternary C at the same shift."
  explanation: "Without DEPT, you might mistake a quaternary carbon (e.g., a carbon bonded to four other carbons in a ring junction) for a CH group with an unusual chemical shift. This ambiguity frequently leads to incorrect structure proposals. DEPT resolves it directly, making it a standard companion to ¹³C NMR in structure determination."
```

## Explainer

From proton NMR, you learned to read hydrogen environments — chemical shifts, splitting patterns, and integration tell you about the electronic surroundings, neighboring hydrogens, and relative numbers of equivalent protons. **¹³C NMR** does the analogous job for the carbon skeleton. Each chemically distinct carbon in a molecule produces one peak, so the number of peaks immediately tells you how many unique carbon environments exist. A molecule with high symmetry (like para-xylene) will show fewer peaks than its molecular formula might suggest, because symmetry-equivalent carbons give a single signal.

The chemical shift ranges in ¹³C NMR are more spread out than in ¹H NMR (0–220 ppm vs. 0–12 ppm), which makes peaks easier to distinguish. Alkyl carbons (sp³, no electronegative neighbors) appear near 0–50 ppm. Carbons bonded to oxygen or nitrogen shift downfield to 50–100 ppm. Aromatic and alkene carbons (sp²) appear at 100–150 ppm. Carbonyl carbons are the most deshielded, ranging from about 150 ppm (carboxylic acids, esters) to 220 ppm (ketones, aldehydes). The **DEPT experiment** (Distortionless Enhancement by Polarization Transfer) adds another layer: it distinguishes CH₃, CH₂, CH, and quaternary carbons by running the spectrum under different conditions and comparing which peaks point up, down, or vanish.

**IR spectroscopy** complements NMR by identifying functional groups through the frequencies at which bonds vibrate. Each bond type absorbs infrared light at a characteristic frequency — the carbonyl C=O stretch near 1700 cm⁻¹ is one of the strongest and most recognizable absorptions in organic chemistry. A broad O-H stretch between 2500–3300 cm⁻¹ screams "carboxylic acid." A sharp N-H absorption near 3300–3500 cm⁻¹ indicates an amine or amide. The fingerprint region below 1500 cm⁻¹ is unique to each molecule but difficult to interpret peak-by-peak — it is most useful for confirming identity against a reference spectrum rather than for de novo structure determination.

The real power emerges when you combine all three techniques. Start with the molecular formula to calculate the **degree of unsaturation** (also called the index of hydrogen deficiency), which tells you the total number of rings plus double bonds. Then use IR to identify functional groups — is there a carbonyl? An O-H? An N-H? Next, use ¹³C NMR (with DEPT) to count unique carbons and classify them by hybridization and environment. Finally, use your ¹H NMR data for detailed connectivity information — splitting patterns reveal which hydrogens are neighbors, and integration confirms ratios. Each technique constrains the possibilities, and together they typically narrow the structure down to one candidate. This multi-technique approach is the standard workflow for structure determination in organic chemistry, and mastering it prepares you for tackling unknown compounds in both coursework and research.

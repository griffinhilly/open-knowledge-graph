---
id: isotope-dilution
title: Isotope Dilution
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: mass-spectrometry-analytical
  type: hard
- id: internal-standards
  type: soft
tags:
- isotope dilution
- isotope-labeled standard
- IDMS
- equilibration
- definitive method
- high-accuracy quantification
stage: advanced
status: draft
---

# Isotope Dilution

## Core Idea
Isotope dilution mass spectrometry (IDMS) adds a known amount of an isotopically labeled analog of the analyte (e.g., ¹³C-labeled or deuterated) to the sample before any processing, then measures the ratio of labeled to unlabeled species by mass spectrometry. Because the labeled and natural analyte are chemically identical (or nearly so), they experience exactly the same losses during extraction, cleanup, and chromatography, making the measured ratio invariant to recovery. This self-correcting property makes IDMS one of the most accurate quantitative methods available, and it is designated a "definitive method" by metrology organizations for certifying reference materials. The key requirement is complete equilibration of the spike with the native analyte before any separation steps begin.

## How It's Best Learned
Spike a biological sample with a deuterium-labeled internal standard, carry it through a full SPE and LC-MS/MS workflow, and quantify the analyte from the isotope ratio. Then deliberately vary the extraction recovery (e.g., by shortening extraction time) and observe that the final concentration remains accurate despite poor recovery — demonstrating the self-correcting power of the isotope-ratio approach.

## Common Misconceptions
- Isotope dilution does not eliminate all sources of error; if the labeled standard does not fully equilibrate with the native analyte (e.g., the analyte is protein-bound and the spike is free), the ratio will be biased and the result incorrect.
- Deuterium-labeled standards can exhibit slight chromatographic isotope effects (eluting a few seconds earlier than the unlabeled analyte), which can cause differential matrix effects in LC-ESI-MS; ¹³C-labeled standards avoid this issue.

## Explainer

From your study of internal standards, you know the basic idea: add a known compound to your sample early in the workflow so that any losses during sample preparation affect both the analyte and the standard equally, and the ratio between them stays constant. Isotope dilution takes this concept to its theoretical limit. Instead of adding a *similar* compound as an internal standard, you add an **isotopically labeled version of the exact same molecule** — identical in structure, reactivity, and physical behavior, differing only in atomic mass. This makes the correction essentially perfect rather than approximate.

Imagine you are measuring cortisol in a blood plasma sample. You spike in a known amount of cortisol-d4 (four hydrogens replaced with deuterium). When you extract the plasma with organic solvent, both natural cortisol and cortisol-d4 partition into the solvent at exactly the same rate — they have the same polarity, the same hydrogen bonding, the same solubility. If your extraction recovers only 60% of the cortisol, it also recovers exactly 60% of the cortisol-d4. The ratio of natural to labeled cortisol in the extract is therefore identical to the ratio in the original spiked sample. When the mass spectrometer measures this ratio — distinguishing the two by their 4-dalton mass difference — the concentration calculation is independent of recovery. You could recover 30% or 90% and get the same answer.

This **self-correcting property** is what makes IDMS a **definitive method** in metrology — the science of measurement. National metrology institutes like NIST use IDMS to certify the concentration of reference materials because it eliminates the largest source of error in quantitative analysis: variable and incomplete sample recovery. The key requirement is **complete equilibration**: the labeled spike must be thoroughly mixed with the native analyte before any separation step begins. If the native analyte is trapped inside protein aggregates or bound to particulate matter while the spike floats freely in solution, they will not experience the same losses, and the ratio will be biased. Proper equilibration often requires incubation time, vigorous mixing, or even enzymatic digestion to release bound analyte.

The choice of isotope label matters more than it might seem. **Deuterium labels** (²H) are the cheapest and most widely available, but deuterium-for-hydrogen substitution slightly changes the compound's polarity and chromatographic behavior — a phenomenon called the **deuterium isotope effect**. In LC-MS with electrospray ionization, even a one-second difference in retention time between the labeled and unlabeled forms means they experience different matrix ion suppression, undermining the ratio's accuracy. **Carbon-13 labels** (¹³C) avoid this problem entirely because replacing ¹²C with ¹³C changes the mass without altering any bond properties, polarity, or chromatographic retention. For the highest-accuracy work, ¹³C-labeled standards are preferred despite their higher cost.

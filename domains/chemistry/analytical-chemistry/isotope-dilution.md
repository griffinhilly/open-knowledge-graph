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
stage: formal-systems
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

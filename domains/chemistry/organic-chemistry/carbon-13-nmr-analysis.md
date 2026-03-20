---
id: carbon-13-nmr-analysis
title: Carbon-13 NMR Spectroscopy and DEPT
domain: chemistry
course: organic-chemistry
prerequisites:
- id: nmr-spectroscopy-organic
  type: hard
tags:
- carbon-13
- c-nmr
- dept
- quaternary-carbon
- offsets
stage: advanced
status: draft
---

# Carbon-13 NMR Spectroscopy and DEPT

## Core Idea
¹³C NMR directly observes all carbon atoms, with offsets reflecting bonding environment (quaternary carbons are typically more deshielded). DEPT (Distortionless Enhancement by Polarization Transfer) distinguishes carbon types: CH₃ and CH point up; CH₂ points down; quaternary carbons disappear. Since ¹³C has low natural abundance (~1%) and long relaxation times, ¹³C NMR is less sensitive than ¹H NMR but provides direct carbon connectivity and is essential for assigning quaternary carbons.

## Explainer

From your study of ¹H NMR, you know that magnetic nuclei in different electronic environments resonate at different frequencies, producing distinct chemical shifts. **¹³C NMR** applies the same principle directly to carbon atoms. While ¹H NMR tells you about hydrogen environments, ¹³C NMR tells you how many *chemically distinct carbon atoms* a molecule contains and what kind of bonding environment each one occupies. This is especially valuable for carbons that carry no hydrogens at all — quaternary carbons, which are invisible in ¹H NMR, show up directly in a ¹³C spectrum.

The ¹³C chemical shift range is much wider than ¹H (roughly 0–220 ppm versus 0–12 ppm), which means peaks are better separated and less likely to overlap. The general trends follow the same shielding logic you already know: carbons bonded to electronegative atoms or involved in pi bonding are **deshielded** and appear downfield. Alkyl carbons (sp³, no electronegative neighbors) typically appear between 0–50 ppm, alkene and aromatic carbons between 100–150 ppm, and carbonyl carbons between 170–220 ppm. Each distinct carbon environment in the molecule produces one peak, so counting peaks immediately tells you the number of unique carbon environments — a powerful constraint when proposing structures.

The major practical limitation of ¹³C NMR is **sensitivity**. The ¹³C isotope has only ~1.1% natural abundance (most carbon is ¹²C, which is NMR-silent), and its gyromagnetic ratio is about one-quarter that of ¹H. Together, these factors make ¹³C NMR roughly 6,000 times less sensitive than ¹H NMR. To compensate, ¹³C spectra are typically acquired with **broadband proton decoupling**, which collapses all C–H splitting into singlets, concentrating signal intensity into single sharp peaks. This simplifies the spectrum enormously but sacrifices information about how many hydrogens each carbon carries.

That lost information is recovered by the **DEPT experiment** (Distortionless Enhancement by Polarization Transfer). DEPT uses a clever pulse sequence to sort carbons by their attached hydrogen count. In a DEPT-135 spectrum, **CH₃ and CH groups point up** (positive peaks), **CH₂ groups point down** (negative peaks), and **quaternary carbons disappear entirely**. By comparing the DEPT-135 with the broadband-decoupled spectrum, you can immediately classify every carbon in the molecule. This combination — broadband ¹³C for the full carbon count, DEPT for hydrogen attachment — is one of the most efficient tools in organic structure determination.

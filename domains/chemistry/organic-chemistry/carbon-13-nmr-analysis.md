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
stage: formal-systems
status: validated
---

# Carbon-13 NMR Spectroscopy and DEPT

## Core Idea
¹³C NMR directly observes all carbon atoms, with offsets reflecting bonding environment (quaternary carbons are typically more deshielded). DEPT (Distortionless Enhancement by Polarization Transfer) distinguishes carbon types: CH₃ and CH point up; CH₂ points down; quaternary carbons disappear. Since ¹³C has low natural abundance (~1%) and long relaxation times, ¹³C NMR is less sensitive than ¹H NMR but provides direct carbon connectivity and is essential for assigning quaternary carbons.

## Questions

```yaml
- question: "A DEPT-135 spectrum shows three positive peaks and one negative peak. The broadband-decoupled ¹³C spectrum shows those four peaks plus one additional peak. What can you conclude about the extra peak?"
  type: multiple-choice
  options:
    - "It is a CH₂ carbon, which points down in DEPT-135 and was missed"
    - "It is a quaternary carbon with no attached hydrogens"
    - "It is an artifact caused by incomplete decoupling"
    - "It is a CH carbon that was folded over in the DEPT experiment"
  answer: 1
  explanation: "Quaternary carbons — those with no attached hydrogens — appear in the broadband-decoupled ¹³C spectrum but produce no signal in DEPT-135 because DEPT relies on polarization transfer from attached protons. A peak present in the full ¹³C spectrum but absent in DEPT-135 is diagnostic of a quaternary carbon (C, carbonyl carbon, quaternary alkyl carbon, etc.). This is precisely the situation where comparing the two spectra is essential."

- question: "Why is ¹³C NMR roughly 6,000 times less sensitive than ¹H NMR?"
  type: multiple-choice
  options:
    - "Because carbon nuclei are larger and harder to excite with radiofrequency pulses"
    - "Because the ¹³C isotope has only ~1.1% natural abundance and a gyromagnetic ratio about one-quarter that of ¹H"
    - "Because carbon-carbon bonds prevent the magnetization from relaxing properly"
    - "Because ¹³C nuclei have too many neutrons to respond to the applied magnetic field"
  answer: 1
  explanation: "Two independent factors multiply to create the sensitivity gap. First, only ~1.1% of all carbon atoms are the NMR-active ¹³C isotope (the rest are ¹²C, which is NMR-silent). Second, the gyromagnetic ratio of ¹³C is about one-quarter that of ¹H, which affects both the resonance frequency and the size of the detectable signal. Together, these factors reduce intrinsic sensitivity by roughly 6,000-fold, requiring longer acquisition times, more scans, or more concentrated samples."

- question: "In a DEPT-135 experiment, most types of carbon atoms produce peaks — they differ mainly in whether the peak points up or down."
  type: true-false
  answer: false
  explanation: "This is the most important practical point about DEPT-135: quaternary carbons (those with no attached hydrogens) produce NO peak at all. They disappear entirely from the spectrum because DEPT relies on polarization transfer from attached ¹H nuclei to ¹³C, and quaternary carbons have no such protons. This is why DEPT-135 must always be compared with a broadband-decoupled ¹³C spectrum to identify the quaternary carbons that DEPT misses."

- question: "The wider chemical shift range of ¹³C NMR compared to ¹H NMR means that ¹³C peaks from structurally distinct carbons are less likely to overlap."
  type: true-false
  answer: true
  explanation: "¹³C NMR spans roughly 0–220 ppm while ¹H NMR spans only 0–12 ppm. This 18-fold wider range means that even carbons in similar environments are more likely to be resolved as distinct peaks. For complex molecules, this separation is a practical advantage: counting the peaks in a ¹³C spectrum gives the number of chemically distinct carbon environments in the molecule with much less ambiguity than counting ¹H peaks."

- question: "Why must a broadband-decoupled ¹³C spectrum and a DEPT experiment typically be run together rather than relying on DEPT alone for structure determination?"
  type: short-answer
  answer: "DEPT-135 does not detect quaternary carbons at all, so DEPT alone provides an incomplete carbon count. Running broadband-decoupled ¹³C gives the total number of distinct carbon environments, while DEPT-135 classifies each as CH₃/CH (positive), CH₂ (negative), or quaternary (absent in DEPT). Any peak in the full ¹³C spectrum that has no DEPT counterpart must be a quaternary carbon. Without both experiments, you would not know how many quaternary carbons the molecule contains."
  explanation: "The two experiments are complementary. Broadband decoupling maximizes sensitivity and gives a complete carbon count but destroys multiplicity information. DEPT-135 recovers that multiplicity information (hydrogen count per carbon) but misses quaternary carbons. Together they give both the count and the type of every carbon, which is essential for structural assignment — especially for molecules containing carbonyl groups, quaternary stereocenters, or aromatic carbons bearing substituents rather than hydrogens."
```

## Explainer

From your study of ¹H NMR, you know that magnetic nuclei in different electronic environments resonate at different frequencies, producing distinct chemical shifts. **¹³C NMR** applies the same principle directly to carbon atoms. While ¹H NMR tells you about hydrogen environments, ¹³C NMR tells you how many *chemically distinct carbon atoms* a molecule contains and what kind of bonding environment each one occupies. This is especially valuable for carbons that carry no hydrogens at all — quaternary carbons, which are invisible in ¹H NMR, show up directly in a ¹³C spectrum.

The ¹³C chemical shift range is much wider than ¹H (roughly 0–220 ppm versus 0–12 ppm), which means peaks are better separated and less likely to overlap. The general trends follow the same shielding logic you already know: carbons bonded to electronegative atoms or involved in pi bonding are **deshielded** and appear downfield. Alkyl carbons (sp³, no electronegative neighbors) typically appear between 0–50 ppm, alkene and aromatic carbons between 100–150 ppm, and carbonyl carbons between 170–220 ppm. Each distinct carbon environment in the molecule produces one peak, so counting peaks immediately tells you the number of unique carbon environments — a powerful constraint when proposing structures.

The major practical limitation of ¹³C NMR is **sensitivity**. The ¹³C isotope has only ~1.1% natural abundance (most carbon is ¹²C, which is NMR-silent), and its gyromagnetic ratio is about one-quarter that of ¹H. Together, these factors make ¹³C NMR roughly 6,000 times less sensitive than ¹H NMR. To compensate, ¹³C spectra are typically acquired with **broadband proton decoupling**, which collapses all C–H splitting into singlets, concentrating signal intensity into single sharp peaks. This simplifies the spectrum enormously but sacrifices information about how many hydrogens each carbon carries.

That lost information is recovered by the **DEPT experiment** (Distortionless Enhancement by Polarization Transfer). DEPT uses a clever pulse sequence to sort carbons by their attached hydrogen count. In a DEPT-135 spectrum, **CH₃ and CH groups point up** (positive peaks), **CH₂ groups point down** (negative peaks), and **quaternary carbons disappear entirely**. By comparing the DEPT-135 with the broadband-decoupled spectrum, you can immediately classify every carbon in the molecule. This combination — broadband ¹³C for the full carbon count, DEPT for hydrogen attachment — is one of the most efficient tools in organic structure determination.

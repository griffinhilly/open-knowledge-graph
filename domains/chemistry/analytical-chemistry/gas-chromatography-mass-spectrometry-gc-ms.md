---
id: gas-chromatography-mass-spectrometry-gc-ms
title: 'Gas Chromatography-Mass Spectrometry: GC-MS'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: gas-chromatography
  type: hard
- id: mass-spectrometry-analytical
  type: hard
- id: gas-chromatography-quantitative-analysis
  type: soft
builds-toward:
- liquid-chromatography-mass-spectrometry-lc-ms
tags:
- GC-MS
- hyphenated-technique
- compound-identification
- quantitation
stage: advanced
status: draft
---

# Gas Chromatography-Mass Spectrometry: GC-MS

## Core Idea
GC-MS couples chromatographic separation with mass spectrometric detection, providing both molecular weight and structural information. This powerful combination enables identification of unknowns through spectrum matching, analysis of trace compounds through selective ion monitoring (SIM), and confirmation of analyte identity alongside quantitation in environmental and forensic matrices.

## Explainer

You already understand gas chromatography as a separation technique — volatile compounds partition between a carrier gas and a stationary phase inside a heated column, emerging at characteristic retention times. And you know mass spectrometry as a detection and identification technique — molecules are ionized, separated by mass-to-charge ratio, and counted. **GC-MS** is the direct coupling of these two instruments, where the GC column feeds its separated compounds one at a time into the mass spectrometer's ion source. The result is an analytical method that simultaneously tells you *what* is in a sample (through mass spectral identification) and *how much* (through signal intensity), a combination neither technique achieves alone.

The interface between the GC and MS is elegantly simple compared to LC-MS. Because GC already delivers analytes in the gas phase, they can flow directly into the electron ionization (EI) source of the mass spectrometer — no spray, no nebulizer, no desolvation needed. **Electron ionization** bombards each molecule with 70 eV electrons, producing a highly reproducible fragmentation pattern. This reproducibility is the foundation of GC-MS identification: the fragmentation pattern of a compound at 70 eV is essentially a molecular fingerprint. Libraries like the NIST Mass Spectral Library contain hundreds of thousands of reference spectra, and software can match an unknown spectrum against the library in seconds — turning an unidentified chromatographic peak into a named compound with high confidence.

For quantitative work, GC-MS offers a critical advantage over non-selective GC detectors like the FID. In **full scan mode**, the MS records the entire mass spectrum continuously, which is ideal for identifying unknowns. But when you already know what you are looking for, you can switch to **selected ion monitoring (SIM)**, where the MS tracks only one or a few characteristic m/z values for your target analyte. SIM dramatically improves sensitivity — often by 10–100× over full scan — because the detector spends all its time monitoring the ions you care about instead of scanning the entire mass range. This makes GC-MS the method of choice for trace analysis: detecting pesticide residues at parts-per-billion levels in food, identifying drugs of abuse in urine, or quantifying environmental pollutants in water.

The limitation of GC-MS follows directly from the limitation of GC itself: the analyte must be volatile enough to pass through the heated column without decomposing. Compounds that are too polar, too large, or thermally labile cannot be analyzed by GC-MS without chemical derivatization to make them volatile. This is why LC-MS was developed as a complement for non-volatile analytes. But for the vast world of volatile and semi-volatile organic compounds — solvents, fragrances, fuels, metabolites, drugs, explosives — GC-MS remains the gold standard, combining the resolving power of capillary GC with the identification certainty and sensitivity of mass spectrometry.

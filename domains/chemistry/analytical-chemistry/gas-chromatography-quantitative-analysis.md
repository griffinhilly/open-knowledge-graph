---
id: gas-chromatography-quantitative-analysis
title: 'Gas Chromatography: Quantitative Analysis and Calibration'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: gas-chromatography
  type: hard
- id: chromatography-fundamentals
  type: hard
- id: calibration-curve-methods
  type: soft
builds-toward:
- gas-chromatography-mass-spectrometry-gc-ms
- two-dimensional-chromatography-comprehensive
tags:
- GC
- quantitation
- calibration
- peak-area
- internal-standard
stage: advanced
status: draft
---

# Gas Chromatography: Quantitative Analysis and Calibration

## Core Idea
Quantitative GC converts detector signals (FID, ECD, etc.) into analyte concentration through area or height measurement and calibration. Advanced approaches include internal standard methods to correct for injection volume variation, response factor calculations accounting for detector sensitivity, and handling of co-eluting compounds through peak deconvolution.

## How It's Best Learned
Analyze multi-component GC standards, prepare calibration curves using different methods, and quantify unknowns with various approaches.

## Common Misconceptions
Assuming peak height and area give equivalent results (they diverge when peak shape varies). Neglecting the impact of sample matrix on detector response factors.

## Explainer

From your study of gas chromatography, you understand how compounds are separated by differential partitioning between a mobile gas phase and a stationary phase inside a column. From chromatography fundamentals, you know that the detector at the column exit produces a signal proportional to the amount of analyte passing through it. Quantitative GC is the discipline of converting that detector signal into a reliable concentration or mass value — and the gap between "getting a peak" and "getting an accurate number" is larger than it first appears.

The detector output is a chromatogram: a series of peaks plotted as signal intensity versus time. For quantitation, you measure either **peak area** (the integrated area under the curve) or **peak height** (the maximum signal intensity). Peak area is generally preferred because it is proportional to the total mass of analyte that passed through the detector, regardless of peak shape. Peak height can be affected by band broadening, tailing, or slight retention time shifts that change the peak's width without changing the total mass. However, height can outperform area when peaks partially overlap, because area integration of merged peaks introduces larger errors than reading the height of a partially resolved maximum.

The relationship between peak area and analyte concentration is established through **calibration**. The simplest approach is external standard calibration: you inject standards of known concentration, plot area versus concentration, and read unknown concentrations from the resulting curve. This works when injection volumes are highly reproducible. In practice, manual or autosampler injections vary slightly in volume, introducing scatter. The **internal standard method** corrects for this by adding a fixed amount of a non-analyte compound (the internal standard) to every sample and standard. You then plot the ratio of analyte area to internal standard area versus concentration. Since both compounds experience the same injection volume variation, the ratio cancels the error. Choosing an internal standard requires that it be chemically similar to the analyte (so it behaves similarly in the injection and separation) but fully resolved chromatographically.

A subtlety often overlooked is that different detectors have different **response factors** for different compounds. An FID (flame ionization detector) responds roughly in proportion to the number of carbon atoms, so equal masses of hexane and toluene give different peak areas. A **relative response factor** quantifies this ratio and must be determined experimentally or looked up in reference tables. Ignoring response factors — treating all peak areas as directly comparable — is a common source of quantitative error, especially in multicomponent analyses where you need accurate concentrations for every compound in a mixture, not just relative abundances.

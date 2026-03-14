---
id: internal-standards
title: Internal Standards
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: calibration-curve-methods
  type: hard
- id: method-validation
  type: soft
tags:
- internal standard
- response factor
- precision
- quantification
- calibration
- ISTD
stage: formal-systems
status: draft
---

# Internal Standards

## Core Idea
An internal standard (ISTD) is a known compound added at a fixed concentration to all samples and standards before analysis, so that the analyte signal is always expressed as a ratio (analyte response / ISTD response) rather than as an absolute value. This ratio corrects for variations in injection volume, detector drift, extraction recovery, and matrix effects — any factor that affects analyte and ISTD equally cancels out. The ideal internal standard is chemically similar to the analyte (so it experiences the same losses and matrix effects), chromatographically resolved from it, absent from the original sample, and stable throughout the procedure. The response factor, defined as the ratio of analyte sensitivity to ISTD sensitivity, must remain constant across the calibration range for quantification to be valid.

## How It's Best Learned
Prepare a calibration curve for a GC or HPLC analysis both with and without an internal standard, intentionally varying injection volumes slightly. Compare the %RSD of the two approaches to see how internal standardization dramatically improves precision when injection reproducibility is imperfect.

## Common Misconceptions
- The internal standard does not need to be the same compound as the analyte — it needs to behave similarly during sample preparation and measurement, which is why structural analogs or isotope-labeled versions are preferred.
- Adding an internal standard does not correct for every source of error; if the ISTD and analyte experience different matrix effects or different extraction recoveries, the correction will be incomplete or misleading.

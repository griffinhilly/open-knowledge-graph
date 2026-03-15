---
id: chromatography-fundamentals
title: 'Chromatography: Principles and Theoretical Plate Model'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: intermolecular-forces
  type: hard
- id: colligative-properties
  type: soft
- id: sample-preparation
  type: soft
- id: diffusion-and-ficks-laws
  type: soft
builds-toward:
- gas-chromatography
- hplc
- thin-layer-chromatography
tags:
- chromatography
- stationary phase
- mobile phase
- retention factor
- resolution
- theoretical plates
stage: advanced
status: validated
---
# Chromatography: Principles and Theoretical Plate Model

## Core Idea
Chromatography separates mixtures by differential migration through a system with a stationary phase and a flowing mobile phase; analytes are separated because they partition between the two phases to different extents. The retention factor k = (time in stationary phase)/(time in mobile phase) characterizes analyte affinity. The theoretical plate model treats a column as N discrete equilibration stages; column efficiency N = (tR/σ)² governs peak width. Resolution R = (ΔtR)/(average peak width) must exceed 1.5 for baseline separation and depends on selectivity, efficiency, and retention.

## How It's Best Learned
Calculate N, k, and R from a real chromatogram before exploring how changes in mobile phase, temperature, or column length affect each parameter. The van Deemter equation connecting N to mobile phase velocity illustrates the trade-off between speed and efficiency.

## Common Misconceptions
- More theoretical plates always improve resolution, but only to the extent that selectivity (α) is non-unity — a column with 10,000 plates cannot separate two compounds with identical partition coefficients.
- Peak tailing is not normal; it indicates poor column packing, active sites, or column overloading.

---
id: x-ray-diffraction-materials
title: X-Ray Diffraction and Crystal Identification
domain: engineering
course: materials-science
prerequisites:
- id: miller-indices
  type: hard
- id: wave-interference
  type: hard
- id: diffraction-gratings
  type: soft
tags:
- XRD
- bragg-law
- diffraction
- crystal-identification
- lattice-parameter
stage: formal-systems
status: validated
---

# X-Ray Diffraction and Crystal Identification

## Core Idea
X-ray diffraction (XRD) exploits constructive interference of X-rays scattered by periodic crystal planes to determine crystal structure. Bragg's law (nλ = 2d sinθ) relates the X-ray wavelength, the interplanar spacing d (determined by Miller indices and lattice parameter), and the diffraction angle θ. An XRD pattern — peaks at specific 2θ angles with characteristic relative intensities — serves as a fingerprint for phase identification, lattice parameter measurement, and residual stress analysis. XRD is the primary technique for confirming the crystal structure of new materials and for monitoring phase transformations in heat-treated alloys.

## How It's Best Learned
Apply Bragg's law to calculate the expected 2θ angles for the first three peaks of an FCC metal (e.g., copper) and compare to a measured diffractogram. Use systematic absences (structure factor rules) to explain why certain reflections are missing.

## Common Misconceptions
- Bragg's law gives a necessary condition for diffraction but not a sufficient one — the structure factor (from the atomic arrangement within the unit cell) can extinguish peaks that geometry predicts.
- XRD measures average long-range structure; amorphous materials and very small crystallites produce broad, diffuse patterns rather than sharp peaks.

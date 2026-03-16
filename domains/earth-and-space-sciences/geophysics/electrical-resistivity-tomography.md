---
id: electrical-resistivity-tomography
title: Electrical Resistivity Tomography and 2D Imaging
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: electromagnetic-induction-methods
  type: hard
- id: electrical-conductivity-crustal
  type: soft
tags:
- ert
- resistivity
- tomography
- imaging
stage: advanced
status: draft
---

# Electrical Resistivity Tomography and 2D Imaging

## Core Idea
2D electrical resistivity tomography (ERT) inverts multi-electrode surface measurements to image subsurface conductivity. Applications include groundwater mapping, contaminant plume imaging, and engineering site characterization.

## Explainer

From your study of electromagnetic induction methods, you understand that different earth materials have different electrical conductivities — clay-rich sediments conduct well, dry sand and intact bedrock resist current flow, and groundwater salinity dramatically affects conductivity. **Electrical resistivity tomography (ERT)** exploits these contrasts by injecting current into the ground through electrodes and measuring the resulting voltage differences to build a 2D cross-sectional image of subsurface resistivity.

The basic measurement uses four electrodes: two **current electrodes** (A and B) that inject and collect current, and two **potential electrodes** (M and N) that measure the voltage difference created by that current flowing through the ground. From the injected current, measured voltage, and known electrode geometry, you calculate an **apparent resistivity** — the resistivity the ground would have if it were perfectly uniform. Of course the ground is not uniform, so the apparent resistivity is a weighted average of the true resistivities along the current's path. By varying electrode spacing and position, you sample different depths and lateral positions, building up a dataset that contains information about the full 2D resistivity structure.

Modern ERT uses a **multi-electrode array** — dozens or even hundreds of electrodes planted along a survey line, connected by a switching unit that automatically cycles through thousands of four-electrode combinations. Common array configurations include Wenner (equal spacing, good vertical resolution), dipole-dipole (good lateral resolution, sensitive to horizontal boundaries), and Schlumberger (a balance of depth penetration and resolution). Wider electrode separations push current deeper, so the dataset naturally samples from shallow to deep as spacing increases.

The raw apparent resistivity values are arranged in a **pseudosection** — a preliminary image where each measurement is plotted at a position and depth related to its electrode geometry. But a pseudosection is not a true image; it is a distorted representation because apparent resistivity conflates contributions from many depths. The real image comes from **inversion**: an algorithm starts with a guess of the true resistivity distribution, forward-models what voltages that distribution would produce, compares them to the measured data, and iteratively adjusts the model until predicted and observed data converge. The result is a 2D resistivity section showing how resistivity varies with depth and lateral position — revealing aquifer boundaries, contamination plumes, bedrock topography, or buried structures with spatial resolution on the order of the electrode spacing.

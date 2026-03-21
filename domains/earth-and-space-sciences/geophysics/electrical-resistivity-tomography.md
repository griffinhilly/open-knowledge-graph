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

## Questions

```yaml
- question: "A geophysicist records an apparent resistivity of 200 Ω·m at a given electrode configuration. What does this value directly represent?"
  type: multiple-choice
  options:
    - "The true electrical resistivity of the rock or sediment at the depth directly below the electrode midpoint"
    - "A weighted average of resistivities along the entire current path through the ground — not the true resistivity at any single point"
    - "The maximum resistivity within the depth range sampled by that electrode spacing"
    - "The resistivity of the deepest layer reached by the injected current"
  answer: 1
  explanation: "Apparent resistivity is calculated from the injected current, measured voltage, and electrode geometry assuming the ground is uniform. Because the ground is not uniform, the resulting value conflates contributions from every part of the subsurface through which current flows — shallow materials, deep materials, and everything in between, weighted by how much current passes through each part. A single 200 Ω·m measurement cannot be attributed to any specific layer or location. Recovering the true resistivity distribution requires inversion."

- question: "A researcher displays an ERT pseudosection and labels it 'a 2D cross-section of subsurface resistivity.' A colleague says this label is misleading. Who is correct?"
  type: multiple-choice
  options:
    - "The researcher is correct; the pseudosection is produced by plotting measurements directly at their true subsurface locations"
    - "The colleague is correct; a pseudosection plots apparent resistivity values at conventional positions derived from electrode geometry — it is a distorted preliminary display, not a true image of subsurface structure"
    - "The pseudosection is accurate only for the Wenner array; other arrays require inversion before display"
    - "Both are right; inversion merely smooths the pseudosection without fundamentally changing what it represents"
  answer: 1
  explanation: "A pseudosection is a convenient display convention, not a physical image. Each measurement is plotted at a depth proportional to electrode spacing and a lateral position at the array midpoint, but this depth assignment is geometric, not physical — it does not represent the actual depth at which resistivity was sampled. Because each apparent resistivity is a smeared average over the current path, the pseudosection systematically distorts the true structure (shallow anomalies appear as deep ones, lateral boundaries appear curved, etc.). Inversion uses a forward model to find the true resistivity distribution that would reproduce the observed data — this is the essential step that converts data into a geologically interpretable image."

- question: "Increasing the electrode spacing in an ERT survey allows the injected current to penetrate deeper into the subsurface, enabling sampling of deeper structures."
  type: true-false
  answer: true
  explanation: "Current spreading in the subsurface is controlled by electrode geometry: closely spaced electrodes inject current that stays shallow, while widely spaced electrodes force current deeper before it returns to the surface. This is the physical basis for depth sounding — by systematically increasing electrode separations across a multi-electrode array and analyzing how apparent resistivity changes with spacing, ERT builds a dataset that contains information about resistivity at progressively greater depths. The maximum investigation depth is roughly one-fifth to one-sixth of the maximum electrode spacing, depending on the array type and subsurface conditions."

- question: "An ERT pseudosection directly shows the true 2D distribution of subsurface resistivity, making inversion an optional refinement that improves image quality but is not required for geological interpretation."
  type: true-false
  answer: false
  explanation: "Inversion is not optional — it is the step that converts raw apparent resistivity data into a physically interpretable model. A pseudosection is a distorted representation: shallow anomalies can appear at wrong depths, resistivity contrasts are blurred, and the geometry of boundaries is not preserved. Using a pseudosection for geological interpretation without inversion would be like using a blurry, geometrically distorted photograph to make precise measurements. The inversion algorithm iteratively adjusts a model resistivity distribution until the forward-modeled response matches the observed data, producing a cross-section where values correspond to actual subsurface resistivity and spatial positions correspond to actual locations."

- question: "Explain why inversion, rather than simply plotting apparent resistivity values, is necessary to create an accurate image of subsurface structure from ERT data."
  type: short-answer
  answer: "Each apparent resistivity measurement integrates contributions from a large volume of the subsurface — it is a nonlinear weighted average of true resistivities along the entire current path, not a reading at a specific point. Plotting these values at conventional positions (the pseudosection) produces a distorted image where true boundaries appear curved, depths are misrepresented, and adjacent measurements overlap in sensitivity. Inversion addresses this by constructing a model of the true 2D resistivity distribution and iteratively adjusting it until the forward-predicted apparent resistivities match the observed data within noise levels. Only after inversion do the displayed values correspond to actual rock resistivities at actual subsurface positions."
  explanation: "The pseudosection is a useful preliminary quality-check display, but geophysicists are careful not to over-interpret it directly. The inversion is what makes ERT a quantitative imaging technique rather than just a qualitative anomaly detector. Understanding this distinction separates practitioners who can extract reliable information from ERT surveys from those who draw incorrect conclusions from pseudosection artifacts."
```

## Explainer

From your study of electromagnetic induction methods, you understand that different earth materials have different electrical conductivities — clay-rich sediments conduct well, dry sand and intact bedrock resist current flow, and groundwater salinity dramatically affects conductivity. **Electrical resistivity tomography (ERT)** exploits these contrasts by injecting current into the ground through electrodes and measuring the resulting voltage differences to build a 2D cross-sectional image of subsurface resistivity.

The basic measurement uses four electrodes: two **current electrodes** (A and B) that inject and collect current, and two **potential electrodes** (M and N) that measure the voltage difference created by that current flowing through the ground. From the injected current, measured voltage, and known electrode geometry, you calculate an **apparent resistivity** — the resistivity the ground would have if it were perfectly uniform. Of course the ground is not uniform, so the apparent resistivity is a weighted average of the true resistivities along the current's path. By varying electrode spacing and position, you sample different depths and lateral positions, building up a dataset that contains information about the full 2D resistivity structure.

Modern ERT uses a **multi-electrode array** — dozens or even hundreds of electrodes planted along a survey line, connected by a switching unit that automatically cycles through thousands of four-electrode combinations. Common array configurations include Wenner (equal spacing, good vertical resolution), dipole-dipole (good lateral resolution, sensitive to horizontal boundaries), and Schlumberger (a balance of depth penetration and resolution). Wider electrode separations push current deeper, so the dataset naturally samples from shallow to deep as spacing increases.

The raw apparent resistivity values are arranged in a **pseudosection** — a preliminary image where each measurement is plotted at a position and depth related to its electrode geometry. But a pseudosection is not a true image; it is a distorted representation because apparent resistivity conflates contributions from many depths. The real image comes from **inversion**: an algorithm starts with a guess of the true resistivity distribution, forward-models what voltages that distribution would produce, compares them to the measured data, and iteratively adjusts the model until predicted and observed data converge. The result is a 2D resistivity section showing how resistivity varies with depth and lateral position — revealing aquifer boundaries, contamination plumes, bedrock topography, or buried structures with spatial resolution on the order of the electrode spacing.

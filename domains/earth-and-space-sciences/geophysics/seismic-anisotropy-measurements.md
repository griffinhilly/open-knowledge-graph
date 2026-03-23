---
id: seismic-anisotropy-measurements
title: Seismic Anisotropy and Shear-Wave Splitting Analysis
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-anisotropy-shear-wave-splitting
  type: hard
- id: seismic-body-waves-p-and-s
  type: hard
tags:
- anisotropy
- shear-wave-splitting
- polarization
stage: expert
status: validated
---

# Seismic Anisotropy and Shear-Wave Splitting Analysis

## Core Idea
Aligned minerals or cracks cause seismic velocity to vary with direction (anisotropy). Shear-wave splitting measures two perpendicular S-wave velocities; splitting patterns constrain mantle fabric and stress orientation.

## Questions

```yaml
- question: "An SKS phase recorded at a seismic station shows shear-wave splitting with a fast polarization direction of NE-SW. What does this fast polarization direction most likely indicate about the mantle fabric beneath the station?"
  type: multiple-choice
  options:
    - "Seismic waves travel faster toward the NE-SW direction due to random compositional heterogeneity"
    - "The dominant mantle flow or strain direction is oriented NE-SW, consistent with olivine fast-axis alignment with flow"
    - "The crust is anomalously thick in the NE-SW direction beneath the station"
    - "The delay time indicates the mantle is isotropic, and the fast direction is an artifact"
  answer: 1
  explanation: "In the upper mantle, olivine — the dominant mineral — develops a crystallographic preferred orientation (CPO) when it deforms under flow. The olivine fast axis aligns with the flow direction. An S-wave entering this fabric splits into a fast component polarized parallel to the alignment (NE-SW in this case) and a slow component perpendicular. The fast polarization direction therefore directly records the mantle flow or past strain direction. Option C (crustal thickness) would not produce consistent S-wave splitting. Anisotropy by definition means the medium is NOT isotropic (option D)."

- question: "A seismologist measures SKS splitting at two stations with similar fast polarization directions (both ~N45°E) but very different delay times: 0.5 seconds at one station and 2.0 seconds at the other. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "One station is in a seismically quiet area with no anisotropy, producing artificially small delay times"
    - "The stations overlie mantle with the same fabric orientation but different thicknesses or strengths of the anisotropic layer"
    - "The differences reflect different earthquake source mechanisms biasing the measurements"
    - "Fast polarization directions of N45°E are unreliable, so both measurements should be discarded"
  answer: 1
  explanation: "The delay time δt reflects how much time the fast and slow S-wave components separate as they travel through the anisotropic layer — it depends on both the intrinsic strength of the anisotropy AND the thickness of the anisotropic region traversed. Similar fast polarization directions at both stations indicate the same fabric orientation (same mantle flow direction), while the different delay times indicate that one station sits above a thicker or more strongly anisotropic mantle column. Option B is correct — the two parameters are independent: fast direction → orientation, delay time → strength × thickness."

- question: "An S-wave passing through a perfectly isotropic medium will not undergo shear-wave splitting."
  type: true-false
  answer: true
  explanation: "Shear-wave splitting requires velocity to vary with the polarization direction of the S-wave — the defining property of an anisotropic medium. In a perfectly isotropic medium, S-wave velocity is the same in all polarization directions, so there is no preferred fast or slow component and no splitting occurs. The S-wave propagates with a single velocity and its polarization is preserved. This is precisely why shear-wave splitting is used as a diagnostic tool: detecting splitting proves the presence of anisotropy and provides quantitative information about the fabric causing it."

- question: "The delay time measured from SKS splitting reveals the orientation of the anisotropic fabric, while the fast polarization direction reveals the thickness of the anisotropic layer."
  type: true-false
  answer: false
  explanation: "These roles are reversed. The FAST POLARIZATION DIRECTION (φ) reveals the fabric orientation — in the mantle, typically the direction of olivine alignment and thus mantle flow. The DELAY TIME (δt) reveals the product of anisotropy strength and layer thickness — a larger δt means either stronger anisotropy, a thicker anisotropic layer, or both. This is an important distinction: the same φ at two stations tells you the same fabric orientation; different δt tells you different amounts of anisotropy accumulated along the path."

- question: "Why do seismologists prefer SKS phases over direct S-waves for measuring mantle anisotropy beneath a seismic station? What property of SKS phases makes them particularly useful?"
  type: short-answer
  answer: "SKS phases travel as P-waves through the Earth's outer core and convert back to S-waves upon exiting the core on the receiver side. The critical property is that this P-to-S conversion gives the wave a known, fixed initial polarization in the radial direction. Any shear-wave splitting observed in SKS must therefore have been acquired in the mantle and crust beneath the receiving station — not at the earthquake source or along the distant path. Direct S-waves, by contrast, could have picked up splitting anywhere along their long path from source to receiver, making it impossible to isolate the contribution from beneath the station."
  explanation: "The near-vertical incidence of SKS arrivals adds another advantage: the wave travels nearly straight up through the mantle beneath the station, so the splitting parameters (φ and δt) sample a well-defined, roughly vertical column of mantle. This makes SKS splitting a station-specific measurement of local mantle fabric, enabling researchers to map lateral variations in flow patterns by comparing measurements across arrays of stations."
```

## Explainer

From your prerequisites on seismic body waves and shear-wave splitting, you know that S-waves oscillate perpendicular to their travel direction and that in an anisotropic medium, an S-wave splits into two components traveling at different speeds. Seismic anisotropy measurements turn this phenomenon into a tool for probing the internal fabric of the Earth — revealing how minerals are aligned, how the mantle flows, and how stress is oriented in the crust.

The physical basis is straightforward. Many Earth materials are **anisotropic** because their constituent minerals or structures have a preferred orientation. In the upper mantle, the dominant mineral olivine develops a crystallographic preferred orientation (CPO) when it deforms under mantle flow — the crystal's fast axis aligns with the flow direction. In the upper crust, aligned fluid-filled cracks oriented parallel to the maximum horizontal stress create a different kind of anisotropy. In both cases, seismic waves traveling through the aligned medium experience direction-dependent velocities. An S-wave entering such a region splits into a **fast component** polarized parallel to the alignment direction and a **slow component** polarized perpendicular to it.

The measurement extracts two parameters: the **fast polarization direction** (φ) and the **delay time** (δt). The fast direction tells you the orientation of the anisotropic fabric — in the mantle, it typically indicates the direction of flow or past deformation; in the crust, it often parallels the maximum compressive stress. The delay time tells you the strength and/or thickness of the anisotropic layer — a thicker or more strongly anisotropic region produces a larger time separation between the fast and slow arrivals. Typical delay times for SKS splitting (using core-refracted phases that arrive with near-vertical incidence) are 1–2 seconds, accumulating over path lengths of hundreds of kilometers through the upper mantle.

In practice, seismologists use teleseismic phases like **SKS** and **SKKS** because these waves convert from S to P at the outer core boundary and back to S upon exiting, arriving at the station with a known initial polarization. Any splitting observed must have been acquired on the receiver side — in the mantle and crust beneath the station. By analyzing SKS splitting at arrays of stations, researchers map mantle flow patterns. Beneath oceanic plates, the fast direction typically aligns with absolute plate motion, consistent with shear-driven olivine alignment at the base of the plate. Beneath continents, patterns are more complex, reflecting both present-day flow and frozen-in fabric from ancient deformation events. Near subduction zones, splitting measurements reveal complex 3D flow patterns in the mantle wedge, including trench-parallel flow that challenges simple 2D corner-flow models. These measurements provide constraints on mantle dynamics that no other geophysical method can offer.

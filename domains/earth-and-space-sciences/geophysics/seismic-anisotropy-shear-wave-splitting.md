---
id: seismic-anisotropy-shear-wave-splitting
title: Seismic Anisotropy and Shear Wave Splitting
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-surface-waves-rayleigh-love
  type: hard
- id: elastic-wave-propagation-in-solids
  type: hard
tags:
- seismology
- anisotropy
- shear-wave-splitting
- wave-propagation
stage: expert
status: validated
---

# Seismic Anisotropy and Shear Wave Splitting

## Core Idea
Seismic anisotropy—directional dependence of wave velocity—arises from aligned minerals (e.g., olivine in the mantle or mica in schists) or aligned fluid-filled cracks. S-waves split into orthogonal fast (Sf) and slow (Ss) polarizations when propagating through anisotropic media; the time delay δt between them is proportional to anisotropy strength and path length. Shear wave splitting measurements constrain mantle fabric (flow direction), crack orientation (stress or fluids), and deformation depth, providing windows into lithospheric and mantle dynamics.

## Questions

```yaml
- question: "A seismic station records SKS shear-wave splitting with a fast polarization direction of N10°E and a delay time δt = 1.8 seconds. What is the most geophysically meaningful interpretation?"
  type: multiple-choice
  options:
    - "The crust beneath the station has fluid-filled cracks aligned N10°E, producing the 1.8-second delay"
    - "The upper mantle beneath the station has a fabric with a N10°E fast axis, likely from olivine crystals aligned by northward mantle flow; the 1.8-second delay implies strong or thick anisotropy"
    - "The seismic wave was deflected by a fault striking N10°E, and 1.8 seconds is the travel-time anomaly"
    - "The lower mantle has a NNE-oriented fabric; SKS phases sample the entire mantle"
  answer: 1
  explanation: "SKS phases convert from S to P in the liquid outer core and back to S at the core-mantle boundary, arriving at the station with a known initial polarization. Any splitting they acquire occurs in the solid mantle and crust. The dominant contribution is typically the upper mantle (100-200 km thick anisotropic layer), where olivine lattice-preferred orientation (LPO) from mantle flow creates the anisotropy. A 1.8-second delay is too large to be primarily crustal (crustal splitting is typically 0.1-0.3s). Fluid-filled cracks (option A) are a crustal mechanism inconsistent with a 1.8s delay. The lower mantle (option D) is largely isotropic or has minimal contribution to SKS splitting."

- question: "Two seismologists compare splitting measurements. Station A shows δt = 0.5s; Station B shows δt = 1.5s. Seismologist X concludes the mantle under B is three times more anisotropic than under A. Is this conclusion justified?"
  type: multiple-choice
  options:
    - "Yes — δt is directly proportional to anisotropy strength, so a 3× larger delay means 3× stronger anisotropy"
    - "No — δt depends on both anisotropy strength and path length through the anisotropic region; Station B may have weaker anisotropy over a longer path, or stronger anisotropy over a similar path"
    - "No — δt measures only the depth of the anisotropic layer, not its strength"
    - "Yes — but only if the two stations use the same SKS phase, otherwise the comparison is invalid"
  answer: 1
  explanation: "The delay time δt is the product of the percentage anisotropy and the path length through the anisotropic medium: δt ∝ (anisotropy strength) × (path length). A larger δt could reflect stronger anisotropy over the same path length, the same anisotropy strength over a longer path, or some combination. Without independent constraints on path length (e.g., from receiver function analysis of lithospheric thickness), you cannot disentangle the two contributions. This is an important limitation of shear-wave splitting — it measures the integrated effect along the entire path, not the local anisotropy at any specific depth."

- question: "Shear-wave splitting occurs because an S-wave entering an anisotropic medium splits into two components that travel at different velocities, producing a time delay between their arrivals at the surface."
  type: true-false
  answer: true
  explanation: "This is the core phenomenon. In an isotropic medium, S-wave velocity is the same regardless of polarization direction. In an anisotropic medium (e.g., olivine-rich mantle with LPO, or crust with aligned fluid-filled cracks), velocity depends on polarization direction relative to the fabric. The incoming S-wave projects onto the fast and slow polarization eigenvectors of the medium, and these two components then propagate at different speeds. By the time they emerge, a delay δt has accumulated. A seismogram shows two S-wave pulses instead of one, with orthogonal polarizations. This is directly analogous to optical birefringence in calcite crystals."

- question: "A large delay time (δt > 2 seconds) in shear-wave splitting measurements always indicates very strong seismic anisotropy in the mantle."
  type: true-false
  answer: false
  explanation: "δt = (fractional anisotropy) × (path length through anisotropic region) / (average S-wave velocity). A large δt can result from moderate anisotropy spread over a thick layer (e.g., 200 km of 2% anisotropy) just as easily as from strong anisotropy over a thin layer. In subduction zones, for example, large δt values sometimes reflect a thick anisotropic wedge of mantle material rather than exceptionally strong crystal alignment. Conversely, short path lengths through strongly anisotropic material (e.g., in a thin but intensely deformed shear zone) can produce small δt despite high local anisotropy. Disentangling strength from thickness requires combining splitting measurements with other constraints."

- question: "Explain the physical process by which a single S-wave becomes two distinct arrivals after passing through an anisotropic region of the mantle."
  type: short-answer
  answer: "When an S-wave enters an anisotropic medium, its particle motion (polarization) projects onto two orthogonal eigenvectors of the medium: the fast polarization direction and the slow polarization direction. These two components propagate independently at different wave speeds — the fast component moves at higher velocity than the slow component. As both components travel through the anisotropic region, they accumulate a time difference proportional to the anisotropy strength and path length. Upon exiting, what was a single coherent pulse arrives as two separate pulses offset in time, polarized at 90° to each other. The effect is identical to optical birefringence in crystals like calcite."
  explanation: "The analogy to optics is exact because both phenomena arise from the same physical principle: in a medium with directional symmetry breaking, waves with different polarizations couple to different effective elastic (or optical) moduli and therefore travel at different speeds. Geophysicists exploit this by measuring the fast direction φ (which tells them about mantle flow or stress orientation) and the delay time δt (which quantifies the integrated effect of anisotropy along the path)."
```

## Explainer

From your study of elastic wave propagation, you know that S-waves (shear waves) oscillate perpendicular to their travel direction and cannot propagate through fluids. In an **isotropic** medium — one with the same properties in every direction — an S-wave travels at a single velocity regardless of its polarization direction. But Earth materials are often not isotropic. When the medium has a directional fabric, the velocity of a shear wave depends on which direction it oscillates relative to that fabric. This directional dependence of wave speed is **seismic anisotropy**, and its most diagnostic observable is **shear wave splitting**.

The splitting phenomenon works by direct analogy with optical birefringence. When polarized light enters a crystal like calcite, it splits into two rays traveling at different speeds. Similarly, when a shear wave enters an anisotropic region, it splits into two orthogonally polarized components: a **fast component** (Sf) polarized parallel to the fast direction of the medium, and a **slow component** (Ss) polarized perpendicular to it. The two components travel at different velocities, so by the time they emerge from the anisotropic region, a time delay (**δt**) has accumulated between them. A seismogram that started as a simple S-wave pulse arrives as two pulses separated in time, with orthogonal polarizations.

Two measurable quantities characterize the splitting: the **fast polarization direction** (φ), which tells you the orientation of the anisotropic fabric, and the **delay time** (δt), which is proportional to the strength of anisotropy multiplied by the path length through the anisotropic region. In the upper mantle, anisotropy is primarily caused by **lattice-preferred orientation (LPO)** of olivine crystals, which align their fast crystallographic axis with the direction of mantle flow. A splitting measurement showing φ oriented east-west, for example, suggests east-west mantle flow beneath the station. In the crust, anisotropy more often arises from **stress-aligned fluid-filled cracks**: microcracks open preferentially perpendicular to the minimum compressive stress, creating a fabric whose fast direction parallels the maximum horizontal stress.

Splitting analysis is typically performed on teleseismic SKS phases — S-waves that convert to P in the liquid outer core and back to S upon exiting, arriving at the station with a known initial polarization. By comparing the observed two-component waveform to what a single unsplit arrival would look like, analysts determine φ and δt. Typical delay times of 1–2 seconds for SKS phases imply anisotropy distributed over 100–200 km of upper mantle. Crustal anisotropy produces much smaller delays (0.1–0.3 s) because the path through the crust is shorter. Mapping splitting parameters across a seismic network reveals spatial patterns of mantle flow, stress orientation, and deformation — making shear wave splitting one of the most direct geophysical probes of dynamic processes beneath the surface.

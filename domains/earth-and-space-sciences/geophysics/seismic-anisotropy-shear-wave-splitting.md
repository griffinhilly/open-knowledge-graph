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
stage: advanced
status: draft
---

# Seismic Anisotropy and Shear Wave Splitting

## Core Idea
Seismic anisotropy—directional dependence of wave velocity—arises from aligned minerals (e.g., olivine in the mantle or mica in schists) or aligned fluid-filled cracks. S-waves split into orthogonal fast (Sf) and slow (Ss) polarizations when propagating through anisotropic media; the time delay δt between them is proportional to anisotropy strength and path length. Shear wave splitting measurements constrain mantle fabric (flow direction), crack orientation (stress or fluids), and deformation depth, providing windows into lithospheric and mantle dynamics.

## Explainer

From your study of elastic wave propagation, you know that S-waves (shear waves) oscillate perpendicular to their travel direction and cannot propagate through fluids. In an **isotropic** medium — one with the same properties in every direction — an S-wave travels at a single velocity regardless of its polarization direction. But Earth materials are often not isotropic. When the medium has a directional fabric, the velocity of a shear wave depends on which direction it oscillates relative to that fabric. This directional dependence of wave speed is **seismic anisotropy**, and its most diagnostic observable is **shear wave splitting**.

The splitting phenomenon works by direct analogy with optical birefringence. When polarized light enters a crystal like calcite, it splits into two rays traveling at different speeds. Similarly, when a shear wave enters an anisotropic region, it splits into two orthogonally polarized components: a **fast component** (Sf) polarized parallel to the fast direction of the medium, and a **slow component** (Ss) polarized perpendicular to it. The two components travel at different velocities, so by the time they emerge from the anisotropic region, a time delay (**δt**) has accumulated between them. A seismogram that started as a simple S-wave pulse arrives as two pulses separated in time, with orthogonal polarizations.

Two measurable quantities characterize the splitting: the **fast polarization direction** (φ), which tells you the orientation of the anisotropic fabric, and the **delay time** (δt), which is proportional to the strength of anisotropy multiplied by the path length through the anisotropic region. In the upper mantle, anisotropy is primarily caused by **lattice-preferred orientation (LPO)** of olivine crystals, which align their fast crystallographic axis with the direction of mantle flow. A splitting measurement showing φ oriented east-west, for example, suggests east-west mantle flow beneath the station. In the crust, anisotropy more often arises from **stress-aligned fluid-filled cracks**: microcracks open preferentially perpendicular to the minimum compressive stress, creating a fabric whose fast direction parallels the maximum horizontal stress.

Splitting analysis is typically performed on teleseismic SKS phases — S-waves that convert to P in the liquid outer core and back to S upon exiting, arriving at the station with a known initial polarization. By comparing the observed two-component waveform to what a single unsplit arrival would look like, analysts determine φ and δt. Typical delay times of 1–2 seconds for SKS phases imply anisotropy distributed over 100–200 km of upper mantle. Crustal anisotropy produces much smaller delays (0.1–0.3 s) because the path through the crust is shorter. Mapping splitting parameters across a seismic network reveals spatial patterns of mantle flow, stress orientation, and deformation — making shear wave splitting one of the most direct geophysical probes of dynamic processes beneath the surface.

---
id: em-waves-anisotropic-media
title: Electromagnetic Waves in Anisotropic Media
domain: physics
course: electrodynamics
prerequisites:
- id: electromagnetic-wave-equation
  type: hard
- id: frequency-dependent-permittivity
  type: hard
builds-toward:
- birefringence-and-dichroism
tags:
- anisotropy
- crystals
- birefringence
stage: advanced
status: draft
---

# Electromagnetic Waves in Anisotropic Media

## Core Idea
In anisotropic materials the permittivity is a tensor ε_ij(ω). Waves propagate along principal axes without polarization rotation, but arbitrary polarizations decompose into eigenmodes with different phase velocities, causing birefringence.

## Explainer

You know that in an isotropic medium the permittivity ε is a scalar: the electric polarization P always points parallel to the applied field E, and the wave propagates with a single phase velocity v = c/n. Now remove the assumption of isotropy. In a crystal whose structure is different along different axes — say, calcite or quartz — the electrons are easier to displace in some directions than others. The response of the medium to an applied field therefore depends on the field's orientation: a field pointing along one crystal axis polarizes the medium more strongly than the same field along a different axis.

The compact way to express this is with a **permittivity tensor** ε_ij: the i-th component of D equals Σ_j ε_ij E_j. In general, D and E are not parallel — the displacement and the field can point in different directions. However, every real symmetric tensor can be diagonalized by rotating to its **principal axes**. Along these special directions, D and E are parallel and the material behaves like an isotropic medium — just with a different ε value for each axis (ε_x, ε_y, ε_z called the principal permittivities). These define the three **principal refractive indices** n_x, n_y, n_z.

The consequences for wave propagation are striking. For a wave traveling along a principal axis, any linearly polarized wave with E along one of the other principal axes is an eigenmode — it propagates without changing its polarization state. But it travels at a speed set by the permittivity for its polarization direction. A second linearly polarized wave with E along the other transverse principal axis is also an eigenmode, but it travels at a different speed. Now send in a wave polarized at 45° to both principal axes: it decomposes into equal parts of the two eigenmodes, which accumulate a **phase difference** as they travel. After a certain thickness, the two components are 90° out of phase and the initially linear polarization has become circular. After twice that thickness, they are 180° apart and the polarization has rotated 90°. This is **birefringence** — the splitting of one beam into two with different velocities — and it is the working principle behind wave plates and polarization optics. The frequency-dependent permittivity you studied earlier adds the further complication that the eigenmode phase velocities depend on ω, so different wavelengths develop different phase differences at the same thickness.

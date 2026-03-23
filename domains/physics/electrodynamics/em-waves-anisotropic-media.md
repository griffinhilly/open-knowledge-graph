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
stage: expert
status: draft
---

# Electromagnetic Waves in Anisotropic Media

## Core Idea
In anisotropic materials the permittivity is a tensor ε_ij(ω). Waves propagate along principal axes without polarization rotation, but arbitrary polarizations decompose into eigenmodes with different phase velocities, causing birefringence.

## Questions

```yaml
- question: "A linearly polarized light wave enters a birefringent crystal with its polarization at 45° to the two principal axes. After propagating through the crystal, the polarization state will be:"
  type: multiple-choice
  options:
    - "Still linear at 45°, because the crystal is symmetric about the propagation axis"
    - "Rotated by 45° to align with one of the principal axes"
    - "Elliptical (or circular), because the two eigenmodes accumulate a phase difference as they travel at different speeds"
    - "Unchanged because birefringence only affects waves polarized along a principal axis"
  answer: 2
  explanation: "A wave polarized at 45° decomposes into equal parts of the two eigenmodes (one along each principal axis). Each eigenmode propagates at its own phase velocity, set by the corresponding principal permittivity. After a distance, the two components are out of phase by some amount φ. When φ = 90°, the polarization is circular; at other values it is elliptical. Only when φ = 0° or 180° is the polarization linear again. This is the working principle of wave plates. Option A is wrong because the two principal axes have different ε values — the crystal is not symmetric in the relevant sense. Option B conflates birefringence with optical rotation."

- question: "In an anisotropic crystal, why are the displacement vector D and the electric field E generally not parallel?"
  type: multiple-choice
  options:
    - "Because D includes the magnetic contribution to the field while E does not"
    - "Because the permittivity tensor ε_ij couples different components of E when producing D, so D = ε·E mixes directions"
    - "Because D is always perpendicular to the wave's propagation direction while E can have a longitudinal component"
    - "This only occurs at interfaces between materials; inside a uniform crystal D and E are always parallel"
  answer: 1
  explanation: "In an isotropic medium, ε is a scalar so D = εE: D and E point the same way. In an anisotropic medium, ε is a tensor: the i-th component of D is Σ_j ε_ij E_j. If ε has off-diagonal components (i.e., the coordinate axes are not the principal axes), then an E field pointing along one direction generates a D with components along multiple directions. The result is D ≠ εE in the scalar sense, and D and E are generally not parallel. Along principal axes, ε is diagonal and D is parallel to E — but only along those special directions."

- question: "Along a principal axis of a birefringent crystal, a linearly polarized wave with its electric field directed along another principal axis propagates as an eigenmode — its polarization state does not change."
  type: true-false
  answer: true
  explanation: "Principal axes are the directions along which the permittivity tensor is diagonal. For a wave traveling along one principal axis, the transverse directions are the other two principal axes, and for these polarizations D and E are parallel (since ε is diagonal in this frame). Each such polarization is an eigenmode of propagation: it travels at a definite phase velocity without mixing into the other polarization. Birefringence arises when you combine two such eigenmodes — not when you propagate one of them alone."

- question: "Birefringence means that two polarization eigenmodes propagate at different frequencies through the crystal, so blue light and red light experience the same phase shift."
  type: true-false
  answer: false
  explanation: "Birefringence means the two eigenmodes travel at *different phase velocities* (different refractive indices), not at different frequencies. Both components of a given wavelength propagate at the same frequency — they must, since frequency is set by the source and is conserved at interfaces. What differs is the phase velocity v = c/n, where n depends on both the polarization direction and (due to dispersion) on frequency ω. So blue and red light do experience different phase shifts at the same thickness — but this is because n(ω) depends on frequency, not because the eigenmodes have different frequencies."

- question: "Explain in physical terms why a wave polarized at 45° to the principal axes of a birefringent crystal does not propagate unchanged, but instead undergoes a change in polarization state."
  type: short-answer
  answer: "A wave polarized at 45° to the two principal axes is not an eigenmode of the crystal. It decomposes into two eigenmodes — one polarized along each principal axis — each of which propagates at its own phase velocity v₁ = c/n₁ and v₂ = c/n₂. Because n₁ ≠ n₂, the two components travel at different speeds and accumulate a phase difference Δφ = (2π/λ)(n₁ − n₂)L as they travel a distance L. The combined polarization state at any point is determined by the phase difference between the two components: at Δφ = 0 the polarization is linear (same as input); at Δφ = π/2 it is circular; at intermediate values it is elliptical. The polarization state continuously evolves as the wave propagates through the crystal."
  explanation: "This is birefringence in action. The key physical point is that a non-eigenmode polarization cannot maintain its state because its two component eigenmodes are accumulating different phases. Wave plates exploit this deliberately: a quarter-wave plate is tuned to produce Δφ = π/2, converting linear to circular polarization; a half-wave plate produces Δφ = π, rotating linear polarization by 90°."
```

## Explainer

You know that in an isotropic medium the permittivity ε is a scalar: the electric polarization P always points parallel to the applied field E, and the wave propagates with a single phase velocity v = c/n. Now remove the assumption of isotropy. In a crystal whose structure is different along different axes — say, calcite or quartz — the electrons are easier to displace in some directions than others. The response of the medium to an applied field therefore depends on the field's orientation: a field pointing along one crystal axis polarizes the medium more strongly than the same field along a different axis.

The compact way to express this is with a **permittivity tensor** ε_ij: the i-th component of D equals Σ_j ε_ij E_j. In general, D and E are not parallel — the displacement and the field can point in different directions. However, every real symmetric tensor can be diagonalized by rotating to its **principal axes**. Along these special directions, D and E are parallel and the material behaves like an isotropic medium — just with a different ε value for each axis (ε_x, ε_y, ε_z called the principal permittivities). These define the three **principal refractive indices** n_x, n_y, n_z.

The consequences for wave propagation are striking. For a wave traveling along a principal axis, any linearly polarized wave with E along one of the other principal axes is an eigenmode — it propagates without changing its polarization state. But it travels at a speed set by the permittivity for its polarization direction. A second linearly polarized wave with E along the other transverse principal axis is also an eigenmode, but it travels at a different speed. Now send in a wave polarized at 45° to both principal axes: it decomposes into equal parts of the two eigenmodes, which accumulate a **phase difference** as they travel. After a certain thickness, the two components are 90° out of phase and the initially linear polarization has become circular. After twice that thickness, they are 180° apart and the polarization has rotated 90°. This is **birefringence** — the splitting of one beam into two with different velocities — and it is the working principle behind wave plates and polarization optics. The frequency-dependent permittivity you studied earlier adds the further complication that the eigenmode phase velocities depend on ω, so different wavelengths develop different phase differences at the same thickness.

---
id: birefringence-and-dichroism
title: Birefringence and Dichroism
domain: physics
course: electrodynamics
prerequisites:
- id: em-waves-anisotropic-media
  type: hard
- id: electromagnetic-wave-polarization
  type: hard
tags:
- birefringence
- dichroism
- polarization
- optical-activity
stage: advanced
status: draft
---

# Birefringence and Dichroism

## Core Idea
Birefringence (anisotropic refractive index) causes different polarizations to propagate at different speeds, rotating linear polarization or converting between linear and circular. Dichroism (anisotropic absorption) attenuates different polarizations differently.

## Explainer

You have studied how electromagnetic waves in anisotropic media propagate differently depending on polarization direction, because the permittivity tensor ε has different diagonal components along different crystal axes. In an isotropic medium like glass, all polarizations see the same refractive index n, so a linearly polarized wave stays linearly polarized as it propagates. In a **birefringent** crystal like calcite or quartz, the two orthogonal linear polarization components — called the **ordinary ray** (polarized perpendicular to the optical axis) and the **extraordinary ray** (polarized with a component along the optical axis) — see different refractive indices n_o and n_e, and therefore travel at different speeds.

The consequence is **phase retardation**. Suppose a linearly polarized wave enters a birefringent crystal with its polarization at 45° to the optical axis, so the ordinary and extraordinary components have equal amplitude. They start in phase, but as they propagate, the faster component accumulates a phase lead. If the crystal thickness is chosen so the phase difference is exactly π/2 (a **quarter-wave plate**), the recombined output is circularly polarized — equal amplitudes but 90° out of phase. If the thickness gives a π phase shift (a **half-wave plate**), the output is linearly polarized again but rotated by twice the angle between the input polarization and the optical axis. These wave plates are the fundamental tools for engineering any desired polarization state in an optics lab.

**Dichroism** is a distinct but related phenomenon: different polarizations experience different absorption rather than different phase velocity. The imaginary part of the refractive index — which governs attenuation — is anisotropic. A **linear polarizer** exploits dichroism: the material strongly absorbs one linear polarization direction while transmitting the perpendicular one. Polaroid films are made of stretched polymer chains aligned to absorb horizontal polarization; the transmitted vertical polarization accounts for the glare-reducing effect of polarized sunglasses.

The two phenomena can coexist, described by a complex refractive index tensor where both the real part (phase) and imaginary part (absorption) are anisotropic. **Circular dichroism** — different absorption for left- versus right-circularly polarized light — is especially important in chemistry and structural biology. Chiral molecules such as amino acids and DNA interact differently with the two circular polarizations. A circular dichroism spectrum is a sensitive fingerprint of protein secondary structure (α-helices and β-sheets give characteristic signatures), making it a standard tool in biochemical research.

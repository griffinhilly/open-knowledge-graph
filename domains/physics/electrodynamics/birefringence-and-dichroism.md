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

## Questions

```yaml
- question: "A linearly polarized beam enters a birefringent crystal with its polarization at 45° to the optical axis. The crystal thickness is chosen so the ordinary and extraordinary rays accumulate a phase difference of exactly π/2. What is the polarization state of the output beam?"
  type: multiple-choice
  options:
    - "Linearly polarized, rotated 45° relative to the input polarization"
    - "Linearly polarized, aligned with the optical axis of the crystal"
    - "Circularly polarized"
    - "Unpolarized, because the two components have traveled at different speeds"
  answer: 2
  explanation: "When the input is at 45°, the ordinary and extraordinary components have equal amplitude. A π/2 phase difference between equal-amplitude orthogonal components produces circular polarization — the electric field vector traces a circle. This is the quarter-wave plate. Option A would result from a half-wave plate (π phase shift). Option D is wrong: the two components remain coherent (they come from the same original beam), so their recombination gives a definite polarization state, not incoherent unpolarized light."

- question: "Polaroid sunglasses reduce glare from horizontal surfaces because reflected light is preferentially horizontally polarized. The Polaroid material achieves this by:"
  type: multiple-choice
  options:
    - "Birefringence — the horizontal polarization travels slower and is redirected by the crystal structure"
    - "Dichroism — aligned polymer chains absorb the horizontal polarization strongly while transmitting the perpendicular (vertical) polarization"
    - "Total internal reflection of the horizontal polarization component at the lens surface"
    - "Constructive interference for vertical polarization and destructive interference for horizontal"
  answer: 1
  explanation: "Polaroid films exploit dichroism: the anisotropic absorption of a material aligned to absorb one polarization direction. Stretched polymer chains create a preferred absorption axis; the horizontal polarization (aligned with the chains) is strongly absorbed, while the vertical polarization passes through. This is distinct from birefringence, which affects phase velocity (the real part of the refractive index) rather than absorption (the imaginary part). A birefringent material would change the polarization state, not block one component."

- question: "Birefringence and dichroism are different names for the same physical phenomenon — both describe anisotropic optical properties of a material."
  type: true-false
  answer: false
  explanation: "They are distinct phenomena with the same underlying cause (anisotropy) but different physical mechanisms. Birefringence is anisotropy in the REAL part of the complex refractive index — different polarizations travel at different phase velocities, accumulating a relative phase. Dichroism is anisotropy in the IMAGINARY part — different polarizations experience different amounts of absorption. Both can coexist in the same material (described by a complex refractive index tensor with anisotropic real and imaginary parts), but a material can have one without the other."

- question: "A half-wave plate converts linearly polarized light to a different linear polarization, with the output polarization direction determined by the angle between the input polarization and the crystal's optical axis."
  type: true-false
  answer: true
  explanation: "A half-wave plate imposes a π phase difference between ordinary and extraordinary components. If the input polarization makes angle θ with the optical axis, the output polarization is rotated by 2θ from the input. At θ = 45°, the output is rotated 90° from the input. The output is always linearly polarized (not circular or elliptical) because a π phase shift between two components is equivalent to reflecting one component, which preserves linear polarization while rotating its direction."

- question: "Explain why a quarter-wave plate converts linearly polarized light to circularly polarized light. What does 'phase retardation' mean physically, and why does the 45° orientation of the input matter?"
  type: short-answer
  answer: "Phase retardation means the two orthogonal polarization components (ordinary and extraordinary) travel at different speeds through the birefringent crystal, so one accumulates a phase lead relative to the other. The amount of retardation depends on the refractive index difference (n_e − n_o) and the crystal thickness. A quarter-wave plate is thick enough to impose exactly π/2 (90°) phase difference. For the output to be circularly polarized, both components must have equal amplitude AND be 90° out of phase. Equal amplitudes require the input to be at 45° to the optical axis — that splits the original linear polarization equally between the ordinary and extraordinary directions. If the input were at any other angle, the amplitudes would be unequal, producing elliptical (not circular) polarization. So both conditions are needed: quarter-wave thickness for the phase, and 45° orientation for the equal-amplitude split."
  explanation: "The quarter-wave plate is the fundamental tool for interconverting linear and circular polarization. Applied twice (two quarter-wave plates in series), it acts as a half-wave plate. The key physical insight is that polarization state depends on the relative phase and amplitude of two orthogonal components — birefringence controls the phase, while the input angle controls the amplitudes."
```

## Explainer

You have studied how electromagnetic waves in anisotropic media propagate differently depending on polarization direction, because the permittivity tensor ε has different diagonal components along different crystal axes. In an isotropic medium like glass, all polarizations see the same refractive index n, so a linearly polarized wave stays linearly polarized as it propagates. In a **birefringent** crystal like calcite or quartz, the two orthogonal linear polarization components — called the **ordinary ray** (polarized perpendicular to the optical axis) and the **extraordinary ray** (polarized with a component along the optical axis) — see different refractive indices n_o and n_e, and therefore travel at different speeds.

The consequence is **phase retardation**. Suppose a linearly polarized wave enters a birefringent crystal with its polarization at 45° to the optical axis, so the ordinary and extraordinary components have equal amplitude. They start in phase, but as they propagate, the faster component accumulates a phase lead. If the crystal thickness is chosen so the phase difference is exactly π/2 (a **quarter-wave plate**), the recombined output is circularly polarized — equal amplitudes but 90° out of phase. If the thickness gives a π phase shift (a **half-wave plate**), the output is linearly polarized again but rotated by twice the angle between the input polarization and the optical axis. These wave plates are the fundamental tools for engineering any desired polarization state in an optics lab.

**Dichroism** is a distinct but related phenomenon: different polarizations experience different absorption rather than different phase velocity. The imaginary part of the refractive index — which governs attenuation — is anisotropic. A **linear polarizer** exploits dichroism: the material strongly absorbs one linear polarization direction while transmitting the perpendicular one. Polaroid films are made of stretched polymer chains aligned to absorb horizontal polarization; the transmitted vertical polarization accounts for the glare-reducing effect of polarized sunglasses.

The two phenomena can coexist, described by a complex refractive index tensor where both the real part (phase) and imaginary part (absorption) are anisotropic. **Circular dichroism** — different absorption for left- versus right-circularly polarized light — is especially important in chemistry and structural biology. Chiral molecules such as amino acids and DNA interact differently with the two circular polarizations. A circular dichroism spectrum is a sensitive fingerprint of protein secondary structure (α-helices and β-sheets give characteristic signatures), making it a standard tool in biochemical research.

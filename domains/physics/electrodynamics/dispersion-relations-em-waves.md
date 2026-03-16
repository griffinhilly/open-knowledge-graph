---
id: dispersion-relations-em-waves
title: Dispersion Relations for Electromagnetic Waves
domain: physics
course: electrodynamics
prerequisites:
- id: electromagnetic-waves-in-dielectrics
  type: hard
- id: plane-electromagnetic-waves
  type: hard
builds-toward:
- refractive-index-and-dispersion
tags:
- dispersion
- wave-velocity
- frequency-dependence
stage: advanced
status: draft
---

# Dispersion Relations for Electromagnetic Waves

## Core Idea
The dispersion relation ω(k) connects frequency and wavenumber for waves in a medium, determining the wave velocity v_phase = ω/k and group velocity v_group = dω/dk. Different frequency components travel at different speeds due to material dispersion, causing pulse broadening and chromatic effects. Understanding dispersion is crucial for signal propagation, optical design, and analyzing material properties.

## Explainer

From your study of plane electromagnetic waves and waves in dielectrics, you know that a monochromatic wave traveling in a medium can be written as e^{i(kx − ωt)}, where k is the wavenumber (spatial frequency) and ω is the angular frequency (temporal frequency). In vacuum, these are locked together by the simple relation ω = ck — frequency and wavenumber are always proportional, and every frequency travels at the same speed c. A **dispersion relation** ω(k) is the medium's specific version of this constraint. When ω(k) is not simply proportional to k — when the function is nonlinear — the medium is called dispersive, and different frequency components of a wave travel at different speeds.

The two distinct velocities that emerge from a dispersion relation deserve careful attention. The **phase velocity** v_phase = ω/k is the speed at which a single-frequency sinusoidal wave pattern moves — the rate at which a particular crest propagates. The **group velocity** v_group = dω/dk is the speed at which a localized packet of waves (a superposition of nearby frequencies) moves, and crucially, it is the speed at which energy and information travel. In vacuum they are equal (both equal c), but in a dispersive medium they can differ significantly. You can build the intuition with a simple picture: if you superpose two sine waves of slightly different frequency, you get a slowly beating envelope. The phase velocity is how fast the individual fringes move; the group velocity is how fast the envelope moves. For normal dispersion, v_group < v_phase; in anomalous dispersion regions, counterintuitive orderings can occur.

Why do real materials disperse? The answer lies in the response of bound electrons and ions. When an electromagnetic wave drives the charges in a material, they respond resonantly — near an atomic or molecular resonance frequency, the polarization is large and strongly frequency-dependent. The index of refraction n(ω) = ck/ω captures this frequency dependence, and its variation with ω is what causes dispersion. A glass prism spreads white light into a spectrum precisely because n is slightly different for red and violet light; violet photons travel more slowly and refract more. This is normal dispersion: dn/dω > 0, so higher-frequency (violet) light has a larger n and slower phase velocity.

The practical consequence of dispersion is **pulse broadening**. A light pulse in an optical fiber contains a range of frequencies — it is not a single monochromatic wave. In a dispersive medium, these frequency components walk apart: higher-frequency components slow down relative to lower-frequency ones. After propagating a long distance, what started as a sharp pulse has spread into a longer, blurrier pulse. In fiber-optic communications, this limits data rates: pulses must be spaced far enough apart that they don't overlap after broadening. Dispersion-managed fiber design and the careful choice of operating wavelength near dispersion-zero points (where dv_group/dω ≈ 0) are central engineering challenges, making the dispersion relation not just a theoretical curiosity but a daily design constraint.

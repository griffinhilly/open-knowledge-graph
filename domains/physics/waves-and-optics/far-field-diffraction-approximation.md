---
id: far-field-diffraction-approximation
title: Far-Field Diffraction and the Fraunhofer Approximation
domain: physics
course: waves-and-optics
prerequisites:
- id: fresnel-zones-wavefront
  type: soft
- id: single-aperture-diffraction-minima
  type: hard
tags:
- diffraction
- approximation
stage: advanced
status: draft
---

# Far-Field Diffraction and the Fraunhofer Approximation

## Core Idea
In the far field (observation distance >> aperture size / wavelength), diffraction patterns simplify because all diffracted rays are approximately parallel. The Fraunhofer approximation makes the diffraction integral a Fourier transform, explaining why grating and slit patterns have such clean mathematical forms. This regime applies for microscopy, telescopes, and typical laboratory optics.

## Explainer

When a wave passes through an aperture or past an obstacle, it diffracts — bending and spreading, creating an interference pattern downstream. From single-aperture-diffraction-minima, you know where the dark fringes in that pattern fall. This topic addresses the deeper question: why does the math simplify so cleanly at large distances, and what does that simplification reveal? The answer is the **Fraunhofer approximation**, which applies in the **far field**.

The distinction between near-field and far-field diffraction comes down to wavefront curvature. Close to the aperture, waves arriving at an observation point have traveled different path lengths, and those differences involve quadratic (squared) terms in the geometry — this is the **Fresnel regime**. In the far field, the observation point is so distant that all diffracted rays from across the aperture arrive along nearly parallel paths. The quadratic terms become negligible, and only the linear (first-order) path differences survive. The approximate criterion is z >> a²/λ, where z is the observation distance, a is the aperture size, and λ is the wavelength. For visible light through a 1 mm slit, this puts the far field beyond about 1 meter — well within a typical optics lab.

This geometric simplification has a remarkable mathematical consequence: the diffraction integral becomes a **Fourier transform** of the aperture's transmission function. Whatever shape you cut in the aperture — a uniform slit, a grating of N slits, a circular opening — the far-field pattern is exactly the Fourier transform of that spatial profile. A single uniform slit gives a sinc function (sin(u)/u); a diffraction grating gives a comb of sharp peaks; a circular aperture gives an **Airy disk** pattern. The Fourier relationship also explains why a grating with many closely spaced slits produces sharper, more widely separated diffraction orders: more slits means a longer periodic aperture, whose Fourier transform has narrower, better-resolved peaks.

In telescopes, microscopes, and most precision optical instruments, the geometry satisfies the far-field condition because the aperture (mirror or lens) is small relative to the image distances involved. This is why diffraction-limited resolution — the Rayleigh criterion — can be derived cleanly from Fourier analysis of the circular aperture. Whenever you see a clean, symmetric diffraction pattern in an optics experiment, the Fraunhofer approximation is at work, reducing complex wave interference to the elegant structure of a Fourier transform.

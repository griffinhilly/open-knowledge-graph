---
id: fresnel-zones-wavefront
title: Fresnel Zones and Wavefront Propagation
domain: physics
course: waves-and-optics
prerequisites:
- id: diffraction-resolution-angular-separation
  type: soft
builds-toward:
- far-field-diffraction-approximation
tags:
- diffraction
- fresnel
- wavefront
stage: advanced
status: draft
---

# Fresnel Zones and Wavefront Propagation

## Core Idea
Fresnel zones divide a wavefront into annular regions of equal path-length difference (λ/2 between consecutive zones). Each zone contributes a phasor to the total amplitude; adjacent zones tend to cancel. Fresnel zone analysis provides intuition for diffraction and explains why full wavefronts are often not needed—a single zone plate can focus waves like a lens.

## Explainer

From diffraction, you know that waves bend around obstacles and through apertures, and that the resolution of an optical system depends on how much of the wavefront contributes to the image. Fresnel zone analysis gives a systematic way to account for the *entire* wavefront's contribution — not just the direct path, but every point on the spreading wave — by dividing it into concentric annular regions based on how much extra path length they add.

Imagine a point source emitting a spherical wave, and a point of observation P some distance away. Consider all the points on the wavefront that lie at distances between r and r + λ/2 from P, where r is the shortest path length. Waves from all these points arrive at P within half a wavelength of each other — they're mostly in phase and add constructively. Call this ring the **first Fresnel zone**. The next ring, where distances fall between r + λ/2 and r + λ, forms the **second Fresnel zone**. Adjacent zones arrive roughly half a wavelength apart from each other, so they tend to cancel: contributions from zone 1 and zone 2 partially cancel, as do zones 2 and 3. The full wavefront's net amplitude is surprisingly small — about half the contribution of zone 1 alone, because most zones cancel in pairs.

This cancellation explains something counterintuitive: blocking *half* the wavefront can dramatically *increase* the amplitude at a point. A **zone plate** that blocks alternate Fresnel zones removes the canceling contributions, leaving only the in-phase zones to add constructively. This produces a bright focus at P, behaving like a lens but using diffraction rather than refraction. Zone plates are still used in X-ray optics where conventional refractive lenses don't work, because X-rays pass through most materials without bending usefully.

The deeper insight is that wavefront propagation in free space is dominated by the innermost few Fresnel zones — the outer zones mostly cancel each other. This is why line-of-sight matters in practical systems: an obstacle that blocks even part of the **first Fresnel zone** causes significant diffraction effects and signal loss, which is why wireless network engineers maintain clearance around the first Fresnel zone ellipsoid between transmitter and receiver. Outer zones can be obstructed with little effect, but the first zone is critical.

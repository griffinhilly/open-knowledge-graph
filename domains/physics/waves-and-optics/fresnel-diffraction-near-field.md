---
id: fresnel-diffraction-near-field
title: 'Fresnel Diffraction: Near-Field Diffraction Phenomena'
domain: physics
course: waves-and-optics
prerequisites:
- id: diffraction-and-huygen-principle
  type: hard
builds-toward:
- rayleigh-criterion-resolution
tags:
- fresnel-diffraction
- near-field
- diffraction
stage: formal-systems
status: draft
---

# Fresnel Diffraction: Near-Field Diffraction Phenomena

## Core Idea
Fresnel diffraction occurs when source or observation point is near the diffracting aperture, requiring consideration of wavefront curvature. More complex than Fraunhofer diffraction, it involves Fresnel zones and Cornu spirals. Important for understanding diffraction near edges and apertures.

## Explainer

In your study of Huygens' principle and Fraunhofer diffraction, you learned to treat every point on a wavefront as a secondary source of spherical wavelets. In the far field — when the observation screen is very far from the aperture relative to its size — those wavelets arrive at the screen with nearly flat (planar) wavefronts, and the geometry simplifies to a Fourier transform relationship between aperture shape and intensity pattern. **Fresnel diffraction** drops this simplifying assumption. When the screen is close enough that the curvature of the incoming wavefronts matters, the analysis must explicitly account for the varying path lengths from different points on the aperture to the observation point.

The central bookkeeping tool is the **Fresnel zone** construction. Imagine drawing concentric rings on the aperture such that successive rings contribute path lengths that differ by λ/2. The first zone contains all wavelet sources within λ/2 of the shortest path; the second zone adds another λ/2; and so on. Contributions from odd-numbered zones arrive roughly in phase with each other and tend to constructively interfere, while even-numbered zones arrive out of phase and tend to cancel. The total amplitude at the observation point depends on how many Fresnel zones are uncovered by the aperture — a dramatic dependence on geometry that has no analog in geometric optics.

One striking consequence is the **Poisson bright spot** (also called the Arago spot): a circular obstacle should, by geometric reasoning, cast a dark shadow. But diffraction theory predicts — and experiments confirm — that a bright spot appears at the geometric center of the shadow, because all the wavelet paths around the edge of the obstacle are nearly equal in length and interfere constructively. This was a famous historical test of wave optics in the early nineteenth century, and it remains a vivid demonstration that near-field diffraction can produce intensity maxima exactly where shadows are geometrically expected.

The **Cornu spiral** is the graphical tool for computing Fresnel diffraction amplitudes when dealing with straight edges rather than circular apertures. As you sweep the integration variable along the aperture, the amplitude vector traces a spiral in the complex plane (phasor space). The intensity at any observation point corresponds to the squared length of the chord connecting two points on the spiral. Near a sharp edge, the spiral's curling tail explains why the intensity doesn't simply snap from bright to dark — it oscillates with diminishing amplitude into the geometric shadow before settling to half the unobstructed intensity exactly at the edge. These oscillations (the bright and dark fringes near an edge) are the signature of Fresnel diffraction in everyday settings like the bright-dark fringe you can observe at the silhouette of a razor blade in coherent light.


---
id: wavefront-and-ray-description
title: Wavefronts and Ray Description of Wave Propagation
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-motion-definition
  type: soft
- id: geometric-optics-ray-approximation
  type: soft
builds-toward:
- huygens-principle
- geometric-optics-ray-approximation
tags:
- geometric-optics
- wavefronts
- ray-optics
stage: formal-systems
status: draft
---

# Wavefronts and Ray Description of Wave Propagation

## Core Idea
Wavefronts are surfaces of constant phase connecting all points oscillating in phase. Rays are lines perpendicular to wavefronts showing energy flow direction. The ray approximation is valid when wavelength is much smaller than obstacles, forming the basis of geometric optics.

## Explainer

You already have a sense of wave motion — a disturbance propagating through a medium with a definite speed, wavelength, and frequency. Now imagine watching a single-frequency wave spreading outward from a point source, like ripples on water. Every point at the same distance from the source oscillates identically — rising and falling in unison. Connect all those simultaneously-peaking points and you trace a **wavefront**: a surface (or line, in two dimensions) of constant phase. For a point source, wavefronts are concentric spheres expanding outward. Very far from the source, the curvature of those spheres becomes negligible and the wavefronts are approximately flat — these are called **plane waves**.

A **ray** is simply a line drawn perpendicular to the wavefront, pointing in the direction the wave energy travels. Rays and wavefronts are dual descriptions of the same physical reality: they carry identical information in different geometric forms. When a wavefront is flat, rays are straight parallel lines. When a wavefront is curved (as near a point source), rays fan outward like spokes of a wheel. This duality is not just a notational convenience — it is the bridge between two regimes of optics. The ray picture is natural when you want to track the direction of light travel; the wavefront picture is natural when you want to understand how phase relationships across an extended surface give rise to interference and diffraction.

The **ray approximation** holds when the wavelength is much smaller than the objects and apertures the wave encounters. In this limit, diffraction — the spreading of waves around corners — is negligible, and light travels in straight lines that bend only at boundaries between materials (governed by Snell's law). This is the regime of **geometric optics**: lenses, mirrors, prisms, and the optics of everyday instruments. The approximation breaks down when a slit or obstacle is only a few wavelengths wide, because diffraction then dramatically alters the wavefront shape in ways that no ray diagram can capture.

Huygens's principle — which builds directly on the wavefront picture — states that every point on a wavefront can be treated as a new point source of spherical wavelets, and the next wavefront is the envelope of all those wavelets. This principle explains why wavefronts bend when they cross from one medium into another (refraction) and why they spread around small obstacles (diffraction). The ray/wavefront duality therefore represents not just a choice of description but a choice of regime: geometric optics when wavelength is negligible, wave optics when it is not. Knowing which picture applies — and when to switch — is one of the central skills of the waves-and-optics course.

---
id: seismic-ray-theory
title: Seismic Ray Theory and Ray Tracing
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: elastic-wave-propagation-in-solids
  type: hard
- id: seismic-body-waves-p-and-s
  type: hard
- id: differential-equations-intro
  type: soft
- id: wave-equation-one-dimensional
  type: soft
- id: geometric-optics-ray-approximation
  type: hard
- id: wave-motion-definition
  type: hard
- id: wave-properties-intro
  type: hard
- id: snells-law
  type: hard
builds-toward:
- seismic-refraction-surveys
- seismic-tomography-velocity-imaging
tags:
- seismic
- ray
- theory
- propagation
stage: advanced
status: draft
---

# Seismic Ray Theory and Ray Tracing

## Core Idea
Ray theory describes wave propagation as rays traveling along paths determined by Snell's law and the velocity structure. Ray parameters (p-values) remain constant along rays, enabling inversion of travel times to velocity models.

## Explainer

You already understand that seismic waves travel through the Earth as P-waves and S-waves, and from your study of wave properties and geometric optics, you know that waves change direction when they encounter changes in the medium they travel through. **Seismic ray theory** applies the same high-frequency approximation used in optics — treating wave propagation as the tracing of rays along paths — to the problem of seismic waves traveling through Earth's interior. Just as a light ray bends when it passes from air into glass, a seismic ray bends when it crosses a boundary between rocks with different seismic velocities.

The foundation of ray theory is **Snell's law**, which you have already encountered: sin(θ)/v = constant along a ray path, where θ is the angle between the ray and the vertical, and v is the local seismic velocity. This constant is called the **ray parameter** (p), and its conservation is the single most important principle in seismic ray tracing. In a medium where velocity increases smoothly with depth — as it generally does in Earth's interior — Snell's law requires rays to curve continuously, bending away from the vertical as they descend into faster material and then curving back toward the surface. The result is that seismic rays follow curved paths that arc through the interior, diving to a maximum depth (the **turning point**, where the ray becomes horizontal) before rising back to the surface. The turning depth depends on the ray parameter: rays with smaller p values (launched more steeply) penetrate deeper, while rays with larger p values (launched at shallow angles) turn at shallower depths.

This geometry means that a seismometer at a given distance from an earthquake receives energy that has sampled a specific depth range of the Earth's interior. By recording the **travel time** — the time elapsed between the earthquake and the arrival of the seismic wave — at many stations at different distances, seismologists build a **travel-time curve**: a plot of arrival time versus angular distance. The shape of this curve encodes the velocity structure of the interior. Where velocity increases gradually, the travel-time curve is smooth and concave downward. A sharp velocity increase (like the Moho at the base of the crust) produces a discontinuity in the curve, and a **low-velocity zone** causes a shadow zone where no direct rays arrive at certain distances — exactly analogous to how a lens can create regions of focused and defocused light.

The practical power of ray theory lies in the **inverse problem**: given observed travel times, reconstruct the velocity model. The Herglotz-Wiechert inversion formula provides an exact solution for a spherically symmetric Earth, converting the observed p(Δ) function (ray parameter as a function of distance) into a velocity-depth profile v(z). Modern seismology extends this approach with numerical ray tracing through three-dimensional velocity models, iteratively adjusting the model until computed travel times match observations. This is the foundation of **seismic tomography**, which images velocity variations throughout Earth's mantle and core — but that extension builds directly on the ray-theoretical framework of Snell's law, ray parameters, and the relationship between travel times and velocity structure.

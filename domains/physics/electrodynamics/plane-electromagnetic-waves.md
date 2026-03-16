---
id: plane-electromagnetic-waves
title: Plane Electromagnetic Waves
domain: physics
course: electrodynamics
prerequisites:
- id: electromagnetic-wave-equation
  type: hard
- id: harmonic-functions-complex-analysis
  type: soft
- id: complex-exponential-form
  type: soft
builds-toward:
- electromagnetic-wave-polarization
- poynting-vector-energy-flow
tags:
- plane-waves
- wave-solutions
- em-waves
stage: advanced
status: draft
---

# Plane Electromagnetic Waves

## Core Idea
Plane waves are the simplest solutions to Maxwell's equations, with electric and magnetic fields perpendicular to each other and to the direction of propagation, oscillating sinusoidally in space and time. In a plane wave, E and B are related by B = k × E/ω, and their magnitudes are equal in SI units. Most radiation problems can be analyzed locally using plane wave approximations.

## Explainer

From the electromagnetic wave equation, you know that Maxwell's equations in free space predict that **E** and **B** both satisfy ∇²**F** = (1/c²)∂²**F**/∂t² — a wave equation guaranteeing propagation at speed c. But this tells you nothing about the geometric structure of the fields: what direction do they point, and how do **E** and **B** relate to each other? **Plane waves** are the simplest solutions and answer these questions completely: sinusoidal disturbances in which the fields vary only in the direction of propagation and oscillate in phase with each other.

The solution takes the form **E**(r,t) = **E**₀ exp(i(**k**·**r** − ωt)), where **k** is the **wave vector** pointing in the direction of propagation and ω = c|**k**| is the angular frequency. The complex exponential notation (your prerequisite) transforms differential equations into algebraic ones: ∂/∂t → −iω and ∇ → i**k**, making manipulation tractable. The physical field is the real part of this expression. The corresponding magnetic field follows from Faraday's law: **B** = (**k̂** × **E**)/c. This means **B** is perpendicular to both **E** and the propagation direction **k̂**, and its magnitude is |**E**|/c. This three-way perpendicularity — **E** ⊥ **B** ⊥ **k̂** — is the defining geometric signature of a plane wave in free space.

The "plane" in plane wave refers to the **wavefronts** — surfaces of constant phase — which are infinite flat planes perpendicular to **k̂**. At a given moment, all points on a wavefront have identical field values. In contrast, a point source produces spherical wavefronts; at large distances from any finite source, these spheres become locally indistinguishable from flat planes, which is why treating sunlight or radar pulses as plane waves is an excellent approximation far from the source. More fundamentally, any electromagnetic field can be decomposed into a superposition of plane waves via Fourier analysis — just as any sound can be built from pure tones — making plane waves the natural basis functions of all wave optics and radiation theory.

The constraint **E** ⊥ **k̂** — that the electric field has no component along the propagation direction — reflects the fact that free-space EM waves are **transverse**. This follows directly from Gauss's law: ∇ · **E** = 0 in free space translates for a plane wave to i**k** · **E**₀ = 0, forcing **E**₀ to lie in the plane perpendicular to **k**. Transversality limits the electric field to a two-dimensional plane, opening the door to **polarization** — whether **E** oscillates along a fixed axis (linear polarization), traces a circle (circular polarization), or traces an ellipse (elliptical polarization). The plane wave framework is the entry point to understanding energy transport via the Poynting vector **S** = **E** × **B**/μ₀, radiation pressure, and ultimately the interaction of light with matter in optics and spectroscopy.

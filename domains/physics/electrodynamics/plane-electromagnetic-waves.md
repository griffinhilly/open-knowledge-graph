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
stage: expert
status: validated
---

# Plane Electromagnetic Waves

## Core Idea
Plane waves are the simplest solutions to Maxwell's equations, with electric and magnetic fields perpendicular to each other and to the direction of propagation, oscillating sinusoidally in space and time. In a plane wave, E and B are related by B = k × E/ω, and their magnitudes are equal in SI units. Most radiation problems can be analyzed locally using plane wave approximations.

## Questions

```yaml
- question: "A student claims that an electromagnetic wave in free space could have its electric field pointing partly in the direction of propagation. Which of Maxwell's equations directly contradicts this claim?"
  type: multiple-choice
  options:
    - "Faraday's law (∇ × E = −∂B/∂t)"
    - "Gauss's law for electric fields (∇ · E = 0 in free space)"
    - "Ampère's law with Maxwell's correction (∇ × B = μ₀ε₀ ∂E/∂t)"
    - "Gauss's law for magnetic fields (∇ · B = 0)"
  answer: 1
  explanation: "In free space, Gauss's law states ∇ · E = 0. For a plane wave E = E₀ exp(i(k·r − ωt)), the divergence condition becomes ik · E₀ = 0, which forces E₀ to be perpendicular to k. This is transversality — the electric field cannot have any component along the propagation direction k̂. Faraday's law constrains the relationship between E and B; Gauss's law for E is what directly enforces transversality of the electric field."

- question: "A plane electromagnetic wave travels in the +z direction. At a given point and time, the electric field is E = E₀ x̂. What is the direction of the magnetic field at the same point and time?"
  type: multiple-choice
  options:
    - "+x̂ (parallel to E)"
    - "+ẑ (along the direction of propagation)"
    - "+ŷ (perpendicular to both E and k̂)"
    - "−ẑ (antiparallel to the propagation direction)"
  answer: 2
  explanation: "The magnetic field of a plane wave is given by B = (k̂ × E)/c. With k̂ = ẑ and E = E₀ x̂, we get B = (ẑ × x̂)E₀/c = ŷ E₀/c. The result is +ŷ, perpendicular to both E (which points in x̂) and the propagation direction (ẑ). This three-way mutual perpendicularity — E ⊥ B ⊥ k̂ — is the defining geometric structure of a plane wave in free space. Option A (E ∥ B) and B/D (either field along k̂) both violate transversality."

- question: "Treating sunlight as a plane wave is an excellent approximation for objects on Earth, even though the Sun emits spherical wavefronts."
  type: true-false
  answer: true
  explanation: "A point source emits spherical wavefronts, but at distances much larger than the source, any small patch of a sphere is locally indistinguishable from a flat plane. Since the Earth is ~150 million km from the Sun, the curvature of the wavefront across any human-scale apparatus is negligible. The plane wave approximation holds whenever the observation region is much smaller than the distance to the source — which is almost always true for astrophysical sources. This is why plane waves are the workhorse of optics and antenna theory."

- question: "In a plane electromagnetic wave, the electric and magnetic fields are 90° out of phase with each other — E peaks when B is zero, and vice versa."
  type: true-false
  answer: false
  explanation: "This is a common confusion imported from LC circuits, where voltage and current are 90° out of phase. In an electromagnetic plane wave, E and B oscillate in phase — they peak and cross zero simultaneously. This follows from B = (k̂ × E)/c: B is directly proportional to E at every point and time, with no phase lag. The 90° out-of-phase relationship is a feature of standing waves in cavities, not of traveling plane waves in free space."

- question: "Why must the electric field of an electromagnetic plane wave in free space be perpendicular to the direction of propagation? What does this constraint imply about polarization?"
  type: short-answer
  answer: "In free space, Gauss's law requires ∇ · E = 0. For a plane wave with wave vector k, this condition translates to k · E₀ = 0, meaning E₀ must be perpendicular to k — the wave is transverse. Because E is confined to the plane perpendicular to k (a two-dimensional plane), the electric field can point in any direction within that plane. This two-dimensional freedom is exactly polarization: linear polarization occurs when E oscillates along a fixed direction in that plane, circular polarization when E rotates with constant magnitude, and elliptical polarization for the general case."
  explanation: "Transversality does not come from an ad-hoc assumption — it is a direct consequence of Maxwell's equations in free space. The constraint that E lies in a plane perpendicular to k is what opens up the rich phenomenology of polarization states, with applications in optics, communications, and astronomy (polarimetry of starlight, for instance)."
```

## Explainer

From the electromagnetic wave equation, you know that Maxwell's equations in free space predict that **E** and **B** both satisfy ∇²**F** = (1/c²)∂²**F**/∂t² — a wave equation guaranteeing propagation at speed c. But this tells you nothing about the geometric structure of the fields: what direction do they point, and how do **E** and **B** relate to each other? **Plane waves** are the simplest solutions and answer these questions completely: sinusoidal disturbances in which the fields vary only in the direction of propagation and oscillate in phase with each other.

The solution takes the form **E**(r,t) = **E**₀ exp(i(**k**·**r** − ωt)), where **k** is the **wave vector** pointing in the direction of propagation and ω = c|**k**| is the angular frequency. The complex exponential notation (your prerequisite) transforms differential equations into algebraic ones: ∂/∂t → −iω and ∇ → i**k**, making manipulation tractable. The physical field is the real part of this expression. The corresponding magnetic field follows from Faraday's law: **B** = (**k̂** × **E**)/c. This means **B** is perpendicular to both **E** and the propagation direction **k̂**, and its magnitude is |**E**|/c. This three-way perpendicularity — **E** ⊥ **B** ⊥ **k̂** — is the defining geometric signature of a plane wave in free space.

The "plane" in plane wave refers to the **wavefronts** — surfaces of constant phase — which are infinite flat planes perpendicular to **k̂**. At a given moment, all points on a wavefront have identical field values. In contrast, a point source produces spherical wavefronts; at large distances from any finite source, these spheres become locally indistinguishable from flat planes, which is why treating sunlight or radar pulses as plane waves is an excellent approximation far from the source. More fundamentally, any electromagnetic field can be decomposed into a superposition of plane waves via Fourier analysis — just as any sound can be built from pure tones — making plane waves the natural basis functions of all wave optics and radiation theory.

The constraint **E** ⊥ **k̂** — that the electric field has no component along the propagation direction — reflects the fact that free-space EM waves are **transverse**. This follows directly from Gauss's law: ∇ · **E** = 0 in free space translates for a plane wave to i**k** · **E**₀ = 0, forcing **E**₀ to lie in the plane perpendicular to **k**. Transversality limits the electric field to a two-dimensional plane, opening the door to **polarization** — whether **E** oscillates along a fixed axis (linear polarization), traces a circle (circular polarization), or traces an ellipse (elliptical polarization). The plane wave framework is the entry point to understanding energy transport via the Poynting vector **S** = **E** × **B**/μ₀, radiation pressure, and ultimately the interaction of light with matter in optics and spectroscopy.

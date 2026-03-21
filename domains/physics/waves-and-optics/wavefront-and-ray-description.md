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

## Questions

```yaml
- question: "A scientist models light passing through a narrow slit using a ray diagram and predicts a sharp geometric shadow on a screen beyond. Under which condition would this prediction be most accurate?"
  type: multiple-choice
  options:
    - "When the slit width is many times larger than the wavelength of the light"
    - "When the slit width equals the wavelength of the light"
    - "When the light source is very bright and highly coherent"
    - "When the screen is placed very close to the slit"
  answer: 0
  explanation: "The ray approximation holds when the wavelength is much smaller than the relevant apertures and obstacles, making diffraction negligible. When the slit is much wider than the wavelength, the wave spreads only slightly and a ray diagram captures the geometry well. When the slit approaches the wavelength (option B), diffraction dominates and the ray model fails completely — the wave spreads around the edges in ways no ray diagram can predict. Brightness and screen distance do not determine the validity of the approximation."

- question: "A point source of light is observed from very far away. Which description best characterizes the wavefronts and rays at that large distance?"
  type: multiple-choice
  options:
    - "Wavefronts become cylindrical because the source energy spreads primarily in one plane"
    - "Rays converge back toward the source because of energy conservation"
    - "Wavefronts become approximately flat planes, and rays become approximately parallel lines"
    - "Wavefronts disappear at large distances and only rays remain"
  answer: 2
  explanation: "Near a point source, wavefronts are concentric spheres and rays fan outward like spokes. At very large distances, the radius of curvature of those spheres becomes so large that the wavefronts appear locally flat — these are called plane waves — and the corresponding rays are approximately parallel. This is why sunlight (from a source ~150 million km away) is modeled as parallel rays. Rays never converge back toward a source in a uniform medium, and wavefronts and rays are dual descriptions that always coexist."

- question: "A ray and a wavefront are two independent physical entities that coexist in wave propagation; the ray points in the direction of energy travel and is always perpendicular to the associated wavefront."
  type: true-false
  answer: true
  explanation: "This is correct. Rays and wavefronts are dual representations of the same wave propagation: wavefronts are surfaces of constant phase, and rays are lines drawn perpendicular to those surfaces indicating the direction of energy flow. They are not independent objects but complementary descriptions — each encodes the same physical information in different geometric form. Near a point source, spherical wavefronts pair with outward-radiating rays; for plane waves, flat wavefronts pair with parallel rays."

- question: "The ray approximation for light is valid as long as the light source produces coherent, monochromatic light, regardless of the size of the obstacles or apertures the light encounters."
  type: true-false
  answer: false
  explanation: "The validity of the ray approximation depends on the ratio of wavelength to obstacle/aperture size — not on the coherence of the source. The approximation holds when λ << (size of obstacles), making diffraction negligible. Coherent, monochromatic light can exhibit dramatic diffraction effects when it passes through a slit of comparable width to its wavelength — this is precisely the setup used to demonstrate diffraction. Coherence makes interference patterns sharper, but does not suppress diffraction."

- question: "Why does the ray approximation break down when a slit is narrowed to roughly the wavelength of light, and what physical phenomenon replaces it?"
  type: short-answer
  answer: "When the slit width is comparable to the wavelength, diffraction becomes significant: the wave spreads around the edges of the slit rather than continuing in a straight line. Huygens's principle explains this — each point on the wavefront at the slit acts as a new point source of spherical wavelets, and these wavelets interfere to produce a spreading pattern far wider than the geometric shadow. The ray model predicts a sharp shadow; wave optics predicts a broad diffraction pattern with alternating bright and dark fringes. No ray diagram can capture this behavior."
  explanation: "The key transition is from geometric optics (rays, sharp shadows) to wave optics (wavefronts, diffraction, interference). The condition λ << aperture size ensures that wavefront spreading is negligible and rays describe the geometry accurately. As the aperture shrinks toward λ, the wavefront curvature introduced by diffraction at the edges becomes comparable to the aperture itself, and the entire geometric picture breaks down. This is why microscopes using visible light cannot resolve features smaller than roughly the wavelength of light — diffraction sets a fundamental resolution limit."
```

## Explainer

You already have a sense of wave motion — a disturbance propagating through a medium with a definite speed, wavelength, and frequency. Now imagine watching a single-frequency wave spreading outward from a point source, like ripples on water. Every point at the same distance from the source oscillates identically — rising and falling in unison. Connect all those simultaneously-peaking points and you trace a **wavefront**: a surface (or line, in two dimensions) of constant phase. For a point source, wavefronts are concentric spheres expanding outward. Very far from the source, the curvature of those spheres becomes negligible and the wavefronts are approximately flat — these are called **plane waves**.

A **ray** is simply a line drawn perpendicular to the wavefront, pointing in the direction the wave energy travels. Rays and wavefronts are dual descriptions of the same physical reality: they carry identical information in different geometric forms. When a wavefront is flat, rays are straight parallel lines. When a wavefront is curved (as near a point source), rays fan outward like spokes of a wheel. This duality is not just a notational convenience — it is the bridge between two regimes of optics. The ray picture is natural when you want to track the direction of light travel; the wavefront picture is natural when you want to understand how phase relationships across an extended surface give rise to interference and diffraction.

The **ray approximation** holds when the wavelength is much smaller than the objects and apertures the wave encounters. In this limit, diffraction — the spreading of waves around corners — is negligible, and light travels in straight lines that bend only at boundaries between materials (governed by Snell's law). This is the regime of **geometric optics**: lenses, mirrors, prisms, and the optics of everyday instruments. The approximation breaks down when a slit or obstacle is only a few wavelengths wide, because diffraction then dramatically alters the wavefront shape in ways that no ray diagram can capture.

Huygens's principle — which builds directly on the wavefront picture — states that every point on a wavefront can be treated as a new point source of spherical wavelets, and the next wavefront is the envelope of all those wavelets. This principle explains why wavefronts bend when they cross from one medium into another (refraction) and why they spread around small obstacles (diffraction). The ray/wavefront duality therefore represents not just a choice of description but a choice of regime: geometric optics when wavelength is negligible, wave optics when it is not. Knowing which picture applies — and when to switch — is one of the central skills of the waves-and-optics course.

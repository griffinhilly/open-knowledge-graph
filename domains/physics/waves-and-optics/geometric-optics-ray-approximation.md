---
id: geometric-optics-ray-approximation
title: Geometric Optics and the Ray Approximation
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-and-snells-law
  type: hard
- id: reflection-and-law-of-reflection
  type: hard
builds-toward:
- thin-lens-equation
- mirror-equation
tags:
- geometric-optics
- ray-approximation
- propagation
stage: formal-systems
status: draft
---

# Geometric Optics and the Ray Approximation

## Core Idea
Geometric optics approximates light as rays perpendicular to wavefronts, valid when wavelength is much smaller than optical element size. Rays follow straight paths through uniform media and obey the laws of reflection and refraction at interfaces. Geometric optics successfully describes lenses, mirrors, and optical instruments but cannot explain diffraction or interference.

## Explainer

You already know that light reflects from surfaces following the law of reflection (angle in = angle out) and bends at interfaces following Snell's law. Those two rules are enough to explain a remarkable range of optical phenomena — but only if we're willing to treat light as something simpler than it actually is. **Geometric optics** is the formal commitment to that simplification: rather than tracking wavefronts and their oscillations, we track **rays** — idealized lines that represent the direction light is traveling. A ray is always perpendicular to the wavefront it belongs to.

This approximation is valid when the wavelength of light (roughly 400–700 nm for visible light) is vastly smaller than the optical elements it encounters — lenses, mirrors, apertures, and the like. A lens might be several centimeters across, which is roughly 100,000 times larger than a wavelength. At that scale, the wave nature of light is negligible and the ray model gives essentially exact predictions. The approximation breaks down when the two scales become comparable: a tiny pinhole, a fine diffraction grating, or a thin film all have features near the wavelength of light, and wave effects (diffraction, interference) dominate. Geometric optics is silent about those phenomena — it cannot even acknowledge them.

Within its domain of validity, the ray model is enormously powerful. To trace what a lens or mirror does to an image, you apply two rules at every interface: Snell's law for refraction, and the law of reflection for mirrors. **Principal rays** — parallel-to-axis rays, rays through the focal point, and rays through the optical center — are especially useful because their behavior after encountering a lens or mirror can be predicted immediately. Where those rays converge, a **real image** forms; where they appear to diverge from, a **virtual image** forms.

The practical payoff is that complex optical instruments — cameras, telescopes, microscopes, eyeglasses — can be designed and analyzed by tracing just a few rays through each element. The thin lens equation, the mirror equation, and the lensmaker's equation all emerge from this ray-tracing logic. Understanding the ray approximation is therefore the conceptual foundation for everything in geometric optics: it tells you when the tools are valid, why they work, and where they stop working. When a phenomenon can't be explained by ray tracing alone — a halo around a street light on a foggy night, the colors in a soap bubble, the resolution limit of a microscope — wave optics takes over.

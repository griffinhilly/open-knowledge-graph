---
id: refraction-and-snells-law
title: Refraction and Snell's Law
domain: physics
course: waves-and-optics
prerequisites:
- id: wavelength-frequency-speed-relationship
  type: hard
- id: wave-properties-and-classification
  type: soft
builds-toward:
- snells-law
- critical-angle-total-internal-reflection-optical
tags:
- refraction
- snells-law
- refractive-index
stage: formal-systems
status: draft
---

# Refraction and Snell's Law

## Core Idea
Refraction occurs when a wave crosses an interface between two media with different wave speeds, causing the wave to bend. Snell's law relates incident and refracted angles: n₁ sin θ₁ = n₂ sin θ₂, where n is the refractive index of each medium. Refraction happens because the wave slows down (or speeds up), changing its direction while maintaining frequency.

## Explainer

From your study of wave properties, you know that waves have three interdependent quantities: frequency f, wavelength λ, and speed v, related by v = fλ. When a wave crosses the boundary between two media, its frequency cannot change — the wave crests arrive at the boundary at the same rate they depart, so f is fixed by the source. But the wave speed changes because the new medium has different physical properties. Since v = fλ and f is constant, a slower medium means a shorter wavelength. This wavelength compression is the mechanical cause of refraction.

The direction change can be understood with a simple marching band analogy. Imagine a line of marchers walking diagonally from pavement onto mud, where they can only walk at half the speed. The marchers who hit the mud first slow down while the others are still on pavement. The whole line pivots toward the slower side. Waves do exactly this: the portion of the wavefront that enters the denser medium first slows and the wavefront rotates, bending the ray toward the normal (the perpendicular to the surface). **Snell's law**, n₁ sin θ₁ = n₂ sin θ₂, is the quantitative statement of this rotation, where angles are measured from the normal and n = c/v is the **refractive index** (how many times slower light travels in the medium compared to a vacuum).

The direction of bending follows from the index values. When light goes from a lower-index medium to a higher-index one (air into glass, n₁ < n₂), it slows down and bends toward the normal — the refracted angle is smaller than the incident angle. Going the other way (glass into air), light speeds up and bends away from the normal. A flat slab of glass produces two parallel refractions that cancel out, leaving the beam displaced but not deflected. A prism refracts the beam twice at non-parallel surfaces, producing a net deflection — and because different wavelengths have slightly different refractive indices in glass (**dispersion**), they exit at different angles, spreading white light into its spectrum.

Everyday examples abound. A straw appears bent in a glass of water because the light rays from the submerged part refract at the water-air interface, changing direction before reaching your eye. The apparent depth of a swimming pool is less than the actual depth for the same reason — refracted rays make the bottom appear closer. Eyeglass lenses and camera optics deliberately engineer specific curvatures to exploit refraction at precise angles, making Snell's law the governing equation behind essentially all of optics that involves glass or water. The next topics in this course — total internal reflection and lenses — are both direct extensions of this single equation.



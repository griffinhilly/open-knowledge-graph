---
id: dispersion-and-prisms
title: Dispersion and Prisms
domain: physics
course: waves-and-optics
prerequisites:
- id: snells-law
  type: hard
- id: total-internal-reflection
  type: soft
tags:
- dispersion
- prism
- spectrum
- rainbow
- index of refraction
stage: formal-systems
status: validated
---

# Dispersion and Prisms

## Core Idea
The refractive index of a medium is slightly wavelength-dependent: shorter wavelengths (violet) refract more than longer wavelengths (red). This wavelength dependence of n is called dispersion. A prism separates white light into its constituent colors because each wavelength refracts by a slightly different angle. Rainbows form by the same mechanism — dispersion and total internal reflection inside spherical water droplets.

## How It's Best Learned
Pass white light through a glass prism and project the spectrum onto a screen. Identify the order of colors (red bends least, violet most). Use Snell's law with two different indices for red and violet to compute the angular separation.

## Common Misconceptions
- The prism does not add color to white light; it separates colors already present.
- Red bends less than violet, opposite to many students' intuition based on 'red is dangerous' or 'red is energetic'.

## Explainer

From Snell's law, you know that when light crosses from one medium to another, it bends by an amount that depends on the refractive index: n₁ sin θ₁ = n₂ sin θ₂. The key assumption you may have treated as fixed — that each material has a single refractive index — turns out to be a simplification. In reality, the refractive index of any transparent material is slightly different for different wavelengths of light. This wavelength dependence of n is called **dispersion**, and it is the physical basis for everything in this topic.

The relationship is consistent across most transparent materials: shorter wavelengths (violet, ~400 nm) experience a slightly higher refractive index than longer wavelengths (red, ~700 nm). A typical glass prism might have n = 1.523 for red and n = 1.532 for violet — a difference of less than 1%, but enough to produce a visible angular separation. When white light (containing all visible wavelengths) enters the prism, each wavelength bends by a different amount according to Snell's law. Violet bends most sharply; red bends least. The prism does not create colors — it **disperses** colors that were already mixed together in white light, spatially separating them into the familiar spectrum: red, orange, yellow, green, blue, violet.

The geometry of a prism amplifies this effect. Light refracts once when entering and again when exiting the prism, and both refractions act in the same angular direction — so the angular spread between red and violet accumulates across both surfaces. If you were to replace the triangular prism with a flat glass slab, the two surfaces would be parallel, and refraction at exit would exactly undo refraction at entry, recombining the colors. The triangular shape is essential: the non-parallel surfaces ensure the second refraction continues to spread the wavelengths apart rather than reversing them.

**Rainbows** are produced by the same physics, but inside spherical water droplets. Sunlight enters the droplet, disperses into its color components, undergoes total internal reflection off the back surface (your prerequisite concept), and exits at a wavelength-dependent angle — roughly 42° for red and 40° for violet, measured from the incoming sunlight direction. You see a rainbow arc because each color reaches your eye from a different part of the sky, corresponding to droplets at slightly different angles. The red arc is always on the outside (higher elevation) of the primary rainbow because red exits at the larger angle. A secondary rainbow, when visible, appears outside the primary and has colors reversed — it has undergone two internal reflections, which reverses the geometry.

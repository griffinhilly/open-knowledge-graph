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

## Questions

```yaml
- question: "A student passes white light through a glass prism and observes a spectrum on a screen. They claim the prism must be adding color to the light because white light has no colors in it. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "The student is correct — prisms generate color through fluorescence"
    - "White light is a mixture of all visible wavelengths; the prism spatially separates wavelengths already present by refracting each one by a different angle"
    - "The prism adds color, but only because of the glass's chemical composition reacting with photons"
    - "The student is correct that white light has no colors, but the spectrum comes from reflections inside the prism"
  answer: 1
  explanation: "White light contains all visible wavelengths simultaneously — it is a mixture, not a pure state. The prism exploits the wavelength-dependence of the refractive index (dispersion): shorter wavelengths (violet) experience a slightly higher n and bend more; longer wavelengths (red) bend less. The prism is a separator, not a generator. This is confirmed by the reverse experiment: focusing the dispersed spectrum back through a second prism recombines the colors into white light."

- question: "Red light enters a glass prism. Compared to violet light entering the same prism at the same angle, red light exits with a smaller deflection angle. What is the direct physical reason?"
  type: multiple-choice
  options:
    - "Red photons have higher energy and resist bending more than lower-energy violet photons"
    - "Red light travels faster in vacuum than violet light, so it enters the glass at a larger angle"
    - "Red light has a longer wavelength, experiences a lower refractive index in glass, and therefore bends less at each surface according to Snell's law"
    - "The prism absorbs red photons before they can be fully deflected, reducing their deflection"
  answer: 2
  explanation: "Snell's law states n₁ sin θ₁ = n₂ sin θ₂. A smaller n₂ (as glass has for red light) means a larger exit angle — less bending. Red light in typical glass has n ≈ 1.523 while violet has n ≈ 1.532, a small but sufficient difference to produce visible angular separation. The energy of the photon (red is lower energy than violet) does not directly enter Snell's law; it is the wavelength-dependence of n that drives dispersion. The refraction occurs twice — at entry and exit — and both refractions add to the angular spread."

- question: "If white light passes through a glass slab with perfectly parallel faces (not a prism), the exiting beam is white, not a spectrum."
  type: true-false
  answer: true
  explanation: "In a flat slab, both faces are parallel. Dispersion does occur at the first surface — each wavelength bends by a different angle. But at the second parallel surface, each wavelength bends back by exactly the same amount in the opposite direction, recombining all wavelengths to reconstruct the original direction and white appearance. A triangular prism has non-parallel surfaces, so the second refraction continues spreading the wavelengths apart rather than reversing the first. The geometry of the prism is essential; flat glass cannot produce a persistent spectrum."

- question: "In a primary rainbow, red appears at the top (outside) of the arc and violet at the bottom (inside) — which is the opposite of the order colors exit a prism."
  type: true-false
  answer: false
  explanation: "The order is not reversed relative to a prism. In both a prism and a rainbow, red bends the least and violet the most. In a primary rainbow, red appears at the outside (higher elevation angle, ~42° from the antisolar point) and violet at the inside (~40°). This matches the prism order: red bends least, exits at the shallowest angle relative to the incoming beam, and corresponds to droplets at the highest angular position above the antisolar point. The geometry differs from a prism (it involves total internal reflection inside spherical droplets), but the underlying dispersion — violet refracts more than red — is the same."

- question: "Why does a triangular glass prism produce a visible spectrum when white light passes through it, while a rectangular glass slab with parallel faces does not?"
  type: short-answer
  answer: "A prism's two refracting surfaces are angled relative to each other (non-parallel). At the first surface, each wavelength refracts by a slightly different amount (violet more, red less). At the second, non-parallel surface, refraction acts in the same angular direction, further increasing the angular spread. The divergence between red and violet accumulates across both surfaces. In a flat slab, the two parallel surfaces cause the second refraction to exactly cancel the first — each wavelength returns to its original direction and all colors recombine. The non-parallel geometry of a prism is the essential feature that prevents cancellation."
  explanation: "This is the geometric key to all dispersion devices. The triangular shape isn't cosmetic — it ensures the two surfaces cooperate in spreading wavelengths apart rather than working against each other. A direct consequence: two prisms arranged apex-to-base will reconstruct white light from a dispersed spectrum, confirming that the prism separates but doesn't destroy the original mixture."
```

## Explainer

From Snell's law, you know that when light crosses from one medium to another, it bends by an amount that depends on the refractive index: n₁ sin θ₁ = n₂ sin θ₂. The key assumption you may have treated as fixed — that each material has a single refractive index — turns out to be a simplification. In reality, the refractive index of any transparent material is slightly different for different wavelengths of light. This wavelength dependence of n is called **dispersion**, and it is the physical basis for everything in this topic.

The relationship is consistent across most transparent materials: shorter wavelengths (violet, ~400 nm) experience a slightly higher refractive index than longer wavelengths (red, ~700 nm). A typical glass prism might have n = 1.523 for red and n = 1.532 for violet — a difference of less than 1%, but enough to produce a visible angular separation. When white light (containing all visible wavelengths) enters the prism, each wavelength bends by a different amount according to Snell's law. Violet bends most sharply; red bends least. The prism does not create colors — it **disperses** colors that were already mixed together in white light, spatially separating them into the familiar spectrum: red, orange, yellow, green, blue, violet.

The geometry of a prism amplifies this effect. Light refracts once when entering and again when exiting the prism, and both refractions act in the same angular direction — so the angular spread between red and violet accumulates across both surfaces. If you were to replace the triangular prism with a flat glass slab, the two surfaces would be parallel, and refraction at exit would exactly undo refraction at entry, recombining the colors. The triangular shape is essential: the non-parallel surfaces ensure the second refraction continues to spread the wavelengths apart rather than reversing them.

**Rainbows** are produced by the same physics, but inside spherical water droplets. Sunlight enters the droplet, disperses into its color components, undergoes total internal reflection off the back surface (your prerequisite concept), and exits at a wavelength-dependent angle — roughly 42° for red and 40° for violet, measured from the incoming sunlight direction. You see a rainbow arc because each color reaches your eye from a different part of the sky, corresponding to droplets at slightly different angles. The red arc is always on the outside (higher elevation) of the primary rainbow because red exits at the larger angle. A secondary rainbow, when visible, appears outside the primary and has colors reversed — it has undergone two internal reflections, which reverses the geometry.

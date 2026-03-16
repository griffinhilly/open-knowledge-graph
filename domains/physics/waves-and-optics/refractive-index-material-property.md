---
id: refractive-index-material-property
title: Refractive Index as a Material Property
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-and-snells-law
  type: hard
builds-toward:
- dispersion-and-prisms
tags:
- refractive-index
- material-property
- speed-of-light
stage: formal-systems
status: draft
---

# Refractive Index as a Material Property

## Core Idea
The refractive index n = c/v is the ratio of light speed in vacuum (c) to light speed in the material (v). Water has n ≈ 1.33, glass typically n ≈ 1.5, and vacuum has n = 1 by definition. Refractive index is wavelength-dependent (dispersion), generally increasing as wavelength decreases. Higher refractive index means slower light and greater bending.

## Explainer

From Snell's law, you know that light bends when it crosses a boundary between two media because its speed changes. The **refractive index** n is the number that quantifies how much a given material slows light: n = c/v, where c is the speed of light in vacuum (~3 × 10⁸ m/s) and v is the speed of light in that material. Since light can only slow down, not speed up, n is always ≥ 1. Vacuum has n = 1 exactly; air is so close to vacuum that n_air ≈ 1.0003, usually rounded to 1. Water slows light by about 25% (n ≈ 1.33), and glass slows it by about 33% (n ≈ 1.5). Diamond, famous for its intense sparkle, has n ≈ 2.42 — light travels at less than half its vacuum speed inside a diamond.

Snell's law — which you already know — takes on a cleaner form in terms of refractive indices: n₁ sin θ₁ = n₂ sin θ₂. When light passes from a low-n medium to a high-n medium (say, from air into glass), it slows and bends toward the normal. When it passes from high-n to low-n (glass into air), it speeds up and bends away from the normal. The larger the difference in refractive indices between two materials, the more dramatic the bending at their interface. This is why the air-glass interface in a lens redirects light rays to a focus, and why a coin in a glass of water appears to be in a different position than it actually is.

The refractive index is not a single fixed number for a material — it depends on the wavelength of light. This property is called **dispersion**: blue light (shorter wavelength) typically has a higher n in glass than red light (longer wavelength). When white light enters a prism, each wavelength bends by a slightly different amount because each experiences a slightly different refractive index, spreading the light into a spectrum. This is why rainbows form: water droplets act as tiny prisms, dispersing sunlight into its component colors. Dispersion is also why optical lenses for cameras and microscopes require careful design — if not corrected, a simple lens would bring red and blue light to focus at different distances, causing colored fringes called **chromatic aberration**. Lens designers combine multiple glass types with different dispersion characteristics to cancel out this effect.

The physical reason for dispersion is that the refractive index reflects how strongly a material's electrons are driven to oscillate by the passing electromagnetic wave. Electrons respond more strongly near their natural resonance frequencies — which typically lie in the ultraviolet for most glass materials. Blue light is closer to that ultraviolet resonance than red light, so it couples more strongly to the electrons and slows more. This connection between n and the electronic structure of the material is why **refractive index is a material property**: it encodes something fundamental about how the electrons in a substance interact with electromagnetic radiation.

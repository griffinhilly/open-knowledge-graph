---
id: dispersion-wavelength-dependent-refraction
title: Dispersion and Wavelength-Dependent Refraction
domain: physics
course: waves-and-optics
prerequisites:
- id: refractive-index-material-property
  type: hard
builds-toward:
- dispersion-and-prisms
tags:
- dispersion
- wavelength-dependent
- prism
stage: formal-systems
status: validated
---

# Dispersion and Wavelength-Dependent Refraction

## Core Idea
Dispersion is the wavelength-dependent variation of refractive index in a material: shorter wavelengths (blue light) have higher refractive indices than longer wavelengths (red light) in normal dispersion. This causes white light to separate into its component colors when passing through a prism. Dispersion is the origin of rainbows and explains why different colors refract at different angles.

## Questions

```yaml
- question: "White light enters a glass prism. Which color is deflected the most upon exiting, and why?"
  type: multiple-choice
  options:
    - "Red, because it has the longest wavelength and interacts most strongly with glass"
    - "Green, because it is in the middle of the visible spectrum"
    - "Violet, because it has the highest refractive index in the glass"
    - "All colors deflect equally — the prism only sorts them spatially after exit"
  answer: 2
  explanation: "In normal dispersion, shorter wavelengths (higher frequency) drive electron oscillations closer to resonance, producing stronger interactions and a higher refractive index. Violet light has the highest n and therefore bends the most according to Snell's law. Red light has the lowest n and bends the least. Option D is incorrect — the angular separation occurs at each glass-air interface, not after exit."

- question: "A glass lens produces 'chromatic aberration' — different colors focus at slightly different distances. What property of glass directly causes this?"
  type: multiple-choice
  options:
    - "Glass absorbs shorter wavelengths more strongly than longer ones"
    - "The refractive index of glass varies with wavelength, so each color refracts by a different amount"
    - "The speed of light in vacuum is different for different colors"
    - "Glass surfaces reflect longer wavelengths more than shorter ones"
  answer: 1
  explanation: "Chromatic aberration is a direct consequence of dispersion: because n varies with wavelength, different colors are refracted by different amounts at each lens surface and come to focus at different points. This is the same physics as a prism separating colors. Option C is wrong — all light travels at the same speed c in vacuum; the difference arises inside the glass. Option A (differential absorption) affects intensity, not focus."

- question: "In normal dispersion, red light travels more slowly through glass than violet light does."
  type: true-false
  answer: false
  explanation: "In normal dispersion, violet (shorter wavelength) has a higher refractive index than red. Since v = c/n, a higher n means a lower speed. Therefore violet light travels more slowly through glass than red light — the opposite of what the statement claims. This is counterintuitive because we often think of 'energetic' blue/violet light as 'faster,' but inside a dispersive medium, it is actually slower."

- question: "Dispersion occurs because different wavelengths of light interact differently with the electrons in a material, resulting in wavelength-dependent propagation speeds."
  type: true-false
  answer: true
  explanation: "This is the physical mechanism of dispersion. Light drives oscillations of the bound electrons in the material; higher-frequency (shorter-wavelength) light drives oscillations closer to the electrons' natural resonance frequency, producing stronger coupling and more slowing. This wavelength-dependent interaction is captured by the wavelength-dependent refractive index n(λ), which is the macroscopic signature of microscopic electron-photon coupling."

- question: "In a rainbow, why does red appear on the outer arc and violet on the inner arc, given that violet has a higher refractive index in water than red does?"
  type: short-answer
  answer: "Each water droplet refracts and internally reflects sunlight, dispersing it by color. Violet light, having a higher n, bends more sharply at the entry and exit surfaces, causing it to exit at a smaller angle from the incoming sunlight direction (~40°). Red light bends less and exits at a larger angle (~42°). When you look at the sky, droplets at ~42° from the antisolar point return red light to your eye; droplets at ~40° return violet. Because larger angles correspond to higher positions in the arc, red is on the outside (top) and violet on the inside."
  explanation: "The key is relating refractive index to exit angle via Snell's law and the geometry of the spherical droplet. Higher n → more bending at each surface → steeper internal path → different exit angle. The correspondence between exit angle and position in the visible arc (larger angle = higher in sky for primary rainbow) places red at the outside. This is not obvious — it requires tracing rays through the droplet geometry — but it follows directly from n_violet > n_red."
```

## Explainer

Dispersion builds directly on what you know about refractive index. You learned that n = c/v, where c is the speed of light in vacuum and v is its speed in the medium. When light enters glass, it slows down, and n captures how much. Dispersion extends this by revealing that n is not a single fixed number for a given material — it depends on the frequency (and therefore wavelength) of the light. The refractive index of glass for blue light is measurably higher than for red light.

The physical reason is that light interacts with the electrons in the material, and this interaction is strongly frequency-dependent. Higher-frequency light (shorter wavelengths, bluer) drives electron oscillations closer to their natural resonance frequency, producing a stronger interaction and more slowing. This is called **normal dispersion** and is the behavior of glass, water, and most transparent solids at visible wavelengths. The relationship between n and wavelength is not linear — it curves steeply toward the ultraviolet end of the spectrum. Empirical formulas like the Cauchy equation (n ≈ A + B/λ²) capture this behavior well for visible light.

The consequence is that Snell's law — n₁ sin θ₁ = n₂ sin θ₂ — produces a different refraction angle for each color. When white light enters a prism, each wavelength bends by a different amount at both the entry and exit surfaces. Blue light, with the highest n, bends the most; red light, with the lowest n, bends the least. The cumulative effect of two refractions (entry and exit) spreads the colors into a continuous spectrum. The angular spread between red and violet across the visible spectrum is the **dispersion** of the material, and it varies widely between glass types — which is why lens designers combine different glass types to cancel dispersion while preserving focusing power.

Rainbows arise from the same physics in spherical water droplets. Sunlight enters a droplet, reflects off the back interior surface, and refracts again on exit. Because each wavelength exits at a slightly different angle (red at ~42°, violet at ~40° from the antisolar point), different colors reach your eye from droplets at different positions in the sky. The result is the colored arc. The key insight in both prisms and rainbows is the same: dispersion is not an imperfection or side effect — it is a fundamental consequence of how electromagnetic waves interact with bound electrons, and it is the mechanism behind spectroscopy, optical fiber chromatic dispersion, and the chromatic aberration that lens designers work to correct.

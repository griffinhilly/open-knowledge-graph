---
id: wavelength-color-refractive-index
title: 'Dispersion: Wavelength and Refractive Index'
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-interface-snell-relation
  type: hard
- id: dispersion-wavelength-dependent-refraction
  type: soft
- id: dispersion-and-prisms
  type: soft
tags:
- dispersion
- optics
- wavelength
stage: advanced
status: validated
---
# Dispersion: Wavelength and Refractive Index

## Core Idea
The refractive index varies with wavelength (n(λ)), so different colors refract at different angles. Short wavelengths (blue) refract more than long wavelengths (red) in normal dispersion. This causes white light to separate into a spectrum. Dispersion explains rainbows and is exploited in prisms for spectroscopy. Dispersion relation n(ω) or n(k) is fundamental to understanding wave behavior in all media.

## Questions

```yaml
- question: "White light enters a glass prism. Which color emerges at the steepest exit angle (most deflected from its original path), and why?"
  type: multiple-choice
  options:
    - "Red light, because it has the longest wavelength and thus more energy to push through the glass"
    - "Violet/blue light, because shorter wavelengths have a higher refractive index in normal dispersion, causing more bending at each interface"
    - "All colors deflect equally — different colors travel at the same speed through glass"
    - "Green light, because it sits at the center of the visible spectrum and interacts most strongly with glass"
  answer: 1
  explanation: "In normal dispersion (which applies to common glass), n(λ) decreases as wavelength increases: n(blue) > n(red). Snell's law n₁sinθ₁ = n₂sinθ₂ means a higher n produces a larger bend at the interface. Blue/violet light has a higher n, bends more at both entry and exit faces of the prism, and emerges at the steepest angle. Red has the lowest n and bends least. Option A is the most common misconception — associating longest wavelength with more bending — but the refractive index has the opposite dependence on wavelength in normal dispersion."

- question: "In an optical fiber carrying data as a broadband light pulse, chromatic dispersion degrades the signal because:"
  type: multiple-choice
  options:
    - "Higher-frequency light is absorbed more strongly by the fiber core, attenuating those wavelengths over distance"
    - "Different wavelengths have different refractive indices, so they travel at different speeds and the pulse spreads out in time"
    - "Total internal reflection fails at certain wavelengths, allowing some light to escape the fiber"
    - "The fiber's core diameter limits which wavelengths can propagate, selectively filtering the pulse"
  answer: 1
  explanation: "Because n varies with wavelength, different wavelengths travel at different speeds v = c/n through the fiber. A pulse that starts as a narrow spike in time broadens as it travels — the 'blue' components arrive at a slightly different time than the 'red' components. Over long distances, the spread becomes large enough that successive pulses overlap, making individual bits indistinguishable. This is a fundamental physical limitation arising directly from dispersion. Option A describes attenuation, a separate issue. Option C describes a failure of confinement, not dispersion. Option D describes modal dispersion, a different phenomenon."

- question: "In normal dispersion (as found in glass and water), blue light travels more slowly through the medium than red light."
  type: true-false
  answer: true
  explanation: "Speed in a medium is v = c/n. In normal dispersion, n(blue) > n(red), so blue light has lower speed: v(blue) = c/n(blue) < c/n(red) = v(red). This is why blue light bends more than red at a refracting surface — it slows down more upon entering the medium. The chain is: shorter wavelength → higher n → lower speed → more bending. This relationship is what produces the color separation in prisms and rainbows."

- question: "A rainbow forms because water droplets in the atmosphere reflect different colors of sunlight at different angles due to differences in how reflective the droplet surface is at each wavelength."
  type: true-false
  answer: false
  explanation: "Rainbows form through refraction and dispersion, not differential reflectivity. Sunlight enters the front face of a spherical water droplet and refracts — different wavelengths bend by different amounts because n(λ) varies. The light then reflects off the back interior surface (with essentially equal reflectivity for all visible wavelengths) and refracts again on exit. The two refractions compound, separating colors: red exits at about 42° from the direction of incoming sunlight, violet at about 40°. The color separation is entirely due to the wavelength-dependence of refraction, not of reflectivity."

- question: "Why does the refractive index of a material vary with wavelength, and what observable consequence does this have for white light passing through a prism?"
  type: short-answer
  answer: "Refractive index varies with wavelength because different frequencies of light interact differently with the electrons in the medium. Shorter wavelengths (higher frequencies) resonate more strongly with the electron cloud, slowing the light more and producing a higher n. Longer wavelengths interact less strongly, travel faster, and have a lower n. When white light (a mixture of all wavelengths) enters a prism, each wavelength refracts by a different amount at both the entry and exit faces, governed by Snell's law with each color's own n. The two refractions compound, spreading the colors into a spectrum: violet bends most, red bends least."
  explanation: "This wavelength-dependence of n — the dispersion relation n(λ) — is fundamental to optics. It explains why prisms spread light into a spectrum, why rainbows are colored (rather than white), why optical fibers suffer signal degradation over long distances (different wavelengths arrive at different times), and why lenses suffer chromatic aberration (focal length varies with wavelength because n does). Understanding that n is a function of wavelength, not a material constant, is the conceptual step that connects simple Snell's law to the full behavior of light in matter."
```

## Explainer

From your study of refraction, you know that light bends at an interface according to Snell's law: n₁sinθ₁ = n₂sinθ₂. The refractive index n of a material compares the speed of light in vacuum to its speed in the medium — n = c/v. What you may not have questioned yet is whether n is a single fixed number. It turns out it is not: n depends on the wavelength of light. This wavelength-dependence is called **dispersion**, and it has profound consequences for how light behaves in real materials.

The physical reason is that different wavelengths interact differently with the electrons in a medium. Shorter wavelengths (violet, blue) carry higher frequency oscillations that resonate more strongly with the electron cloud, slowing them more in the medium. Longer wavelengths (red, orange) interact less strongly and travel faster. Because n = c/v, higher speed means lower n. So **normal dispersion** — the type in most transparent materials like glass and water — means n decreases as wavelength increases: n(blue) > n(red). Applying Snell's law at an interface, a larger n means a larger bend. Blue light bends more than red light at the same interface.

This differential bending is what separates white light into a spectrum. A glass prism has two angled interfaces; white light enters and refracts once, travels through the glass, then refracts again at the exit face. Both refractions bend blue more than red, and the two bends compound. The result is the familiar spread of colors from violet at the most-bent end to red at the least-bent end. A **rainbow** is the same effect in reverse geometry: sunlight enters the front face of a spherical water droplet, reflects off the back, and exits the front again. The angle at which each color exits depends on its refractive index — red exits at about 42° from the incident sunlight direction, violet at about 40°, producing concentric colored arcs at different angles in the sky.

The broader concept is the **dispersion relation** n(λ) or equivalently n(ω), which characterizes how a medium responds to waves of different frequencies. In spectroscopy, prisms and diffraction gratings both exploit dispersion to separate wavelengths, allowing identification of elements from their emission lines. In optical fiber communications, dispersion is a limitation — a pulse composed of many wavelengths spreads out as different colors travel at different speeds, smearing the signal over distance. Understanding that n is not a constant but a function of wavelength is the step that connects simple Snell's law refraction to the full, frequency-resolved behavior of light in matter.

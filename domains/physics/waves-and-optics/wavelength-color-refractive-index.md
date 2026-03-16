---
id: wavelength-color-refractive-index
title: 'Dispersion: Wavelength and Refractive Index'
domain: physics
course: waves-and-optics
prerequisites:
- id: refraction-interface-snell-relation
  type: hard
tags:
- dispersion
- optics
- wavelength
stage: formal-systems
status: draft
---

# Dispersion: Wavelength and Refractive Index

## Core Idea
The refractive index varies with wavelength (n(λ)), so different colors refract at different angles. Short wavelengths (blue) refract more than long wavelengths (red) in normal dispersion. This causes white light to separate into a spectrum. Dispersion explains rainbows and is exploited in prisms for spectroscopy. Dispersion relation n(ω) or n(k) is fundamental to understanding wave behavior in all media.

## Explainer

From your study of refraction, you know that light bends at an interface according to Snell's law: n₁sinθ₁ = n₂sinθ₂. The refractive index n of a material compares the speed of light in vacuum to its speed in the medium — n = c/v. What you may not have questioned yet is whether n is a single fixed number. It turns out it is not: n depends on the wavelength of light. This wavelength-dependence is called **dispersion**, and it has profound consequences for how light behaves in real materials.

The physical reason is that different wavelengths interact differently with the electrons in a medium. Shorter wavelengths (violet, blue) carry higher frequency oscillations that resonate more strongly with the electron cloud, slowing them more in the medium. Longer wavelengths (red, orange) interact less strongly and travel faster. Because n = c/v, higher speed means lower n. So **normal dispersion** — the type in most transparent materials like glass and water — means n decreases as wavelength increases: n(blue) > n(red). Applying Snell's law at an interface, a larger n means a larger bend. Blue light bends more than red light at the same interface.

This differential bending is what separates white light into a spectrum. A glass prism has two angled interfaces; white light enters and refracts once, travels through the glass, then refracts again at the exit face. Both refractions bend blue more than red, and the two bends compound. The result is the familiar spread of colors from violet at the most-bent end to red at the least-bent end. A **rainbow** is the same effect in reverse geometry: sunlight enters the front face of a spherical water droplet, reflects off the back, and exits the front again. The angle at which each color exits depends on its refractive index — red exits at about 42° from the incident sunlight direction, violet at about 40°, producing concentric colored arcs at different angles in the sky.

The broader concept is the **dispersion relation** n(λ) or equivalently n(ω), which characterizes how a medium responds to waves of different frequencies. In spectroscopy, prisms and diffraction gratings both exploit dispersion to separate wavelengths, allowing identification of elements from their emission lines. In optical fiber communications, dispersion is a limitation — a pulse composed of many wavelengths spreads out as different colors travel at different speeds, smearing the signal over distance. Understanding that n is not a constant but a function of wavelength is the step that connects simple Snell's law refraction to the full, frequency-resolved behavior of light in matter.

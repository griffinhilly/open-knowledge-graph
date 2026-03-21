---
id: diffraction-resolution-angular-separation
title: Diffraction Limit and the Rayleigh Criterion
domain: physics
course: waves-and-optics
prerequisites:
- id: single-aperture-diffraction-minima
  type: hard
builds-toward:
- optical-system-magnification
tags:
- resolution
- diffraction
- optics
stage: advanced
status: draft
---

# Diffraction Limit and the Rayleigh Criterion

## Core Idea
The Rayleigh criterion states that two point sources are just resolvable if the central diffraction maximum of one coincides with the first dark fringe of the other. For a circular aperture of diameter D, the minimum resolvable angular separation is θ ≈ 1.22 λ/D. This fundamental limit applies to all optical instruments.

## Questions

```yaml
- question: "A telescope manufacturer builds a perfect, completely aberration-free lens with exquisite optical coatings. Can this lens resolve two stars separated by an angle smaller than 1.22 λ/D?"
  type: multiple-choice
  options:
    - "Yes — eliminating aberrations removes all resolution limits"
    - "Yes — better coatings allow more light collection, improving resolution"
    - "No — the diffraction limit is a fundamental physical constraint, not an engineering one"
    - "No — but a larger magnification eyepiece would overcome this"
  answer: 2
  explanation: "The Rayleigh criterion expresses a fundamental limit set by wave optics, not by imperfections in the instrument. Even a perfect lens diffracts light at its aperture, producing an Airy disk rather than a point image. Eliminating aberrations, improving coatings, or increasing magnification cannot reduce the size of the Airy disk — only a larger aperture D or shorter wavelength λ can do that. This is the key insight: the diffraction limit belongs to physics, not engineering."

- question: "A radio telescope observing at λ = 21 cm needs to match the angular resolution of an optical telescope with a 10 cm aperture observing at λ = 500 nm. Approximately how large must the radio telescope be?"
  type: multiple-choice
  options:
    - "About 10 cm — resolution depends only on aperture, not wavelength"
    - "About 420 cm — wavelength ratio times the optical aperture"
    - "About 42,000 cm (420 m) — because radio wavelengths are ~4,200× longer"
    - "About 21 m — because radio wavelengths are about 210× the optical aperture"
  answer: 2
  explanation: "The Rayleigh criterion θ ≈ 1.22 λ/D shows resolution depends on the ratio λ/D. To achieve the same θ, if λ increases by a factor of 4,200 (from 500 nm to 21 cm), D must increase by the same factor: 10 cm × 4,200 = 42,000 cm = 420 m. This is why real radio telescopes are enormous — it is not a matter of poor design, but of compensating for wavelengths thousands of times longer than visible light."

- question: "A perfectly crafted, aberration-free lens will eventually beat the Rayleigh criterion if the optical quality is high enough."
  type: true-false
  answer: false
  explanation: "The diffraction limit is not a consequence of imperfect optics — it arises from the wave nature of light itself. Any aperture, no matter how perfect, diffracts light and produces an Airy disk. The Rayleigh criterion sets the minimum resolvable separation for a given aperture and wavelength regardless of optical quality. Super-resolution microscopy methods that go beyond λ/D do so by exploiting molecular photochemistry, not by improving lens quality."

- question: "Using shorter-wavelength light to illuminate a specimen in a microscope will improve its angular resolution."
  type: true-false
  answer: true
  explanation: "Since θ_min ≈ 1.22 λ/D, decreasing λ directly decreases the minimum resolvable angle, improving resolution. This is why electron microscopes can image atomic structures — electron de Broglie wavelengths (~pm) are far shorter than visible light (~hundreds of nm). UV microscopy and X-ray crystallography exploit the same principle: shorter wavelength yields finer resolution."

- question: "Explain why simply building a larger telescope improves its angular resolution, in terms of the physics of diffraction."
  type: short-answer
  answer: "A larger aperture D reduces the angular size of the Airy disk produced by each point source, because the first dark ring of the diffraction pattern falls at an angle θ ≈ 1.22 λ/D. When D increases, θ_min decreases, so two sources that previously fell within each other's Airy disks now produce distinguishable peaks. The telescope isn't 'seeing more detail' because it collects more light — it resolves finer detail because it diffracts less, spreading each point source's image into a smaller disk."
  explanation: "This answer demonstrates understanding that resolution is about diffraction, not light collection. Many students confuse the two benefits of larger apertures (more light AND better resolution). The resolution gain is entirely due to the wave optics of diffraction at the aperture, captured by θ ≈ 1.22 λ/D."
```

## Explainer

From your study of single-aperture diffraction, you know that a circular opening doesn't produce a point image of a point source — it produces a circular **Airy disk**, a bright central maximum surrounded by alternating dark and bright rings. Every lens, mirror, or aperture in an optical system does this. When two nearby point sources are imaged through the same aperture, each produces its own Airy disk on the detector. If the sources are far apart, the two Airy disks are clearly separated and easily resolved. As they move closer together, the disks begin to overlap. The question becomes: at what point does the combined intensity pattern stop showing two distinct peaks and blur into one?

The **Rayleigh criterion** provides a practical, widely-adopted answer: two sources are just resolvable when the central maximum of one Airy disk falls exactly on the first minimum (dark ring) of the other. At this separation, a small but visible dip appears between the two intensity peaks — a trained observer can still tell there are two sources, but just barely. For a circular aperture of diameter D, the angle at which this occurs is θ ≈ 1.22 λ/D. The factor of 1.22 comes from the mathematics of diffraction through a circular aperture (specifically from the first zero of the Bessel function J₁). For a slit rather than a circle, the equivalent formula is θ ≈ λ/D without the 1.22.

The formula θ ≈ 1.22 λ/D contains a complete design recipe: to resolve finer angular detail, either use shorter wavelength light or use a larger aperture. This explains why radio telescopes must be enormous — radio waves have wavelengths thousands of times longer than visible light, so the aperture must be proportionally larger to achieve comparable resolution. It explains why the Hubble Space Telescope works in space (no atmospheric blurring, diffraction-limited by its mirror diameter) and why electron microscopes can resolve atomic structures (electron de Broglie wavelengths are far shorter than visible light). In medical imaging, the same principle governs ultrasound resolution: higher-frequency ultrasound has shorter wavelengths and thus finer resolution, but shorter wavelengths are also absorbed more quickly, limiting penetration depth.

The diffraction limit is not a limitation of instrument quality — it is a fundamental physical limit imposed by wave optics. A perfect, aberration-free lens still cannot beat the Rayleigh criterion. The only ways around it are to use shorter wavelengths (UV microscopy, X-ray crystallography) or to use interference-based techniques like **aperture synthesis** in radio astronomy, where many small telescopes are combined to simulate a single large aperture, or **super-resolution microscopy** in biology, which exploits molecular properties rather than aperture physics to localize sources more precisely than λ/D.

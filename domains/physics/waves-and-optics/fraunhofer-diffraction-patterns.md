---
id: fraunhofer-diffraction-patterns
title: 'Fraunhofer Diffraction: Far-Field Diffraction Patterns'
domain: physics
course: waves-and-optics
prerequisites:
- id: single-slit-diffraction
  type: hard
- id: diffraction-and-huygen-principle
  type: soft
builds-toward:
- diffraction-gratings
tags:
- fraunhofer-diffraction
- far-field
- diffraction-pattern
stage: advanced
status: validated
---

# Fraunhofer Diffraction: Far-Field Diffraction Patterns

## Core Idea
Fraunhofer diffraction occurs when the source and observation screen are far from the diffracting aperture (parallel incident light), producing diffraction patterns determined by Fourier transform of the aperture. Slit width a produces minima at angles where sin θ = nλ/a (n ≠ 0).

## Questions

```yaml
- question: "A laser shines through a narrow slit (0.1 mm wide) and then through a wide slit (1 mm wide) in two separate experiments. Compared to the wide slit, the narrow slit produces a central diffraction maximum that is:"
  type: multiple-choice
  options:
    - "Narrower, because less light passes through and so it spreads less"
    - "The same width, because wavelength determines the pattern, not slit width"
    - "Wider, because localizing the wave spatially spreads it more in angle"
    - "Brighter but the same width, because the smaller aperture concentrates the beam"
  answer: 2
  explanation: "This is the Fourier reciprocity principle: a narrower slit (smaller a) means the function describing the aperture is more spatially confined, and its Fourier transform is broader in angular frequency. The first minimum occurs at sin θ = λ/a — a smaller 'a' gives a larger θ. This is a spatial analogue of the Heisenberg uncertainty principle. The intuitive but wrong answer is option A — students often expect a narrow opening to produce a narrow beam, as if light were a particle stream."

- question: "The Fraunhofer diffraction pattern produced by a complex aperture is mathematically equivalent to:"
  type: multiple-choice
  options:
    - "The convolution of the aperture function with the wavelength"
    - "The magnitude-squared of the Fourier transform of the aperture function"
    - "The integral of the aperture function divided by the observation distance"
    - "The autocorrelation of the aperture function multiplied by wavelength"
  answer: 1
  explanation: "In the far-field limit, the amplitude at angle θ is the Fourier transform of the aperture function evaluated at spatial frequency sin θ/λ. The observed intensity is the square of the amplitude, giving the magnitude-squared of the Fourier transform. This is why diffraction gratings (periodic apertures) produce sharp intensity peaks — the Fourier transform of a periodic comb function is another comb function."

- question: "A larger telescope aperture produces a narrower diffraction-limited angular resolution."
  type: true-false
  answer: true
  explanation: "The angular radius of the Airy disk (the central diffraction maximum for a circular aperture) is proportional to λ/D, where D is the aperture diameter. A larger aperture decreases this angle, allowing finer angular details to be resolved. This is why large telescopes can distinguish stars that appear as a single point through smaller instruments, and why radio telescopes must be enormous — radio wavelengths are centimeters to meters, requiring proportionally huge apertures for the same angular resolution as optical telescopes."

- question: "In a single-slit Fraunhofer diffraction pattern, the secondary maxima are the same width as the central maximum."
  type: true-false
  answer: false
  explanation: "The central maximum is twice as wide as each secondary maximum — it extends from −λ/a to +λ/a in sin θ, while each secondary maximum spans only λ/a. This double-width central fringe is a distinctive signature of single-slit Fraunhofer diffraction. The asymmetry arises because the central maximum spans the range between the ±1st-order minima (on both sides), while secondary maxima each span the range between two adjacent minima on the same side."

- question: "Why does narrowing a slit produce a wider diffraction pattern, rather than a narrower, more beam-like pattern?"
  type: short-answer
  answer: "Because the diffraction pattern is the Fourier transform of the aperture, and Fourier transforms obey a reciprocal relationship: spatial confinement in one domain produces spreading in the reciprocal domain. A narrower slit confines the wavefront more tightly in position, which — by the uncertainty principle for waves — requires a broader distribution of transverse momenta (directions). Each point in the slit emits a Huygens wavelet in all directions, and with fewer points across the slit, there are fewer opportunities for destructive interference to cancel light at large angles, so light spreads more widely."
  explanation: "The intuition that 'a smaller hole makes a smaller spot' is the particle-optics approximation, valid when the wavelength is much smaller than the slit. When the slit width approaches the wavelength, wave effects dominate and the reciprocal relationship asserts itself. This same principle governs why a single atom can diffract electrons, why X-ray diffraction patterns reveal atomic spacings, and why aperture size is the fundamental limit on telescope resolution."
```

## Explainer

From your study of single-slit diffraction and Huygens' principle, you know that every point on a wavefront acts as a source of secondary wavelets. When a wave passes through a slit, all the points across the slit opening emit wavelets, and the observed intensity at any downstream point is determined by how those wavelets interfere. The challenge is that the geometry of the interference depends on exactly how far the screen is from the slit. **Fraunhofer diffraction** is the simplifying limit where the screen is far enough away that you can treat the rays reaching any single point on the screen as effectively parallel — the **far-field** regime.

In this limit, the math becomes clean. The phase difference between a wavelet from the slit's center and one from a point a distance y from the center is simply φ = (2πy/λ) sin θ. To find the total amplitude at angle θ, you sum the contributions from all points across the slit — which, as the slit width becomes a continuous aperture, is an integral. This integral is precisely the **Fourier transform** of the aperture function (the function describing where the slit is open). For a rectangular slit of width a, the transform gives a sinc-function amplitude, and the intensity pattern is sinc²: a bright central maximum flanked by weaker secondary maxima, with dark minima wherever sin θ = nλ/a (n = 1, 2, 3, ...). Notice that the central bright fringe is twice as wide as each secondary maximum — a distinctive signature of single-slit Fraunhofer diffraction.

The Fourier transform connection is more than mathematical elegance. It reveals a fundamental reciprocal relationship: a **narrow** slit (small a) produces a **wide** diffraction pattern, and a **wide** slit produces a **narrow** pattern. This is a spatial analogue of the Heisenberg uncertainty principle: localizing a wave more tightly in space spreads it more broadly in angle. The same principle explains why a telescope with a larger aperture resolves finer angular detail — a wider aperture produces a narrower diffraction limit — and why radio telescopes must be enormous to achieve angular resolution comparable to optical telescopes operating at much shorter wavelengths.

When light passes through two slits, an array of slits, or any complex aperture, the Fraunhofer pattern is always the magnitude-squared of the Fourier transform of that aperture. This is why diffraction gratings — arrays of many closely-spaced slits — produce extremely sharp maxima: the Fourier transform of a periodic array (a comb function) is another comb function, with energy concentrated into sharp, widely-spaced peaks. Understanding Fraunhofer diffraction is therefore the gateway to understanding both diffraction gratings and how scientists use X-ray diffraction to determine crystal structures, where the atomic lattice acts as the diffracting aperture.

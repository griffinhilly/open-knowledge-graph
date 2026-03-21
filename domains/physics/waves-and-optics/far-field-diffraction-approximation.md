---
id: far-field-diffraction-approximation
title: Far-Field Diffraction and the Fraunhofer Approximation
domain: physics
course: waves-and-optics
prerequisites:
- id: fresnel-zones-wavefront
  type: soft
- id: single-aperture-diffraction-minima
  type: hard
tags:
- diffraction
- approximation
stage: advanced
status: draft
---

# Far-Field Diffraction and the Fraunhofer Approximation

## Core Idea
In the far field (observation distance >> aperture size / wavelength), diffraction patterns simplify because all diffracted rays are approximately parallel. The Fraunhofer approximation makes the diffraction integral a Fourier transform, explaining why grating and slit patterns have such clean mathematical forms. This regime applies for microscopy, telescopes, and typical laboratory optics.

## Questions

```yaml
- question: "A diffraction grating has 100 slits spaced 1 μm apart. A second grating has 1000 slits with the same spacing. Both are illuminated with the same monochromatic light and observed in the far field. How do their diffraction patterns differ?"
  type: multiple-choice
  options:
    - "The 1000-slit grating produces orders at different angles, because more slits changes the grating equation"
    - "The 1000-slit grating produces sharper, more intense peaks at the same angular positions as the 100-slit grating"
    - "The 1000-slit grating produces more total orders (more peaks), spread across a wider angular range"
    - "The patterns are identical since the slit spacing determines the peak positions"
  answer: 1
  explanation: "The angular positions of diffraction orders depend on the slit spacing (via the grating equation d sin θ = mλ), so both gratings produce peaks at the same angles. However, the Fourier transform relationship reveals why more slits means sharper peaks: a grating with N slits is a longer periodic aperture function. A longer periodic function has a Fourier transform with narrower peaks (by the uncertainty principle for Fourier pairs: wider spatial extent ↔ narrower frequency content). More slits also means higher peak intensity (amplitude scales as N, intensity as N²) and better angular resolution."

- question: "You are working close to a small aperture — in the Fresnel (near-field) regime. As you move your observation screen farther away, crossing into the Fraunhofer regime, what changes about the diffraction pattern?"
  type: multiple-choice
  options:
    - "The pattern disappears because diffraction only occurs near the aperture"
    - "The pattern simplifies: it becomes exactly the Fourier transform of the aperture's transmission function"
    - "The pattern becomes more complex because more interference terms accumulate with distance"
    - "The pattern shrinks in angular size as you move farther away"
  answer: 1
  explanation: "The key transition from near-field to far-field is the elimination of quadratic phase terms. In the Fresnel regime, path length differences between different parts of the aperture and the observation point involve both linear and quadratic (r²) terms — making the diffraction integral complex. In the far field (z >> a²/λ), the quadratic terms become negligible and only the linear terms remain. The surviving integral is precisely a Fourier transform of the aperture function. The pattern 'simplifies' in the mathematical sense — it acquires the clean structure of a transform — even as it spreads spatially."

- question: "The far-field diffraction pattern of any aperture is mathematically equivalent to the Fourier transform of that aperture's transmission function."
  type: true-false
  answer: true
  explanation: "This is the central result of the Fraunhofer approximation. When the observation distance satisfies z >> a²/λ, the diffraction integral reduces to ∫ t(x) e^{−i2πux} dx, where t(x) is the aperture transmission function and u is the spatial frequency (related to observation angle). This is exactly the Fourier transform of t(x). The result is completely general: any aperture shape, any transmission profile — the far-field pattern is its Fourier transform. This is why a single slit gives a sinc function, a grating gives a comb of sharp peaks, and a circular aperture gives an Airy disk."

- question: "The Fraunhofer approximation is most accurate when the observation point is close to the aperture, where the geometry is simpler."
  type: true-false
  answer: false
  explanation: "The Fraunhofer (far-field) approximation is valid when the observation distance is *large* relative to a²/λ. Close to the aperture, in the Fresnel (near-field) regime, quadratic path length terms are significant and the full Fresnel integral is needed. The Fraunhofer approximation becomes accurate only once those quadratic terms are negligible — which requires large z. For visible light (λ ~ 500 nm) through a 1 mm slit, the far-field condition z >> 1 mm²/(500 nm) = 2 m means you need to be several meters away."

- question: "Why does the far-field condition (z >> a²/λ) cause the diffraction integral to become a Fourier transform?"
  type: short-answer
  answer: "The exact diffraction integral involves the path length from each point in the aperture to the observation point. For a point at position x in the aperture and an observation point at distance z and transverse position X, the path length is approximately z + xX/z + x²/(2z). The quadratic term x²/(2z) is what makes the integral non-Fourier in general (this is the Fresnel term). When z >> a²/λ, the maximum quadratic phase shift across the aperture (proportional to a²/(λz)) becomes much less than 1 radian and can be dropped. What remains is the linear term xX/z, and the integral over x with a linear phase becomes exactly the Fourier transform of the aperture function evaluated at spatial frequency u = X/(λz)."
  explanation: "The Fourier relationship has a deep physical meaning: spatial extent and angular spread are Fourier conjugates, just as position and momentum are in quantum mechanics. A small aperture (localized in space) produces a wide diffraction pattern (spread in angle); a large aperture produces a narrow pattern. This is the optical analogue of Heisenberg's uncertainty principle."
```

## Explainer

When a wave passes through an aperture or past an obstacle, it diffracts — bending and spreading, creating an interference pattern downstream. From single-aperture-diffraction-minima, you know where the dark fringes in that pattern fall. This topic addresses the deeper question: why does the math simplify so cleanly at large distances, and what does that simplification reveal? The answer is the **Fraunhofer approximation**, which applies in the **far field**.

The distinction between near-field and far-field diffraction comes down to wavefront curvature. Close to the aperture, waves arriving at an observation point have traveled different path lengths, and those differences involve quadratic (squared) terms in the geometry — this is the **Fresnel regime**. In the far field, the observation point is so distant that all diffracted rays from across the aperture arrive along nearly parallel paths. The quadratic terms become negligible, and only the linear (first-order) path differences survive. The approximate criterion is z >> a²/λ, where z is the observation distance, a is the aperture size, and λ is the wavelength. For visible light through a 1 mm slit, this puts the far field beyond about 1 meter — well within a typical optics lab.

This geometric simplification has a remarkable mathematical consequence: the diffraction integral becomes a **Fourier transform** of the aperture's transmission function. Whatever shape you cut in the aperture — a uniform slit, a grating of N slits, a circular opening — the far-field pattern is exactly the Fourier transform of that spatial profile. A single uniform slit gives a sinc function (sin(u)/u); a diffraction grating gives a comb of sharp peaks; a circular aperture gives an **Airy disk** pattern. The Fourier relationship also explains why a grating with many closely spaced slits produces sharper, more widely separated diffraction orders: more slits means a longer periodic aperture, whose Fourier transform has narrower, better-resolved peaks.

In telescopes, microscopes, and most precision optical instruments, the geometry satisfies the far-field condition because the aperture (mirror or lens) is small relative to the image distances involved. This is why diffraction-limited resolution — the Rayleigh criterion — can be derived cleanly from Fourier analysis of the circular aperture. Whenever you see a clean, symmetric diffraction pattern in an optics experiment, the Fraunhofer approximation is at work, reducing complex wave interference to the elegant structure of a Fourier transform.

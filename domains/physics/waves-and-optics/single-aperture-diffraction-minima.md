---
id: single-aperture-diffraction-minima
title: Single-Slit Diffraction and Diffraction Patterns
domain: physics
course: waves-and-optics
prerequisites:
- id: double-aperture-interference-fringe
  type: hard
builds-toward:
- diffraction-resolution-angular-separation
- far-field-diffraction-approximation
tags:
- diffraction
- waves
stage: formal-systems
status: draft
---

# Single-Slit Diffraction and Diffraction Patterns

## Core Idea
A single slit of width a produces a diffraction pattern with a bright central maximum and weaker fringes. Dark minima occur at angles where a sin(θ) = nλ (n = 1, 2, 3,...). The pattern results from destructive interference of wavelets from different parts of the slit. Narrower slits produce wider diffraction patterns.

## How It's Best Learned
Use the Huygens-Fresnel principle to explain how different parts of the slit produce wavelets that interfere.

## Common Misconceptions
Single-slit diffraction is not the same as interference; it arises from the slit's finite width, not from multiple separated sources.

## Explainer

From double-slit interference, you know that two coherent point sources produce alternating bright and dark fringes — bright where path differences are whole-number wavelengths, dark where they are half-integer wavelengths. **Single-slit diffraction** extends exactly this logic, but instead of two separated sources, every point across the continuous width of the slit acts as a Huygens wavelet source. The dark minima arise from the same destructive interference principle, just applied to the slit as a whole rather than to a pair of points.

Here is the key physical argument for the first dark minimum. Divide the slit of width *a* into two equal halves. Pair each point in the upper half with the corresponding point directly across from it in the lower half — a separation of a/2. If the path difference for each pair equals λ/2, the two contributions cancel. The geometry requires a sin(θ) = λ for this to hold across every pair simultaneously, which gives the first minimum. For the second minimum, divide the slit into four equal sections and pair them the same way; each pair is separated by a/4 and must satisfy a path difference of λ/2, giving a sin(θ) = 2λ. In general, **dark minima** occur where a sin(θ) = nλ for n = 1, 2, 3, ...

The most important consequence is the inverse relationship between slit width and pattern width. A narrower slit (smaller *a*) means the first minimum occurs at a larger angle, so the bright central maximum spreads wider. This is the wave-optics expression of a fundamental principle: spatially confining a wave (narrowing the slit) spreads it in angle. The **central maximum** spans from θ = −λ/a to θ = +λ/a, making it twice as wide as each secondary maximum on either side. It also carries the vast majority of the energy — secondary maxima are dramatically dimmer because only partial cancellation occurs between the slit portions there.

The distinction from double-slit interference matters for understanding real optical systems. Double-slit interference produces many equally-spaced, approximately equal-brightness fringes. Single-slit diffraction produces a wide, bright central peak flanked by weak, progressively dimmer fringes — an intensity **envelope**. In any real experiment with two finite-width slits, both effects occur simultaneously: the sharp double-slit fringes are multiplied by the single-slit diffraction envelope, so some interference maxima are suppressed where they coincide with diffraction minima. Recognizing the single-slit envelope is the key to understanding why real two-slit patterns do not go on forever with equal brightness.

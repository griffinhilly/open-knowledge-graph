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
stage: advanced
status: validated
---

# Single-Slit Diffraction and Diffraction Patterns

## Core Idea
A single slit of width a produces a diffraction pattern with a bright central maximum and weaker fringes. Dark minima occur at angles where a sin(θ) = nλ (n = 1, 2, 3,...). The pattern results from destructive interference of wavelets from different parts of the slit. Narrower slits produce wider diffraction patterns.

## How It's Best Learned
Use the Huygens-Fresnel principle to explain how different parts of the slit produce wavelets that interfere.

## Common Misconceptions
Single-slit diffraction is not the same as interference; it arises from the slit's finite width, not from multiple separated sources.

## Questions

```yaml
- question: "A single slit of width a produces a diffraction pattern with its first dark minimum at angle θ₁. If the slit is narrowed to width a/2, where does the first dark minimum now appear?"
  type: multiple-choice
  options:
    - "At θ₁/2 — the narrower slit confines the pattern, moving minima inward"
    - "At the same angle θ₁ — diffraction angle depends only on wavelength"
    - "At approximately 2θ₁ — the narrower slit spreads the pattern, pushing minima outward"
    - "The first minimum disappears — a slit too narrow produces no dark fringes"
  answer: 2
  explanation: "The first minimum occurs where a sin θ = λ, so sin θ = λ/a. Halving the slit width to a/2 doubles sin θ, approximately doubling the angle (for small angles, θ ≈ λ/a). The pattern widens because a narrower slit spatially confines the wave more, forcing greater angular spread — the central maximum broadens and its bounding minima move outward. Option A inverts the relationship: it reflects the intuition that a narrower slit should produce a narrower beam, which is the ray-optics expectation. Wave diffraction behaves oppositely."

- question: "A student argues: 'By analogy with double-slit minima (where path difference = λ/2 gives dark fringes), the first single-slit minimum should occur at a sin θ = λ/2.' Why is the correct condition a sin θ = λ instead?"
  type: multiple-choice
  options:
    - "Single-slit diffraction uses a different wavelength convention than double-slit interference"
    - "The slit is divided into two halves; each corresponding pair of points (one from each half, separated by a/2) must cancel. This requires (a/2) sin θ = λ/2, giving a sin θ = λ"
    - "The path difference across the whole slit must equal λ/2, not λ"
    - "The factor of 2 arises because the central maximum is twice as wide as secondary maxima"
  answer: 1
  explanation: "The derivation pairs each point in the upper half of the slit with the point directly below it in the lower half, a distance a/2 apart. For complete destructive interference across all such pairs simultaneously, the path difference for each pair must be λ/2. The geometry gives (a/2) sin θ = λ/2, which simplifies to a sin θ = λ. The student's error is applying the double-slit formula directly: in double-slit, two distinct sources interfere; in single-slit, you must account for contributions from the entire continuous aperture, not just two points, which changes the cancellation condition by a factor of 2."

- question: "Single-slit diffraction occurs because different parts of the slit act as independent Huygens wavelet sources whose contributions can interfere constructively or destructively at a distant screen."
  type: true-false
  answer: true
  explanation: "This is the Huygens-Fresnel principle applied to a finite aperture: every point across the slit width radiates a wavelet, and these wavelets travel different path lengths to a given point on the screen. When the path-length differences satisfy the cancellation condition, destructive interference produces a dark minimum. The entire diffraction pattern — bright central peak, dark minima, weak secondary maxima — follows from systematically computing how all these wavelets interfere. Without the wave nature of light (and thus the Huygens construction), single-slit diffraction would not exist: ray optics predicts a sharp geometric shadow with no banding."

- question: "The central maximum of a single-slit diffraction pattern has the same angular width as each of the secondary maxima on either side."
  type: true-false
  answer: false
  explanation: "The central maximum spans from the first minimum at θ = −λ/a to θ = +λ/a, giving an angular width of 2λ/a. Each secondary maximum sits between consecutive minima — for example, between nλ/a and (n+1)λ/a — spanning an angular width of only λ/a. The central maximum is therefore twice as wide as any secondary maximum. It also carries the overwhelming majority of the diffracted intensity; secondary maxima are dramatically dimmer because only partial cancellation occurs for points contributing to them, and progressively less energy reaches higher-order fringes."

- question: "Why does a narrower slit produce a wider diffraction pattern, and what general principle does this illustrate about waves and spatial confinement?"
  type: short-answer
  answer: "The first dark minimum occurs at a sin θ = λ, so sin θ = λ/a. Reducing the slit width a increases sin θ, pushing the minimum to a larger angle and spreading the central maximum. The general principle is that spatially confining a wave in one dimension forces it to spread in angle: a narrow slit is a small spatial 'window,' and squeezing light through a smaller opening forces greater diffraction. This is the wave-optics analog of the Heisenberg uncertainty principle: tighter spatial localization (small Δx, here the slit width a) implies greater spread in the transverse momentum or wave-vector (large Δkₓ). Ray optics predicts no such spreading — it is an inherently wave phenomenon arising because the slit width becomes comparable to the wavelength."
```

## Explainer

From double-slit interference, you know that two coherent point sources produce alternating bright and dark fringes — bright where path differences are whole-number wavelengths, dark where they are half-integer wavelengths. **Single-slit diffraction** extends exactly this logic, but instead of two separated sources, every point across the continuous width of the slit acts as a Huygens wavelet source. The dark minima arise from the same destructive interference principle, just applied to the slit as a whole rather than to a pair of points.

Here is the key physical argument for the first dark minimum. Divide the slit of width *a* into two equal halves. Pair each point in the upper half with the corresponding point directly across from it in the lower half — a separation of a/2. If the path difference for each pair equals λ/2, the two contributions cancel. The geometry requires a sin(θ) = λ for this to hold across every pair simultaneously, which gives the first minimum. For the second minimum, divide the slit into four equal sections and pair them the same way; each pair is separated by a/4 and must satisfy a path difference of λ/2, giving a sin(θ) = 2λ. In general, **dark minima** occur where a sin(θ) = nλ for n = 1, 2, 3, ...

The most important consequence is the inverse relationship between slit width and pattern width. A narrower slit (smaller *a*) means the first minimum occurs at a larger angle, so the bright central maximum spreads wider. This is the wave-optics expression of a fundamental principle: spatially confining a wave (narrowing the slit) spreads it in angle. The **central maximum** spans from θ = −λ/a to θ = +λ/a, making it twice as wide as each secondary maximum on either side. It also carries the vast majority of the energy — secondary maxima are dramatically dimmer because only partial cancellation occurs between the slit portions there.

The distinction from double-slit interference matters for understanding real optical systems. Double-slit interference produces many equally-spaced, approximately equal-brightness fringes. Single-slit diffraction produces a wide, bright central peak flanked by weak, progressively dimmer fringes — an intensity **envelope**. In any real experiment with two finite-width slits, both effects occur simultaneously: the sharp double-slit fringes are multiplied by the single-slit diffraction envelope, so some interference maxima are suppressed where they coincide with diffraction minima. Recognizing the single-slit envelope is the key to understanding why real two-slit patterns do not go on forever with equal brightness.

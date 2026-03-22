---
id: multiple-slit-grating-equation
title: Diffraction Gratings and the Grating Equation
domain: physics
course: waves-and-optics
prerequisites:
- id: double-aperture-interference-fringe
  type: hard
builds-toward:
- diffraction-resolution-angular-separation
tags:
- diffraction
- gratings
- spectroscopy
stage: advanced
status: draft
---

# Diffraction Gratings and the Grating Equation

## Core Idea
A diffraction grating with spacing d between slits produces sharp bright fringes at angles satisfying d sin(θ) = nλ (grating equation). Each order n shows a different color for white light (spectrum), making gratings powerful tools for spectroscopy. Gratings achieve higher resolution than double slits because many slits interfere simultaneously.

## Questions

```yaml
- question: "A student claims that replacing a double-slit setup with a 1,000-slit grating (same spacing d) would just make the bright fringes brighter, without changing their angular positions or widths. What is actually true?"
  type: multiple-choice
  options:
    - "The student is correct — more slits increase brightness but don't affect fringe position or width"
    - "The fringes shift to different angles because more slits change the path-length condition"
    - "The fringes occur at the same angles but become much sharper (narrower) and much more intense"
    - "More slits cause the fringes to merge, producing a broad continuous bright region"
  answer: 2
  explanation: "The grating equation d sin(θ) = nλ is identical to the double-slit condition — the positions of bright maxima are unchanged because they depend only on slit spacing d and wavelength λ, not on the number of slits. What changes dramatically is fringe width. With N slits, any small angular deviation from the maximum introduces accumulating phase errors across all N waves. For 1,000 slits, a tiny offset puts each slit slightly out of phase with the next, and when 1,000 such waves are summed, they nearly completely cancel. Bright fringes become roughly N times narrower and N² times more intense. This sharpness — not just brightness — is what makes gratings so powerful for spectroscopy."

- question: "Why does a diffraction grating separate white light into a spectrum in each diffraction order, but NOT in the zeroth order (n = 0)?"
  type: multiple-choice
  options:
    - "The zeroth order is absorbed by the grating material, so it never appears"
    - "For n = 0, d sin(θ) = 0 regardless of λ — all wavelengths satisfy this at θ = 0, so they overlap"
    - "The grating equation doesn't apply to the zeroth order"
    - "The zeroth order appears only for gratings with very small slit spacing d"
  answer: 1
  explanation: "For the zeroth order, d sin(θ) = 0·λ = 0, which is satisfied by θ = 0 for every wavelength. Since all wavelengths arrive at the same angle (straight through), there is no angular separation and you see only white light — no spectrum. For orders n ≥ 1, the equation d sin(θ) = nλ requires different angles for different λ: blue light (shorter λ) diffracts less than red light (longer λ), spreading the colors out angularly. This spectral dispersion in non-zero orders makes gratings the key element in spectrometers."

- question: "The maximum diffraction order observable from a grating is limited by the condition that sin(θ) ≤ 1, so higher orders simply cannot exist at any angle."
  type: true-false
  answer: true
  explanation: "The grating equation gives sin(θ) = nλ/d. Since sin(θ) cannot physically exceed 1 (a beam diffracted past 90° would travel backward through the grating), the maximum observable order is n_max = floor(d/λ). For example, a grating with d = 2.0 μm illuminated by λ = 500 nm (d/λ = 4) can show at most orders 0, ±1, ±2, ±3 — order ±4 would require sin(θ) = 4·500/2000 = 1.0 exactly (grazing, impractical), and order ±5 would require sin(θ) = 1.25, which is impossible. No amount of grating size or intensity can make higher orders appear."

- question: "The diffraction grating equation d sin(θ) = nλ is a different physical condition from the double-slit constructive interference condition, generalized to many slits."
  type: true-false
  answer: false
  explanation: "The grating equation is mathematically identical to the double-slit constructive interference condition — both require that adjacent slits have a path-length difference equal to a whole number of wavelengths: Δ = d sin(θ) = nλ. What changes with more slits is not the condition for where maxima occur (same positions), but the sharpness and intensity of the maxima. The double-slit and grating equations are the same formula; the difference in behavior comes entirely from the number of contributing slits. This is a subtle but important point: the grating doesn't 'change the rules,' it enforces the same constructive-interference rule much more strictly."

- question: "Why does a diffraction grating produce much sharper bright maxima than a double slit, even though both use the same grating equation d sin(θ) = nλ?"
  type: short-answer
  answer: "With only two slits, a small angular deviation from a maximum causes partial destructive interference — the two waves go slightly out of phase and partially cancel, so fringe intensity fades gradually on either side. With N slits (e.g., 1,000), the same small angular deviation introduces a small phase error between each adjacent pair of slits. These errors accumulate across all N slits: the total phase difference across the whole grating becomes large, and when you sum N waves with steadily increasing phase offsets, they nearly completely cancel. The result is that bright maxima become extremely narrow spikes with near-zero intensity on either side."
  explanation: "The sharpness scales inversely with N (fringe width ∝ 1/N) and intensity scales as N² at the maximum. The physical insight is that many slits act as a much more stringent 'vote' for constructive interference — all N slits must simultaneously reinforce, and this condition is only met over a very narrow angular range. Just as the accuracy of a clock improves with more oscillations, the precision of a grating improves with more slits. This is why gratings with thousands of lines per mm can resolve spectral lines that differ by fractions of a nanometer — they enforce the constructive-interference condition with extreme precision."
```

## Explainer

From your study of double-slit interference, you know that two slits produce bright fringes wherever the path length difference from the two slits equals a whole number of wavelengths: Δ = nλ. With only two sources, those fringes are broad and relatively dim, because only two waves are reinforcing each other. A **diffraction grating** extends this idea to hundreds or thousands of equally spaced parallel slits, each separated from its neighbors by the same distance d. The bright fringe condition is still Δ = nλ, which gives the grating equation d sin(θ) = nλ — mathematically identical to the double-slit condition, but with a radically different outcome.

The transformative effect of many slits is **sharpness**. When N slits all constructively interfere at angle θ, the resulting fringe is roughly N times narrower and N² times more intense than with two slits. Why? Because any slight deviation from the constructive-interference angle introduces a small phase error in each slit. With two slits, a small error produces only partial destructive interference — the fringe fades gradually. With 1,000 slits, the same small error puts each slit slightly out of phase with the next, and when you sum 1,000 waves with accumulating phase errors, they cancel almost completely. The result is that the bright maxima become narrow spikes separated by nearly dark regions. This is the power of the grating.

The integer n in the equation is the **diffraction order**: n = 0 is straight-through (all wavelengths at the same angle, so no spectral separation), n = ±1 are the first-order maxima, n = ±2 second-order, and so on. Each order fans out white light into a spectrum because d sin(θ) = nλ at different angles for different λ: blue light (shorter λ) bends less than red light (longer λ) at each order. This spectral spread makes gratings the core element of spectrometers — instruments that identify the wavelengths in a light source and hence the chemical composition of the emitting or absorbing material. Every emission spectrum you've seen — the lines of hydrogen, the glow of neon signs — is measured with a diffraction grating.

In solving grating problems, start by identifying d. It may be given as "600 lines per millimeter," meaning d = 1/600 mm ≈ 1.67 μm. Then apply d sin(θ) = nλ for each order of interest. Remember that sin(θ) cannot exceed 1, so the maximum observable order is n_max = floor(d/λ): higher orders would require the diffracted beam to travel at angles beyond 90°, which is physically impossible. For a grating with d = 1.67 μm and red light at λ = 633 nm, n_max = floor(1670/633) = floor(2.64) = 2 — only orders 0, ±1, and ±2 exist.

---
id: diffraction-gratings
title: Diffraction Gratings
domain: physics
course: waves-and-optics
prerequisites:
- id: youngs-double-slit
  type: hard
- id: single-slit-diffraction
  type: soft
- id: electromagnetic-spectrum
  type: soft
- id: multiple-slit-grating-equation
  type: soft
tags:
- diffraction grating
- spectroscopy
- principal maxima
- resolving power
stage: advanced
status: validated
---
# Diffraction Gratings

## Core Idea
A diffraction grating contains thousands of equally spaced slits. The many coherent sources interfere to produce extremely sharp, bright principal maxima at dsinθ = mλ (same condition as double slit). Because maxima are so narrow, different wavelengths are well-separated angularly, making gratings ideal spectrometers. The resolving power R = mN (where N is the number of slits) determines how closely spaced two wavelengths can be and still be distinguished.

## How It's Best Learned
Use a diffraction grating to observe the spectrum of white light and hydrogen discharge tube. Measure the angular positions of spectral lines and back-calculate wavelengths. Compare resolution to a prism spectrometer.

## Common Misconceptions
- A grating does not separate colors by dispersion (like a prism); it works by interference, and different wavelengths have maxima at different angles for the same grating equation.
- Higher grating orders give greater angular separation but also require more grating lines to maintain resolution.

## Questions

```yaml
- question: "A diffraction grating with N = 500 slits produces principal maxima. A second grating has N = 2000 slits with the same slit spacing d. Compared to the first grating, the second grating's principal maxima are:"
  type: multiple-choice
  options:
    - "At four times the angular separation from each other"
    - "At the same angular positions but four times sharper"
    - "Four times as bright but at slightly different angles"
    - "Four times as bright and equally sharp"
  answer: 1
  explanation: "The grating equation d sin θ = mλ determines WHERE maxima appear — it depends on slit spacing d, not the number of slits N. More slits (same d) do not shift positions. What changes is the sharpness: with more coherent sources, any slight angular deviation causes destructive interference to accumulate rapidly, making the peaks dramatically narrower. This is the key distinction from double-slit: the equation is the same, but N controls resolution, not position."

- question: "A physicist needs to resolve two spectral lines near λ = 500 nm separated by Δλ = 0.05 nm. Using diffraction order m = 1, what minimum number of illuminated slits N is required?"
  type: multiple-choice
  options:
    - "100 slits — the grating equation provides enough angular separation at this order"
    - "500 slits — resolving power scales with the slit spacing, not N"
    - "10,000 slits — resolving power R = mN must equal λ/Δλ = 10,000"
    - "N does not matter — only slit spacing d determines resolution"
  answer: 2
  explanation: "Resolving power R = mN must satisfy R ≥ λ/Δλ = 500/0.05 = 10,000. With m = 1, we need N ≥ 10,000. The common misconception is thinking that angular separation (set by d) is what determines resolution — but two wavelengths can have distinct angular positions and still be unresolvable if the peaks are too broad. It is the sharpness of the peaks, controlled by N, that determines whether nearby maxima can be distinguished."

- question: "A diffraction grating with more slits per millimeter produces its principal maxima at larger angles than a coarser grating, for the same wavelength and diffraction order."
  type: true-false
  answer: true
  explanation: "True. More slits per millimeter means smaller slit spacing d. From the grating equation d sin θ = mλ, smaller d requires larger sin θ — and thus larger θ — for the same m and λ. This is how finely ruled gratings achieve greater angular dispersion: the maxima are spread over a wider angular range, making spectral lines easier to separate spatially."

- question: "A diffraction grating and a glass prism both separate white light into its component colors through the same underlying physical mechanism."
  type: true-false
  answer: false
  explanation: "False. A prism separates colors through dispersion: its refractive index varies with wavelength, so different colors bend by different amounts upon entering and exiting the glass. A grating separates colors through interference: the constructive interference condition d sin θ = mλ makes different wavelengths satisfy the condition at different angles. The physics is entirely different — and gratings are preferred for precision spectroscopy because their angular dispersion is linear in λ and scales predictably with N, unlike the nonlinear dispersion of prisms."

- question: "Why does increasing the number of slits in a diffraction grating improve its ability to resolve closely spaced spectral lines, even though the angular positions of the principal maxima are unchanged?"
  type: short-answer
  answer: "More slits make the principal maxima sharper (narrower in angle). With more coherent sources all contributing, any slight deviation from the exact constructive-interference angle causes many slits to partially cancel each other, dropping the combined amplitude steeply toward zero. Sharper peaks mean two nearby wavelengths have less overlapping intensity — they can be distinguished as separate maxima. The resolving power R = mN captures this directly: more slits means narrower peaks means finer wavelength discrimination."
  explanation: "The grating equation sets the position of each maximum; the number of slits sets its width. The first minimum adjacent to a principal maximum is displaced by λ/(Nd cos θ) in angle — narrower for larger N. Two wavelengths are just resolvable when one's maximum coincides with the other's first minimum (the Rayleigh criterion). The more slits illuminated, the narrower each peak, and the closer together two wavelengths can be and still meet this criterion. This is why scientific spectrographs are built to illuminate as many grating lines as possible."
```

## Explainer

You already know from Young's double-slit experiment that two coherent sources produce an interference pattern with bright fringes wherever the path difference is an integer multiple of the wavelength: d sin θ = mλ. A diffraction grating extends this idea to thousands of slits — a typical grating has 500 to 1,200 slits per millimeter. The grating equation d sin θ = mλ is identical to the double-slit condition, so the bright maxima appear at exactly the same angles. What changes dramatically is the *sharpness* of those maxima.

With only two slits, the bright fringes are broad — intensity falls off gradually on either side of each maximum. With N slits all contributing coherently, the constructive interference peak becomes extraordinarily narrow. Think of it this way: if you are just a fraction of a degree away from the exact maximum angle, a wave from slit 1 and a wave from slit N/2 (halfway across the grating) are slightly out of phase. With two slits this barely matters; with 600 slits per millimeter, these small phase errors accumulate and the combined amplitude drops steeply to zero. The result is that the **principal maxima** are bright and razor-sharp, while everything between them is dark.

That sharpness is what makes gratings ideal for **spectroscopy**. Two wavelengths λ₁ and λ₂ that are close together produce principal maxima at slightly different angles. If the fringes are sharp enough, those two maxima are distinguishable — the wavelengths are *resolved*. The **resolving power** R = mN tells you quantitatively: in diffraction order m with N illuminated slits, you can distinguish two wavelengths separated by as little as Δλ = λ/R. More slits and higher orders both improve resolution, which is why real spectrographs are sized to illuminate as many grating lines as possible.

It is important not to confuse a diffraction grating with a prism. A prism separates colors because its refractive index varies with wavelength (dispersion) — different colors bend by different amounts. A grating separates colors because the grating equation d sin θ = mλ makes the constructive interference angle proportional to wavelength — longer wavelengths diffract at larger angles. The physics is entirely different: dispersion versus interference. In practice, gratings are preferred for precision spectroscopy because their angular dispersion is more uniform and their resolving power scales predictably with N, whereas prism dispersion is nonlinear and harder to calibrate.

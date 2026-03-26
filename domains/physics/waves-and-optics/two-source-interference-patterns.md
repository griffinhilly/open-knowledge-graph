---
id: two-source-interference-patterns
title: Two-Source Interference Patterns
domain: physics
course: waves-and-optics
prerequisites:
- id: constructive-destructive-interference
  type: hard
- id: wavelength-frequency-speed-relation
  type: hard
builds-toward:
- diffraction-gratings
- youngs-double-slit
tags:
- interference
- two-source
- pattern
stage: formal-systems
status: validated
---

# Two-Source Interference Patterns

## Core Idea
Two coherent sources separated by distance d create an interference pattern in space, with alternating regions of constructive and destructive interference. Bright fringes occur where the path difference equals nλ (n = 0, 1, 2, ...), and dark fringes occur where the path difference equals (n + ½)λ. The fringe spacing depends on wavelength, source separation, and observation distance.

## Questions

```yaml
- question: "Two coherent speakers broadcast at wavelength λ = 0.5 m. A listener is positioned so that the path difference from the two speakers to her location is 0.75 m. What does she observe?"
  type: multiple-choice
  options:
    - "Maximum sound (constructive interference) — path difference 0.75 m is greater than λ/2, so waves reinforce"
    - "Silence (destructive interference) — 0.75 m = 1.5λ, a half-integer multiple of wavelength, so crests meet troughs"
    - "Maximum sound — any path difference less than 1 m produces constructive interference"
    - "Silence — any path difference other than exactly zero produces destructive interference"
  answer: 1
  explanation: "0.75 m / 0.5 m = 1.5, which is a half-integer multiple of the wavelength (specifically 3λ/2). Destructive interference occurs at path differences of λ/2, 3λ/2, 5λ/2, ... — any (n + ½)λ for integer n. At these locations, the waves arrive exactly out of phase (crest meets trough) and cancel. Constructive interference occurs only at whole-number multiples: 0, λ, 2λ, etc. The pattern is determined entirely by the geometry of path differences."

- question: "Two coherent light sources are 1 mm apart and project fringes onto a screen 2 m away. The source separation is then doubled to 2 mm, while wavelength and screen distance remain constant. What happens to the fringe spacing?"
  type: multiple-choice
  options:
    - "The fringe spacing increases — sources farther apart cast a wider pattern"
    - "The fringe spacing decreases — the formula Δy = λL/d shows that larger d produces smaller fringe spacing"
    - "The fringe spacing stays the same — only wavelength affects the spacing"
    - "The pattern disappears — sources must be close enough for their wave fronts to overlap"
  answer: 1
  explanation: "The fringe spacing formula is Δy = λL/d. With d in the denominator, doubling the source separation halves the fringe spacing. This is counterintuitive: wider source separation makes the fringes *narrower*, not wider. The physical reason: farther-apart sources reach the same path-difference conditions at smaller angular separations, compressing the fringe pattern. Conversely, using a longer wavelength or placing the screen farther away widens the fringes."

- question: "Two incoherent light sources (with randomly fluctuating phase relationship) can produce a stable two-source interference pattern on a screen if they emit the same wavelength."
  type: true-false
  answer: false
  explanation: "Coherence — a fixed phase relationship between the two sources over time — is required for a stable pattern. Incoherent sources have a phase difference that fluctuates randomly, so the fringe positions shift continuously and wash out into uniform brightness when averaged over time. Same wavelength is necessary but not sufficient. This is why Young's original experiment used a single source illuminating two slits: both slits are driven by the same wavefront, guaranteeing coherence."

- question: "In a two-source interference pattern, the central bright fringe at the center of the screen corresponds to a path difference of exactly one wavelength."
  type: true-false
  answer: false
  explanation: "The central bright fringe occurs where the path difference equals zero — both sources are equidistant from the center of the screen, so the waves arrive perfectly in phase regardless of wavelength. A path difference of exactly one wavelength (1λ) gives the first-order bright fringe, displaced from the center. The condition for constructive interference is path difference = nλ for any integer n, and n=0 is the central (zeroth-order) fringe."

- question: "Explain why two separate light bulbs illuminating two pinholes would NOT produce a stable interference pattern, but a single light bulb illuminating two pinholes WOULD. What property is required and why does the setup matter?"
  type: short-answer
  answer: "Coherence — a fixed, stable phase relationship between the two sources — is required for a stable interference pattern. Two separate light bulbs emit light with independently and randomly fluctuating phases. Even if both illuminate the same pinholes, the phase difference between the two pinholes varies randomly, so the fringe positions shift constantly and average out to uniform brightness. A single bulb illuminating two pinholes guarantees coherence: both pinholes are driven by the same wavefront, so the phase difference between them is constant (zero for a point source on the axis). The fringes are stable because the interference condition is fixed in space."
  explanation: "This is why lasers made interference experiments easy and why Young's original 1801 experiment was so ingenious — it extracted coherence from ordinary (incoherent) sunlight by using a single pinhole as the source and two downstream pinholes as the coherent pair. The spatial coherence of the single source is transferred to the pair. Modern interference experiments typically use laser light directly, since laser emission is highly coherent by design."
```

## Explainer

You already know the core principle from constructive and destructive interference: when two waves overlap, their amplitudes add. If they arrive in phase — crest meeting crest — you get a bright spot. If they arrive half a wavelength out of phase — crest meeting trough — they cancel. Two-source interference patterns take this idea and map it across a region of space: at every point in front of the sources, the two waves travel different distances, and that **path difference** determines whether those waves arrive in phase or out of phase.

Imagine two identical speakers (or the two slits in Young's experiment, or two antennas) separated by distance d, both broadcasting the same wavelength λ. For any observation point P, draw lines from each source to P. The difference in those two distances is the path difference Δ. If Δ = 0, 1λ, 2λ, ... — any whole number of wavelengths — the waves arrive perfectly in phase and you get a **bright fringe** (constructive interference). If Δ = ½λ, 3/2λ, 5/2λ, ... — any half-integer number of wavelengths — the waves arrive exactly out of phase and you get a **dark fringe** (destructive interference). The pattern of bright and dark bands you observe on a distant screen is simply the spatial map of where these path-difference conditions are satisfied.

The geometry makes the fringe spacing predictable. For a screen at distance L >> d, the fringe spacing Δy = λL/d. Three variables control the pattern: wavelength λ (longer wavelength → wider fringes), source separation d (closer sources → wider fringes), and screen distance L (farther screen → wider fringes). These relationships are not independent of your prerequisite knowledge — **wavelength** and **frequency** are linked by v = fλ, so changing frequency changes λ, which directly rescales the entire fringe pattern.

**Coherence** is the hidden requirement that makes the pattern stable. Both sources must maintain a fixed phase relationship over time — they must be synchronized. Sunlight from two separate holes would not produce a stable pattern because the phase relationship randomly fluctuates; the bright and dark fringes would wash out into uniform brightness. This is why Young's original experiment used a single source illuminating two slits (the slits are coherent because they're both driven by the same wavefront), and why laser sources make interference experiments easy while ordinary light bulbs do not. Two-source interference is the simplest model for understanding all wave interference, and Young's double-slit result — which you'll see next — is its most famous application.

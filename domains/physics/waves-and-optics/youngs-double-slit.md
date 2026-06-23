---
id: youngs-double-slit
title: 'Young''s Double-Slit Experiment'
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-interference
  type: hard
- id: electromagnetic-waves
  type: soft
- id: right-triangle-trigonometry-intro
  type: hard
- id: electromagnetic-spectrum
  type: soft
- id: huygens-principle
  type: soft
- id: wave-energy-and-intensity
  type: soft
- id: two-source-interference-patterns
  type: hard
builds-toward:
- single-slit-diffraction
- diffraction-gratings
- thin-film-interference
tags:
- double slit
- interference fringes
- path difference
- Young
- light
stage: advanced
status: validated
---
# Young's Double-Slit Experiment

## Core Idea
Thomas Young's 1801 experiment demonstrated the wave nature of light by passing it through two narrow slits and observing alternating bright and dark bands (fringes) on a screen. Bright fringes occur where the path difference from the two slits is an integer number of wavelengths (dsinθ = mλ); dark fringes occur at half-integer path differences. The fringe spacing Δy ≈ λL/d provides a precise way to measure the wavelength of light.

## How It's Best Learned
Set up a laser pointer shining through a double-slit card onto a wall. Measure fringe spacing and back-calculate λ. Then vary slit separation d and screen distance L to see how fringe spacing changes.

## Common Misconceptions
- The double-slit pattern is not simply two overlapping single-slit images; it arises from wave interference between the two coherent sources.
- Central bright fringe is the zeroth order (m=0), not the first order.

## Questions

```yaml
- question: "In Young's experiment, slit separation d is doubled while screen distance L and wavelength λ remain unchanged. What happens to the fringe spacing?"
  type: multiple-choice
  options:
    - "It doubles — wider slits spread light further apart"
    - "It halves — the path-difference geometry changes more rapidly with angle"
    - "It stays the same — fringe spacing depends only on wavelength"
    - "It quadruples — the effect of d is squared in the formula"
  answer: 1
  explanation: "Fringe spacing Δy ≈ λL/d. Doubling d while holding λ and L constant halves Δy. The intuition: wider slit separation means the path difference dsinθ reaches one full wavelength at a smaller angle, squeezing the bright fringes closer together. Option A reverses the relationship, and options C and D misread the formula."

- question: "Newton's corpuscular theory predicted that passing light through two slits would produce two bright bands on the screen. Young instead observed alternating bright and dark bands. Why is this a decisive argument for the wave nature of light?"
  type: multiple-choice
  options:
    - "Particles travel in straight lines and would miss the screen at the dark regions"
    - "Waves can cancel — two waves arriving out of phase produce zero amplitude, but two particles cannot cancel each other"
    - "The bright bands are brighter than a single slit would produce, proving energy is being added"
    - "The dark bands occur exactly where no light hits, proving light bends around corners"
  answer: 1
  explanation: "The dark fringes are the decisive evidence. If light were corpuscular, two streams of particles can only add — you would see two bright bands or a uniform glow, never a region darker than either slit alone. The existence of dark bands (destructive interference) is only possible if light has a wave nature: waves arriving exactly out of phase (half-integer path difference) cancel via superposition. Particles simply cannot cancel each other."

- question: "Bright fringes in Young's double-slit experiment occur where the path difference from the two slits equals an integer multiple of the wavelength."
  type: true-false
  answer: true
  explanation: "This is the constructive interference condition: d sinθ = mλ (m = 0, ±1, ±2, …). When both waves travel the same total distance (or differ by exactly one, two, … wavelengths), they arrive perfectly in phase — crest meets crest, trough meets trough — and their amplitudes add to produce a bright fringe."

- question: "Dark fringes in Young's experiment appear because light from one slit is physically blocked from reaching those regions of the screen by the other slit."
  type: true-false
  answer: false
  explanation: "Dark fringes are not caused by blocking — both slits are open, and light from each slit reaches every part of the screen. Dark fringes arise from destructive interference: when the path difference is a half-integer number of wavelengths (m + ½)λ, the two waves arrive exactly out of phase and their amplitudes cancel. This is wave superposition, not obstruction. The misconception misidentifies a diffraction effect as a geometric shadow effect."

- question: "Why do dark fringes appear in Young's experiment, and what does their existence prove about the nature of light?"
  type: short-answer
  answer: "Dark fringes appear because light from the two slits travels different distances to reach points off-center on the screen. Where this path difference is a half-integer number of wavelengths, the waves arrive 180° out of phase and cancel. This cancellation — two sources of light combining to produce darkness — is only possible if light is a wave. Particles cannot cancel; they can only add. The dark fringes are therefore direct physical evidence that light undergoes wave superposition."
  explanation: "The key distinction is between additive and cancellation behavior. Particle models always predict at least as much intensity with two sources as with one. The fact that adding a second slit can make certain regions darker is the fingerprint of wave interference and cannot be explained by any particle model."
```

## Explainer

From your study of wave interference, you know that two waves overlapping in space either reinforce or cancel depending on whether they arrive **in phase** or **out of phase**. Young's double-slit experiment is nothing more than a precise geometric arrangement that converts this superposition principle into a visible spatial pattern. The two slits act as two coherent sources of light — like two speakers emitting the same frequency — and at every point on the screen the two waves arrive having traveled slightly different distances. That difference in travel distance, the **path difference**, determines whether the waves arrive in phase (bright fringe) or out of phase (dark fringe).

The geometry is the key tool, and your right-triangle trigonometry makes it tractable. Each slit is separated from the other by distance d. A point P on the screen at angle θ from the center is closer to one slit than the other by a distance d sin θ. When this **path difference** equals an integer number of wavelengths (d sin θ = mλ), the two waves arrive perfectly in phase and produce a bright fringe. When it equals a half-integer number of wavelengths — (m + ½)λ — they arrive exactly out of phase and cancel to a dark fringe. For small angles (which is the typical experimental regime), sin θ ≈ tan θ, and since tan θ = y/L (where y is the height on the screen and L is the slit-to-screen distance), the fringe positions are nearly equally spaced. The fringe spacing Δy ≈ λL/d follows directly from this small-angle geometry.

This formula is experimentally powerful. All three variables — wavelength λ, slit separation d, and screen distance L — are independently adjustable, and their effect on fringe spacing is immediately visible. Wider slits (larger d) squeeze the fringes closer together because the path-difference geometry changes more quickly with angle. Shorter wavelengths (bluer light) also squeeze the fringes in, which is why blue and red light produce patterns with different fringe spacings. By measuring Δy and knowing d and L, you can calculate the wavelength of the light to high precision — which is exactly what Young did in 1801, providing one of the first measurements of optical wavelength and, crucially, demonstrating that light behaves as a wave.

The historical significance cannot be overstated. Newton's particle (corpuscular) theory of light — dominant for over a century — predicted that two slits would simply produce two bright bands on the screen. Instead, Young observed alternating light and dark bands. Particles cannot cancel each other; waves can. The dark fringes between the bright ones are the fingerprint of wave superposition, and their presence is direct evidence that light has a wavelength. Every later development in wave optics — diffraction gratings, thin-film interference, holography — rests on the same path-difference logic you use here, making the double-slit experiment both the conceptual entry point and the experimental prototype for all of wave optics.

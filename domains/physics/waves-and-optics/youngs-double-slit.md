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
stage: formal-systems
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

## Explainer

From your study of wave interference, you know that two waves overlapping in space either reinforce or cancel depending on whether they arrive **in phase** or **out of phase**. Young's double-slit experiment is nothing more than a precise geometric arrangement that converts this superposition principle into a visible spatial pattern. The two slits act as two coherent sources of light — like two speakers emitting the same frequency — and at every point on the screen the two waves arrive having traveled slightly different distances. That difference in travel distance, the **path difference**, determines whether the waves arrive in phase (bright fringe) or out of phase (dark fringe).

The geometry is the key tool, and your right-triangle trigonometry makes it tractable. Each slit is separated from the other by distance d. A point P on the screen at angle θ from the center is closer to one slit than the other by a distance d sin θ. When this **path difference** equals an integer number of wavelengths (d sin θ = mλ), the two waves arrive perfectly in phase and produce a bright fringe. When it equals a half-integer number of wavelengths — (m + ½)λ — they arrive exactly out of phase and cancel to a dark fringe. For small angles (which is the typical experimental regime), sin θ ≈ tan θ, and since tan θ = y/L (where y is the height on the screen and L is the slit-to-screen distance), the fringe positions are nearly equally spaced. The fringe spacing Δy ≈ λL/d follows directly from this small-angle geometry.

This formula is experimentally powerful. All three variables — wavelength λ, slit separation d, and screen distance L — are independently adjustable, and their effect on fringe spacing is immediately visible. Wider slits (larger d) squeeze the fringes closer together because the path-difference geometry changes more quickly with angle. Shorter wavelengths (bluer light) also squeeze the fringes in, which is why blue and red light produce patterns with different fringe spacings. By measuring Δy and knowing d and L, you can calculate the wavelength of the light to high precision — which is exactly what Young did in 1801, providing one of the first measurements of optical wavelength and, crucially, demonstrating that light behaves as a wave.

The historical significance cannot be overstated. Newton's particle (corpuscular) theory of light — dominant for over a century — predicted that two slits would simply produce two bright bands on the screen. Instead, Young observed alternating light and dark bands. Particles cannot cancel each other; waves can. The dark fringes between the bright ones are the fingerprint of wave superposition, and their presence is direct evidence that light has a wavelength. Every later development in wave optics — diffraction gratings, thin-film interference, holography — rests on the same path-difference logic you use here, making the double-slit experiment both the conceptual entry point and the experimental prototype for all of wave optics.

---
id: thin-film-interference
title: Thin-Film Interference
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-interference
  type: hard
- id: snells-law
  type: hard
- id: youngs-double-slit
  type: soft
tags:
- thin film
- optical path length
- phase shift
- anti-reflection
- soap bubble
stage: formal-systems
status: validated
---
# Thin-Film Interference

## Core Idea
When light reflects from both surfaces of a thin transparent film, the two reflected beams interfere. The path difference equals 2nt (where n is the film's index of refraction and t is thickness), but a phase shift of π (half wavelength) occurs whenever light reflects off a medium with higher refractive index. This means a film of thickness t = λ/4n gives destructive interference for reflected light (used in anti-reflection coatings) while t = λ/2n gives constructive interference.

## How It's Best Learned
Examine a soap bubble or oil slick in sunlight and observe the swirling colors. Map which wavelengths are constructively vs destructively reflected at a given film thickness and work through the phase-shift accounting systematically.

## Common Misconceptions
- Students often forget the phase shift upon reflection, leading to wrong conditions for constructive/destructive interference.
- Both reflections must be accounted for — only one may receive a phase shift depending on relative indices.

## Explainer

From wave interference and Snell's law you know two things: waves that are in phase add up while waves a half-wavelength out of phase cancel, and light slows down and bends when it enters a denser medium. Thin-film interference combines both ideas. When a beam of light hits a thin transparent layer — a soap bubble, an oil slick, an anti-reflection coating — it splits at the first surface. One portion reflects immediately from the top; the rest transmits into the film, bounces off the bottom surface, and exits upward. These two reflected beams then travel together and interfere. The question is always: what is the phase difference between them?

The phase difference has two contributions. The first is the **optical path difference**: the beam that went through the film traveled an extra distance of 2t (down through thickness t and back up), but inside a medium of refractive index n, so the effective extra distance is 2nt. Converting to phase: every wavelength λ of path difference corresponds to 2π of phase, so the path-difference contribution is (2π/λ) × 2nt. The second contribution comes from **phase shifts upon reflection**: whenever a wave reflects off a boundary with a higher refractive index, it picks up a phase shift of π (a half-wavelength flip). This is analogous to a pulse on a rope reversing when it hits a fixed wall. In the standard soap bubble geometry, the top reflection (air→film, denser medium) acquires a π shift; the bottom reflection (film→air, less dense medium) does not. The net effect is an extra half-wavelength of phase difference injected by the reflections alone.

Putting these together: the total phase difference is (4πnt/λ) + π (from the one phase-flipped reflection). Destructive interference — the two beams canceling — occurs when the total phase difference is an odd multiple of π, meaning the path-difference term alone equals an even multiple of π: 2nt = mλ, where m is an integer. Constructive interference requires the path-difference term to supply the extra half-wavelength to compensate: 2nt = (m + ½)λ. This is counterintuitive at first — the thickness condition for constructive interference looks like "half-integer wavelengths" rather than "whole wavelengths" — but it follows directly from accounting for the one phase flip.

The practical application is the **anti-reflection coating** on camera lenses and eyeglasses. A thin layer of magnesium fluoride (n ≈ 1.38) is deposited on glass (n ≈ 1.5). Now both reflections occur at a denser medium (air→coating and coating→glass), so both acquire a π phase shift — they cancel each other out, and the destructive interference condition becomes 2nt = λ/2, or t = λ/(4n), a quarter-wavelength optical thickness. A coating tuned to visible green light (λ ≈ 550 nm) reflects nearly zero green light, which is why coated lenses have a characteristic purple-magenta tint: green is suppressed while the red and blue ends of the spectrum reflect more freely.

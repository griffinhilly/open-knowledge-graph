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
- id: constructive-destructive-interference
  type: hard
- id: optical-path-length-definition
  type: soft
tags:
- thin film
- optical path length
- phase shift
- anti-reflection
- soap bubble
stage: advanced
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

## Questions

```yaml
- question: "A soap bubble film (air outside, film with n > 1, air inside) has thickness t = λ/(4n). Considering that only the top reflection (air-to-film) acquires a π phase shift, what does this film produce for reflected light?"
  type: multiple-choice
  options:
    - "Destructive interference — a quarter-wave film always cancels reflected light"
    - "Constructive interference — the phase flip combines with the path difference to bring the beams into phase"
    - "No interference — the film is too thin to produce a measurable effect"
    - "Partial interference only — the beams must have equal amplitude to interfere"
  answer: 1
  explanation: "For a soap bubble with one phase flip: total phase = (4πnt/λ) + π. At t = λ/(4n): 4πnt/λ = 4πn·(λ/4n)/λ = π. Total phase = π + π = 2π — constructive interference. This is the soap bubble's first constructive maximum. Intuition says a quarter-wave film should cancel, which IS true when both reflections flip (the anti-reflection coating case). With only one flip, the condition inverts: a quarter-wave film gives constructive for a soap bubble but destructive for a coated lens on glass — the same thickness produces opposite results depending on the number of phase shifts."

- question: "When light reflects from the two surfaces of a thin film, which reflections acquire a π phase shift?"
  type: multiple-choice
  options:
    - "Both reflections always acquire a π phase shift at any interface"
    - "Only the top reflection (entering the film from less dense medium) acquires a π phase shift; the bottom reflection (exiting to less dense medium) does not"
    - "Only the bottom reflection acquires a π phase shift, because the light has already slowed down inside the film"
    - "Neither reflection acquires a phase shift unless the film is thicker than λ/2"
  answer: 1
  explanation: "A π phase shift occurs whenever light reflects off a medium with a HIGHER refractive index — analogous to a wave on a rope reflecting off a fixed end. For a soap bubble (air n=1, film n≈1.33, air n=1): the top reflection is air→film (going to higher n) → π shift acquired; the bottom reflection is film→air (going to lower n) → no shift. This asymmetry is critical: it changes the conditions for constructive and destructive interference. If both reflections flip or neither does, the conditions are different again (as in anti-reflection coatings on glass)."

- question: "When light reflects off a medium with a higher refractive index, it undergoes a phase shift of π, analogous to a transverse wave on a string reflecting off a fixed wall."
  type: true-false
  answer: true
  explanation: "This phase shift is a general wave phenomenon at boundaries where the wave is entering a 'harder' medium. For electromagnetic waves, the boundary conditions of Maxwell's equations require a sign reversal of the electric field upon reflection from a denser medium — equivalent to a half-wavelength phase shift. The string analogy is exact: a pulse traveling along a rope and hitting a fixed (immovable) wall reflects inverted; a pulse hitting a free end reflects non-inverted. Dense medium = fixed wall (inverted/π shift); less-dense medium = free end (no shift)."

- question: "For a very thin soap bubble film (thickness approaching zero), the two reflected beams interfere constructively because the path difference between them approaches zero."
  type: true-false
  answer: false
  explanation: "As t → 0, the optical path difference 2nt → 0, so the phase contribution from the path difference → 0. However, the top reflection still acquires a π phase shift regardless of thickness. Total phase → 0 + π = π, which gives DESTRUCTIVE interference. This is why very thin soap bubble films appear black (near the top where gravity has thinned them most): they reflect essentially no light. The black film is not an absence of film but a demonstration that the π phase flip from reflection dominates when path-length effects are negligible."

- question: "Why does an anti-reflection coating of thickness t = λ/(4n) suppress reflected light? Why does careful phase-shift accounting matter here?"
  type: short-answer
  answer: "An AR coating (e.g., MgF₂ on glass) has n_coating between n_air and n_glass, so BOTH reflections occur at a denser medium — both acquire a π phase shift. These two shifts sum to 2π (a full cycle), effectively canceling each other. The path difference at t = λ/(4n) contributes phase = 4πnt/λ = π. Total phase = 0 (from two canceling flips) + π (from path) = π → destructive interference. Without tracking both phase shifts, one would naively set 2nt = λ/2 (half-wave path difference) for destructive, but that actually produces constructive interference in this two-flip geometry."
  explanation: "The phase accounting table clarifies all cases: (0 flips) constructive when 2nt = mλ; (1 flip, soap bubble) constructive when 2nt = (m+½)λ; (2 flips, AR coating) constructive when 2nt = mλ again (flips cancel). The same film thickness means completely different interference results depending on the stack geometry. Anti-reflection coatings work precisely because the two flips cancel, leaving the path difference alone to produce destructive interference at the designed wavelength."
```

## Explainer

From wave interference and Snell's law you know two things: waves that are in phase add up while waves a half-wavelength out of phase cancel, and light slows down and bends when it enters a denser medium. Thin-film interference combines both ideas. When a beam of light hits a thin transparent layer — a soap bubble, an oil slick, an anti-reflection coating — it splits at the first surface. One portion reflects immediately from the top; the rest transmits into the film, bounces off the bottom surface, and exits upward. These two reflected beams then travel together and interfere. The question is always: what is the phase difference between them?

The phase difference has two contributions. The first is the **optical path difference**: the beam that went through the film traveled an extra distance of 2t (down through thickness t and back up), but inside a medium of refractive index n, so the effective extra distance is 2nt. Converting to phase: every wavelength λ of path difference corresponds to 2π of phase, so the path-difference contribution is (2π/λ) × 2nt. The second contribution comes from **phase shifts upon reflection**: whenever a wave reflects off a boundary with a higher refractive index, it picks up a phase shift of π (a half-wavelength flip). This is analogous to a pulse on a rope reversing when it hits a fixed wall. In the standard soap bubble geometry, the top reflection (air→film, denser medium) acquires a π shift; the bottom reflection (film→air, less dense medium) does not. The net effect is an extra half-wavelength of phase difference injected by the reflections alone.

Putting these together: the total phase difference is (4πnt/λ) + π (from the one phase-flipped reflection). Destructive interference — the two beams canceling — occurs when the total phase difference is an odd multiple of π, meaning the path-difference term alone equals an even multiple of π: 2nt = mλ, where m is an integer. Constructive interference requires the path-difference term to supply the extra half-wavelength to compensate: 2nt = (m + ½)λ. This is counterintuitive at first — the thickness condition for constructive interference looks like "half-integer wavelengths" rather than "whole wavelengths" — but it follows directly from accounting for the one phase flip.

The practical application is the **anti-reflection coating** on camera lenses and eyeglasses. A thin layer of magnesium fluoride (n ≈ 1.38) is deposited on glass (n ≈ 1.5). Now both reflections occur at a denser medium (air→coating and coating→glass), so both acquire a π phase shift — they cancel each other out, and the destructive interference condition becomes 2nt = λ/2, or t = λ/(4n), a quarter-wavelength optical thickness. A coating tuned to visible green light (λ ≈ 550 nm) reflects nearly zero green light, which is why coated lenses have a characteristic purple-magenta tint: green is suppressed while the red and blue ends of the spectrum reflect more freely.

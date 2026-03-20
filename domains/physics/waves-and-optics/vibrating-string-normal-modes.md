---
id: vibrating-string-normal-modes
title: Resonance in Strings and Normal Modes
domain: physics
course: waves-and-optics
prerequisites:
- id: standing-waves
  type: hard
- id: wavelength-frequency-speed-relation
  type: hard
builds-toward:
- fundamental-frequency-and-overtones
tags:
- resonance
- strings
- harmonics
stage: advanced
status: draft
---

# Resonance in Strings and Normal Modes

## Core Idea
A string fixed at both ends resonates at frequencies where standing waves fit exactly: f_n = nv/(2L) for n = 1, 2, 3,... (n = 1 is the fundamental, higher n are harmonics). Wave speed v = √(T/μ) depends on tension T and mass per unit length μ. Plucking excites multiple harmonics simultaneously, determining the string's timbre.

## Explainer

You've studied standing waves: two identical waves traveling in opposite directions interfere to create a pattern of **nodes** (points of zero displacement) and **antinodes** (points of maximum displacement) that appears stationary. A string fixed at both ends is a perfect physical realization of this — the fixed endpoints are forced to be nodes. The physics then constrains which standing waves are geometrically possible.

The constraint is simple: only wavelengths that fit an integer number of half-wavelengths within the string's length L are allowed. The longest possible wave — one loop with one antinode — has λ₁ = 2L. The next pattern has two loops: λ₂ = L. Then three loops: λ₃ = 2L/3. In general, λₙ = 2L/n. These are the only patterns that produce nodes at both fixed endpoints; all others cancel destructively and cannot persist. They are the **normal modes** of the string.

Now apply the wave relation v = fλ. The wave speed v = √(T/μ) depends on the physical properties of the string — tension T and mass per unit length μ — and is fixed for a given string. The allowed frequencies are f_n = v/λₙ = nv/(2L). The lowest, f₁ = v/(2L), is the **fundamental**. Higher harmonics are exact integer multiples: f₂ = 2f₁, f₃ = 3f₁, and so on. This integer relationship is what makes a vibrating string sound musical — the harmonics align into a tonal pattern the ear interprets as pitch.

When you pluck a guitar string, you excite many harmonics simultaneously. The relative amplitudes of those harmonics determine the **timbre** — the tonal quality that makes a violin sound different from a guitar even at the same pitch. Tuning uses both control variables: tightening the string (increasing T) raises v and therefore raises all f_n proportionally; pressing the string against a fret shortens the effective length L, also raising frequency. A guitarist pressing the 12th fret halves L, doubling all frequencies — raising the pitch by exactly one octave, which is the f₁ → 2f₁ interval.

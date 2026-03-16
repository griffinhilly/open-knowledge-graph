---
id: resonance-strings-and-pipes
title: Resonance in Strings and Pipes
domain: physics
course: waves-and-optics
prerequisites:
- id: standing-waves
  type: hard
builds-toward:
- sound-intensity-and-decibels
tags:
- resonance
- harmonics
- strings
- open pipe
- closed pipe
- overtones
stage: abstract-reasoning
status: validated
---

# Resonance in Strings and Pipes

## Core Idea
When a system is driven at one of its natural (resonant) frequencies, standing waves form and large amplitude vibrations build up. For a string fixed at both ends or an open pipe (antinodes at both ends), all integer harmonics are present: fₙ = nf₁. A pipe closed at one end (node at closed end, antinode at open end) supports only odd harmonics: fₙ = nf₁, n = 1, 3, 5…. These principles underlie the physics of all string and wind instruments.

## How It's Best Learned
Blow across the tops of test tubes with varying water levels to hear how pitch changes with pipe length. Derive the harmonic series for open and closed pipes and compare experimentally.

## Common Misconceptions
- The closed-pipe result surprises students who expect the same harmonic series as open pipes; the boundary condition difference (node vs antinode at the closed end) changes which modes are allowed.
- Resonance does not require large driving amplitude — it requires matching the natural frequency.

## Explainer

From your study of standing waves, you know that a standing wave forms when a wave and its reflection superimpose to produce fixed **nodes** (zero displacement) and **antinodes** (maximum displacement). The key constraint is that only certain wavelengths fit a given geometry — those that satisfy the boundary conditions at both ends simultaneously. **Resonance** is what happens when you drive the system at one of those allowed frequencies: energy accumulates with each cycle rather than being disrupted by destructive interference, and large-amplitude vibrations build up.

For a **string fixed at both ends**, both endpoints must be displacement nodes — the string can't move where it's clamped. The longest wavelength that satisfies this is a half-wavelength: the string vibrates in one arch, with L = λ₁/2, so λ₁ = 2L and f₁ = v/(2L). This is the **fundamental frequency** or first harmonic. But any integer number of half-wavelengths also fits: λₙ = 2L/n, giving fₙ = nf₁ for n = 1, 2, 3, ... This full **harmonic series** — all integer multiples of f₁ — is present because the boundary conditions (node-node) are symmetric and allow both even and odd numbers of half-wavelengths. An **open pipe** (open at both ends) behaves identically, because open ends are displacement antinodes, and the antinode-antinode boundary conditions produce the same mathematical constraint.

A **pipe closed at one end** changes the boundary conditions asymmetrically: the closed end must be a displacement node (the air can't move against a rigid wall) while the open end must be a displacement antinode (air is free to move). The smallest number of wavelength fractions that satisfies node-at-one-end, antinode-at-other-end is a quarter-wavelength: L = λ₁/4, so λ₁ = 4L and f₁ = v/(4L). Notice this fundamental is lower than the open pipe of the same length — a closed pipe resonates at a lower pitch. The next allowed mode must again start at a node and end at an antinode, which requires three-quarter wavelengths: L = 3λ/4, giving f₃ = 3f₁. Only odd multiples fit: fₙ = nf₁ for n = 1, 3, 5, ... The even harmonics are absent because no even multiple of a quarter-wavelength satisfies both boundary conditions simultaneously.

These principles explain the characteristic sounds of musical instruments. A guitar string (fixed-fixed: all harmonics) produces a rich, full tone. A clarinet behaves approximately as a closed cylindrical pipe (odd harmonics only), giving a hollow, woody timbre distinct from a flute (open pipe, all harmonics). A skilled instrumentalist adjusts pitch by changing the effective vibrating length — fretting a string, covering tone holes in a wind instrument — which shifts the fundamental and with it the entire harmonic series. The physics you have just worked through is the foundation of all acoustic instrument design.

## Questions

```yaml
- question: "A string of length 0.8 m has a wave speed of 320 m/s. What are the frequencies of the first three harmonics?"
  type: short-answer
  answer: "f₁ = v/(2L) = 320/(2·0.8) = 200 Hz. f₂ = 2f₁ = 400 Hz. f₃ = 3f₁ = 600 Hz. All integer harmonics are present because the string is fixed at both ends."
  explanation: "The fundamental formula for a string (or open pipe) is f₁ = v/(2L). Each higher harmonic is an integer multiple: fₙ = nf₁. For a fixed-fixed string, n = 1, 2, 3, ... with no missing harmonics."

- question: "Why does a pipe closed at one end only support odd harmonics?"
  type: short-answer
  answer: "A closed end requires a displacement node; an open end requires an antinode. The only wavelengths that satisfy node-at-one-end and antinode-at-the-other end are those where the pipe length equals an odd multiple of a quarter-wavelength: L = λ/4, 3λ/4, 5λ/4... This gives frequencies fₙ = nf₁ where n = 1, 3, 5 only. Even multiples would require the same boundary condition at both ends, which isn't the case here."
  explanation: "Contrast with an open pipe (antinode at both ends) or a fixed string (node at both ends) — those symmetric conditions allow both even and odd harmonics. The asymmetric boundary conditions of the closed pipe are what eliminate the even harmonics."

- question: "An open organ pipe has a fundamental frequency of 120 Hz. A closed pipe of the same length is played. What is its fundamental frequency, and what harmonics does it produce?"
  type: multiple-choice
  options:
    - "120 Hz; all integer harmonics"
    - "60 Hz; odd harmonics only"
    - "240 Hz; even harmonics only"
    - "60 Hz; all integer harmonics"
  answer: 1
  explanation: "A closed pipe's fundamental is v/(4L), while an open pipe's is v/(2L). Same length means the closed fundamental is exactly half: 60 Hz. And because of the asymmetric boundary conditions, closed pipes only produce odd harmonics: 60 Hz, 180 Hz, 300 Hz, ..."
```

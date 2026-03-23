---
id: acoustic-resonance-pipes
title: Acoustic Resonance in Pipes and Air Columns
domain: physics
course: waves-and-optics
prerequisites:
- id: standing-waves-formation-mechanism
  type: hard
- id: sound-waves-longitudinal
  type: hard
builds-toward:
- fundamental-frequency-and-overtones
tags:
- resonance
- pipes
- air-columns
- open-closed
stage: formal-systems
status: validated
---

# Acoustic Resonance in Pipes and Air Columns

## Core Idea
Pipes open at both ends resonate at f_n = nv/(2L), producing antinodes at both ends. Pipes closed at one end resonate at odd harmonics only: f_n = (2n-1)v/(4L), producing a node at the closed end and antinode at the open end. These boundary condition differences explain why closed pipes have a different tone quality despite having the same length as open pipes.

## Questions

```yaml
- question: "A closed-open pipe and an open-open pipe have the same length L. What is the ratio of their fundamental frequencies (closed : open)?"
  type: multiple-choice
  options:
    - "2 : 1 — the closed pipe vibrates twice as fast"
    - "1 : 2 — the closed pipe has half the fundamental frequency of the open pipe"
    - "1 : 1 — same length means same fundamental frequency"
    - "1 : 4 — the closed pipe vibrates at one-quarter the frequency"
  answer: 1
  explanation: "Open-open: f₁ = v/(2L). Closed-open: f₁ = v/(4L). Ratio = (v/4L)/(v/2L) = 1/2. The closed pipe's fundamental frequency is half that of the open pipe — one octave lower — because the node at the closed end forces the standing wave to fit a quarter-wavelength across L rather than a half-wavelength. The boundary conditions, not the length alone, determine the pitch."

- question: "A clarinet (closed-open pipe) produces a fundamental frequency of 220 Hz. Which harmonics does it produce?"
  type: multiple-choice
  options:
    - "220 Hz, 440 Hz, 660 Hz, 880 Hz (all integer multiples)"
    - "220 Hz, 660 Hz, 1100 Hz (odd multiples only)"
    - "440 Hz, 880 Hz, 1320 Hz (even multiples only)"
    - "220 Hz, 330 Hz, 440 Hz (multiples of 1.5)"
  answer: 1
  explanation: "A closed-open pipe supports only odd harmonics: f_n = (2n−1)v/(4L), giving frequencies at 1×, 3×, 5×, … the fundamental. At 220 Hz: 220, 660, 1100, 1540 Hz, etc. The even harmonics (440, 880 Hz) are absent because no standing wave satisfying 'node at closed end, antinode at open end' can fit an even number of quarter-wavelengths across the pipe. This restricted harmonic series produces the clarinet's characteristically hollow timbre."

- question: "An open end of a resonating pipe is always a displacement antinode."
  type: true-false
  answer: true
  explanation: "At an open end, air molecules are free to move — there is no wall to constrain them. This freedom means displacement is at maximum, making the open end an antinode by physical necessity. At a closed end, the wall prevents air displacement, forcing a node. These boundary conditions are imposed by the physics of the situation, and they determine which wavelengths can fit in the pipe and therefore which frequencies resonate."

- question: "Two pipes of the same length but different end conditions (one open-open, one closed-open) will resonate at the same fundamental frequency."
  type: true-false
  answer: false
  explanation: "End conditions change everything. An open-open pipe of length L fits a half-wavelength as its fundamental: f₁ = v/(2L). A closed-open pipe fits only a quarter-wavelength: f₁ = v/(4L). The closed-open pipe sounds one full octave lower despite being the same physical length. This is why instrument designers treat end conditions as a design variable — the same tube can produce different pitches depending on how the ends are configured."

- question: "Why does a closed-open pipe produce only odd harmonics, and what is the physical reason no even harmonics can form?"
  type: short-answer
  answer: "A closed-open pipe requires a node at the closed end and an antinode at the open end. The simplest fitting pattern is one quarter-wavelength. The next allowed pattern requires three quarter-wavelengths, then five, then seven — always an odd number of quarter-wavelengths. An even number would put both ends in the same condition (both antinodes or both nodes), violating the boundary conditions. Since frequency is proportional to the number of quarter-wavelengths that fit, only odd multiples of the fundamental are supported."
  explanation: "The answer reveals that odd-harmonic production is not an arbitrary fact to memorize — it is the direct logical consequence of the boundary conditions. Once you know what each end must do, the allowed wavelengths follow automatically. This same reasoning applies to all resonance problems: identify the boundary conditions first, then derive the allowed modes."
```

## Explainer

From your study of standing waves, you know that a standing wave forms when two identical waves travel in opposite directions and interfere. The result is a pattern of fixed **nodes** (zero displacement) and **antinodes** (maximum displacement). What determines which standing waves can exist in a pipe is the **boundary condition** at each end — that is, what the wave must do at the wall or opening.

At an open end of a pipe, air is free to move, so the displacement must be maximum: an open end is always an **antinode**. At a closed end, the wall blocks air movement, so displacement must be zero: a closed end is always a **node**. These constraints act like requirements that the standing wave pattern must satisfy. Only wavelengths that fit these boundary conditions are allowed, and those correspond to the resonant frequencies.

For an open-open pipe, both ends are antinodes. The simplest pattern that satisfies this places half a wavelength across the full pipe length L, giving the fundamental frequency f₁ = v/(2L). You can fit any whole number of half-wavelengths: 1, 2, 3, … This means all harmonics are present: f_n = nv/(2L). For a closed-open pipe, one end is a node and the other an antinode. The simplest fitting pattern is a quarter-wavelength, giving f₁ = v/(4L). The next pattern requires three-quarter wavelengths, then five-quarter — only **odd multiples** fit. So closed pipes only produce odd harmonics: f_n = (2n-1)v/(4L).

The practical consequence is tonal color. A clarinet, which behaves acoustically like a closed-open pipe, produces only odd harmonics and has a characteristically hollow, woody sound. A flute, which is open-open, produces all harmonics and sounds brighter and fuller. Two pipes of the same length can sound very different because the set of harmonics they support — determined entirely by whether each end is open or closed — shapes the **timbre** of the resulting sound.


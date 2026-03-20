---
id: vibrating-air-column-modes
title: Resonance in Air Columns and Pipes
domain: physics
course: waves-and-optics
prerequisites:
- id: standing-waves
  type: hard
- id: acoustic-wave-speed-properties
  type: hard
tags:
- resonance
- acoustics
- pipes
stage: advanced
status: draft
---

# Resonance in Air Columns and Pipes

## Core Idea
A closed pipe (closed at both ends) resonates at f_n = nv/(2L). An open pipe (open at both ends) also resonates at f_n = nv/(2L). A pipe open at one end and closed at the other resonates at f_n = (2n-1)v/(4L), containing only odd harmonics. These differences arise from boundary conditions: closed ends require nodes (zero velocity), open ends require antinodes.

## Explainer

You already know from standing waves that resonance occurs when a wave reflects back on itself and the reflected wave reinforces the original — the two waves superpose constructively at every point. In a string, the fixed endpoints force displacement nodes there. In an air column, the physics is analogous but the boundary conditions differ depending on whether the end is open or closed.

At a **closed end**, air molecules cannot move — the wall stops them. This forces a **displacement node** (zero molecular motion) at that position. At an **open end**, air pressure must match the atmosphere outside, which means the pressure variation drops to zero there. Since pressure and displacement are 90° out of phase in a sound wave, zero pressure variation at an open end means maximum displacement — an **antinode**. These two boundary conditions are the only physics you need to derive all the resonance formulas.

For an **open-open pipe**, both ends require antinodes. The simplest standing wave pattern that satisfies this has antinodes at both ends with a node in the middle — that is exactly half a wavelength fitting in the pipe: L = λ/2, so λ = 2L. Higher harmonics fit additional half-wavelengths: L = nλ/2, giving f_n = nv/(2L) for all integers n = 1, 2, 3, … The full harmonic series is present. For a **closed-closed pipe**, both ends need nodes — the math works out identically and all harmonics are present.

For a **closed-open pipe** (like a clarinet), one end has a node and the other an antinode. The simplest pattern that satisfies this is a quarter wavelength: L = λ/4, so λ = 4L, and f₁ = v/(4L). The next pattern must have a node at the closed end and antinode at the open end with one more half-cycle in between — that requires L = 3λ/4, giving f = 3v/(4L). The pattern continues as L = (2n−1)λ/4, yielding only **odd harmonics**: f_n = (2n−1)v/(4L). This is why a clarinet (closed-open) sounds darker than a flute (open-open) at the same fundamental pitch — the clarinet's timbre lacks the even harmonics that would add brightness. The tube geometry is acoustic destiny: boundary conditions dictate the overtone spectrum, which dictates the instrument's voice.

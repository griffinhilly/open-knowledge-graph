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

## Questions

```yaml
- question: "A pipe of length L is open at one end and closed at the other (like a clarinet). Which harmonics are present in its resonant spectrum?"
  type: multiple-choice
  options:
    - "All integer harmonics: f_n = nv/(2L) for n = 1, 2, 3, ..."
    - "Only odd harmonics: f_n = (2n−1)v/(4L) for n = 1, 2, 3, ..."
    - "All integer harmonics, but starting at f = v/(4L) rather than v/(2L)"
    - "Only even harmonics, because the open-closed geometry requires an even number of quarter-wavelengths"
  answer: 1
  explanation: "A closed end requires a displacement node; an open end requires a displacement antinode. The simplest wave fitting these constraints is a quarter-wavelength (L = λ/4). The next requires L = 3λ/4, then L = 5λ/4 — only odd multiples of the quarter-wavelength fit. This yields f_n = (2n−1)v/(4L): only odd harmonics. This is the boundary-condition derivation of the formula — you don't need to memorize it if you understand why nodes occur at closed ends and antinodes at open ends."

- question: "At an open end of a pipe, what boundary condition applies and why?"
  type: multiple-choice
  options:
    - "Displacement node — air molecules must stop moving as they exit the pipe into open space"
    - "Pressure node (displacement antinode) — air pressure must equal atmospheric pressure at the opening, so pressure variation goes to zero"
    - "Pressure antinode (displacement node) — air compresses at the opening because of the sudden change in area"
    - "No boundary condition applies — open ends are physically unconstrained"
  answer: 1
  explanation: "At an open end, the air pressure must match the atmosphere outside, so the excess pressure (deviation from atmospheric) must be zero there — a pressure node. Since pressure variation and displacement variation are 90° out of phase in a longitudinal sound wave, a pressure node corresponds to maximum displacement — a displacement antinode. This is the physically correct boundary condition, and it is what distinguishes open-open pipes (antinodes at both ends, all harmonics present) from closed-open pipes (node at closed end, antinode at open end, only odd harmonics)."

- question: "A clarinet (effectively a closed-open pipe) playing the same fundamental frequency as a flute (effectively an open-open pipe) will have a different timbre because the clarinet's resonant spectrum lacks even harmonics."
  type: true-false
  answer: true
  explanation: "True. Both instruments can play the same fundamental pitch, but their overtone spectra differ. The flute (open-open) supports all harmonics (f, 2f, 3f, 4f, ...), adding brightness from even-numbered partials. The clarinet (closed-open) supports only odd harmonics (f, 3f, 5f, 7f, ...), giving it a darker, more hollow sound. This is a direct consequence of boundary conditions, not just tube length or mouthpiece design. The geometry of the air column is acoustic destiny."

- question: "A pipe closed at both ends supports the same resonant frequencies as a pipe open at both ends of the same length."
  type: true-false
  answer: true
  explanation: "True — and this surprises many students. A closed-closed pipe requires displacement nodes at both ends; an open-open pipe requires displacement antinodes at both ends. In both cases, the simplest mode fits one half-wavelength in the pipe (L = λ/2), and all integer multiples of the half-wavelength also fit. Both give f_n = nv/(2L) for all integers n = 1, 2, 3, ... The harmonic series is identical. The difference between open-open and closed-open (where one end has a node and the other has an antinode) is what breaks the symmetry and eliminates even harmonics."

- question: "Explain, starting from physical boundary conditions (not just formulas), why a closed-open pipe supports only odd harmonics while an open-open pipe of the same length supports all harmonics."
  type: short-answer
  answer: "Boundary conditions: a closed end requires a displacement node (molecules cannot move through the wall); an open end requires a displacement antinode (pressure there equals atmospheric, so pressure variation is zero, meaning displacement variation is maximum). For an open-open pipe, the simplest standing wave has antinodes at both ends, fitting one half-wavelength (L = λ/2). Higher modes fit 2, 3, 4, ... half-wavelengths: L = nλ/2, giving f_n = nv/(2L) — all integers present. For a closed-open pipe, the simplest wave has a node at one end and an antinode at the other. This requires L = λ/4. The next mode must again have node at closed, antinode at open — the next fitting pattern has L = 3λ/4, then 5λ/4. Only odd multiples of λ/4 fit: L = (2n−1)λ/4, giving f_n = (2n−1)v/(4L) — only odd harmonics. The missing even harmonics are not a mathematical accident but a direct geometric consequence of the mixed boundary conditions."
  explanation: "The key is that mixed boundary conditions (node on one side, antinode on the other) break the symmetry that allows half-integer as well as odd-quarter-integer wavelengths. With symmetric boundary conditions (node-node or antinode-antinode), the fitting condition gives all harmonics. With asymmetric boundary conditions (node-antinode), only odd harmonics fit. This is why the clarinet — a closed-open cylindrical tube — sounds darker and more 'reedy' than a flute of comparable length: the even harmonics that would add brightness are simply absent."
```

## Explainer

You already know from standing waves that resonance occurs when a wave reflects back on itself and the reflected wave reinforces the original — the two waves superpose constructively at every point. In a string, the fixed endpoints force displacement nodes there. In an air column, the physics is analogous but the boundary conditions differ depending on whether the end is open or closed.

At a **closed end**, air molecules cannot move — the wall stops them. This forces a **displacement node** (zero molecular motion) at that position. At an **open end**, air pressure must match the atmosphere outside, which means the pressure variation drops to zero there. Since pressure and displacement are 90° out of phase in a sound wave, zero pressure variation at an open end means maximum displacement — an **antinode**. These two boundary conditions are the only physics you need to derive all the resonance formulas.

For an **open-open pipe**, both ends require antinodes. The simplest standing wave pattern that satisfies this has antinodes at both ends with a node in the middle — that is exactly half a wavelength fitting in the pipe: L = λ/2, so λ = 2L. Higher harmonics fit additional half-wavelengths: L = nλ/2, giving f_n = nv/(2L) for all integers n = 1, 2, 3, … The full harmonic series is present. For a **closed-closed pipe**, both ends need nodes — the math works out identically and all harmonics are present.

For a **closed-open pipe** (like a clarinet), one end has a node and the other an antinode. The simplest pattern that satisfies this is a quarter wavelength: L = λ/4, so λ = 4L, and f₁ = v/(4L). The next pattern must have a node at the closed end and antinode at the open end with one more half-cycle in between — that requires L = 3λ/4, giving f = 3v/(4L). The pattern continues as L = (2n−1)λ/4, yielding only **odd harmonics**: f_n = (2n−1)v/(4L). This is why a clarinet (closed-open) sounds darker than a flute (open-open) at the same fundamental pitch — the clarinet's timbre lacks the even harmonics that would add brightness. The tube geometry is acoustic destiny: boundary conditions dictate the overtone spectrum, which dictates the instrument's voice.

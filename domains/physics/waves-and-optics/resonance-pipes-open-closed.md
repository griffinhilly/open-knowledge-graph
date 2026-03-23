---
id: resonance-pipes-open-closed
title: 'Resonance in Pipes: Open and Closed Ends'
domain: physics
course: waves-and-optics
prerequisites:
- id: standing-waves
  type: hard
- id: acoustic-resonance-pipes
  type: soft
builds-toward:
- fundamental-frequency-and-overtones
tags:
- resonance
- sound
- pipes
stage: advanced
status: validated
---

# Resonance in Pipes: Open and Closed Ends

## Core Idea
Open pipes (open at both ends) resonate at frequencies fₙ = nv/(2L) for all integers n ≥ 1. Closed pipes (closed at one end) resonate at frequencies fₙ = (2n-1)v/(4L) for n ≥ 1, producing only odd harmonics. Open ends correspond to pressure antinodes; closed ends to pressure nodes.

## Questions

```yaml
- question: "A student reasons: 'A closed end of a pipe is like a fixed end of a string — both prevent motion — so a closed pipe end should behave exactly like a fixed string end.' What is correct about this reasoning and what is importantly wrong?"
  type: multiple-choice
  options:
    - "The student is fully correct — both create displacement nodes and the acoustic behavior is identical"
    - "The student correctly identifies that a closed end creates a displacement node (air cannot move into a wall), but fails to note that in a pressure wave, a displacement node corresponds to a pressure *antinode*, not a pressure node — so the acoustic boundary condition is opposite in character to what students expect from strings"
    - "The student is incorrect — a closed end creates a displacement antinode because air pressure builds up at the wall"
    - "The analogy is entirely invalid because sound is longitudinal while string waves are transverse"
  answer: 1
  explanation: "The analogy is partially right: a closed end does create a displacement node, just as a fixed string end does. But the crucial difference is that in an air column, displacement and pressure are 90° out of phase — a displacement node is a pressure antinode, and vice versa. This is the opposite of what students intuitively expect. When air molecules are forced to stop moving at a wall (displacement node), the pressure variations pile up maximally there (pressure antinode). This reversal is what determines the allowed standing wave patterns and hence the harmonic series for closed vs. open pipes."

- question: "A pipe is 0.5 m long and closed at one end. Taking the speed of sound as 340 m/s, what is the second resonant frequency of this pipe?"
  type: multiple-choice
  options:
    - "170 Hz — the fundamental of the closed pipe, which is also its first (not second) resonance"
    - "510 Hz — closed pipes support only odd harmonics, so the second resonance is the third harmonic: f₃ = 3v/(4L) = 3×340/(4×0.5) = 510 Hz"
    - "680 Hz — twice the fundamental, as if the pipe had even harmonics like an open pipe"
    - "340 Hz — the fundamental of an open pipe of the same length"
  answer: 1
  explanation: "The fundamental of a closed pipe is f₁ = v/(4L) = 340/(4×0.5) = 170 Hz. Because closed pipes only support odd harmonics, there is no second harmonic — the next resonance is the third harmonic: f₃ = 3v/(4L) = 510 Hz. Option C (680 Hz = 2×170 Hz) represents the non-existent second harmonic; closed pipes skip all even harmonics. This is the key distinction from open pipes, which do support all harmonics (170 Hz, 340 Hz, 510 Hz, ...). A student who forgets that closed pipes have only odd harmonics will incorrectly guess 340 Hz or 680 Hz as the second resonance."

- question: "An open end of an air column is a point of maximum pressure variation — a pressure antinode."
  type: true-false
  answer: false
  explanation: "An open end is a pressure *node* — a point of minimum (zero) pressure variation. At an open end, the air pressure must match the surrounding atmospheric pressure, so the pressure cannot oscillate. It is instead a displacement *antinode*: air molecules are free to move in and out maximally. This reversal — open end = pressure node = displacement antinode; closed end = pressure antinode = displacement node — is the central conceptual fact about pipe resonance and is the opposite of what most students initially expect."

- question: "A clarinet and a flute of the same physical length will produce the same fundamental frequency."
  type: true-false
  answer: false
  explanation: "A clarinet behaves as a closed-open pipe (the reed seals one end, creating a pressure antinode there) and resonates with a fundamental frequency f₁ = v/(4L). A flute is open at both ends and resonates at f₁ = v/(2L). With the same length L, the flute's fundamental is exactly twice the clarinet's — an octave higher. This is why clarinets and flutes of the same length have different pitch ranges, and it is a direct consequence of the boundary conditions imposed by their playing mechanisms."

- question: "Why does a closed pipe produce only odd harmonics while an open pipe produces all harmonics? Ground your explanation in the boundary conditions at each end of the pipe."
  type: short-answer
  answer: "The allowed harmonics are determined by which standing wave patterns satisfy the boundary conditions at both ends simultaneously. For an open pipe (pressure nodes at both ends), we need an integer number of half-wavelengths to fit between the two nodes: L = nλ/2, giving fₙ = nv/(2L) for n = 1, 2, 3, ... — all harmonics. For a closed pipe (pressure antinode at the closed end, pressure node at the open end), we need a pressure antinode at one end and a node at the other. The simplest pattern fitting this requirement has a quarter-wavelength: L = λ/4, giving f₁ = v/(4L). The next pattern fitting both boundary conditions requires three-quarter wavelengths (antinode–node–antinode–node), giving f₃ = 3v/(4L). In general, only odd multiples fit: L = (2n−1)λ/4, so fₙ = (2n−1)v/(4L). Even harmonics require two pressure nodes or two pressure antinodes at the ends — incompatible with having one of each."
  explanation: "The key insight is that the closed end forces one particular boundary condition (pressure antinode) while the open end forces the other (pressure node). You can only fit standing wave patterns that honor both conditions simultaneously. The requirement of one antinode and one node at the two ends turns out to be satisfied only by odd multiples of the quarter-wavelength — geometrically, you can fit 1/4, 3/4, 5/4, ... wavelengths between the two ends, but not 2/4, 4/4, etc."
```

## Explainer

From standing waves, you know that a standing wave requires specific boundary conditions at each end of the medium. In a string, fixed ends create displacement nodes (the string cannot move there). In a pipe filled with air, the standing wave is a longitudinal pressure wave, and the boundary conditions follow a parallel but distinct logic. Mastering pipe resonance means mastering what boundary conditions apply at open versus closed ends — the formulas follow automatically.

The key rule is: a **closed end** creates a displacement node (air molecules cannot move into a wall) and equivalently a pressure antinode (pressure variation is maximum there). An **open end** creates a displacement antinode (air is free to move maximally) and a pressure node (pressure must match atmospheric at the opening, so the pressure variation is zero). Open end → pressure node. Closed end → pressure antinode. Once you have the boundary conditions at both ends, you fit half-wavelengths (or quarter-wavelengths) to satisfy them.

For an **open pipe**, both ends are pressure nodes. The simplest pattern requires one half-wavelength to span the pipe: λ₁/2 = L, giving λ₁ = 2L and f₁ = v/(2L). Each additional half-wavelength also fits (two nodes at the ends with any number of antinodes in between), giving fₙ = nv/(2L) for n = 1, 2, 3... All harmonics are present — the full series of multiples of the fundamental.

For a **closed pipe** (one end closed, one open), you need a pressure antinode at the closed end and a pressure node at the open end. The simplest pattern fitting this condition has a quarter-wavelength: λ₁/4 = L, giving f₁ = v/(4L). The next pattern that also satisfies both boundary conditions fits three-quarter wavelengths (one antinode at the closed end, then a node, another antinode, another node at the open end), giving f₃ = 3v/(4L). Only odd multiples of the quarter-wavelength fit — hence only odd harmonics: fₙ = (2n−1)v/(4L). The missing even harmonics explain why a **clarinet** (which behaves as a closed-open pipe because the reed seals one end) has a hollow, reedy timbre — its spectrum contains only odd harmonics 1, 3, 5... A **flute** (open at both ends) produces all harmonics and sounds richer. Two pipes of the same length produce fundamentals an octave apart: the open pipe's fundamental is twice the closed pipe's fundamental, because half the pipe length fits a half-wavelength instead of a quarter-wavelength.

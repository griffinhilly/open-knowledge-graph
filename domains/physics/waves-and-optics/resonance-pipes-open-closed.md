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
status: draft
---

# Resonance in Pipes: Open and Closed Ends

## Core Idea
Open pipes (open at both ends) resonate at frequencies fₙ = nv/(2L) for all integers n ≥ 1. Closed pipes (closed at one end) resonate at frequencies fₙ = (2n-1)v/(4L) for n ≥ 1, producing only odd harmonics. Open ends correspond to pressure antinodes; closed ends to pressure nodes.

## Explainer

From standing waves, you know that a standing wave requires specific boundary conditions at each end of the medium. In a string, fixed ends create displacement nodes (the string cannot move there). In a pipe filled with air, the standing wave is a longitudinal pressure wave, and the boundary conditions follow a parallel but distinct logic. Mastering pipe resonance means mastering what boundary conditions apply at open versus closed ends — the formulas follow automatically.

The key rule is: a **closed end** creates a displacement node (air molecules cannot move into a wall) and equivalently a pressure antinode (pressure variation is maximum there). An **open end** creates a displacement antinode (air is free to move maximally) and a pressure node (pressure must match atmospheric at the opening, so the pressure variation is zero). Open end → pressure node. Closed end → pressure antinode. Once you have the boundary conditions at both ends, you fit half-wavelengths (or quarter-wavelengths) to satisfy them.

For an **open pipe**, both ends are pressure nodes. The simplest pattern requires one half-wavelength to span the pipe: λ₁/2 = L, giving λ₁ = 2L and f₁ = v/(2L). Each additional half-wavelength also fits (two nodes at the ends with any number of antinodes in between), giving fₙ = nv/(2L) for n = 1, 2, 3... All harmonics are present — the full series of multiples of the fundamental.

For a **closed pipe** (one end closed, one open), you need a pressure antinode at the closed end and a pressure node at the open end. The simplest pattern fitting this condition has a quarter-wavelength: λ₁/4 = L, giving f₁ = v/(4L). The next pattern that also satisfies both boundary conditions fits three-quarter wavelengths (one antinode at the closed end, then a node, another antinode, another node at the open end), giving f₃ = 3v/(4L). Only odd multiples of the quarter-wavelength fit — hence only odd harmonics: fₙ = (2n−1)v/(4L). The missing even harmonics explain why a **clarinet** (which behaves as a closed-open pipe because the reed seals one end) has a hollow, reedy timbre — its spectrum contains only odd harmonics 1, 3, 5... A **flute** (open at both ends) produces all harmonics and sounds richer. Two pipes of the same length produce fundamentals an octave apart: the open pipe's fundamental is twice the closed pipe's fundamental, because half the pipe length fits a half-wavelength instead of a quarter-wavelength.

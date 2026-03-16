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
status: draft
---

# Acoustic Resonance in Pipes and Air Columns

## Core Idea
Pipes open at both ends resonate at f_n = nv/(2L), producing antinodes at both ends. Pipes closed at one end resonate at odd harmonics only: f_n = (2n-1)v/(4L), producing a node at the closed end and antinode at the open end. These boundary condition differences explain why closed pipes have a different tone quality despite having the same length as open pipes.

## Explainer

From your study of standing waves, you know that a standing wave forms when two identical waves travel in opposite directions and interfere. The result is a pattern of fixed **nodes** (zero displacement) and **antinodes** (maximum displacement). What determines which standing waves can exist in a pipe is the **boundary condition** at each end — that is, what the wave must do at the wall or opening.

At an open end of a pipe, air is free to move, so the displacement must be maximum: an open end is always an **antinode**. At a closed end, the wall blocks air movement, so displacement must be zero: a closed end is always a **node**. These constraints act like requirements that the standing wave pattern must satisfy. Only wavelengths that fit these boundary conditions are allowed, and those correspond to the resonant frequencies.

For an open-open pipe, both ends are antinodes. The simplest pattern that satisfies this places half a wavelength across the full pipe length L, giving the fundamental frequency f₁ = v/(2L). You can fit any whole number of half-wavelengths: 1, 2, 3, … This means all harmonics are present: f_n = nv/(2L). For a closed-open pipe, one end is a node and the other an antinode. The simplest fitting pattern is a quarter-wavelength, giving f₁ = v/(4L). The next pattern requires three-quarter wavelengths, then five-quarter — only **odd multiples** fit. So closed pipes only produce odd harmonics: f_n = (2n-1)v/(4L).

The practical consequence is tonal color. A clarinet, which behaves acoustically like a closed-open pipe, produces only odd harmonics and has a characteristically hollow, woody sound. A flute, which is open-open, produces all harmonics and sounds brighter and fuller. Two pipes of the same length can sound very different because the set of harmonics they support — determined entirely by whether each end is open or closed — shapes the **timbre** of the resulting sound.


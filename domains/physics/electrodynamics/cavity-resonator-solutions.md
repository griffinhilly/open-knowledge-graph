---
id: cavity-resonator-solutions
title: Electromagnetic Field Solutions in Cavities
domain: physics
course: electrodynamics
prerequisites:
- id: cavity-resonators
  type: hard
- id: rectangular-waveguide-propagation
  type: soft
builds-toward:
- cavity-resonator-quality-factor
tags:
- cavity-resonators
- resonant-modes
- standing-waves
stage: advanced
status: draft
---

# Electromagnetic Field Solutions in Cavities

## Core Idea
Cavity resonators confine standing wave patterns through metal boundaries. Resonant frequencies ωₙₘₚ are determined by boundary conditions; TMₙₘₚ modes have all three field components while TEₙₘₚ modes have zero Ez or Hz. Field patterns are spatial modes with time-harmonic oscillation.

## Questions

```yaml
- question: "A rectangular cavity has dimensions a × b × d. An engineer doubles the length d while keeping a and b fixed. What happens to the resonant frequencies?"
  type: multiple-choice
  options:
    - "All resonant frequencies are halved, since the cavity is twice as large"
    - "Resonant frequencies of modes with p ≠ 0 shift to lower values; modes with p = 0 are unaffected"
    - "All resonant frequencies are unchanged, since only a and b determine resonance"
    - "All resonant frequencies double, since the cavity's resonant condition scales with volume"
  answer: 1
  explanation: "The resonant frequency formula ωₙₘₚ = cπ√[(n/a)² + (m/b)² + (p/d)²] shows that doubling d replaces (p/d)² with (p/2d)², reducing the contribution of that term by a factor of 4. Modes with p = 0 have no dependence on d and are unaffected; modes with p ≠ 0 shift lower."

- question: "Why are resonant frequencies in a cavity discrete rather than forming a continuum?"
  type: multiple-choice
  options:
    - "Because TE and TM modes cannot coexist, limiting available frequencies"
    - "Because the boundary condition E_tan = 0 on all conducting walls requires integer numbers of half-wavelengths to fit along each dimension simultaneously"
    - "Because electromagnetic energy dissipates at non-resonant frequencies before establishing a standing wave"
    - "Because the cavity material has a discrete permittivity spectrum"
  answer: 1
  explanation: "Every conducting wall requires the tangential electric field to vanish. This forces an integer number of half-wavelengths to fit along each direction, just like a string fixed at both ends. Only specific frequency triplets (n, m, p) satisfy all six boundary conditions simultaneously — making the allowed frequencies a discrete set."

- question: "The dominant mode (lowest resonant frequency) of a rectangular cavity resonator is determined primarily by the cavity's largest dimension."
  type: true-false
  answer: true
  explanation: "ωₙₘₚ is minimized when the term under the square root is smallest. The largest dimension contributes the smallest (p/L)² term, so the mode that places one half-wavelength along the longest axis is the lowest-frequency resonant mode."

- question: "A TE mode in a cavity resonator has no magnetic field component along the propagation axis."
  type: true-false
  answer: false
  explanation: "It is the ELECTRIC field that has no component along the propagation axis in a TE (transverse electric) mode — Hz ≠ 0 but Ez = 0. TM (transverse magnetic) modes have no magnetic field component along the propagation axis. Confusing the two is a very common error."

- question: "Explain why sealing both ends of a waveguide to form a cavity produces discrete resonant frequencies, using an analogy with a vibrating string."
  type: short-answer
  answer: "A string fixed at both ends can only sustain standing waves where an integer number of half-wavelengths fit between the endpoints; other frequencies produce destructive interference and die out. A closed cavity is the 3D electromagnetic analog: sealing the ends forces the field to reflect and interfere. Constructive standing waves exist only when integer half-wavelengths fit along all three dimensions simultaneously, selecting a discrete set of resonant frequencies."
  explanation: "The key insight is that boundary conditions at the ends impose a quantization condition. In both the string and the cavity, the discreteness arises from the requirement that the wave 'fit' in the confined space with nodes at every boundary — a count of half-wavelengths."
```

## Explainer

A waveguide is an open channel — fields travel down it indefinitely. A **cavity resonator** is a waveguide sealed at both ends, creating a metal box. When you close the ends, the forward-traveling and backward-traveling waves reflect back and forth and interfere. At most frequencies this interference is destructive and the field quickly dies out. But at specific frequencies the reflections reinforce constructively, creating a stable **standing wave** pattern. These are the resonant modes of the cavity — the electromagnetic analog of the harmonics of a vibrating string.

For a rectangular cavity of dimensions a × b × d, the resonant frequencies take the form ωₙₘₚ = c·π√[(n/a)² + (m/b)² + (p/d)²]. Each triplet of integers (n, m, p) labels a distinct mode, and each mode has its own spatial field pattern. The integers count half-wavelengths that fit along each dimension — exactly the same standing-wave quantization you know from a vibrating string fixed at both ends. The lowest resonant frequency (dominant mode) is set by the largest dimension of the cavity.

The **TM** and **TE** mode classification that applied to waveguides extends naturally to cavities. **TE modes** (transverse electric) have no electric field component along the propagation axis; **TM modes** (transverse magnetic) have no magnetic field component along that axis. In a closed cavity, all three spatial directions must satisfy boundary conditions simultaneously — the tangential E-field must vanish at every conductor wall. This constraint is why the resonant frequencies are discrete: only field patterns that simultaneously satisfy E_tan = 0 on all six walls can exist as standing modes.

The physical importance of cavities is that they store electromagnetic energy at a precise frequency with very low loss. A microwave oven cavity confines energy to heat food; a microwave cavity in a particle accelerator stores energy to kick particles to higher speed; an atomic clock uses a cavity to define a precise frequency reference. In each case the cavity's geometry determines which frequencies are resonant, and the quality of the conducting walls determines how well energy is retained between driving cycles — a quantity captured by the cavity Q-factor, which you'll study next.

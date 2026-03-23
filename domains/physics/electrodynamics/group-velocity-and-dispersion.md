---
id: group-velocity-and-dispersion
title: Group Velocity and Dispersion Relations
domain: physics
course: electrodynamics
prerequisites:
- id: dispersion-relations-em-waves
  type: hard
- id: electromagnetic-waves
  type: hard
builds-toward:
- evanescent-waves-total-reflection
tags:
- group-velocity
- phase-velocity
- dispersion
- wave-packets
stage: expert
status: validated
---

# Group Velocity and Dispersion Relations

## Core Idea
The group velocity vg = dω/dk describes wave packet motion while phase velocity vp = ω/k describes individual wavefront motion. Dispersion (vg ≠ vp) causes wave packets to spread. When dω/dk is imaginary, waves are evanescent rather than propagating.

## Questions

```yaml
- question: "A radar pulse travels through a dispersive medium. An observer notices that the individual wave crests inside the pulse appear to move faster than the pulse envelope as a whole. This means:"
  type: multiple-choice
  options:
    - "There is a measurement error — wave crests must travel at the same speed as the envelope"
    - "The phase velocity exceeds the group velocity in this medium"
    - "The group velocity exceeds the phase velocity in this medium"
    - "The medium is non-dispersive, and the two velocities are equal"
  answer: 1
  explanation: "The crests (individual wavefronts) move at the phase velocity vₚ = ω/k; the envelope (the pulse as a whole) moves at the group velocity vg = dω/dk. When crests visibly slide through the envelope — moving faster than the bump — this means vₚ > vg. This is common in water waves, where ripples (phase) travel faster than the wave group (envelope). It is not an error; it is the expected behavior in a dispersive medium where vg ≠ vₚ."

- question: "A narrow pulse of light travels through a long optical fiber. After propagating a great distance, the pulse has broadened significantly. The primary cause is:"
  type: multiple-choice
  options:
    - "Energy absorption at the fiber walls gradually removes the pulse's outer frequencies"
    - "The pulse contains multiple frequency components that travel at slightly different phase velocities, causing them to drift apart over time"
    - "Group velocity is zero in dispersive media, so pulses inevitably stop"
    - "Diffraction causes the pulse to spread transversely, reducing its longitudinal coherence"
  answer: 1
  explanation: "Pulse spreading (group velocity dispersion) occurs because a real pulse is a superposition of many frequency components, not a single sinusoid. In a dispersive medium, different frequencies have different phase velocities, so they drift apart over time — the high-frequency components arrive at a different time than the low-frequency ones. This is the fundamental limit on data rates in fiber-optic communications: if pulses spread into each other, adjacent bits become indistinguishable."

- question: "In a non-dispersive medium, the group velocity and phase velocity are equal, and a wave packet travels without spreading."
  type: true-false
  answer: true
  explanation: "A non-dispersive medium has a linear dispersion relation ω = ck, so vₚ = ω/k = c and vg = dω/dk = c — they are equal. All frequency components travel at the same speed, so a superposition of frequencies (a wave packet) maintains its shape indefinitely. Vacuum is non-dispersive for electromagnetic waves: any pulse shape travels at c without distortion. Dispersion requires the dispersion relation to be nonlinear."

- question: "The phase velocity of a wave describes how quickly a wave packet (like a signal or pulse) travels through a medium."
  type: true-false
  answer: false
  explanation: "The group velocity, not the phase velocity, describes the motion of a wave packet or pulse. The phase velocity describes the motion of individual wave crests — the speed at which surfaces of constant phase move. These can differ significantly in dispersive media, and in some media the phase velocity can even exceed c without violating relativity, because phase carries no information. Energy and information travel at the group velocity (in normal dispersion), which is why it is physically the more important quantity."

- question: "Explain why wave packets spread as they propagate through a dispersive medium, using the concepts of phase velocity and group velocity."
  type: short-answer
  answer: "A wave packet is built from a superposition of sinusoidal components with different frequencies. In a dispersive medium, different frequencies travel at different phase velocities (because ω/k varies with k). This means the various frequency components that make up the packet drift apart as they propagate — faster components run ahead while slower ones fall behind. The group velocity dω/dk gives the speed of the peak of the packet, but because dω/dk itself varies across the packet's frequency range, the packet broadens over time. The rate of spreading is governed by d²ω/dk² (group velocity dispersion): larger dispersion means faster broadening."
  explanation: "The contrast with a non-dispersive medium makes this concrete: in vacuum (ω = ck), all components travel at exactly c regardless of frequency, so the packet shape is preserved. Any deviation from linearity in ω(k) introduces spreading."
```

## Explainer

From your study of electromagnetic waves and dispersion relations, you know that a medium's dispersion relation ω(k) connects a wave's frequency to its wavenumber. For light in vacuum, ω = ck — a perfectly linear relationship — so all frequencies travel at the same speed c. But in any real medium, the relationship is more complicated, and different frequency components travel at different speeds. This **dispersion** is what a prism exploits: red and violet light travel at slightly different speeds in glass, bending by different angles and separating into a rainbow.

The two velocity concepts arise naturally when you think about a **wave packet** — a spatially localized group of waves, like a radar pulse or a light pulse in a fiber. Such a packet is built by superposing many sinusoidal waves with slightly different frequencies and wavenumbers. Two superposed waves of nearly equal frequency ω₁, ω₂ and wavenumber k₁, k₂ produce a beat pattern: a fast carrier oscillation modulated by a slow envelope. The carrier travels at the **phase velocity** vₚ = ω/k, which describes how quickly the individual wave crests move. The envelope — the actual "bump" of the pulse, the part carrying the energy and information — travels at the **group velocity** vg = dω/dk, the slope of the dispersion curve. In a non-dispersive medium like vacuum, vg = vₚ = c; in a dispersive medium, they differ.

Dispersion causes two distinct effects. First, if vg ≠ vₚ, the carrier oscillations slide through the envelope as the packet travels — the "wiggles" move at a different speed than the "bump." This is observable in water waves, where ripples travel faster than the wave group. Second, and more practically important, **pulse spreading** occurs: different frequency components of the packet travel at slightly different speeds, so they drift apart over time and the pulse broadens. This limits data rates in fiber-optic cables, since overlapping pulses become indistinguishable — the fundamental reason why fiber dispersion must be carefully managed in long-haul communications.

**Evanescent waves** arise when the dispersion relation yields an imaginary wavenumber k at a given frequency — meaning the wave cannot propagate and instead decays exponentially. This happens below the cutoff frequency of a waveguide: the mode mathematically "exists" but its amplitude dies away within a skin depth rather than oscillating. The group velocity formula dω/dk becomes imaginary, signaling no energy transport. This is physically consistent: no propagating mode means no energy flow. Understanding evanescent waves is essential for analyzing total internal reflection, waveguide cutoff, and quantum mechanical tunneling, where the same exponentially-decaying solution appears in classically forbidden regions.

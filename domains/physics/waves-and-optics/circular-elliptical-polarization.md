---
id: circular-elliptical-polarization
title: 'Polarization States: Linear, Circular, and Elliptical'
domain: physics
course: waves-and-optics
prerequisites:
- id: electromagnetic-wave-polarization
  type: soft
- id: phase-of-oscillation-initial
  type: hard
tags:
- polarization
- waves
stage: advanced
status: draft
---

# Polarization States: Linear, Circular, and Elliptical

## Core Idea
Polarization describes the orientation of the electric field oscillation. Linear polarization confines the field to a single direction. Circular polarization occurs when two perpendicular components have equal amplitude and 90° phase difference; the field vector rotates as the wave travels. Elliptical polarization is the general case with unequal amplitudes or non-90° phase differences. Malus's law governs transmission through polarizers.

## Questions

```yaml
- question: "Two perpendicular electric field components of equal amplitude are combined with a phase difference of 45°. What polarization state results?"
  type: multiple-choice
  options:
    - "Circular polarization — equal amplitudes are the only requirement for circular polarization"
    - "Linear polarization — the phase difference shifts the oscillation direction but keeps it fixed"
    - "Elliptical polarization — both equal amplitudes AND a 90° phase difference are required for circular; 45° produces an ellipse"
    - "Unpolarized light — phase differences between components randomize the polarization"
  answer: 2
  explanation: "Circular polarization requires two simultaneous conditions: equal amplitudes AND exactly 90° phase difference. If either condition fails, the E-field tip traces an ellipse instead of a circle. With equal amplitudes and a 45° phase difference, the path is an ellipse — not a circle. The most common misconception is remembering 'equal amplitudes' while forgetting the equally critical 90° phase requirement."

- question: "Linearly polarized light of intensity I₀ passes through a polarizer whose transmission axis is at 60° to the polarization direction. What intensity emerges?"
  type: multiple-choice
  options:
    - "I₀/2 — because only the cosine component of the electric field is transmitted"
    - "I₀ cos(60°) = I₀/2"
    - "I₀ cos²(60°) = I₀/4"
    - "0 — because 60° is too close to the crossed-polarizer condition"
  answer: 2
  explanation: "Malus's law states I = I₀cos²θ. At θ = 60°, cos(60°) = 1/2, so cos²(60°) = 1/4, giving I = I₀/4. The cos²θ factor arises because intensity is proportional to amplitude squared: the polarizer transmits the E-field component along its axis (amplitude reduced by cosθ), and since intensity ∝ E², the result is cos²θ. The answer I₀/2 is the classic error from forgetting to square the cosine."

- question: "Linear polarization and circular polarization are both limiting cases of elliptical polarization."
  type: true-false
  answer: true
  explanation: "Elliptical polarization is the general case for the superposition of two perpendicular components with any amplitudes and any phase difference. When the phase difference is 0° or 180° and amplitudes are arbitrary, the ellipse degenerates to a line — linear polarization. When amplitudes are equal and phase difference is exactly 90°, the ellipse becomes a perfect circle — circular polarization. All three are described by the same framework; linear and circular are special limiting cases."

- question: "Circularly polarized light can be produced from a single linearly polarized beam by introducing a 90° phase shift to that beam."
  type: true-false
  answer: false
  explanation: "Circular polarization requires two perpendicular components. A single linearly polarized beam has one field component; adding a phase shift to a single component just shifts its phase — you still have one component oscillating in one direction, which remains linear polarization. To produce circular polarization, the beam must first be decomposed into two perpendicular components (by a quarter-wave plate oriented at 45°), and those two components must be given a 90° phase difference with equal amplitudes."

- question: "What two conditions must both be satisfied for light to be circularly polarized rather than elliptically polarized, and what happens when only one condition is met?"
  type: short-answer
  answer: "Circular polarization requires: (1) the two perpendicular E-field components must have equal amplitudes, and (2) they must have exactly 90° phase difference. If only condition (1) is met — equal amplitudes but phase difference not 90° — the E-field tip traces an ellipse with the phase offset distorting the circle. If only condition (2) is met — 90° phase difference but unequal amplitudes — the tip again traces an ellipse, elongated along the axis of the larger component. Both conditions together give uniform rotation at constant radius: a circle."
  explanation: "The intuition: circular polarization means the E-field vector rotates at constant angular velocity with constant magnitude — like a vector of fixed length spinning steadily. Unequal amplitudes make the magnitude vary as it rotates (ellipse). A non-90° phase difference makes the rotation uneven in angle (also an ellipse). Both constraints together — equal amplitudes, 90° phase — enforce uniform rotation."
```

## Explainer

Think of a transverse wave as a rope being shaken — the rope can oscillate up-down, left-right, or anywhere in between. Light is an electromagnetic wave with an oscillating electric field, and **polarization** describes the direction that field oscillates as the wave travels. When you already understand phase of oscillation, you have the key tool for distinguishing all three polarization states: what makes them different is the phase relationship and amplitude balance between two perpendicular field components.

**Linear polarization** is the simplest case: the electric field oscillates along a single fixed direction — say, always vertical. Mathematically, this is one non-zero field component and zero in the perpendicular direction. A polarizing filter produces this by blocking all field orientations except one, transmitting only the component aligned with the filter's **transmission axis**. When unpolarized light (with electric field pointing in all transverse directions randomly) hits a polarizer, roughly half the intensity passes through — the half that happened to be aligned.

**Circular polarization** arises when you combine two perpendicular components of *equal amplitude* and exactly 90° phase difference. Imagine a vertical component E_y = A sin(kx - ωt) and a horizontal component E_z = A sin(kx - ωt + 90°) = A cos(kx - ωt). At any instant, the combined tip of the electric field vector traces a circle as the wave travels forward — the field doesn't flicker back and forth, it spins. The sign of the phase shift determines whether it's left-handed or right-handed circular polarization, a distinction that matters in optics and chemistry alike.

**Elliptical polarization** is the general case. When the two perpendicular components have *unequal* amplitudes, or a phase difference that isn't exactly 90°, the field vector traces an ellipse rather than a perfect circle or a line. Linear and circular polarization are limiting cases: a degenerate ellipse (flat line) and a perfectly round ellipse respectively. Most light emerging from crystals or optical waveplates is elliptically polarized.

**Malus's law** governs what happens when linearly polarized light passes through a second polarizer tilted at angle θ to the polarization direction: I = I₀cos²θ. At θ = 0° all intensity passes; at θ = 90° (crossed polarizers) none does. This squared cosine comes directly from the projection of the electric field vector onto the polarizer axis — intensity is proportional to amplitude squared, and the projected amplitude is the full amplitude times cos θ.

---
id: electromagnetic-wave-polarization
title: Polarization of Electromagnetic Waves
domain: physics
course: electrodynamics
prerequisites:
- id: plane-electromagnetic-waves
  type: hard
builds-toward:
- electromagnetic-waves-in-dielectrics
tags:
- polarization
- wave-properties
- em-waves
stage: expert
status: validated
---

# Polarization of Electromagnetic Waves

## Core Idea
The polarization of an electromagnetic wave describes how the electric field vector varies in direction as the wave propagates. Waves can be linearly polarized (E oscillates along a fixed direction), circularly polarized (E traces a helix), or elliptically polarized. Polarization is determined by the superposition of orthogonal field components and is crucial for understanding light-matter interactions and optical devices.

## Questions

```yaml
- question: "Two ideal linear polarizers are oriented with their transmission axes crossed at 90°, blocking nearly all light. A third polarizer is inserted between them at 45° to each. What happens?"
  type: multiple-choice
  options:
    - "No light passes — two crossed polarizers block all light regardless of what is inserted between them"
    - "Some light passes — the middle polarizer projects the first polarizer's output onto its own axis and rotates the polarization, allowing the final polarizer to transmit a fraction"
    - "All the original intensity is restored, since the middle polarizer cancels the effect of the outer two"
    - "Light is blocked more effectively because three filters are more absorbing than two"
  answer: 1
  explanation: "After the first polarizer, light is linearly polarized. The middle polarizer at 45° transmits cos²(45°) = ½ of that intensity and rotates the polarization to 45°. The final polarizer is now only 45° from the incoming polarization and transmits another cos²(45°) = ½, giving total transmission of ¼ of I₀/2 = I₀/8. Option (a) is the key misconception — crossed polarizers block light only when light arrives already polarized along one axis. Inserting a polarizer at 45° breaks this by rotating the polarization state at each step."

- question: "What two conditions are required to produce circularly polarized light by superimposing two orthogonally polarized waves?"
  type: multiple-choice
  options:
    - "Equal amplitudes and a frequency difference of exactly ω/2"
    - "Equal amplitudes and a phase difference of exactly 90°"
    - "Unequal amplitudes and a phase difference of 90°"
    - "Equal amplitudes traveling in opposite directions along the propagation axis"
  answer: 1
  explanation: "Circular polarization requires (1) equal amplitudes in the two orthogonal components and (2) a 90° phase difference. If the amplitudes are unequal, the tip of E⃗ traces an ellipse, not a circle. If the phase difference is not 90°, the result is also elliptical. Elliptical polarization is the general case; circular and linear are special limits. Option (d) confuses polarization with standing waves."

- question: "Elliptical polarization is the most general polarization state — both linear and circular polarization are special limiting cases of elliptical polarization."
  type: true-false
  answer: true
  explanation: "Any polarization state can be described as the superposition of two orthogonal linearly polarized components with some amplitude ratio and phase difference. When the amplitudes are equal and the phase difference is 90°, the ellipse becomes a circle (circular polarization). When the phase difference is 0° or 180°, the ellipse collapses to a line (linear polarization). All other combinations produce an ellipse, making elliptical polarization the general form."

- question: "Unpolarized light, such as sunlight, has its electric field oscillating in all directions, including along the direction of propagation."
  type: true-false
  answer: false
  explanation: "Electromagnetic waves are transverse — the electric field E⃗ is always confined to the plane perpendicular to the direction of propagation. Unpolarized light does not oscillate along the propagation direction; rather, its polarization direction varies randomly and rapidly within the transverse plane. A longitudinal electric field component would violate Maxwell's equations for EM waves in vacuum."

- question: "Why can electromagnetic waves be polarized but sound waves cannot?"
  type: short-answer
  answer: "Sound waves are longitudinal — particle displacement is parallel to the direction of propagation. There is only one direction of displacement, so there is no transverse degree of freedom to describe. Electromagnetic waves are transverse — the electric field vector lies in the plane perpendicular to propagation. Within that plane, E⃗ can point in any direction or rotate, giving rise to different polarization states. Polarization is a property of transverse waves only."
  explanation: "This distinction has practical consequences: polarizers work by selecting one orientation of the electric field. No equivalent device exists for sound because sound has no transverse degree of freedom to select. Understanding why polarization exists requires recognizing that 'transverse' means there are two independent directions in the plane perpendicular to propagation, and polarization describes how the wave distributes energy between them."
```

## Explainer

From your study of plane electromagnetic waves, you know that E⃗ and B⃗ are perpendicular to each other and to the direction of propagation. If the wave travels in the z-direction, E⃗ must lie in the xy-plane. But within that plane, E⃗ can point in any direction — and **polarization** describes exactly how that direction varies as the wave propagates or as time passes. It is a degree of freedom that has no analog in, say, sound waves (which are longitudinal), and it turns out to be physically consequential for reflection, absorption, and how light interacts with anisotropic materials.

The simplest case is **linear polarization**: the electric field oscillates back and forth along a single fixed direction in the xy-plane. For example, E⃗(z,t) = E₀ cos(kz - ωt) x̂. The field is always along x̂, just oscillating in magnitude. Sunlight reflected at a shallow angle off water or glass tends to be predominantly horizontally polarized, which is why polarized sunglasses (which block horizontal polarization) reduce glare. A linear polarizer transmits only the component of E along its transmission axis, so the transmitted intensity follows Malus's law: I = I₀ cos²θ, where θ is the angle between the incoming polarization and the polarizer axis.

Now consider superimposing two orthogonal linearly polarized waves with equal amplitude but a phase difference of 90°: E⃗ = E₀ cos(kz - ωt) x̂ + E₀ sin(kz - ωt) ŷ. At any fixed z, the tip of E⃗ traces a circle as time progresses — this is **circular polarization**. Left and right circular polarization differ only in the sign of the phase difference (±90°). If the two amplitudes are unequal, or if the phase difference is anything other than 90°, the tip traces an ellipse: **elliptical polarization** is the general case, with linear and circular polarization as special limits. This decomposition — any polarization state as a superposition of two orthogonal components — is fundamental, and it has a direct quantum-mechanical analog in photon spin states.

**Unpolarized light**, such as that from the sun or an incandescent bulb, has E⃗ oriented randomly and rapidly in all directions within the plane perpendicular to propagation — the polarization state changes on a timescale faster than any detector can resolve. A single polarizer transmits half of unpolarized light (on average) and fully polarizes it. Two crossed polarizers (with transmission axes at 90°) transmit essentially nothing — but inserting a third polarizer at 45° between them allows some light through again, because each polarizer projects onto its axis and rotates the polarization state. Polarization is not just an abstract property; it underlies LCD screens, optical fiber communication, spectroscopy of chiral molecules, and the operation of wave plates and beam splitters.

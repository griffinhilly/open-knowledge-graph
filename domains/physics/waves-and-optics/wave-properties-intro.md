---
id: wave-properties-intro
title: 'Wave Properties: Wavelength, Frequency, and Amplitude'
domain: physics
course: waves-and-optics
prerequisites:
- id: simple-harmonic-motion
  type: hard
- id: amplitude-period-phase-shift
  type: soft
- id: graphing-sine-and-cosine
  type: soft
- id: graphing-sine-and-cosine
  type: soft
- id: transverse-wave-characteristics
  type: soft
builds-toward:
- wave-speed-medium
- transverse-and-longitudinal-waves
- wave-superposition
tags:
- waves
- wavelength
- frequency
- amplitude
- period
stage: formal-systems
status: validated
---
# Wave Properties: Wavelength, Frequency, and Amplitude

## Core Idea
A wave is a disturbance that transfers energy through a medium or space without transferring matter. The key descriptors are wavelength (λ, distance between crests), frequency (f, cycles per second in Hz), amplitude (peak displacement from equilibrium), and period (T = 1/f). These are related by the universal wave equation v = fλ, where v is the wave's propagation speed.

## How It's Best Learned
Start with a demonstration of a rope or slinky to build physical intuition before applying the math. Practice converting between period and frequency and computing wave speed from f and λ. Graph sinusoidal waves and identify each quantity geometrically.

## Common Misconceptions
- Amplitude and wavelength are often confused; amplitude is the height of the wave, wavelength is the horizontal distance between repeating features.
- Students confuse period (in seconds) with frequency (in Hz); they are reciprocals, not equals.
- Waves carry energy, not matter — the medium returns to equilibrium after the wave passes.

## Questions

```yaml
- question: "A wave has a period of T = 0.02 s. What is its frequency?"
  type: multiple-choice
  options: ["0.02 Hz", "2 Hz", "50 Hz", "500 Hz"]
  answer: 2
  explanation: "Frequency and period are reciprocals: f = 1/T = 1/0.02 = 50 Hz. A common error is treating period and frequency as equal or confusing the units. Period is in seconds; frequency is in cycles per second (Hz)."

- question: "When an ocean wave passes through water, the water molecules travel horizontally along with the wave from one place to another."
  type: true-false
  answer: false
  explanation: "Waves transfer energy, not matter. Water molecules move in roughly circular orbits as a wave passes but return to their original positions afterward. It is the disturbance — not the medium — that travels."

- question: "A wave travels faster through steel than through air. If the frequency of the wave stays the same when it crosses from air into steel, what happens to its wavelength?"
  type: short-answer
  answer: "The wavelength increases. Since v = fλ and f is constant, a higher wave speed means a proportionally longer wavelength."
  explanation: "The wave equation v = fλ shows that speed, frequency, and wavelength are linked. Frequency is set by the source and doesn't change at a boundary. Speed changes with the medium, so wavelength must adjust accordingly."
```

## Explainer

Wave properties build directly on what you learned from simple harmonic motion (SHM). In SHM, a single object oscillates back and forth around an equilibrium position — think of a mass on a spring. A wave is what happens when that oscillation propagates through space: each part of the medium repeats the same oscillation, but slightly delayed relative to its neighbor. The result is a traveling disturbance that carries energy without carrying matter.

The **amplitude** is the maximum displacement from equilibrium — how far the medium is pushed at its most extreme. A larger amplitude means more energy in the wave (sound waves with high amplitude are louder; water waves with high amplitude are taller). The **period** (T) is how long one complete oscillation takes, and **frequency** (f) is how many complete oscillations occur per second. These are reciprocals: f = 1/T. If a wave completes one cycle every 0.01 seconds, its frequency is 100 Hz.

The **wavelength** (λ) is a spatial measure — the distance between two identical, adjacent points on the wave, such as crest to crest or trough to trough. While period and frequency describe time, wavelength describes space. Don't confuse them: amplitude is the *height* of the wave (vertical), wavelength is the *length* of one cycle (horizontal).

These quantities connect through the **universal wave equation**: v = fλ. The speed of a wave through a given medium is fixed by that medium's properties — you cannot change it by adjusting the source. But you can change frequency (by adjusting the source) or wavelength (which then adjusts automatically). If you double the frequency of a wave in the same medium, the wavelength halves to keep the speed constant.

A useful mental image: imagine snapping a rope at different rates. Snap slowly (low frequency) and you get long, lazy waves (large wavelength). Snap quickly (high frequency) and you get short, rapid waves (small wavelength). The speed at which the disturbance travels down the rope doesn't change based on how fast you snap — that's governed by the rope's tension and mass per unit length, not you.

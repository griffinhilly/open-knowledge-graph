---
id: acoustic-pressure-and-amplitude
title: Acoustic Pressure and Amplitude in Sound Waves
domain: physics
course: waves-and-optics
prerequisites:
- id: sound-waves-intro
  type: hard
- id: pressure
  type: soft
builds-toward:
- sound-intensity-and-decibels
tags:
- sound
- pressure
- amplitude
stage: formal-systems
status: validated
---

# Acoustic Pressure and Amplitude in Sound Waves

## Core Idea
Sound waves create oscillating pressure variations in the medium: P = Pamplitude × sin(kx - ωt). Acoustic pressure amplitude is related to particle velocity amplitude by P = ρvvₚ. Higher pressure amplitudes correspond to louder sounds and higher acoustic intensity.

## Questions

```yaml
- question: "A sound engineer doubles the pressure amplitude of a speaker output. What happens to the acoustic intensity?"
  type: multiple-choice
  options:
    - "It doubles — intensity is proportional to pressure amplitude"
    - "It quadruples — intensity is proportional to the square of pressure amplitude"
    - "It increases by √2 — intensity scales with the RMS pressure"
    - "It stays the same — intensity depends on frequency, not amplitude"
  answer: 1
  explanation: "Acoustic intensity is proportional to the square of pressure amplitude: I ∝ P_amplitude². Doubling the amplitude multiplies the intensity by 2² = 4. This squared relationship is the same as for all wave types — the 'double amplitude, quadruple intensity' rule — and is precisely why the decibel scale is logarithmic: the ear handles an enormous range of intensities."

- question: "Acoustic impedance (ρv_sound) links pressure amplitude to particle velocity amplitude. What does a high acoustic impedance mean physically?"
  type: multiple-choice
  options:
    - "Sound travels faster in that medium, so particles vibrate at higher frequency"
    - "A large pressure swing is required to drive a given particle velocity in that medium"
    - "The medium absorbs more sound energy, reducing amplitude over distance"
    - "The medium has lower density, so particles respond more strongly to pressure"
  answer: 1
  explanation: "The relation P_amplitude = ρ × v_sound × v_p shows that high acoustic impedance (large ρv_sound) means more pressure is needed to achieve the same particle velocity — analogous to high electrical resistance requiring more voltage to drive the same current. This is why sound transmits poorly from air (low impedance) into water (high impedance): the mismatch at the boundary causes most energy to be reflected."

- question: "Acoustic pressure at a point in a medium equals the total air pressure at that point."
  type: true-false
  answer: false
  explanation: "Acoustic pressure is the *deviation* from the undisturbed ambient pressure — not the total pressure. As a wave passes, the local pressure oscillates above and below atmospheric pressure (~101,325 Pa), and the acoustic pressure captures only this oscillating departure. A loud sound might have a pressure amplitude of a few pascals; a whisper around 0.02 Pa. These are tiny fractions of total air pressure, which is why sound barely disturbs the medium even at high volumes."

- question: "Doubling the pressure amplitude of a sound wave quadruples its acoustic intensity."
  type: true-false
  answer: true
  explanation: "True. The quadratic relationship I ∝ P_amplitude² is fundamental and applies to all wave types. This squared proportionality arises because intensity measures power per unit area — power goes as the square of the driving amplitude. The same relationship exists for water waves, electromagnetic waves, and strings: to transfer four times the energy, you need twice the amplitude."

- question: "Why can the human ear detect pressure amplitudes as small as 0.00002 Pa, even though atmospheric pressure is roughly 101,325 Pa?"
  type: short-answer
  answer: "The ear responds to changes in pressure (acoustic pressure), not to the absolute ambient pressure. Even though the ambient pressure is huge, the oscillating departures from that baseline — the acoustic pressure — are what the ear's hair cells detect. The auditory system is exquisitely tuned to measure differential pressure across the eardrum, which amplifies tiny vibrations mechanically before they reach the cochlea."
  explanation: "This is a conceptual shift from thinking about total pressure to pressure variation. The ear evolved to detect predators and communication signals, which involve tiny, rapid pressure fluctuations. The mechanism (tympanic membrane deflection → ossicle amplification → cochlear fluid motion → hair cell bending) extracts enormous sensitivity from very small pressure differences, not from the ambient pressure itself."
```

## Explainer

You already know from sound-waves-intro that sound is a longitudinal wave — particles in the medium being pushed together (compressions) and pulled apart (rarefactions) as the wave passes. The next step is to describe these disturbances quantitatively. The key quantity is **acoustic pressure**: the difference between the local pressure at a point in the medium and the undisturbed ambient pressure. As the wave passes, each point oscillates between positive acoustic pressure (compression) and negative acoustic pressure (rarefaction). This oscillation follows the same sinusoidal form as any wave: P(x,t) = P_amplitude × sin(kx − ωt).

The **pressure amplitude** P_amplitude is the peak value of that departure from ambient. A whisper produces a pressure amplitude of roughly 0.02 Pa — a tiny fraction of atmospheric pressure (101,325 Pa), yet easily detected by the ear. A jet engine at close range produces roughly 200 Pa. These numbers make clear that we are dealing with extremely small pressure variations relative to background, which is why the ear evolved such extraordinary sensitivity to detect them.

There is a deep physical link between acoustic pressure and particle motion. When a compression arrives, the particles are not only squeezed together — they are also moving, rushing toward the region of high pressure. The pressure amplitude and the **particle velocity amplitude** v_p are proportional through the medium's properties: P_amplitude = ρ × v_sound × v_p, where ρ is the medium's density and v_sound is the wave speed. The product ρv_sound is called the **acoustic impedance** of the medium. A high acoustic impedance means a large pressure swing is required to drive a given particle velocity — just as high electrical resistance requires high voltage to drive a given current.

The practical payoff is the relationship between pressure amplitude and **acoustic intensity** (power per unit area): I ∝ P_amplitude². This is the same squared-amplitude proportionality you saw for mechanical waves — doubling the pressure amplitude quadruples the intensity. This quadratic relationship is precisely why the decibel scale (which you'll encounter next in sound-intensity-and-decibels) uses a logarithmic unit: the enormous range of intensities the ear can handle compresses into a manageable 0–140 dB scale.

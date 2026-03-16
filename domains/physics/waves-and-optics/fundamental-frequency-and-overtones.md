---
id: fundamental-frequency-and-overtones
title: Fundamental Frequency and Overtones
domain: physics
course: waves-and-optics
prerequisites:
- id: acoustic-resonance-strings
  type: hard
- id: acoustic-resonance-pipes
  type: soft
tags:
- fundamental
- overtones
- harmonics
- timbre
stage: formal-systems
status: draft
---

# Fundamental Frequency and Overtones

## Core Idea
The fundamental frequency is the lowest resonant frequency of an object. Overtones (harmonics) are integer multiples of the fundamental. The presence and relative amplitudes of overtones determine the timbre or tone quality of an instrument: a pure tone has only the fundamental, while musical instruments produce many overtones simultaneously.

## Explainer

From your study of acoustic resonance in strings and pipes, you know that a standing wave forms when the boundary conditions force nodes at specific points — the ends of a string, the closed end of a pipe, or the open ends of a flute. Each valid standing wave pattern corresponds to a resonant frequency, and the string or air column will naturally oscillate at any of these frequencies. The lowest one — the longest wavelength that fits the geometry — is the **fundamental frequency** (f₁). It sets the perceived pitch of the note.

The higher resonant frequencies are called **overtones** or **harmonics**. For an ideal stretched string fixed at both ends, these occur at exactly 2f₁, 3f₁, 4f₁, and so on — they are **integer multiples** of the fundamental, which is why the string is called a **harmonic oscillator**. The second harmonic (2f₁) fits exactly two half-wavelengths into the string's length; the third harmonic (3f₁) fits three. Each harmonic has an additional node in the middle of the string. Open cylindrical pipes (like a flute) follow the same integer-multiple pattern; closed pipes (like a clarinet) support only odd harmonics (f₁, 3f₁, 5f₁, ...) because the closed end forces a node while the open end forces an antinode.

When you pluck a guitar string or bow a violin, you don't excite just one frequency — you excite many harmonics simultaneously. The string vibrates at f₁ and 2f₁ and 3f₁ all at once, with different amplitudes for each. This mixture is what the ear hears as a single complex tone. The recipe of which harmonics are present and how loud each one is determines the **timbre** — the characteristic sound quality that makes a violin sound different from a flute even when both play the same note at the same volume. A pure sine wave at 440 Hz sounds clinical and electronic; an oboe playing A4 sounds rich and reedy because it adds a dense stack of overtones on top of the fundamental.

Different physical objects favor different overtone mixtures. A struck marimba bar has overtones shaped by the bar's mass distribution (which is why bars are often shaved underneath to tune the overtones). A plucked string's overtone mix depends on where along its length you pluck — plucking near the center suppresses even harmonics, producing a hollow sound; plucking near the bridge emphasizes them, producing brightness. Understanding the harmonic series is the gateway to explaining why instruments have their characteristic voices, how synthesizers recreate those voices digitally, and why some combinations of notes sound consonant while others clash.

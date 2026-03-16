---
id: electronic-sound-design-techniques
title: Electronic Sound Design and Synthesis in Composition
domain: music
course: composition
prerequisites:
- id: electronic-composition-basics
  type: hard
tags:
- electronic
- synthesis
- sound-design
- timbre
stage: formal-systems
status: draft
---

# Electronic Sound Design and Synthesis in Composition

## Core Idea
Electronic composition requires understanding synthesis methods (subtractive, additive, granular) and how to shape timbre dynamically. Electronic sounds offer compositional possibilities unavailable in acoustic music, including continuous timbral evolution and microtonality.

## Explainer

Think of synthesis as building sound from scratch rather than recording it. In acoustic music, a violin's timbre is fixed by its physical construction — wood, strings, resonating body. In electronic sound design, you sculpt timbre from raw materials. The three synthesis architectures give you fundamentally different starting points.

**Subtractive synthesis** begins with a harmonically rich waveform — a sawtooth or square wave packed with overtones — and removes frequencies using a **filter**. Think of it like carving a sculpture: you start with everything and cut away what you don't want. A low-pass filter lets bass frequencies through while rolling off highs; as you sweep the cutoff frequency, the sound brightens or darkens continuously. This is the foundation of classic synthesizer sounds (Moog basses, Minimoog leads). **Additive synthesis** works the opposite way, building a sound by summing sine waves at different frequencies and amplitudes — reconstructing timbre from the overtone series. It offers precise timbral control but is computationally demanding and less intuitive. **Granular synthesis** fragments a sound into tiny "grains" (often 10–100 milliseconds) and reassembles them, enabling extreme time stretching, pitch shifting, and cloud-like textures impossible in other methods.

Across all synthesis types, the **ADSR envelope** is the central shaping tool. ADSR controls how a sound evolves over time: Attack (how quickly it rises), Decay (how it falls from peak to sustain level), Sustain (the level held while a key is depressed), and Release (how it fades after release). Apply this envelope to amplitude and you control the dynamic shape of a note. Apply it to filter cutoff and the timbre itself opens and closes over time. A plucked sound has fast attack, fast decay, zero sustain; a bowed string has slow attack, long sustain. Understanding envelopes lets you make electronic sounds behave organically.

The compositional dividend of synthesis is that **timbre becomes a compositional parameter** on equal footing with pitch and rhythm. An acoustic composer can orchestrate timbre by choosing instruments, but those timbres are essentially fixed. An electronic composer can write a timbre that slowly morphs from noise to pure tone over thirty seconds, or microtonally detune a single voice by 5 cents to create imperceptible beating that adds shimmer. **Microtonality** — pitches between the twelve equal-tempered semitones — is essentially free in electronic music; you simply specify a frequency in Hz rather than selecting from the keyboard's fixed grid. This opens harmonic worlds unavailable on conventional instruments, from just intonation (pure overtone ratios) to entirely invented tuning systems.


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

## Questions

```yaml
- question: "A composer wants a sound that begins as a single pure tone and gradually accumulates timbral complexity over 30 seconds. Which synthesis method is best suited for this goal, and why?"
  type: multiple-choice
  options:
    - "Subtractive — progressively close a high-pass filter to roll off the upper harmonics over time"
    - "Granular — fragment the source tone into grains and reassemble them for cloud-like texture"
    - "Additive — begin with one sine wave at the fundamental and progressively layer in harmonics at controlled amplitudes and rates"
    - "FM synthesis — the only method that supports timbral evolution over long time spans"
  answer: 2
  explanation: "Additive synthesis builds timbre by summing sine waves, giving direct control over which harmonics are present and at what amplitude. Starting with only the fundamental and gradually fading in partials over 30 seconds directly enacts the desired evolution. Subtractive synthesis starts with a rich waveform and removes frequencies — well-suited for brightening or darkening, but requires a rich source to begin with. Granular synthesis creates cloud-like textures from fragmented samples, which serves a different purpose."

- question: "A synthesizer's ADSR envelope is set to: Attack = 1ms, Decay = 50ms, Sustain = 0, Release = 0. What character will this envelope give to a sound?"
  type: multiple-choice
  options:
    - "A slow, atmospheric pad that swells gradually and fades over several seconds"
    - "A sharp percussive transient — a short click or pluck that rises and dies almost instantly with no sustained body"
    - "A bowed-string quality with a long held note and smooth release"
    - "A tremolo effect with rhythmic amplitude oscillation"
  answer: 1
  explanation: "With near-zero attack (immediate peak), fast decay (rapid fall from peak), zero sustain (nothing held), and zero release (instant cut after key release), the sound is essentially a very brief spike — the envelope shape of a plucked string, drumstick hit, or percussive click. The ADSR shape is the sonic fingerprint of how a sound evolves over time; mastering it means you can predict and design the feel of a sound by its envelope alone, before even choosing a waveform."

- question: "In subtractive synthesis, sweeping a low-pass filter's cutoff frequency downward (toward lower frequencies) will make the sound progressively darker and more bass-heavy."
  type: true-false
  answer: true
  explanation: "A low-pass filter lets frequencies below the cutoff through and attenuates those above it. Sweeping the cutoff downward removes more and more high-frequency harmonics from the waveform, leaving only the fundamental and lowest partials — which the ear perceives as a darker, warmer, more bass-heavy tone. This timbral evolution through filter sweeping is the defining sound of classic subtractive synthesis (e.g., the Moog filter sweep). The raw sawtooth or square wave contains all these harmonics; the filter sculpts the timbre by selectively removing them."

- question: "Microtonality — pitches between the standard twelve equal-tempered semitones — is primarily an acoustic phenomenon and is difficult to achieve in electronic synthesis, which is generally locked to the standard keyboard grid."
  type: true-false
  answer: false
  explanation: "This is precisely backwards. Electronic synthesis makes microtonality trivially easy: you simply specify a frequency in Hz rather than selecting a MIDI note from the 12-tone grid. A standard acoustic piano cannot produce the pitch between A4 (440 Hz) and A#4 (466 Hz), but a synthesizer can produce 450 Hz or 442.7 Hz or any arbitrary frequency with equal ease. Electronic music opens harmonic worlds — just intonation, 19-tone equal temperament, invented tuning systems — that are essentially inaccessible on conventional instruments. Microtonality is one of the defining freedoms of electronic composition."

- question: "How does the ADSR envelope transform timbre from a fixed property of a sound into a dynamic compositional parameter? Give a concrete example of applying an envelope to filter cutoff rather than amplitude, and describe the musical result."
  type: short-answer
  answer: "The ADSR envelope controls how a parameter changes over time — not just its final value. Applied to amplitude, it shapes the volume arc of a note. Applied to filter cutoff, it makes the timbral brightness itself evolve. For example: a synthesizer bass patch with a fast-attack, fast-decay envelope on the filter cutoff will momentarily open the filter (adding bright harmonics) at the moment a key is struck, then quickly close it back to a dark sustained tone. The result is the characteristic 'vowel-like' wah quality of many classic bass sounds — the timbre momentarily flares bright at the attack transient, then settles into a darker body, mimicking the behavior of acoustic instruments where the attack transient is spectrally richer than the sustained tone."
  explanation: "This example illustrates the key principle: in electronic synthesis, timbre is not fixed at design time but can be programmed to evolve across the duration of each note, across a phrase, or across an entire piece. An acoustic composer orchestrates timbre by choosing instruments; an electronic composer writes the timbral trajectory itself."
```

## Explainer

Think of synthesis as building sound from scratch rather than recording it. In acoustic music, a violin's timbre is fixed by its physical construction — wood, strings, resonating body. In electronic sound design, you sculpt timbre from raw materials. The three synthesis architectures give you fundamentally different starting points.

**Subtractive synthesis** begins with a harmonically rich waveform — a sawtooth or square wave packed with overtones — and removes frequencies using a **filter**. Think of it like carving a sculpture: you start with everything and cut away what you don't want. A low-pass filter lets bass frequencies through while rolling off highs; as you sweep the cutoff frequency, the sound brightens or darkens continuously. This is the foundation of classic synthesizer sounds (Moog basses, Minimoog leads). **Additive synthesis** works the opposite way, building a sound by summing sine waves at different frequencies and amplitudes — reconstructing timbre from the overtone series. It offers precise timbral control but is computationally demanding and less intuitive. **Granular synthesis** fragments a sound into tiny "grains" (often 10–100 milliseconds) and reassembles them, enabling extreme time stretching, pitch shifting, and cloud-like textures impossible in other methods.

Across all synthesis types, the **ADSR envelope** is the central shaping tool. ADSR controls how a sound evolves over time: Attack (how quickly it rises), Decay (how it falls from peak to sustain level), Sustain (the level held while a key is depressed), and Release (how it fades after release). Apply this envelope to amplitude and you control the dynamic shape of a note. Apply it to filter cutoff and the timbre itself opens and closes over time. A plucked sound has fast attack, fast decay, zero sustain; a bowed string has slow attack, long sustain. Understanding envelopes lets you make electronic sounds behave organically.

The compositional dividend of synthesis is that **timbre becomes a compositional parameter** on equal footing with pitch and rhythm. An acoustic composer can orchestrate timbre by choosing instruments, but those timbres are essentially fixed. An electronic composer can write a timbre that slowly morphs from noise to pure tone over thirty seconds, or microtonally detune a single voice by 5 cents to create imperceptible beating that adds shimmer. **Microtonality** — pitches between the twelve equal-tempered semitones — is essentially free in electronic music; you simply specify a frequency in Hz rather than selecting from the keyboard's fixed grid. This opens harmonic worlds unavailable on conventional instruments, from just intonation (pure overtone ratios) to entirely invented tuning systems.


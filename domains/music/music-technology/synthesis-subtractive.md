---
id: synthesis-subtractive
title: Subtractive Synthesis
domain: music
course: music-technology
prerequisites:
- id: pitch-and-frequency
  type: hard
- id: equalization-theory
  type: soft
builds-toward: []
tags:
- synthesis
- subtractive-synthesis
- sound-design
- synthesizers
stage: advanced
status: validated
---

# Subtractive Synthesis

## Core Idea
Subtractive synthesis begins with harmonically rich waveforms and uses filters to sculpt their timbre by removing (subtracting) frequency content. It is the oldest and most widely understood synthesis method, the foundation of classic analog synthesizers like the Moog Minimoog, Roland Juno, and Sequential Prophet-5, and it remains central to electronic music production today.

The signal path of a subtractive synthesizer follows the VCO → VCF → VCA architecture. The voltage-controlled oscillator (VCO) generates the raw waveform. A sawtooth wave contains all harmonics (both odd and even) at amplitudes that decrease as 1/n — rich, bright, and buzzy. A square wave contains only odd harmonics, producing a hollow, woody sound. A triangle wave has odd harmonics falling off steeply, sounding nearly sinusoidal. A sine wave has no harmonics at all — just the fundamental. Starting with harmonic-rich waveforms gives the filter material to work with.

The voltage-controlled filter (VCF) is the heart of subtractive synthesis. Low-pass filters are most common — they pass frequencies below the cutoff while attenuating frequencies above it. The slope of the filter (12 dB/octave or 24 dB/octave) determines how sharply it rolls off above the cutoff. Resonance (also called Q or emphasis) boosts frequencies at the cutoff point; at high resonance, the filter emphasizes a narrow band and can self-oscillate, producing a sine wave at the cutoff frequency — which itself can be played as a pitched instrument.

The voltage-controlled amplifier (VCA) and envelope generator control amplitude over time. ADSR (Attack, Decay, Sustain, Release) envelopes shape both the filter cutoff and amplitude, creating sounds that evolve from pluck to pad. An LFO (low-frequency oscillator, typically below 20 Hz) introduces periodic modulation — vibrato (LFO to pitch), tremolo (LFO to amplitude), or wah (LFO to filter cutoff).

## Questions

```yaml
- question: "In subtractive synthesis, what is the primary role of the voltage-controlled filter (VCF)?"
  type: multiple-choice
  options:
    - "Amplify the oscillator signal"
    - "Remove harmonics and shape timbre"
    - "Add new harmonics to the waveform"
    - "Create stereo width"
  answer: 1
  explanation: "The VCF removes (subtracts) harmonics, transforming bright, buzzy raw waveforms into warmer, more complex tones. The filter is the central tone-shaping element of subtractive synthesis."

- question: "What does a sawtooth wave contain that a sine wave does not?"
  type: multiple-choice
  options:
    - "Lower fundamental frequencies"
    - "Both odd and even harmonics at decreasing amplitudes"
    - "A complex envelope"
    - "Stereo information"
  answer: 1
  explanation: "A sine wave contains only the fundamental frequency. A sawtooth contains all harmonics (odd and even) at amplitudes inversely proportional to their harmonic number. This harmonic richness is what gives the filter material to subtract."

- question: "What is an envelope generator?"
  type: short-answer
  answer: "A module that modulates a parameter (like filter cutoff or amplitude) over time with four stages: Attack (time to reach peak), Decay (time to fall to sustain level), Sustain (held level while key is pressed), Release (time to fall to silence after key release)."
  explanation: "Envelope generators shape how a sound evolves from key-press to key-release, adding dynamic character. Applied to the filter, they create tonal variation over time; applied to the VCA, they control volume shape."

- question: "Why is resonance important in subtractive synthesis?"
  type: multiple-choice
  options:
    - "It sets the filter color across all frequencies equally"
    - "It emphasizes the cutoff frequency, adding presence and character, and at extreme values causes the filter to self-oscillate"
    - "It removes frequencies more efficiently"
    - "It has no audible effect on the sound"
  answer: 1
  explanation: "High resonance creates a ringing, emphasized band at the cutoff frequency. This is responsible for the classic 'wah' and 'sweep' sounds of analog synthesis. At maximum resonance, many filters self-oscillate — producing a sine wave pitch."

```

## Explainer

Subtractive synthesis is the architecture of the classic analog synthesizer, and understanding it provides a mental model applicable to nearly all subsequent synthesis methods. The VCO-VCF-VCA-ADSR signal flow is simple enough to grasp quickly but deep enough to produce virtually unlimited timbral variety through parameter interaction.

The analog circuit imperfections that gave classic synthesizers their character — slight pitch instability in VCOs (warmth), the nonlinear behavior of transistor ladder filters (harmonic saturation), the asymmetry in VCA gain stages — are now emulated in software with great precision. Understanding why these imperfections were musically desirable requires knowing the clean theoretical signal flow they deviated from.

Modern subtractive synthesizers often include polyphony (multiple simultaneous notes), unison modes (multiple detuned oscillators per voice for thickness), and modulation matrices (routing any modulation source to any destination with adjustable depth). These extensions build on the core VCO-VCF-VCA architecture, which remains the clearest entry point into electronic sound design.

---
id: sampling-theory-audio
title: Sampling Theory in Audio
domain: music
course: music-technology
prerequisites:
- id: digital-audio-fundamentals
  type: hard
builds-toward: []
tags:
- digital-audio
- sampling
- nyquist
- signal-processing
stage: advanced
status: validated
---

# Sampling Theory in Audio

## Core Idea
Sampling theory describes the mathematical conditions under which a continuous analog signal can be captured and perfectly reconstructed from discrete samples. The central result — the Nyquist-Shannon sampling theorem — states that a bandlimited signal can be exactly reconstructed if the sample rate exceeds twice the signal's highest frequency component. This upper limit is called the Nyquist frequency.

When audio content exists at frequencies above half the sample rate, aliasing occurs: those high-frequency components "fold back" into the audible spectrum as false, spurious tones. A 20 kHz tone recorded at 32 kHz sample rate would alias to 12 kHz — a clearly audible artifact that wasn't in the original sound. Anti-aliasing filters (low-pass filters applied before the analog-to-digital converter) prevent aliasing by removing content above Nyquist before sampling.

Oversampling — recording at a multiple of the target sample rate — allows more gradual filter slopes, reducing phase distortion and ripple in the audio passband. Many modern converters oversample internally at 8x or 16x the output rate, then use digital filters to downsample to 44.1 or 48 kHz. This produces audibly cleaner results than steep analog anti-aliasing filters.

Sample rate also matters for pitch-shifting and time-stretching algorithms. Time-domain techniques like granular synthesis and phase vocoders operate on the sample-level structure of audio. Higher sample rates provide more samples per period of each frequency, giving these algorithms more data to work with and producing less artifacting at extreme settings.

## Questions

```yaml
- question: "What happens when audio containing a 25 kHz tone is recorded at a 44.1 kHz sample rate without an anti-aliasing filter?"
  type: multiple-choice
  options:
    - "The tone is captured faithfully"
    - "The tone is silently discarded"
    - "The tone folds back into the audible spectrum as a false frequency"
    - "The sample rate automatically increases to accommodate the tone"
  answer: 2
  explanation: "Aliasing occurs when signal frequency exceeds Nyquist (22.05 kHz at 44.1 kHz). The 25 kHz tone aliases to 44.1 - 25 = 19.1 kHz — an audible artifact not in the original audio."

- question: "True or false: The Nyquist frequency equals the sample rate."
  type: true-false
  answer: false
  explanation: "The Nyquist frequency is half the sample rate. At 44.1 kHz, the Nyquist frequency is 22.05 kHz. Frequencies above that cannot be faithfully sampled."

- question: "What is oversampling, and what problem does it solve?"
  type: short-answer
  answer: "Oversampling means digitizing at a multiple of the target rate (e.g., 8x or 16x), then downsampling digitally. It allows gentler digital anti-aliasing filters instead of steep analog filters, reducing phase distortion in the passband."
  explanation: "Steep analog anti-aliasing filters cause phase ringing near the cutoff frequency. Oversampling shifts the anti-aliasing problem into the digital domain where linear-phase filters can be used."

- question: "A sound designer records foley at 96 kHz but delivers at 48 kHz. What must happen during the conversion?"
  type: multiple-choice
  options:
    - "The file must be pitch-shifted down by one octave"
    - "Content above 24 kHz must be filtered before halving the sample count"
    - "Bit depth must also be halved"
    - "No conversion is needed — 96 kHz files play fine at 48 kHz"
  answer: 1
  explanation: "Downsampling from 96 kHz to 48 kHz requires filtering all content above 24 kHz (the new Nyquist) to prevent those frequencies from aliasing into the audible band during the sample-count reduction."

```

## Explainer

Sampling theory provides the mathematical foundation for all digital audio systems. Claude Shannon and Harry Nyquist formalized the conditions for lossless digital representation of analog signals, and their theorem governs every decision about sample rate in modern audio hardware and software.

The practical implications extend beyond the recording stage. Sample rate affects latency in real-time processing (higher rates mean smaller buffer sizes for equivalent latency), computational load in plugins (more samples per second to process), and the accuracy of time-domain algorithms. Understanding the Nyquist theorem prevents common errors like recording at rates too low for high-frequency content and failing to apply appropriate anti-aliasing when downsampling.

Sampling theory also connects directly to synthesis and audio programming: wavetable synthesis scans through stored single-cycle waveforms at sample-accurate rates, and any synthesis algorithm generating frequencies above Nyquist must include appropriate limiting to prevent aliasing artifacts in the output.

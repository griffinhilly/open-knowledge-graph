---
id: synthesis-fm-and-additive
title: FM and Additive Synthesis
domain: music
course: music-technology
prerequisites:
- id: synthesis-subtractive
  type: hard
builds-toward: []
tags:
- synthesis
- fm-synthesis
- additive-synthesis
- sound-design
stage: advanced
status: validated
---

# FM and Additive Synthesis

## Core Idea
FM (Frequency Modulation) synthesis and additive synthesis represent two fundamentally different approaches to generating complex timbres — both contrast sharply with subtractive synthesis's start-and-remove approach.

In FM synthesis, one oscillator (the modulator) modulates the frequency of another oscillator (the carrier) at audio rates. When modulation occurs in the audio frequency range (above ~20 Hz), it generates new sidebands — frequency components that do not exist in either oscillator alone. The sidebands appear at frequencies of carrier ± (n × modulator), where n is an integer. This means a small change in the modulation index (depth) creates dramatic, nonlinear timbral shifts. The classic FM sound — bells, electric pianos, clangorous metallic tones, glassy organs — comes from these harmonic and inharmonic sidebands. The Yamaha DX7 (1983), built on John Chowning's FM research at Stanford, defined an era of pop music. FM synthesis is CPU-efficient, generating complex timbres from simple sine waves, but parameter-to-sound relationships are nonintuitive and require experience to navigate.

Additive synthesis works from first principles: the Fourier theorem states that any complex waveform can be expressed as a sum of sine waves at different frequencies, amplitudes, and phases. Additive synthesis constructs sounds by explicitly controlling each partial — ideally hundreds of them — with individual amplitude envelopes. This offers complete control over every harmonic, allowing precise reproduction of acoustic instruments or the creation of sounds physically impossible in nature. The computational cost is high (many oscillators per voice), and real-time control of hundreds of partials requires specialized interfaces. Spectral modeling tools like SPEAR and iZotope RX decompose recorded audio into additive components, enabling hybrid resynthesis and transformation.

The operator concept from FM bridges into FM-additive hybrids: operators can be configured in various algorithms (parallel or series chains of modulators and carriers), with each configuration producing distinct spectral character.

## Questions

```yaml
- question: "In FM synthesis, what happens to the timbre when the modulation index is increased?"
  type: multiple-choice
  options:
    - "The sound becomes quieter"
    - "New sideband frequencies are generated, dramatically changing the harmonic content"
    - "The carrier frequency shifts higher"
    - "The sound becomes more sinusoidal"
  answer: 1
  explanation: "Increasing modulation index generates more and stronger sidebands at carrier ± (n × modulator). This is why small modulation index changes in FM synthesis produce dramatic, nonlinear timbral shifts."

- question: "True or false: Additive synthesis generates sound by starting with harmonically rich waveforms and filtering them."
  type: true-false
  answer: false
  explanation: "That describes subtractive synthesis. Additive synthesis constructs sound by summing many individual sine wave partials, each with its own frequency, amplitude, and phase — building up complexity from the simplest components."

- question: "What is the relationship between the carrier and modulator oscillators in FM synthesis?"
  type: short-answer
  answer: "The modulator's output is applied to the carrier's frequency input, varying the carrier's instantaneous pitch at audio rates. This frequency modulation generates sidebands at carrier ± (n × modulator frequency)."
  explanation: "When modulation rate is in the audible range, it produces sidebands rather than simple pitch vibrato. The ratio of modulator to carrier frequency determines whether the sidebands are harmonic (integer ratio) or inharmonic (non-integer ratio)."

- question: "Why do non-integer ratios between carrier and modulator frequencies produce metallic or bell-like tones in FM synthesis?"
  type: multiple-choice
  options:
    - "Non-integer ratios produce lower sideband frequencies"
    - "Non-integer ratios generate inharmonic sidebands that don't fit the harmonic series, creating the inharmonic spectra characteristic of metal and bells"
    - "Non-integer ratios increase the amplitude of all harmonics equally"
    - "Non-integer ratios cause FM synthesis to revert to subtractive behavior"
  answer: 1
  explanation: "When carrier:modulator ratios are non-integer (e.g., 1:1.4), the sidebands fall at non-harmonic frequencies. Physical objects like bells and metal bars have inharmonic partial series, so FM's inharmonic sidebands naturally mimic those timbres."

```

## Explainer

FM synthesis revolutionized electronic music production in the 1980s by enabling complex, bright, metallic timbres from inexpensive hardware — a Yamaha DX7 cost far less than a Moog but could produce electric piano, vibraphone, and percussive sounds with remarkable realism for the era. The limitation — opaque parameter relationships — became an aesthetic signature: the DX7's "wrong" patches became iconic sounds in their own right.

Additive synthesis offers a complementary perspective: where FM achieves complexity through modulation interactions, additive achieves it through explicit harmonic specification. Understanding additive synthesis provides deep insight into the structure of timbre itself — the fact that all steady-state sounds can be decomposed into sinusoidal components. This connects directly to Fourier analysis, spectrograms, and spectral audio processing.

Modern synthesizers often combine synthesis approaches. Serum combines wavetable oscillators with FM modulation. Ableton Operator is a four-operator FM synthesizer. Spitfire's granular engine resynthesizes recordings as additive partial tracks. Understanding FM and additive synthesis unlocks these hybrid instruments and provides the theoretical framework to understand spectral transformations applied in mastering and restoration processing.

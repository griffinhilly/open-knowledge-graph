---
id: timbre-frequency-domain
title: Timbre Analysis in the Frequency Domain
domain: music
course: advanced-music-theory
prerequisites:
- id: spectral-composition-acoustics
  type: hard
- id: pitch-and-frequency
  type: hard
- id: fourier-series-definition
  type: soft
builds-toward:
- electroacoustic-composition
tags:
- timbre
- frequency
- acoustics
- analysis
stage: advanced
status: draft
---

# Timbre Analysis in the Frequency Domain

## Core Idea
Fourier analysis decomposes complex timbres into frequency components. Understanding timbre in the frequency domain reveals why certain harmonies sound unified (similar spectra) or clashing (conflicting partials), explaining perceptual phenomena that note-based analysis cannot address.

## Explainer

From your prerequisite on spectral acoustics, you know that a musical sound is not a pure sine wave but a complex periodic waveform: a fundamental frequency f₀ sounded simultaneously with its harmonics at 2f₀, 3f₀, 4f₀, and so on, each present at a different amplitude. From your study of pitch and frequency, you know that these harmonics correspond to the intervals of the overtone series — the octave, octave plus fifth, double octave, and so on up. **Timbre** is the signature of how energy is distributed across these harmonics. A clarinet and a violin playing concert A at 440 Hz share the same fundamental but differ dramatically in which harmonics are amplified and which are attenuated. The frequency domain makes this distribution visible.

**Fourier analysis** decomposes any periodic waveform into a sum of sinusoids at discrete frequencies. The result is a **spectrum**: a plot of amplitude versus frequency showing peaks at the fundamental and each harmonic. The clarinet's spectrum is characterized by strong odd harmonics (1st, 3rd, 5th…) and weak even ones — a consequence of its cylindrical bore and single-reed mouthpiece. A violin's spectrum includes both odd and even harmonics, with the amplitudes shaped by the instrument's resonance chambers. A flute's spectrum is dominated by the fundamental with weak upper harmonics, producing its characteristic "pure" tone. The **spectral envelope** — the smooth curve connecting the harmonic peaks — is what the ear primarily tracks for timbre identification, more than the fine detail of individual partial amplitudes.

Harmony and dissonance are grounded in spectral interactions that note-based analysis cannot see. When two pitches are played simultaneously, their harmonic series either **align** or **conflict**. A perfect fifth (3:2 frequency ratio) aligns harmonics: the upper note's fundamental (3f₀) coincides with the lower note's third harmonic, its second harmonic (6f₀) coincides with the lower note's sixth, and so on. The spectra mesh, producing a fused, consonant sound. A minor second places two fundamentals close but not equal, and their respective harmonic series spawn many **near-misses** — partials close enough to interfere and produce **beating** (rapid amplitude fluctuations). The auditory system interprets dense beating as roughness, which is the physical basis of dissonance. This is not a cultural convention but an acoustical fact about spectral overlap.

Timbre is not static but **dynamic**: it evolves over the duration of a note. The **attack transient** — the first 20–100 milliseconds — typically contains inharmonic, noisy components that disappear as the tone stabilizes into its steady-state spectrum. The attack is paradoxically the most information-rich part: subjects in listening experiments identify instruments correctly from attack alone, but struggle when the attack is removed and only the sustained tone remains. Piano notes played backwards illustrate this vividly — the sound becomes a strange organ-like tone, recognizable as piano-derived but lacking the crisp attack that defines the piano's identity. A **spectrogram** (frequency on the vertical axis, time on the horizontal, amplitude as color intensity) captures this temporal evolution. Spectral composers — Murail, Grisey, Saariaho — use spectrograms as compositional blueprints, writing orchestral music that traces the frequency-domain evolution of a single instrument's tone, turning timbre analysis into compositional structure.

---
id: spectral-harmony-overtone-analysis
title: Spectral Harmony and Overtone Analysis
domain: music
course: advanced-music-theory
prerequisites:
- id: spectral-analysis-acoustics
  type: hard
- id: timbre-frequency-domain
  type: hard
- id: proportions
  type: soft
- id: fourier-series-definition
  type: soft
builds-toward:
- timbre-evolution-analysis
- frequency-modulation-synthesis-theory
tags:
- spectral
- harmony
- acoustics
stage: expert
status: validated
---

# Spectral Harmony and Overtone Analysis

## Core Idea
Spectral harmony derives chords from natural overtone series, treating partials as pitch elements. This acoustically-grounded approach creates harmonic relationships independent of equal temperament. Spectral composers use overtone stacks to bridge timbre and harmony, creating novel sonorities rooted in acoustic reality.

## How It's Best Learned
Analyze overtone series of various instruments and extract potential chords. Study Grisey and Murail spectral compositions, tracing how chord progressions arise from spectral filtering or instrument combinations.

## Common Misconceptions
- Assuming spectral harmony always uses full, literal overtone stacks; composers select relevant partials. - Confusing spectral harmony with harmonic analysis of tonal music; spectral approaches suspend functional relationships. - Overlooking that equal temperament significantly alters overtone-derived pitches.

## Questions

```yaml
- question: "Why do spectral composers often write music that cannot be performed accurately on instruments tuned to equal temperament?"
  type: multiple-choice
  options:
    - "Equal temperament creates pitches that don't correspond to actual overtone partials, distorting the acoustic coherence that spectral harmony seeks"
    - "Equal temperament has too few pitches to represent the full chromatic spectrum spectral composers need"
    - "Equal temperament was designed for tonal music and physically cannot produce dissonant intervals"
    - "Spectral harmony requires ancient tuning systems that predate equal temperament by centuries"
  answer: 0
  explanation: "The overtone series produces pitches at exact integer multiples of the fundamental. These spectral pitches — especially partials 7, 11, and 13 — fall between the semitones of equal temperament. Partial 7 is a noticeably flat minor seventh; partial 11 is flatter than a tritone. Spectral composers like Grisey embrace these deviations as the defining acoustic character of their work, not approximating them to equal-tempered pitches but writing microtonal notation or choosing instruments (brass, voices, strings) that can produce them naturally."

- question: "A chord built from partials 12–16 of a low fundamental, compared to one built from partials 1–4 of the same fundamental, will tend to sound:"
  type: multiple-choice
  options:
    - "More stable and open, since higher frequency partials have greater acoustic energy"
    - "Denser and noisier, approaching the acoustic character of a sustained percussion sound"
    - "Harmonically equivalent, since both reference the same fundamental"
    - "More tonal and functional, since high partials correspond to upper scale degrees"
  answer: 1
  explanation: "Low partials (1–4) correspond to the fundamental, octave, perfect fifth, and double octave — open, stable intervals that resemble a root-position triad. High partials (12–16) are densely spaced in frequency and produce complex, nearly-noise-like textures. Grisey described this as the acoustic analogy to a sound's decay: a sustained tone begins with strong fundamental and low partials, then fills out with overtone shimmer. Moving from low to high partials in a piece mirrors a sound evolving through time."

- question: "Spectral harmony can be analyzed using functional Roman numeral analysis because both spectral and tonal music organize pitches around a fundamental harmonic series."
  type: true-false
  answer: false
  explanation: "Spectral harmony explicitly suspends functional harmonic relationships. In tonal music, chords have roles (tonic, dominant, subdominant) defined by their position in a key. In spectral music, the organizing logic is acoustic — relationships are defined by their position in the overtone series of a fundamental. Progression in spectral music is transformation of the sonic 'body' of a sound, not motion through tonal functions. Applying Roman numeral analysis would misrepresent the underlying compositional logic."

- question: "Partials 7, 11, and 13 of the overtone series deviate noticeably from the nearest equal-tempered pitches."
  type: true-false
  answer: true
  explanation: "These upper partials are among the most acoustically significant deviations from equal temperament. Partial 7 is roughly a flat minor seventh — about 31 cents flatter than equal temperament's minor seventh. Partial 11 is approximately a tritone but about 49 cents flat. Partial 13 approximates a major sixth. These 'between-note' pitches are a defining feature of spectral harmony's sonic color, and composers like Murail notate them using quarter-tones or arrows indicating pitch deviation."

- question: "What is the primary compositional decision in spectral writing, and why don't spectral composers simply use all available overtone partials?"
  type: short-answer
  answer: "The primary decision is selecting which partials to include in a chord or texture. Using all partials from 1 to 16 would produce an extremely dense, thick sound — more like noise than a chord. Instead, composers choose specific partials for their pitch content, register, and acoustic interaction: low partials (1–4) for stable open intervals, partial 7 for the characteristic flat minor seventh color, partials 11 and 13 for ambiguous 'between-note' pitches that blur tonal identity. Selective filtering of the overtone series is the compositional craft — choosing which aspects of a sound's acoustic 'body' to emphasize at each moment."
  explanation: "This selective approach is analogous to timbre design: a composer 'sculpts' a sound from its spectral components. Grisey called the process of moving through different spectral densities the 'genesis of sound,' treating the piece itself as one long, slowly transforming tone."
```

## Explainer

From your study of acoustics and the frequency domain, you know that a vibrating string or column of air doesn't produce a single pure frequency — it produces a **harmonic series**: a fundamental frequency f₀ and overtones at 2f₀, 3f₀, 4f₀, 5f₀, and so on. Your work with Fourier series formalized this: any periodic waveform decomposes into sinusoidal components at integer multiples of the fundamental. In practice, an oboe playing A at 440Hz simultaneously produces energy at 880Hz, 1320Hz, 1760Hz, etc., each partial present at varying amplitudes that define the instrument's timbre. Spectral harmony takes this observation and turns it inside out: rather than treating the overtone series as the acoustic explanation of timbre, it treats the overtone series as a **compositional resource** — a chord built directly from nature.

The first 16 partials of a fundamental produce pitches that approximate many of the notes in a chromatic scale, but not quite. Partial 7 is a noticeably flat minor seventh; partial 11 is roughly a tritone but flatter than equal temperament; partial 13 approximates a major sixth. These **spectral pitches** don't fit neatly into equal temperament at all. Spectral composers like Gérard Grisey and Tristan Murail embrace this deviation as a feature rather than a bug. A chord built from partials 8–16 of a low E has a shimmer and acoustic coherence that no equal-tempered chord quite captures — each pitch is simultaneously a harmonic and a "color" of the fundamental, creating a blurring of the boundary between pitch and timbre. When the fundamental shifts, the entire chord system shifts with it, and the progression sounds less like harmonic motion in the functional sense and more like a transformation of the sonic "body" of a single sound.

**Selecting partials** is the primary compositional decision in spectral writing. A full overtone stack from partial 1 to 16 would be thick and dense; most spectral composers filter the series, choosing partials for their pitch content, register, and acoustic interaction. Partial 3 (an octave plus fifth, i.e., a perfect fifth above the first octave) gives open, stable intervals. Partial 7 introduces the characteristic flat minor seventh that gives spectral harmony its distinctive color. Partials 11 and 13 add ambiguous "between-note" pitches that blur tonal identity. The composer's craft lies in choosing which partials to use, how to distribute them across voices, and how to create motion by shifting the fundamental or gradually introducing higher, more dissonant partials — a process Grisey called the "genesis of sound."

Spectral progressions can be analyzed as transformations of the underlying physical model. A chord built on low partials (1–4) is acoustically stable — it resembles a root-position triad. A chord emphasizing high partials (12–16) is dense and noisy, approaching the acoustic character of the consonant noise bands in percussion. Moving through a spectral progression from low to high partials mirrors the acoustic trajectory of a sound in time: the onset of a sustained tone begins with prominent fundamental and low partials, while the decay brings out overtone shimmer. Spectral composers often structure entire pieces around this arc, treating the piece as one long "living sound." Understanding this acoustic grounding is what separates spectral analysis from other post-tonal methods — the organizing logic is not serial, not tonal, not aleatoric, but physical: the natural acoustic properties of vibrating matter.

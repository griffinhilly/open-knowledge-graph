---
id: tuning-systems-temperament
title: Tuning Systems and Temperament
domain: music
course: advanced-music-theory
prerequisites:
- id: intervals-basics
  type: hard
- id: pitch-and-frequency
  type: hard
- id: ratios
  type: soft
- id: logarithms-intro
  type: soft
- id: logarithm-properties
  type: soft
- id: rational-numbers-operations
  type: soft
tags:
- tuning
- temperament
- acoustics
- intonation
stage: advanced
status: draft
---

# Tuning Systems and Temperament

## Core Idea
Different tuning systems (just intonation, Pythagorean, equal temperament, meantone, and non-Western systems) produce different sonorities and harmonic relationships; understanding these distinctions explains compositional choices and performance practice in different musical traditions. Contemporary microtonality deliberately exploits these alternative tuning systems for new expressive and structural possibilities.

## Explainer

From your study of pitch and frequency you know that musical intervals correspond to frequency ratios: an octave is a 2:1 ratio, a perfect fifth is 3:2, a major third is 5:4. These **pure ratios** arise from the overtone series — the natural harmonics that sound objects produce — and they are what the ear perceives as maximally consonant. A tuning system is a decision about which frequency ratios to use for the notes of a scale. The problem is that pure ratios are mathematically incompatible with each other at scale, and every tuning system is a different compromise.

Here is the fundamental conflict, which your knowledge of logarithms and rational numbers will help you see precisely. Stack twelve perfect fifths (each 3:2): you move upward by (3/2)^12. Stack seven octaves (each 2:1): you move upward by 2^7 = 128. If the circle of fifths truly closed — if twelve fifths equaled seven octaves — these two numbers would be equal. But (3/2)^12 = 531441/4096 ≈ 129.746, not 128. The ratio 531441/524288 (≈ 1.01364) is the **Pythagorean comma**: the small gap by which a twelve-fifth stack overshoots seven octaves. Every tuning system is a strategy for distributing this comma across the scale.

**Pythagorean tuning** keeps all fifths pure (3:2) and accepts that the major thirds will be wide — specifically the ratio 81:64 rather than the pure 5:4. This produces a characteristic bright, tense sound for thirds, which suits monophonic melody but creates beating in sustained chords. **Just intonation** instead tunes the major thirds pure (5:4) and accepts that some fifths must be impure. The result is maximally consonant harmony in one key but uneven intervals that make modulation problematic. **Meantone temperament** — dominant from the Renaissance through the Baroque — splits the difference: slightly narrow fifths (each reduced by one quarter of the syntonic comma) produce pure or near-pure major thirds, enabling rich polyphony in common keys while relegating certain remote keys to extreme dissonance.

**Equal temperament** takes the comma and distributes it uniformly: all twelve fifths are slightly narrow by the same amount, making each semitone exactly the twelfth root of 2 (2^(1/12) ≈ 1.05946). Every key is equally in tune — and equally slightly out of tune relative to pure ratios. The logarithm is central here: the **cent** is defined as one hundredth of an equal-tempered semitone, or (2^(1/12))^(1/100) = 2^(1/1200). Any interval can be expressed in cents by taking 1200 × log₂(frequency ratio). A pure perfect fifth is 701.96 cents; an equal-tempered fifth is exactly 700 cents — a difference of less than 2 cents, imperceptible to most listeners but nonzero. Understanding these systems reveals that Western tonal harmony as we know it rests on a practical compromise accepted in the 18th century, and that composers working in microtonality — using intervals between the twelve equal-tempered pitches — are not departing from tradition but returning to its full mathematical richness.

---
id: microtonal-systems-analysis
title: Microtonal Systems and Harmonic Implications
domain: music
course: advanced-music-theory
prerequisites:
- id: extended-harmony-clusters
  type: hard
- id: just-intonation-acoustics
  type: hard
- id: rational-numbers-operations
  type: soft
- id: fractions-of-a-set
  type: soft
- id: ratios
  type: soft
- id: logarithms-intro
  type: soft
- id: modular-arithmetic
  type: soft
tags:
- microtonality
- harmony
- tuning
- systems
stage: abstract-reasoning
status: draft
---

# Microtonal Systems and Harmonic Implications

## Core Idea
Microtonal music divides the octave into intervals smaller than the semitone. Each tuning system (19-ET, 31-ET, Bohlen-Pierce, spectral tunings) has distinct harmonic properties and suggest different harmonic vocabularies. Analyzing microtonality requires understanding both the mathematical structure of tuning systems and their perceptual effects.

## Explainer

You already understand **just intonation**: tuning intervals to small-integer ratios (perfect fifth = 3:2, major third = 5:4) to achieve acoustically pure intervals with minimal beating. The problem is that pure intervals in one key create wolf intervals in others, which is why 12-tone equal temperament (12-TET) divides the octave into 12 equal logarithmic steps and accepts small deviations from just ratios in exchange for full transposability. **Microtonal systems** ask a deeper question: what if we treat the tuning system itself as a compositional resource, choosing the octave division for its specific harmonic affordances rather than accepting 12-TET as a neutral default?

In **equal temperament systems** (n-ET), the octave is divided into n equal steps of 1200/n cents each. **19-ET** uses steps of ~63 cents and produces a major third (6 steps = 378 cents) closer to just (386 cents) than 12-TET's 400 cents, along with a very narrow chromatic semitone that gives it a distinctive leading-tone pull. **31-ET** (steps of ~39 cents) approximates just intervals still more accurately — its perfect fifth, major third, and harmonic seventh all fall within 5 cents of just values — and enharmonic equivalents like C# and Db become genuinely distinct pitches separated by a diesis of ~41 cents. Each system supports different harmonic vocabularies: 31-ET opens up extended just-intonation chord structures within an equal-tempered framework, while 19-ET has a natural grammar for chromatic voice-leading.

Systems like **Bohlen-Pierce** break from the octave entirely. Instead of dividing the 2:1 ratio, Bohlen-Pierce divides the **tritave** (3:1) into 13 equal steps. This produces a scale with no conventional octave equivalence but strong consonances built from 3:5:7 ratios — the same odd-integer ratios that dominate the seventh partial of the harmonic series. **Spectral tunings** derive pitch collections directly from the overtone series of a single fundamental, so the intervals match the actual partials produced by a given instrument's timbre. The mathematical tools you need to work with these systems are logarithms (to convert frequency ratios into cents: cents = 1200 × log₂(ratio)) and modular arithmetic (to understand how n-ET step classes wrap around the octave or tritave and define equivalence classes).

Analyzing a piece in a microtonal system requires starting from scratch with interval tables. In 12-TET, a tritone (600 cents) is its own inversion and creates tritone-substitution equivalences. In 31-ET, the tritone and its complement are distinct, and the system contains approximations of 7-limit intervals (7:4 ≈ 969 cents, 7:6 ≈ 267 cents) absent from 12-TET. Voice-leading, harmonic roots, and set-class equivalences all depend on the step size of the system you are in. The theoretical apparatus — interval classes, transposition, inversion, prime forms — must be rebuilt relative to the system's modular structure. This is what makes microtonal analysis genuinely different from retuning 12-TET music: the harmonic logic is not just stretched or compressed, it is structurally reorganized.

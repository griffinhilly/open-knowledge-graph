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
stage: expert
status: draft
---

# Microtonal Systems and Harmonic Implications

## Core Idea
Microtonal music divides the octave into intervals smaller than the semitone. Each tuning system (19-ET, 31-ET, Bohlen-Pierce, spectral tunings) has distinct harmonic properties and suggest different harmonic vocabularies. Analyzing microtonality requires understanding both the mathematical structure of tuning systems and their perceptual effects.

## Questions

```yaml
- question: "A composer trained in 12-TET wants to compose in 31-ET by 'stretching' their usual harmonic vocabulary to fit the new tuning. What is the fundamental problem with this approach?"
  type: multiple-choice
  options:
    - "31-ET has fewer consonant intervals than 12-TET, so the vocabulary would need to shrink, not stretch"
    - "In 31-ET, enharmonic equivalents like C# and Db are genuinely distinct pitches, so the 12-TET system of equivalences breaks down and the harmonic grammar must be rebuilt from scratch"
    - "31-ET cannot approximate any just-intonation intervals, making harmonic analysis impossible"
    - "Nothing is fundamentally wrong; 31-ET is essentially 12-TET with higher resolution"
  answer: 1
  explanation: "In 12-TET, C# and Db are the same pitch — enharmonic equivalence is a structural feature of the system. In 31-ET they are separated by a diesis (~41 cents), making them genuinely distinct. This is not a small adjustment; it means interval classes, set equivalences, and even the concept of 'tritone substitution' all depend on the specific modular arithmetic of 31 rather than 12. The theoretical apparatus — transposition, inversion, prime forms — must be rebuilt around mod-31 arithmetic, not adapted from mod-12."

- question: "The Bohlen-Pierce scale is built on what structural foundation that sets it apart from most Western microtonal systems?"
  type: multiple-choice
  options:
    - "It divides the perfect fifth (3:2) into equal logarithmic steps"
    - "It divides the tritave (3:1 frequency ratio) into 13 equal steps, replacing the octave as the equivalence interval"
    - "It is derived from the overtone series of a specific instrument's timbre"
    - "It uses 19 equal steps instead of 12, producing a closer approximation to just intervals"
  answer: 1
  explanation: "Most tuning systems — 12-TET, 19-ET, 31-ET — divide the octave (2:1). Bohlen-Pierce instead takes the tritave (3:1, a frequency ratio of three to one) as its equivalence interval and divides it into 13 equal logarithmic steps. This produces a scale with no conventional octave equivalence but strong consonances built on 3:5:7 ratios. It is not a variation of octave-based tuning but a fundamentally different structural choice."

- question: "Analyzing a microtonal piece requires rebuilding theoretical concepts — interval classes, set equivalences, transposition operators — specific to that system's step count."
  type: true-false
  answer: true
  explanation: "In 12-TET, the interval class of a tritone is 6 (out of 12 possible pitch classes), and the transposition operator T_n cycles through 12 steps. In 19-ET, every interval has a different class number out of 19, and what was a 'tritone' (6 semitones in 12-TET) has no direct equivalent. Set-class equivalences, inversional symmetry, and prime forms are all relative to the modular structure of the specific system. You cannot import 12-TET pitch-class theory into 19-ET or 31-ET without rebuilding it."

- question: "A microtonal piece composed in 24-TET (quarter-tone tuning) can be analyzed using standard 12-TET pitch-class theory, since 12-TET is simply a subset of 24-TET."
  type: true-false
  answer: false
  explanation: "While 12-TET pitches do appear within 24-TET (every other step), the harmonic structure of a 24-TET composition includes intervals that have no 12-TET equivalents (quarter tones), and the equivalence classes, consonance hierarchies, and voice-leading norms are defined within the 24-step system. Using 12-TET theory to analyze a work that exploits quarter-tone intervals misses what is structurally essential to those intervals — it would be like analyzing functional tonal harmony with only pentatonic theory."

- question: "Why does moving from 12-TET to a different equal-temperament system (such as 31-ET) require rebuilding music-theoretical concepts from scratch, rather than simply adjusting interval sizes?"
  type: short-answer
  answer: "In any n-ET system, the theoretical concepts — interval classes, inversional equivalence, set classes, transposition operators — are defined relative to the modular arithmetic of n pitch classes. In 12-TET, mod-12 arithmetic defines which intervals are equivalent, what counts as an inversion, and how set classes are catalogued. In 31-ET, this becomes mod-31 arithmetic: intervals that were equivalent in 12-TET (like the tritone and its inversion) are now distinct, new approximations to just intervals (like the harmonic seventh) become available, and the entire structure of consonance and equivalence reorganizes. The grammar is not stretched — it is rewritten."
  explanation: "An analogy: switching from a 12-hour clock to a 31-hour clock doesn't just change the spacing between hours — it changes which times are equivalent (mod 12 vs mod 31) and therefore the entire structure of time-keeping relationships."
```

## Explainer

You already understand **just intonation**: tuning intervals to small-integer ratios (perfect fifth = 3:2, major third = 5:4) to achieve acoustically pure intervals with minimal beating. The problem is that pure intervals in one key create wolf intervals in others, which is why 12-tone equal temperament (12-TET) divides the octave into 12 equal logarithmic steps and accepts small deviations from just ratios in exchange for full transposability. **Microtonal systems** ask a deeper question: what if we treat the tuning system itself as a compositional resource, choosing the octave division for its specific harmonic affordances rather than accepting 12-TET as a neutral default?

In **equal temperament systems** (n-ET), the octave is divided into n equal steps of 1200/n cents each. **19-ET** uses steps of ~63 cents and produces a major third (6 steps = 378 cents) closer to just (386 cents) than 12-TET's 400 cents, along with a very narrow chromatic semitone that gives it a distinctive leading-tone pull. **31-ET** (steps of ~39 cents) approximates just intervals still more accurately — its perfect fifth, major third, and harmonic seventh all fall within 5 cents of just values — and enharmonic equivalents like C# and Db become genuinely distinct pitches separated by a diesis of ~41 cents. Each system supports different harmonic vocabularies: 31-ET opens up extended just-intonation chord structures within an equal-tempered framework, while 19-ET has a natural grammar for chromatic voice-leading.

Systems like **Bohlen-Pierce** break from the octave entirely. Instead of dividing the 2:1 ratio, Bohlen-Pierce divides the **tritave** (3:1) into 13 equal steps. This produces a scale with no conventional octave equivalence but strong consonances built from 3:5:7 ratios — the same odd-integer ratios that dominate the seventh partial of the harmonic series. **Spectral tunings** derive pitch collections directly from the overtone series of a single fundamental, so the intervals match the actual partials produced by a given instrument's timbre. The mathematical tools you need to work with these systems are logarithms (to convert frequency ratios into cents: cents = 1200 × log₂(ratio)) and modular arithmetic (to understand how n-ET step classes wrap around the octave or tritave and define equivalence classes).

Analyzing a piece in a microtonal system requires starting from scratch with interval tables. In 12-TET, a tritone (600 cents) is its own inversion and creates tritone-substitution equivalences. In 31-ET, the tritone and its complement are distinct, and the system contains approximations of 7-limit intervals (7:4 ≈ 969 cents, 7:6 ≈ 267 cents) absent from 12-TET. Voice-leading, harmonic roots, and set-class equivalences all depend on the step size of the system you are in. The theoretical apparatus — interval classes, transposition, inversion, prime forms — must be rebuilt relative to the system's modular structure. This is what makes microtonal analysis genuinely different from retuning 12-TET music: the harmonic logic is not just stretched or compressed, it is structurally reorganized.

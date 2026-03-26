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
- id: graphic-notation-interpretation
  type: soft
tags:
- tuning
- temperament
- acoustics
- intonation
stage: expert
status: validated
---
# Tuning Systems and Temperament

## Core Idea
Different tuning systems (just intonation, Pythagorean, equal temperament, meantone, and non-Western systems) produce different sonorities and harmonic relationships; understanding these distinctions explains compositional choices and performance practice in different musical traditions. Contemporary microtonality deliberately exploits these alternative tuning systems for new expressive and structural possibilities.

## Questions

```yaml
- question: "A lutenist performing a piece in Eb major on a meantone-tuned instrument notices that several chords sound unusually harsh and dissonant — almost unplayable. The most accurate explanation is:"
  type: multiple-choice
  options:
    - "The lute is physically out of tune and needs restringing"
    - "Meantone temperament allocates its compromises unevenly across keys: common keys get near-pure thirds, while remote keys like Eb major receive extremely wide or 'wolf' intervals"
    - "Eb major is inherently more dissonant than other keys due to the number of flats it contains"
    - "Meantone temperament was only designed for keyboard instruments and cannot be used on lutes"
  answer: 1
  explanation: "Meantone temperament is a deliberate tradeoff: it narrows the fifths just enough to produce near-pure major thirds in the most commonly used keys (roughly those with few sharps or flats). This comes at a cost — the remaining 'wolf' intervals, typically concentrated in remote keys, are extremely wide or out of tune. A piece in Eb major, requiring notes far around the circle of fifths, will encounter these wolf intervals. Equal temperament solved this by distributing the impurity evenly across all keys, making all of them equally (slightly) impure rather than some pure and others unplayable."

- question: "The Pythagorean comma arises because:"
  type: multiple-choice
  options:
    - "The major third and the minor third do not add up to a perfect fifth"
    - "Stacking twelve pure perfect fifths (3:2 each) produces a pitch that is slightly higher than seven pure octaves (2:1 each)"
    - "Equal temperament uses irrational frequency ratios that never exactly repeat"
    - "The octave ratio (2:1) is incommensurable with the perfect fourth ratio (4:3)"
  answer: 1
  explanation: "(3/2)^12 = 531441/4096 ≈ 129.746, while 2^7 = 128. If the circle of fifths truly closed, twelve pure fifths would equal seven octaves — but they don't. The Pythagorean comma (≈ 1.01364, or about 23.5 cents) is this gap. Every tuning system must deal with it: Pythagorean tuning leaves the comma in one wide third, meantone spreads it through the thirds, equal temperament distributes it equally across all twelve fifths by making each fifth exactly 700 cents (2 cents narrower than the pure 701.96 cents)."

- question: "In equal temperament, most musical intervals except the octave are tuned to pure frequency ratios, which is why equal temperament produces the most consonant chords of any tuning system."
  type: true-false
  answer: false
  explanation: "This is the opposite of the truth. Equal temperament tunes all intervals (except the octave) to slightly impure ratios — the semitone is exactly 2^(1/12), an irrational number that matches no simple integer ratio. A pure perfect fifth is 3:2 = 1.5 exactly; the equal-tempered fifth is 2^(7/12) ≈ 1.4983, about 2 cents flat. This slight impurity is the price of universal transposability. Systems like just intonation and meantone produce purer (more consonant) intervals in their favored keys — equal temperament is the compromise that makes all keys equally (slightly) impure."

- question: "A pure perfect fifth (frequency ratio 3:2) and an equal-tempered perfect fifth (2^(7/12)) have different frequency ratios, meaning they are slightly different in pitch."
  type: true-false
  answer: true
  explanation: "2^(7/12) ≈ 1.49831, while 3/2 = 1.5 exactly. The difference is about 1.96 cents — less than 2% of a semitone and below the threshold of casual perception, but real and measurable. A cent is defined as 2^(1/1200), so 1200 × log₂(3/2) ≈ 701.96 cents for the pure fifth versus exactly 700 cents for the equal-tempered fifth. This 2-cent discrepancy is exactly 1/12 of the Pythagorean comma, distributed equally across all twelve fifths in the circle."

- question: "Why is it mathematically impossible to construct a 12-note octave-repeating tuning system in which all intervals are tuned to pure frequency ratios (exact small-integer ratios)?"
  type: short-answer
  answer: "Pure frequency ratios involve powers of different prime numbers (2 for octaves, 3 for fifths, 5 for major thirds), and no power of 3/2 ever equals a power of 2 — these are incommensurable. The Pythagorean comma shows this: (3/2)^12 ≠ 2^7. Similarly, (5/4)^3 ≠ 2 (three pure major thirds don't make an octave). Because the frequency ratios corresponding to different interval types belong to different prime factorizations, they cannot all be simultaneously pure within a fixed set of 12 notes."
  explanation: "This is ultimately a number-theoretic fact. The frequency of a note in a scale is determined by a chain of interval ratios from the starting pitch. If every interval in that chain must be a ratio of small integers, the only way all intervals can be pure simultaneously is if the intervals' ratios are commensurate — powers of the same base. But the octave (2:1), fifth (3:2), and major third (5:4) involve different prime factors (2, 3, 5) that are multiplicatively independent. No matter how many notes you add, you cannot make all these intervals simultaneously pure. This is why every tuning system is a compromise, and why the problem has fascinated mathematicians and musicians for centuries."
```

## Explainer

From your study of pitch and frequency you know that musical intervals correspond to frequency ratios: an octave is a 2:1 ratio, a perfect fifth is 3:2, a major third is 5:4. These **pure ratios** arise from the overtone series — the natural harmonics that sound objects produce — and they are what the ear perceives as maximally consonant. A tuning system is a decision about which frequency ratios to use for the notes of a scale. The problem is that pure ratios are mathematically incompatible with each other at scale, and every tuning system is a different compromise.

Here is the fundamental conflict, which your knowledge of logarithms and rational numbers will help you see precisely. Stack twelve perfect fifths (each 3:2): you move upward by (3/2)^12. Stack seven octaves (each 2:1): you move upward by 2^7 = 128. If the circle of fifths truly closed — if twelve fifths equaled seven octaves — these two numbers would be equal. But (3/2)^12 = 531441/4096 ≈ 129.746, not 128. The ratio 531441/524288 (≈ 1.01364) is the **Pythagorean comma**: the small gap by which a twelve-fifth stack overshoots seven octaves. Every tuning system is a strategy for distributing this comma across the scale.

**Pythagorean tuning** keeps all fifths pure (3:2) and accepts that the major thirds will be wide — specifically the ratio 81:64 rather than the pure 5:4. This produces a characteristic bright, tense sound for thirds, which suits monophonic melody but creates beating in sustained chords. **Just intonation** instead tunes the major thirds pure (5:4) and accepts that some fifths must be impure. The result is maximally consonant harmony in one key but uneven intervals that make modulation problematic. **Meantone temperament** — dominant from the Renaissance through the Baroque — splits the difference: slightly narrow fifths (each reduced by one quarter of the syntonic comma) produce pure or near-pure major thirds, enabling rich polyphony in common keys while relegating certain remote keys to extreme dissonance.

**Equal temperament** takes the comma and distributes it uniformly: all twelve fifths are slightly narrow by the same amount, making each semitone exactly the twelfth root of 2 (2^(1/12) ≈ 1.05946). Every key is equally in tune — and equally slightly out of tune relative to pure ratios. The logarithm is central here: the **cent** is defined as one hundredth of an equal-tempered semitone, or (2^(1/12))^(1/100) = 2^(1/1200). Any interval can be expressed in cents by taking 1200 × log₂(frequency ratio). A pure perfect fifth is 701.96 cents; an equal-tempered fifth is exactly 700 cents — a difference of less than 2 cents, imperceptible to most listeners but nonzero. Understanding these systems reveals that Western tonal harmony as we know it rests on a practical compromise accepted in the 18th century, and that composers working in microtonality — using intervals between the twelve equal-tempered pitches — are not departing from tradition but returning to its full mathematical richness.

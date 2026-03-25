---
id: tuning-and-intonation-assessment
title: Tuning and Intonation Assessment by Ear
domain: music
course: ear-training
prerequisites:
- id: just-intonation-acoustics
  type: hard
- id: interval-quality-basics
  type: soft
- id: mixed-interval-ear-training
  type: soft
builds-toward:
- spectral-analysis-acoustics
tags:
- tuning-systems
- intonation
- ear-training
- acoustics
stage: advanced
status: validated
---
# Tuning and Intonation Assessment by Ear

## Core Idea
Different tuning systems (just intonation, equal temperament, Pythagorean) produce slightly different interval sizes and overtone relationships. Developing sensitivity to intonation differences trains a refined ear for subtle pitch variations and supports understanding of tuning systems across cultures.

## How It's Best Learned
Compare the same interval played in just intonation versus equal temperament (with synthesizer or tuning software). Listen for the 'purity' of just intervals versus the slight 'beating' of equal temperament intervals. Research and listen to non-Western tuning systems (Indian raag, Arabic maqam) to understand alternative intonation.

## Common Misconceptions
- Thinking equal temperament is 'the correct' tuning; it is a compromise that allows transposition but sacrifices pure intervals.
- Assuming all Western instruments use equal temperament; string players and singers adjust intonation contextually.

## Questions

```yaml
- question: "A string quartet holds a sustained major third chord. One player slightly flattens her upper note toward the pure 5:4 ratio, away from equal temperament. What happens to the sound?"
  type: multiple-choice
  options:
    - "The chord sounds more out of tune, because she is deviating from the equal-temperament standard"
    - "The beating decreases, because her note is moving closer to frequency alignment with the lower pitch"
    - "The beating increases, because any deviation from equal temperament introduces interference"
    - "The sound is unchanged, as beating is determined by room acoustics rather than the players"
  answer: 1
  explanation: "The equal-tempered major third is 14 cents sharp relative to the pure 5:4 ratio. Beating occurs when two frequencies are nearly but not exactly aligned — the more misaligned, the faster the beating. By flattening toward 5:4, the player is moving toward alignment, reducing the beating rate. The common misconception (option A) assumes equal temperament is the standard of 'in tune,' but beating is an acoustic fact about frequency alignment, not a judgment about temperament."

- question: "You hear rapid, harsh beating in a sustained major third played on an organ. This is most consistent with which tuning system?"
  type: multiple-choice
  options:
    - "Just intonation, which tunes major thirds to a pure 5:4 ratio"
    - "Equal temperament, which tunes major thirds 14 cents sharp relative to pure"
    - "Pythagorean tuning, which stacks pure fifths and produces major thirds that are noticeably sharp"
    - "Meantone temperament, which narrows major thirds toward the pure 5:4 ratio"
  answer: 2
  explanation: "Pythagorean tuning generates major thirds via a chain of pure fifths (3:2), producing a major third of 81:64 — about 22 cents sharper than the pure 5:4 ratio of 80:64. This causes rapid, harsh beating in sustained chords. By contrast, just intonation's major third is beatless, equal temperament's is slightly impure (14 cents sharp, slower beating), and meantone deliberately narrows the third toward pure."

- question: "In equal temperament, the perfect fifth is tuned closer to its pure ratio than the major third is to its pure ratio."
  type: true-false
  answer: true
  explanation: "True — the equal-tempered perfect fifth is only about 2 cents flat of the pure 3:2 ratio, which is nearly imperceptible. The equal-tempered major third, however, is about 14 cents sharp of the pure 5:4 ratio — audibly impure in sustained contexts. This asymmetry is why string players and singers often adjust thirds more aggressively than fifths when playing in ensemble."

- question: "Equal temperament is used on all Western instruments because it produces the purest possible intervals."
  type: true-false
  answer: false
  explanation: "False — equal temperament deliberately compromises interval purity in order to allow transposition to any key without re-tuning. Nearly every interval in equal temperament (except the octave) is slightly misaligned from its pure ratio. The system is used on fixed-pitch instruments (pianos, fretted guitars) for practical reasons. String players and singers do not use equal temperament; they adjust intonation contextually toward pure ratios in sustained harmonies."

- question: "Why does equal temperament sacrifice pure interval ratios, and under what musical circumstances might a performer choose to deviate from it?"
  type: short-answer
  answer: "Equal temperament divides the octave into 12 equal semitones so that all keys are equally usable and transposition is possible without re-tuning. This requires slight misalignment of almost every interval from its pure frequency ratio. Performers deviate from equal temperament in sustained harmonies — particularly major thirds and pure fifths — where the beating of tempered intervals is audible. String players, singers, and wind players commonly tune toward just intonation in slow, sustained passages and return to equal temperament for chromatic or quickly moving lines."
  explanation: "The core insight is that there is no single 'correct' tuning — different musical contexts optimize for different priorities. Equal temperament optimizes for transposability; just intonation optimizes for harmonic purity in a given key; Pythagorean tuning optimizes for pure fifths. The skill in ensemble intonation is understanding which intervals matter most in context and adjusting accordingly."
```

## Explainer

You already know from just intonation that pure intervals arise when frequency ratios are simple whole numbers: a perfect fifth is 3:2, a major third is 5:4, an octave is 2:1. These ratios produce intervals that are **beatless** — the overtones of the two notes align perfectly, and the combined sound is smooth and stable. Equal temperament, the tuning system used on most modern keyboards and fretted instruments, slightly misaligns almost every interval from its pure ratio in order to make all twelve keys equally usable. The result is that nearly every interval in equal temperament is slightly "wrong" compared to just intonation — by a small but audible amount.

The audible consequence of this misalignment is **beating** — a slow, regular wavering in the sound that occurs when two nearly-aligned frequencies interfere with each other. When a major third is played in just intonation (ratio 5:4), there is no beating; when played in equal temperament, the third is slightly wider than 5:4, and you hear a subtle cyclic fluctuation in the sustained sound. The faster the beating, the further out of tune the interval is. Learning to hear beating — first in sustained intervals, then in chords, then in melodic playing — is the core skill of intonation assessment. In ensemble playing, string players, singers, and wind players adjust their intonation constantly, pulling toward the pure ratio when playing sustained harmonies. A sensitive ear for beating guides this adjustment.

Different tuning systems represent different compromises. **Pythagorean tuning** stacks perfect fifths (3:2 ratios), producing very pure fifths but notably sharp major thirds — the major third in Pythagorean tuning beats rapidly and sounds harsh in sustained chords. **Just intonation** prioritizes pure major and minor thirds alongside pure fifths, making triads sound beautiful in one key but creating problems when modulating (the same pitch needs to be tuned slightly differently depending on its harmonic context, making fixed-pitch instruments impractical). **Equal temperament** splits the difference: no interval is perfectly pure, but no key is systematically worse than any other. The equal-tempered perfect fifth is only 2 cents (hundredths of a semitone) flat; the equal-tempered major third is 14 cents sharp — audibly impure in sustained contexts.

The broader lesson is that there is no single "correct" tuning — different musical contexts optimize for different priorities. Unaccompanied choral music often gravitates naturally toward just intonation as singers bend toward the pure ratios that feel most consonant. String quartets playing Bach adjust contextually, tuning pure fifths in open-string passages and adjusting thirds in sustained chords. Non-Western tuning systems — Arabic **maqam**, Indian classical music, Javanese **gamelan** — divide the octave in ways that follow entirely different theoretical logic and sound dissonant to ears trained only on equal temperament, yet are internally coherent and expressive within their own frameworks. Developing your intonation assessment by ear means learning to hear these distinctions analytically — understanding *why* something sounds the way it does — rather than defaulting to equal temperament as the neutral benchmark.

---
id: interval-inversion-basics
title: Interval Inversion
domain: music
course: music-theory-fundamentals
prerequisites:
- id: interval-quality-basics
  type: hard
builds-toward:
- voice-leading-smooth-progressions
tags:
- intervals
- transformation
stage: formal-systems
status: validated
---

# Interval Inversion

## Core Idea
An inverted interval is created by moving the lower note up an octave or the upper note down an octave. Inverted intervals follow predictable rules: unison inverts to an octave, a second to a seventh, a third to a sixth, and so on; major becomes minor and vice versa, while perfect remains perfect.

## How It's Best Learned
Play intervals and their inversions on an instrument, identify them on a staff, and verify the complementary relationship using the nine-semitone rule.

## Common Misconceptions
Interval inversion is not the same as playing the notes in reverse order—the actual pitches (which note is higher) must swap.

## Questions

```yaml
- question: "What interval is produced by inverting a major sixth?"
  type: multiple-choice
  options:
    - "A major third"
    - "A minor third"
    - "A perfect fourth"
    - "A minor sixth"
  answer: 1
  explanation: "Apply both inversion rules. Size: 9 − 6 = 3, so the inverted interval is a third. Quality: major inverts to minor. Result: a minor third. A common error is to apply only one rule — getting the size right but keeping 'major' (producing the wrong answer 'major third'), or forgetting the size rule entirely. Both rules must be applied simultaneously."

- question: "A student claims that C–E (a major third) and E–C are the same interval because they use the same two notes. Another student says E–C is a minor sixth. Which student is correct, and what principle does this illustrate?"
  type: multiple-choice
  options:
    - "The first student — C–E and E–C are both major thirds since the notes are the same"
    - "The second student — E–C is a minor sixth, because inverting a major third yields a minor sixth (9−3=6, major→minor)"
    - "Both are correct — major and minor are interchangeable descriptions of the same pitch relationship"
    - "Neither — E–C is a diminished sixth because the lower note changed"
  answer: 1
  explanation: "Interval inversion changes both the size and quality of the interval. C up to E is a major third (4 semitones). E up to C spans 9 semitones — a minor sixth. The inversion rules confirm this: 9 − 3 = 6 (sixth), major → minor. The two students are not describing the same thing: 'using the same notes' does not mean 'same interval,' because interval identity depends on which note is lower."

- question: "A perfect fifth inverts to a perfect fourth, and together their sizes sum to nine."
  type: true-false
  answer: true
  explanation: "5 + 4 = 9 ✓. The quality rule confirms it: perfect inverts to perfect, so perfect fifth → perfect fourth. This can be verified directly: C up to G is a perfect fifth (7 semitones); G up to C is a perfect fourth (5 semitones); 7 + 5 = 12 = one octave, consistent with the two notes together spanning exactly an octave after one is flipped."

- question: "Inverting an interval means playing the notes in the opposite order — for instance, naming C–G as G–C while keeping C in the lower register."
  type: true-false
  answer: false
  explanation: "Inversion requires one note to change octave so that the originally lower note becomes the higher note (or vice versa). Simply reversing the naming order of C–G to G–C, while still having C below G, does not change the interval at all — it is still a perfect fifth. Inversion means the lower note moves up an octave (or the upper note moves down an octave), so the two notes switch their vertical relationship. This is the misconception noted in the topic: reversal of order is not the same as inversion."

- question: "Explain why inverted interval sizes always sum to nine. What property of the octave makes this relationship inevitable?"
  type: short-answer
  answer: "When you invert an interval, one note moves by an octave (8 letter-name steps). Since the original interval spans some number of steps s, and the inverted interval spans the remaining steps within that octave, the two intervals together cover exactly one octave's worth of scale steps. In terms of letter names, one octave spans 8 steps (C to C = 1, D = 2, ..., C = 8), and the original and inverted intervals partition those 8 steps with a shared endpoint — giving sizes that sum to 9 (because each endpoint is counted once in each interval). For example, C to E is a third (C=1, D=2, E=3); E to C is a sixth (E=1, F=2, G=3, A=4, B=5, C=6); 3 + 6 = 9."
  explanation: "The 'sum to nine' rule is not arbitrary — it reflects the structure of the diatonic octave. Understanding why it works makes it memorable and lets you apply it confidently in any context, rather than memorizing it as an isolated fact."
```

## Explainer

From your study of intervals, you know how to measure the distance between two notes: count the letter names from bottom to top, and adjust the quality (perfect, major, minor, augmented, diminished) based on the exact semitone count. **Interval inversion** asks a specific question: what happens to an interval when you flip it — when the lower note becomes the higher note, or the higher note becomes the lower? The answer follows two clean rules that reward understanding rather than memorization.

The first rule governs **size**: inverted intervals always sum to nine. A second inverts to a seventh (2 + 7 = 9). A third inverts to a sixth (3 + 6 = 9). A fourth inverts to a fifth (4 + 5 = 9). A unison inverts to an octave (1 + 8 = 9). This is not a coincidence — it follows from the fact that the two notes together span exactly an octave (8 half-steps) once one of them flips. You can verify this with any example: if you take a major second (C up to D), and move the C up an octave (now D up to C), you have a minor seventh. Count the semitones: D to C spans 10 semitones — a minor seventh. The size rule gives you 9 minus 2 = 7, and the quality rule gives you the "minor."

The second rule governs **quality**: major becomes minor, and minor becomes major. Perfect stays perfect. This is because inverting a major interval removes exactly those extra semitones that made it major rather than minor, and vice versa. Perfect intervals — unisons, fourths, fifths, octaves — have a symmetrical internal structure that survives inversion intact. (Augmented inverts to diminished, and vice versa, by the same logic.) Together the two rules give you the complete answer in one step: a major third (size 3, quality major) inverts to a minor sixth (size 9 − 3 = 6, quality minor).

Why does this matter? In **voice leading** — the art of connecting chords smoothly — understanding inversion is essential because the same two notes can appear in two different arrangements. The interval from C to G is a perfect fifth; flip it and you have G to C, a perfect fourth. Both use C and G, but they place the tension differently in a chord voicing. A composer choosing between root position and first inversion of a triad is partly choosing between different intervals ringing against the bass. Knowing how intervals invert lets you see these choices as related — different angles on the same pitch relationship rather than unrelated events.

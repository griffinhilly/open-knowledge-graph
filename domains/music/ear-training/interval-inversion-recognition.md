---
id: interval-inversion-recognition
title: Interval Inversion Recognition by Ear
domain: music
course: ear-training
prerequisites:
- id: interval-inversion
  type: hard
- id: interval-recognition-by-ear
  type: hard
builds-toward:
- invertible-counterpoint-advanced
- contrapuntal-composition
tags:
- intervals
- ear-training
- inversion
- pitch-relationships
stage: formal-systems
status: validated
---

# Interval Inversion Recognition by Ear

## Core Idea
Interval inversions (e.g., a major third becomes a minor sixth) have different interval qualities and sound characteristics. Recognizing inversions by ear develops deeper understanding of interval relationships and supports contrapuntal and harmonic analysis.

## How It's Best Learned
Play an interval and then its inversion immediately after, noting the change in quality and sound. Create a reference chart: seconds invert to sevenths, thirds to sixths, fourths to fifths. Practice identifying interval inversions in isolated form and within voice-leading progressions.

## Common Misconceptions
- Thinking inversions produce the same quality interval; a major third inverts to a minor sixth, not another major third.
- Confusing compound intervals with simple inversions; compound intervals add an octave.

## Questions

```yaml
- question: "A major sixth (M6) is inverted. What interval does it become?"
  type: multiple-choice
  options:
    - "Minor sixth (m6)"
    - "Major third (M3)"
    - "Minor third (m3)"
    - "Perfect fifth (P5)"
  answer: 2
  explanation: "Interval inversion follows two rules: the size numbers sum to 9 (6 + 3 = 9), and major inverts to minor (and vice versa). So a major sixth inverts to a minor third. The common error is option B — choosing major third — which gets the size right (9 − 6 = 3) but forgets that quality flips: major becomes minor. Perfect intervals stay perfect (P4 ↔ P5), major ↔ minor, augmented ↔ diminished."

- question: "A student hears a major third (C up to E) played, then hears the inversion voiced as a simple interval within an octave. What should she recognize?"
  type: multiple-choice
  options:
    - "A major sixth — inversions of major intervals are always major"
    - "A minor sixth — because major inverts to minor and 3 + 6 = 9"
    - "A perfect fourth — because C and E are a fourth apart when rearranged"
    - "A minor third — the same quality but a larger interval"
  answer: 1
  explanation: "A major third inverts to a minor sixth: 3 + 6 = 9 (size rule), and major → minor (quality rule). Option A gets the size right but forgets the quality flip — a major interval does not invert to another major interval. The quality flip from major to minor is the key recognition skill: the minor sixth has a distinctly more open, expansive sound than the compact major third that preceded it."

- question: "Inverting a minor interval usually produces another minor interval."
  type: true-false
  answer: false
  explanation: "Inverting a minor interval produces a MAJOR interval (e.g., minor third → major sixth; minor second → major seventh). The quality-flip rule states: major ↔ minor, augmented ↔ diminished, and perfect ↔ perfect. Only perfect intervals invert to the same quality. This is one of the most important rules of interval inversion and the most common source of error: students expect quality to be preserved and are surprised to find it changes."

- question: "The interval numbers of an interval and its inversion always sum to 9."
  type: true-false
  answer: true
  explanation: "For simple intervals, the sizes always sum to 9: unison (1) inverts to octave (8), 2nd inverts to 7th, 3rd to 6th, 4th to 5th. 1+8=9, 2+7=9, 3+6=9, 4+5=9. This is because an octave spans 8 diatonic steps, and splitting it into two intervals that together fill an octave always gives pairs summing to 9 (not 8, because both endpoints count the starting note). Memorizing the complementary pairs — 2nds/7ths, 3rds/6ths, 4ths/5ths — is the practical takeaway."

- question: "Why does inverting an interval change its quality (e.g., major to minor), and how does this affect the sound of the inversion compared to the original interval?"
  type: short-answer
  answer: "When you invert an interval by moving the lower note up an octave (or the upper note down an octave), the distance changes and with it the arrangement of half steps. A major third (4 half steps) inverts to a minor sixth (8 half steps): the half-step count is different, producing a different quality. Major intervals have one more half step than the corresponding minor interval, and inversion redistributes those half steps across the octave complement. Sonically, the inversion sounds distinctly different — a minor sixth is more open and expansive than the compact major third."
  explanation: "The quality flip happens because quality is determined by the exact number of half steps, not just the diatonic letter span. When you invert, the half steps that made the interval 'major' get redistributed across the octave. This is why ear training for inversion requires listening for quality, not just size: the two intervals in a complementary pair (e.g., M3 and m6) share no perceptual quality — they sound different and must be recognized as distinct sounds that happen to be mathematically related."
```

## Explainer

From your prerequisite in interval inversion theory, you know the two rules: interval sizes sum to 9 (a third inverts to a sixth, a fourth to a fifth), and quality flips (major becomes minor, augmented becomes diminished, perfect stays perfect). From interval recognition by ear, you can identify intervals as they sound. This topic connects the two: hearing an interval and then hearing its inversion as a **related but distinctly different sound**, building the aural awareness that these mathematically paired intervals share an underlying structure despite sounding nothing alike.

The key ear-training insight is that inversions do **not** sound like their originals. A major third (C up to E) is compact and warm; its inversion, a minor sixth (E up to C), is wide and somewhat plaintive. They contain the same two pitch classes, but the reversal of which note is on top changes the sound character entirely. This is because quality flips when you invert: the four half steps of a major third become the eight half steps of a minor sixth, and the resulting sound is perceptually distinct. Ear training for inversions therefore requires treating each complementary pair (M3/m6, m3/M6, P4/P5, M2/m7, m2/M7) as a pair of **different sounds that you know are mathematically related**, not as two versions of the same sound.

The practical exercise is straightforward but requires repetition to internalize. Play an interval, name it, then immediately play its inversion and name that. The pattern C-E (M3) followed by E-C (m6) trains your ear to hear the shift: the compact warmth opens into a wider, more open sound. Then reverse: play the sixth first and then the third, hearing the contraction. Do this for every complementary pair. Over time, you develop the ability to hear an interval and **predict** what its inversion will sound like before playing it — a skill that directly supports contrapuntal listening, where intervals between voices flip as voices cross registers.

This skill becomes essential in analyzing and hearing **invertible counterpoint**, where a subject and countersubject are designed to work regardless of which voice is on top. When two voices swap registers, every interval between them inverts: a third becomes a sixth, a sixth becomes a third, and a fifth becomes a fourth (which is why perfect fifths between voices require special care in invertible counterpoint — they become fourths, which were treated as dissonances in earlier practice). Hearing interval inversions by ear means you can follow the contrapuntal logic of a fugue or invention even when voices exchange registers, recognizing the same intervallic relationships in their inverted form rather than losing the thread when the voices cross.

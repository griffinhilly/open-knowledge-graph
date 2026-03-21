---
id: voice-leading-parallel-fifths-octaves
title: 'Voice Leading: Avoiding Parallel Fifths and Octaves'
domain: music
course: music-theory-fundamentals
prerequisites:
- id: voice-leading-basics
  type: hard
- id: interval-quality-basics
  type: soft
builds-toward:
- voice-leading-principles
- four-part-writing
tags:
- voice-leading
- parallel-motion
- forbidden-intervals
stage: formal-systems
status: draft
---

# Voice Leading: Avoiding Parallel Fifths and Octaves

## Core Idea
In four-part counterpoint and voice leading, parallel perfect fifths and parallel perfect octaves between any two voices are generally avoided because they reduce harmonic independence and create a hollow sound. Direct fifths (also called direct motion to a perfect fifth or octave) are sometimes allowed. This rule develops clear harmonic texture and independent voice motion.

## How It's Best Learned
Write four-part progressions and listen for parallel perfect intervals. Study Bach chorales and other chorale examples to see how composers navigate voice leading while respecting this constraint.

## Common Misconceptions
- Thinking parallel fifths or octaves are always absolutely forbidden (they can occasionally be used for effect).
- Not recognizing that parallel thirds and sixths are acceptable and even desirable for smooth voice leading.

## Questions

```yaml
- question: "In four-part writing, the soprano moves from C5 to D5 while the bass moves from G3 to A3 simultaneously. Is this a voice-leading violation?"
  type: multiple-choice
  options:
    - "No — the voices are moving in different octaves, so the interval doesn't apply"
    - "No — only inner voices are subject to the parallel fifths rule"
    - "Yes — C-G and D-A are both perfect fifths, and moving through them in parallel reduces harmonic independence"
    - "Yes — any parallel motion in contrary registers is prohibited"
  answer: 2
  explanation: "C to G is a perfect fifth, and D to A is also a perfect fifth. When two voices move in parallel motion through two consecutive perfect fifths, this is a parallel fifths violation — regardless of which octave the voices occupy. The prohibition applies to all six pairings in four-part writing (S-A, S-T, S-B, A-T, A-B, T-B), not just inner voices. The acoustic reason is that these voices begin to fuse rather than sound independent."

- question: "A student argues: 'Parallel thirds and parallel fifths are essentially the same — both are just two voices moving in the same direction by the same interval size, so they should have the same effect.' How would you evaluate this argument?"
  type: multiple-choice
  options:
    - "Correct — parallel motion of any interval tends to weaken voice independence equally"
    - "Incorrect — parallel thirds blend warmly without fusing voices, while parallel fifths cause acoustic fusion that destroys independence; the rule is specific to perfect intervals"
    - "Incorrect — parallel thirds are actually more problematic because thirds are closer together"
    - "Correct — both are avoided in strict counterpoint for the same acoustic reason"
  answer: 1
  explanation: "The student's argument confuses parallel motion (same direction) with acoustically identical effects. Parallel thirds (ratio approximately 5:4) and sixths blend pleasantly but do not fuse — the two voices remain perceptually distinct. Parallel perfect fifths (ratio 3:2) and octaves (2:1) cause the voices to merge acoustically, reducing four-part texture to fewer effective voices. The rule targets perfect consonances specifically because of their strong overtone relationships, not all parallel motion."

- question: "Parallel octaves between the soprano and bass are a voice-leading error, but parallel octaves between inner voices (alto and tenor) are generally acceptable in four-part writing."
  type: true-false
  answer: false
  explanation: "Parallel octaves (and parallel perfect fifths) are prohibited between any pair of voices in four-part writing — not just the outer voices. All six pairings (S-A, S-T, S-B, A-T, A-B, T-B) must be checked. The soprano-bass pair is most audible and most commonly cited, which may create the impression the rule is limited to outer voices, but inner-voice parallel octaves also collapse two voices into one and are equally forbidden in strict counterpoint."

- question: "The acoustic reason parallel perfect fifths reduce harmonic independence is that the 3:2 frequency ratio of a perfect fifth causes two voices moving in parallel through such intervals to fuse perceptually rather than remain distinct."
  type: true-false
  answer: true
  explanation: "This is the underlying acoustic principle. Perfect fifths and octaves are the strongest consonant intervals in the overtone series. When two voices maintain a perfect fifth or octave while moving in parallel, the overtone relationship between them is so strong that the ear begins to merge them into a single, distinctive sound — a hollow medieval drone quality. This acoustic fusion is what reduces the harmonic independence that four-part writing depends on."

- question: "Why are parallel thirds acceptable in voice leading when parallel perfect fifths are not? What acoustic property distinguishes them?"
  type: short-answer
  answer: "Parallel thirds blend warmly but do not cause acoustic fusion — the two voices remain perceptually distinct because thirds (frequency ratio approximately 5:4) do not have the same overtone-series dominance as perfect fifths (3:2) or octaves (2:1). Perfect fifths and octaves are the intervals most strongly reinforced by the natural overtone series, so when two voices move in parallel through them, the ear merges them. Thirds and sixths lie further from this perfect alignment; they blend without fusing, allowing each voice to retain its identity."
  explanation: "The rule is not about avoiding parallel motion in general — parallel thirds and sixths are actually desirable for smooth harmonization. The rule is specifically about intervals that cause acoustic fusion: perfect consonances with the simplest frequency ratios. Understanding the acoustic basis explains why parallel thirds are a standard technique (used throughout folk and classical music to harmonize melodies) while parallel fifths hollow out the texture."
```

## Explainer

You have already worked with voice-leading basics and intervals, so you know that four-part writing involves distributing four voices — soprano, alto, tenor, bass — that move from one chord to the next in smooth, independent lines. The rule against parallel perfect fifths and octaves exists because of what happens acoustically when two voices move in parallel through those specific intervals: they begin to fuse rather than sound independent. Two voices a perfect fifth apart moving in parallel are not heard as two distinct lines — the overtone relationship between them is so strong that the ear starts to merge them into a single sound with unusual tonal color. The result is a **hollow** quality that empties out the texture rather than enriching it.

The acoustic explanation connects to the overtone series, which is your prerequisite's background knowledge. A perfect fifth (frequency ratio 3:2) is the second-strongest consonant interval after the octave (2:1). When two voices move in parallel octaves, they collapse into a single pitch heard at different registers — you effectively lose a voice entirely. When two voices move in parallel fifths, they fuse into something that sounds like a single medieval drone rather than two independent harmonic lines. Both effects reduce the harmonic information conveyed by four-part writing, which is why trained composers since the Renaissance systematically avoided them when writing in the contrapuntal tradition.

Parallel thirds and sixths work differently. These intervals (ratios 5:4 and 5:3 or 6:5) blend pleasantly but do not fuse acoustically in the same way. You can run parallel thirds between soprano and alto through an entire passage and the two voices remain distinct, each contributing its own color to the harmony. This is why **parallel thirds** are a staple technique for harmonizing melodies: hymns, folk arrangements, and classical first themes commonly double the top voice a third below to fill out the texture warmly. The rule is specific to perfect intervals — it is not a general prohibition on parallel motion.

In practice, spotting parallel fifths and octaves requires keeping track of all six pairings in four-part writing (S-A, S-T, S-B, A-T, A-B, T-B) simultaneously. The common errors occur at the outer voices (soprano and bass) because students focus on those more than inner voice pairs. The fix is usually to use **contrary motion** — move one voice up while the other moves down — or **oblique motion** — hold one voice stationary while the other moves. Bach chorales are the canonical training corpus: every measure demonstrates how to navigate smooth voice leading while keeping voices genuinely independent, and the occasional exceptions (for special effects or in particular stylistic contexts) reveal what the rule actually protects against.


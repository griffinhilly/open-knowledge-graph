---
id: interval-inversion
title: Interval Inversion
domain: music
course: music-theory-fundamentals
prerequisites:
- id: interval-quality-basics
  type: hard
builds-toward:
- chord-inversions
- voice-leading-basics
tags:
- intervals
- inversion
stage: formal-systems
status: validated
---

# Interval Inversion

## Core Idea
When an interval is inverted (the lower note moves up an octave), the interval name and quality change predictably. Generic names add to 9 (a 3rd inverts to a 6th). Quality inversions follow a pattern: major becomes minor, perfect stays perfect, augmented becomes diminished. Understanding inversion is crucial for voice leading.

## How It's Best Learned
Practice inverting intervals on staff and keyboard, observing name and quality changes. Listen to inverted intervals and hear how sound differs while maintaining the same pitch classes. Memorize quality inversion rules.

## Common Misconceptions
Inverted intervals sound completely different (they share pitch content). Perfect intervals don't stay perfect when inverted (they do). Miscounting generic interval names after inversion.

## Questions

```yaml
- question: "What is the inversion of a major 6th?"
  type: multiple-choice
  options:
    - "A major 3rd — quality stays the same, size inverts"
    - "A minor 3rd — size changes (6+3=9), quality flips from major to minor"
    - "A perfect 5th — quality becomes perfect when inverted"
    - "An augmented 4th — the tritone is the inversion of a major 6th"
  answer: 1
  explanation: "Apply both rules. Generic size: 6 + ? = 9, so ? = 3 — it becomes a 3rd. Quality: major inverts to minor. Therefore a major 6th inverts to a minor 3rd. Option A fails to apply the quality-flip rule. The sum-to-9 rule and quality-flip rules must both be applied together; neither alone gives the correct answer."

- question: "A melody and bass note are a perfect 5th apart, with the melody on top. The bass note is moved up an octave so it is now above the melody. What interval do they now form?"
  type: multiple-choice
  options:
    - "A perfect 5th — 'perfect stays perfect' means the size is also preserved"
    - "A perfect 4th — size changes (5+4=9) but quality stays perfect"
    - "An augmented 4th — inverting a 5th produces the tritone"
    - "A diminished 5th — quality flips when the voices cross"
  answer: 1
  explanation: "Option A is the classic trap: 'perfect stays perfect' refers to the quality (the word 'perfect'), not the numeric size. The size still changes by the sum-to-9 rule: 5 + 4 = 9, so a 5th inverts to a 4th. Since perfect quality is preserved under inversion, a perfect 5th inverts to a perfect 4th. The rule is: number changes (add to 9), quality follows its own pattern (major↔minor, perfect stays, aug↔dim)."

- question: "An inverted interval contains the same two pitch classes as the original interval, just with their registers swapped."
  type: true-false
  answer: true
  explanation: "Inversion moves one note by exactly one octave — no new pitches are introduced. If the original interval is C up to E (a major 3rd), the inversion E up to C (a minor 6th) still involves only C and E. This shared pitch-class content is why inverted intervals have a sonic connection and why theorists in some contexts treat an interval and its inversion as related — they literally contain the same notes, just voiced differently."

- question: "The inversion of a major 2nd is a major 7th."
  type: true-false
  answer: false
  explanation: "The size rule is correct: 2 + 7 = 9, so a 2nd inverts to a 7th. But the quality flips: major inverts to minor, not major. A major 2nd inverts to a minor 7th. A student who remembers the sum-to-9 rule but forgets the quality-flip will make exactly this error. To get the full answer, both rules must be applied: size follows the sum-to-9, and quality follows the major↔minor / perfect↔perfect / aug↔dim pattern."

- question: "A student says 'interval inversion just flips the interval upside down, so the two sounds are completely unrelated.' What's right and what's wrong about this?"
  type: short-answer
  answer: "The student is right that the interval is flipped — one note moves an octave, changing which is on top. But wrong that the sounds are completely unrelated. An inverted interval shares the exact same two pitch classes as the original; only the voicing changes. A major 3rd (C–E) and its inversion, a minor 6th (E–C), both contain C and E — they are closely related in pitch content despite sounding different."
  explanation: "The misconception that inversions are unrelated sounds prevents understanding of why chord inversions are considered variants of the same chord rather than entirely different harmonies. The sum-to-9 and quality-flip rules tell you precisely how the interval name changes, but the preservation of pitch-class content is what ties the original and its inversion together sonically and functionally. This connection is foundational for understanding voice leading and counterpoint."
```

## Explainer

You've already learned to measure intervals — to identify both the generic size (second, third, fourth, etc.) and the quality (major, minor, perfect, augmented, diminished) of the distance between two notes. Inversion asks a different question: what happens when you flip an interval? Specifically, when you take the **lower note** of an interval and move it up an octave — or equivalently, take the upper note down an octave — you produce the **inversion** of that interval. The same two pitch classes remain involved; only which sits on top has changed.

The generic size of an interval and its inversion always **sum to 9**. This single fact is the key to inversion: a 2nd inverts to a 7th (2 + 7 = 9), a 3rd inverts to a 6th (3 + 6 = 9), a 4th inverts to a 5th (4 + 5 = 9). The rule works because an octave spans 8 generic scale steps, and when you flip an interval, the two resulting pieces must together cover an octave — but interval counting counts both endpoints, which adds the extra 1. Quality changes follow their own predictable pattern: **major becomes minor** (and minor becomes major), **perfect stays perfect**, **augmented becomes diminished** (and diminished becomes augmented). So a major 3rd (C up to E) inverts to a minor 6th (E up to C). A perfect 5th (C up to G) inverts to a perfect 4th (G up to C). An augmented 4th inverts to a diminished 5th — which is the tritone relationship, symmetric and self-inverting in quality.

Why does this matter? Because in four-voice writing and voice leading, chords appear in different **inversions** (a term that extends directly from interval inversion), and the intervals between voices shift depending on which chord tone is in the bass. Understanding how interval quality changes when voices flip helps you predict and control the sound of progressions. When composers write counterpoint, they frequently use **contrary motion** — voices moving in opposite directions — which naturally produces inverted intervals from one beat to the next. Recognizing that a major 6th and a minor 3rd are inversions of each other explains why they feel like mirror images: they contain exactly the same pitch classes, just reordered in register.

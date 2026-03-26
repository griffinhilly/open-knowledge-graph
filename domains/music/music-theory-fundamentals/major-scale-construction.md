---
id: major-scale-construction
title: Major Scale Construction
domain: music
course: music-theory-fundamentals
prerequisites:
- id: intervals-basics
  type: hard
- id: note-names-and-octaves
  type: hard
builds-toward:
- major-scales
- key-signatures
- diatonic-harmony
tags:
- scales
- construction
- whole-half
- intervals
stage: formal-systems
status: validated
---

# Major Scale Construction

## Core Idea
Every major scale follows the same pattern of whole steps and half steps: W-W-H-W-W-W-H. Starting from any pitch and applying this interval pattern produces a major scale—the seven-pitch collection that forms the basis of tonal music. Understanding this pattern lets you construct any major scale.

## How It's Best Learned
Start with C major and identify the W-H pattern. Build major scales from different roots and verify each interval. Listen to major scales to recognize the pattern by ear.

## Common Misconceptions
All major scales don't have the same pitches—only C major uses all naturals. The pattern is based on intervals, not alphabet positions. Misremembering the W-H sequence.

## Questions

```yaml
- question: "You are building a major scale starting on G. You reach the 7th scale degree and the W-W-H-W-W-W-H pattern requires a whole step from the 6th degree (E). Which note must you use?"
  type: multiple-choice
  options:
    - "F natural, because major scales should use as many natural notes as possible"
    - "F♯, because the pattern requires a whole step from E, and F natural is only a half step above E"
    - "Either F or F♯ — the choice is left to the performer's preference"
    - "F♯ only when playing in a sharp key; F natural when playing in a flat key"
  answer: 1
  explanation: "E to F natural is a half step (they are adjacent semitones). The W-W-H-W-W-W-H pattern requires a whole step between scale degrees 6 and 7, so F must be raised to F♯ to produce the required whole step (E to F♯ = 2 semitones). The sharp is not optional — it is required by the interval pattern. Deviating from the pattern would produce a different scale quality, not G major."

- question: "A melody written in C major is transposed to G major. Why does the transposed melody sound like 'the same melody'?"
  type: multiple-choice
  options:
    - "Because both scales use mostly white keys on the piano"
    - "Because the interval relationships between consecutive notes are preserved — the internal structure of the scale is identical"
    - "Because both melodies are in the same register and tempo"
    - "Because C and G are closely related keys and share many of the same pitches"
  answer: 1
  explanation: "Transposition preserves all intervallic relationships within the melody. Since every major scale has the identical W-W-H-W-W-W-H pattern, the distance between any two scale degrees is the same in C major and G major. The melody's shape — the sequence of ups and downs, steps and leaps — is entirely preserved; only the absolute pitch level changes. This is why the major scale's character comes from its interval pattern, not from any particular set of pitches."

- question: "All major scales share the same interval pattern (W-W-H-W-W-W-H), regardless of their starting note."
  type: true-false
  answer: true
  explanation: "This is the defining property of major scales. The W-W-H-W-W-W-H pattern is what makes a scale 'major' — not which specific pitches it contains. C major, G major, D♭ major, and every other major scale all have this identical internal structure. The pitches differ, and some require sharps or flats, but the pattern of whole and half steps is invariant. A scale with a different interval pattern would be a different scale quality (minor, dorian, etc.)."

- question: "C major is unique among major scales because it is the main one that follows the W-W-H-W-W-W-H pattern without requiring any sharps or flats."
  type: true-false
  answer: false
  explanation: "The statement is almost right, but contains a critical error: C major is NOT unique because it follows a different pattern — ALL major scales follow the same W-W-H-W-W-W-H pattern. C major is simply the one that happens to land on all natural notes when applied starting from C. Other major scales require sharps or flats to maintain the same pattern starting from different roots. The pattern is universal; the all-natural coincidence of C major is a consequence of where C sits on the chromatic scale."

- question: "Why are sharps or flats required when constructing major scales that start on notes other than C?"
  type: short-answer
  answer: "The W-W-H-W-W-W-H pattern specifies exact distances in semitones between adjacent scale degrees. Starting from any note other than C, applying these distances will eventually land on a note that is a semitone away from the next natural letter name when a whole step is required, or on a note that is a whole step away when only a half step is needed. Raising or lowering those notes by a half step (with a sharp or flat) corrects the distance to match the required pattern. The accidentals are not adjustments to a 'standard' — they are the result of faithfully applying the universal interval template to a different starting pitch."
  explanation: "G major, for example, reaches F when the 7th scale degree should be a whole step above E. Since E to F is only a half step, F must become F♯. This is not a stylistic choice; it is mathematically required by the interval pattern. The key signature system codifies which accidentals are required for each major scale."
```

## Explainer

You have learned about intervals — the specific distances between pitches — and you know how to name notes across octaves. The **major scale** is the first systematic application of both skills: a procedure that takes any starting note and produces the characteristic seven-pitch collection that defines major-key tonal music. The recipe is a fixed interval pattern: **W-W-H-W-W-W-H** (whole step, whole step, half step, whole step, whole step, whole step, half step). Apply this pattern starting from any pitch, and you get a major scale.

The easiest place to start is **C major**, because the W-W-H-W-W-W-H pattern lands exactly on the white keys of a piano: C-D-E-F-G-A-B-C. Between C and D is a whole step (two semitones), D to E is a whole step, E to F is a half step (they are adjacent white keys with no black key between them), and so on. This is why C major is typically taught first — there are no accidentals to manage. But the rule is not "use white keys." The rule is the interval pattern. When you start on G instead: G-A-B-C-D-E-F♯-G. The F must become F♯ to maintain the whole step between E and the sixth degree, and the half step between the seventh degree (F♯) and the octave (G). The sharp is not optional — it is required by the pattern.

This is the deeper insight: **the major scale's character comes from its interval pattern, not from any particular set of pitches**. Every major scale sounds recognizably "major" because every major scale has the same internal structure — the same arrangement of whole and half steps, regardless of where it starts. This is why a melody transposed from C major to G major sounds like the same melody: the interval relationships between notes are preserved. When you build a scale from D♭, you will need flats to maintain the pattern; when you build from B, you will need sharps. The accidentals are the cost of preserving the template.

This pattern also explains the **key signature system** you will encounter next. Each major scale requires a specific set of sharps or flats to maintain the W-W-H-W-W-W-H pattern, and key signatures encode that information at the start of a piece. Knowing that G major requires F♯, and that D major requires F♯ and C♯, reveals a systematic relationship: each step up on the **circle of fifths** adds one more sharp. The major scale construction procedure is not just an exercise — it is the engine behind the entire key signature system, and understanding it makes every aspect of tonal harmony more intelligible.

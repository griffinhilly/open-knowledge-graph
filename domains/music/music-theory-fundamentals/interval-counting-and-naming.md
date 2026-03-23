---
id: interval-counting-and-naming
title: Interval Counting and Naming
domain: music
course: music-theory-fundamentals
prerequisites:
- id: intervals-basics
  type: hard
- id: note-names-and-octaves
  type: hard
builds-toward:
- interval-quality-basics
- triad-construction-major-minor
- voice-leading-basics
tags:
- intervals
- counting
- naming
stage: formal-systems
status: validated
---

# Interval Counting and Naming

## Core Idea
Intervals are named by counting letter names from the lower note to the upper note, giving each interval its generic name: 2nd, 3rd, 4th, etc. The count includes both starting and ending notes. C to E is a 3rd (C-D-E); C to G is a 5th. This counting system is the foundation for understanding interval quality.

## How It's Best Learned
Practice counting intervals on staff and keyboard, speaking letter names aloud. Start with simple intervals and progress to larger ones. Name intervals before worrying about quality.

## Common Misconceptions
Forgetting to include the starting note in the count. Confusing interval name with the number of semitones (they're different). Miscounting when the interval spans an octave.

## Questions

```yaml
- question: "A student counts the interval from D to G♭ and concludes it is a 3rd because the flat 'brings G closer to F.' What is the correct interval number for D to G♭?"
  type: multiple-choice
  options:
    - "3rd — the flat makes it smaller than a 4th, so it must be a third"
    - "4th — both D to G and D to G♭ have the same generic interval number because accidentals don't change the letter-name count"
    - "Diminished 4th — a special category that counts differently than a normal 4th"
    - "5th — because the flat adds a chromatic step"
  answer: 1
  explanation: "Generic interval names count letter names, not semitones. D to G spans D(1)–E(2)–F(3)–G(4) — four letter names, regardless of whether G has a flat, sharp, or natural. The flat changes the interval's quality (making it a diminished 4th rather than a perfect 4th), but not its number. This is the essential point: accidentals affect quality, not generic size. The student's error is conflating semitone distance with letter-name count."

- question: "How many letter names are spanned by a sixth?"
  type: multiple-choice
  options:
    - "5 — you travel 5 steps to reach the 6th pitch"
    - "6 — you count 6 letter names including both the starting and ending note"
    - "7 — because a sixth spans most of an octave"
    - "4 — because a sixth is the inversion of a third, which spans 3"
  answer: 1
  explanation: "A sixth spans 6 letter names: the starting note counts as 1. From C: C(1)–D(2)–E(3)–F(4)–G(5)–A(6) — a sixth. The number is always one more than the number of steps taken, because you are counting positions, not moves. Option A (5 steps) is the classic off-by-one error from starting the count at 0. The interval name directly equals the number of letter names touched."

- question: "C to E♭ and C to E♯ are both thirds, because both span three letter names: C, D, and E."
  type: true-false
  answer: true
  explanation: "Correct. Generic interval size depends only on letter names. Both C–D–E♭ and C–D–E♯ span three letter names (C, D, E), so both are thirds — a minor third and an augmented third respectively. The accidental on E changes how many semitones are in the interval (its quality), not how many letter names are spanned (its number). This is why number and quality are treated as independent layers of interval description."

- question: "A unison — the same note played twice — counts as 0 in the interval numbering system, since no distance is traveled."
  type: true-false
  answer: false
  explanation: "A unison counts as 1, not 0. The starting note is counted as the first note, not as zero. This is the source of the pervasive counting error in interval naming: beginners start counting at 0 (like an array index) instead of 1 (like ordinal counting). From C, staying on C = unison (1); moving to D = 2nd (2 letter names); moving to E = 3rd (3 letter names). The interval number is always one more than the number of steps taken."

- question: "Why are intervals named by counting letter names rather than by counting semitones?"
  type: short-answer
  answer: "Letter-name counting preserves the functional identity of intervals in the staff system and in harmonic analysis. Two intervals can have the same number of semitones but different functional roles — C to D♯ (augmented 2nd, 3 semitones) and C to E♭ (minor 3rd, 3 semitones) look identical on a piano but behave differently in voice leading and harmony. Counting letter names captures this distinction and provides the foundation for quality, chord construction, and scale analysis."
  explanation: "The deeper point is that Western music notation and theory are built around the seven letter names, not the 12 chromatic pitches. The staff organizes pitch by letter name; chord symbols name intervals by letter name; scale degrees correspond to letter names. Interval numbering follows this same logic: it maps onto the notational system that musicians use. Semitone counting would be necessary for some purposes but would destroy the functional distinctions that music theory requires."
```

## Explainer

You already know from your study of intervals and note names that an interval measures the distance between two pitches, and that pitches are named with the seven letter names A through G cycling repeatedly across octaves. **Interval counting** gives every interval a number name — a **generic interval size** — by counting letter names from the lower note to the upper note, including both the starting and ending note in the count.

The critical rule is: count every letter name you touch, starting at 1. From C to E: C(1), D(2), E(3) — that's a **third**. From C to G: C(1), D(2), E(3), F(4), G(5) — that's a **fifth**. From D to A: D(1), E(2), F(3), G(4), A(5) — also a fifth. Notice that the number name comes from the count of letter names, not from the number of half steps. C to E♭ and C to E♯ are both thirds — they span the same three letter names (C, D, E) even though one has one fewer semitone than the other. This is why the number and the quality (major, minor, perfect) are separate ideas: the number tells you how many letter names are spanned; the quality refines exactly how many semitones that span contains.

The most common counting error is starting the count at 0 instead of 1. From C upward, beginners will sometimes count C as 0, D as 1, E as 2 — arriving at "C to E is a second." The fix is simple: the starting note *is* the first note, not the zeroth. Think of it like floors in a building: the ground floor is floor 1, not floor 0. When you are standing on C and you count C-D-E, you are on three different floors — a third. Another way to check yourself: a note to itself (no movement) is a **unison**, which counts as 1. One step up is a **second** (2 letter names). Two steps up is a **third** (3 letter names). The number is always one more than the number of steps.

The generic interval name gives you the foundation for everything that follows in harmony: triad construction (a major triad stacks a third and a fifth above the root), scale analysis (the diatonic scale steps are all seconds), and chord inversions (which note is on top, and how many thirds above the bass is it?). When you encounter interval *quality* — major 3rd, minor 3rd, perfect 5th, diminished 5th — you will already have the number name established. Quality is the next layer of precision, telling you exactly how many semitones fill that generic span. But that refinement only works if your generic counting is reliable first.

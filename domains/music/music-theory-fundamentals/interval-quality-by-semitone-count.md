---
id: interval-quality-by-semitone-count
title: Determining Interval Quality by Semitone Count
domain: music
course: music-theory-fundamentals
prerequisites:
- id: interval-identification-counting-method
  type: hard
- id: whole-step-half-step-fundamentals
  type: hard
builds-toward:
- consonance-dissonance-harmonic-function
- triad-construction-from-scale-degrees
tags:
- intervals
- quality
- semitones
- major-minor-perfect
stage: formal-systems
status: validated
---

# Determining Interval Quality by Semitone Count

## Core Idea
Interval quality (major, minor, perfect, augmented, diminished) is determined by counting the number of semitones between two pitches. For example, a major third contains 4 semitones, a minor third contains 3 semitones, and a perfect fifth contains 7 semitones. Combining letter-name counting with semitone counting allows you to identify any interval precisely.

## How It's Best Learned
Count semitones between intervals on a keyboard or with a chromatic scale. Create a reference chart of common intervals and their semitone counts. Practice identifying intervals both visually on the staff and by ear.

## Common Misconceptions
Students often confuse the interval name (determined by counting letters) with interval quality (determined by semitones). They may also assume all major intervals are 'better' than minor intervals, not understanding they simply have different harmonic functions.

## Questions

```yaml
- question: "A student measures the interval from C up to A♭. They count letter names: C, D, E, F, G, A — six letters (a sixth). They count semitones: C to A is 9, but A♭ is one lower, so 8 semitones. What is the correct interval name?"
  type: multiple-choice
  options:
    - "Major sixth — because it spans six letter names"
    - "Diminished sixth — because 8 semitones is two less than a major sixth"
    - "Minor sixth — because 8 semitones with a sixth span gives minor quality"
    - "Augmented fifth — because 8 semitones also matches that interval"
  answer: 2
  explanation: "Both steps are required. Step 1 gives the interval number: six letter names = a sixth. Step 2 gives the quality: 9 semitones is a major sixth, so 8 semitones — one semitone smaller — is a minor sixth. Option D is the trap: C to G# is also 8 semitones, but G# spans five letter names (C–D–E–F–G), making it an augmented fifth — a completely different interval. The letter-name count determines the interval type first; semitones then determine quality."

- question: "Two notes are 7 semitones apart. A student immediately labels the interval a 'perfect fifth.' Could this identification be incorrect?"
  type: multiple-choice
  options:
    - "No — 7 semitones always means perfect fifth, regardless of the notes"
    - "Yes — the notes could span six letter names, making it a diminished sixth (also 7 semitones)"
    - "Yes — 7 semitones could also be an augmented fourth depending on enharmonic spelling"
    - "No — semitone counting is always sufficient to determine the complete interval"
  answer: 1
  explanation: "Semitone counting alone is insufficient. Consider C to A♭♭ (A double-flat): this is 7 semitones, but A♭♭ is enharmonically G. C to G spans five letter names = fifth (perfect fifth). But C to A♭♭ spans six letter names (C–D–E–F–G–A = sixth), making it a diminished sixth — same pitch, different interval name. Letter-name counting must come first to get the correct interval number, and only then does the semitone count determine quality."

- question: "C to D♯ and C to E♭ have the same number of semitones but are different intervals."
  type: true-false
  answer: true
  explanation: "C to D♯: letter names C, D — two letters = a second. 3 semitones with a second span = augmented second. C to E♭: letter names C, D, E — three letters = a third. 3 semitones with a third span = minor third. Both are 3 semitones and sound identical on an equal-tempered instrument, but they are named differently because interval number is determined by letter-name count. This is precisely why semitone counting alone cannot identify an interval."

- question: "The word 'perfect' can be applied to any interval that sounds particularly consonant and stable, such as a major third or major sixth."
  type: true-false
  answer: false
  explanation: "'Perfect' is a specific quality term that applies only to unisons, fourths, fifths, and octaves — intervals that appear with a single natural form in the diatonic scale. Major thirds and major sixths are consonant but are described as 'major,' not 'perfect.' The major/minor distinction applies to seconds, thirds, sixths, and sevenths. The terminology is a formal system, not a description of perceived consonance."

- question: "Why are two separate operations — counting letter names and counting semitones — both necessary to identify an interval completely?"
  type: short-answer
  answer: "Letter-name counting determines the interval number (second, third, fourth, etc.), while semitone counting determines the quality (major, minor, perfect, augmented, diminished). Neither operation alone is sufficient: different intervals can share a semitone count (C to D♯ and C to E♭ are both 3 semitones but a second and a third respectively), and different intervals can share a letter span (C to E♮ and C to E♭ both span three letters but differ by a semitone). Only the combination of both counts uniquely identifies an interval."
  explanation: "Musical notation encodes two independent pieces of information: the diatonic letter name (position in the scale) and the chromatic alteration (accidentals that modify pitch by semitones). Interval quality is the relationship between these two dimensions — how many semitones a particular letter-span contains compared to its default diatonic version. Mastering this two-step process is the foundation of all subsequent harmonic work, from triad construction to ear training."
```

## Explainer

Identifying an interval precisely requires two separate operations, and confusing them is the most common beginner error. You already know how to count letter names to get the interval **number** — C to E is a third (C, D, E — three letters). But "third" alone is incomplete: a minor third and a major third are different intervals with very different sounds and functions. The interval **quality** is determined by counting **semitones** — the actual pitch distance, not just the letter distance. This second count is what this topic teaches.

Start with the keyboard as a reference tool. Every adjacent key (including black keys) is one semitone apart. From C up to E♭ is 3 semitones; from C up to E♮ is 4 semitones. Both span three letter names (C–D–E), so both are thirds. But 3 semitones gives a **minor third**, and 4 semitones gives a **major third**. The interval number (third) stays the same; the quality changes with the semitone count. The key reference facts to internalize are: unison = 0 semitones; **major second** = 2; **minor third** = 3; **major third** = 4; **perfect fourth** = 5; **tritone** (augmented fourth or diminished fifth) = 6; **perfect fifth** = 7; **minor sixth** = 8; **major sixth** = 9; **minor seventh** = 10; **major seventh** = 11; **perfect octave** = 12.

Notice that the words "major" and "minor" apply to seconds, thirds, sixths, and sevenths — intervals that come in two natural versions. The word "perfect" applies to unisons, fourths, fifths, and octaves — intervals that have a single natural version in the diatonic scale, highly consonant and stable. If you expand a perfect interval by a semitone, it becomes **augmented**; if you compress it, it becomes **diminished**. Major intervals shrunken by a semitone become minor; minor intervals shrunken by a semitone become diminished; major intervals expanded by a semitone become augmented.

The two-step process is: (1) count letter names to determine the interval number; (2) count semitones to determine the quality. For example: C to A♭. Step 1: C, D, E, F, G, A — six letters, so it's a sixth. Step 2: C to A is 9 semitones (a major sixth), but A♭ is one semitone lower than A, so C to A♭ is 8 semitones — a **minor sixth**. Neither step alone is sufficient. Letter counting without semitone counting leaves quality undetermined. Semitone counting without letter counting can misidentify the interval number (C to D♯ is 3 semitones, same as C to E♭ — but one is a second and one is a third).

Building this skill pays off immediately when you begin constructing triads: a major triad is a major third (4 semitones) plus a perfect fifth (7 semitones) above the root; a minor triad is a minor third (3 semitones) plus a perfect fifth. Your ability to hear and name intervals is also the foundation of all ear training — recognizing that the opening of "Happy Birthday" begins with a major second, or that a perfect fifth has a particular open, stable resonance, gives you perceptual anchors for everything from chord identification to melodic dictation.

---
id: seventh-chord-construction
title: Seventh Chord Construction
domain: music
course: music-theory-fundamentals
prerequisites:
- id: triad-construction-major-minor
  type: hard
- id: interval-quality
  type: hard
builds-toward:
- seventh-chords
- functional-harmony
- harmonic-function-basics
- jazz-harmony-basics
tags:
- chords
- seventh
- dominant
stage: formal-systems
status: validated
---

# Seventh Chord Construction

## Core Idea
Seventh chords add a 7th interval above the root to any triad, creating four-note chords with richer harmonic color. The dominant 7th (major triad plus minor 7th) has strong pull toward resolution. Major 7th and minor 7th chords are also fundamental. Seventh chords appear frequently in tonal music and jazz.

## How It's Best Learned
Build seventh chords by first constructing the triad, then adding a 7th. Verify all intervals. Listen to each chord type and hear how the 7th color differs from its triadic base.

## Common Misconceptions
Thinking the 7th is always minor (it can be major or minor). Confusing different seventh chord types without understanding underlying intervals. Building a dominant 7 with a major 7 instead of minor 7.

## Questions

```yaml
- question: "Which of the following correctly identifies the notes of a dominant seventh chord built on D?"
  type: multiple-choice
  options:
    - "D–F♯–A–C♯ (D major triad plus a major seventh)"
    - "D–F♯–A–C (D major triad plus a minor seventh)"
    - "D–F–A–C (D minor triad plus a minor seventh)"
    - "D–F♯–A♭–C (D augmented triad plus a minor seventh)"
  answer: 1
  explanation: "A dominant seventh chord is always a major triad plus a minor seventh. D major triad = D–F♯–A; the minor seventh above D is C (ten half-steps, not eleven). Option A is a major seventh chord (D–F♯–A–C♯), the most common confusion — adding a major seventh instead of a minor seventh produces a major-7 chord, which has a lush floating quality rather than the driving urgency of the dominant seventh."

- question: "Why does the dominant seventh chord create such a strong pull toward resolution in tonal music?"
  type: multiple-choice
  options:
    - "Its major triad quality creates brightness that naturally contrasts with the tonic chord"
    - "It is built on the fifth scale degree, which by convention always resolves to the first"
    - "It contains a tritone between its third and seventh, producing two simultaneous tension forces that resolve by half-step motion"
    - "The minor seventh interval is inherently dissonant and must resolve upward by a half step"
  answer: 2
  explanation: "The tritone is the key. In G7 (G–B–D–F), the third (B) and seventh (F) form a tritone — the most unstable interval in Western harmony. B is the leading tone that pulls up to C; F pulls down to E. These two simultaneous half-step resolutions make the dominant seventh the most directional chord in tonal music. Convention (being built on scale degree 5) is a consequence of this acoustic pull, not the cause."

- question: "A major seventh chord and a dominant seventh chord both use a major triad as their foundation."
  type: true-false
  answer: true
  explanation: "Yes — both chord types start with a major triad. What distinguishes them is the quality of the added seventh: the major seventh chord adds a major seventh (e.g., Cmaj7 = C–E–G–B), while the dominant seventh chord adds a minor seventh (e.g., C7 = C–E–G–B♭). This single half-step difference dramatically changes the harmonic quality: the major seventh floats softly; the dominant seventh drives urgently toward resolution."

- question: "The dominant seventh chord built on G in the key of C major is G–B–D–F♯."
  type: true-false
  answer: false
  explanation: "The seventh above G in the key of C major is F♮ (a minor seventh — ten half-steps), not F♯ (a major seventh — eleven half-steps). G–B–D–F♯ would be a Gmaj7 chord. The dominant seventh chord is G–B–D–F. This is the single most common construction error: using a major seventh where a minor seventh is needed, which eliminates the tritone and with it the chord's directional pull."

- question: "Explain why understanding a seventh chord's intervallic recipe (triad type + seventh quality) is more useful than memorizing the notes of each chord spelling."
  type: short-answer
  answer: "The intervallic recipe lets you build any seventh chord from any root without a lookup table. Once you know a dominant seventh is always 'major triad + minor seventh,' you can construct D7, B♭7, or F♯7 instantly by applying the recipe. It also explains why each chord type sounds as it does — the dominant seventh drives because of its tritone, the major seventh floats because its major seventh is a half-step from the octave. Memorized spellings break the moment you change key or encounter a chromatic context; the recipe works everywhere."
  explanation: "This is the difference between instrumental knowledge and declarative knowledge. The recipe is portable: it scales to all 12 roots, all four common seventh chord types, and arbitrary transpositions. More importantly, it preserves the 'why' — you understand the chord's sonic character in terms of its intervals, not just its letter names."
```

## Explainer

You already know how to build **triads** — three-note chords constructed by stacking thirds above a root. A major triad stacks a major third then a minor third; a minor triad reverses the order. The **seventh chord** extends this logic one step further: take any triad and add another third on top, a seventh above the root. This single additional pitch transforms the chord's sonic character dramatically — triads can sound complete and stable, but seventh chords carry an inherent tension that pushes toward resolution.

The most important seventh chord in tonal music is the **dominant seventh**: a major triad with a minor seventh above the root. In C major, this is G-B-D-F. The G major triad (G-B-D) provides the dominant's upward-driving **leading tone** (B, a half step below C), and the added F — a minor seventh above G — creates a second source of tension. F and B together form a **tritone** (an augmented fourth / diminished fifth), the most unstable interval in Western harmony, which resolves compellingly: B rises a half step to C, F falls a half step to E. The dominant seventh chord is the engine of tonal music's forward motion.

Other seventh chord types produce very different qualities. The **major seventh chord** (major triad + major seventh) has a lush, slightly unresolved quality — the major seventh (a half step below the octave) creates gentle tension without the driving urgency of the tritone. This sound is characteristic of jazz and late Romantic harmony. The **minor seventh chord** (minor triad + minor seventh) is softer still, commonly found on the ii and vi chords in major keys, where it serves subdominant or pre-dominant functions. The **diminished seventh chord** (fully diminished) is maximally tense — built entirely of minor thirds, its every stacked pair is a tritone — making it useful for dramatic moments and enharmonic modulations.

The key skill is **not memorizing chord spellings but understanding the intervallic recipe**: what triad type is at the base, and what quality of seventh is added? Once you internalize that a dominant seventh is always a major triad plus a minor seventh, you can build one from any root without lookup. G7 = G major triad + F. D7 = D major triad + C. A7 = A major triad + G. This logic extends to all seventh chord types. The intervallic understanding also tells you *why* each chord type sounds as it does — the dominant seventh drives forward because of its embedded tritone, the major seventh floats because its seventh is just one half step shy of resolution. Seventh chords are not just new vocabulary to memorize; they are the next layer of the interval logic you already know.

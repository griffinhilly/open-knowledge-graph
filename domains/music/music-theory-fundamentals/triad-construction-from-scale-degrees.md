---
id: triad-construction-from-scale-degrees
title: Building Triads from Scale Degrees
domain: music
course: music-theory-fundamentals
prerequisites:
- id: major-scale-construction-fundamentals
  type: hard
- id: natural-minor-scale-construction-fundamentals
  type: hard
- id: interval-quality-by-semitone-count
  type: hard
- id: augmented-triads-construction
  type: soft
builds-toward:
- diatonic-chord-construction-fundamentals
- primary-harmony-functions
tags:
- triads
- harmony
- scale-degrees
- diatonic
stage: formal-systems
status: validated
---
# Building Triads from Scale Degrees

## Core Idea
Triads (three-note chords) can be built on each scale degree using every other note of the scale. In major keys, the triads on I, IV, and V are major; on ii, iii, and vi are minor; and on vii° is diminished. In minor keys, the pattern differs based on which form of minor scale is used. Understanding this system reveals the harmonic foundation of a key.

## How It's Best Learned
Build all seven triads in a major key on staff paper. Play them on an instrument. Identify the quality of each (major, minor, diminished). Repeat for minor keys.

## Common Misconceptions
Students sometimes forget that triads use non-consecutive pitches (skipping every other scale degree). Another error: applying major-key triad qualities to minor keys without accounting for the different interval structure.

## Questions

```yaml
- question: "What type of triad is built on scale degree 2 (D) of C major, and how do you determine this without memorizing a chart?"
  type: multiple-choice
  options:
    - "Major — the second scale degree always produces a major triad"
    - "Minor — counting semitones gives D to F (3 semitones) then F to A (4 semitones), a minor triad"
    - "Diminished — the second scale degree is adjacent to the leading tone"
    - "Augmented — the raised fourth gives the third an extra semitone"
  answer: 1
  explanation: "To identify the triad on D in C major, take the diatonic notes D–F–A. Count semitones: D to F is 3 semitones (minor third), F to A is 4 semitones (major third). Minor third stacked below major third = minor triad. The skill is derivation from interval counting, not memorization. This is the ii chord of C major — always minor in any major key, for the same structural reason."

- question: "In natural minor, the chord built on scale degree 5 is minor rather than major. Why does this matter for harmony?"
  type: multiple-choice
  options:
    - "It doesn't matter — the fifth scale degree sounds the same regardless of chord quality"
    - "A minor v chord lacks the leading tone, weakening the dominant-to-tonic resolution that defines functional harmony"
    - "A minor v chord is easier to play on instruments, which is why natural minor is preferred"
    - "The fifth scale degree must be major by definition — natural minor raises it automatically"
  answer: 1
  explanation: "Functional harmony depends on the leading tone — the note a half step below the tonic — creating strong upward pull into the tonic. In natural minor, scale degree 7 is a whole step below the tonic (the subtonic), not a half step. The natural v chord contains no leading tone and produces a much weaker dominant-to-tonic pull. When composers want a strong authentic cadence in a minor key, they raise scale degree 7, creating harmonic minor and a major V chord. This is why harmonic minor exists."

- question: "In a major key, the triad built on scale degree 7 (the leading tone) is diminished."
  type: true-false
  answer: true
  explanation: "Build the triad on B in C major: B–D–F. B to D is a minor third (3 semitones), D to F is a minor third (3 semitones). Two stacked minor thirds = diminished triad. This holds in every major key because the seventh scale degree's position — one semitone below the tonic — means the intervals above it always stack two minor thirds. No memorization required; the interval structure of the major scale forces this result."

- question: "Every diatonic triad in a major key is either major or minor."
  type: true-false
  answer: false
  explanation: "The triad built on scale degree 7 (the leading tone) is diminished — neither major nor minor. A diminished triad consists of two stacked minor thirds, producing a tritone between root and fifth rather than a perfect fifth. In C major, B–D–F is the diminished triad (vii°). This matters in practice: the vii° chord functions differently from major and minor triads and is typically treated as an incomplete dominant seventh chord."

- question: "Describe the process for determining the quality of any diatonic triad without referring to a memorized chart."
  type: short-answer
  answer: "Identify the root (the scale degree), take the note a third above it in the scale (skip one scale degree), then take the note a fifth above the root (skip another). Count the semitones from root to third, and from third to fifth. If the lower interval is 4 semitones (major third) and the upper is 3 (minor third), the triad is major. If 3 then 4, it is minor. If 3 then 3, it is diminished. The quality is a direct consequence of the scale's interval pattern, not something to memorize separately."
  explanation: "This derivation approach is both more durable and deeper than memorization: understanding why vii° is always diminished in major keys connects to the structure of the major scale itself. A student who can derive triad quality from interval counting will never confuse major-key and minor-key triad patterns, because they understand the underlying mechanism."
```

## Explainer

A **triad** is a three-note chord built by stacking intervals of a third — that is, by taking every other note of a scale. From your work with major and minor scale construction and interval quality counting, you have all the tools needed to build and identify every triad in a key. The key insight is that when you stack thirds using only the notes of a given scale, the resulting triads inherit the scale's interval structure, which means different scale degrees produce triads of different qualities.

Let's work through C major. On scale degree 1 (C), take C–E–G: C to E is a major third (4 semitones), E to G is a minor third (3 semitones). A major third stacked below a minor third = a **major triad**. On scale degree 2 (D), take D–F–A: D to F is a minor third (3 semitones), F to A is a major third (4 semitones). Minor third below + major third above = **minor triad**. On scale degree 7 (B), take B–D–F: B to D is a minor third, D to F is a minor third. Two stacked minor thirds = **diminished triad**. You don't need to memorize that "vii is diminished" — you can derive it from counting semitones. But after doing this enough times in enough keys, the pattern becomes automatic: I–ii–iii–IV–V–vi–vii° for major keys.

The **minor key** case is more complex because the natural minor scale produces a different interval pattern, yielding a different set of triad qualities: i–ii°–III–iv–v–VI–VII (in natural minor). The critical difference from major is the v chord: in natural minor, the chord on scale degree 5 is a *minor* triad rather than a major one. This matters because the dominant-to-tonic resolution that defines functional harmony depends on the leading tone — the note a half step below the tonic that creates strong upward pull. Natural minor's fifth scale degree does not contain the leading tone; it contains the subtonic (a whole step below the tonic) instead. When composers want a strong authentic cadence in a minor key, they typically raise the seventh scale degree to create a major V chord, which is why the harmonic minor scale exists.

The practical workflow for triad construction is: (1) identify the root (the scale degree you're building on), (2) take the scale note a third above (skip one scale note), (3) take the scale note a fifth above the root (skip another scale note). The resulting notes are all diatonic — no accidentals needed beyond what the key signature supplies. Count the semitones between root and third, and between third and fifth, to identify the quality. Over time, this process should become fast enough that building all seven triads in a key takes under a minute — the foundation for everything in harmony that follows.

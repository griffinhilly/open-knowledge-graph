---
id: diatonic-triad-harmonization
title: 'Diatonic Triads: Harmonizing Scale Degrees'
domain: music
course: music-theory-fundamentals
prerequisites:
- id: major-scale-construction
  type: hard
- id: triads
  type: hard
- id: scale-degree-names-and-function
  type: hard
- id: minor-scale-types-comparison
  type: soft
- id: triad-construction-from-intervals
  type: hard
builds-toward:
- harmonic-function-basics
- harmonic-progression-analysis
- diatonic-chords-major-minor-keys
tags:
- diatonic
- harmonization
- scale-degree
- chord-progression
stage: formal-systems
status: validated
---

# Diatonic Triads: Harmonizing Scale Degrees

## Core Idea
In any major or minor key, specific triads naturally occur when building chords on each scale degree using only notes from that key. The I, IV, and V are major triads in major keys; the i, IV, and V are found in minor keys. The quality and harmonic function of each diatonic chord are determined by the key's structure. Understanding diatonic harmonization is fundamental to composing, analyzing, and improvising within a key.

## Questions

```yaml
- question: "You are harmonizing in G major. What quality is the chord built on the 2nd scale degree (A)?"
  type: multiple-choice
  options:
    - "Major — A is a common note shared with many chords in G major"
    - "Minor — the diatonic structure of every major key produces a minor triad on scale degree ii"
    - "Diminished — it is adjacent to the tonic and therefore unstable"
    - "Major — it shares two notes with the I chord and therefore inherits its quality"
  answer: 1
  explanation: "In G major, building a triad on A using only notes from the key gives A–C–E. The interval from A to C is a minor third (1.5 steps), so the chord is minor. This is not specific to G major — the diatonic structure of every major key produces a minor triad on the 2nd degree (ii). The chord quality follows from the interval structure of the scale, not from any choice or convention."

- question: "A composer wants a major chord on the 2nd scale degree in C major and uses D–F#–A instead of D–F–A. This chord:"
  type: multiple-choice
  options:
    - "Is perfectly diatonic — composers can choose the quality of any chord in their key"
    - "Is a non-diatonic chord that introduces F#, a note outside C major, making it a chromatic or borrowed chord"
    - "Is the standard ii chord in C major, since D major is closely related"
    - "Is allowed because F# belongs to the G major scale, which shares six notes with C major"
  answer: 1
  explanation: "Diatonic chords are built using only the notes of the key. In C major, the note F is natural (not F#), so the triad on D is D–F–A (minor). Using F# introduces a chromatic alteration that makes this a non-diatonic chord — a technique available to composers, but one that leaves the diatonic system. The quality of diatonic chords is fixed by the key's interval structure, not a free choice."

- question: "In any major key, the chords built on scale degrees I, IV, and V are always major triads."
  type: true-false
  answer: true
  explanation: "This follows from the interval structure of the major scale (W-W-H-W-W-W-H). The whole-step and half-step pattern guarantees that building triads on degrees 1, 4, and 5 using only scale tones always produces major thirds above those roots, yielding major triads. This is true regardless of the key — C major, F# major, Bb major, or any other."

- question: "The chord built on the 7th scale degree of a major key (vii) is a minor triad."
  type: true-false
  answer: false
  explanation: "The chord on the 7th scale degree is a *diminished* triad, not minor. In C major it is B–D–F. The interval from B to D is a minor third (correct for minor or diminished), but the interval from B to F is a diminished fifth (tritone), not a perfect fifth. A minor triad has a perfect fifth above the root; a diminished triad has a diminished fifth. The vii° symbol (with the degree symbol) specifically denotes diminished quality."

- question: "Why do the diatonic triads in every major key always have the same chord qualities on the same scale degrees — I and IV and V always major, ii and iii and vi always minor, vii always diminished — regardless of which major key you are in?"
  type: short-answer
  answer: "Because all major keys share the same interval structure (W-W-H-W-W-W-H). When you build a triad on each scale degree using only the notes of that key, the pattern of whole and half steps determines whether the third above the root is major (2 whole steps) or minor (1.5 steps), which in turn fixes the chord quality. The same interval structure in every key produces the same quality pattern on every degree."
  explanation: "This is why Roman numeral analysis is so powerful — the numerals describe relationships that hold across all major keys. Once you know that ii is always minor and V is always major, you can read and transpose progressions without recalculating from scratch in each new key."
```

## Explainer

You already know how to build major and minor triads from any root note, and you know the names of each scale degree. **Diatonic triad harmonization** brings these two skills together: for each scale degree in a key, you build a triad using only the notes that belong to that key. The triad's quality — major, minor, or diminished — is not a free choice. It is determined entirely by the key's half-step and whole-step structure.

In C major, for example, the seven diatonic triads are: C-E-G (I, major), D-F-A (ii, minor), E-G-B (iii, minor), F-A-C (IV, major), G-B-D (V, major), A-C-E (vi, minor), and B-D-F (vii°, diminished). Notice that the root, third, and fifth of each chord are all picked from the C major scale — no accidentals needed. The result is that **I, IV, and V come out major** because the key's interval structure places major thirds above those roots. The chords on ii, iii, and vi come out minor; the chord on vii comes out diminished. These qualities are fixed by the key and cannot be changed without borrowing from another key.

Roman numeral notation encodes this directly. **Uppercase numerals** (I, IV, V) indicate major triads; **lowercase numerals** (ii, iii, vi) indicate minor triads; a degree symbol (vii°) indicates diminished. This convention lets you read harmonic function at a glance and transpose a chord progression to any key instantly, because the numerals describe relationships, not specific pitches.

The three major triads — I, IV, and V — carry the most structural weight in tonal harmony. They are called the **primary triads** and between them contain all seven notes of the major scale. The I chord (tonic) is home base; the V chord (dominant) creates the strongest tension pulling back toward I; the IV chord (subdominant) creates a gentler departure from tonic. The minor triads — ii, iii, and vi — are called **secondary triads** and frequently serve as substitutes or embellishments of the primary triads. The ii chord, for instance, shares two notes with IV and often moves toward V in the same way IV does. Learning to hear these relationships by ear, not just name them on paper, is the goal — the table of diatonic triads is a tool for understanding why certain chord progressions sound stable or unsettled, not just a memorization exercise.

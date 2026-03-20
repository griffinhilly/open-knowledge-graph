---
id: diatonic-harmony
title: Diatonic Harmony and Roman Numeral Analysis
domain: music
course: music-theory-fundamentals
prerequisites:
- id: triads
  type: hard
- id: major-scales
  type: hard
- id: key-signatures
  type: soft
- id: chord-inversions
  type: soft
- id: modes
  type: soft
- id: seventh-chords
  type: soft
builds-toward:
- chord-progressions
- cadences
tags:
- diatonic
- roman numerals
- scale degrees
- harmony
- analysis
stage: formal-systems
status: validated
---
# Diatonic Harmony and Roman Numeral Analysis

## Core Idea
Diatonic harmony refers to chords built exclusively from the notes of a given scale. In a major key, each scale degree generates a triad: I and IV and V are major, ii and iii and vi are minor, and vii° is diminished. Roman numerals label these chords (uppercase for major, lowercase for minor), making the analysis transposable to any key. The I, IV, and V chords are the 'primary' chords that form the harmonic backbone of most tonal music; ii, iii, and vi are 'secondary' chords with related functions.

## How It's Best Learned
Build all seven diatonic triads in C major and label them with Roman numerals. Then transpose the analysis to G major and F major to see that the Roman numeral pattern stays the same. Analyze a simple folk song using Roman numerals.

## Common Misconceptions
- Roman numeral analysis describes harmonic function relative to the key, not absolute pitch — I in G major is G, but I in D major is D.
- The vii° chord is diminished, not minor, because it is built on the leading tone with two stacked minor thirds.

## Questions

```yaml
- question: "In a major key, which scale degree produces a minor triad?"
  type: multiple-choice
  options: ["I (tonic)", "IV (subdominant)", "V (dominant)", "ii (supertonic)"]
  answer: 3
  explanation: "In a major key, chords built on scale degrees ii, iii, and vi are minor — they receive lowercase Roman numerals. I, IV, and V are major (uppercase). The ii chord, built on the second scale degree, is a minor triad, which is why it is written in lowercase. The tonic (I), subdominant (IV), and dominant (V) are all major."

- question: "Roman numeral I always refers to the note C."
  type: true-false
  answer: false
  explanation: "Roman numerals describe harmonic function relative to the current key, not absolute pitches. I means the tonic chord of whatever key you are in — G major in G major, D major in D major, Bb major in Bb major. This transposability is exactly what makes Roman numeral analysis powerful: the same numeral pattern applies in every key."

- question: "Why is the chord built on the seventh scale degree of a major key diminished rather than major or minor?"
  type: short-answer
  answer: "It is built by stacking two minor thirds: from the leading tone up a minor third to the second scale degree, then another minor third to the fourth scale degree. Two stacked minor thirds produce a diminished triad."
  explanation: "In C major, vii° is B-D-F. B to D is a minor third (3 half steps); D to F is also a minor third (3 half steps). A major triad uses a major third then minor third; a minor triad uses a minor third then major third. The all-minor-thirds structure of vii° creates a diminished fifth (tritone) between B and F, giving the chord its strong instability and drive toward the tonic."
```

## Explainer

When you learned to build triads, you discovered that the quality of a chord (major, minor, diminished) depends on which thirds are stacked. Diatonic harmony takes this one step further: if you build a triad on every note of a major scale using only the notes already in that scale, a predictable pattern of chord qualities emerges. This pattern is the same in every major key, which is why Roman numeral analysis is so useful — you learn it once and it works everywhere.

In any major key, the seven diatonic triads follow this quality pattern: **I major, ii minor, iii minor, IV major, V major, vi minor, vii° diminished**. The uppercase Roman numerals (I, IV, V) signal major chords; the lowercase (ii, iii, vi) signal minor chords; and the degree symbol (vii°) signals diminished. The reason this pattern is fixed is that major scale intervals are fixed — the whole- and half-step structure of the scale always places the same interval relationships between scale degrees.

The most important chords to internalize first are the **primary chords**: I (tonic), IV (subdominant), and V (dominant). These three chords between them can harmonize almost any melody in a major key, and they form the backbone of folk songs, hymns, blues, and pop music. The **secondary chords** — ii, iii, vi — have related functions: ii tends to move toward V (a common pre-dominant), vi often substitutes for I (sharing two of its three pitches), and iii is rarer and sometimes functions like a tonic substitute.

A common stumbling block is the vii° chord. Students sometimes expect it to be minor (since it is built on the leading tone, a note that is "almost" the tonic), but the scale forces both intervals to be minor thirds, yielding a diminished triad. The tritone between the root and fifth of vii° gives it tremendous instability and a powerful drive to resolve to I — a useful property that composers exploit constantly.

Practicing Roman numeral analysis means learning to read chords relative to a key rather than by their absolute names. When you see a chord labeled IV, you immediately know it is major and built on the fourth scale degree of the current key — regardless of what key that is. This flexibility is what makes Roman numeral notation the standard tool for harmonic analysis across all of tonal music.

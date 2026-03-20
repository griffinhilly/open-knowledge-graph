---
id: chord-inversions
title: Chord Inversions
domain: music
course: music-theory-fundamentals
prerequisites:
- id: triads
  type: hard
- id: seventh-chords
  type: soft
builds-toward:
- diatonic-harmony
- chord-progressions
- cadences
tags:
- inversions
- voice leading
- bass note
- figured bass
- harmony
stage: formal-systems
status: validated
---

# Chord Inversions

## Core Idea
A chord inversion occurs when a note other than the root is the lowest-sounding voice. A triad in root position has the root on the bottom; first inversion has the third on the bottom; second inversion has the fifth on the bottom. Inversions create smoother bass lines and allow chords to connect more fluidly. Figured bass notation (numbers below the bass note) originated in Baroque music to indicate inversions and remains a standard analytical shorthand.

## How It's Best Learned
Play a simple I-IV-V-I progression first in root position, then revoice each chord to achieve a smooth, stepwise bass line using inversions. Identify the bass note of each chord and determine the inversion before analyzing the full chord.

## Common Misconceptions
- An inverted chord is still the same chord — a C major chord in first inversion is still C major, just voiced differently.
- Second inversion chords (6/4 chords) are harmonically unstable and typically require special resolution contexts.

## Questions

```yaml
- question: "A C major chord is played with E in the bass, G in the middle, and C on top. What inversion is this?"
  type: multiple-choice
  options: ["Root position", "First inversion", "Second inversion", "Third inversion"]
  answer: 1
  explanation: "First inversion has the third of the chord (E, the third of C major) as the lowest-sounding note. The other voices can be arranged in any order above the bass. This is notated in figured bass as '6' (or 6/3), since the upper voices form intervals of a sixth and a third above the bass."

- question: "Changing a C major chord from root position to first inversion makes it a fundamentally different chord with a different harmonic function."
  type: true-false
  answer: false
  explanation: "Inversion changes the voicing and the bass note, which affects the sound and stability of the chord, but it does not change the chord's identity or harmonic function. A C major chord in any inversion is still functioning as tonic harmony — its relationship to the key is unchanged. The bass note creates a different color and smoothness, not a different chord."

- question: "Why are second-inversion triads (6/4 chords) treated with special care in traditional harmony, unlike root position and first inversion triads?"
  type: short-answer
  answer: "In second inversion, the fifth of the chord is in the bass, creating a fourth above the bass to the root. The fourth was historically considered dissonant against a bass note, making the 6/4 chord harmonically unstable. It typically appears in three specific contexts: the cadential 6/4 (which resolves to a dominant chord), the passing 6/4 (bass moves stepwise through it), and the pedal 6/4 (bass stays stationary). In each case, the chord is understood as needing resolution rather than resting as a stable harmony."
  explanation: "The instability of the 6/4 chord is a crucial practical point. Students often treat all inversions as interchangeable, but placing the dominant or subdominant in second inversion at a cadence without proper resolution sounds weak and unresolved."
```

## Explainer

When you learned to build triads, you stacked thirds above a root: for C major, that is C (root), E (third), G (fifth). Root position puts C in the bass, and that is the most stable, grounded sound. But a triad contains three notes, and any of them can be moved to the bottom — those are the inversions.

First inversion places the third of the chord in the bass. For C major, E is now on the bottom. The chord still contains the same three pitches and still functions as C major harmony, but the sound is lighter and more restless — less settled than root position. First inversion chords are common in passing contexts, where the bass line moves smoothly through a scalar passage. Because the bass note is E rather than C, the bass line can move up to F (for an F major chord in root position) or down to D (for other harmonies), creating smooth stepwise motion. This is one of the primary reasons composers use inversions: to create a smooth, singable bass line rather than a bass that leaps from root to root.

Second inversion places the fifth in the bass. For C major, G is now on the bottom. This creates an interval of a fourth from the bass up to the root (G up to C), which traditional harmony treats as dissonant above a bass note. Second inversion chords are therefore unstable and require specific contexts: the most important is the cadential 6/4, where the I chord appears in second inversion just before the dominant at a cadence (I⁶₄ → V → I). Here the 6/4 chord functions almost like an embellishment of the dominant, with the fifth in the bass and the root and third resolving downward by step to the dominant chord.

Figured bass notation, which originated in Baroque music, labels inversions with numbers representing the intervals above the bass. Root position (5/3) is usually written with no numbers or just as the Roman numeral. First inversion is marked with 6 (short for 6/3). Second inversion is marked 6/4. When you see "I⁶" in a harmonic analysis, it means the tonic chord in first inversion; "V⁶₄" is the dominant in second inversion. These symbols remain standard analytical tools in music theory today.

The practical skill to build is quickly identifying the inversion of any chord: look at the bass note, identify which member of the chord it is (root, third, or fifth), and that tells you the inversion. Then ask whether the bass line is moving smoothly — because that is usually why the composer chose an inversion in the first place.

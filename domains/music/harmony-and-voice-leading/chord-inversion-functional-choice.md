---
id: chord-inversion-functional-choice
title: Choosing Chord Inversions for Harmonic Function
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: chord-inversions-voice-leading-options
  type: hard
- id: harmonic-function-basics
  type: hard
builds-toward:
- cadential-voice-leading-patterns
tags:
- inversions
- function
- harmony
stage: formal-systems
status: validated
---

# Choosing Chord Inversions for Harmonic Function

## Core Idea
The choice of root position, first inversion, or second inversion affects both the bass line and the harmonic weight of a chord. Root position sounds strongest and most stable; first inversion creates harmonic motion and supports stepwise bass lines; second inversion sounds weak and typically appears at specific structural points like cadences. Each inversion supports different voice-leading and harmonic goals.

## Questions

```yaml
- question: "A student composes a phrase ending on a tonic chord in second inversion, expecting a strong, stable arrival. The passage sounds weak and unresolved. What is the source of this problem?"
  type: multiple-choice
  options:
    - "Tonic chords should never appear at phrase endings"
    - "Second inversion is the most stable inversion and should work for arrivals — the problem must lie elsewhere"
    - "Second inversion places the fifth of the chord in the bass, creating an unstable, suspended quality that calls for resolution rather than signaling arrival"
    - "The problem is that first inversion also creates instability; only a root-position dominant chord sounds resolved"
  answer: 2
  explanation: "Second inversion is the most unstable inversion because scale degree 5 in the bass sets up dominant function rather than projecting tonic stability. The classic use of second inversion (the cadential I6/4) exploits this instability — I6/4 functions as a pre-dominant preparation, not a stable tonic. Using second inversion to end a phrase mistakes the chord's letter-name (I) for its functional effect. Only root-position tonic provides the full harmonic weight of arrival."

- question: "A composer wants a smooth stepwise descending bass line from scale degree 1 down to scale degree 5. Which principle is guiding her inversion choices?"
  type: multiple-choice
  options:
    - "Root position must always be used to maintain harmonic clarity"
    - "Bass-line goals drive inversion choices — each chord is placed in the inversion whose bass note creates the desired stepwise motion"
    - "Inversions are chosen based solely on the soprano melody"
    - "Harmonic function must always take priority over smooth voice leading"
  answer: 1
  explanation: "Fluent tonal writing often starts from bass-line goals and derives inversion choices from them. A stepwise bass from 1 to 5 might use: I (root position, bass on 1) → I6 (first inversion, bass on 3) → IV (root position, bass on 4) → I6/4 (second inversion, bass on 5). Each inversion is chosen to place the correct scale degree in the bass for the desired bass-line shape. This is the intersection of harmonic function and voice leading working together."

- question: "A first-inversion tonic chord sounds lighter and more passing than root-position tonic because it has the third, not the root, in the bass."
  type: true-false
  answer: true
  explanation: "The bass note carries significant structural weight in tonal music. When the root is in the bass, the chord projects stability and arrival. When the third is in the bass, the harmony retains its tonal identity (still tonic) but feels less conclusive — it is passing through rather than landing. This is why first-inversion chords are natural in flowing bass lines but would be inappropriate as the final chord of a cadence, which requires root-position tonic for full closure."

- question: "In a cadential six-four progression (I6/4 – V – I), the I6/4 functions as a stable tonic harmony that prepares the dominant."
  type: true-false
  answer: false
  explanation: "Despite being spelled with tonic pitch classes, the cadential six-four does not function as stable tonic. Scale degree 5 is in the bass — the dominant scale degree — and the chord members above create a suspended effect that implies dominant motion. The I6/4 is more accurately understood as an intensification of the dominant: a pre-dominant chord that makes the subsequent V arrival feel even stronger. Treating it as a stable tonic arrival is one of the most common errors in harmonic analysis."

- question: "Explain why a second-inversion tonic chord (I6/4) at a cadence does not represent a stable tonic. What is it actually doing harmonically?"
  type: short-answer
  answer: "In the cadential six-four, scale degree 5 is in the bass — the same bass note the following V chord will have. Rather than sounding like a tonic chord in an unstable position, it functions as an elaboration over the dominant bass. The upper voices (forming a 6/4 above the bass) create tension that resolves downward to the fifth and third of the dominant chord when V arrives. The I6/4 belongs to the dominant function, not the tonic function, despite being spelled as a tonic triad."
  explanation: "This is a case where spelling and function diverge — a critical concept in harmonic analysis. The chord is spelled with tonic pitch classes but functions as part of the dominant. Recognizing this requires understanding that harmonic function is determined by context and bass position, not just by which pitch classes are present. The cadential I6/4 is one of the clearest demonstrations that inversion choice is functionally consequential, not merely coloristic."
```

## Explainer

You've learned that a chord can be placed in root position (root in the bass), first inversion (third in the bass), or second inversion (fifth in the bass), and you understand how each inversion affects voice-leading options. Now the question is compositional: given a harmonic goal, which inversion serves it best? The choice is not arbitrary — **inversions carry different harmonic weight**, and choosing the right inversion is as important to the effect of a progression as choosing the right chord.

Root-position chords are the **strongest and most stable**. When a tonic chord appears in root position at the end of a phrase, it lands with full structural weight — there's nothing tentative about it. For this reason, root-position tonic chords mark arrival points: the end of a period, the conclusion of a development section, the final resolution of a piece. In contrast, placing the same tonic chord in **first inversion** (third in the bass) creates a lighter, more passing quality. The harmony is still clearly tonic, but it feels like it's moving through rather than stopping — first-inversion chords are natural constituents of a flowing bass line rather than structural anchors.

**Second-inversion chords** are the most unstable and require careful handling. A tonic chord in second inversion (fifth of the chord — scale degree 5 — in the bass) sounds like it wants to move: the bass note is already the dominant scale degree, and the chord members above it create a suspended quality that calls for resolution. The most common formal use is the **cadential six-four**: I6/4 resolving to V and then to I. The I6/4 is not a stable tonic here — it functions as an intensification of the dominant, its fifth in the bass setting up the dominant root arrival. Recognizing this special function of second-inversion chords prevents the common error of treating them as freely interchangeable with root-position tonic.

The practical upshot is that **bass-line goals often drive inversion choices**. If you want a smooth stepwise descending bass from scale degree 1 to 5, you might write: I (root position, bass on 1) — I6 (first inversion, bass on 3) — IV (root position, bass on 4) — I6/4 (second inversion, bass on 5) — V — I. Every bass note is a step from the previous, yet the harmonies above follow a clear functional arc. This bass-line thinking — building inversions around where you want the bass to go rather than always defaulting to root position — is one of the distinguishing skills of fluent tonal writing, and the place where harmonic function and voice leading most directly intersect.

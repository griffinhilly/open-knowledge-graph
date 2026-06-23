---
id: secondary-dominant-resolution-voice-leading
title: Secondary Dominant Voice Leading and Resolution
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: secondary-dominants
  type: hard
- id: seventh-chord-resolution-tritone
  type: hard
- id: secondary-dominant-extended-voice-leading
  type: soft
- id: authentic-cadence-voice-leading
  type: hard
builds-toward:
- chromatic-borrowed-chords-voice-leading
tags:
- secondary-dominant
- applied-chord
- tonicization
- voice-leading
stage: formal-systems
status: validated
---
# Secondary Dominant Voice Leading and Resolution

## Core Idea
Secondary dominants function like V chords to a key other than the tonic and follow V-chord voice leading rules: the tritone (7th and 3rd of the secondary dominant) must resolve inward to the third of the target chord, and the leading tone resolves up. The resolution must move to the intended target chord (ii, iii, IV, V, or vi). These voice leading requirements create strong directional motion that confirms tonicization.

## How It's Best Learned
Identify secondary dominants in chorale examples and trace the tritone resolution. Write progressions with secondary dominants like V/V-V-I and V/IV-IV-I, listening to how the voice leading creates the tonicization effect.

## Questions

```yaml
- question: "In C major, you write D7 (V/V) resolving to G major. Which voice leading moves are obligatory?"
  type: multiple-choice
  options:
    - "The root D must step down to the root G to anchor the resolution"
    - "All four voices should move to the nearest available chord tone"
    - "F# must resolve up by half step to G, and C must resolve down by half step to B"
    - "F# can move freely since it is a chromatic pitch added outside the key signature"
  answer: 2
  explanation: "The tritone in D7 is F#–C. F# is the local leading tone (third of D7, leading tone of G) and must resolve upward by half step to G. C is the chordal seventh and must resolve downward by half step to B (the third of G major). These two converging motions are what create the tonicization effect. If F# leaps elsewhere or C stays put, the secondary dominant function dissolves — the progression sounds unmotivated rather than purposeful."

- question: "A student writes V/IV (C7) resolving to F major, correctly moving E up to F, but letting Bb leap down to D instead of resolving to A. What is wrong with this voice leading?"
  type: multiple-choice
  options:
    - "E should have resolved downward to Eb, not upward to F"
    - "C7 cannot function as V/IV in C major because C is already the tonic"
    - "The seventh of C7 (Bb) should resolve down by step to A (the third of F major) — leaping to D breaks the tritone resolution"
    - "Nothing is wrong; the seventh of a secondary dominant chord can move freely"
  answer: 2
  explanation: "The tritone in C7 is E–Bb. E (the local leading tone of F) correctly resolves up to F. But Bb is the chordal seventh and must resolve down by step to A — the third of F major. Leaping to D is an unresolved seventh: it abandons the voice leading obligation that makes the secondary dominant convincing. The tritone resolution is the engine of tonicization; both voices must follow through."

- question: "In secondary dominant voice leading, the altered pitch acting as a local leading tone must resolve upward by half step to the root of the target chord."
  type: true-false
  answer: true
  explanation: "Yes — the third of a secondary dominant (e.g., F# in D7 = V/V in C) functions as the leading tone of the temporary tonic and follows leading-tone behavior: it rises by half step to the tonic pitch (G). This is the same rule that governs the seventh-degree in a regular dominant: Ti resolves to Do. The secondary dominant borrows this same resolution logic and applies it to a temporary tonic."

- question: "When a secondary dominant resolves, it is the root of the secondary dominant chord that moves by step to create the sense of resolution."
  type: true-false
  answer: false
  explanation: "The root of a secondary dominant typically leaps — it moves down a fifth (or up a fourth) to the root of the target chord, just as V moves to I by root motion of a fifth. The voices that move by step to create the resolution are the chordal seventh (resolving down by half step) and the third/leading tone (resolving up by half step). The smooth, obligatory stepwise motion belongs to the tritone voices, not the root."

- question: "Why does failing to resolve the tritone in a secondary dominant make the tonicization sound 'unmotivated,' even if the chord symbols are correct?"
  type: short-answer
  answer: "The tonicization effect is created by the converging half-step resolutions of the tritone — the leading tone rising to the local tonic, the seventh falling to the third. These motions produce directed, purposeful voice movement that the ear hears as arrival. If the tritone voices leap or stall instead of resolving, the listener hears no arrival — just a chord change. The secondary dominant label may be technically correct, but the acoustic effect of tonicization depends on the voice leading, not the label."
  explanation: "This is why secondary dominant voice leading is taught as an extension of dominant seventh voice leading, not as a separate category. The same tritone mechanics that make V7–I conclusive are exactly what make V/x–x sound like a local cadence. Remove the tritone resolution, and you remove the tonicization."
```

## Explainer

You already know how the **tritone** in a dominant seventh chord drives resolution. In G7 resolving to C major, the tritone is B–F: B (the third of G7, which is the leading tone of C) resolves up by half step to C, and F (the seventh of G7) resolves down by half step to E. These two converging motions — one rising, one falling — are what make V7–I so conclusive. Secondary dominant voice leading applies this exact same mechanism, but now the "I" that everything resolves toward is a temporary one.

Consider V/V–V in C major. The secondary dominant is D7: D–F#–A–C. This chord functions as a dominant seventh to G major. The tritone in D7 is F#–C: F# is the leading tone of G and resolves up to G; C is the seventh of D7 and resolves down to B (the third of the G major chord). When you write D7 moving to G (major or as a triad), you must follow these resolutions in your voice leading. The F# must move up to G; the C must move down to B. If you don't follow them — if F# leaps somewhere else or C stays — the secondary dominant function dissolves and the progression sounds unmotivated.

The same framework applies to any secondary dominant. For V/ii (A7 resolving to Dm in C major): A7 contains C# and G as its tritone. C# (the leading tone of D minor) resolves up to D; G resolves down to F (the third of Dm). For V/IV (C7 resolving to F major): C7 contains E and Bb as its tritone. E resolves up to F; Bb resolves down to A (the third of F major). In each case, identify the **chordal seventh** and the **altered third** (which acts as the local leading tone), and resolve them by step in the correct direction. These two voices are the engine of tonicization; the remaining voices — root and fifth — have more flexibility in how they move.

One practical complication is the **secondary leading tone in minor keys**. When writing V/V in a minor key, or any secondary dominant that would require raising a pitch that is already in the key signature, you need to add accidentals explicitly. These accidentals are not errors — they are the mechanism by which the secondary dominant creates its chromaticism. Seeing an unexpected sharp or natural in the inner voices of a chorale is often the first signal that a secondary dominant is present. When resolving, those accidentals must follow through: a raised pitch wants to continue rising; a lowered pitch wants to continue falling. Treating the secondary dominant as a complete local V7 — with all of the voice-leading obligations that implies — ensures that the tonicization sounds convincing and the progression moves with harmonic purpose.

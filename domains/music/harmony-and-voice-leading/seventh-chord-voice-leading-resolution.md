---
id: seventh-chord-voice-leading-resolution
title: Seventh Chord Resolution and Voice Leading
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: seventh-chords
  type: hard
- id: voice-leading-smooth-stepwise-motion
  type: hard
- id: dominant-seventh-voice-leading-tritone
  type: hard
builds-toward:
- extended-chords-upper-extensions-voicing
- secondary-dominant-extended-voice-leading
tags:
- seventh-chords
- resolution
- tritone
- voice-leading
stage: formal-systems
status: draft
---

# Seventh Chord Resolution and Voice Leading

## Core Idea
Seventh chords introduce tension through the seventh interval, requiring careful resolution in voice leading. The seventh must resolve downward by step, and the tritone (when present) resolves inward within one measure to the target chord. Different seventh chord types (maj7, min7, dom7, half-diminished) have distinct voice-leading requirements based on their harmonic function and interval content.

## Questions

```yaml
- question: "When a dominant seventh chord (V7) resolves to the tonic (I), which voice-leading motion is obligatory for the seventh of the chord?"
  type: multiple-choice
  options:
    - "The seventh rises by step to the root of the tonic chord"
    - "The seventh resolves downward by step to the third of the tonic chord"
    - "The seventh may move in any direction as long as parallel fifths are avoided"
    - "The seventh is doubled in the tonic chord and can resolve in either direction"
  answer: 1
  explanation: "The seventh always resolves downward by step — this is the fundamental rule of seventh chord voice leading. In G7 resolving to C major, the seventh (F) falls by step to E, the third of the tonic. This downward resolution reflects the dissonant status of the seventh: it was added above the consonant triad, creating tension that the ear resolves by moving toward the nearest stable tone below. Rising resolution moves away from the stability the dissonance is pulling toward."

- question: "A student says that a half-diminished seventh chord (ii°7) resolves 'just like a minor seventh chord.' What is the key error in this claim?"
  type: multiple-choice
  options:
    - "The student is correct — both chord types have identical voice-leading requirements"
    - "The half-diminished chord contains two dissonant intervals (tritone and minor seventh) that both require simultaneous resolution, creating a stronger sense of release than a simple minor seventh"
    - "The half-diminished chord cannot resolve to V; it must resolve directly to I"
    - "The half-diminished chord's resolution is identical to a dominant seventh chord, not a minor seventh"
  answer: 1
  explanation: "The half-diminished seventh chord (ø7) has a diminished fifth (tritone) in addition to the minor seventh — two dissonant intervals requiring simultaneous resolution. The tritone contracts inward (diminished fifth → major third) while the seventh falls by step. A minor seventh chord has only the minor seventh to discharge. The double dissonance of the half-diminished is what makes ii°7–V in minor sound so gravitationally compelling — the buildup and release is more intense than the equivalent progression in major."

- question: "A fully diminished seventh chord can resolve convincingly to four different tonic chords because its notes are related by equal minor-third intervals, making it enharmonically equivalent at multiple pitch levels."
  type: true-false
  answer: true
  explanation: "This is the defining special property of fully diminished seventh chords. Built from stacked minor thirds, respelling any one note enharmonically makes it function as the leading tone of a different key. C#–E–G–Bb can be respelled to resolve to four different targets depending on which voice is treated as the leading tone. Nineteenth-century composers exploited this for rapid modulations: the same chord, respelled, pivots to a completely new key. The flexibility arises directly from the equal-interval symmetry."

- question: "The seventh of a seventh chord may resolve upward when the chord is in inversion, since inversion changes which interval appears at the top of the texture."
  type: true-false
  answer: false
  explanation: "The downward resolution of the seventh is a rule about voice-leading obligation — it applies to whichever voice carries the seventh, regardless of register or inversion. Inversion changes the bass note and the spacing of voices, but it does not change which interval is dissonant or which direction resolves it. The seventh's obligation to move downward by step is independent of its register. Voice-leading analysis tracks individual voices, not just the top of the texture."

- question: "Why does the seventh of a seventh chord resolve downward by step? What is the structural reason this direction is obligatory?"
  type: short-answer
  answer: "The seventh is added above the consonant triad, creating a dissonance with the chord tone immediately below it. Resolving downward by step moves the seventh to the nearest consonant tone below — the smallest motion that discharges the tension. Upward motion would move away from that nearest consonance, maintaining or increasing tension rather than releasing it. The rule captures the voice-leading principle that dissonances resolve toward consonance by the most economical step."
  explanation: "The deeper principle is that dissonances in tonal harmony are 'prepared' and 'resolved': a voice enters a seventh chord as a consonance, becomes dissonant within it, then moves by the smallest step to restore consonance. Downward by step is almost always that smallest path. The direction is not arbitrary convention — it follows from the geometry of the chord: the seventh was added *above* the triad, so it sits above the nearest resolution target and must descend to reach it."
```

## Explainer

You already know seventh chords as four-note structures built by stacking thirds, and you've practiced smooth voice leading that moves voices by step or small leap while avoiding parallel fifths and octaves. The dominant seventh chord's tritone resolution — from your prerequisite work on dominant seventh voice leading — gave you the model: the tritone between the third and seventh of V7 collapses inward, with the third (leading tone) rising to the tonic and the seventh falling by step. Seventh chord voice leading generalizes that pattern across all the chord types you encounter, each with its own profile of stable and unstable intervals.

The unifying rule is: **the seventh always resolves downward by step**. This is not arbitrary convention — it reflects the fact that the seventh is added *above* the consonant triad, creating a dissonance that the ear wants to see "corrected" by moving toward the nearest stable tone below it. In a dominant seventh (G7 resolving to C), the seventh (F) moves down to E — the third of the tonic chord. In a minor seventh chord (Am7 resolving to D or Dm), the seventh (G) moves down to F♯ or F depending on context. In a major seventh chord (Cmaj7 resolving inward), the seventh (B) moves down to the stable consonance below it. The direction of resolution is almost always the same; what changes is the target pitch and the chord that receives the resolution.

The **half-diminished seventh chord** (also written ø7) deserves special attention because it has *two* dissonant intervals that need resolution: a minor seventh and a diminished fifth (tritone). The half-diminished chord frequently appears as ii° in minor keys (the chord built on the second scale degree in minor), and it typically resolves to V. When it does, both the tritone and the seventh must resolve: the tritone resolves inward (the diminished fifth contracts to a third), and the seventh moves downward by step. This double resolution creates a sense of multiple voices simultaneously releasing tension, which is why the ii°7–V progression in minor sounds so gravitationally compelling — it has more dissonance to discharge than the equivalent progression in major.

**Fully diminished seventh chords** (°7) are the most symmetrically tense of the seventh chord types, built entirely from stacked minor thirds, and they have a unique property that complicates their voice leading: they are **enharmonically equivalent at multiple pitch levels**. The chord C♯–E–G–B♭ contains the same pitches as E–G–B♭–D♭ (respelled enharmonically), which means a diminished seventh chord can resolve to four different chords depending on which voice you treat as the leading tone. In practice, the resolution is determined by context and spelling: you identify which voice is the leading tone (the one half a step below a tonicized pitch), and that voice rises while the others resolve to stable chord tones. This flexibility made diminished seventh chords a favorite of nineteenth-century composers for rapid modulations — by respelling one note, the chord can pivot to a completely new key.

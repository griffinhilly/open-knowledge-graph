---
id: seventh-chord-resolution-tritone
title: Seventh Chord Resolution and Tritone Voice Leading
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: seventh-chords
  type: hard
- id: harmonic-function-basics
  type: soft
builds-toward:
- secondary-dominant-resolution-voice-leading
- extended-chords-upper-extensions-voicing
tags:
- seventh-chords
- tritone
- dissonance-resolution
- voice-leading
stage: formal-systems
status: draft
---

# Seventh Chord Resolution and Tritone Voice Leading

## Core Idea
The tritone interval formed between the third and seventh of a seventh chord (e.g., B-F in a G7 chord) creates dissonance that demands resolution. The tritone resolves by inward motion: the upper note steps down to the third of the target chord, the lower note steps up to the seventh. This resolution requirement shapes voice leading in dominant seventh and secondary dominant chords. Proper tritone resolution creates strong harmonic closure and defines the function of the seventh chord.

## How It's Best Learned
Play tritones on an instrument and feel the tension and resolution when voices move inward. Then write V7-I progressions where you resolve the tritone in multiple voicings to internalize the principle.

## Questions

```yaml
- question: "In a G7 chord (G-B-D-F) resolving to C major, which two notes form the tritone and how do they each resolve?"
  type: multiple-choice
  options:
    - "G and D form the tritone; G rises to C and D falls to E"
    - "B and F form the tritone; B rises by half step to C and F falls by half step to E"
    - "B and F form the tritone; both notes move outward — B falls to A and F rises to G"
    - "D and F form the tritone; D falls to C and F rises to G"
  answer: 1
  explanation: "The tritone in G7 is B-F (the third and seventh of the chord). This interval spans an augmented fourth / diminished fifth — exactly three whole tones, creating maximum dissonance. Resolution happens by inward motion: B (the leading tone) rises by half step to C (the tonic), and F (the chordal seventh) falls by half step to E (the third of C major). This inward contraction to the stable C major third is what creates harmonic closure. Option C describes outward motion, which would produce a much weaker or non-functional resolution."

- question: "A composer wants V7-I to feel inconclusive and avoid a strong cadence. Which of the following deviations from conventional tritone resolution would most effectively undermine the sense of closure?"
  type: multiple-choice
  options:
    - "Doubling the root of the dominant seventh chord in the bass"
    - "Resolving the seventh (F) upward to G instead of downward to E, moving the tritone outward rather than inward"
    - "Using a root-position dominant seventh rather than an inversion"
    - "Holding the fifth (D) of the G7 chord through the resolution"
  answer: 1
  explanation: "The inward resolution of the tritone is what creates the feeling of closure. If F resolves upward to G instead of downward to E, the tritone expands outward — exactly the opposite of the conventional resolution. This prevents the voice leading from arriving at the stable third-fifth interval of the tonic chord and undermines the cadential pull. Composers use this deliberately to create deceptive or weakened cadences. Options A, C, and D involve voicing choices that don't fundamentally alter the tritone resolution direction."

- question: "In a dominant seventh chord, the tritone resolves by both voices moving in the same direction — both stepping upward toward the tonic chord."
  type: true-false
  answer: false
  explanation: "The tritone resolves by CONTRARY (inward) motion: the two notes move toward each other, not in the same direction. The upper note of the tritone (the chordal seventh) steps DOWN; the lower note (the chordal third / leading tone) steps UP. In G7 → C: F goes down to E, B goes up to C. This contrary motion is not arbitrary — the leading tone has an inherent upward tendency toward the tonic, while the chordal seventh has an inherent downward tendency. Moving both voices in the same direction would violate these tendencies and produce a much weaker resolution."

- question: "The tendency of the seventh of a dominant chord to resolve downward by step is a fundamental principle of common-practice voice leading."
  type: true-false
  answer: true
  explanation: "In common-practice tonal music (roughly 1600-1900), the chordal seventh consistently resolves downward by step. This downward tendency comes from the dissonant role of the seventh — it must 'resolve' its dissonance by moving to a consonant note in the next chord, and stepwise downward motion is the conventional resolution. The seventh of a V7 chord (e.g., F in G7) resolves to the third of the I chord (E in C major). Composers who violate this — resolving the seventh upward or leaving it unresolved — create intentional tension or unusual effects that listeners trained in this tradition immediately notice."

- question: "Why does the tritone's inward resolution create a stronger sense of harmonic closure than outward (expanding) resolution would?"
  type: short-answer
  answer: "Inward resolution works because it simultaneously satisfies two independent voice-leading tendencies that happen to point toward the same chord. The chordal third (B in G7) is the leading tone — one half step below the tonic — and has strong upward pull toward the tonic note (C). The chordal seventh (F) is a dissonance that must resolve, and its natural direction is downward by step (to E, the third of the tonic chord). These two resolutions converge on the third and root of the tonic chord, creating a complete and stable arrival. Outward expansion would move both voices away from each other into less stable intervals, satisfying neither the leading tone's upward pull nor the seventh's downward tendency — producing continuation rather than closure."
  explanation: "The deeper point is that tritone resolution is overdetermined by tonal voice-leading principles: two independent dissonance-resolution rules both point toward the same inward motion. This double determination is why the V7-I progression became the most conclusive cadence in tonal music — it resolves both the harmonic tension (dominant function) and the contrapuntal tension (tritone dissonance) simultaneously."
```

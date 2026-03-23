---
id: consonance-dissonance-harmonic-function
title: Consonance and Dissonance in Harmony
domain: music
course: music-theory-fundamentals
prerequisites:
- id: interval-quality-by-semitone-count
  type: hard
builds-toward:
- triad-construction-from-scale-degrees
- voice-leading-smooth-motion-and-errors
tags:
- intervals
- consonance
- dissonance
- harmonic-function
stage: formal-systems
status: validated
---

# Consonance and Dissonance in Harmony

## Core Idea
Consonant intervals (unison, octave, perfect fourth, perfect fifth, major/minor third, major/minor sixth) sound stable and require no resolution. Dissonant intervals (major/minor second, major/minor seventh, tritone) sound tense and typically resolve to consonant intervals. This distinction between tension and resolution is fundamental to harmonic progression and voice leading.

## Questions

```yaml
- question: "The tritone is considered the most unstable interval in Western tonal music. What makes it uniquely dissonant compared to other dissonant intervals?"
  type: multiple-choice
  options:
    - "It spans exactly six semitones, which exceeds the natural hearing range for consonance"
    - "It splits the octave exactly in half, lacks strong overtone alignment, and generates bidirectional resolution pressure in both voices"
    - "It always contains two pitches from different diatonic scales, creating a clash between key areas"
    - "It is the only interval that cannot appear within a major scale"
  answer: 1
  explanation: "The tritone's unique instability comes from multiple factors: it divides the octave symmetrically (making it harmonically ambiguous), it has poor alignment with the overtone series (neither pitch strongly reinforces the other's harmonics), and it generates strong bidirectional resolution pressure — both voices want to resolve, either inward or outward. Options C and D are false: the tritone (F–B) occurs naturally within the C major scale."

- question: "In G major, the dominant seventh chord (D–F#–A–C) resolves to the tonic (G–B–D). What happens to the tritone (F#–C) during this resolution?"
  type: multiple-choice
  options:
    - "The tritone dissolves by both voices staying stationary as the harmony changes beneath them"
    - "F# moves up to G and C moves down to B, so the tritone resolves inward to a third"
    - "F# moves down to E and C moves up to D, so the tritone resolves outward to a sixth"
    - "The tritone resolves by the bass note D moving to G, while F# and C remain as passing tones"
  answer: 1
  explanation: "The tritone F#–C resolves inward: F# (the leading tone) moves up by half step to G (the tonic root), and C (the chordal seventh) moves down by half step to B (the tonic third). Both voices move by half step in contrary motion, collapsing the diminished fifth into a major third. This specific inward resolution is what makes dominant-to-tonic feel so inevitable. Option C describes the augmented fourth resolving outward, which is the opposite interval and opposite motion."

- question: "Consonant intervals require resolution because they create harmonic tension in the listener."
  type: true-false
  answer: false
  explanation: "It is dissonant intervals that create tension and require resolution. Consonant intervals (perfect fifths, thirds, sixths, octaves, unisons) sound stable and self-sufficient — they can end a phrase without creating a sense of incompleteness. Dissonant intervals (seconds, sevenths, the tritone) sound tense and incomplete, generating the expectation that they will move to a consonant resolution. This is the most common confusion about this topic: the label (consonant/dissonant) and the behavior (stable/needing resolution) go in opposite directions from what students often assume."

- question: "The cycle of dissonance and resolution — tension sought and dissolved — is what gives tonal music its sense of directed motion and arrival."
  type: true-false
  answer: true
  explanation: "Tonal music is fundamentally organized around the tension-resolution cycle. Dissonant intervals and chords create instability that drives the music forward; their resolution to consonant intervals and stable harmonies creates the sense of arrival. Without dissonance, music has nowhere to go — it remains static. Without resolution, tension accumulates without release. The interplay between the two is the mechanism behind harmonic motion, phrase structure, and the experience of a piece 'going somewhere.'"

- question: "Why does the dominant seventh chord create such strong urgency to resolve to the tonic? Explain the role of its specific intervals."
  type: short-answer
  answer: "The dominant seventh chord (e.g., G–B–D–F in C major) contains two dissonant elements that both demand resolution simultaneously: the tritone between the third and seventh (B–F), and the minor seventh interval (G–F). The tritone wants to resolve inward — B moves up to C and F moves down to E — collapsing into a third on the tonic chord. The seventh also wants to step downward by half step. These two dissonances act together, creating compound urgency that makes the dominant seventh the strongest tension chord in tonal music."
  explanation: "This is why the V7–I progression is the most powerful cadential motion in tonal music. A plain V chord (without the seventh) has only the leading-tone pull; adding the seventh introduces the tritone, which dramatically amplifies the urgency. The stacking of dissonances — tritone plus minor seventh — makes the dominant seventh uniquely effective as a tension generator. When both dissonances resolve together to the tonic chord, the listener experiences a double release that feels conclusive in a way that simple V–I does not."
```

## Explainer

From your work on interval quality and semitone counts, you can already identify any interval by its size and quality — you know that a major seventh spans eleven semitones and a perfect fifth spans seven. Consonance and dissonance take that knowledge one step further: they tell you what those intervals *do* to a listener and how they behave in musical time.

**Consonance** describes intervals that sound stable, complete, and self-sufficient. When you play a perfect fifth (C and G, seven semitones), nothing about the sound demands continuation — it could end there. The same is true of thirds and sixths, which give tonal music its warm, "in tune" quality. **Dissonance** describes intervals that sound tense, incomplete, and unstable. Play a major seventh (C and B, eleven semitones) and you immediately feel a pull toward resolution — the B wants to move up to C, or C wants to move down to B, collapsing the gap into a unison or octave. The most extreme dissonance in Western tonal music is the **tritone** (augmented fourth / diminished fifth, six semitones, like C and F#): it splits the octave exactly in half and generates maximum instability. Medieval theorists called it *diabolus in musica* — the devil in music — because its restless quality is so difficult to ignore.

The physics of consonance involves the **overtone series**: when a string vibrates at a fundamental frequency, it also vibrates at integer multiples — the 2nd harmonic (octave), 3rd harmonic (fifth), 4th, 5th (major third), and so on. Intervals that appear early in the overtone series are consonant because the two pitches share more overtones and "fit" together acoustically. Intervals appearing later in the series — or not at all — generate more acoustic friction. This is why perfect intervals feel purest and thirds feel sweeter than seconds.

What makes this genuinely musical — not just acoustic — is that dissonance has **function**: it creates the expectation of resolution, and resolved dissonance is the engine of tonal harmony. The classic example is the **dominant seventh chord** (C–E–G–B♭ in G major): it contains both a tritone (between B and F) and a minor seventh, stacking two dissonances that urgently demand resolution to the tonic chord. The tritone wants to resolve inward to the tonic's third and fifth; the seventh wants to step down. When the chord resolves, the tension releases. This cycle of tension and resolution — dissonance sought and dissolved — is what gives tonal music its sense of motion, arrival, and meaning. Understanding consonance and dissonance is not just labeling intervals; it's understanding why music feels like it goes somewhere.

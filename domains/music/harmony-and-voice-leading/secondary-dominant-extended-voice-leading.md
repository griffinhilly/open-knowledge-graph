---
id: secondary-dominant-extended-voice-leading
title: Secondary Dominants and Extended Voice-Leading Applications
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: secondary-dominant-introduction
  type: hard
- id: seventh-chord-voice-leading-resolution
  type: hard
- id: dominant-seventh-voice-leading-tritone
  type: hard
builds-toward:
- modulation-enharmonic-pivot-technique
- tonicization-and-modulation-voice-leading
tags:
- secondary-dominant
- applied-chord
- tonicization
- tritone
stage: formal-systems
status: validated
---

# Secondary Dominants and Extended Voice-Leading Applications

## Core Idea
Secondary dominants (V/ii, V/iii, V/IV, V/V, V/vi) apply dominant function to non-tonic chords, creating temporary harmonic emphasis. Voice-leading principles remain consistent: tritone resolution, leading-tone resolution, and smooth stepwise motion. Each secondary dominant can be extended with a seventh, ninth, or other extensions, each requiring careful voice-leading resolution to its target chord's function.

## Questions

```yaml
- question: "In C major, the chord V/V is a dominant seventh chord that resolves to V (G major). Which note functions as the leading tone in V/V, and where does it resolve?"
  type: multiple-choice
  options:
    - "E natural, which resolves up to F — the third of the home tonic"
    - "F# (raised 4th of C major), which resolves up to G — the root of the tonicized V chord"
    - "B natural, which resolves up to C — the home tonic"
    - "F# resolves down to F natural to avoid chromaticism"
  answer: 1
  explanation: "V/V in C major is D–F#–A (or D–F#–A–C as a seventh chord). F# is the leading tone of G major — the tonicized chord — and it resolves upward by half step to G, just as B resolves to C in a standard V–I. The key insight is that secondary dominant voice-leading is calculated relative to the tonicized chord, not the home key. The same resolution principle applies (leading tone rises to tonic), but 'tonic' here means the root of the borrowed-to chord."

- question: "What fundamentally distinguishes a secondary dominant from a borrowed chord (modal mixture)?"
  type: multiple-choice
  options:
    - "Secondary dominants always contain a tritone; borrowed chords never do"
    - "A secondary dominant applies dominant harmonic function to temporarily tonicize a diatonic chord; a borrowed chord imports a chord from the parallel mode without implying tonicization"
    - "Borrowed chords resolve to the tonic; secondary dominants resolve to the dominant"
    - "Secondary dominants are only used in major keys; modal mixture only occurs in minor keys"
  answer: 1
  explanation: "The distinction is functional, not merely chromatic. A secondary dominant creates a local dominant–tonic motion, pointing toward a diatonic chord as if it were a temporary tonic. A borrowed chord (e.g., iv in a major key, borrowed from minor) introduces a modal color without creating dominant function aimed at a new target. Both involve chromatic alteration, but secondary dominants carry voice-leading implications (tritone and leading-tone resolution) that borrowed chords do not."

- question: "The tritone in a secondary dominant resolves the same way as in a primary dominant — the chord seventh falls and the leading tone rises — but the resolution target is the tonicized chord, not the home tonic."
  type: true-false
  answer: true
  explanation: "This is the key insight of secondary dominant voice-leading: the rules don't change, only the reference point shifts. In V7–I, the tritone formed by the seventh and third resolves inward (seventh down by step, leading tone up by half step) to the tonic. In V7/V–V, the same tritone resolution applies, but 'tonic' means the root and third of V. The voice-leading apparatus is identical — what changes is which chord is being treated as the temporary goal."

- question: "When a secondary dominant seventh (e.g., V7/IV) resolves to its target chord, the chord seventh should resolve upward by step to the fifth of the tonicized chord."
  type: true-false
  answer: false
  explanation: "The seventh of a dominant seventh chord always resolves downward by step, never upward — this is true whether it is a primary or secondary dominant. Upward resolution of the seventh would defeat the downward tendency that creates the dominant's sense of pull. In V7/IV resolving to IV, the seventh resolves down by step to the fifth of IV, while the leading tone resolves upward. Confusing the seventh (resolves down) with the leading tone (resolves up) is a common voice-leading error."

- question: "Why do the same voice-leading rules that govern primary dominant resolution — tritone resolution, leading-tone pull, smooth stepwise motion — apply equally to secondary dominants?"
  type: short-answer
  answer: "Secondary dominants borrow dominant function and apply it to a different target. Dominant function is not specific to the home tonic — it is a harmonic relationship between a chord containing a tritone and the chord a fifth below whose root and third resolve that tritone. Any chord can be temporarily treated as a local tonic, and the dominant-to-tonic motion that drives voice-leading in the primary key operates identically in the secondary context. The rules are not key-specific; they are function-specific."
  explanation: "This is why understanding secondary dominants deepens your grasp of voice-leading as a whole: it reveals that the tritone resolution, leading-tone pull, and stepwise motion are properties of dominant function itself, not of the particular key. Once you internalize this, secondary dominants stop feeling like exceptions and start feeling like applications of the same underlying logic — transposed to a new local tonic."
```

## Explainer

From your prerequisites in secondary dominant introduction, seventh-chord resolution, and dominant-seventh tritone voice leading, you know the core mechanism: a secondary dominant borrows dominant function from another key and applies it to a diatonic chord, and the tritone within a dominant seventh chord resolves by inward contrary motion (the leading tone rises, the seventh falls). Extended voice-leading applications take this further — systematically working through all five common secondary dominants (V/ii, V/iii, V/IV, V/V, V/vi) and their seventh-chord forms, understanding how each one's chromatic content creates specific voice-leading obligations.

The unifying principle is that **voice-leading rules are function-specific, not key-specific**. The leading tone of any dominant chord resolves upward by half step to the root of its target chord. The seventh of any dominant seventh chord resolves downward by step. The tritone formed between the third and seventh contracts inward. These rules apply identically whether the chord is the primary V7 resolving to I or a secondary V7/vi resolving to vi. In C major, V7/V is the chord D-F#-A-C: F# is the leading tone of G (the tonicized chord), and it resolves upward to G. C is the seventh, and it resolves downward to B. The tritone F#-C resolves inward: F# rises to G, C falls to B. This is the same pattern as G7-C (B rises to C, F falls to E), just shifted to a new reference point.

Each secondary dominant introduces a **specific chromatic pitch** that functions as the temporary leading tone. V/ii introduces #1 (C# in C major, pointing to D). V/iii introduces #2 (D# in C major, pointing to E). V/IV is unique — it is built on the tonic pitch (C-E-G-Bb in C major) and introduces b7 (Bb, the seventh of the chord), which resolves down to A (the third of IV). V/V introduces #4 (F# in C major, pointing to G). V/vi introduces #5 (G# in C major, pointing to A). Each chromatic pitch must be **approached smoothly** — typically by half step from its diatonic neighbor — and **resolved correctly** to the root of its target chord.

When secondary dominants are extended with ninths or other upper voices, the additional tones create further resolution obligations that follow the same logic. A V9/ii chord adds the ninth above the root of the applied dominant, and this ninth typically resolves down by step to the fifth of the tonicized chord. The practical discipline is consistent: identify which note is the temporary leading tone, resolve it upward; identify which note is the chordal seventh, resolve it downward; resolve the tritone inward; move all other voices by the smoothest available path. Once you internalize this as a **transferable pattern** rather than five separate rules for five separate chords, secondary dominants stop being a confusing catalogue of chromatic exceptions and become straightforward applications of dominant voice-leading logic aimed at different targets.

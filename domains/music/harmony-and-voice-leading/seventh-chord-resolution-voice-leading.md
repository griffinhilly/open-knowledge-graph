---
id: seventh-chord-resolution-voice-leading
title: Seventh Chord Resolution and Voice Leading
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: seventh-chords
  type: hard
- id: voice-leading-principles
  type: hard
- id: dominant-seventh-function-resolution
  type: soft
builds-toward:
- extended-harmony-voice-leading-handling
tags:
- seventh-chords
- resolution
- dissonance
stage: formal-systems
status: draft
---

# Seventh Chord Resolution and Voice Leading

## Core Idea
The seventh of a seventh chord must resolve down by step, and the tritone between the third and seventh of a dominant seventh requires specific resolution. The bass note independently follows harmonic function, while upper voices resolve their dissonant intervals. This creates the characteristic voice-leading sound of seventh chords.

## Questions

```yaml
- question: "A ii7 chord in C major (D-F-A-C) resolves to V (G-B-D). The seventh of ii7 is C (scale degree 1). Where does this voice go in the resolution?"
  type: multiple-choice
  options:
    - "It rises by step to D, doubling the root of the V chord"
    - "It falls by step to B, the third of the V chord"
    - "It stays on C as a common tone, since C is in both chords"
    - "It can resolve freely in either direction depending on the soprano line"
  answer: 1
  explanation: "The seventh of any seventh chord must resolve downward by step. C (scale degree 1) falls by step to B (scale degree 7, the leading tone), which is the third of V. The tempting wrong answer is option C: although C is in the key of C major, it is NOT a common tone between ii7 and V (which contains G, B, D) — the seventh must resolve rather than remain. Option A would be an upward resolution of the seventh, which violates the fundamental rule."

- question: "A student writes a V7→I progression but resolves the seventh of V7 (scale degree 4, F in C major) upward by step to G. What voice-leading rule is violated?"
  type: multiple-choice
  options:
    - "The leading tone must resolve upward to tonic"
    - "The seventh of the chord must resolve downward by step"
    - "No parallel fifths are allowed between any two voices"
    - "The bass must move by fourth or fifth at all cadences"
  answer: 1
  explanation: "The seventh of a seventh chord must resolve downward by step — this is the fundamental rule of seventh-chord voice leading. F (scale degree 4) must fall to E (scale degree 3), the third of the I chord. Resolving the seventh upward to G violates this obligatory direction. The acoustic rationale: the seventh sits above the root with a natural downward tendency; resolving it upward fights this tendency and weakens the harmonic arrival."

- question: "The dominant seventh chord (V7) is special because it is the only seventh chord in tonal music that contains a dissonant interval."
  type: true-false
  answer: false
  explanation: "All seventh chords contain a dissonant seventh interval between their root and seventh — that's what makes them seventh chords. V7 is special not because it's the only dissonant seventh chord but because it additionally contains a tritone between its third (the leading tone, scale degree 7) and its seventh (scale degree 4). This double dissonance — the seventh and the tritone resolving simultaneously — is why V7→I sounds so conclusive. Non-dominant seventh chords are also dissonant; they simply lack the extra tritone urgency."

- question: "In a V7→I resolution, both the leading tone and the seventh of the chord have specific obligatory resolution directions."
  type: true-false
  answer: true
  explanation: "Yes — this is what makes V7→I structurally compelling. The leading tone (scale degree 7, the third of V7) must rise by half step to tonic; the seventh (scale degree 4) must fall by step to scale degree 3. These two resolutions happen simultaneously, releasing the tritone tension by both voices moving inward toward each other. The bass follows harmonic function (root of V to root of I), while these two upper voices resolve their specific dissonances — all together producing the characteristic cadential sound."

- question: "Why must the seventh of a seventh chord resolve downward rather than upward, and does this rule apply only to dominant seventh chords or to all seventh chords?"
  type: short-answer
  answer: "The seventh is an acoustically restless interval — it sits a step below the octave of the root, and its natural tendency is to collapse by step downward to a more consonant position in the resolution chord. Resolving it downward moves toward the nearest consonant chord tone; resolving it upward skips over consonant tones and weakens the harmonic arrival. This rule applies to all seventh chords, not just V7: whether it is ii7, IV7, viio7, or any other, the voice carrying the seventh must resolve down by step."
  explanation: "The rule's universality is important: ii7→V, IV7→I, viio7→I all require the seventh to resolve downward. V7 is the most prominent case because of its structural role and the added tritone, but the seventh-resolution rule is a general principle of tonal voice leading. Understanding it as universal — dissonance resolves in the direction of least resistance, which for the seventh is downward — gives you the framework to handle any seventh chord correctly, not just the dominant."
```

## Explainer

You already know how to build seventh chords and understand basic voice-leading principles. From your prerequisite work on the dominant seventh, you know that V7 has a specific resolution pattern. This topic generalizes that knowledge: every seventh chord creates dissonance — a seventh interval between its root and seventh — and dissonance in tonal music is governed by a simple principle: it must resolve, and resolution means moving in the direction that relieves the tension.

The **seventh of any seventh chord** must resolve downward by step. This is not an arbitrary rule — it reflects the acoustic behavior of dissonant intervals. The seventh is a note that does not fit neatly into the harmonic series of the chord's root; it sits an octave minus a step above the root, and its natural tendency is to collapse by half step or whole step downward to a more consonant position. When you write a ii7 chord resolving to V, the seventh of ii7 — the tonic pitch — resolves down by step to the leading tone of V. When IV7 moves to I, its seventh resolves down by step. The bass note follows the chord's harmonic function (moving by fourth or fifth as roots typically do), while the upper voice carrying the seventh moves by step. These two movements operate independently but together create the characteristic flow.

The **dominant seventh chord** is the special case because it contains not just the dissonance of the seventh but also a **tritone** — the interval between the third (leading tone, 7̂) and the seventh (4̂). Your prerequisite knowledge covers this in detail: the tritone resolves by both voices moving inward, toward each other, by half step. The leading tone rises to tonic; the seventh falls to the third scale degree. This double resolution is why V7 → I sounds so conclusive — two dissonant intervals resolve simultaneously, releasing maximum tension. When you write V7 in first inversion or with incomplete doubling, the tritone resolution still drives the voice leading; the bass simply follows a different path.

Non-dominant seventh chords — ii7, IV7, viio7, and others — follow the same seventh-resolution rule but without the tritone's extra intensity. The **leading-tone seventh chord** (viio7 or viiø7) is the most dissonant diatonic seventh chord after V7; it contains two tritones in its fully-diminished form and resolves with maximum urgency to I. When you write it, all four voices have specific places to go: the root resolves up by half step (leading tone behavior), the third resolves down by half step (resolving a tritone), the fifth resolves down by step, and the seventh resolves down by step. Mastering these resolution patterns across chord types gives you the fluency to write convincingly functional voice leading in any harmonic context.

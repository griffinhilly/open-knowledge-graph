---
id: tritone-resolution-direction
title: Tritone Resolution Direction and Voice-Leading
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: interval-quality
  type: hard
- id: voice-leading-principles
  type: hard
builds-toward:
- dominant-seventh-voice-leading-tritone
tags:
- tritone
- interval
- voice-leading
stage: formal-systems
status: draft
---

# Tritone Resolution Direction and Voice-Leading

## Core Idea
Tritones (augmented fourths and diminished fifths) must resolve by contrary motion: augmented fourths expand outward to a fifth; diminished fifths contract inward to a fourth. This resolution convention drives harmonic closure and voice-leading direction.

## Questions

```yaml
- question: "In C major, the tritone B–F within a G7 chord resolves to C major (I). What interval do B and F move to, and in which directions?"
  type: multiple-choice
  options:
    - "B and F both move inward, both descending to form a unison on C"
    - "B moves up a half step to C, and F moves down a half step to E — contrary motion, resolving the diminished fifth to a major third"
    - "B moves down a half step to B♭, and F stays, since it is already the tonic's third"
    - "B and F both expand outward — B down to A and F up to G — to form a fifth"
  answer: 1
  explanation: "The tritone B–F in G7 is spelled as a diminished fifth (B on bottom, F on top). Diminished fifths contract inward by half step: B moves up to C (the leading tone resolves to tonic) and F moves down to E (the fourth scale degree resolves to the third). The result is a major third C–E. This contrary motion — both voices moving toward each other — is the voice-leading mechanism that makes the V–I cadence feel inevitable. The leading tone's upward pull and the fourth degree's downward pull are each driven by half-step gravity."

- question: "Which factor determines whether a tritone resolves by expanding outward or contracting inward?"
  type: multiple-choice
  options:
    - "Whether the tritone is between two white keys or involves an accidental"
    - "Whether the tritone is spelled as an augmented fourth (expands outward) or a diminished fifth (contracts inward) — determined by which note occupies the lower position"
    - "The tempo of the piece — faster passages expand outward, slower passages contract inward"
    - "The instrument — string instruments expand, wind instruments contract"
  answer: 1
  explanation: "The same two pitches (say, B and F) can be spelled either as a diminished fifth (B below F) or an augmented fourth (F below B). Diminished fifths contract inward to a third; augmented fourths expand outward to a sixth. The direction is determined by the voice-leading context — specifically, which note is the leading tone and which is the fourth scale degree. It is the spelling and position within the key, not any acoustic feature, that determines resolution direction."

- question: "An augmented fourth and a diminished fifth are enharmonically equivalent in equal temperament (same number of half steps) but resolve in opposite directions."
  type: true-false
  answer: true
  explanation: "Both the augmented fourth and diminished fifth span exactly 6 half steps — they sound the same in equal temperament. But their voice-leading resolutions differ based on spelling and context. An augmented fourth (like F–B in C major, with F below) expands outward to a major sixth or fifth. A diminished fifth (like B–F with B below) contracts inward to a major third. The same two pitches, spelled differently, create different tonal functions and resolve in opposite directions — a vivid example of how tonal context, not just acoustic content, drives voice leading."

- question: "If a composer keeps the leading tone stationary (not resolving upward) at a V–I cadence, this is considered standard voice-leading practice and has no effect on the sense of tonal resolution."
  type: true-false
  answer: false
  explanation: "The leading tone is scale degree 7, one half step below the tonic, and has a strong conventional pull upward. Failing to resolve it at a V–I cadence creates a friction against expectation — the ear anticipates the half-step ascent and is left unsatisfied. In strict tonal voice leading, the leading tone must ascend to the tonic. When a composer deliberately holds it down, it reads as a deceptive effect or error, not neutral practice. This resolution is not arbitrary convention but reflects the natural gravitational pull of the tritone's half-step resolution structure."

- question: "Why does the tritone in a dominant seventh chord resolve by contrary motion, and what is the connection to the leading tone?"
  type: short-answer
  answer: "The dominant seventh chord contains a tritone between the leading tone (scale degree 7) and the fourth scale degree. The leading tone has natural upward pull by half step to the tonic; the fourth scale degree has natural downward pull by half step to the third. When both resolutions happen simultaneously — the leading tone ascending and the fourth descending — the two voices move toward each other (contrary motion), and the tritone resolves. The contrary motion is not an arbitrary rule but the simultaneous expression of two independent half-step gravitational pulls."
  explanation: "This is the physical mechanism behind harmonic closure in tonal music. The tritone in G7 (B–F in C major) packs two half-step resolutions into one interval: B wants to move up to C (leading-tone resolution) and F wants to move down to E (fourth-degree resolution). Because these movements go in opposite directions, contrary motion is the natural outcome. Understanding this means you can predict voice-leading behavior in any tonal context that contains a tritone, not just in dominant seventh chords — including diminished sevenths, leading-tone triads, and chromatic passing harmonies."
```

## Explainer

The tritone — an interval spanning exactly three whole steps, equivalent to six half steps — has been called the *diabolus in musica* by medieval theorists. Its sonic character is unstable and demanding: neither the brightness of a perfect fifth nor the sweetness of a third, the tritone creates a tension that strongly implies motion. Understanding *which direction* that motion goes is one of the most practically useful concepts in voice leading, because the tritone appears in every dominant seventh chord and therefore governs every authentic cadence.

From your prerequisite work with interval quality, you know that the tritone appears in two enharmonically equivalent forms: the **augmented fourth** (like F to B♭ in C major — wait, actually F to B in C major) and the **diminished fifth** (like B to F in C major). These are the same size in equal temperament but resolve differently because of the voice-leading context. The rule is: **augmented fourths expand outward** to a major sixth or fifth, while **diminished fifths contract inward** to a major third or fourth. The direction of resolution is determined by which note is the leading tone and which is the fourth scale degree — the same two notes, but the direction each moves depends on which one is "above" and which is "below."

The most important application is the **dominant seventh chord**. In C major, the G7 chord contains the tritone B–F: B is the leading tone (scale degree 7, pulling upward to the tonic C), and F is the fourth scale degree (pulling downward to the third, E). When this chord resolves to I, B moves up a half step to C and F moves down a half step to E — contrary motion, each moving toward their nearest resolution. This is not a stylistic convention but a consequence of the natural tendency of each pitch within the key. The leading tone *must* ascend; the fourth degree has strong gravitational pull downward. The tritone resolution is the acoustical and tonal logic that makes the V–I cadence feel inevitable rather than arbitrary.

This principle extends to every chord containing a tritone, including **diminished seventh chords** (which contain two tritones simultaneously, creating even greater tension) and the **leading-tone triad** (vii°). In each case, identifying the tritone within the chord and applying the expansion/contraction rule predicts how the chord should resolve. When you violate these resolutions — holding a leading tone down, or moving the fourth scale degree upward — you create a friction against expectation that, in tonal music, reads as an error or an intentional deceptive effect. Fluency with tritone resolution is therefore not just a rule to follow but a tool for understanding *why* tonal harmony sounds the way it does: the gravitational pull of half-step resolutions, directed by contrary motion, is the physical mechanism underneath harmonic tension and release.


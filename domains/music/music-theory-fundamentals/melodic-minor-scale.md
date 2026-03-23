---
id: melodic-minor-scale
title: Melodic Minor Scale
domain: music
course: music-theory-fundamentals
prerequisites:
- id: natural-minor-scale
  type: hard
- id: harmonic-minor-scale
  type: soft
builds-toward:
- minor-scales
- melodic-writing
- jazz-harmony-basics
tags:
- scales
- minor
- melodic
- ascending
stage: formal-systems
status: validated
---

# Melodic Minor Scale

## Core Idea
Melodic minor raises both the 6th and 7th degrees when ascending, avoiding the awkward augmented 2nd of harmonic minor while maintaining a leading tone. When descending, it typically reverts to natural minor. This dual nature makes melodic minor ideal for smooth, singable melodies.

## How It's Best Learned
Build melodic minor ascending and then descending (as natural minor) to feel the directional quality. Sing melodic minor scales in both directions. Listen for how it eliminates the augmented 2nd that appears in harmonic minor.

## Common Misconceptions
Melodic minor has fixed pitches regardless of direction (it changes ascending vs. descending). Confusing it with harmonic minor (harmonic doesn't raise the 6th when ascending). Assuming descending melodic minor uses raised 6 and 7.

## Questions

```yaml
- question: "In A melodic minor ascending, which scale degrees are raised compared to A natural minor?"
  type: multiple-choice
  options:
    - "Only the 7th degree (G → G♯), to create a leading tone"
    - "Only the 6th degree (F → F♯), to smooth the step from scale degree 5"
    - "Both the 6th and 7th degrees (F → F♯ and G → G♯)"
    - "The 6th, 7th, and 3rd degrees, to approach the tonic from multiple directions"
  answer: 2
  explanation: "Melodic minor raises both the 6th and 7th ascending. The 7th is raised to create a leading tone (a semitone below the tonic); the 6th is raised to eliminate the augmented 2nd that would otherwise appear between ♭6 and ♯7. Raising only the 7th (as harmonic minor does) leaves the awkward augmented second intact."

- question: "A violinist descends from the tonic through a melodic minor scale. Which pitches does she use for scale degrees 7 and 6?"
  type: multiple-choice
  options:
    - "The raised versions (♯7 and ♯6) — the same as ascending, for consistency"
    - "The raised 7th but the natural 6th — the same as harmonic minor descending"
    - "The natural versions (♭7 and ♭6) — reverting to natural minor descending"
    - "Either set of pitches, since the choice is purely ornamental"
  answer: 2
  explanation: "In traditional practice, melodic minor descends using natural minor — both the 6th and 7th revert to their unraised forms. Descending toward the tonic does not require a leading tone, so the pull of ♯7 is unnecessary; using natural minor's ♭7 and ♭6 gives a smooth, relaxed descent. This bidirectional character — two different pitch sets depending on direction — is melodic minor's defining feature."

- question: "The harmonic minor scale raises both the 6th and 7th scale degrees to eliminate the augmented second."
  type: true-false
  answer: false
  explanation: "Harmonic minor raises only the 7th scale degree, creating a leading tone. This produces an augmented second between the unraised ♭6 and the raised ♯7. Melodic minor is the scale that solves this problem by also raising the 6th ascending, smoothing out the gap. Confusing harmonic and melodic minor on this point is one of the most common errors in scale theory."

- question: "Melodic minor uses different pitches when ascending versus descending in traditional practice."
  type: true-false
  answer: true
  explanation: "This bidirectional character is what defines melodic minor. Ascending, both 6th and 7th are raised for smooth approach to the tonic with a leading tone. Descending, both revert to their natural-minor positions, because the leading-tone pull is unnecessary when moving away from the tonic. It is the only standard scale that explicitly changes based on melodic direction."

- question: "What problem does melodic minor solve that harmonic minor creates, and how does it solve it?"
  type: short-answer
  answer: "Harmonic minor raises the 7th scale degree to create a leading tone, but this leaves an augmented second (three semitones) between the ♭6 and the raised ♯7 — an interval too large to sing smoothly. Melodic minor solves this by also raising the 6th degree ascending, filling the augmented second with a smooth whole step while preserving the leading tone. The descending form reverts to natural minor because the leading tone is not needed moving away from the tonic."
  explanation: "The augmented second is not just a technical problem — it gives harmonic minor its distinctive exotic or Eastern quality, which is expressive in some contexts but inappropriate for smooth singable melody. Melodic minor is a practical solution: optimize the ascending path for smooth stepwise motion toward the tonic, and relax back to natural minor on the way down."
```

## Explainer

Start from what you know. The **natural minor scale** has a ♭7 — the seventh scale degree is a whole step below the tonic rather than a half step. This means there is no **leading tone**: no note that sits a semitone below the tonic and pulls strongly upward toward it. Natural minor's floating, unresolved quality can be expressive, but it also makes it difficult to write melodies or harmonies that strongly arrive on the tonic. The V chord in natural minor is a minor chord, which lacks the pull of a major dominant.

**Harmonic minor** solves the leading-tone problem by raising the 7th scale degree. The V chord is now major (with the raised 7th as its third), creating a powerful V–i pull. But harmonic minor introduces a new problem: between the ♭6 and the raised ♯7, there is now an **augmented second** — an interval of three semitones. This gap is larger than a whole step, and it creates a distinctive exotic or "Eastern" sound that is awkward to sing smoothly. For composed melodies that need to pass through this part of the scale, harmonic minor creates friction.

**Melodic minor** resolves this by raising *both* the 6th and 7th degrees when ascending. The raised 7th preserves the leading-tone pull toward the tonic; the raised 6th fills in the augmented second with a smooth whole step. The ascending scale is entirely stepwise and singable. When descending, however, the pull toward the tonic is less relevant — you're moving away from it — so the traditional practice is to revert to natural minor on the way down, restoring both ♭7 and ♭6. This gives melodic minor its distinctive **bidirectional character**: different pitches ascending versus descending, each optimized for the melodic direction it serves. Think of it as a scale that is efficient: it uses the pitches that serve the music at each moment. In jazz theory, "melodic minor" typically refers only to the ascending form, used in both directions — this simplification produces a scale with a particularly rich set of modes that underpin jazz harmony, which you'll encounter in later topics.


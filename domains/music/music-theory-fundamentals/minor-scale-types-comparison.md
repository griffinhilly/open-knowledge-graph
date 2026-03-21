---
id: minor-scale-types-comparison
title: Comparing Natural, Harmonic, and Melodic Minor
domain: music
course: music-theory-fundamentals
prerequisites:
- id: natural-minor-scale
  type: hard
- id: harmonic-minor-scale
  type: hard
- id: melodic-minor-scale
  type: hard
builds-toward:
- diatonic-triad-harmonization
- harmonic-function-basics
tags:
- minor-scale
- scale-variants
- harmonic-context
stage: formal-systems
status: draft
---

# Comparing Natural, Harmonic, and Melodic Minor

## Core Idea
Natural minor has a lowered third, sixth, and seventh compared to major. Harmonic minor raises the seventh to create a leading tone and a strong dominant seventh chord. Melodic minor raises both sixth and seventh when ascending (like major in the upper tetrachord) but returns to natural minor when descending. Each variant serves different compositional purposes and harmonic contexts.

## How It's Best Learned
Write all three forms of a minor scale side-by-side and listen to their differences. Analyze where each form appears in actual compositions.

## Common Misconceptions
- Thinking melodic minor always has raised sixth and seventh (it only does ascending).
- Not recognizing that harmonic minor is rarely used purely melodically because of its large interval.

## Questions

```yaml
- question: "A composer writing in A minor needs to harmonize a cadence with maximum gravitational pull toward the tonic. Which scale form provides the necessary leading tone?"
  type: multiple-choice
  options:
    - "Natural minor — it contains the authentic minor sound that defines the key"
    - "Harmonic minor — it raises the seventh scale degree to create a leading tone and a major dominant chord"
    - "Melodic minor — it provides the smoothest melodic motion toward the tonic"
    - "Any minor scale works equally well for cadences — the choice is purely stylistic"
  answer: 1
  explanation: "Strong cadential pull depends on the leading tone — scale degree 7 sitting a half-step below the tonic. Natural minor has a lowered seventh, making the dominant chord minor (weak pull). Harmonic minor raises the seventh, restoring the leading tone and making the dominant major or dominant-seventh — creating powerful cadential motion. This is exactly why it's called 'harmonic' minor: it was developed to solve the harmonic problem of weak cadences in natural minor."

- question: "A singer performing a minor-key melody that ascends stepwise toward the high tonic finds an awkward, wide interval using harmonic minor. What causes it, and how does melodic minor address it?"
  type: multiple-choice
  options:
    - "The leading tone is too high, so melodic minor lowers the seventh to fix the range"
    - "The raised seventh creates an augmented second between b6 and the raised 7, which is melodically awkward; melodic minor also raises the sixth to eliminate this gap"
    - "Harmonic minor has too many sharps, so melodic minor reduces them for ease of performance"
    - "There is no awkward interval in harmonic minor — the augmented second only occurs when descending"
  answer: 1
  explanation: "Harmonic minor's fix — raising the seventh — creates an augmented second (three semitones) between the lowered sixth (b6) and the raised seventh. This is harmonically powerful but melodically ungainly, especially in vocal writing. Melodic minor addresses this by also raising the sixth, creating a smooth stepwise ascent that matches the major scale's upper tetrachord. When descending, the leading-tone pull is no longer needed, so both alterations are dropped."

- question: "Harmonic minor raises only the seventh scale degree compared to natural minor, and this creates an augmented second interval between the sixth and seventh degrees."
  type: true-false
  answer: true
  explanation: "Natural minor has b6 and b7. Harmonic minor raises b7 to the natural seventh (the leading tone), leaving b6 unchanged. The interval between b6 and the natural 7 spans three semitones — an augmented second. This is what makes harmonic minor melodically awkward for ascending lines but harmonically useful for cadential progressions where strong dominant-to-tonic resolution is needed."

- question: "Melodic minor uses raised sixth and seventh scale degrees in both ascending and descending directions."
  type: true-false
  answer: false
  explanation: "Melodic minor uses raised sixth and seventh only when ascending toward the tonic, where the leading tone's pull is needed and smooth stepwise motion matters most. When descending away from the tonic, the leading-tone drive is no longer needed, so both alterations are dropped and the scale reverts to natural minor. The asymmetry — different notes ascending and descending — is the defining feature of melodic minor, directly reflecting its functional purpose."

- question: "Why do three different minor scale forms exist rather than a single universal minor scale?"
  type: short-answer
  answer: "Three forms exist because no single minor scale simultaneously satisfies all musical needs. Natural minor captures the authentic minor color but lacks a leading tone, giving it weak dominant-to-tonic cadential motion. Harmonic minor fixes the cadential problem by raising the seventh but creates an awkward augmented second in melodic lines. Melodic minor fixes the melodic awkwardness by also raising the sixth ascending while reverting to natural minor descending. Each form is a solution to a different tension between harmonic function and melodic smoothness."
  explanation: "The three forms coexist within a single piece rather than competing. A composer might use a harmonic minor dominant chord at a cadence, a natural minor sixth degree in a melody, and a melodic minor passage when a line ascends to the tonic — sometimes within the same phrase. Understanding which form is active at any moment requires knowing whether the context is primarily harmonic (cadential) or melodic (linear motion), and whether the line is ascending or descending."
```

## Explainer

You already know each of the three minor scale types individually. The real skill is understanding *why* there are three forms rather than one, and what problem each one solves. That understanding comes from recognizing the tension at the heart of minor tonality: the natural minor scale captures the authentic sound of the minor mode, but it creates harmonic problems that composers have solved in two different ways.

**Natural minor** is the foundation: scale degrees 1–2–b3–4–5–b6–b7–1. Its distinctively minor color comes from the lowered third (giving that characteristic "sad" quality), but also from the lowered seventh. That lowered seventh is the issue. In major tonality, the seventh scale degree sits a half-step below the tonic — it wants to resolve upward. This is the **leading tone**, and it gives the dominant chord (built on scale degree 5) its powerful drive back to the tonic. In natural minor, the lowered seventh means the dominant chord is a minor chord — weaker, with less gravitational pull toward home.

**Harmonic minor** fixes this by raising the seventh a half-step back to match the major scale. Now the dominant chord is major (or dominant seventh), and the leading-tone resolution is restored. This is exactly the harmonic context composers used when they needed strong cadential motion in minor keys — hence the name "harmonic" minor. But the fix creates a side effect: between the b6 and the raised 7, there is now an **augmented second** (three half-steps). This interval sounds unusual and tense when sung or played melodically. It's great for the harmonically important moment of resolution; it's awkward as a melody.

**Melodic minor** solves the melodic awkwardness. When ascending toward the tonic — the direction where leading-tone drive matters most — it raises both the sixth and seventh to eliminate the augmented second while preserving the leading tone. When descending away from the tonic, there's no need for the leading tone's pull, so it reverts to natural minor for a smooth, stepwise descent. The result is a scale that is, in a sense, context-dependent: its shape changes based on direction and harmonic function.

In practice, these three forms coexist within a single piece rather than appearing in isolation. A composer might use a harmonic minor dominant chord at a cadence, natural minor sixth degree in a melody, and melodic minor passage when a line ascends to the tonic. Learning to recognize which form is in play at any moment — and why — is the foundation for analyzing diatonic harmony in minor keys, which builds directly on this comparison.

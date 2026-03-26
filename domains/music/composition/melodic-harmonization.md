---
id: melodic-harmonization
title: Melodic Harmonization
domain: music
course: composition
prerequisites:
- id: roman-numeral-analysis
  type: hard
- id: chord-progressions
  type: hard
- id: non-chord-tones
  type: hard
- id: harmonic-rhythm
  type: soft
builds-toward:
- bass-line-composition
- arranging-for-small-ensemble
- lead-sheet-notation
tags:
- harmonization
- melody
- chord-choice
- non-chord-tones
- voice-leading
stage: formal-systems
status: validated
---

# Melodic Harmonization

## Core Idea
Harmonizing a melody means selecting chords that support each melodic pitch while forming a coherent, expressive harmonic progression. The melody note may function as the root, third, fifth, or a non-chord tone (passing tone, neighbor tone, suspension) of each chosen chord, giving the composer multiple viable harmonizations for any given note. Choosing among these options requires weighing melodic accent, harmonic rhythm, voice-leading smoothness, and formal function.

## How It's Best Learned
Take a simple eight-measure melody and write out three distinct harmonizations using different chord choices; compare how each version changes the emotional character and phrase direction.

## Common Misconceptions
- Every melody note does not require a chord change — holding a chord through non-chord tones is often more effective than changing harmony on every beat.
- The 'obvious' harmonization is not always the best; unexpected chord choices can transform a plain melody into something distinctive.

## Questions

```yaml
- question: "A melody has a chord tone on beat 1 followed by a stepwise passing eighth note on the 'and' of beat 1 that doesn't belong to any obvious chord. What should a skilled harmonizer typically do?"
  type: multiple-choice
  options:
    - "Find a new chord that contains the passing note so every melody note is harmonized"
    - "Hold the chord from beat 1 through the passing note, treating it as a non-chord tone"
    - "Remove the passing note from the melody to simplify harmonization"
    - "Use a chromatic chord under the passing note to add color"
  answer: 1
  explanation: "Non-chord tones — passing tones, neighbor tones, suspensions — are a compositional tool, not a problem to solve with chord changes. Holding the chord and treating the weak-beat note as a passing tone is nearly always more graceful than scrambling to find a new chord for every note. Changing harmony on every beat to accommodate passing tones destroys harmonic rhythm and misuses the concept of non-chord tones entirely."

- question: "A harmonizer wants a phrase to end with a strong sense of closure. Which approach best reflects deliberate, expert practice?"
  type: multiple-choice
  options:
    - "Harmonize the melody note by note from the beginning and see what cadence results naturally"
    - "Use IV–V–I at every phrase ending to guarantee closure"
    - "Decide on the cadence type first, then choose interior chords that lead convincingly toward it"
    - "Increase harmonic rhythm near the end to create more motion approaching the final note"
  answer: 2
  explanation: "Expert harmonization is end-directed: you choose the cadence type first (authentic for closure, half cadence for expectancy, deceptive for surprise), then build backward to find chords that create a convincing path toward that arrival. Harmonizing left-to-right without a target cadence tends to produce aimless progressions that land at the end by accident rather than design."

- question: "A melody note falling on a strong beat most naturally functions as a chord tone (root, third, or fifth) of the chord sounding beneath it."
  type: true-false
  answer: true
  explanation: "Strong-beat melody notes are structural tones that the ear hears as defining the harmony. Placing a non-chord tone on a strong beat creates dissonance that sounds like an error rather than an ornament. Skilled harmonization anchors chord tones to strong beats and reserves weak beats for non-chord tones — identifying structural tones is the first step in any harmonization."

- question: "The most effective melodic harmonizations change the chord on nearly every beat so that nearly every melody note belongs to the chord currently sounding."
  type: true-false
  answer: false
  explanation: "This is one of the most persistent beginner mistakes. Holding a chord across a non-chord tone is nearly always more graceful than assigning a new chord to every note. Over-harmonization produces choppy progressions and destroys harmonic rhythm — one of the most expressive levers in harmonization. Slower harmonic rhythm creates spaciousness and inevitability; dense chord changes belong only where the music genuinely requires that density."

- question: "Explain why a harmonizer typically decides on the cadence type before choosing the interior chords of a phrase, rather than harmonizing the melody from beginning to end in order."
  type: short-answer
  answer: "The cadence determines the phrase's emotional outcome — whether it closes, pauses, or surprises. Interior chords only make sense as a path leading toward that destination. Deciding the ending first ensures every harmonic choice contributes to a coherent direction; working forward without a target cadence produces progressions that arrive accidentally rather than inevitably."
  explanation: "End-directed thinking is what separates deliberate harmonization from note-by-note chord guessing. The cadence is the phrase's goal; the interior harmony is the argument that builds toward it. Just as effective writing begins with a conclusion, effective harmonization begins with a harmonic destination."
```

## Explainer

You already know from Roman numeral analysis how to identify what chord is sounding and how to label non-chord tones — passing tones, neighbor tones, suspensions. Melodic harmonization reverses that analytical process: instead of being given the chords and asked what they are, you are given the melody and asked to choose the chords. The core insight is that most melody notes are **ambiguous** — the pitch C in C major could belong to I, iii, vi, IV, or even V/IV. The harmonizer's job is to resolve that ambiguity in a way that serves the phrase's direction and emotional character.

Start by identifying the **structural tones** in the melody — the notes that fall on strong beats or are held longest. These are your anchors: strong-beat melody notes most naturally sound as chord tones (root, third, or fifth) of whatever chord you place beneath them. Weaker-beat notes can be non-chord tones — passing tones moving between chord tones, neighbor tones that decorate a chord tone and return to it, or suspensions that delay the resolution of a preceding consonance. The skill of recognizing non-chord tones from your theory studies is now a compositional tool: knowing a weak-beat note can be a passing tone gives you the freedom to hold the underlying chord across it, rather than scrambling to find a chord that contains every note.

**Harmonic rhythm** — the rate at which chords change — is perhaps the most expressive lever in harmonization. A melody harmonized with one chord per beat feels driven and dense; the same melody with one chord per measure feels spacious and inevitable. Typically, phrase beginnings have slower harmonic rhythm (one or two chords establish the key), the middle accelerates (more chord changes create motion toward the cadence), and the cadence itself can slow again as the final chord is approached and confirmed. When you wrote harmonizations in theory class, you may have habitually changed chords on every beat — resist this. Holding a chord across a non-chord tone is nearly always more graceful.

The most important moment in any phrase is the **cadence**, where the harmonic motion arrives at a point of rest or questioning. An **authentic cadence** (V–I) creates closure; a **half cadence** (ending on V) creates an expectant pause; a **deceptive cadence** (V–vi) creates surprise. Build your harmonization backward from the cadence you want: decide whether the phrase will close, pause, or swerve, then work backward to support that ending. A phrase that ends on a half cadence often needs a dominant pedal or a clear approach chord (like ii or IV leading to V) to signal the arrival. The interior choices — which chord serves each structural melody note — then fill in the path between opening and cadence. This end-directed thinking is what separates deliberate harmonization from note-by-note chord guessing.

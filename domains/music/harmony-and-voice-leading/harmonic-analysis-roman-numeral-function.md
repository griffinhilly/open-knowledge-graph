---
id: harmonic-analysis-roman-numeral-function
title: Harmonic Analysis with Roman Numerals and Function
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: roman-numeral-analysis
  type: hard
- id: harmonic-function-basics
  type: hard
- id: chord-inversions
  type: hard
builds-toward:
- voice-leading-reduction-and-schenkerian-analysis
tags:
- analysis
- roman-numeral
- function
- chord-inversion
stage: formal-systems
status: validated
---

# Harmonic Analysis with Roman Numerals and Function

## Core Idea
Roman numeral analysis provides systematic notation for harmonic content (I, ii, iii, IV, V, vi, vii°) with figured bass indicating inversions (root position, first inversion 6, second inversion 6/4). Analysis reveals harmonic structure through functional labels (T = tonic, S = subdominant, D = dominant) and identification of applied chords and modulations. This analytical framework shows how harmony and voice leading work together to create musical form and meaning.

## Questions

```yaml
- question: "A student analyzes a I6/4 chord appearing immediately before a V chord at a cadence and labels it: 'tonic chord in second inversion — stable, home-base feeling.' What is wrong with this analysis?"
  type: multiple-choice
  options:
    - "The inversion notation is incorrect; second inversion should be labeled with '6' not '6/4'"
    - "The I6/4 at a cadential point functions as a dissonance in the dominant area that creates tension resolving into the V, not as a stable tonic"
    - "The cadential 6/4 should be relabeled as IV to reflect its subdominant function"
    - "There is no error; I6/4 always functions as a stable tonic regardless of where it appears"
  answer: 1
  explanation: "The cadential 6/4 (I6/4 at a cadence) is one of the most important functional exceptions in tonal harmony. Despite being built on the tonic pitch class, it functions in the dominant area — the bass note (the fifth of the chord) acts like a dissonance that must resolve down by step into the dominant chord. Labeling it 'stable tonic' misses its actual harmonic role and predicts the wrong outcome: a stable tonic doesn't urgently need to resolve. The notation 'cad. 6/4' or understanding it as a double suspension over the dominant bass clarifies the function."

- question: "A passage in C major arrives on a D major chord. One analyst labels it 'II' (major supertonic); another labels it 'V/V' (secondary dominant). Which label more accurately reveals the harmonic meaning?"
  type: multiple-choice
  options:
    - "'II' — Roman numeral analysis should identify scale degrees, and D is the second scale degree in C major"
    - "'V/V' — it reveals that the chord is functioning as a dominant aimed at V, borrowing the V-I tension and directing it at a temporary target"
    - "'II' — slash notation is only appropriate when the piece actually modulates to a new key"
    - "Both labels are equally informative; the choice is a matter of analytical preference"
  answer: 1
  explanation: "Roman numeral analysis aims to reveal harmonic function, not just identify chords. 'II' correctly identifies the scale degree but tells you nothing about why this chord is here or where it's going. 'V/V' reveals the harmonic logic: this chord is functioning as the dominant of the dominant — it creates dominant-to-tonic momentum aimed temporarily at V rather than I. That functional description predicts what comes next (the G major chord) and explains the heightened tension the D major chord creates. When a chord is borrowed from outside the key to act as a local dominant, slash notation captures that role; a scale-degree label obscures it."

- question: "In Roman numeral analysis, uppercase and lowercase numerals distinguish major from minor chord quality, but this distinction carries no information about harmonic function."
  type: true-false
  answer: false
  explanation: "Case distinction carries both quality and functional information. In a major key, the three major triads (I, IV, V) correspond exactly to the three harmonic functions: tonic, subdominant, and dominant. The three minor triads (ii, iii, vi) fill secondary functional roles — ii is the subdominant substitute, vi is the tonic substitute, iii is ambiguous. The diminished vii° is the dominant substitute. This mapping is not coincidental: it reflects the acoustic and voice-leading properties of each position in the scale. Reading case without thinking about function misses half the information the notation provides."

- question: "The purpose of Roman numeral analysis is to catalog which specific chords appear in a passage — identifying their root, quality, and inversion — rather than to describe what role those chords play in the harmonic narrative."
  type: true-false
  answer: false
  explanation: "If Roman numeral analysis were only about identifying chords, it would be no more useful than a chord chart. Its purpose is to reveal harmonic function and relationship. 'This is V' tells you the chord is the dominant — that it is directional, tense, and wants to resolve to I. 'This is I6/4' at a cadence tells you it's a dissonance in the dominant area despite its tonic spelling. 'This is V/V' tells you a borrowed chord is creating local dominant tension aimed at the real dominant. The notation is a language for describing harmonic meaning, not just harmonic content."

- question: "Why is 'V/V' a more analytically useful label than 'II' for a D major chord in C major, even though 'II' correctly identifies the chord's scale-degree position?"
  type: short-answer
  answer: "Roman numeral analysis exists to reveal harmonic function — what a chord is doing, not just what it is. 'II' correctly names the chord's scale degree but is silent about its function. It doesn't explain why the chord is there, what tension it creates, or what must follow it. 'V/V' reveals the chord's functional role: it is acting as the dominant of the dominant, borrowing the V-I resolution momentum and pointing it temporarily at V rather than I. This predicts both the listener's experience (heightened tension, expectation of V) and the likely continuation (resolution to G major/V). The slash notation makes the borrowed dominant function explicit in a way the scale-degree label cannot."
  explanation: "This is the core purpose of functional harmonic analysis: the same chord can have completely different harmonic meanings in different contexts. D major in C major as 'II' sounds like a surprising major chord on the second scale degree; D major as 'V/V' is a familiar and structurally clear secondary dominant. The notation reflects which reading better describes what the chord is doing in the passage — and 'V/V' almost always wins because it captures the voice-leading motion and the functional tension."
```

## Explainer

Roman numeral analysis is a reading system for tonal harmony — a way of translating the surface of a piece (specific chords, specific keys) into a description of **function and relationship**. You already know how to identify individual chord qualities and inversions from your prerequisites. What Roman numeral analysis adds is the functional layer: instead of noting "there is a G major chord here," you note "this is V in C major," which tells you what role the chord plays in the harmonic narrative.

The **case of the numeral** carries primary information: uppercase means major quality (I, IV, V), lowercase means minor quality (ii, iii, vi), and the diminished symbol ° marks diminished quality (vii°). Case also reflects function: the three major triads in a major key — I, IV, and V — cover the **tonic, subdominant, and dominant** functions respectively. These three functions define the fundamental harmonic logic of tonal music. Tonic chords (I and vi) feel stable; subdominant chords (IV and ii) feel poised for motion; dominant chords (V and vii°) feel tense and directional. Progressions make harmonic sense when they move through these functions in coherent patterns — typically T → S → D → T, which traces the standard harmonic arc of a phrase.

**Figured bass** notation in Roman numeral analysis encodes the bass note relative to the chord root. A plain Roman numeral (no figures) means root position — the root is in the bass. A superscript 6 means first inversion — the third is in the bass (abbreviated from the figured bass interval 6/3). A superscript 6/4 means second inversion — the fifth is in the bass. Inversions are not merely cosmetic variations: they change the sound and function of a chord meaningfully. A I6/4 chord (tonic in second inversion) creates a distinctive suspenseful quality and typically appears as a **cadential 6/4** immediately before a V chord at a cadence, where it functions as a dissonance resolving into the dominant rather than as a stable tonic. Labeling it correctly — cad. 6/4 or I6/4 — signals that understanding.

The full power of Roman numeral analysis emerges when you extend it to **applied chords and modulations**. An applied dominant (e.g., V/V) is a secondary dominant: a chord that functions as V in relation to a non-tonic scale degree. Notating it as V/V rather than II (which would obscure its dominant function toward V) reveals the harmonic logic — it's borrowing the V-I momentum and directing it at a temporary target. When a passage modulates to a new key, you annotate where the old key ends and the new Roman numerals begin. This notation turns a harmonic analysis into a map of the piece's tonal journey, showing not just what chords appear but what story they tell.

---
id: set-class-transformation
title: Set-Class Transformations in Harmonic Analysis
domain: music
course: advanced-music-theory
prerequisites:
- id: set-class-equivalence
  type: hard
- id: transformational-analysis-music
  type: hard
- id: group-definition-and-examples
  type: soft
- id: function-composition-and-inverses
  type: soft
- id: group-actions
  type: soft
- id: binary-operations-and-algebraic-structures
  type: soft
- id: permutation-groups
  type: soft
- id: binary-operations-algebraic-structures
  type: soft
builds-toward:
- post-tonal-harmonic-analysis
tags:
- set-theory
- transformation
- harmony
- analysis
stage: expert
status: validated
---

# Set-Class Transformations in Harmonic Analysis

## Core Idea
Advanced harmonic analysis tracks how set classes transform and relate in a passage. Rather than cataloging chords, this method shows how harmonic material evolves through transposition, inversion, and rotation, revealing underlying unities in works that resist functional harmony analysis.

## Questions

```yaml
- question: "An analyst finds that three successive chords in a passage are {0,1,4}, {2,3,6}, and {4,5,8} — all members of set class [0,1,4]. The analyst labels each chord '[0,1,4]' and concludes the analysis. What does transformation analysis add that this labeling cannot show?"
  type: multiple-choice
  options:
    - "Nothing — identifying that all chords share the same set class is the complete post-tonal analysis"
    - "Transformation analysis assigns Roman numeral equivalents to each chord for comparison with tonal music"
    - "It reveals the specific operations relating successive chords — here T2 each time — showing that the progression is governed by a consistent whole-step transposition, which is the compositional logic driving the harmony"
    - "It determines whether the music is atonal by testing whether the set class appears in tonal music"
  answer: 2
  explanation: "Labeling all three chords [0,1,4] identifies what they have in common but says nothing about how they relate. Transformation analysis reveals that {0,1,4} → {2,3,6} is T2, and {2,3,6} → {4,5,8} is also T2 — the composer is systematically transposing the motive up by a whole step each time. This sequential transposition scheme is the compositional narrative of the passage. Two passages could use the same set class throughout but be organized by completely different transformation logic; only transformation analysis distinguishes them."

- question: "In a Webern passage, a set S is followed by T5I(S). What does the operation T5I do to each pitch class x in S?"
  type: multiple-choice
  options:
    - "Transposes x up 5 semitones, then inverts around C (maps to -x mod 12)"
    - "Maps x to (5 − x) mod 12 — inverts by reflecting around the axis between D# and E, with the specific axis index n=5"
    - "Rotates the pitch classes in S so that the 5th element becomes the first"
    - "Maps x to (x + 5) mod 12, which is pure transposition"
  answer: 1
  explanation: "TnI maps each pitch class x to (n − x) mod 12. So T5I maps x to (5 − x) mod 12: pitch class 0 (C) → 5 (F), pitch class 1 (C#) → 4 (E), pitch class 5 (F) → 0 (C), and so forth. The operation reflects pitch classes around the axis between the pitch classes n/2 and n/2 + 6. Option A is wrong about the order — TnI means 'inversion then transposition by n,' not 'transposition then inversion,' though the formula (n − x) mod 12 captures both."

- question: "Two sets related by TnI (inversion-transposition) belong to different set classes because inversion creates fundamentally different interval content."
  type: true-false
  answer: false
  explanation: "This is a foundational point of set-class theory. A set class is defined as the equivalence class of all sets related by any of the 24 operations — the 12 transpositions T0–T11 and the 12 inversion-transpositions T0I–T11I. Inversion transforms a set by reversing its interval content (intervals become their complements mod 12), but the resulting set belongs to the SAME set class because set-class equivalence explicitly includes inversion. The prime form is chosen to represent all 24 related versions, and TnI-related sets are by definition members of the same class."

- question: "The 24 transposition and inversion-transposition operations on pitch classes form a group under composition, structurally equivalent to the symmetries of a regular 12-gon."
  type: true-false
  answer: true
  explanation: "The 12 transpositions T0–T11 and 12 inversion-transpositions T0I–T11I together form the dihedral group D₁₂ under composition. The group closure, associativity, identity (T0), and inverses all check out: Tn ∘ Tm = T(n+m), TnI ∘ TmI = T(n−m), and Tn ∘ TmI = T(n+m)I. This is exactly the symmetry group of a regular 12-gon — the 12 rotations correspond to transpositions, the 12 reflections to inversion-transpositions. Knowing this algebraic structure lets you compute how chains of operations combine without working out each step from scratch."

- question: "Why does tracking transformations between pitch-class sets reveal something about post-tonal music that simply labeling each harmony by its set class cannot show?"
  type: short-answer
  answer: "Set-class labels identify what each harmony IS in isolation — its interval content, its prime form. Transformation labels identify how harmonies RELATE — the specific operation (Tn or TnI) that maps one to the next. In post-tonal music where functional harmonic progressions are absent, the compositional logic lies in these transformation relationships. A passage might be organized by consistent T6 relationships (tritone transpositions), or alternating Tn and TnI pairs, or a network of T3I operations around a fixed axis. These patterns create structural coherence that is entirely invisible from set-class labels alone. Transformation analysis builds a directed graph — nodes are sets, edges are labeled operations — and when the graph reveals consistent patterns, you have found the organizing principle of the music."
  explanation: "The analogy to tonal music: a Roman numeral analysis doesn't just name chords — it shows how they progress (I→IV→V→I). Transformation analysis serves the same function for post-tonal music: it shows the direction and logic of harmonic motion. Two passages that use the same set class throughout can be organized by completely different transformation schemes and thus have completely different compositional logic."
```

## Explainer

From your study of set-class equivalence, you know that a pitch-class set is characterized by its **prime form** — the most compressed, left-packed ordering of its interval content — and that two sets belong to the same set class if one can be mapped onto the other by transposition (Tn) or inversion followed by transposition (TnI). **Set-class transformation analysis** turns this equivalence relationship into a compositional and analytical tool: rather than simply labeling harmonies by their set class, you trace how harmonic material evolves through these operations across a passage, revealing the underlying logic of the music.

The twelve transpositions T0–T11 and twelve inversion-transpositions T0I–T11I together form a group of 24 operations under composition. If you have studied group theory, you will recognize this as the **dihedral group D₁₂** — the same structure that describes the symmetries of a regular 12-gon. In pitch-class terms: Tn shifts every pitch class up by n semitones (mod 12); T0I maps each pitch class x to (0−x) mod 12 = (12−x) mod 12, reflecting around C; TnI maps x to (n−x) mod 12. Because these are group operations, Tn followed by Tm gives T(n+m), and TnI followed by TmI gives T(n-m). Knowing the algebra lets you predict how transformations chain and verify them efficiently.

In practice, analysis works as follows. Suppose a passage opens with the set {0, 1, 4} (C, C#, E) and is followed by {2, 3, 6} (D, Eb, F#). Compute T2({0,1,4}) = {2,3,6}: confirmed as transposition by a whole step. A third set appears: {8, 9, 0} (Ab, A, C). Check T8({0,1,4}) = {8,9,0}: confirmed. The analysis now reveals T0 → T2 → T8, and you can investigate whether the transposition intervals (2, then 6) themselves form a pattern. Or check whether the third set is an inversion: T8I({0,1,4}) maps to {8, 7, 4} = {4, 7, 8} in normal form, prime form [0,1,4] — the same set class. Whether you find a transposition or an inversion tells you something different about the compositional strategy.

This approach is most powerful in post-tonal music by Schoenberg, Webern, Berg, and later serialist composers, where functional harmonic progressions have been replaced by transformational logic. A motive might appear in its original form (T0), then transposed up a tritone (T6), then inverted around a specific axis (T3I), and these relationships create structural coherence invisible to Roman numeral analysis. Your earlier work on transformational analysis prepared you for individual-chord relationships; here, you build a **transformation network** across an entire passage — a directed graph where nodes are pitch-class sets and edges are labeled by the operation relating them. When the network reveals a consistent pattern (say, all T6 or alternating Tn and TnI operations), you have found the organizing principle of that section. The prime form is the identity that persists; the transformation sequence is the musical narrative.

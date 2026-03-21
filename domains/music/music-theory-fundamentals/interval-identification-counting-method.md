---
id: interval-identification-counting-method
title: Identifying Intervals by Letter Name Counting
domain: music
course: music-theory-fundamentals
prerequisites:
- id: note-names-and-octaves
  type: hard
- id: whole-step-half-step-fundamentals
  type: soft
builds-toward:
- interval-quality-by-semitone-count
- triad-construction-from-scale-degrees
tags:
- intervals
- naming
- counting
- letter-names
stage: formal-systems
status: draft
---

# Identifying Intervals by Letter Name Counting

## Core Idea
Intervals are named by counting the letter names from the lower note to the upper note (inclusive). For example, C to E is a third (C-D-E = three letters), while C to G is a fifth (C-D-E-F-G = five letters). This counting method provides the generic interval name without regard to accidentals, which affect quality but not the basic interval type.

## Questions

```yaml
- question: "What is the generic interval from D up to A?"
  type: multiple-choice
  options:
    - "A fourth"
    - "A fifth"
    - "A sixth"
    - "A seventh"
  answer: 1
  explanation: "Count letter names inclusively: D (1), E (2), F (3), G (4), A (5). Five letter names = a fifth. The inclusive counting rule — including both the starting and ending note — is essential. A student who counts only the steps between notes would get four, arriving at the wrong answer of 'fourth.' Always begin your count at 1 with the lower note, not at 0 or 1 with the first step above it."

- question: "A student counts the interval from C to G and arrives at 'four.' What error did they make?"
  type: multiple-choice
  options:
    - "They used incorrect letter names — C and G are not adjacent in the musical alphabet"
    - "They forgot to count the starting note C, so they counted four steps (C→D→E→F→G) rather than five letter names (C, D, E, F, G)"
    - "They should have counted semitones instead of letter names"
    - "They needed to account for accidentals before counting"
  answer: 1
  explanation: "The error is non-inclusive counting — treating C as 'zero' rather than 'one.' The correct count is: C (1), D (2), E (3), F (4), G (5) = five letter names = a fifth. This is the single most common mistake in interval identification. Think of it like floors in a building: standing on the first floor and going up to the fifth floor means you count 1, 2, 3, 4, 5 — the floor you start on counts. Accidentals (option D) do not affect the generic interval name, only the quality."

- question: "C to E♭ is a second because the flat makes E♭ closer to C than E natural is."
  type: true-false
  answer: false
  explanation: "C to E♭ is a third — the same generic interval as C to E natural. Generic interval names are determined entirely by the number of letter names spanned (C, D, E = three), not by the number of semitones or the distance in pitch. The flat on E changes the interval's quality (from major third to minor third) but does not change its generic name. A flat on E does not turn E into a D; it is still E in the letter-name sequence."

- question: "C♯ to E♯ is a third, just as C to E is a third, because both pairs span the same three letter names."
  type: true-false
  answer: true
  explanation: "Generic intervals depend only on letter names, not accidentals. C♯ (1), D (2), E♯ (3) — three letter names, so a third. C (1), D (2), E (3) — also a third. The accidentals change the quality (C to E is a major third; C♯ to E♯ is also a major third; C to E♭ is a minor third), but the number-name stays the same. This is why the generic interval and the interval quality are learned as two separate but related concepts."

- question: "A student knows that C to E is a major third and immediately concludes that C♯ to E♭ is not a third at all. Are they correct? Explain."
  type: short-answer
  answer: "No. C♯ to E♭ is still a third generically — it spans three letter names (C, D, E). However, it is a diminished third in quality: C♯ to E would be a major third (4 semitones), and lowering the top note by a half step makes it C♯ to E♭ = 3 semitones, which is a diminished third. The generic name (third) stays fixed by the letter-name count; accidentals affect only the quality."
  explanation: "The two-part system of interval naming — generic name from letter-name counting, quality from semitone counting — means that accidentals never change the first part. Any pair of notes whose letter names are C and E form some kind of third: major, minor, augmented, or diminished. The student's error is conflating quality with generic name and thinking that an unusual quality (diminished) means the generic name changes too. It doesn't: the letter names are the ground truth for the number."
```

## Explainer

You know note names and octaves, so you can already identify every letter on the staff — A through G, repeating. Interval naming builds directly on that knowledge: an interval is simply the distance between two notes, and you name that distance by counting letter names. The crucial rule is that you count **inclusively** — you include both the starting note and the ending note in your count. C to E: C (one), D (two), E (three). That is a **third**. C to G: C, D, E, F, G — five letters, so a **fifth**. C back to C (one octave up): C, D, E, F, G, A, B, C — eight letters, so an **octave** (from the Latin for "eight").

The most common mistake is forgetting to count the starting note, which produces an answer that is always one too small — what should be a third gets called a second, what should be a fifth gets called a fourth. Think of it like counting floors in a building: if you start on the first floor and go up to the third floor, you count 1-2-3, not 0-1-2. Both the ground you start from and the destination count.

Notice that accidentals — sharps, flats, naturals — do not change the generic interval name. C to E is a third, and so is C to E♭, and so is C♯ to E♯. All three pairs span the same three letter names. What changes with accidentals is the interval's **quality** — whether it is major, minor, perfect, augmented, or diminished — which you will learn in the next topic. For now, the letter-counting method gives you the **generic interval**: the number-name that tells you how many letter-names the interval spans, independent of the exact number of semitones.

This generic name is surprisingly informative on its own. Thirds are the building blocks of chords. Fifths define the basic shape of a power chord and the framework of Western harmony. Octaves identify notes with the same pitch class. Before you can analyze any of those structures, you need to be able to read off the interval number reliably and instantly. Practice by picking any two notes and counting letter names — always inclusive, always starting from the lower note — until the count becomes automatic.

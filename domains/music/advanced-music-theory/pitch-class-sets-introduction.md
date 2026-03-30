---
id: pitch-class-sets-introduction
title: 'Pitch-Class Sets: Introduction'
domain: music
course: advanced-music-theory
prerequisites:
- id: accidentals-and-enharmonics
  type: hard
- id: roman-numeral-analysis
  type: soft
- id: set-fundamentals
  type: soft
builds-toward:
- pitch-class-set-operations
- set-class-equivalence
tags:
- set-theory
- pitch-class
- post-tonal
- atonality
stage: advanced
status: validated
---

# Pitch-Class Sets: Introduction

## Core Idea
Pitch-class set theory treats musical materials abstracted from rhythm, meter, and register—focusing only on which pitch classes (C, C#, D, etc., ignoring octave) are present and their relationships. This approach is essential for analyzing post-tonal, atonal, and contemporary music where traditional harmonic functions don't apply.

## How It's Best Learned
Start with small 3-4 note sets from familiar atonal works. Write out all transpositions of a single pitch-class set. Use integer notation (0-11) and learn to convert between pitch names and integers fluently.

## Common Misconceptions
- Set theory requires abandoning harmonic hearing. - Set class and pitch-class set are the same thing. - Set theory can explain emotional content or aesthetic quality.

## Questions

```yaml
- question: "An analyst identifies the set {0, 4, 7} at multiple points in an atonal piece, appearing at different transposition levels: {0,4,7}, {2,6,9}, {5,9,0}. What analytical claim does this identification make?"
  type: multiple-choice
  options:
    - "All three passages are in the same key and share the same tonal function"
    - "All three passages contain the same interval structure — they belong to the same set class and share identical interval-class content"
    - "The composer used a 12-tone row and these are consecutive segments of it"
    - "The three passages sound identical to a trained listener because they use the same pitches"
  answer: 1
  explanation: "The analytical claim is structural, not tonal. Identifying the same set class across transpositions reveals that different surface-level passages share the same underlying interval relationships. {0,4,7}, {2,6,9}, and {5,9,0} are all transpositions of the same prime form [0,4,7] — they contain a minor third, a major third, and a perfect fifth (in some arrangement). In atonal music without a tonal center, this shared interval structure is meaningful in the same way that 'same key' is meaningful in tonal music. The passages don't sound identical — they're at different pitch levels — but they share an abstract intervallic identity."

- question: "Two pitch-class sets have the same prime form [0, 1, 4]. What can we conclude about them?"
  type: multiple-choice
  options:
    - "They contain the same pitches, just played in a different order"
    - "They belong to the same set class, have the same interval-class vector, and are equivalent under transposition and/or inversion"
    - "They were composed using the same 12-tone row"
    - "They occur at the same transposition level, starting on the same pitch class"
  answer: 1
  explanation: "Prime form is the canonical representation of a set class — the smallest-span transposition of the normal form, starting on 0. Two sets with the same prime form belong to the same set class, meaning they are equivalent under transposition (same interval structure at a different pitch level) or inversion (interval pattern flipped). They share the same interval-class vector (same count of each interval class 1–6). They do NOT necessarily contain the same pitches, and they could appear at any transposition level. The prime form abstracts away from specific pitch content to reveal structural equivalence."

- question: "A pitch class and a pitch are the same thing: C4 (middle C) and C5 are different pitch classes because they are in different octaves."
  type: true-false
  answer: false
  explanation: "This is the foundational definition of pitch class: a pitch class is an equivalence class of all pitches that differ only by octave. C4, C5, C2, and C7 are all the same pitch class — PC 0 in integer notation. This octave equivalence is why there are only 12 pitch classes (corresponding to the 12 chromatic notes) regardless of register. The abstraction from specific octave placement is what allows set theory to analyze interval content independently of register — a chord can be spread across multiple octaves and still constitute the same pitch-class set."

- question: "Set class equivalence allows an analyst to recognize that two musical passages share the same underlying interval structure even when they appear at different transpositions or inversions — the post-tonal analog of recognizing that two passages are in the same key."
  type: true-false
  answer: true
  explanation: "This comparison captures the core analytical move in pitch-class set theory. In tonal analysis, recognizing that two passages are both in G major reveals a structural relationship regardless of their different harmonic contexts. In set theory, recognizing that two passages share the same set class (same prime form) reveals a structural relationship — shared interval content — regardless of transposition level or whether the interval pattern is inverted. This is why set theory is powerful for atonal music: it provides a vocabulary for structural similarity when tonal function is absent."

- question: "Why does pitch-class set theory use integer notation (0–11) and modulo-12 arithmetic rather than traditional note names, and what does this allow analysts to do that Roman numeral analysis cannot?"
  type: short-answer
  answer: "Integer notation maps the 12 chromatic pitch classes to the integers 0–11 (C=0, C#=1, …, B=11) and uses modulo-12 arithmetic so that interval calculations 'wrap around' like a clock. This allows analysts to compute intervals precisely (the interval from pitch class 4 to pitch class 9 is 9-4=5, a perfect fourth), identify enharmonic equivalences automatically (C# and D♭ are both 1), and compare sets abstractly by their interval content rather than their note names. Roman numeral analysis can only describe relationships within a tonal key — it requires a tonal center to give chords their function. Set theory describes interval relationships that hold regardless of whether a tonal center exists, making it the primary tool for post-tonal and atonal music where Roman numerals are inapplicable."
  explanation: "The shift to integers is not arbitrary — it enables the mathematical operations that define set theory: transposition (adding a constant mod 12), inversion (subtracting from 12 mod 12), normal form computation, and interval-class vector calculation. These operations would be cumbersome with letter names and impossible to generalize. The result is an analytical system that works on the interval structure of any collection of pitch classes, independent of tonal context — which is precisely what atonal music requires."
```

## Explainer

In tonal music — the harmonic language you've analyzed with **Roman numerals** — the system works because pitches function relative to a key. A G in C major is the dominant; in G major it's the tonic. The same pitch has different functional meanings depending on context, and the system of chords, voice leading, and resolution is the grammar. Post-tonal music, beginning roughly with late Liszt, Scriabin, and the Second Viennese School (Schoenberg, Berg, Webern), deliberately dismantled these functional relationships. Without a tonal center to provide hierarchy, new analytical tools are needed. **Pitch-class set theory** is the primary one.

A **pitch class** (PC) is an equivalence class of pitches that differ only by octave. Middle C and the C four octaves above are the same pitch class. Because there are twelve distinct pitch classes in equal temperament (corresponding to the twelve notes of the chromatic scale), pitch classes are conveniently labeled with integers 0–11: C=0, C#/D♭=1, D=2, …, B=11. This is **integer notation**, and arithmetic on pitch classes is done modulo 12 — like clock arithmetic. From your prerequisite with accidentals and enharmonics, you know that C# and D♭ name the same pitch in equal temperament; in PC notation, they both map to 1.

A **pitch-class set** is any unordered collection of pitch classes. The chord {C, E, G} becomes the set {0, 4, 7}. The opening three notes of Schoenberg's Op. 11 No. 1 — say {B, G#, G} — become {11, 8, 7}, or after reordering {7, 8, 11}. The analyst can then ask questions about the *structure* of this collection: how many semitones separate its members? What intervals does it contain? Does it appear elsewhere in the piece at a different transposition? These structural questions are answerable without any reference to tonal function — and they reveal patterns in atonal music that ordinary chord-name analysis misses entirely.

The most important concept for comparing sets is **normal form** and **prime form**. To find the prime form, you arrange the PCs in ascending order (modulo 12) across the smallest possible span, then transpose so the first PC is 0. This canonical representation lets you recognize when two sets are "the same" up to transposition. But two sets can also be equivalent under **inversion** (flipping the interval pattern), and the **set class** groups together all transpositions and inversions of a set. A set class is named by its prime form (e.g., [0,1,4]) and catalogued in reference works like Allen Forte's tables. Recognizing that different-sounding musical surfaces share the same underlying set class is the key analytical move — the post-tonal equivalent of recognizing that two passages are in the same key.

The shift from tonal to pitch-class set analysis is a shift in *what counts as a relationship*. In tonal analysis, two chords are related by function (V going to I). In set theory, two collections are related by *interval content*. The **interval-class vector** is a six-entry list counting how many of each interval class (1 through 6) the set contains. Two sets with identical interval vectors may "sound similar" in a abstract spectral sense, even if they appear at different transpositions or inversions. This is why set theory is powerful for music where the ear can't rely on harmonic function: it provides an objective vocabulary for describing what notes are present and how they relate by interval — the remaining structure when tonal hierarchy is absent.

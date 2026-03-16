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
status: draft
---

# Pitch-Class Sets: Introduction

## Core Idea
Pitch-class set theory treats musical materials abstracted from rhythm, meter, and register—focusing only on which pitch classes (C, C#, D, etc., ignoring octave) are present and their relationships. This approach is essential for analyzing post-tonal, atonal, and contemporary music where traditional harmonic functions don't apply.

## How It's Best Learned
Start with small 3-4 note sets from familiar atonal works. Write out all transpositions of a single pitch-class set. Use integer notation (0-11) and learn to convert between pitch names and integers fluently.

## Common Misconceptions
- Set theory requires abandoning harmonic hearing. - Set class and pitch-class set are the same thing. - Set theory can explain emotional content or aesthetic quality.

## Explainer

In tonal music — the harmonic language you've analyzed with **Roman numerals** — the system works because pitches function relative to a key. A G in C major is the dominant; in G major it's the tonic. The same pitch has different functional meanings depending on context, and the system of chords, voice leading, and resolution is the grammar. Post-tonal music, beginning roughly with late Liszt, Scriabin, and the Second Viennese School (Schoenberg, Berg, Webern), deliberately dismantled these functional relationships. Without a tonal center to provide hierarchy, new analytical tools are needed. **Pitch-class set theory** is the primary one.

A **pitch class** (PC) is an equivalence class of pitches that differ only by octave. Middle C and the C four octaves above are the same pitch class. Because there are twelve distinct pitch classes in equal temperament (corresponding to the twelve notes of the chromatic scale), pitch classes are conveniently labeled with integers 0–11: C=0, C#/D♭=1, D=2, …, B=11. This is **integer notation**, and arithmetic on pitch classes is done modulo 12 — like clock arithmetic. From your prerequisite with accidentals and enharmonics, you know that C# and D♭ name the same pitch in equal temperament; in PC notation, they both map to 1.

A **pitch-class set** is any unordered collection of pitch classes. The chord {C, E, G} becomes the set {0, 4, 7}. The opening three notes of Schoenberg's Op. 11 No. 1 — say {B, G#, G} — become {11, 8, 7}, or after reordering {7, 8, 11}. The analyst can then ask questions about the *structure* of this collection: how many semitones separate its members? What intervals does it contain? Does it appear elsewhere in the piece at a different transposition? These structural questions are answerable without any reference to tonal function — and they reveal patterns in atonal music that ordinary chord-name analysis misses entirely.

The most important concept for comparing sets is **normal form** and **prime form**. To find the prime form, you arrange the PCs in ascending order (modulo 12) across the smallest possible span, then transpose so the first PC is 0. This canonical representation lets you recognize when two sets are "the same" up to transposition. But two sets can also be equivalent under **inversion** (flipping the interval pattern), and the **set class** groups together all transpositions and inversions of a set. A set class is named by its prime form (e.g., [0,1,4]) and catalogued in reference works like Allen Forte's tables. Recognizing that different-sounding musical surfaces share the same underlying set class is the key analytical move — the post-tonal equivalent of recognizing that two passages are in the same key.

The shift from tonal to pitch-class set analysis is a shift in *what counts as a relationship*. In tonal analysis, two chords are related by function (V going to I). In set theory, two collections are related by *interval content*. The **interval-class vector** is a six-entry list counting how many of each interval class (1 through 6) the set contains. Two sets with identical interval vectors may "sound similar" in a abstract spectral sense, even if they appear at different transpositions or inversions. This is why set theory is powerful for music where the ear can't rely on harmonic function: it provides an objective vocabulary for describing what notes are present and how they relate by interval — the remaining structure when tonal hierarchy is absent.

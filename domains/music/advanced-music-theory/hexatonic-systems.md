---
id: hexatonic-systems
title: Hexatonic Systems and Harmonic Regions
domain: music
course: advanced-music-theory
prerequisites:
- id: tonnetz-pitch-space
  type: hard
- id: pitch-class-sets-introduction
  type: soft
- id: modular-arithmetic
  type: soft
tags:
- hexatonic
- pitch-class
- neo-riemannian
- tonal-ambiguity
stage: advanced
status: draft
---

# Hexatonic Systems and Harmonic Regions

## Core Idea
Hexatonic systems are six-note subsets of the twelve pitch classes organized under neo-Riemannian operations such that certain PLR operations keep the music within the same hexatonic system. Analyzing hexatonic systems illuminates tonal ambiguity and the harmonic language of late 19th-century music where multiple pitch centers coexist.

## Explainer

From your study of the Tonnetz, you know that major and minor triads can be related by three transformations: **P** (parallel — same root, mode flips), **L** (leading-tone exchange — one voice moves by semitone to flip mode), and **R** (relative — shared fifth flips mode). On the Tonnetz, these operations correspond to flipping a triangle across one of its edges. Now consider what happens when you chain these operations: starting from a C major triad, applying P → L → P → L repeatedly. You cycle through six triads and return to the start. The six pitch classes those triads collectively use form a **hexatonic system**.

Richard Cohn identified four such hexatonic systems, sometimes called the **Northern, Western, Southern, and Eastern** hexatonic poles (after their positions on the Tonnetz). Each system contains exactly six pitch classes and six triads — three major and three minor — and is closed under the **PL** and **LP** cycle. For example, the Northern hexatonic system contains the pitch classes {E, G#/Ab, B, C, Eb, G} and the triads C major, E major, Ab major, C minor, E minor, and Ab minor. The magic is that while each individual triad sounds like it implies a key, no single tonal center governs all six: the three major triads are spaced four semitones apart (a **augmented triad** spacing), making tonic ambiguous.

The analytical payoff comes in late Romantic music — Schubert, Brahms, Wagner, Liszt — where progressions move smoothly between triads with no diatonic logic. A C major triad moving to E major (a mediant relation involving no common tones in traditional voice-leading) makes sense as a single L or PL operation on the Tonnetz and as a move within the Northern hexatonic system. The **hexatonic pole** progression — C major to Ab minor — is the most distant pair within a system: no pitch classes in common, yet connected by a single P move within the system. These progressions are jarring tonally but fluid from a neo-Riemannian perspective. Your pitch-class set background helps here too: each hexatonic system is a set-class with a distinctive **interval vector**, which explains why these six pitch classes consistently support the smooth voice-leading that neo-Riemannian operations produce.

The four hexatonic systems partition all twelve pitch classes into four disjoint groups of six, covering the entire chromatic space without overlap. This exhaustive partition is structurally similar to how the twelve pitch classes are partitioned by whole-tone scales or diminished seventh chords — symmetrical divisions that produce equal-interval spacing and harmonic ambiguity. Understanding hexatonic systems gives you a map of the harmonic space that Wagner and late Liszt navigate: progressions that cross hexatonic system boundaries mark genuine harmonic ruptures, while motion within a system is fluid and tonally suspended.

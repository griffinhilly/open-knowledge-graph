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
stage: expert
status: validated
---

# Hexatonic Systems and Harmonic Regions

## Core Idea
Hexatonic systems are six-note subsets of the twelve pitch classes organized under neo-Riemannian operations such that certain PLR operations keep the music within the same hexatonic system. Analyzing hexatonic systems illuminates tonal ambiguity and the harmonic language of late 19th-century music where multiple pitch centers coexist.

## Questions

```yaml
- question: "A late Romantic passage cycles through C major → E major → Ab major → C minor → E minor → Ab minor → C major via PL operations. How should this be analyzed?"
  type: multiple-choice
  options:
    - "As a diatonic progression that returns to C major as tonic"
    - "As a modulation through three keys (C, E, Ab) and back"
    - "As a cycle through a single hexatonic system, producing tonal ambiguity because no single pitch center governs all six triads"
    - "As a sequence of secondary dominants since each chord is a major third from the previous"
  answer: 2
  explanation: "The PL cycle is closed within one hexatonic system — it never leaves that system. The three major triads are spaced four semitones apart (augmented triad spacing), so no single pitch class asserts itself as tonic. This is precisely the tonal ambiguity hexatonic systems create. Option B (modulation) implies arrival at new tonal centers, but the smooth neo-Riemannian motion within the system never establishes a new key — it suspends tonal gravity entirely."

- question: "Why does a hexatonic system produce tonal ambiguity rather than implying a single tonal center?"
  type: multiple-choice
  options:
    - "Because it uses all twelve pitch classes, preventing any single pitch from dominating"
    - "Because the three major triads within the system are spaced four semitones apart — augmented triad spacing — so no single root stands out as the tonic"
    - "Because hexatonic systems are atonal by definition and have no key signatures"
    - "Because PLR operations are undefined in tonal music"
  answer: 1
  explanation: "The three major triads in any hexatonic system (e.g., C, E, Ab in the Northern system) each sound like they could be a local tonic, but they are spaced symmetrically a major third apart — the same spacing as an augmented triad. Symmetric divisions of the octave like this have no natural resting point; every root is equally privileged (or equally deprivileged). Option A is wrong: hexatonic systems use only six of the twelve pitch classes, not all twelve."

- question: "The four hexatonic systems partition all twelve pitch classes into four disjoint groups of six, with no pitch class appearing in more than one system."
  type: true-false
  answer: true
  explanation: "Cohn showed that the four hexatonic systems (Northern, Western, Southern, Eastern) are disjoint and together cover all twelve pitch classes exactly once. This is structurally analogous to how the twelve pitch classes are partitioned by whole-tone scales or diminished seventh chords — symmetric divisions that create equal-interval spacing and harmonic ambiguity. Each system is a closed, self-contained harmonic region."

- question: "The hexatonic pole progression (e.g., C major to Ab minor) sounds smooth because the two chords share several pitch classes in common."
  type: true-false
  answer: false
  explanation: "C major {C, E, G} and Ab minor {Ab, Cb, Eb} share no pitch classes whatsoever. The hexatonic pole pair is the most distant pair within a system precisely because of this zero-common-tone relationship. The smoothness comes from the near-semitonal voice leading enabled by the P transformation within the system — each voice moves by a small interval — not from common tones. This is what makes the hexatonic pole progression so striking: it is harmonically jarring (no shared notes) yet tonally fluid (smooth voice leading)."

- question: "What makes hexatonic systems analytically useful for late 19th-century music, and what does a passage staying within one hexatonic system tell us about that music?"
  type: short-answer
  answer: "Hexatonic systems explain smooth harmonic progressions with no diatonic logic — triads with no common tones or diatonic relationship can be adjacent steps in a PL cycle within one system. A passage staying within a single system is harmonically suspended: it moves through a tonally ambiguous region where no pitch center is established, yet the voice leading is smooth and the motion is internally coherent. This helps explain why late Liszt and Wagner can feel simultaneously fluid and destabilizing — the logic operates in neo-Riemannian space, not in tonal key relationships."
  explanation: "Traditional tonal analysis requires identifying keys, modulations, and dominant-tonic motion. But many late Romantic passages resist this — they move between triads with no common-tone or diatonic basis. Hexatonic analysis provides an alternative framework: these passages are navigating a single harmonic region defined by neo-Riemannian closure, not by key. Progressions that cross hexatonic system boundaries mark genuine harmonic ruptures; motion within a system is fluid but tonally weightless."
```

## Explainer

From your study of the Tonnetz, you know that major and minor triads can be related by three transformations: **P** (parallel — same root, mode flips), **L** (leading-tone exchange — one voice moves by semitone to flip mode), and **R** (relative — shared fifth flips mode). On the Tonnetz, these operations correspond to flipping a triangle across one of its edges. Now consider what happens when you chain these operations: starting from a C major triad, applying P → L → P → L repeatedly. You cycle through six triads and return to the start. The six pitch classes those triads collectively use form a **hexatonic system**.

Richard Cohn identified four such hexatonic systems, sometimes called the **Northern, Western, Southern, and Eastern** hexatonic poles (after their positions on the Tonnetz). Each system contains exactly six pitch classes and six triads — three major and three minor — and is closed under the **PL** and **LP** cycle. For example, the Northern hexatonic system contains the pitch classes {E, G#/Ab, B, C, Eb, G} and the triads C major, E major, Ab major, C minor, E minor, and Ab minor. The magic is that while each individual triad sounds like it implies a key, no single tonal center governs all six: the three major triads are spaced four semitones apart (a **augmented triad** spacing), making tonic ambiguous.

The analytical payoff comes in late Romantic music — Schubert, Brahms, Wagner, Liszt — where progressions move smoothly between triads with no diatonic logic. A C major triad moving to E major (a mediant relation involving no common tones in traditional voice-leading) makes sense as a single L or PL operation on the Tonnetz and as a move within the Northern hexatonic system. The **hexatonic pole** progression — C major to Ab minor — is the most distant pair within a system: no pitch classes in common, yet connected by a single P move within the system. These progressions are jarring tonally but fluid from a neo-Riemannian perspective. Your pitch-class set background helps here too: each hexatonic system is a set-class with a distinctive **interval vector**, which explains why these six pitch classes consistently support the smooth voice-leading that neo-Riemannian operations produce.

The four hexatonic systems partition all twelve pitch classes into four disjoint groups of six, covering the entire chromatic space without overlap. This exhaustive partition is structurally similar to how the twelve pitch classes are partitioned by whole-tone scales or diminished seventh chords — symmetrical divisions that produce equal-interval spacing and harmonic ambiguity. Understanding hexatonic systems gives you a map of the harmonic space that Wagner and late Liszt navigate: progressions that cross hexatonic system boundaries mark genuine harmonic ruptures, while motion within a system is fluid and tonally suspended.

---
id: parallel-major-minor-comparison
title: Parallel Major and Minor Scales
domain: music
course: music-theory-fundamentals
prerequisites:
- id: major-scale-construction-fundamentals
  type: hard
- id: natural-minor-scale-construction-fundamentals
  type: hard
builds-toward:
- chromatic-borrowed-chords-basics
- minor-key-harmony
tags:
- scales
- tonality
- major-minor-relationship
- parallel
stage: formal-systems
status: validated
---

# Parallel Major and Minor Scales

## Core Idea
Parallel major and minor scales start on the same pitch but have different notes. C major and C minor are parallel—they begin on C but C minor has three flats (Eb, Ab, Bb) while C major has no accidentals. This relationship is useful for understanding harmonic color and chromaticism, where composers borrow chords from the parallel minor.

## Questions

```yaml
- question: "C major and C natural minor are parallel keys. Which scale degrees differ between them?"
  type: multiple-choice
  options:
    - "Scale degrees 2, 4, and 5 — these are raised in major and appear lowered in natural minor"
    - "Scale degrees 3, 6, and 7 — each is lowered by a half step in natural minor (written ♭3, ♭6, ♭7)"
    - "Scale degrees 1, 3, and 5 — the tonic triad pitches change between parallel major and minor"
    - "Scale degrees 4, 6, and 7 — the subdominant and subtonic distinguish major from natural minor"
  answer: 1
  explanation: "Comparing C major (C–D–E–F–G–A–B) with C natural minor (C–D–E♭–F–G–A♭–B♭) degree by degree: scale degrees 1 (C), 2 (D), 4 (F), and 5 (G) are identical. Only degrees 3, 6, and 7 differ — each lowered by a half step in natural minor. These three altered degrees, written ♭3, ♭6, and ♭7, account for the entire structural difference between parallel major and minor. Knowing exactly which degrees change — and which stay the same — is what enables borrowed chord analysis."

- question: "A composer is writing in C major and uses an A♭ major chord — a chord that doesn't belong to the C major scale. A student says 'this must mean the piece has modulated to a new key.' What is a more accurate description of what's likely happening?"
  type: multiple-choice
  options:
    - "The student is correct — any chord containing a pitch outside the home key signature indicates a modulation to a new tonal center"
    - "The A♭ major chord borrows the ♭6 scale degree from C minor (the parallel minor) — this is modal mixture, not modulation, because C remains the tonal center throughout"
    - "A♭ major is enharmonically G# major, which is the mediant of E major, so the passage has briefly tonicized E"
    - "The A♭ is a chromatic passing chord with purely voice-leading function and no structural harmonic role"
  answer: 1
  explanation: "Modal mixture (borrowed chords) allows a composer to import chords from the parallel minor while keeping the same tonic. A♭ in C major contains ♭6 — a degree found in C minor but not C major. Using this chord darkens the harmonic color without leaving the C tonal center; it is not a modulation. Modulation involves establishing a new tonic; mixture borrows from the parallel mode while staying home. This distinction is only visible once you can map the precise degree-by-degree difference between parallel keys."

- question: "C major and A minor are parallel keys because they share the same starting pitch."
  type: true-false
  answer: false
  explanation: "C major and A minor are *relative* keys — they share the same key signature (no sharps or flats) but start on different pitches (C and A respectively). Parallel keys share the same starting pitch (tonic) but have different key signatures. C major and C minor are parallel: both start on C, but C minor has three flats (E♭, A♭, B♭). Confusing relative and parallel is one of the most common errors in early music theory — and it matters because the two relationships have completely different analytical applications."

- question: "Scale degrees 1, 2, 4, and 5 are identical in parallel major and natural minor scales built on the same tonic."
  type: true-false
  answer: true
  explanation: "In C major: C–D–E–F–G–A–B. In C natural minor: C–D–E♭–F–G–A♭–B♭. Scale degrees 1 (C), 2 (D), 4 (F), and 5 (G) are the same in both. Only degrees 3, 6, and 7 differ. This precise shared-versus-altered mapping is what makes borrowed chords conceptually coherent: you know exactly which pitches stay the same when you move between parallel modes and which ones change."

- question: "Why is understanding the parallel relationship (rather than only the relative relationship) essential for analyzing chromatic chords in tonal music?"
  type: short-answer
  answer: "The parallel relationship reveals which specific scale degrees differ between major and minor on the same tonic — ♭3, ♭6, and ♭7. This is the structural basis for modal mixture: a composer can import chords containing these altered degrees from the parallel minor while keeping the same tonal center. The relative relationship (same key signature, different tonic) doesn't explain this — borrowed chords come from the parallel mode, not from the relative key."
  explanation: "Modal mixture is one of the most expressive harmonic resources in tonal music, from Beethoven's 'Ode to Joy' to contemporary film scores. A composer writing in C major who darkens the harmony with a ♭VI chord (A♭ major) or a iv chord (F minor) is drawing on C minor — the parallel minor, not any other key. You can only see this mechanism clearly once you've mapped exactly where C major and C minor diverge and where they coincide."
```

## Explainer

You know how to build both major and minor scales from scratch: major follows W-W-H-W-W-W-H, natural minor follows W-H-W-W-H-W-W. You've learned these as two separate scale shapes. **Parallel comparison** means placing them side by side on the same starting pitch and observing exactly where they diverge — not just noting that they're different, but mapping the precise structural relationship between them.

Take C as the starting pitch. C major is C–D–E–F–G–A–B–C. C natural minor is C–D–E♭–F–G–A♭–B♭–C. Compare them degree by degree: scale degrees 1, 2, 4, and 5 are identical. Degrees 3, 6, and 7 are each lowered by a half step in minor. In scale-degree notation these are written **♭3, ♭6, ♭7** — and these three lowered scale degrees account for the entire structural difference between parallel major and minor. The half-step shift on scale degree 3 (from E to E♭ in C) determines whether the tonic triad is major or minor, which is the primary signal listeners use to perceive mode. The ♭6 and ♭7 modify the color and function of chords built on those degrees.

This structural mapping is the key to understanding **modal mixture** (also called **borrowed chords**), which you'll encounter soon. Once you can see that C major and C minor share a tonic but differ in three specific scale degrees, you can understand what it means to "borrow" a chord from the parallel minor into a major-key context. A composer working in C major who uses an A♭ major chord is importing the ♭6 degree from C minor — a move that creates an immediate darkening of color without leaving the C tonic. This practice is ubiquitous from Beethoven through contemporary pop and film music.

It's worth distinguishing the parallel relationship clearly from the **relative** relationship you already know. C major and A minor are *relative* — they share the same key signature (no sharps or flats) but begin on different pitches. C major and C minor are *parallel* — they share the same starting pitch but have different key signatures (C minor has three flats). Both relationships matter for different purposes: relative keys help you understand key signatures, modulation to closely related keys, and scale degree equivalences across modes. Parallel keys help you understand harmonic color, chromaticism, and the emotional palette composers draw from when they want to darken or brighten a passage without fully changing tonal center. Keeping them distinct — same signature vs. same root — prevents one of the most common confusions in music theory study.

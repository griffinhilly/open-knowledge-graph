---
id: chromatically-altered-harmony-mixture
title: Chromatic Alterations and Mixture Harmony
domain: music
course: harmony-and-voice-leading
prerequisites:
- id: borrowed-chords
  type: hard
- id: harmonic-function-voice-leading-tension-resolution
  type: hard
- id: chromatic-scale-construction
  type: soft
builds-toward:
- borrowed-chords-parallel-modes-voice-leading
tags:
- borrowed-chord
- mixture
- chromatic
- parallel-mode
stage: formal-systems
status: draft
---

# Chromatic Alterations and Mixture Harmony

## Core Idea
Mixture (borrowed harmony) brings chords from the parallel minor or major key, darkening or brightening harmonic color through chromatic alteration. Voice-leading considerations are critical: chromatic alterations require careful resolution following stepwise motion principles. Common borrowed chords include iv (from minor in major keys) and VI (from minor), each serving specific harmonic functions while introducing unexpected chromatic pitches.

## Questions

```yaml
- question: "In a piece in C major, a composer uses the chord F–Ab–C (F minor, iv). A student says, 'The piece has temporarily modulated to C minor.' What is wrong with this analysis?"
  type: multiple-choice
  options:
    - "The chord F–Ab–C does not exist in C minor"
    - "A single borrowed chord creates a momentary color change without establishing a new tonal center — this is mixture, not modulation"
    - "Modulation requires the borrowed chord to be tonicized with its own dominant"
    - "The student is correct; using any chord from the parallel minor counts as modulating to that key"
  answer: 1
  explanation: "Mixture (modal borrowing) and modulation are fundamentally different: mixture brings a chord from the parallel key for coloristic effect while the tonal center remains in the original key; modulation actually shifts the tonal center to a new key. A single borrowed iv chord in C major creates a darkening effect without leaving C as the home key — we're still hearing C major with a borrowed color, not C minor as a new tonal center. Modulation typically requires establishing the new key with a cadence or prolonged presence."

- question: "In C major, a voice has the note Ab drawn from a borrowed iv chord. According to mixture voice-leading principles, where should this Ab resolve?"
  type: multiple-choice
  options:
    - "Up to A-natural, restoring the diatonic scale degree"
    - "Down to G, resolving stepwise in the direction of the lowering"
    - "It can move freely in any direction since it is a borrowed tone"
    - "Down to F, because Ab is the third of the iv chord and thirds typically fall"
  answer: 1
  explanation: "The voice-leading rule for chromatic mixture is that altered tones resolve in the direction of their alteration: lowered tones resolve downward, raised tones resolve upward. Ab is a half-step lowering of A-natural, so it resolves down to G — its nearest diatonic neighbor in the downward direction, typically as part of a V or I chord. Resolving Ab upward to A-natural creates a cross-relation (Ab and A-natural in close proximity across voices), which clashes with the intended darkening effect."

- question: "The iv chord in a C major passage is a borrowed chord because it contains Ab, the lowered sixth scale degree drawn from the C natural minor scale."
  type: true-false
  answer: true
  explanation: "In C major, the diatonic sixth scale degree is A-natural, producing a IV chord of F–A–C (F major). C natural minor has Ab as its sixth scale degree. Borrowing iv from C minor introduces Ab into the C major context. This single chromatic alteration — one half step — produces the characteristic darkening effect of mixture. The chord is 'borrowed' because it belongs natively to the parallel minor key, not to the major key where it appears."

- question: "Chromatic mixture and modulation are essentially the same technique — both involve using pitches from outside the home key to create variety."
  type: true-false
  answer: false
  explanation: "Mixture and modulation differ fundamentally in their effect on tonal center. Mixture temporarily borrows chords from the parallel key for coloristic effect while remaining anchored in the original key — the tonic does not change. Modulation actually shifts the tonal center: the music establishes a new key, often confirmed by a cadence. Mixture is a momentary visit; modulation is a move. A borrowed iv chord in C major is mixture; establishing F minor as a new home key with its own authentic cadence would be modulation."

- question: "A composer borrows the bVI chord (Ab major) into a passage in C major. What chromatic pitches does this introduce, where do they come from, and how should they resolve?"
  type: short-answer
  answer: "In C major, bVI is Ab–C–Eb. The chromatic pitches are Ab (lowered 6th) and Eb (lowered 3rd); C is already diatonic. Both Ab and Eb come from the C natural minor (Aeolian) scale. According to mixture voice-leading principles, lowered tones resolve downward: Ab resolves down to G (the 5th scale degree), and Eb resolves down to D (the 2nd) or to C. This typically means bVI moves to a V chord (where G is present) or to I. The result is a smooth, darkening harmonic color followed by a return to diatonic territory."
  explanation: "Understanding where the altered tones go is the practical skill of mixture harmony. Without careful resolution, borrowed pitches create cross-relations and awkward leaps. The rule 'lowered tones resolve down, raised tones resolve up' keeps the borrowed harmony expressive and the voice leading smooth."
```

## Explainer

You already know that **borrowed chords** come from the parallel key — using chords from C minor inside a piece in C major, or vice versa. Chromatic mixture is the systematic application of this borrowing, and the key to understanding it is hearing what the borrowed pitch *does* to the harmonic color. When you take a chord from the parallel minor into a major-key passage, you lower one or more scale degrees by a half step. That single half-step alteration doesn't just change the chord — it shifts the entire emotional register of the moment, introducing a shadow or darkening that the diatonic harmony can't achieve on its own.

The most common example in major keys is the **iv chord** — the subdominant minor. In C major, the diatonic IV chord is F–A–C (F major). Borrowing from C minor gives you iv: F–Ab–C (F minor). The only difference is Ab instead of A-natural, but the effect is dramatic. That lowered sixth scale degree (Ab in C major) has a characteristic plaintive, darkening quality — it's the sound of unexpected minor coloring in a major-key passage. You hear it in countless popular songs ("Oh! Darling" by the Beatles, or the chorus of "Hotel California") where it provides emotional intensity that pure major harmony can't deliver. The voice-leading rule is straightforward: Ab wants to resolve by step, typically down to G (as part of a V or I chord). Avoid the half-step clash of having Ab and A-natural occur in close proximity in different voices.

The **bVI chord** (flat-six major) is another essential mixture chord. In C major, bVI is Ab–C–Eb — the major triad built on the lowered sixth. It doesn't function as a dominant-preparation chord the way IV does; instead, it creates a shift in tonal gravity, often pulling toward a plagal resolution or a deceptive cadence effect. The bVI can also function as a pre-dominant chord moving to V or directly to I in what some theorists call a "backdoor" progression (bVII–I or bVI–bVII–I). The chromatic pitches (Ab and Eb in C major) are from the natural minor scale, so the borrowed chord feels like a brief visit to the parallel minor world.

**Voice leading** is the critical craft issue with mixture harmony. Chromatic alterations introduce pitches that have strong directional pull — they are leading tones or tendency tones in a new temporary context. The lowered pitch (the borrowed chord's characteristic tone) typically wants to resolve stepwise **downward** to reinforce its "darkening" effect, while a raised pitch (in the opposite direction of borrowing) wants to resolve **upward**. Allowing a chromatic pitch to move by augmented intervals or to resolve in the wrong direction creates awkward, ungainly lines that undercut the expressive effect. The rule of thumb: any pitch altered by chromatic mixture should resolve in the direction of its alteration — lowered tones resolve down, raised tones resolve up.

Practiced together, mixture chords form a **chromatic vocabulary** that expands the emotional palette of tonal harmony without leaving the home key. Unlike modulation, which shifts tonal center, mixture stays anchored to the original tonic while reaching into the parallel key for coloristic resources. The skill you are developing is not just identifying which chords are borrowed, but hearing the specific darkening or brightening effect they produce and understanding how the altered tones must be handled to maintain smooth, purposeful voice leading.

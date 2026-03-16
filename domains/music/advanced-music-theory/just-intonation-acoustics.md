---
id: just-intonation-acoustics
title: Just Intonation and Harmonic-Series-Based Composition
domain: music
course: advanced-music-theory
prerequisites:
- id: pitch-and-frequency
  type: hard
- id: tuning-systems-temperament
  type: hard
- id: rational-numbers-operations
  type: soft
- id: ratios
  type: soft
- id: proportions
  type: soft
- id: logarithm-properties
  type: soft
- id: fractions
  type: soft
- id: divisibility-and-primes-discrete
  type: soft
builds-toward:
- microtonal-systems-analysis
- spectral-composition-acoustics
tags:
- just-intonation
- harmonic-series
- tuning
- acoustics
stage: abstract-reasoning
status: draft
---

# Just Intonation and Harmonic-Series-Based Composition

## Core Idea
Just intonation uses frequency ratios based on the harmonic series (3:2, 5:4, etc.) rather than equal temperament. Chords in just intonation create distinct colors; complex ratios sound increasingly dissonant. Composers using just intonation (La Monte Young, Ben Johnston) compose harmonies that are impossible in equal temperament.

## Questions

```yaml
- question: "What frequency ratio defines a perfect fifth in just intonation?"
  type: multiple-choice
  options: ["5:4", "3:2", "4:3", "9:8"]
  answer: 1
  explanation: "A just perfect fifth is a 3:2 ratio — the second and third harmonics of the overtone series. 5:4 is the just major third, 4:3 is the just perfect fourth, and 9:8 is the just major second. The 3:2 ratio produces zero beats between the two tones, giving the pure, locked-in sound characteristic of just intonation."

- question: "Just intonation is universally superior to equal temperament because all of its intervals are mathematically pure ratios."
  type: true-false
  answer: false
  explanation: "Just intonation produces acoustically pure intervals within a fixed key but creates the 'comma problem' when modulating: stacking pure fifths or thirds generates small pitch discrepancies (commas) that make distant keys sound out of tune. Equal temperament distributes these discrepancies evenly so every key is equally usable — a genuine trade-off, not a deficiency."

- question: "What is a 'comma' in the context of just intonation, and why does it matter for practical composition?"
  type: short-answer
  answer: "A comma is a small interval (typically 20–25 cents) that arises from the discrepancy between different just-intonation paths to the same pitch — for example, stacking 12 pure fifths (3:2 each) overshoots 7 octaves by about 23 cents (the Pythagorean comma). This matters because it makes fixed-pitch just-intonation instruments unplayable across multiple keys without retuning."
  explanation: "Commas expose the inherent arithmetic incompatibility of stacking simple ratios. Just intonation composers must either restrict themselves to a limited harmonic region, design instruments with extra pitches per octave, or write for flexible-pitch ensembles (voices, strings) that can adjust on the fly."
```

## Explainer

You already know that pitch is frequency, and that the harmonic series stacks integer multiples above a fundamental: 1f, 2f, 3f, 4f, 5f, and so on. Just intonation is the practice of tuning intervals so their frequency ratios match the simple integer relationships found in that series. A perfect fifth at 3:2 means one note vibrates exactly 1.5 times as fast as the other; a major third at 5:4 means one note vibrates exactly 1.25 times as fast. When frequencies sit in these exact ratios, their overtones align and you hear a pure, beatless sound — the characteristic "locked-in" quality of just intervals.

The contrast with equal temperament is precise and measurable. In 12-tone equal temperament, every semitone is exactly the twelfth root of 2 (≈1.0595), so a perfect fifth is 2^(7/12) ≈ 1.4983 — not quite 3:2 (1.5000). The discrepancy is only about 2 cents (hundredths of a semitone), small enough that most listeners don't notice in fast music. But in sustained, quiet harmony — a chorale, a drone, a slow string passage — the difference is audible as a slow oscillation in volume called beating. Just fifths don't beat; tempered fifths beat about once per second at concert pitch. This is the perceptual core of the just/tempered distinction.

The crisis of just intonation appears when you try to modulate. If you tune C-G-D-A-E-B as a chain of pure 3:2 fifths, you eventually arrive at a B that is about 23 cents sharper than the B you get by tuning up pure major thirds from C. This discrepancy — the Pythagorean comma — means the two routes to the "same" note disagree. Equal temperament exists precisely to dissolve this problem by making every fifth equally slightly impure. Just intonation composers work around it by writing for flexible-pitch ensembles (choirs, string quartets), designing extended instruments with 53 or more pitches per octave, or embracing a fixed harmonic region and treating commas as expressive events rather than errors.

Composers like La Monte Young exploit sustained just tuning to create harmony that resonates with unusual clarity and reveals combination tones — faint pitches produced by the interaction of two frequencies. Ben Johnston extends just intonation into complex prime ratios (7:4, 11:8, 13:8), producing intervals that have no close analogue in equal temperament. These composers treat the harmonic series itself as a compositional structure, not just a reference for tuning. To engage with their music or to experiment with just intonation yourself, the essential tool is ratio arithmetic: multiply ratios to stack intervals (3:2 × 3:2 = 9:4, then reduce to 9:8 by halving), and convert to cents using the formula cents = 1200 × log₂(ratio).

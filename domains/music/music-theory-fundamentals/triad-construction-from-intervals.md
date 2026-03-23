---
id: triad-construction-from-intervals
title: Building Triads Using Intervals
domain: music
course: music-theory-fundamentals
prerequisites:
- id: intervals-basics
  type: hard
- id: triads
  type: hard
- id: triad-construction-major-minor
  type: soft
builds-toward:
- seventh-chord-types-and-qualities
- diatonic-triad-harmonization
tags:
- triad
- interval
- construction
- harmony
stage: formal-systems
status: validated
---

# Building Triads Using Intervals

## Core Idea
A triad is constructed of two stacked thirds: a root, a third above it, and a fifth above the root. The quality of those thirds (major or minor) determines the chord quality (major, minor, diminished, augmented). Understanding triads as interval stacks clarifies how seventh chords and extensions are built.

## Questions

```yaml
- question: "Which interval structure correctly describes a minor triad?"
  type: multiple-choice
  options:
    - "Major third on the bottom, major third on top"
    - "Minor third on the bottom, major third on top"
    - "Major third on the bottom, minor third on top"
    - "Minor third on the bottom, minor third on top"
  answer: 1
  explanation: "A minor triad is built m3 + M3: a minor third (3 half steps) from root to the middle note, and a major third (4 half steps) from the middle note to the top. Example — D minor: D to F is a minor third, F to A is a major third. This is the exact reversal of a major triad (M3 + m3). Both triads use the same two intervals; only the order changes. Recognizing this symmetry is the core insight: same ingredients, opposite arrangement, opposite color."

- question: "You build a chord by stacking two minor thirds starting from C: C–E♭–G♭. What type of triad is this?"
  type: multiple-choice
  options:
    - "Minor triad — two minor thirds produce a minor chord"
    - "Diminished triad — two stacked minor thirds produce a diminished fifth from root to top"
    - "Augmented triad — the flatted notes create an augmented quality"
    - "Major triad — minor thirds combine to produce a major sound at the outer interval"
  answer: 1
  explanation: "Two stacked minor thirds (3 + 3 = 6 half steps) produce a diminished fifth — the tritone — from root to top note. C–E♭ is a minor third; E♭–G♭ is another minor third; C to G♭ is only 6 half steps, a diminished fifth. This is the diminished triad (m3 + m3). Two minor thirds never produce a minor chord — a minor triad requires m3 + M3. The instability of the tritone at the outer interval is what gives diminished chords their tense, restless quality."

- question: "A major triad and a minor triad contain the same two intervals (a major third and a minor third) — they just appear in opposite order."
  type: true-false
  answer: true
  explanation: "This is the core insight of interval-stack triad construction. Major triad: M3 (bottom) + m3 (top). Minor triad: m3 (bottom) + M3 (top). Same two intervals, reversed order. The placement of the larger interval at the bottom vs. the top completely changes the chord's character from bright (major) to darker (minor). Understanding this reversal explains both triads from a single structural observation."

- question: "An augmented triad has a larger outer interval (root to fifth) than a major triad."
  type: true-false
  answer: true
  explanation: "An augmented triad is built M3 + M3: two major thirds stacked. This gives an augmented fifth (8 half steps) from root to top, compared to the perfect fifth (7 half steps) in a major triad. By contrast, a diminished triad (m3 + m3) has only a diminished fifth (6 half steps). The outer interval — perfect, augmented, or diminished — names the chord quality and follows directly from the stacked intervals."

- question: "How would you construct a dominant seventh chord using the interval-stack method? Name each stacked interval and give a concrete example starting from G."
  type: short-answer
  answer: "A dominant seventh chord stacks three intervals: M3 + m3 + m3. Starting from G: G to B is a major third (4 half steps), B to D is a minor third (3 half steps), D to F is a minor third (3 half steps). Result: G–B–D–F, the G dominant seventh chord."
  explanation: "The interval-stack view extends directly from triads to seventh chords by adding one more third above. The dominant seventh begins with the major triad (M3 + m3) and adds a minor third on top. Rather than memorizing a separate formula for each chord type, you apply the same stacking logic: identify the quality of each successive third. This framework also extends to ninths, elevenths, and thirteenth chords (jazz extensions) by continuing to stack thirds above."
```

## Explainer

You know that an **interval** is a measured distance between two pitches — a major third spans four half steps, a minor third spans three. You also know that a **triad** has three notes: a root, a third, and a fifth. What you're learning here is how to see those two ideas as one: a triad is nothing more than two stacked thirds. This perspective is more powerful than memorizing chord formulas, because it makes the entire system of chords transparent and extensible.

Start with a C major triad: C–E–G. From C to E is a **major third** (4 half steps). From E to G is a **minor third** (3 half steps). So a major triad = M3 on the bottom, m3 on top. Now build a D minor triad: D–F–A. From D to F is a **minor third** (3 half steps). From F to A is a major third (4 half steps). Minor triad = m3 on the bottom, M3 on top. The two qualities are the same two intervals, just in reverse order. This is why major and minor triads share an interval-content but have opposite "color" — the placement of the larger interval at the bottom versus the top changes the triad's character entirely.

The other two triad qualities follow the same logic. A **diminished triad** stacks two minor thirds: m3 + m3. C–E♭–G♭ is an example. Because both thirds are small, the fifth from root to top note is only 6 half steps — a **diminished fifth** (also called a tritone). This interval is unstable and tense, which is why diminished chords have a characteristic restless quality. An **augmented triad** does the opposite: M3 + M3. C–E–G♯ gives you a major third from C to E, another major third from E to G♯, and a resulting **augmented fifth** (8 half steps) from root to top. The symmetry makes augmented chords ambiguous — you can't easily tell which note is the "root" by ear.

The real payoff of the interval-stack view is that it makes **seventh chords** and beyond immediately comprehensible. A seventh chord is just a triad with another third stacked on top. A **major seventh chord** is M3 + m3 + M3 (three thirds stacked). A **dominant seventh chord** (the most important in tonal music) is M3 + m3 + m3. A **minor seventh chord** is m3 + M3 + m3. You don't need to memorize each formula separately — you just need to know what the stacked intervals are and listen for the quality at each step. From there, adding ninths, elevenths, and thirteenths (extended chords in jazz) follows the exact same logic, just adding more thirds above. The triad-as-interval-stack is not just one way to think about chords; it is the generative structure that makes all of tonal harmony coherent.

---
id: invertible-counterpoint-extended
title: Extended Invertible Counterpoint
domain: music
course: advanced-music-theory
prerequisites:
- id: invertible-counterpoint-advanced
  type: hard
- id: voice-leading-voice-exchange
  type: soft
builds-toward:
- species-counterpoint-free-composition
- polyphonic-analysis-advanced
tags:
- counterpoint
- inversion
- voice-leading
stage: expert
status: draft
---

# Extended Invertible Counterpoint

## Core Idea
Extended invertible counterpoint allows voices to exchange at compound intervals and across multiple voice counts. This maximizes contrapuntal flexibility in complex textures while maintaining harmonic integrity. Analysis reveals how exchanges clarify or obscure voice function.

## How It's Best Learned
Study triple and quadruple invertible counterpoint in Brahms symphonies and Mozart concertos. Compose passages in extended invertible counterpoint, monitoring harmonic function across inversional exchanges.

## Common Misconceptions
- Assuming invertible counterpoint requires literal inversion of all voices; free inversion and partial exchange occur. - Confusing interval of inversion with voice count; four-part invertible counterpoint may use multiple inversion intervals. - Overlooking harmonic ambiguity when interval direction changes timbre.

## Questions

```yaml
- question: "A composer writes a three-voice texture in which any voice can serve as soprano, alto, or bass. How many distinct voice orderings must all produce acceptable counterpoint for the texture to qualify as triple invertible counterpoint?"
  type: multiple-choice
  options:
    - "2 — the original ordering and one complete inversion"
    - "3 — one for each voice serving as the bass line"
    - "6 — all permutations of three distinct voices"
    - "9 — each pair of voices can exchange positions independently"
  answer: 2
  explanation: "With three voices, the possible orderings (soprano/alto/bass assignments) are the 3! = 6 permutations of three objects. Genuine triple invertible counterpoint requires that ALL six permutations produce acceptable voice-leading. This is the combinatorial heart of the technique: each additional voice multiplies the number of required valid arrangements factorially, which is why the compositional constraints grow so rapidly."

- question: "In counterpoint designed to invert at the tenth (a compound third), what does a perfect fifth (interval 5) transform to under voice exchange?"
  type: multiple-choice
  options:
    - "A perfect fourth (interval 4) — as in standard inversion at the octave, using formula 9 − n"
    - "A perfect fifth (interval 5) — perfect fifths are preserved under any inversion"
    - "A sixth (interval 6) — using the formula 11 − n at the tenth"
    - "An octave (interval 8) — compound inversion doubles the interval value"
  answer: 2
  explanation: "At the octave the formula is 9 − n: a fifth (5) maps to a fourth (4). At the tenth, the formula changes to 11 − n: a fifth (5) maps to 11 − 5 = 6, a sixth. This different mapping means that intervals safe at the octave may be problematic at the tenth, and vice versa. The interval of inversion must be chosen first, then the transformation formula applied consistently to identify which intervals to use and avoid."

- question: "Quadruple invertible counterpoint is more demanding than triple invertible counterpoint because it requires all 24 permutations of four voices to produce acceptable part-writing."
  type: true-false
  answer: true
  explanation: "4! = 24 permutations must all satisfy contrapuntal constraints, versus 3! = 6 for triple invertible counterpoint. This factorial growth explains why writing genuine quadruple invertible counterpoint is among the most demanding compositional feats. Bach's Art of Fugue and Brahms's late chamber works contain celebrated examples; in practice, composers often exploit a subset of the 24 permutations rather than all of them."

- question: "In invertible counterpoint at the octave, a perfect fifth between two voices transforms to another perfect fifth after the voices exchange positions."
  type: true-false
  answer: false
  explanation: "At the octave, the transformation formula is 9 − n. A perfect fifth (interval 5) maps to 9 − 5 = 4 — a perfect fourth, not another fifth. This exchange between fifths and fourths is exactly why those intervals require careful handling: a fifth in the original (generally consonant in strict counterpoint) becomes a fourth (treated as a dissonance requiring resolution in many contrapuntal contexts) after voice exchange."

- question: "Explain why the interval of inversion matters when composing invertible counterpoint, and how the transformation formula changes between inversion at the octave and at the tenth."
  type: short-answer
  answer: "The interval of inversion determines how each interval between voices transforms after the exchange. At the octave, when voices swap register, interval n becomes 9 − n: a third (3) becomes a sixth (6), a fifth (5) becomes a fourth (4). At the tenth, the formula changes to 11 − n: a third (3) becomes an octave (8), a fifth (5) becomes a sixth (6). Different mappings mean different intervals are 'safe' (consonant in both the original and inverted forms). A composer must choose the inversion interval first, then apply the appropriate formula to identify which intervals to use and avoid throughout the passage."
  explanation: "This is why analyzing invertible counterpoint requires identifying the intended inversion interval — the same passage may be technically correct for one inversion interval and full of violations for another. The formula change between octave and tenth arises from the different transposition the inversion produces on the interval stack."
```

## Explainer

You already know invertible counterpoint at the octave (and likely at the 10th and 12th): two voices swap their relative positions so that the upper voice moves below and vice versa. The interval-sum formula tells you which intervals remain consonant after exchange — at the octave, an interval of n becomes 9 − n, so you must avoid any original interval whose complement under this formula produces a dissonance. **Extended** invertible counterpoint generalizes both dimensions of this idea: it extends to more than two voices, and to exchange intervals other than the simple octave.

**Triple invertible counterpoint** involves three voices that can be placed in any of their 3! = 6 possible orderings (top, middle, bottom permuted freely) while still producing acceptable part-writing in every arrangement. This is a remarkable compositional economy: a single three-voice module generates six distinct textures. Bach's inventions and sinfonias show this routinely; the opening of the C-minor Sinfonia BWV 773 is a canonical example where the three voices are exhaustively permuted across the piece. The compositional constraint is stringent — every interval relationship must remain consonant under all six permutations — but the payoff is a passage that recombines itself without requiring new material.

**Quadruple invertible counterpoint** extends to four voices and 4! = 24 possible arrangements, though in practice composers exploit a subset of permutations rather than all twenty-four. The interval constraints multiply correspondingly, severely restricting what harmonic intervals and melodic profiles the individual voices can contain. Writing genuine quadruple invertible counterpoint is among the most demanding contrapuntal feats, and Brahms's late chamber works and Bach's The Art of Fugue contain some of the most celebrated examples.

The **compound interval** dimension adds another layer of complexity. In standard invertible counterpoint, a voice exchange produces a new interval at a predictable transposition. When voices exchange at a compound interval — say, at the 10th (a third plus an octave) — the interval transformation formula changes: at the 10th, interval n becomes 11 − n. This different mapping changes which intervals are safe and which are dangerous. A fifth (5) maps to 11 − 5 = 6, a dissonant sixth in certain contrapuntal contexts, so fifths must be used with care in counterpoint designed to invert at the 10th. Mastering extended invertible counterpoint means internalizing these different transformation formulas and voice-count constraints simultaneously — which is why the technique is reserved for advanced study and appears most naturally in analysis of the high Baroque and German Classical tradition.

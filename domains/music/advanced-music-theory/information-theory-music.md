---
id: information-theory-music
title: Information Theory in Music
domain: music
course: advanced-music-theory
prerequisites:
- id: musical-mathematics-symmetry
  type: soft
- id: fourier-analysis-musical-signals
  type: soft
- id: bayes-theorem
  type: soft
- id: probability-axioms
  type: soft
- id: conditional-probability
  type: soft
- id: logarithm-properties
  type: soft
- id: expected-value-theory
  type: soft
builds-toward:
- psychoacoustics-perception-theory
tags:
- information-theory
- mathematics
- perception
stage: advanced
status: draft
---

# Information Theory in Music

## Core Idea
Information theory quantifies predictability (entropy) and surprise (information content) in music. High entropy signals maximum unpredictability; low entropy signals redundancy. Listener engagement often optimizes at intermediate entropy. This framework explains how structure and variation interact.

## How It's Best Learned
Analyze entropy in excerpts of minimalist, serial, and tonal music. Calculate information content of pitch sequences to quantify predictability and surprise.

## Common Misconceptions
- Assuming high entropy always creates interest; predictable music may be engaging for other reasons. - Confusing information content with information theory; distinct technical meanings. - Overlooking that information theory ignores context, style convention, and listener expectation.

## Explainer

You already know entropy and expected value from probability theory. **Shannon entropy** H(X) = −Σ p(xᵢ) log₂ p(xᵢ) measures the average unpredictability of a random variable X. When applied to music, X is a musical event — the next pitch, the next chord, the next rhythmic value — and the probabilities come from how often each value follows the previous context. A melody where every note is drawn uniformly from twelve pitch classes has maximum entropy (about 3.58 bits per note). A melody that always repeats a single pitch has zero entropy. Most tonal music sits far below maximum entropy because the harmonic and melodic conventions of a style heavily constrain what comes next.

The **information content** of a specific event xᵢ is −log₂ p(xᵢ). Rare events carry high information content; common events carry low information content. In tonal music, the leading tone resolving to the tonic has very low information content — it is almost certain to happen. A sudden chromatic pitch in a diatonic melody has high information content — it surprises. This is the formal definition of musical surprise: not a subjective impression, but a measurable quantity derived from the statistical model of the style. Bayesian updating is implicit here: listeners continuously revise their probabilistic model of the piece as it unfolds, using conditional probabilities P(next note | everything heard so far) to predict what comes next.

The key insight for musical aesthetics is what researchers call the **optimal entropy zone**. Extremely low-entropy music (highly predictable repetition) quickly becomes boring — the listener's prediction engine has nothing to do. Extremely high-entropy music (random, unpredictable events) overwhelms the listener and prevents the formation of expectations that can then be fulfilled or violated. The most engaging music occupies an intermediate zone where expectations are formed and then sometimes confirmed and sometimes beautifully violated. This predicts why both rigid minimalism and chaotic serialism can exhaust listeners, while tonal music with its mixture of predictable cadences and expressive surprises holds attention.

Applying this framework requires choosing what to model: pitch sequences, harmonic progressions, rhythmic patterns, or all simultaneously. Each choice gives a different entropy estimate. A Baroque chorale has low harmonic entropy (progressions follow strict rules) but may have moderate melodic entropy (individual voice leading contains more surprises). A serialist work may have low entropy at the row level (the row is deterministic) but high entropy from the listener's perspective (who cannot perceive the row without score study). Information theory thus distinguishes between the composer's structure and the listener's experience — a distinction your prerequisite in Fourier analysis and psychoacoustics should remind you is fundamental to how music perception works.

---
id: entropy-predictability-music
title: Information Theory and Entropy in Musical Structure
domain: music
course: advanced-music-theory
prerequisites:
- id: mathematical-structure-analysis
  type: soft
- id: stochastic-composition
  type: soft
- id: expected-value
  type: soft
- id: probability-axioms
  type: soft
- id: logarithm-properties
  type: soft
- id: conditional-probability
  type: hard
tags:
- information-theory
- entropy
- predictability
- analysis
stage: abstract-reasoning
status: draft
---

# Information Theory and Entropy in Musical Structure

## Core Idea
Information theory measures the predictability of a sequence. High-entropy music (high uncertainty) sounds random; low-entropy music (high predictability) sounds monotonous. Optimal listening experience often occupies middle ground. Analyzing entropy reveals how composers balance familiarity with surprise to engage listeners.

## Explainer

From your study of probability and expected value, you know that entropy H(X) = −Σ p(x) log₂ p(x) measures the average uncertainty in a random variable. When all outcomes are equally likely, entropy is maximized — you can't predict anything. When one outcome is certain (p = 1 for some x), entropy is zero — there's nothing to learn. Applied to music, the "random variable" is the next note, chord, or rhythmic event, and the "distribution" comes from the statistical regularities in the piece. A piece where every chord transition is equally probable would have maximum harmonic entropy; a piece where every chord is the same would have zero entropy. Real music occupies the space between.

The key tool for measuring musical entropy is the **n-gram model**, borrowed from computational linguistics. A 1-gram (unigram) model counts how often each pitch class or chord appears in isolation. A 2-gram (bigram) model tracks which events tend to follow which others. A 3-gram (trigram) model conditions on the previous two events. The conditional entropy H(Xₙ₊₁ | Xₙ) — which you can compute from your prerequisite knowledge of conditional probability — measures how much uncertainty remains about the next event given the current one. This is the entropy that matters for perceived predictability: a tonal melody in C major has very low conditional pitch entropy because scale degrees strongly constrain the next note. A serial row, intentionally avoiding repetition, has much higher conditional entropy.

The psychoacoustic insight is that **optimal engagement** lies in the middle range of entropy — neither fully predictable nor fully random. Fully predictable music (like a nursery rhyme ostinato) loses interest because there is nothing to learn or anticipate. Fully random music (white noise, or an uncorrelated sequence of pitches) provides no pattern to latch onto and sounds like noise. This "sweet spot" principle underlies why tonal music uses hierarchical structure: phrase-level patterns are predictable enough to provide stability, while local melodic and harmonic choices carry enough surprise to sustain interest. Composers like Haydn are sometimes described as masters of **controlled entropy** — establishing expectations and then violating them at precisely calculated moments.

Analyzing entropy across a piece reveals its large-scale architecture. Passages of tension typically correspond to high local entropy: chromatic lines, ambiguous harmonies, accelerated rhythm. Passages of release correspond to low entropy: diatonic motion, clear tonal centers, regular meter. The **entropy profile** over time can be thought of as a formal map of the piece's emotional trajectory — not a replacement for conventional analysis, but a complementary view that quantifies the intuitive language of tension and release that musicians have always used. More advanced applications use Markov chain models of harmony (building on your study of stochastic composition) to generate music with a target entropy level, or to compare the statistical "style signature" of different composers.

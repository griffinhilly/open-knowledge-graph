---
id: algorithmic-composition-theory
title: Algorithmic Composition Theory
domain: music
course: advanced-music-theory
prerequisites:
- id: stochastic-composition
  type: soft
- id: temporal-proportions-ratios
  type: soft
- id: algorithm-complexity
  type: soft
- id: algorithm-analysis-big-o
  type: soft
- id: recursion
  type: soft
builds-toward:
- musical-mathematics-symmetry
- information-theory-music
tags:
- algorithm
- composition
- mathematics
stage: advanced
status: draft
---

# Algorithmic Composition Theory

## Core Idea
Algorithmic composition uses formal rules, randomness, or dynamical systems to generate structure. Algorithms may be deterministic (rule-based) or probabilistic (chance-based); they may operate at pitch, rhythm, form, or orchestration levels. Analyzing algorithmic music reveals how rules interact with compositional intent.

## How It's Best Learned
Study Xenakis's stochastic and granular works and Cope's algorithmic systems. Implement a simple compositional algorithm (L-system, cellular automaton) and analyze results for musical interest and coherence.

## Common Misconceptions
- Assuming algorithmic composition is impersonal; algorithms are compositional tools shaped by designers. - Confusing algorithmic composition with random chance; many algorithms are highly structured and deterministic. - Overlooking that listener perception may diverge from algorithmic intent.

## Explainer

An **algorithm** is a finite set of rules that, given an input, produces an output. You already know this from your programming prerequisites. Algorithmic composition simply applies this idea to music: the input is some initial state or seed, the rules govern how musical material is generated or transformed, and the output is a score or performance. What makes algorithmic composition theoretically interesting is that the composer's choices live at the level of the rules, not the notes — the composer designs a system, and the system generates the music.

The spectrum from deterministic to stochastic covers most approaches. At the deterministic end, a **rule-based system** produces identical output from identical input. **L-systems** (Lindenmayer systems), which you know from recursion, are a key example: a grammar with rewrite rules (e.g., A → AB, B → A) generates strings that grow self-similarly with each iteration. When these strings are mapped to pitches or rhythms, the result has fractal-like structure — the small-scale shape mirrors the large-scale shape. Xenakis used such recursive and mathematical structures extensively. At the stochastic end, **Markov chains** — which connect to your stochastic composition prerequisite — generate each note by sampling from a probability distribution that depends on the preceding note (or notes). First-order Markov chains capture local melodic tendencies; higher-order chains capture longer patterns. The result sounds more "style-like" than purely random, but is not deterministic.

**Cellular automata** offer a striking middle ground. A one-dimensional cellular automaton begins with a row of cells, each in a state (say 0 or 1), and applies a local rule at each time step: the new state of each cell depends on the states of its neighbors. The result is a time-space grid whose rows can be interpreted as rhythm patterns or pitch sequences. Rule 30 (one of Wolfram's elementary automata) produces apparently random output from a single "on" cell; Rule 110 produces structured, complex patterns. Mapping these patterns to musical parameters yields textures that are rule-governed but perceptually unpredictable — a combination that many composers find musically rich.

The deepest theoretical question in algorithmic composition is not technical but aesthetic: what is the composer's role when the system generates the notes? The answer is that the composer's voice lives in the choice and design of the algorithm — what parameters are controlled, what randomness is admitted, how musical parameters are mapped from formal structures. David Cope's Experiments in Musical Intelligence (EMI) analyzed style signatures from large corpora and recombined them algorithmically, producing music that fooled expert listeners in blind tests. This raised the question of whether style is rule-capturable and what authorship means when rules are generative. Algorithmic composition theory does not resolve this question — it sharpens it.

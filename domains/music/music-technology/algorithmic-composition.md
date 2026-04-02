---
id: algorithmic-composition
title: Algorithmic Composition
domain: music
course: music-technology
prerequisites:
- id: audio-programming-fundamentals
  type: soft
builds-toward: []
tags:
- algorithmic-composition
- generative-music
- computer-music
- music-theory
stage: expert
status: validated
---

# Algorithmic Composition

## Core Idea
Algorithmic composition is the use of formal rules, mathematical processes, or computational systems to generate musical structures — notes, rhythms, harmonies, textures, and form — either autonomously or as extensions of a composer's intent. Rather than specifying every note manually, the composer designs a system whose output is the composition.

The history of algorithmic composition predates computers. Mozart's "Musikalisches Würfelspiel" (Musical Dice Game, ~1793) used random dice rolls to select pre-composed measures from tables, assembling a new minuet on each play. Twelve-tone serialism (Schoenberg, Webern) applied strict permutation rules to a tone row. Iannis Xenakis applied stochastic processes (probability distributions, Markov chains, random walks) to generate large-scale texture and density — his Metastasis uses mathematical transformations of a pitch set to create the orchestral glissandi of its opening.

Contemporary algorithmic composition uses several paradigms. Constraint-based composition specifies rules (harmonic constraints, voice-leading rules, rhythmic patterns) and searches for solutions — similar to constraint satisfaction problems in computer science. Markov chain composition builds transition probability matrices from existing music (or user-specified probabilities) and generates new sequences by stochastic transitions between states. L-systems (Lindenmayer systems, originally developed for modeling plant growth) generate recursive, self-similar musical structures that produce complex patterns from simple rewriting rules. Generative AI approaches (trained on large MIDI or audio datasets) learn statistical structure from existing music and generate novel compositions probabilistically.

Live coding — writing and modifying algorithmic code in real time as a performance practice — has emerged as a distinct art form, exemplified by environments like TidalCycles (Haskell-based) and SuperCollider, where the code itself is projected to the audience.

## Questions

```yaml
- question: "In a first-order Markov chain model for melody generation, what determines the next note?"
  type: multiple-choice
  options:
    - "The key and tempo of the piece"
    - "A probability distribution conditioned only on the current note"
    - "The last three notes and the current beat position"
    - "A random selection from all available pitches with equal probability"
  answer: 1
  explanation: "A first-order Markov chain has the Markov property: the next state depends only on the current state (the current note), not on the history before it. This produces statistically plausible melodic steps but lacks long-range coherence."

- question: "True or false: Algorithmic composition necessarily produces music with no human involvement or artistic intent."
  type: true-false
  answer: false
  explanation: "Algorithmic composition is a compositional technique, not a replacement for human authorship. The composer designs the system, selects parameters, curates outputs, and makes all the significant aesthetic decisions — the algorithm extends and executes their intent."

- question: "What is an L-system in the context of algorithmic composition, and what type of musical structures does it produce?"
  type: short-answer
  answer: "An L-system (Lindenmayer system) is a parallel rewriting system that recursively replaces symbols in a string with more complex substitutions according to production rules. Applied to music, it generates self-similar, fractal-like structures — nested rhythmic or melodic patterns that exhibit similar structure at multiple scales."
  explanation: "The recursive nature of L-systems produces structural self-similarity: a theme that appears at multiple hierarchical levels simultaneously, similar to fractal geometry. Bach's counterpoint and natural forms like branching trees exhibit similar nested self-similarity."

- question: "A composer wants to generate music that statistically resembles Bach chorales — using the same harmonic progressions and voice-leading tendencies — without directly copying any existing chorale. Which algorithmic approach is most appropriate?"
  type: multiple-choice
  options:
    - "Randomly select notes from Bach's scale choices"
    - "Train a Markov chain or neural network on a corpus of Bach chorales, then generate new sequences by sampling from the learned distributions"
    - "Apply the same rules to a different tone row"
    - "Use an L-system with Bach's melodic intervals as production rules"
  answer: 1
  explanation: "Markov chains or neural networks trained on Bach chorale data learn the statistical regularities of his harmonic and voice-leading choices — transition probabilities between chords, melodic interval tendencies, cadence patterns. Generating from these models produces new sequences with similar stylistic properties."

```

## Explainer

Algorithmic composition represents a fundamental reframing of the composer's role: from one who specifies every event to one who designs systems that generate events. This shift extends creative possibilities in both directions — algorithms can produce complexity and detail far beyond what any human could manually specify, while also exploring territory outside human intuition.

The relationship between algorithmic output and musical value is philosophically complex. Markov-generated melodies can be statistically indistinguishable from their training corpus at the local level but fail to exhibit the large-scale coherence and intention of human composition. Neural network models have closed this gap significantly — OpenAI's MuseNet, Google's Magenta, and Sony's Flow Machines demonstrated that neural models can generate hours of stylistically coherent music. But the question of whether statistically sophisticated generation constitutes musical creativity remains open.

Algorithmic composition also offers practical tools for non-specialists. Generative composition software (Nodal, MaxScore, Symbolic Composer) allows musicians without programming backgrounds to build algorithmic systems through graphical interfaces. Music theory researchers use algorithmic tools to test hypotheses about tonal syntax, generating corpora of controlled examples that would be impractical to compose manually. In game audio, procedural music — algorithmically assembled from components based on gameplay state — extends algorithmic composition principles into interactive media, where fixed composed scores cannot accommodate the branching, open-ended nature of play.

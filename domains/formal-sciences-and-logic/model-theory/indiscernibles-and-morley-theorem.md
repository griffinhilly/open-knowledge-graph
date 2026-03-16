---
id: indiscernibles-and-morley-theorem
title: Indiscernible Sequences and Morley's Categoricity Theorem
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: morleys-uncountable-categoricity
  type: hard
- id: compactness-theorem-model-theory
  type: soft
builds-toward:
- strongly-minimal-and-geometry
- spectrum-and-number-of-models
tags:
- indiscernibles
- morley
- categoricity
stage: advanced
status: draft
---

# Indiscernible Sequences and Morley's Categoricity Theorem

## Core Idea
An indiscernible sequence is a sequence of elements that realize the same type in all parameters. Morley's categoricity theorem uses indiscernibles to prove: if a complete theory T is categorical in some uncountable cardinality, then T is categorical in all uncountable cardinalities. This deep result reveals that categorical theories have uniform structure across uncountable cardinalities.

## How It's Best Learned
Study the proof of Morley's theorem, focusing on the construction of indiscernibles using a Ramsey-theoretic argument on types.

## Explainer

When you study a structure model-theoretically, you describe elements through the formulas they satisfy — their *types*. An **indiscernible sequence** takes this idea further: a sequence (a₁, a₂, a₃, ...) is indiscernible over a parameter set A if, for any two finite subsequences of the same length, they satisfy exactly the same formulas with parameters from A. In other words, the elements are interchangeable — the theory cannot tell them apart by any formula. Think of it as a sequence of "generic" elements where the order matters but individual identities do not.

Indiscernibles are built using a Ramsey-theoretic argument on types. Given any infinite sequence of elements in a saturated model, one can extract an infinite indiscernible subsequence — a version of the infinite Ramsey theorem applied to types rather than colors. This gives an incredibly powerful tool: whenever you need a "uniform" or "generic" collection of elements in a model, indiscernibles provide them. The compactness theorem from your prerequisites ensures that such sequences can be found not just in a single model but in arbitrarily large ones.

**Morley's categoricity theorem** is the central result in classical model theory. It states: if a complete theory T (in a countable language) is categorical in *some* uncountable cardinality — meaning it has exactly one model of that size up to isomorphism — then T is categorical in *all* uncountable cardinalities. This is surprising because models of different uncountable cardinalities can look very different in other theories. Morley's theorem says categoricity at one uncountable size propagates everywhere.

The proof uses indiscernibles essentially. In a categorical theory, the models must have highly uniform structure — any large model can be "built up" from indiscernible sequences in a controlled way. The key steps are: (1) show that a categorical theory is ω-stable (types over countable sets are countable); (2) use ω-stability to construct indiscernible sequences in models of any uncountable size; (3) show these sequences determine the model up to isomorphism. The indiscernibles act as "coordinates" that uniquely characterize the model's structure.

Morley's theorem launched the modern classification theory of first-order theories. The question "how many models of each cardinality does a theory have?" — the **spectrum problem** — turns out to have a surprisingly structured answer (Shelah's main gap theorem). But Morley's result was the first deep evidence that model structure is not arbitrary: theories that are categorical anywhere are categorical everywhere, revealing a dichotomy between the "tame" (categorical) and the "wild" (many models) that permeates all of classification theory.

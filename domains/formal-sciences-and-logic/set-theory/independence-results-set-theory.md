---
id: independence-results-set-theory
title: Independence Results in Set Theory
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: continuum-hypothesis
  type: hard
- id: cofinality-and-regular-cardinals
  type: soft
- id: godels-incompleteness-theorems
  type: soft
tags:
- independence
- forcing
- constructible universe
- Godel
- Cohen
- models
stage: formal-systems
status: validated
---

# Independence Results in Set Theory

## Core Idea
A statement is independent of ZFC if neither it nor its negation is provable from ZFC. Gödel (1938) constructed the inner model L (the constructible universe) and showed both CH and AC hold in L, proving ZFC cannot refute them. Cohen (1963) invented forcing — building generic extensions of models by adding new sets satisfying carefully chosen conditions — and showed ZFC cannot prove CH or many other natural statements. Independence results demonstrate that ZFC leaves infinitely many natural questions about infinite sets undecided, including the exact value of 2^ℵ₀, the existence of measurable cardinals, and the projective determinacy of infinite games.

## How It's Best Learned
Study Gödel's L at the sketch level: sets built by definable operations in a transfinite hierarchy, within which CH holds by a counting argument. Then understand Cohen forcing conceptually: forcing conditions are finite partial approximations to a new 'generic' set; combining countably many conditions produces a model in which CH fails. The key takeaway is that different models of ZFC can have wildly different cardinal arithmetic.

## Common Misconceptions
- Independence does not mean a statement is meaningless or lacks a truth value — it means ZFC cannot determine it. Whether it has a 'real' truth value depends on philosophical commitments about mathematical Platonism.
- Forcing does not change 'the' actual universe of sets; it constructs alternative models within a meta-theory, usually ZFC itself or a fragment of it.

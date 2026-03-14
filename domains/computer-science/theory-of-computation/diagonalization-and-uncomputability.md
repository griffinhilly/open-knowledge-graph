---
id: diagonalization-and-uncomputability
title: Diagonalization and Uncomputability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: universal-turing-machine
  type: hard
- id: cardinality-and-countability
  type: soft
builds-toward:
- undecidable-language-examples
tags:
- diagonalization
- uncomputability
- unrecognizable
- cantor
- proof-technique
stage: advanced
status: draft
---

# Diagonalization and Uncomputability

## Core Idea
The diagonal argument proves there are uncomputable languages: list all TMs and strings; construct a language differing from the i-th TM's language on the i-th string. This language cannot be recognized by any TM. Diagonalization, adapted from Cantor's set theory, establishes fundamental limits: computation is countable but languages are uncountable.

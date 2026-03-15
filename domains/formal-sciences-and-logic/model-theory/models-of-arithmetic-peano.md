---
id: models-of-arithmetic-peano
title: Models of Peano Arithmetic and Non-Standard Models
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: formal-arithmetic-and-expressibility
  type: hard
- id: complete-first-order-theories
  type: soft
- id: arithmetic-functions-and-multiplicativity
  type: soft
builds-toward:
- undecidability-and-gödel
- omitting-types-theorem-countable
tags:
- peano-arithmetic
- non-standard-models
- arithmetic
stage: advanced
status: draft
---

# Models of Peano Arithmetic and Non-Standard Models

## Core Idea
Peano arithmetic (PA) has non-standard models: countably infinite models satisfying all PA axioms but containing infinite integers beyond all standard numerals. Every non-standard model contains a copy of the standard natural numbers followed by a densely ordered structure of infinitely large elements. Non-standard models demonstrate that first-order logic cannot axiomatize arithmetic uniquely.

## How It's Best Learned
Construct a non-standard model using the compactness theorem by adding a constant c and axioms c > n for all numerals n. Study the structure of the infinite part.

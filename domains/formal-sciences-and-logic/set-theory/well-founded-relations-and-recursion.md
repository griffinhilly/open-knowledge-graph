---
id: well-founded-relations-and-recursion
title: Well-Founded Relations and Transfinite Recursion
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: binary-relations-definition-and-properties
  type: hard
- id: recursion-on-finite-structures
  type: soft
- id: binary-relations
  type: soft
builds-toward:
- transfinite-induction
- natural-numbers-as-iterative-construction
- ordinal-numbers-and-order
tags:
- well-foundedness
- recursion
- induction
stage: formal-systems
status: draft
---

# Well-Founded Relations and Transfinite Recursion

## Core Idea
A relation R is well-founded if every non-empty subset has an R-minimal element. Well-founded relations support recursion and induction: any function can be defined recursively by specifying its value on R-minimal elements and then using values at 'R-smaller' arguments. This generalizes finite induction to potentially infinite domains.

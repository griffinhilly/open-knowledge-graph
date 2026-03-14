---
id: time-hierarchy-theorem
title: Time Hierarchy Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: time-complexity-classes-formal
  type: hard
- id: turing-machines-formal
  type: hard
builds-toward:
- space-hierarchy-theorem
tags:
- separations
- resource-bounded
- computability
stage: advanced
status: draft
---

# Time Hierarchy Theorem

## Core Idea
The time hierarchy theorem states that for reasonable complexity measures, strictly greater time allows a Turing machine to decide strictly more languages. Formally, if f and g are time-constructible functions with f·log(f) = o(g), then DTIME(f) ⊊ DTIME(g). This unconditionally proves P ⊂ EXPTIME and guarantees unbounded growth of computational power with time resources.

## How It's Best Learned
Understand the proof using diagonalization: a TM with more time can solve the time-bounded halting problem for TMs with less time, constructing a language not in the smaller class.

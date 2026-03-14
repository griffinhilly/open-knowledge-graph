---
id: recursively-enumerable-languages
title: 'Recursively Enumerable Languages: Semi-Decidability'
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: recursive-languages
  type: hard
builds-toward:
- turing-degrees-equivalence
- undecidable-problems-examples
tags:
- semi-decidable
- recursively-enumerable
- halting
- verification
stage: advanced
status: draft
---

# Recursively Enumerable Languages: Semi-Decidability

## Core Idea
A language is recursively enumerable (RE) if there exists a Turing machine that accepts exactly those strings in the language but may not halt on strings outside the language. RE languages represent problems where 'yes' answers are verifiable but 'no' answers may require infinite computation. Every recursive language is RE, but not vice versa.

## How It's Best Learned
Use the Halting Problem as motivating example: it's RE (simulate and accept if halts) but not recursive. Contrast with problems that are RE and recursive.

## Common Misconceptions
- Confusing 'enumerates' with 'lists in order.' RE means we can verify membership by simulation, not necessarily list in canonical order.
- Thinking RE languages are rarer than recursive. In fact, the complement of an undecidable problem is often not RE.

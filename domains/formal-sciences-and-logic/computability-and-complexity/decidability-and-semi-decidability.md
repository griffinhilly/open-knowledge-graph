---
id: decidability-and-semi-decidability
title: Decidable and Semi-Decidable Languages
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: turing-machines-formal
  type: hard
- id: halting-problem-formal
  type: hard
builds-toward:
- re-and-co-re-languages
- reducibility-many-one-formal
tags:
- decidability
- languages
- recognition
stage: advanced
status: draft
---

# Decidable and Semi-Decidable Languages

## Core Idea
A language is decidable (in RE ∩ co-RE) if a Turing machine can recognize it and also recognize its complement. A language is semi-decidable (RE) if a machine can recognize membership but may loop indefinitely on non-members. The halting problem is semi-decidable but not decidable, illustrating the fundamental gap between 'can verify a solution' and 'can decide membership.'

## How It's Best Learned
Construct machines that decide versus semi-decide simple languages (e.g., palindromes vs. Gödel numbers of terminating programs).

## Common Misconceptions
- Treating 'semi-decidable' as 'almost decidable' (the gap is absolute: a machine cannot bound the time before giving up).
- Confusing co-RE with the complement of a language (co-RE is the complement in the recursion-theoretic hierarchy).

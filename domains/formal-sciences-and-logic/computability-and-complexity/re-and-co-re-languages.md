---
id: re-and-co-re-languages
title: Recursively Enumerable and Co-RE Languages
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: halting-problem
  type: hard
- id: computability-reductions
  type: hard
- id: cardinality-and-countability
  type: soft
builds-toward:
- arithmetical-hierarchy
- kolmogorov-complexity
tags:
- computability
- language-classes
- recognizability
- decidability
stage: advanced
status: draft
---

# Recursively Enumerable and Co-RE Languages

## Core Idea
A language is recursively enumerable (RE) if some Turing machine accepts every string in it, though it may loop forever on strings not in it. A language is decidable (recursive) if some TM both accepts strings in it and rejects strings not in it, always halting. Co-RE languages are complements of RE languages. A language is decidable if and only if it is both RE and co-RE. The halting problem is RE but not decidable; its complement is co-RE but not RE. These classes form the base of the arithmetical hierarchy.

## How It's Best Learned
Contrast 'recognizing' (may loop on negatives) versus 'deciding' (always halts). Prove that the class of decidable languages is closed under complement, while RE is not. Use diagonalization to show the existence of languages outside RE entirely — most languages over any alphabet are not even RE.

## Common Misconceptions
- 'Recursively enumerable' does not imply the language is infinite — every finite language is RE (and in fact decidable).
- A TM that loops forever on some inputs still recognizes a language; recognition requires only that all positives are eventually accepted.

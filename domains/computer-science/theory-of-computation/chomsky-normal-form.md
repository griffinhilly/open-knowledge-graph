---
id: chomsky-normal-form
title: Chomsky Normal Form (CNF)
domain: computer-science
course: theory-of-computation
prerequisites:
- id: context-free-grammars
  type: hard
- id: parse-trees-derivations
  type: soft
builds-toward:
- cfg-pda-equivalence
- pumping-lemma-cfl
tags:
- CNF
- normal-form
- CFG
- CYK
stage: advanced
status: draft
---

# Chomsky Normal Form (CNF)

## Core Idea
Chomsky Normal Form (CNF) is a standardized form for CFGs in which every production is either A → BC (two variables) or A → a (one terminal). Every context-free language has a CFG in CNF. Converting a grammar to CNF involves eliminating ε-productions, unit productions (A → B), and long productions, then ensuring only binary or terminal rules remain. CNF simplifies proofs about CFGs and enables the CYK algorithm for O(n³) parsing of any CFG. Parse trees for CNF grammars are full binary trees.

## How It's Best Learned
Practice the four-step conversion (eliminate ε-rules, unit rules, useless symbols, then binarize) on a concrete grammar. Verify that the converted grammar generates the same language (minus ε if it was originally in the language).

## Common Misconceptions
- Thinking CNF conversion changes the language — it preserves the language (up to possible exclusion of ε).
- Applying the steps out of order, which can reintroduce problems already eliminated.

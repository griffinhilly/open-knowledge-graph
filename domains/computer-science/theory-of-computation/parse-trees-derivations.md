---
id: parse-trees-derivations
title: Parse Trees and Derivations
domain: computer-science
course: theory-of-computation
prerequisites:
- id: context-free-grammars
  type: hard
- id: binary-trees
  type: soft
builds-toward:
- chomsky-normal-form
- cfg-pda-equivalence
tags:
- parse-trees
- derivations
- ambiguity
- CFG
stage: advanced
status: draft
---

# Parse Trees and Derivations

## Core Idea
A parse tree for a CFG derivation is a rooted tree where the root is labeled by the start variable, internal nodes are labeled by variables, leaves are terminals (or ε), and each internal node's children match the right-hand side of some production rule. The yield (left-to-right reading of the leaves) is the derived string. A grammar is ambiguous if some string has two distinct parse trees. Ambiguity matters for parsing: an ambiguous grammar for arithmetic expressions would give different operator precedence for the same input.

## How It's Best Learned
Write parse trees for arithmetic expressions under different grammars (ambiguous vs. unambiguous) and observe how tree structure encodes operator precedence. Distinguish leftmost derivation (always expand leftmost variable first) from rightmost derivation and show both correspond to unique parse trees.

## Common Misconceptions
- Conflating ambiguity in a grammar with ambiguity of a language — some languages are *inherently* ambiguous (no unambiguous grammar exists), but this is distinct from a particular grammar being ambiguous.
- Thinking leftmost and rightmost derivations are the same — they yield the same string but may produce different parse trees for ambiguous grammars.

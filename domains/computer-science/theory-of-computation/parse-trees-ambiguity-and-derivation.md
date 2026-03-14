---
id: parse-trees-ambiguity-and-derivation
title: Parse Trees, Derivations, and Ambiguity in CFGs
domain: computer-science
course: theory-of-computation
prerequisites:
- id: context-free-grammars-and-languages
  type: hard
builds-toward:
- normal-forms-for-context-free-grammars
- cyk-parsing-algorithm
tags:
- cfg
- parse-trees
- ambiguity
stage: abstract-reasoning
status: draft
---

# Parse Trees, Derivations, and Ambiguity in CFGs

## Core Idea
A derivation is a sequence of rule applications producing a string from the start symbol. A parse tree is a hierarchical representation of this derivation. A grammar is ambiguous if some string has multiple distinct parse trees (or leftmost derivations), which complicates parsing and semantics.

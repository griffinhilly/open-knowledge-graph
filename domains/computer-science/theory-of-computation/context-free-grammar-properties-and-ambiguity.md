---
id: context-free-grammar-properties-and-ambiguity
title: Context-Free Grammar Properties and Ambiguity
domain: computer-science
course: theory-of-computation
prerequisites:
- id: context-free-grammars
  type: hard
- id: grammar-fundamentals-and-definitions
  type: soft
builds-toward:
- grammar-normal-forms-analysis
tags:
- cfg
- ambiguity
- left-recursion
- properties
- parse-trees
stage: advanced
status: draft
---

# Context-Free Grammar Properties and Ambiguity

## Core Idea
A grammar is ambiguous if some string has multiple parse trees (different derivations). Left recursion (A → Aα | β) complicates top-down parsing. These properties affect compiler construction: ambiguous grammars must be disambiguated via precedence rules; left-recursive grammars require transformation for LL parsing. Analyzing and fixing these properties is essential for language design.

## Common Misconceptions
- All unambiguous grammars are equally suitable for parsing; actually, LL and LR grammars have specific structural requirements.

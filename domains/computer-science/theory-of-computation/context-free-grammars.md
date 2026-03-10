---
id: context-free-grammars
title: Context-Free Grammars (CFGs)
domain: computer-science
course: theory-of-computation
prerequisites:
- id: regular-language-properties
  type: soft
- id: set-theory-basics
  type: soft
- id: recursion-basics
  type: soft
builds-toward:
- parse-trees-derivations
- chomsky-normal-form
- pushdown-automata
- closure-properties-cfl
tags:
- CFG
- context-free
- grammars
- productions
- derivation
stage: advanced
status: draft
---

# Context-Free Grammars (CFGs)

## Core Idea
A context-free grammar (CFG) is a 4-tuple (V, Σ, R, S) of variables, terminals, production rules, and a start variable. Each rule replaces a single variable with any string of variables and terminals. The language of a CFG is the set of terminal strings derivable from the start variable. CFGs are strictly more powerful than regular expressions — they can describe languages like {aⁿbⁿ} that no DFA can recognize. CFGs are the foundation of programming language syntax, used in parser generators and compilers.

## How It's Best Learned
Begin by writing grammars for arithmetic expressions (which naturally requires recursion) and palindromes. Trace leftmost and rightmost derivations step-by-step. Then attempt to characterize which languages require CFGs versus which are regular.

## Common Misconceptions
- Thinking 'context-free' means the grammar is simple — the term refers specifically to the rule form (single variable on the left side), not the complexity of the language.
- Confusing a grammar with its language: many grammars can generate the same language.
- Assuming every grammar is unambiguous — ambiguity (multiple parse trees for one string) is common and often problematic.

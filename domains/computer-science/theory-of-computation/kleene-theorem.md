---
id: kleene-theorem
title: Kleene's Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: regular-expressions-formal
  type: hard
- id: nfa-to-dfa-conversion
  type: hard
builds-toward:
- regular-language-properties
- closure-properties-regular
tags:
- kleene
- equivalence
- regular
- DFA
- NFA
- regular-expressions
stage: advanced
status: draft
---

# Kleene's Theorem

## Core Idea
Kleene's Theorem states that the three models — DFAs, NFAs, and regular expressions — all define exactly the same class of languages (the regular languages). The theorem is proved constructively: Thompson's construction converts any regular expression to an NFA, subset construction converts NFAs to DFAs, and state elimination converts DFAs back to regular expressions. This equivalence justifies treating these three formalisms as interchangeable descriptions of regular languages.

## Common Misconceptions
- Assuming that because regular expressions look more expressive they must accept more languages.
- Missing that state elimination for DFA→regex can produce exponentially large expressions.
- Thinking the equivalence extends to more powerful models — it holds only among these three finite-state formalisms.

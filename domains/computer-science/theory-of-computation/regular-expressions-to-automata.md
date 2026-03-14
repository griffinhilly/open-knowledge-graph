---
id: regular-expressions-to-automata
title: Regular Expressions and Conversion to Automata
domain: computer-science
course: theory-of-computation
prerequisites:
- id: nondeterministic-finite-automata-nfa
  type: hard
builds-toward:
- regular-languages-fundamentals
- kleene-closure-and-regular-expressions
tags:
- regular-expressions
- automata
- conversion
stage: abstract-reasoning
status: draft
---

# Regular Expressions and Conversion to Automata

## Core Idea
Regular expressions are a compact notation for specifying regular languages using operators: concatenation, alternation (union), and Kleene star. Thompson's construction converts any regular expression into an equivalent NFA, providing a systematic way to build automata from high-level descriptions.

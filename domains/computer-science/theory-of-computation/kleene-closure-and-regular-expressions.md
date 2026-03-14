---
id: kleene-closure-and-regular-expressions
title: Kleene Closure, Kleene Star, and Regular Language Operations
domain: computer-science
course: theory-of-computation
prerequisites:
- id: regular-expressions-to-automata
  type: hard
builds-toward:
- regular-languages-fundamentals
- closure-properties-regular-languages
tags:
- regular-languages
- operations
- closure
stage: abstract-reasoning
status: draft
---

# Kleene Closure, Kleene Star, and Regular Language Operations

## Core Idea
The Kleene star L* of a language L denotes zero or more repetitions of strings from L. Regular languages are closed under union, concatenation, and Kleene star; these operations preserve recognizability by finite automata. Kleene's theorem states that a language is regular if and only if it can be expressed using these operations starting from singleton languages.

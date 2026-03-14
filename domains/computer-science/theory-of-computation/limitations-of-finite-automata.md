---
id: limitations-of-finite-automata
title: Limitations of Finite Automata and Non-Regular Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: pumping-lemma-for-regular-languages
  type: hard
builds-toward:
- context-free-grammars-and-languages
tags:
- automata-limits
- non-regular
- hierarchy
stage: abstract-reasoning
status: draft
---

# Limitations of Finite Automata and Non-Regular Languages

## Core Idea
Finite automata cannot recognize languages requiring unbounded memory, such as balanced parentheses or the set {aⁿbⁿ}. These limitations motivate more powerful models like pushdown automata and context-free grammars, establishing the hierarchy of language classes.

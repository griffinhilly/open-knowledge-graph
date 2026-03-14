---
id: recognizable-languages
title: Recognizable Languages and Turing Recognizability
domain: computer-science
course: theory-of-computation
prerequisites:
- id: decidable-languages
  type: hard
builds-toward:
- undecidable-problems
tags:
- recognizable
- semi-decidable
- turing-recognizable
stage: abstract-reasoning
status: draft
---

# Recognizable Languages and Turing Recognizability

## Core Idea
A language is recognizable (or recursively enumerable) if there exists a Turing machine that halts and accepts all strings in the language, but may loop indefinitely on strings outside the language. Not all recognizable languages are decidable; the halting problem is recognizable but not decidable.

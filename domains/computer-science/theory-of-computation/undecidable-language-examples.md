---
id: undecidable-language-examples
title: 'Undecidable Languages: Examples and Techniques'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: halting-problem
  type: hard
- id: diagonalization-and-uncomputability
  type: soft
builds-toward:
- reduction-techniques-undecidability
tags:
- undecidability
- halting
- tm-equivalence
- acceptance
- examples
stage: advanced
status: draft
---

# Undecidable Languages: Examples and Techniques

## Core Idea
Beyond the halting problem, many natural problems are undecidable: equivalence of TMs (do two TMs accept the same language?), universal language (does a TM accept all strings?), and emptiness variants. Some are recognizable (Turing-recognizable) but not decidable; others like the complement of halting are not recognizable. Recognizing undecidability requires more than diagonalization—typically reduction techniques.

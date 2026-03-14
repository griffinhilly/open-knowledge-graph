---
id: post-correspondence-problem
title: Post Correspondence Problem and Applications
domain: computer-science
course: theory-of-computation
prerequisites:
- id: reduction-techniques-undecidability
  type: hard
tags:
- pcp
- undecidability
- tiling
- string-matching
- canonical
stage: advanced
status: draft
---

# Post Correspondence Problem and Applications

## Core Idea
The Post Correspondence Problem (PCP) asks: given domino pairs (u₁, v₁), ..., (uₙ, vₙ) of strings, can you arrange them to form identical strings? PCP is undecidable without direct reference to TMs—undecidability arises from combinatorial structure. PCP reductions elegantly prove undecidability of grammar problems (CFG equivalence, ambiguity of unrestricted grammars).

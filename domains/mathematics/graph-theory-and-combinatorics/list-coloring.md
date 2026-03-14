---
id: list-coloring
title: List Coloring and the List Chromatic Number
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: edge-coloring-vizings-theorem
  type: soft
tags:
- list-coloring
- choosability
- advanced-coloring
stage: abstract-reasoning
status: draft
---

# List Coloring and the List Chromatic Number

## Core Idea
In list coloring, each vertex has a list of allowed colors, and a coloring must assign each vertex a color from its list. The list chromatic number (or choosability) ch(G) is the minimum list size guaranteeing a coloring exists for any assignment of lists. For many graphs, ch(G) > χ(G), surprising at first.

## How It's Best Learned
Construct adversarial list assignments showing when a small list size fails, demonstrating that ch(G) > χ(G) is possible. Verify the list chromatic number for small graphs.

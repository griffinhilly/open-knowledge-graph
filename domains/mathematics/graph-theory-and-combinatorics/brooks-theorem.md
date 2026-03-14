---
id: brooks-theorem
title: Brooks' Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: chromatic-number-bounds
  type: hard
tags:
- brooks-theorem
- chromatic-number
- tight-bounds
stage: abstract-reasoning
status: draft
---

# Brooks' Theorem

## Core Idea
Brooks' theorem refines the degree bound: for connected graphs that are neither complete nor odd cycles, χ(G) ≤ Δ(G). This is tight for many graph families and shows that the crude bound χ(G) ≤ Δ(G) + 1 can often be improved.

## How It's Best Learned
Find graphs where χ(G) = Δ(G) and others where χ(G) < Δ(G). Verify that complete graphs and odd cycles are the only exceptions.

## Common Misconceptions
- Forgetting the exceptions (complete graphs and odd cycles) when applying Brooks' theorem.
- Thinking the bound is always tight for every graph class.

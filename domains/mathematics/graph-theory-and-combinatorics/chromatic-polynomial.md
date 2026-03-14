---
id: chromatic-polynomial
title: Chromatic Polynomials and Deletion-Contraction
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-coloring
  type: hard
tags:
- graph-theory
- coloring
- polynomials
stage: abstract-reasoning
status: draft
---

# Chromatic Polynomials and Deletion-Contraction

## Core Idea
The chromatic polynomial P(G, k) counts the number of proper k-colorings of a graph G. It satisfies the deletion-contraction recurrence P(G, k) = P(G-e, k) - P(G/e, k), which recursively reduces to base cases. Chromatic polynomials encode structural information and can be analyzed algebraically to determine graph properties.

## How It's Best Learned
Compute chromatic polynomials for small graphs (paths, cycles, stars) by hand using deletion-contraction, verifying by direct enumeration.

## Common Misconceptions
The chromatic polynomial is NOT the same as the number of proper colorings for a fixed G; rather, it's a polynomial in k that gives the count for any number of colors k.

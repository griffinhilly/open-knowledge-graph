---
id: chromatic-polynomial-computation
title: Chromatic Polynomial and Counting Proper Colorings
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-coloring-chromatic
  type: hard
tags:
- graph-theory
- chromatic-polynomial
stage: formal-systems
status: draft
---

# Chromatic Polynomial and Counting Proper Colorings

## Core Idea
The chromatic polynomial P(G, k) counts the number of proper k-colorings of graph G. It can be computed using deletion-contraction: P(G,k) = P(G-e,k) - P(G/e,k), where G-e removes edge e and G/e contracts it. The chromatic number is the smallest k where P(G,k) > 0.

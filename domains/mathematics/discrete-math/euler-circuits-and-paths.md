---
id: euler-circuits-and-paths
title: Eulerian Circuits and Paths
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: graph-theory-intro
  type: hard
builds-toward:
- hamiltonian-circuits
tags:
- euler-circuit
- euler-path
- eulerian-graph
- konigsberg-bridges
stage: formal-systems
status: draft
---

# Eulerian Circuits and Paths

## Core Idea
An Eulerian circuit is a closed walk traversing every edge exactly once; an Eulerian path is an open walk doing the same. Euler's theorem (1736) states: a connected graph has an Eulerian circuit if and only if every vertex has even degree, and an Eulerian path (but not circuit) if and only if exactly two vertices have odd degree. The Königsberg bridge problem — can one cross all seven bridges without repeating any? — was Euler's original motivation and arguably the founding problem of graph theory.

## How It's Best Learned
Attempt Eulerian circuits on small graphs by hand before seeing the theorem. Verify Euler's condition on several examples. Connect to practical route-planning problems (mail delivery, snow plowing) where the goal is to traverse all edges with minimum repetition.

## Common Misconceptions
- Confusing Eulerian circuits (edges traversed once) with Hamiltonian circuits (vertices visited once) — these are fundamentally different problems with very different theories.
- Thinking even degree is sufficient without the connectivity requirement.

---
id: euler-paths-circuits
title: Eulerian Paths, Circuits, and Characterization
domain: mathematics
course: discrete-math
prerequisites:
- id: walks-paths-cycles
  type: hard
- id: degree-sequences-graphs
  type: soft
builds-toward:
- hamiltonian-paths-cycles
tags:
- graph-theory
- euler
stage: formal-systems
status: draft
---

# Eulerian Paths, Circuits, and Characterization

## Core Idea
An Eulerian path traverses every edge exactly once; an Eulerian circuit is a closed Eulerian path. A connected graph has an Eulerian circuit if and only if all vertices have even degree. It has an Eulerian path if and only if exactly 0 or 2 vertices have odd degree.

## How It's Best Learned
Draw small graphs and try to find Eulerian paths by hand. Check the degree condition before attempting.

## Common Misconceptions
- Confusing Eulerian paths with Hamiltonian paths (edges vs. vertices).
- Assuming all graphs have Eulerian paths.
- Misapplying the degree condition.

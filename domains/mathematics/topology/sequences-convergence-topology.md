---
id: sequences-convergence-topology
title: Convergence of Sequences in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: limit-points-and-accumulation
  type: hard
builds-toward:
- continuous-functions-topology
- first-countable-spaces
tags:
- sequences
- convergence
stage: formal-systems
status: draft
---

# Convergence of Sequences in Topological Spaces

## Core Idea
A sequence (xₙ) converges to x in a topological space if every open set containing x eventually contains all terms of the sequence—that is, for every open U containing x, there exists N such that xₙ ∈ U for all n ≥ N. This generalizes the ε-ball definition from metric spaces. Unlike metric spaces, limits in general topological spaces need not be unique; uniqueness requires the Hausdorff separation axiom. Furthermore, sequences alone may not suffice to characterize the topology—in non-first-countable spaces, nets or filters are needed to fully describe convergence behavior.

## How It's Best Learned
Compare convergence in a metric space with convergence in the cofinite topology on an infinite set, where sequences can converge to every point simultaneously. This dramatic contrast motivates why separation axioms matter.

## Common Misconceptions
Students often assume sequential convergence fully determines the topology. This holds in metric and first-countable spaces but fails in general. Also, a sequence can have multiple limits in non-Hausdorff spaces—this is a feature of the topology, not an error.


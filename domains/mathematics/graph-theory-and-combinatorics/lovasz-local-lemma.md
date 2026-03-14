---
id: lovasz-local-lemma
title: Lovász Local Lemma
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: probabilistic-method-graphs
  type: hard
tags:
- combinatorics
- probability
stage: abstract-reasoning
status: draft
---

# Lovász Local Lemma

## Core Idea
The Lovász Local Lemma is a powerful tool showing that if many 'bad events' have limited dependencies, then with positive probability none occur. If each event has probability at most p and affects at most d others, and ep(d+1) ≤ 1, then P(no bad event) > 0. This lemma resolves seemingly impossible combinatorial existence questions.

## How It's Best Learned
Apply the lemma to a concrete problem like showing existence of graphs with low discrepancy or high girth.

## Common Misconceptions
The condition ep(d+1) ≤ 1 is sufficient but not necessary; the actual threshold for positivity can be better. Also, 'd' counts neighbors in the dependency graph, not arbitrary other events.

---
id: topological-invariants-intro
title: Topological Invariants and Properties
domain: mathematics
course: topology
prerequisites:
- id: homeomorphisms-topological-equivalence
  type: hard
builds-toward:
- fundamental-group-definition
- connected-spaces
tags:
- invariants
- properties
stage: advanced
status: draft
---

# Topological Invariants and Properties

## Core Idea
A topological property is preserved under homeomorphisms. Compactness, connectedness, and separability are examples. Invariants help classify spaces up to homeomorphism.

## Explainer

A **topological invariant** is a property that is preserved by every homeomorphism — a property that, if it holds for X, must also hold for any space homeomorphic to X. From your study of homeomorphisms, you know that a homeomorphism is a continuous bijection with a continuous inverse: it is the topological notion of "same shape." Topological invariants are the fingerprints that let you prove two spaces are *not* homeomorphic without having to check every possible map between them.

The logic works by contrapositive. Suppose property P is a topological invariant, space X has property P, and space Y does not. Then X and Y cannot be homeomorphic — because if they were, the homeomorphism would carry P from X to Y, but Y lacks P. This is a powerful negative result: you never need to show that all possible maps fail; one invariant discrepancy is enough.

Concrete examples make this vivid. **Compactness** is a topological invariant: the closed interval [0, 1] is compact, but the real line ℝ is not, so they cannot be homeomorphic. **Connectedness** is a topological invariant: remove a single point from a circle and it remains connected; remove a single point from a line segment and it splits into two pieces — this "cut-point argument" proves a circle and a line segment are not homeomorphic. **The number of connected components** is also an invariant: a space with two components cannot be homeomorphic to a space with three.

The deeper structure behind invariants is that they assign the same algebraic or numerical object to every space in a homeomorphism class. Numbers like topological dimension, or algebraic structures like the fundamental group, are **stronger invariants** — they distinguish more spaces. Two spaces can share compactness and connectedness but differ in their fundamental group (a circle vs. a disk), and that algebraic invariant makes the distinction. Learning topology is, in large part, developing an arsenal of invariants with increasing discriminating power: each new invariant draws a finer partition across the universe of topological spaces.

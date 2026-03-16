---
id: cardinal-comparison-and-schroeder-bernstein
title: 'Comparing Cardinalities: The Schröder-Bernstein Theorem'
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: injections-surjections-and-inverse-functions
  type: hard
- id: uncountable-sets-and-the-reals
  type: soft
builds-toward:
- aleph-and-beth-hierarchy-introduction
- cardinal-arithmetic
tags:
- comparison
- order
- bijection
stage: formal-systems
status: draft
---

# Comparing Cardinalities: The Schröder-Bernstein Theorem

## Core Idea
The Schröder-Bernstein theorem states: if there exist injections f: A → B and g: B → A, then there exists a bijection between A and B. This makes cardinality a total order: for any two sets A and B, either |A| < |B|, |A| = |B|, or |A| > |B|. It avoids needing explicit bijections.

## Explainer

From your work on injections and bijections, you know that two sets have the same cardinality when there exists a bijection between them. But finding an explicit bijection can be surprisingly hard. The **Schröder-Bernstein theorem** (also called the Cantor-Schröder-Bernstein theorem) gives you a way around this: instead of one bijection, you provide two injections going in opposite directions, and the theorem guarantees a bijection must exist.

The theorem says: if f: A → B is an injection and g: B → A is an injection, then |A| = |B|. Intuitively, if A can fit inside B without collisions, and B can fit inside A without collisions, then they must be the same size. The proof constructs the bijection explicitly through a clever partitioning argument — elements are classified by whether their "ancestry chain" (repeatedly applying f and g backwards) terminates in A, terminates in B, or loops forever. This tri-partite structure lets you piece together a bijection from the two injections.

The theorem is most powerful when finding a direct bijection is difficult but finding two injections is easy. For example, proving |(0,1)| = |[0,1]| (the open and closed intervals have the same cardinality) directly is awkward because the endpoints of [0,1] have no obvious bijective image in (0,1). But injecting (0,1) → [0,1] is trivial (the identity works), and injecting [0,1] → (0,1) is easy (scale: x ↦ (x+1)/3 works). Two easy injections, and Schröder-Bernstein delivers the bijection.

This theorem establishes that **cardinal comparison** is a total order. We write |A| ≤ |B| if there exists an injection from A to B. Schröder-Bernstein shows this is antisymmetric: if |A| ≤ |B| and |B| ≤ |A|, then |A| = |B|. Combined with transitivity of injections, cardinality becomes a well-behaved ordering on sets. This is the foundation for comparing infinite cardinalities — the aleph hierarchy and cardinal arithmetic all build on this ordering, and Schröder-Bernstein is the essential tool that makes the ordering coherent.

---
id: zorns-lemma
title: Zorn's Lemma
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: axiom-of-choice
  type: hard
- id: partial-orders
  type: hard
builds-toward:
- cardinal-arithmetic
tags:
- Zorn's lemma
- maximal element
- chain
- axiom of choice
- equivalents
stage: formal-systems
status: draft
---

# Zorn's Lemma

## Core Idea
Zorn's lemma states: if (P, ≤) is a non-empty partially ordered set in which every chain (totally ordered subset) has an upper bound in P, then P has at least one maximal element. It is equivalent to the axiom of choice over ZF and to the well-ordering theorem. Zorn's lemma is the preferred formulation of choice in algebra and analysis: it directly produces maximal objects such as maximal ideals in rings, Hamel bases for vector spaces over arbitrary fields, and ultrafilters. Its power lies in converting the global choice principle into a local maximality argument that is easy to apply in specific algebraic or topological settings.

## How It's Best Learned
Memorize the precise statement: every chain has an upper bound (not necessarily a maximum), and the conclusion is a maximal element (not a maximum of P). Apply it to produce: (1) a maximal ideal in any non-trivial commutative ring, (2) a basis for any vector space, (3) a maximal consistent set of formulas. In each case, identify the poset P and verify chains have upper bounds.

## Common Misconceptions
- An upper bound for a chain need not be in the chain itself — it only needs to be in P and above all chain elements.
- Maximal does not mean maximum: a maximal element m satisfies 'm ≤ x implies m = x', but there may be incomparable maximal elements.
- Zorn's lemma does not assert that the maximal element is unique.

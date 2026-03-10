---
id: axiom-of-power-set
title: Axiom of Power Set
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: zfc-axioms-overview
  type: hard
- id: axiom-of-separation
  type: soft
builds-toward:
- cantor-theorem
- infinite-cardinal-numbers
tags:
- ZFC
- power set
- subsets
- uncountability
stage: formal-systems
status: draft
---

# Axiom of Power Set

## Core Idea
The power set axiom asserts that for every set A there exists a set P(A) whose elements are precisely the subsets of A. This axiom is responsible for the existence of uncountable sets: by Cantor's theorem, |P(A)| > |A| for every set A, so P(ℕ) is strictly larger than ℕ. Iterating the power set operation generates an unbounded hierarchy of ever-larger infinite sets, underlying the rich structure of Cantor's transfinite cardinals. The power set axiom is the most impredicative axiom in ZFC and is rejected in some constructive and predicative variants of set theory.

## How It's Best Learned
Enumerate all subsets of small finite sets (|A| = 0, 1, 2, 3) to confirm |P(A)| = 2^|A|. Then study why P(ℕ) corresponds to the set of real numbers via binary representations, connecting the power set axiom to the uncountability of ℝ. This bridge between the axiom and the existence of ℝ is one of ZFC's key payoffs.

## Common Misconceptions
- P(A) contains A itself (as A ⊆ A) and ∅ (as ∅ ⊆ A); do not confuse A ∈ P(A) with A ∈ A.
- The power set axiom asserts only that the collection of all subsets exists as a set; it does not describe what those subsets are.

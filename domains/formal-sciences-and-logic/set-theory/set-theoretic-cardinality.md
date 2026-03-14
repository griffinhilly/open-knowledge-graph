---
id: set-theoretic-cardinality
title: Set-Theoretic Cardinality
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: cantor-theorem
  type: hard
builds-toward:
- aleph-numbers
- descriptive-set-theory-intro
tags:
- cardinality
- countability
- bijection
- Hilbert's hotel
- diagonalization
- uncountability
- equinumerosity
stage: formal-systems
status: draft
---

# Set-Theoretic Cardinality

## Core Idea
Two sets A and B have the same cardinality (|A| = |B|) if and only if there exists a bijection between them — a function that is both injective and surjective. A set is countably infinite if it has the same cardinality as the natural numbers ℕ, and countable if it is either finite or countably infinite. Hilbert's hotel illustrates the surprising properties of countable infinity: the integers, rationals, and even ℕ × ℕ are all countable despite appearing 'larger' than ℕ. Cantor's diagonal argument then shatters the intuition that all infinite sets are the same size by proving that the reals (equivalently, P(ℕ)) are uncountable. Within ZFC, the Cantor-Bernstein-Schroeder theorem provides a powerful tool: if |A| ≤ |B| and |B| ≤ |A| (injections in both directions), then |A| = |B|.

## How It's Best Learned
Construct explicit bijections: ℕ → ℤ (dovetail positive and negative), ℕ → ℚ (Cantor's zigzag through a grid), ℕ → ℕ × ℕ (pairing function). Then work through the diagonal argument to prove [0,1] is uncountable. The contrast — building bijections for 'large-looking' countable sets, then failing for the reals — drives home what cardinality really measures. Finally, prove the Cantor-Bernstein theorem to see that cardinality comparison is well-behaved.

## Common Misconceptions
- 'Countable' does not mean 'listable in order' — the rationals are countable but cannot be listed in their natural order (which is dense, not well-ordered).
- The existence of a surjection from A onto B does not mean |A| = |B|; equality requires a bijection (or injections in both directions, by the Cantor-Bernstein theorem).

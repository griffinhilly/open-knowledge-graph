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

## Explainer

Cardinality is the rigorous answer to the question "how many elements does a set have?" For finite sets the answer seems obvious — count them. But counting is really just constructing a bijection to {1, 2, ..., n}. **Cardinality** generalizes this idea: two sets have the same cardinality if and only if there exists a **bijection** (a one-to-one correspondence) between them. This definition sidesteps the question "how many?" entirely and replaces it with the question "can they be paired up perfectly?"

The power of the definition becomes clear when you apply it to infinite sets. From your work with infinite cardinal numbers, you know that "infinity" is not a single thing. But the bijection criterion lets you compare infinite sets precisely. The integers ℤ seem much larger than the naturals ℕ — after all, ℤ includes all negative numbers too. Yet the function f(n) = (n/2 for even n, -(n+1)/2 for odd n) constructs a perfect pairing: 0↔0, 1↔−1, 2↔1, 3↔−2, ... This is **Hilbert's Hotel** made formal: a hotel with infinitely many rooms can always accommodate new guests by shifting everyone down. The takeaway is that countably infinite sets can absorb new elements or even finitely many copies of themselves without changing cardinality. The rationals are countable too — Cantor's zigzag argument through the grid ℕ × ℕ lists every positive fraction exactly once, showing |ℚ| = |ℕ|.

Then comes Cantor's diagonal argument, which you already know through Cantor's theorem. Applied to the real numbers, it shows that no matter how you try to list all real numbers in [0,1] — even infinitely — you can always construct a real number not on the list by differing from the nth entry in the nth decimal place. This proves the reals are **uncountable**: |ℝ| > |ℕ|. The rationals and reals both look like "lots of numbers," but they belong to fundamentally different size classes. There are multiple infinite cardinalities, forming a strict hierarchy.

The **Cantor-Bernstein-Schroeder theorem** is the tool that makes cardinality comparison practical. Rather than constructing an explicit bijection — which can be fiendishly difficult — you can establish |A| = |B| by finding an injection from A into B and a separate injection from B into A. The theorem guarantees these two one-way matchings can be woven into a two-way bijection, even though the proof is non-constructive. Think of it as the cardinality analogue of the squeeze theorem: bounding |A| ≤ |B| ≤ |A| pins down equality. This technique is indispensable for proving, for example, that |(0,1)| = |ℝ| by embedding each into the other.

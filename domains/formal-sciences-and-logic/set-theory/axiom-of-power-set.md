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
status: validated
---

# Axiom of Power Set

## Core Idea
The power set axiom asserts that for every set A there exists a set P(A) whose elements are precisely the subsets of A. This axiom is responsible for the existence of uncountable sets: by Cantor's theorem, |P(A)| > |A| for every set A, so P(ℕ) is strictly larger than ℕ. Iterating the power set operation generates an unbounded hierarchy of ever-larger infinite sets, underlying the rich structure of Cantor's transfinite cardinals. The power set axiom is the most impredicative axiom in ZFC and is rejected in some constructive and predicative variants of set theory.

## How It's Best Learned
Enumerate all subsets of small finite sets (|A| = 0, 1, 2, 3) to confirm |P(A)| = 2^|A|. Then study why P(ℕ) corresponds to the set of real numbers via binary representations, connecting the power set axiom to the uncountability of ℝ. This bridge between the axiom and the existence of ℝ is one of ZFC's key payoffs.

## Common Misconceptions
- P(A) contains A itself (as A ⊆ A) and ∅ (as ∅ ⊆ A); do not confuse A ∈ P(A) with A ∈ A.
- The power set axiom asserts only that the collection of all subsets exists as a set; it does not describe what those subsets are.

## Explainer

From your overview of ZFC axioms, you know that each axiom guarantees the existence of a particular kind of set. The axiom of separation (your soft prerequisite) lets you carve out a subset of an existing set by specifying a property. But separation alone cannot *generate* genuinely new sets — it only gives you pieces of sets you already have. The **power set axiom** is categorically different: for any set A, it asserts the existence of the set P(A) of *all* subsets of A. This is a vast act of collection, and for infinite sets, it is what makes the real numbers constructible from the natural numbers.

For finite sets, the count is familiar: if |A| = n, then |P(A)| = 2^n. This grows quickly — P(∅) = {∅} has 1 element, P({a}) = {∅, {a}} has 2, P({a,b}) has 4, P({a,b,c}) has 8. Each element of A either is or is not included in a given subset, giving a binary choice per element and 2^n total combinations. The axiom guarantees that this collection — all 2^n subsets — coexists as a single set, not merely as a class or a concept. The axiom of separation then lets you pick out specific subsets by properties, but the power set axiom is what ensures all subsets are available simultaneously.

The jump to **infinite** sets is where the power set axiom becomes decisive. By **Cantor's theorem**, there is no surjection from A onto P(A) — the diagonal argument shows that any proposed surjection misses at least one subset. Applied to ℕ: P(ℕ) is strictly larger than ℕ. Since ℕ is infinite (countably so), P(ℕ) is **uncountable** — a different, larger kind of infinity. More concretely, each subset S ⊆ ℕ corresponds to an infinite binary sequence (the indicator function of S), and infinite binary sequences biject with real numbers via binary expansion. So the power set axiom, applied to ℕ, delivers the existence of a set the same size as ℝ.

**Iterating** the power set operation generates an unbounded hierarchy of cardinals: ℵ₀ = |ℕ|, then 2^{ℵ₀} = |P(ℕ)| = |ℝ|, then 2^{2^{ℵ₀}} = |P(ℝ)|, and so on. These are the **beth numbers** ℶ₀, ℶ₁, ℶ₂, …, each strictly larger than the last. This is why the power set axiom is called **impredicative**: P(A) quantifies over all subsets of A, including subsets that may themselves be defined using P(A). Constructive and predicative set theories reject this axiom because accepting it requires "collecting together" objects whose definition is circular in this sense. In ZFC, the axiom is accepted unconditionally, and the resulting set-theoretic universe — containing uncountably many infinities at every level — is the standard foundation for modern mathematics.

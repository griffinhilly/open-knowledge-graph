---
id: cantor-theorem
title: Cantor's Theorem
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: axiom-of-power-set
  type: soft
- id: cantor-diagonalization
  type: soft
- id: cardinality-and-countability
  type: soft
builds-toward:
- continuum-hypothesis
- cofinality-and-regular-cardinals
tags:
- Cantor's theorem
- power set
- cardinality
- diagonal argument
- uncountability
stage: formal-systems
status: validated
---

# Cantor's Theorem

## Core Idea
Cantor's theorem states that for any set A, the power set P(A) has strictly greater cardinality than A: there is an injection A → P(A) but no surjection. The proof is a diagonal argument: given any function f: A → P(A), the set D = {x ∈ A : x ∉ f(x)} lies in P(A) but is not in the range of f. Applied to ℕ, this shows P(ℕ) is uncountable; applied to any infinite cardinal κ, it shows 2^κ > κ, generating an unbounded tower of infinities. Consequently, there is no largest cardinal — the cardinal numbers form a proper class.

## How It's Best Learned
Prove the theorem first for A = ℕ (Cantor's diagonal argument for the reals). Then abstract the proof to an arbitrary set A. Work through the tower P(ℕ), P(P(ℕ)), P(P(P(ℕ))), ... and verify that each step strictly increases cardinality. Confirm that the diagonal set D is well-defined and always escapes any given f.

## Common Misconceptions
- Cantor's theorem applies to ALL sets, including finite ones: |P(∅)| = 1 > 0 and |P({a})| = 2 > 1.
- The theorem shows no surjection A → P(A) exists, but there is always an injection x ↦ {x} from A into P(A).

## Explainer

You have studied cardinality and countability, and you know that two sets have the same cardinality when there is a bijection between them. Cantor's theorem is the most powerful result in this territory: for any set A whatsoever, the **power set** P(A) — the set of all subsets of A — is strictly larger than A. There is an injection A → P(A) (send each element x to its singleton {x}), but no surjection. Since cardinality comparison requires a bijection, and no bijection can exist when there's no surjection, we get |A| < |P(A)|.

The proof is the diagonal argument you studied for Cantor's diagonalization. Suppose for contradiction that f: A → P(A) is a surjection. Then every subset of A is in the range of f. Construct the set D = {x ∈ A : x ∉ f(x)} — the set of all elements of A that are *not* members of the subset assigned to them by f. D is a perfectly well-defined subset of A. Since f is a surjection, D = f(d) for some d ∈ A. Now ask: is d ∈ D? If d ∈ D, then by the definition of D, d ∉ f(d) = D — contradiction. If d ∉ D, then d ∉ f(d), so by the definition of D, d ∈ D — contradiction. Either way, we reach an impossibility. Therefore no surjection f: A → P(A) can exist.

The consequences are sweeping. Applied to A = ℕ, the theorem gives |P(ℕ)| > |ℕ|: the power set of the natural numbers is uncountable. (In fact, P(ℕ) has the same cardinality as the reals ℝ, both equal to 2^ℵ₀.) Applied to any infinite cardinal κ, it gives 2^κ > κ: the power of the power set always exceeds the original. This generates an unbounded tower of infinities: ℵ₀ < 2^ℵ₀ < 2^(2^ℵ₀) < ···, none of which can be the largest cardinal, since we can always take another power set. The cardinals form a proper class — there is no set containing all of them.

This connects directly to the **continuum hypothesis** question that builds from this theorem: is there a cardinal strictly between ℵ₀ and 2^ℵ₀? Cantor's theorem tells you 2^ℵ₀ > ℵ₀, but does not tell you how much bigger it is. That question turns out to be independent of ZFC — neither provable nor disprovable — a fact that took nearly a century after Cantor's proof to establish. The diagonal argument itself becomes a versatile proof technique: the same structure appears in the proof that the reals are uncountable, in Russell's paradox, in Gödel's incompleteness proof, and in the proof that the halting problem is undecidable. Learning to recognize the diagonal structure across these contexts is one of the deepest payoffs of studying Cantor's theorem.

---
id: cardinality-and-countability-methods-of-proof
title: Cardinality and Countability
domain: mathematics
course: methods-of-proof
prerequisites:
- id: injective-surjective-bijective
  type: hard
tags:
- cardinality
- infinity
- countability
stage: formal-systems
status: draft
---

# Cardinality and Countability

## Core Idea
Cardinality measures set size via bijections: two sets have equal cardinality if a bijection exists between them. A set is countable if it has the same cardinality as ℕ. This enables precise reasoning about infinite sets.

## Explainer

You have already studied injections, surjections, and bijections as tools for comparing sets by pairing their elements. **Cardinality** lifts this idea to a definition of "size": two sets have the same cardinality if and only if a bijection exists between them. For finite sets this agrees with ordinary counting — a bijection from a 5-element set to a 3-element set cannot exist, and that impossibility is exactly what "5 ≠ 3" means. The power of the definition is that it extends unchanged to infinite sets, generating a rich and surprising theory.

A set is **countably infinite** if a bijection exists between it and the natural numbers ℕ. This might seem to describe only ℕ itself, but many larger-looking sets turn out countable too. The integers ℤ are countable: list them as 0, 1, −1, 2, −2, 3, −3, ..., which is an explicit bijection with ℕ. The rationals ℚ are countable via Cantor's diagonal-grid argument: arrange all fractions p/q in a grid indexed by numerator and denominator, then trace a zigzag path through the grid — every rational appears, so the path defines a surjection from ℕ onto ℚ, implying countability. More generally, a countable union of countable sets is countable, so countability is surprisingly hard to escape once you have it.

Yet not all infinite sets are countable. The real numbers ℝ are **uncountable** — their cardinality, denoted **c**, is strictly greater than ℵ₀ (the cardinality of ℕ). Cantor's diagonal proof demonstrates this directly. Suppose you claim to have a list r₁, r₂, r₃, ... covering every real in [0, 1]. Construct a new number by taking the nth decimal digit of rₙ and changing it. This new number differs from every rₙ in at least one position, so it cannot appear on the list — contradicting completeness. Any list misses a real; therefore no bijection between ℕ and ℝ exists. Notice that the proof is constructive: it shows you exactly how to find the missing element given any purported bijection.

The argument generalizes: the **power set** P(A) always has strictly greater cardinality than A, for any set A. This means there is no "largest" infinity — there is an unending hierarchy ℵ₀ < c < P(c) < .... In proof work, cardinality arguments appear in two modes. Constructively, you exhibit a bijection to establish equality of size (e.g., show that an odd natural number corresponds bijectively to every natural number). By contradiction, you assume a bijection exists and derive a diagonalization contradiction to prove no such bijection can exist — as with ℝ. Recognizing which mode applies is a core skill in reasoning about infinite sets.

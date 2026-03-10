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
status: draft
---

# Cantor's Theorem

## Core Idea
Cantor's theorem states that for any set A, the power set P(A) has strictly greater cardinality than A: there is an injection A → P(A) but no surjection. The proof is a diagonal argument: given any function f: A → P(A), the set D = {x ∈ A : x ∉ f(x)} lies in P(A) but is not in the range of f. Applied to ℕ, this shows P(ℕ) is uncountable; applied to any infinite cardinal κ, it shows 2^κ > κ, generating an unbounded tower of infinities. Consequently, there is no largest cardinal — the cardinal numbers form a proper class.

## How It's Best Learned
Prove the theorem first for A = ℕ (Cantor's diagonal argument for the reals). Then abstract the proof to an arbitrary set A. Work through the tower P(ℕ), P(P(ℕ)), P(P(P(ℕ))), ... and verify that each step strictly increases cardinality. Confirm that the diagonal set D is well-defined and always escapes any given f.

## Common Misconceptions
- Cantor's theorem applies to ALL sets, including finite ones: |P(∅)| = 1 > 0 and |P({a})| = 2 > 1.
- The theorem shows no surjection A → P(A) exists, but there is always an injection x ↦ {x} from A into P(A).

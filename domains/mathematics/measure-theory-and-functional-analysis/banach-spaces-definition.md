---
id: banach-spaces-definition
title: 'Banach Spaces: Definition and Examples'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: normed-vector-spaces
  type: hard
- id: cauchy-sequences-completeness
  type: hard
builds-toward:
- bounded-linear-operators
- open-mapping-theorem
- closed-graph-theorem
- uniform-boundedness-principle
tags:
- banach-spaces
- functional-analysis
stage: abstract-reasoning
status: draft
---

# Banach Spaces: Definition and Examples

## Core Idea
A Banach space is a complete normed vector space: every Cauchy sequence converges. Completeness is essential for existence proofs and the fundamental theorems of functional analysis. Examples include L^p, c₀, and ℓ^∞.

## Explainer

You already know that a normed vector space gives you a notion of distance: d(u, v) = ‖u − v‖. But having a distance doesn't guarantee that limits of sequences actually land inside the space. The rational numbers Q form a metric space under |·|, yet the sequence 1, 1.4, 1.41, 1.414, ... is Cauchy in Q — the terms get arbitrarily close — yet it converges to √2, which is irrational. Q has gaps. A **Banach space** is a normed vector space without gaps.

The precise condition: a space is **complete** if every **Cauchy sequence** converges to a limit inside the space. Recall that a Cauchy sequence is one where the elements eventually crowd together — for any ε > 0, there exists N such that ‖xₘ − xₙ‖ < ε for all m, n > N. Convergence of a sequence implies Cauchy (the elements crowd around the limit), but in an incomplete space the converse fails. Banach spaces are complete: every sequence that *looks like* it should converge actually does, and the limit is a member of the space.

The canonical examples are worth knowing concretely. The space **ℓ²** of square-summable sequences — sequences (a₁, a₂, ...) with Σaₙ² < ∞ — is a Banach space under ‖a‖₂ = (Σaₙ²)^(1/2). So is **ℓ^p** for any p ≥ 1, and **ℓ^∞** (bounded sequences under the sup-norm). The space **L^p(μ)** of p-th power integrable functions is Banach — this is the Riesz-Fischer theorem. For contrast: C[0,1] with the L² norm is *not* complete. One can construct a Cauchy sequence of continuous functions whose pointwise limit is discontinuous, meaning the limit escapes the space.

Completeness is not a technical nicety — it is the enabling hypothesis for the major theorems of functional analysis. The Open Mapping Theorem, the Closed Graph Theorem, and the Uniform Boundedness Principle all require Banach spaces as their setting. Each theorem is fundamentally a limit argument: it asserts that certain limit points exist or that certain operators are bounded. Without completeness guaranteeing that limits stay in the space, these arguments would collapse. Banach spaces are the stage on which functional analysis performs.

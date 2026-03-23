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
stage: expert
status: draft
---

# Banach Spaces: Definition and Examples

## Core Idea
A Banach space is a complete normed vector space: every Cauchy sequence converges. Completeness is essential for existence proofs and the fundamental theorems of functional analysis. Examples include L^p, c₀, and ℓ^∞.

## Questions

```yaml
- question: "The space C[0,1] of continuous functions on [0,1] equipped with the L² norm ‖f‖₂ = (∫₀¹|f(x)|² dx)^(1/2). Is this a Banach space?"
  type: multiple-choice
  options:
    - "Yes — C[0,1] is closed under addition and scalar multiplication, so it must be complete"
    - "No — one can construct a Cauchy sequence of continuous functions whose L²-limit is discontinuous, escaping C[0,1]"
    - "Yes — the L² norm guarantees completeness on any closed interval"
    - "No — C[0,1] with the sup-norm is Banach, so it cannot also be Banach under L²"
  answer: 1
  explanation: "C[0,1] with the L² norm is NOT a Banach space. You can construct a Cauchy sequence of continuous functions (e.g., piecewise linear 'ramp' functions converging to a step function) whose L²-limit is discontinuous. The limit exists in L²([0,1]) but not in C[0,1], so the Cauchy sequence has no limit inside the space. L²([0,1]) — the completion of C[0,1] under L² — is Banach (the Riesz-Fischer theorem), but C[0,1] with L² norm is only a normed space, not a Banach space."

- question: "Which of the following correctly states what it means for a normed space to be complete?"
  type: multiple-choice
  options:
    - "Every bounded sequence has a convergent subsequence"
    - "Every Cauchy sequence converges to an element within the space"
    - "Every absolutely convergent series converges"
    - "Every linear operator on the space is bounded"
  answer: 1
  explanation: "A normed space is complete (a Banach space) if every Cauchy sequence — a sequence where the terms become arbitrarily close together — converges to a limit that lies within the space itself. The key word is 'within': the limit must be a member of the space, not just exist in some larger space. Options A and C are related results (compactness and absolute convergence in Banach spaces) but are not the definition. Option D (bounded linear operators) is a property studied in Banach space theory, not the definition of completeness."

- question: "Every normed vector space is a Banach space."
  type: true-false
  answer: false
  explanation: "A normed vector space gives you a notion of distance but does not guarantee that Cauchy sequences converge within the space. The rationals ℚ under |·| form a normed space in which the sequence 1, 1.4, 1.41, 1.414, ... is Cauchy but converges to √2 ∉ ℚ — an 'escape' from the space. Similarly, C[0,1] with the L² norm is a normed space that is not complete. Banach spaces are the complete normed spaces — the special subset where limits stay inside."

- question: "In a Banach space, every Cauchy sequence converges to an element that belongs to the space."
  type: true-false
  answer: true
  explanation: "This is precisely the definition of completeness: Cauchy-ness (terms get arbitrarily close) implies convergence (there is a limit), and the limit belongs to the space. In an incomplete normed space, Cauchy sequences can 'try to converge' to a limit that doesn't exist in the space — there is a gap. Banach spaces are gap-free. This is not a theorem to be proved from other properties; it is the definition of what a Banach space is."

- question: "Why does functional analysis require Banach spaces as its setting, rather than arbitrary normed vector spaces?"
  type: short-answer
  answer: "The major theorems of functional analysis — the Open Mapping Theorem, Closed Graph Theorem, Uniform Boundedness Principle — all involve taking limits: proving that certain sequences of operators or functions converge. Without completeness, those limits might not exist in the space, making the arguments invalid. Completeness is the hypothesis that guarantees limit points stay in the space, enabling existence proofs and allowing limit arguments to be completed."
  explanation: "A concrete example: the Uniform Boundedness Principle says that a family of bounded linear operators that is pointwise bounded must be uniformly bounded. The proof uses the Baire Category Theorem, which requires completeness. On an incomplete space, the same family could be pointwise bounded but unbounded — the principle fails. Every major theorem in functional analysis either assumes Banach spaces explicitly or implicitly uses completeness somewhere in its proof."
```

## Explainer

You already know that a normed vector space gives you a notion of distance: d(u, v) = ‖u − v‖. But having a distance doesn't guarantee that limits of sequences actually land inside the space. The rational numbers Q form a metric space under |·|, yet the sequence 1, 1.4, 1.41, 1.414, ... is Cauchy in Q — the terms get arbitrarily close — yet it converges to √2, which is irrational. Q has gaps. A **Banach space** is a normed vector space without gaps.

The precise condition: a space is **complete** if every **Cauchy sequence** converges to a limit inside the space. Recall that a Cauchy sequence is one where the elements eventually crowd together — for any ε > 0, there exists N such that ‖xₘ − xₙ‖ < ε for all m, n > N. Convergence of a sequence implies Cauchy (the elements crowd around the limit), but in an incomplete space the converse fails. Banach spaces are complete: every sequence that *looks like* it should converge actually does, and the limit is a member of the space.

The canonical examples are worth knowing concretely. The space **ℓ²** of square-summable sequences — sequences (a₁, a₂, ...) with Σaₙ² < ∞ — is a Banach space under ‖a‖₂ = (Σaₙ²)^(1/2). So is **ℓ^p** for any p ≥ 1, and **ℓ^∞** (bounded sequences under the sup-norm). The space **L^p(μ)** of p-th power integrable functions is Banach — this is the Riesz-Fischer theorem. For contrast: C[0,1] with the L² norm is *not* complete. One can construct a Cauchy sequence of continuous functions whose pointwise limit is discontinuous, meaning the limit escapes the space.

Completeness is not a technical nicety — it is the enabling hypothesis for the major theorems of functional analysis. The Open Mapping Theorem, the Closed Graph Theorem, and the Uniform Boundedness Principle all require Banach spaces as their setting. Each theorem is fundamentally a limit argument: it asserts that certain limit points exist or that certain operators are bounded. Without completeness guaranteeing that limits stay in the space, these arguments would collapse. Banach spaces are the stage on which functional analysis performs.

---
id: reflexive-spaces
title: Reflexive Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: weak-convergence
  type: hard
tags:
- duality
stage: expert
status: validated
---

# Reflexive Spaces

## Core Idea
A Banach space X is reflexive if the natural embedding X → X** is surjective. Reflexive spaces have the Bolzano-Weierstrass property: every bounded sequence has a weakly convergent subsequence.

## Questions

```yaml
- question: "A Banach space X has the property that X and X** are isometrically isomorphic as Banach spaces. Does this make X reflexive?"
  type: multiple-choice
  options:
    - "Yes — isometric isomorphism between X and X** is exactly what reflexivity means"
    - "No — reflexivity requires the natural embedding J: X → X** to be surjective, not just any isomorphism"
    - "Yes — any isomorphism between X and X** implies the natural embedding is surjective"
    - "Not necessarily — reflexivity also requires the unit ball to be strongly compact"
  answer: 1
  explanation: "This is the central subtlety of reflexivity. There exist Banach spaces that are isomorphic to their double duals via some abstract isomorphism yet are not reflexive — the natural embedding J(x)(f) = f(x) is not surjective. James's space is a famous example. Reflexivity is defined by the natural embedding specifically, because that canonical map is what connects the algebraic structure to the weak compactness properties. An arbitrary isomorphism provides no such guarantee."

- question: "You want to prove that a certain functional attains its minimum value on a closed convex subset of a Banach space. Which property of the space is most directly needed to extract a convergent subsequence from a minimizing sequence?"
  type: multiple-choice
  options:
    - "Completeness of the space — every Cauchy sequence converges"
    - "Reflexivity — every bounded sequence has a weakly convergent subsequence"
    - "Separability — the space has a countable dense subset"
    - "The space being a Hilbert space — so the inner product norm is available"
  answer: 1
  explanation: "Reflexivity provides the key compactness: in a reflexive Banach space, every bounded sequence has a weakly convergent subsequence (the infinite-dimensional Bolzano-Weierstrass theorem). A minimizing sequence is bounded (energies are decreasing toward the infimum), so reflexivity extracts a weak limit. Then weak lower semicontinuity of the functional finishes the proof. Completeness alone does not give weakly convergent subsequences; separability is useful but not the key; Hilbert spaces work because they are reflexive, not because of the inner product per se."

- question: "A Banach space is reflexive if and mainly if X is isomorphic to X** as abstract Banach spaces."
  type: true-false
  answer: false
  explanation: "False. Reflexivity requires isomorphism via the *natural* embedding J(x)(f) = f(x), not via any isomorphism. A space can be abstractly isomorphic to its double dual without being reflexive — this is the content of the James counterexample. The natural embedding is canonical precisely because it connects the algebraic duality structure to geometric properties like weak compactness."

- question: "In a reflexive Banach space, the closed unit ball is compact in the weak topology."
  type: true-false
  answer: true
  explanation: "True. This is actually an equivalent characterization of reflexivity (via the Kakutani theorem): X is reflexive if and only if its closed unit ball is weakly compact. Weak compactness is the precise infinite-dimensional replacement for finite-dimensional sequential compactness. It explains why every bounded sequence in a reflexive space has a weakly convergent subsequence — sequential weak compactness follows from weak compactness in a separable space, and the general result follows by other means."

- question: "Why does it matter that the natural embedding J: X → X** is used in the definition of reflexivity, rather than the existence of any isomorphism between X and X**?"
  type: short-answer
  answer: "The natural embedding J is canonical — it captures the specific way X sits inside X** as a space of evaluation functionals. It is this embedding that connects reflexivity to weak compactness and to the duality theory of Lᵖ spaces. A non-canonical isomorphism between X and X** would not guarantee that bounded sequences have weakly convergent subsequences or that the unit ball is weakly compact. The existence of some abstract isomorphism tells you only that X and X** have the same cardinality of a Hamel basis; the natural embedding tells you something structural about how evaluation interacts with the double-dual."
  explanation: "The pathological example is instructive: James's space J is isomorphic to its double dual J** via some map, but the natural embedding has codimension 1 — it misses exactly one dimension — so it is not surjective, and J is not reflexive. This shows that abstract isomorphism and canonical isomorphism via J are genuinely different conditions, and it is the canonical one that has the analytic consequences."
```

## Explainer

From your study of weak convergence, you know that a sequence (xₙ) in a Banach space X converges weakly to x if f(xₙ) → f(x) for every bounded linear functional f ∈ X*. The **dual space** X* consists of all bounded linear functionals on X. Now consider the dual of the dual: X** = (X*)* consists of all bounded linear functionals on X*. There is a natural map J: X → X** defined by J(x)(f) = f(x) — it sends each element x ∈ X to the functional on X* that evaluates at x. This map J is always an isometric embedding (it preserves norms and is injective), so X sits inside X** in a canonical way. A Banach space X is called **reflexive** when J is also surjective — meaning X and X** are not merely isomorphic in some abstract sense, but isomorphic via this specific natural map.

The significance of reflexivity is best understood through what it buys you: the **Banach-Alaoglu-style compactness**. In a finite-dimensional space, every bounded sequence has a convergent subsequence (Bolzano-Weierstrass). In infinite dimensions, strong convergence of bounded sequences fails — the sequence of standard basis vectors in ℓ² is bounded but has no strongly convergent subsequence. But in a reflexive space, every bounded sequence has a **weakly convergent** subsequence. This is the correct infinite-dimensional analogue of Bolzano-Weierstrass, and it is the workhorse of existence proofs throughout functional analysis and PDE theory.

The canonical examples clarify the concept. The spaces Lᵖ(μ) for 1 < p < ∞ are reflexive, with dual Lᵍ where 1/p + 1/q = 1. The spaces L¹ and L∞ are not reflexive: (L¹)* = L∞ but (L∞)* is strictly larger than L¹. Hilbert spaces are reflexive (by the Riesz representation theorem, H* ≅ H, so H** ≅ H). Every finite-dimensional Banach space is reflexive trivially.

Reflexivity matters in optimization: to prove a functional attains its minimum on a closed convex set, you extract a minimizing sequence, use reflexivity to find a weakly convergent subsequence, and appeal to the weak lower semicontinuity of the functional. Without reflexivity, that subsequence might not exist. The condition is also tied to geometry — a Banach space is reflexive if and only if its closed unit ball is compact in the weak topology, making the connection between the algebraic structure (the double-dual map) and the topological structure (weak compactness) precise.

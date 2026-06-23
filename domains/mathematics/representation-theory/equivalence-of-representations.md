---
id: equivalence-of-representations
title: Equivalence of Representations
domain: mathematics
course: representation-theory
prerequisites:
- id: group-representations
  type: hard
- id: linear-transformations
  type: hard
- id: matrix-representations
  type: hard
builds-toward:
- reducibility-and-irreducibility
- character-theory
tags:
- equivalence
- intertwining-operator
- isomorphism
stage: expert
status: validated
---

# Equivalence of Representations

## Core Idea
Two representations ρ: G → GL(V) and σ: G → GL(W) are equivalent (isomorphic) if there exists an invertible linear map T: V → W that intertwines the two actions: T∘ρ(g) = σ(g)∘T for all g ∈ G. In matrix terms, this means ρ and σ differ by a change of basis. Equivalence is the right notion of "sameness" for representations — it preserves all structural properties while ignoring coordinate artifacts.

## Questions

```yaml
- question: "An intertwining operator T between representations ρ and σ satisfies Tρ(g) = σ(g)T for all g ∈ G. If T is also invertible, then ρ and σ are equivalent. What happens if T is not invertible?"
  type: multiple-choice
  options:
    - "T cannot exist unless it is invertible"
    - "T is still called an intertwining operator (or G-map), but it establishes a morphism rather than an isomorphism between the representations"
    - "The relation Tρ(g) = σ(g)T cannot hold for a singular T"
    - "T defines an equivalence only between subrepresentations"
  answer: 1
  explanation: "A linear map T: V → W satisfying Tρ(g) = σ(g)T for all g is an intertwining operator (or G-homomorphism) regardless of invertibility. Such maps form the vector space Hom_G(V, W). If T is invertible, it establishes an isomorphism (equivalence); if not, its kernel and image are subrepresentations — a fact that plays a key role in Schur's lemma and the general structure theory."

- question: "If two representations of G have different dimensions, they cannot be equivalent."
  type: true-false
  answer: true
  explanation: "Equivalence requires an invertible linear map T: V → W, which can only exist when dim(V) = dim(W). This is immediate from linear algebra: an invertible linear map is a bijection, and finite-dimensional spaces of different dimensions cannot be in bijection. So dimension is the crudest invariant of a representation — equivalent representations must have the same degree."

- question: "Explain why two representations could have the same dimension and the same character (trace function) yet still fail to be equivalent over ℝ, while being equivalent over ℂ."
  type: short-answer
  answer: "Over ℂ, representations are determined up to equivalence by their characters (for finite groups), so same character implies equivalence. Over ℝ, this can fail because the intertwining matrix P may require complex entries. The real representations may be inequivalent because the necessary change-of-basis matrix does not exist within GL_n(ℝ)."
  explanation: "This subtlety arises because algebraic closure matters. For example, two real representations might become equivalent after extending scalars to ℂ — each matrix can be conjugated to the same form over ℂ, but no real matrix achieves the conjugation. This is why representation theory over ℂ (where the field is algebraically closed) is cleaner than over ℝ."

- question: "The set of all intertwining operators from ρ to σ forms a vector space."
  type: true-false
  answer: true
  explanation: "If T₁ and T₂ both satisfy Tᵢρ(g) = σ(g)Tᵢ for all g, then (αT₁ + βT₂)ρ(g) = ασ(g)T₁ + βσ(g)T₂ = σ(g)(αT₁ + βT₂). So linear combinations of intertwining operators are intertwining operators. This space Hom_G(V, W) is a subspace of Hom(V, W), and its dimension carries important structural information — Schur's lemma tells us this dimension is 0 or 1 when both representations are irreducible."
```

## Explainer

In any mathematical theory, once you define objects, the next essential step is to define when two objects are "the same." For representations, the right notion is **equivalence** (also called isomorphism). Two representations ρ: G → GL(V) and σ: G → GL(W) are equivalent if there exists an invertible linear map T: V → W such that T∘ρ(g) = σ(g)∘T for all g ∈ G. The map T is called an **intertwining isomorphism** or a **G-isomorphism**.

The intertwining condition T∘ρ(g) = σ(g)∘T says that it does not matter whether you first apply the G-action and then translate via T, or first translate via T and then apply the G-action. In matrix terms, if ρ and σ are both n-dimensional, the condition becomes Tρ(g) = σ(g)T, or equivalently σ(g) = Tρ(g)T⁻¹ for all g — which is exactly conjugation by T. So equivalent matrix representations are related by a single change of basis applied uniformly to all group elements.

Why does this definition matter? Because many superficially different-looking representations are secretly the same. The rotation group SO(2) acting on ℝ² in the standard basis gives the familiar rotation matrices. In an eigenvector basis (over ℂ), the same action becomes diagonal. These look different as matrices but carry identical structural information — they are equivalent representations. The goal of representation theory is to classify representations up to equivalence, stripping away coordinate noise to reveal the underlying structure.

The intertwining operators that are not necessarily invertible also play a crucial role. The set Hom_G(V, W) of all G-equivariant linear maps from V to W forms a vector space, and its dimension measures how "similar" two representations are. Schur's lemma, which you will encounter soon, shows that when V and W carry irreducible representations, this space is either zero-dimensional (the representations are inequivalent) or one-dimensional (they are equivalent). This is the beginning of a systematic classification program.

---
id: maschkes-theorem
title: Maschke's Theorem
domain: mathematics
course: representation-theory
prerequisites:
- id: reducibility-and-irreducibility
  type: hard
- id: inner-product-spaces
  type: soft
builds-toward:
- character-theory
- artin-wedderburn-theorem
tags:
- maschke
- complete-reducibility
- semisimple
- averaging
stage: expert
status: validated
---

# Maschke's Theorem

## Core Idea
Maschke's theorem guarantees that every representation of a finite group G over a field whose characteristic does not divide |G| is completely reducible — it decomposes as a direct sum of irreducible subrepresentations. The proof works by averaging an arbitrary inner product over the group to produce a G-invariant one, then taking orthogonal complements. This theorem is the foundation that makes the entire decomposition theory of finite group representations possible.

## Questions

```yaml
- question: "Maschke's theorem fails when the characteristic of the field divides |G|. Give a concrete example."
  type: short-answer
  answer: "Take G = ℤ/pℤ over the field 𝔽_p. The representation ρ(1) = [[1, 1], [0, 1]] has the invariant subspace span{e₁}, but no G-invariant complement exists — the representation is reducible but not completely reducible."
  explanation: "The matrix [[1,1],[0,1]] has order p in GL₂(𝔽_p), giving a valid representation of ℤ/pℤ. The subspace span{e₁} is invariant (fixed by ρ(1)), but any candidate complement must contain a vector with nonzero second component, and applying ρ(1) shifts it by e₁, pushing it outside the complement. The averaging trick fails because dividing by |G| = p is impossible in characteristic p."

- question: "The key step in the proof of Maschke's theorem involves 'averaging' a projection over the group. What does this averaging accomplish?"
  type: multiple-choice
  options:
    - "It makes the projection have norm 1"
    - "It turns an arbitrary linear projection onto an invariant subspace into a G-equivariant projection, whose kernel is then also G-invariant"
    - "It diagonalizes every group element simultaneously"
    - "It constructs the irreducible decomposition directly"
  answer: 1
  explanation: "Given a G-invariant subspace W ⊆ V, pick any linear projection π: V → W. Define π̃ = (1/|G|) Σ_{g∈G} ρ(g)∘π∘ρ(g)⁻¹. This averaged projection is G-equivariant: ρ(h)π̃ = π̃ρ(h). Its kernel ker(π̃) is therefore G-invariant and provides the required complement V = W ⊕ ker(π̃). The averaging uses the group's finiteness (to sum) and the characteristic condition (to divide by |G|)."

- question: "Maschke's theorem applies to all representations of all groups."
  type: true-false
  answer: false
  explanation: "Maschke's theorem has two crucial hypotheses: the group must be finite, and the characteristic of the field must not divide the group's order. It fails for infinite groups in general (though unitary representations of compact groups satisfy an analogue via Haar measure). It also fails in modular representation theory, where char(F) divides |G| — this is a rich and much harder subject."

- question: "Maschke's theorem implies that every representation of S₃ over ℂ is a direct sum of irreducible representations. How many non-isomorphic irreducible representations does S₃ have?"
  type: multiple-choice
  options:
    - "2"
    - "3"
    - "4"
    - "6"
  answer: 1
  explanation: "The number of non-isomorphic irreducible representations of a finite group over ℂ equals the number of conjugacy classes. S₃ has three conjugacy classes: {e}, {(12),(13),(23)}, {(123),(132)}. So it has three irreducible representations: the trivial (degree 1), the sign (degree 1), and the standard (degree 2). Their degrees satisfy 1² + 1² + 2² = 6 = |S₃|, confirming the dimension formula."
```

## Explainer

Maschke's theorem answers the most important structural question in finite group representation theory: can every representation be broken into irreducible pieces? The answer is **yes**, provided the field's characteristic does not divide the group order. Over ℂ (or ℚ, or ℝ), this condition is always satisfied for finite groups, so every complex representation of a finite group is completely reducible.

The proof uses an averaging trick that is characteristic of the subject. Suppose W ⊆ V is a G-invariant subspace. We want to find a G-invariant complement U with V = W ⊕ U. Start with any linear projection π: V → W (this exists by linear algebra, without any G-equivariance). Now average over the group: define π̃(v) = (1/|G|) Σ_{g∈G} ρ(g) π(ρ(g)⁻¹ v). One checks that π̃ is still a projection onto W, and crucially, π̃ commutes with the G-action. The kernel of π̃ is therefore a G-invariant complement to W. The division by |G| is where the characteristic hypothesis enters — in characteristic p dividing |G|, this division is undefined, and the theorem genuinely fails.

The consequence is that every finite-dimensional representation over ℂ can be written as V ≅ V₁^{⊕n₁} ⊕ V₂^{⊕n₂} ⊕ ··· ⊕ Vₖ^{⊕nₖ}, where V₁, …, Vₖ are pairwise non-isomorphic irreducible representations and the multiplicities n₁, …, nₖ are uniquely determined. This is the representation-theoretic analogue of unique prime factorization. The classification problem for all representations thus reduces to: (1) find all irreducible representations, and (2) determine the multiplicities when a given representation is decomposed. Character theory, built on Schur's lemma and Maschke's theorem, solves both problems.

When the characteristic does divide |G|, we enter **modular representation theory**, where complete reducibility fails and indecomposable representations need not be irreducible. This is a deeper and more difficult subject, pioneered by Richard Brauer, that requires fundamentally different techniques. Maschke's theorem thus marks the boundary between the "nice" semisimple world and the "wild" modular world.

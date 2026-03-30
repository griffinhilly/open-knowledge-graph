---
id: frobenius-reciprocity
title: Frobenius Reciprocity
domain: mathematics
course: representation-theory
prerequisites:
- id: induced-representations
  type: hard
- id: orthogonality-relations
  type: soft
builds-toward:
- representations-of-symmetric-groups
tags:
- frobenius-reciprocity
- adjunction
- induction
- restriction
stage: expert
status: validated
---

# Frobenius Reciprocity

## Core Idea
Frobenius reciprocity states that for a subgroup H ≤ G, induction and restriction are adjoint functors: ⟨Ind_H^G(σ), ρ⟩_G = ⟨σ, Res_H^G(ρ)⟩_H for any representation σ of H and ρ of G. Equivalently, Hom_G(Ind_H^G(σ), ρ) ≅ Hom_H(σ, Res_H^G(ρ)). This fundamental adjunction links the representation theories of a group and its subgroups, providing a powerful tool for computing multiplicities without explicitly constructing induced representations.

## Questions

```yaml
- question: "Using Frobenius reciprocity, how can you determine the multiplicity of an irreducible representation ρ of G in Ind_H^G(σ) without computing the induced representation explicitly?"
  type: short-answer
  answer: "The multiplicity of ρ in Ind_H^G(σ) is ⟨Ind_H^G(σ), ρ⟩_G = ⟨σ, Res_H^G(ρ)⟩_H. So you restrict ρ to H (which is straightforward — just evaluate the character at elements of H) and take the inner product with σ in H's character theory."
  explanation: "This is enormously practical. Computing the induced representation directly requires building a [G:H]·dim(σ)-dimensional space and working out the action. Frobenius reciprocity replaces this with a computation entirely within H, which is smaller. This is the primary method for decomposing induced representations in practice."

- question: "Frobenius reciprocity shows that induction from the trivial subgroup {e} gives which representation?"
  type: multiple-choice
  options:
    - "The trivial representation"
    - "The sign representation"
    - "The regular representation"
    - "An irreducible representation of maximum dimension"
  answer: 2
  explanation: "The trivial subgroup has only one representation: the one-dimensional trivial representation. Inducing it to G gives a [G:{e}]-dimensional = |G|-dimensional representation. This is exactly the regular representation, which acts by left multiplication on ℂ[G]. Frobenius reciprocity confirms: the multiplicity of any irreducible ρ in Ind_{e}^G(1) is ⟨1, Res_{e}^G(ρ)⟩_{e} = dim(ρ), matching the known decomposition of the regular representation."

- question: "Frobenius reciprocity is an isomorphism of vector spaces Hom_G(Ind σ, ρ) ≅ Hom_H(σ, Res ρ). This is an example of an adjunction in category theory."
  type: true-false
  answer: true
  explanation: "Induction is the left adjoint of restriction in the category of group representations. This means Hom_G(Ind_H^G(σ), ρ) ≅ Hom_H(σ, Res_H^G(ρ)) naturally in both σ and ρ. This categorical perspective generalizes to other contexts: compact groups (with Haar measure), Lie algebras, and algebraic groups all have analogous induction-restriction adjunctions."

- question: "If every irreducible representation of G appears in Ind_H^G(σ) for a single representation σ of H, what does this imply about the restriction Res_H^G to H?"
  type: short-answer
  answer: "By Frobenius reciprocity, every irreducible ρ of G appearing in Ind_H^G(σ) means ⟨σ, Res_H^G(ρ)⟩_H ≥ 1 for all ρ. So σ appears as a constituent of Res_H^G(ρ) for every irreducible ρ of G — the representation σ is 'seen' by every irreducible when restricted to H."
  explanation: "This duality between induction and restriction is Frobenius reciprocity at work. Information flows both ways: understanding how representations of G restrict to H is equivalent to understanding how representations of H induce to G. Neither direction is more fundamental — they are two sides of the same coin."
```

## Explainer

Frobenius reciprocity connects two fundamental operations in representation theory: **induction** (building representations of G from those of a subgroup H) and **restriction** (obtaining representations of H by forgetting part of the G-structure). The theorem states a precise numerical relationship: the multiplicity of an irreducible G-representation ρ in the induced representation Ind_H^G(σ) equals the multiplicity of an irreducible H-representation σ in the restricted representation Res_H^G(ρ). In inner product notation: ⟨Ind_H^G(σ), ρ⟩_G = ⟨σ, Res_H^G(ρ)⟩_H.

The proof at the character level is a direct computation. The left side is (1/|G|) Σ_{g∈G} χ_{Ind}(g) conjugate(χ_ρ(g)). Substituting the induction formula for χ_{Ind} and rearranging the sums (using the fact that summing x⁻¹gx over all x ∈ G and all g covers all elements of H with the correct multiplicity) yields (1/|H|) Σ_{h∈H} χ_σ(h) conjugate(χ_ρ(h)), which is exactly ⟨σ, Res_H^G(ρ)⟩_H.

The practical power of Frobenius reciprocity is that it replaces a computation in G (decomposing a potentially large induced representation) with a computation in H (decomposing a restriction). Since H is smaller, this is usually far easier. For example, to find the irreducible constituents of a representation induced from a cyclic subgroup, you only need to know how the irreducibles of G look when restricted to that cyclic subgroup — and representations of cyclic groups are completely understood (they are all one-dimensional over ℂ).

In modern algebra, Frobenius reciprocity is recognized as a special case of an **adjunction** between functors. The induction functor Ind_H^G is left adjoint to the restriction functor Res_H^G. This categorical perspective has been enormously fruitful: it generalizes to compact groups (where induction uses integration against Haar measure), Lie algebras (parabolic induction), and algebraic geometry (push-forward and pull-back of sheaves). The same structural relationship appears throughout mathematics, with Frobenius's original group-theoretic version as the prototype.

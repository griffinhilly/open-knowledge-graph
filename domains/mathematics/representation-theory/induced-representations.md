---
id: induced-representations
title: Induced Representations
domain: mathematics
course: representation-theory
prerequisites:
- id: character-theory
  type: hard
- id: normal-subgroups
  type: soft
- id: permutation-representations
  type: soft
builds-toward:
- frobenius-reciprocity
tags:
- induced-representation
- induction
- restriction
- frobenius
stage: expert
status: validated
---

# Induced Representations

## Core Idea
Given a subgroup H ≤ G and a representation σ of H, the induced representation Ind_H^G(σ) is a representation of G constructed by "extending" σ from H to all of G. It acts on a space of dimension [G:H]·dim(σ), built by taking one copy of σ for each coset of H in G. Induction is the primary method for constructing representations of a group from representations of its subgroups, and its character can be computed by an explicit formula.

## Questions

```yaml
- question: "If H has index 3 in G and σ is a 2-dimensional representation of H, what is the dimension of Ind_H^G(σ)?"
  type: multiple-choice
  options:
    - "2"
    - "3"
    - "5"
    - "6"
  answer: 3
  explanation: "dim(Ind_H^G(σ)) = [G:H] · dim(σ) = 3 · 2 = 6. The induced representation is built from [G:H] copies of the representation space, one for each left coset of H in G. Each copy is 'rotated' into the others by elements of G not in H, creating a larger space on which G acts."

- question: "The character of an induced representation Ind_H^G(σ) is given by the formula χ^G(g) = (1/|H|) Σ_{x∈G, x⁻¹gx∈H} χ_σ(x⁻¹gx). Why does the sum only include x with x⁻¹gx ∈ H?"
  type: short-answer
  answer: "The character formula involves extending χ_σ to all of G by setting it to zero outside H. The term χ_σ(x⁻¹gx) is only nonzero when x⁻¹gx ∈ H, so only those terms contribute. Geometrically, we are summing over the coset representatives x that conjugate g back into H, where σ can 'see' the element."
  explanation: "This formula shows that induction depends on how the conjugacy classes of G intersect H. If g is conjugate to no element of H, the induced character is zero at g. The formula can also be written as a sum over coset representatives, making the coset structure of G/H explicit."

- question: "Restriction and induction are inverse operations: inducing and then restricting always returns the original representation."
  type: true-false
  answer: false
  explanation: "Restriction and induction are adjoint functors (this is Frobenius reciprocity), not inverse operations. Res_H^G(Ind_H^G(σ)) is generally much larger than σ — it contains σ as a summand but also contains other components arising from how the cosets interact with H. The precise relationship is given by Mackey's formula."

- question: "Inducing the trivial representation of H to G gives a representation whose character counts what?"
  type: multiple-choice
  options:
    - "The number of elements in each conjugacy class"
    - "The number of fixed points of g acting on G/H (the coset space)"
    - "The order of the centralizer of each element"
    - "The number of subgroups conjugate to H"
  answer: 1
  explanation: "The induced character from the trivial representation of H is χ(g) = |{xH ∈ G/H : gxH = xH}|, which counts the number of cosets fixed by g. This is the permutation character of the action of G on G/H. When H = {e}, this gives the regular representation. When H is larger, it gives the representation associated to the natural action of G on the coset space."
```

## Explainer

**Induction** is the process of building a representation of a group G from a representation of a subgroup H. Given a representation σ: H → GL(W), we construct the **induced representation** Ind_H^G(σ) on a larger space. Choose left coset representatives g₁, …, g_m for H in G (where m = [G:H]). The induced space is V = g₁W ⊕ g₂W ⊕ ··· ⊕ g_mW, a direct sum of m copies of W. An element g ∈ G acts by permuting these copies (since g maps one coset to another) and applying elements of H within each copy.

More formally, V = ℂ[G] ⊗_{ℂ[H]} W, where the tensor product is over the group algebra of H. The G-action is g · (x ⊗ w) = (gx) ⊗ w. This construction is basis-independent and functorial. The dimension is [G:H] · dim(W), which makes sense: you need one copy of W for each coset.

The character of the induced representation has an explicit formula: χ_{Ind}(g) = (1/|H|) Σ_{x∈G} χ̃_σ(x⁻¹gx), where χ̃_σ extends χ_σ by zero outside H. Equivalently, summing over coset representatives: χ_{Ind}(g) = Σᵢ χ̃_σ(gᵢ⁻¹g gᵢ). Only conjugates of g that land in H contribute. This formula is computable and connects the induced character to the conjugacy class structure of G relative to H.

Induction has a natural partner: **restriction**. Given a representation ρ of G, restricting it to H (just forgetting the G-action on elements outside H) gives Res_H^G(ρ). These two operations are adjoint in a precise sense captured by Frobenius reciprocity: ⟨Ind_H^G(σ), ρ⟩_G = ⟨σ, Res_H^G(ρ)⟩_H. This adjunction is one of the most powerful tools in representation theory, relating the representation theories of a group and its subgroups. Many important representations — including the irreducible representations of symmetric groups — are most naturally constructed via induction from carefully chosen subgroups.

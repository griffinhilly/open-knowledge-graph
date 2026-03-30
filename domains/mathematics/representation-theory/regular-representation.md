---
id: regular-representation
title: Regular Representation
domain: mathematics
course: representation-theory
prerequisites:
- id: character-theory
  type: hard
- id: group-actions
  type: soft
builds-toward:
- artin-wedderburn-theorem
tags:
- regular-representation
- left-regular
- group-algebra
stage: expert
status: validated
---

# Regular Representation

## Core Idea
The (left) regular representation of a finite group G acts on the vector space ℂ[G] with basis {eᵍ : g ∈ G} by left multiplication: ρ(g)(eₕ) = e_{gh}. It has dimension |G| and contains every irreducible representation Vᵢ with multiplicity equal to dim(Vᵢ). The regular representation is the "universal" representation from which all others can be extracted, and its decomposition yields the fundamental formula |G| = Σ dᵢ².

## Questions

```yaml
- question: "What is the character of the regular representation evaluated at a non-identity element g ≠ e?"
  type: multiple-choice
  options:
    - "|G|"
    - "1"
    - "0"
    - "−1"
  answer: 2
  explanation: "For g ≠ e, left multiplication by g sends every basis vector eₕ to e_{gh} ≠ eₕ (since gh ≠ h when g ≠ e). So the permutation matrix for ρ(g) has all zeros on the diagonal, giving tr(ρ(g)) = 0. At the identity, ρ(e) = I_{|G|}, so χ_reg(e) = |G|. This character — |G| at e and 0 elsewhere — encodes the fact that the regular representation contains each irreducible dᵢ times."

- question: "The regular representation of any nontrivial group is irreducible."
  type: true-false
  answer: false
  explanation: "The regular representation has dimension |G| and always decomposes into irreducible summands. For example, the trivial representation (the span of Σ eᵍ) is always a one-dimensional subrepresentation. By Maschke's theorem (over ℂ), the regular representation decomposes as ⊕ᵢ Vᵢ^{dᵢ}, where the sum runs over all irreducible representations and dᵢ = dim(Vᵢ). Only for the trivial group G = {e} is the regular representation irreducible."

- question: "The formula |G| = Σᵢ dᵢ² (sum of squares of irreducible dimensions) follows from which property of the regular representation?"
  type: short-answer
  answer: "The regular representation has dimension |G|, and it decomposes as ⊕ᵢ Vᵢ^{dᵢ} where each irreducible Vᵢ appears with multiplicity dᵢ = dim(Vᵢ). So |G| = dim(ℂ[G]) = Σᵢ dᵢ · dim(Vᵢ) = Σᵢ dᵢ²."
  explanation: "The multiplicity of Vᵢ in the regular representation can be computed via characters: nᵢ = ⟨χ_reg, χᵢ⟩ = (1/|G|)·|G|·χᵢ(e) = dᵢ, since χ_reg is zero off the identity. So each irreducible appears exactly dim(Vᵢ) times, and the dimension count gives the sum-of-squares formula."
```

## Explainer

The **regular representation** is constructed from the group itself. Form a vector space ℂ[G] with one basis vector eᵍ for each element g ∈ G, so dim(ℂ[G]) = |G|. Define the left action of G by ρ(g)(eₕ) = e_{gh} — each group element permutes the basis vectors by left multiplication. This is always a faithful representation (distinct group elements give distinct permutations), and it carries maximal information about the group's structure.

The character of the regular representation has a striking form: χ_reg(e) = |G| and χ_reg(g) = 0 for all g ≠ e. The identity fixes every basis vector (trace = |G|), while any non-identity element moves every basis vector (no diagonal entries, trace = 0). Using this character to compute multiplicities: nᵢ = ⟨χ_reg, χᵢ⟩ = (1/|G|) Σ_{g∈G} χ_reg(g) conjugate(χᵢ(g)) = (1/|G|) · |G| · χᵢ(e) = dᵢ. Each irreducible representation Vᵢ appears with multiplicity exactly equal to its dimension.

This decomposition ℂ[G] ≅ ⊕ᵢ Vᵢ^{⊕dᵢ} has profound consequences. Comparing dimensions: |G| = Σ dᵢ². This sum-of-squares formula is one of the most basic constraints in finite group representation theory — it limits which sets of dimensions can arise as irreducible degrees. For example, a group of order 12 might have irreducibles of dimensions 1, 1, 1, 3 (since 1+1+1+9 = 12) or 1, 1, 1, 1, 2, 2 (since 1+1+1+1+4+4 = 12), but never 1, 1, 1, 1, 1, 1, 1, 5 (since 5² = 25 > 12).

The regular representation also reveals the connection between representation theory and the **group algebra** ℂ[G]. The group algebra is ℂ[G] with multiplication defined by extending the group multiplication linearly: (Σ aᵍeᵍ)(Σ bₕeₕ) = Σ aᵍbₕe_{gh}. The decomposition ℂ[G] ≅ ⊕ Mₐᵢ(ℂ) (as an algebra, by the Artin-Wedderburn theorem) connects the representation theory of G to the structure theory of semisimple algebras.

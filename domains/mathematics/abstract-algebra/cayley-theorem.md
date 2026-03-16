---
id: cayley-theorem
title: Cayley's Theorem
domain: mathematics
course: abstract-algebra
prerequisites:
- id: permutation-groups
  type: hard
- id: group-isomorphisms
  type: soft
tags:
- cayley
- embedding
- permutation-representation
stage: advanced
status: draft
---

# Cayley's Theorem

## Core Idea
Every group G is isomorphic to a subgroup of some symmetric group Sₙ. The left-multiplication action of G on itself embeds G into Sₙ where n = |G|. This shows that abstract group theory is equivalent to the concrete theory of permutation groups.

## Explainer

The permutation groups you studied earlier — the symmetric groups Sₙ of all bijections on an n-element set — are in some sense the "universal" groups. Cayley's theorem makes this precise: no matter how abstract your group may seem (matrices, rotations, symmetries of a polygon), it secretly *acts* as a group of permutations of some set. The proof is surprisingly concrete and uses only tools you already have.

The key construction is to let the group act on *itself* by left multiplication. For any fixed g ∈ G, define the function λ_g : G → G by λ_g(x) = gx. Because every element of G has an inverse (g⁻¹), multiplying by g is a bijection — the function is its own inverse when composed with λ_{g⁻¹}. So λ_g is a **permutation** of the set G, meaning λ_g ∈ Sym(G). The map Φ : G → Sym(G) defined by Φ(g) = λ_g is the **left-regular representation** of G.

This map Φ is a group homomorphism: λ_{gh}(x) = ghx = λ_g(λ_h(x)), so Φ(gh) = Φ(g) ∘ Φ(h). It is also injective: if λ_g = λ_h, then gx = hx for all x ∈ G; setting x = e gives g = h. An injective homomorphism is an embedding, so the image Φ(G) = {λ_g : g ∈ G} is a subgroup of Sym(G) that is isomorphic to G. Since |G| = n implies Sym(G) ≅ Sₙ, the theorem follows.

The practical power of Cayley's theorem is that it reduces proofs about abstract groups to proofs about permutation groups, which have rich combinatorial and geometric structure. For example, any property that holds for all subgroups of all symmetric groups holds for all groups. One subtlety worth noting: the embedding sends G into S_{|G|}, which can be far larger than necessary — the cyclic group ℤ₃ of order 3 embeds into S₃ of order 6, not into a group of order 3. More efficient representations (using coset spaces rather than the whole group) are possible, but the left-regular construction guarantees an embedding exists for *every* group, which is the theorem's core claim.

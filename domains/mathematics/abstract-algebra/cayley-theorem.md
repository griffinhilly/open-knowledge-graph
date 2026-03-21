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

## Questions

```yaml
- question: "In the proof of Cayley's theorem, why is the map λ_g : G → G defined by λ_g(x) = gx a bijection (permutation of G)?"
  type: multiple-choice
  options:
    - "Because G is finite, any function from G to G with no repeated outputs is automatically bijective"
    - "Because multiplying by g is reversible via multiplication by g⁻¹, which exists by the group axiom of inverses, making λ_g a permutation of G"
    - "Because left-multiplication maps are linear, and all linear maps on finite sets are bijections"
    - "Because g and x commute in every group, making λ_g its own inverse"
  answer: 1
  explanation: "The bijectivity of λ_g is the first key step in the proof. λ_{g⁻¹} is the inverse function of λ_g: composing them gives λ_{g⁻¹}(λ_g(x)) = g⁻¹(gx) = (g⁻¹g)x = ex = x. So λ_g ∘ λ_{g⁻¹} = identity. This works in every group because every element has an inverse — a group axiom. Option A is false (finiteness alone doesn't guarantee bijectivity for functions between sets of equal size, though injectivity does imply bijectivity for finite sets). Option C is false (left-multiplication is not a linear map in the vector space sense). Option D is false — Cayley's theorem applies to non-abelian groups where elements don't commute."

- question: "A student claims that Cayley's theorem shows every group 'is' a symmetric group. What is the correct statement of the theorem?"
  type: multiple-choice
  options:
    - "The student is right — every group is isomorphic to the full symmetric group Sₙ for some n"
    - "Every group is isomorphic to a subgroup of some symmetric group — it embeds into Sₙ, but need not fill the entire group"
    - "Every group is isomorphic to S_{|G|}, the symmetric group on exactly |G| elements"
    - "Every group contains a copy of some symmetric group as a normal subgroup"
  answer: 1
  explanation: "The theorem says G embeds into Sym(G) ≅ S_{|G|} — meaning G is isomorphic to a *subgroup* of S_{|G|}, not to S_{|G|} itself. ℤ₃ has order 3, but S₃ has order 6; the image of the left-regular representation is a proper subgroup of S₃ of order 3. The distinction matters: Cayley's theorem guarantees an embedding exists, not that G equals the whole symmetric group. Option C conflates the group into which G embeds (S_{|G|}) with G itself. The claim 'every group is isomorphic to a subgroup of some symmetric group' is both precise and powerful."

- question: "Cayley's theorem guarantees that every group has the most efficient possible embedding into a symmetric group, with no 'wasted' elements."
  type: true-false
  answer: false
  explanation: "The left-regular representation embeds a group G of order n into S_{n} — a symmetric group of order n!, which can be vastly larger than G. ℤ₃ (order 3) embeds into S₃ (order 6) via the left-regular representation, even though a cyclic group of order 3 could in principle be represented more compactly. More efficient representations exist: if G acts on a coset space G/H for some subgroup H, the resulting permutation representation embeds G into S_{[G:H]}, which may be much smaller. The theorem's value is existence, not efficiency: it guarantees an embedding for *every* group, making no assumptions about structure."

- question: "Since every group G is isomorphic to a subgroup of some symmetric group by Cayley's theorem, any theorem that holds for all subgroups of all symmetric groups also holds for all groups."
  type: true-false
  answer: true
  explanation: "This is one of the main applications of Cayley's theorem. Isomorphism preserves all group-theoretic properties, so if G ≅ H and a property holds of H, it holds of G. Since every group embeds into a symmetric group, properties that hold universally for subgroups of symmetric groups hold universally for all groups. This lets us reduce abstract group theory to the concrete, combinatorially rich theory of permutation groups — which have geometric, visual, and computational structure that abstract groups lack."

- question: "Explain why the map Φ : G → Sym(G) defined by Φ(g) = λ_g is injective, and why injectivity is essential for Cayley's theorem."
  type: short-answer
  answer: "Φ is injective because if Φ(g) = Φ(h) — meaning λ_g = λ_h as permutations of G — then gx = hx for every x ∈ G. Setting x = e (the identity element) gives g = h. So distinct elements of G produce distinct permutations. Injectivity is essential because Cayley's theorem claims G is *isomorphic* to a subgroup of Sym(G). Isomorphism requires a bijection between G and its image in Sym(G). If Φ were not injective, distinct elements of G would map to the same permutation, and G would not embed faithfully — the image of G in Sym(G) would be a strictly smaller group, not a copy of G. Injectivity is precisely what makes the image Φ(G) ⊆ Sym(G) an isomorphic copy of G."
  explanation: "The proof structure is clean and worth memorizing: λ_g is a bijection (uses inverses), Φ is a homomorphism (uses associativity), Φ is injective (uses the identity element). Three group axioms, three key steps. Together they establish that G embeds as a group of permutations — abstract groups and permutation groups are the same mathematical universe."
```

## Explainer

The permutation groups you studied earlier — the symmetric groups Sₙ of all bijections on an n-element set — are in some sense the "universal" groups. Cayley's theorem makes this precise: no matter how abstract your group may seem (matrices, rotations, symmetries of a polygon), it secretly *acts* as a group of permutations of some set. The proof is surprisingly concrete and uses only tools you already have.

The key construction is to let the group act on *itself* by left multiplication. For any fixed g ∈ G, define the function λ_g : G → G by λ_g(x) = gx. Because every element of G has an inverse (g⁻¹), multiplying by g is a bijection — the function is its own inverse when composed with λ_{g⁻¹}. So λ_g is a **permutation** of the set G, meaning λ_g ∈ Sym(G). The map Φ : G → Sym(G) defined by Φ(g) = λ_g is the **left-regular representation** of G.

This map Φ is a group homomorphism: λ_{gh}(x) = ghx = λ_g(λ_h(x)), so Φ(gh) = Φ(g) ∘ Φ(h). It is also injective: if λ_g = λ_h, then gx = hx for all x ∈ G; setting x = e gives g = h. An injective homomorphism is an embedding, so the image Φ(G) = {λ_g : g ∈ G} is a subgroup of Sym(G) that is isomorphic to G. Since |G| = n implies Sym(G) ≅ Sₙ, the theorem follows.

The practical power of Cayley's theorem is that it reduces proofs about abstract groups to proofs about permutation groups, which have rich combinatorial and geometric structure. For example, any property that holds for all subgroups of all symmetric groups holds for all groups. One subtlety worth noting: the embedding sends G into S_{|G|}, which can be far larger than necessary — the cyclic group ℤ₃ of order 3 embeds into S₃ of order 6, not into a group of order 3. More efficient representations (using coset spaces rather than the whole group) are possible, but the left-regular construction guarantees an embedding exists for *every* group, which is the theorem's core claim.

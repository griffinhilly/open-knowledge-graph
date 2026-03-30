---
id: ca-exact-sequences
title: Exact Sequences of Modules
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-modules-over-rings
  type: hard
- id: ring-homomorphisms
  type: hard
builds-toward:
- ca-flat-modules
- ca-projective-modules
- ca-injective-modules
- ca-koszul-complex
tags:
- exact-sequence
- short-exact-sequence
- kernel
- cokernel
- split
stage: expert
status: validated
---

# Exact Sequences of Modules

## Core Idea
A sequence of module homomorphisms ··· → Mᵢ₋₁ →^{fᵢ₋₁} Mᵢ →^{fᵢ} Mᵢ₊₁ → ··· is exact at Mᵢ if the image of fᵢ₋₁ equals the kernel of fᵢ. A short exact sequence 0 → A → B → C → 0 encodes the idea that B is "built from" A and C, with A embedded as a submodule and C isomorphic to the quotient B/A. Exact sequences are the primary language for expressing structural relationships between modules.

## Questions

```yaml
- question: "Given a short exact sequence 0 → A →^f B →^g C → 0 of R-modules, which of the following must be true?"
  type: multiple-choice
  options:
    - "B ≅ A ⊕ C as R-modules"
    - "f is injective and g is surjective"
    - "A is isomorphic to C"
    - "B is a free module"
  answer: 1
  explanation: "Exactness at A (with 0 → A) means ker(f) = im(0 → A) = 0, so f is injective. Exactness at C (with C → 0) means im(g) = ker(C → 0) = C, so g is surjective. Exactness at B means im(f) = ker(g). The sequence does NOT imply B ≅ A ⊕ C — that holds only when the sequence splits. For example, 0 → ℤ →^{×2} ℤ → ℤ/2ℤ → 0 does not split: ℤ is not isomorphic to ℤ ⊕ ℤ/2ℤ."

- question: "The sequence 0 → 2ℤ → ℤ → ℤ/2ℤ → 0 is a short exact sequence of ℤ-modules. Does it split?"
  type: multiple-choice
  options:
    - "Yes — there is a ℤ-module homomorphism ℤ/2ℤ → ℤ that is a section of the quotient map"
    - "No — any ℤ-module homomorphism ℤ/2ℤ → ℤ must be zero, since ℤ is torsion-free, so no section exists"
    - "Yes — because ℤ is a PID, all short exact sequences of ℤ-modules split"
    - "No — because 2ℤ ≅ ℤ is free, the sequence must split by the splitting lemma"
  answer: 1
  explanation: "A splitting would require a homomorphism s: ℤ/2ℤ → ℤ with the projection composed with s being the identity on ℤ/2ℤ. But any homomorphism from ℤ/2ℤ to ℤ maps the generator 1̄ to some n ∈ ℤ satisfying 2n = 0, hence n = 0. So the only homomorphism is the zero map, which is not a section. The sequence does not split: ℤ ≇ 2ℤ ⊕ ℤ/2ℤ = ℤ ⊕ ℤ/2ℤ."

- question: "If 0 → A → B → C → 0 is a short exact sequence and C is a free module, then the sequence splits."
  type: true-false
  answer: true
  explanation: "If C is free with basis {cᵢ}, choose any preimage bᵢ ∈ B of each cᵢ under the surjection g: B → C. The map s: C → B defined by s(cᵢ) = bᵢ (extended linearly) is a section: g ∘ s = id_C. So the sequence splits, and B ≅ A ⊕ C. This is why free modules have the 'projective' property — maps to them can always be lifted. The previous example showed that when C = ℤ/2ℤ (not free), splitting can fail."

- question: "Every short exact sequence of vector spaces over a field splits."
  type: true-false
  answer: true
  explanation: "Over a field, every module (vector space) is free — it has a basis. By the previous result, if C is free then 0 → A → B → C → 0 splits. Since every vector space is free, every short exact sequence of vector spaces splits, and B ≅ A ⊕ C. This is equivalent to the rank-nullity theorem: dim(B) = dim(A) + dim(C). The failure of splitting over general rings is what makes module theory richer and harder than linear algebra."

- question: "Explain the relationship between exact sequences and the isomorphism theorems from abstract algebra."
  type: short-answer
  answer: "The first isomorphism theorem says that for a homomorphism f: M → N, we have M/ker(f) ≅ im(f). This is encoded by the exact sequence 0 → ker(f) → M → im(f) → 0. More generally, a short exact sequence 0 → A →^f B →^g C → 0 says f is injective (A ≅ im(f) = ker(g)) and C ≅ B/im(f) ≅ B/A. So exact sequences package the isomorphism theorems into a compact, composable notation that generalizes to longer sequences and functorial constructions."
  explanation: "The power of exact sequences over raw isomorphism theorems is composability. You can splice exact sequences together, apply functors to them (localization, tensor product, Hom), and track how exactness is preserved or broken. When a functor fails to preserve exactness, the 'defect' is measured by derived functors — Ext and Tor — which form the basis of homological algebra."
```

## Explainer

In linear algebra, the rank-nullity theorem says that for a linear map T: V → W, dim(V) = dim(ker T) + dim(im T). This is a statement about the exact sequence 0 → ker(T) → V → im(T) → 0. **Exact sequences** generalize this framework to modules over arbitrary rings, where dimension is unavailable and the structural relationships between modules are more subtle.

A sequence of R-module homomorphisms ··· → Mᵢ₋₁ →^{fᵢ₋₁} Mᵢ →^{fᵢ} Mᵢ₊₁ → ··· is **exact at Mᵢ** if im(fᵢ₋₁) = ker(fᵢ): the image of the incoming map is exactly the kernel of the outgoing map. The most important case is the **short exact sequence** 0 → A →^f B →^g C → 0. Exactness at A says ker(f) = 0, so f is injective. Exactness at C says im(g) = C, so g is surjective. Exactness at B says im(f) = ker(g), so A embeds into B and C ≅ B/f(A). In short: B is an extension of C by A.

A short exact sequence 0 → A → B → C → 0 **splits** if B ≅ A ⊕ C via maps compatible with f and g. This happens if and only if there exists a **section** s: C → B with g ∘ s = id_C, or equivalently, a **retraction** r: B → A with r ∘ f = id_A. Over a field, every short exact sequence splits (because every vector space is free), so the theory of extensions is trivial. Over general rings, non-split extensions are ubiquitous — the sequence 0 → ℤ →^{×2} ℤ → ℤ/2ℤ → 0 does not split — and classifying extensions is a central problem solved by the Ext functor.

Exact sequences are not just notation — they are the primary computational tool of homological algebra. Given a functor F (like localization, tensor product, or Hom), you apply it to an exact sequence and ask whether exactness is preserved. **Left exact** functors (like Hom(−, N)) preserve exactness on the left; **right exact** functors (like − ⊗ N) preserve it on the right. The failure of full exactness is measured by **derived functors**: Ext measures the failure of Hom's exactness, and Tor measures the failure of tensor product's exactness. This machinery is the engine of modern commutative algebra and algebraic geometry.

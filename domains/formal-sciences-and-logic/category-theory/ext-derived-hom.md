---
id: ext-derived-hom
title: Ext Functors as Derived Hom
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: exact-sequences
  type: hard
- id: injective-objects
  type: hard
builds-toward:
- derived-functors
- homology-and-cohomology
tags:
- derived-functors
- homological-algebra
- extensions
stage: advanced
status: draft
---

# Ext Functors as Derived Hom

## Core Idea
The Ext functor Ext^n(A, B) is the n-th right derived functor of Hom(A, −), computed via an injective resolution of B. Ext^1(A, B) classifies extensions of A by B, while higher Ext groups measure obstructions to splitting. Ext is fundamental to extension theory and provides invariants for classifying objects in abelian categories.

## Questions

```yaml
- question: "What does it mean when Ext¹(A, B) = 0 for two modules A and B?"
  type: multiple-choice
  options:
    - "There are no short exact sequences involving A and B"
    - "The only short exact sequence 0 → B → E → A → 0 (up to equivalence) is the split one, so E ≅ A ⊕ B"
    - "Hom(A, B) = 0, meaning there are no morphisms from A to B"
    - "A and B are both injective modules"
  answer: 1
  explanation: "Ext¹(A, B) classifies equivalence classes of extensions of A by B — short exact sequences 0 → B → E → A → 0. The zero element of Ext¹ corresponds to the split extension, where E ≅ A ⊕ B. If Ext¹(A, B) = 0, this is the only class: every extension splits, and A and B cannot be non-trivially glued together. This does not say anything directly about Hom(A, B) or the injectivity of A or B."

- question: "How is Ext^n(A, B) computed?"
  type: multiple-choice
  options:
    - "By applying Hom(−, B) to a projective resolution of A and taking cohomology"
    - "By applying Hom(A, −) to an injective resolution of B and taking cohomology"
    - "By taking the n-th homology of the chain complex A → A → A → ⋯"
    - "By iterating the Hom functor n times: Hom(A, Hom(A, ⋯ Hom(A, B) ⋯))"
  answer: 1
  explanation: "Ext^n(A, B) is defined as the n-th cohomology of the cochain complex obtained by applying Hom(A, −) to an injective resolution 0 → B → I⁰ → I¹ → I² → ⋯ of B (after dropping B). The Hom functor is left exact but not right exact, so cohomology at each step measures the failure of exactness. Notably, Ext can also be computed via a projective resolution of A (applying Hom(−, B)), and both methods give the same result — which is why Ext^n(A, B) is well-defined as an invariant of the pair (A, B)."

- question: "Ext⁰(A, B) is a new invariant that captures information not already contained in Hom(A, B)."
  type: true-false
  answer: false
  explanation: "Ext⁰(A, B) = Hom(A, B). It is the zeroth cohomology of the complex obtained by applying Hom(A, −) to the injective resolution, and left exactness of Hom means no information is lost at the zeroth step. The higher Ext groups Ext^n for n ≥ 1 are genuinely new invariants measuring the failure of exactness at subsequent steps — they capture information that Hom alone does not see."

- question: "The Ext groups Ext^n(A, B) are well-defined invariants of the pair (A, B), independent of the choice of injective resolution of B used to compute them."
  type: true-false
  answer: true
  explanation: "This independence is fundamental to Ext being a useful invariant rather than an artifact of construction. Any two injective resolutions of B are related by a chain map (unique up to chain homotopy), and chain homotopic maps induce the same maps on cohomology. Therefore, the cohomology groups you compute are the same regardless of which injective resolution you choose. This is the essential content of the derived functor framework: the construction is canonical."

- question: "Describe the bijection that gives Ext¹(A, B) its geometric meaning as a classifier of extensions."
  type: short-answer
  answer: "There is a natural bijection between elements of Ext¹(A, B) and equivalence classes of short exact sequences 0 → B → E → A → 0, where two extensions are equivalent if there is an isomorphism E → E' making both triangles (involving B and A) commute. The zero element of Ext¹(A, B) corresponds to the split extension B ⊕ A. A nonzero element corresponds to a genuinely non-split extension — a module E that contains B as a submodule with quotient A but is not isomorphic to their direct sum. For example, Ext¹_ℤ(ℤ/2, ℤ) ≅ ℤ/2, reflecting the two extensions: the split one ℤ ⊕ ℤ/2, and the non-split one ℤ (via 0 → ℤ →×2 ℤ → ℤ/2 → 0)."
  explanation: "The bijection makes Ext¹ a computable algebraic invariant for a fundamentally geometric question: in how many essentially different ways can A and B be 'glued together' into a single module? This connection between algebraic computation (derived functors, injective resolutions) and structural classification (extensions) is the hallmark of homological algebra and the reason Ext appears throughout algebraic topology, group cohomology, and algebraic geometry."
```

## Explainer

From your study of exact sequences, you know that a short exact sequence 0 → B → E → A → 0 encodes the idea that E is built from B and A — but not necessarily as a direct sum B ⊕ A. The question of whether such a sequence splits (whether E ≅ A ⊕ B) is a central one, and you've seen that it depends on properties of the morphisms involved. From injective objects, you know that having enough injectives in an abelian category allows you to resolve any object in a canonical way. The Ext functor is where these ideas converge: it measures, systematically, the obstruction to splitting.

The construction begins by choosing an **injective resolution** of B: an exact sequence 0 → B → I^0 → I^1 → I^2 → ⋯ where each I^k is injective. Such resolutions exist in any abelian category with enough injectives (like modules over a ring). Now apply the functor Hom(A, −) to the resolution (dropping B): you get a cochain complex 0 → Hom(A, I^0) → Hom(A, I^1) → Hom(A, I^2) → ⋯. This complex is generally not exact — Hom(A, −) is left exact but not right exact, so exactness can fail at each step. The **n-th cohomology** of this complex is defined to be **Ext^n(A, B)**. Ext^0(A, B) recovers Hom(A, B) itself (the original left-exact piece that did survive). The higher Ext groups measure the failure of the resolution to remain exact after applying Hom.

The deepest result is the **classification theorem for Ext^1**: elements of Ext^1(A, B) are in natural bijection with equivalence classes of short exact sequences 0 → B → E → A → 0, where two extensions are equivalent if there is an isomorphism between them that fixes both B and A. The zero element of Ext^1(A, B) corresponds to the split extension B ⊕ A; a nonzero element corresponds to a genuinely non-split extension. This makes Ext^1 a computable algebraic invariant that encodes whether and how A and B can be "glued together" non-trivially. For example, Ext^1_ℤ(ℤ/2, ℤ) ≅ ℤ/2, which corresponds to the fact that there are exactly two extensions of ℤ/2 by ℤ: the split one (ℤ ⊕ ℤ/2) and the non-split one (ℤ itself, via the sequence 0 → ℤ →×2 ℤ → ℤ/2 → 0).

Higher Ext groups Ext^n(A, B) for n ≥ 2 have a similar interpretation in terms of longer exact sequences and appear naturally in cohomology theories. In group cohomology, Ext^n over the group ring ℤ[G] computes H^n(G, M); in sheaf theory, Ext^n encodes derived global sections. The power of the derived functor framework is that it is universal: regardless of which injective resolution of B you choose, the Ext groups are well-defined up to canonical isomorphism, so they are genuine invariants of the pair (A, B), not artifacts of the resolution.

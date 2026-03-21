---
id: left-right-adjoints
title: Left and Right Adjoints
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: universal-properties
  type: hard
builds-toward:
- kan-extensions
- topos-theory-intro
tags:
- adjoint
- universal-property
- left
- right
stage: advanced
status: draft
---

# Left and Right Adjoints

## Core Idea
For functors F: C → D and G: D → C, F is left adjoint to G (written F ⊣ G) if there exists a natural isomorphism Hom_D(F(−), −) ≅ Hom_C(−, G(−)). This relationship encodes a deep structural property: F and G preserve the monoidal and functorial properties of their source and target categories. Adjoint pairs unify free constructions, tensor products, and many universal properties across algebra and topology.

## How It's Best Learned
Start with concrete adjoint pairs: free-forgetful adjunctions between Set and algebraic categories, tensor product and hom adjunctions between module categories, and homology-cohomology pairings. Verify the adjunction by computing natural isomorphisms of hom-sets explicitly.

## Common Misconceptions
Adjoint functors are not inverses or quasi-inverses; they are distinct functors with a specific structural relationship. Left and right refer to the position in the hom-functor isomorphism, not to group-theoretic inverses. An adjoint pair exists only when the universal property can be satisfied in a natural, categorical way.

## Questions

```yaml
- question: "You know that the tensor product functor M ⊗ − is left adjoint to Hom(M, −). A colleague claims that therefore M ⊗ − preserves all limits — products, kernels, equalizers. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — left adjoints preserve all limits by the adjoint functor theorem"
    - "This is backwards: it is right adjoints that preserve limits; left adjoints preserve colimits (coproducts, cokernels, pushouts)"
    - "Tensor product preserves limits only when M is a flat module, so the claim holds only in special cases"
    - "Hom(M, −) preserves limits and since it is the adjoint of M ⊗ −, they must preserve the same limits"
  answer: 1
  explanation: "The rule is: left adjoints preserve colimits, right adjoints preserve limits. M ⊗ − sits on the left, so it preserves coproducts, cokernels, and filtered colimits — but not kernels or products in general. Hom(M, −) sits on the right, so it preserves kernels and products — but not cokernels. This is why M ⊗ − is right-exact (preserves cokernels as a left adjoint colimit-preservation) but not left-exact (fails to preserve kernels)."

- question: "The free-forgetful adjunction F ⊣ U between Set and Grp illustrates the natural isomorphism Hom_Grp(F(S), G) ≅ Hom_Set(S, U(G)). What does this say about free groups?"
  type: multiple-choice
  options:
    - "Every group homomorphism between free groups is determined solely by the cardinalities of their generating sets"
    - "There is a natural bijection: group homomorphisms from the free group F(S) to any group G correspond exactly to functions from the set S into the underlying set U(G) — this is the universal property of free groups, stated categorically"
    - "Free groups are the 'smallest' groups, which is why they appear on the left side of the category arrow"
    - "The forgetful functor U is the categorical inverse of F, so composing them recovers the original set or group exactly"
  answer: 1
  explanation: "The adjunction isomorphism says: to define a group homomorphism out of a free group, you only need to specify where the generators go — any function from the generating set into the target group extends uniquely to a homomorphism. This is the universal property of free groups, now expressed as an adjunction. Option D is the classic misconception: adjoints are not inverses. U(F(S)) is the underlying set of the free group on S, which contains infinitely many words — not just S."

- question: "If F ⊣ G (F is left adjoint to G), then F and G are inverse functors: applying F then G, or G then F, returns the original object unchanged."
  type: true-false
  answer: false
  explanation: "Adjoint functors are not inverses. Inverse functors (equivalences of categories) satisfy F ∘ G ≅ id and G ∘ F ≅ id. Adjoint functors satisfy a much weaker condition: a natural isomorphism of hom-sets Hom_D(F(−), −) ≅ Hom_C(−, G(−)). For the free-forgetful pair, U(F(S)) is the underlying set of the free group on S — an infinite set of words, not the original finite set S. F and U are far from inverses; the relationship is structural, not invertible."

- question: "The existence of derived functors Tor₁(M, −) and Ext¹(M, −) is a direct consequence of M ⊗ − and Hom(M, −) failing to preserve certain limits or colimits that their left/right adjoint status predicts they 'should' handle better."
  type: true-false
  answer: true
  explanation: "Left adjoints preserve all colimits; right adjoints preserve all limits. M ⊗ − (left adjoint) preserves colimits but fails to preserve some limits — specifically kernels. This failure (the failure of M ⊗ − to be left-exact) is measured by Tor₁(M, −). Hom(M, −) (right adjoint) preserves limits but fails to preserve some colimits — specifically cokernels. This failure is measured by Ext¹(M, −). Derived functors are exactly the algebraic measurement of adjoint failure; they arise precisely where an adjoint cannot do what its position predicts."

- question: "Why does a functor's position as 'left' versus 'right' adjoint determine what it preserves? Give the rule and one concrete consequence."
  type: short-answer
  answer: "Left adjoints preserve colimits (coproducts, pushouts, coequalizers, filtered colimits); right adjoints preserve limits (products, pullbacks, equalizers). This follows from the universal property structure of adjunctions and can be proved once, then applied universally. A concrete consequence: M ⊗ − is left adjoint, so it distributes over direct sums (a colimit: M ⊗ (A ⊕ B) ≅ (M ⊗ A) ⊕ (M ⊗ B)) but need not preserve kernels. This is why tensoring is right-exact but not necessarily left-exact, and why projective modules (over which tensoring is exact) are special."
  explanation: "The limit/colimit preservation theorem is one of the most powerful tools in category theory because it turns a question ('what does this functor preserve?') into a structural lookup ('which side of the adjunction is it on?'). It unifies dozens of separate algebraic facts — distributivity of tensor over direct sums, left-exactness of Hom, exactness of free modules — into a single categorical principle."
```

## Explainer

Building on adjoint functors and universal properties, left and right adjoints unpack a fundamental asymmetry: the **left adjoint** is the "building" functor that freely constructs structure, while the **right adjoint** is the "forgetting" or "embedding" functor that reduces or restricts structure. This asymmetry carries deep consequences for what each functor preserves.

The archetypal example is the free-forgetful adjunction. The forgetful functor U: Grp → Set sends every group to its underlying set, forgetting the group multiplication. The free functor F: Set → Grp sends every set S to the free group generated by S — the group of all words in the symbols of S and their formal inverses. These form an adjoint pair F ⊣ U, and the natural isomorphism Hom_Grp(F(S), G) ≅ Hom_Set(S, U(G)) says: group homomorphisms out of a free group correspond exactly to functions from the generating set into the underlying set of G. This is the **universal property of free groups**, now stated as an adjunction. The left adjoint F occupies the left slot in Hom_D(F(−), −); the right adjoint U occupies the right slot.

The terms **left** and **right** are not arbitrary: they encode which limits and colimits each functor preserves. Left adjoints always preserve colimits — coproducts, coequalizers, pushouts, filtered colimits. Right adjoints always preserve limits — products, equalizers, pullbacks, limits of diagrams. This follows from the universal property structure of the adjunction and can be proven once, then applied everywhere. As a consequence, the tensor product functor M ⊗ − (left adjoint to Hom(M, −)) preserves direct sums but not products in general — it is right-exact but not left-exact. Hom(M, −) (right adjoint to M ⊗ −) preserves products and kernels but not cokernels.

This failure of exactness is not a deficiency — it is a diagnostic. When M ⊗ − fails to preserve a kernel, the failure is measured by Tor₁(M, −). When Hom(M, −) fails to preserve a cokernel, the failure is measured by Ext¹(M, −). Adjoint pairs thus predict exactly where **derived functors** must appear: at every point where the adjoint fails to preserve a limit or colimit it "should" but doesn't. Understanding that Tor and Ext arise from the failure of adjoints to be exact is one of the deepest organizational principles in homological algebra.

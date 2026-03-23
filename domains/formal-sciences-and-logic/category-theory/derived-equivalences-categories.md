---
id: derived-equivalences-categories
title: Derived Equivalences of Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: triangulated-categories
  type: hard
- id: equivalence-of-categories
  type: hard
builds-toward:
- topos-theory-intro
tags:
- derived-equivalence
- derived-category
- Morita
- homological
stage: expert
status: validated
---

# Derived Equivalences of Categories

## Core Idea
Two categories are derived equivalent if their derived categories are equivalent as triangulated categories. Derived equivalence is coarser than ordinary equivalence but preserves homological invariants. Morita equivalence (between module categories) is an instance of derived equivalence. Derived equivalent categories need not be equivalent as ordinary categories but share the same derived categorical structure, making derived equivalence a fundamental invariant in representation theory.

## How It's Best Learned
Study Morita equivalence for rings and modules as the canonical example. Verify that derived equivalent categories have isomorphic Hochschild homology and K-theory. Explore how tilting complexes induce derived equivalences between module categories.

## Common Misconceptions
Derived equivalence is weaker than ordinary equivalence; two derived equivalent categories may have very different ordinary categorical properties. The notion depends on the choice of derived category (unbounded, bounded, etc.). Not every equivalence of derived categories lifts to an equivalence of underlying categories.

## Questions

```yaml
- question: "Rings R and S are Morita equivalent. What can you immediately conclude about their derived categories?"
  type: multiple-choice
  options:
    - "Their derived categories are NOT equivalent, because Morita equivalence is stronger than derived equivalence and implies ordinary, not derived, structure"
    - "Their derived categories are equivalent as triangulated categories, because an ordinary equivalence of module categories induces a derived equivalence"
    - "Their derived categories may or may not be equivalent — Morita equivalence and derived equivalence are unrelated notions"
    - "Their derived categories are equivalent, but only if R and S are commutative rings"
  answer: 1
  explanation: "Morita equivalence means the module categories Mod-R and Mod-S are equivalent as ordinary categories. An ordinary equivalence of abelian categories induces an equivalence of their derived categories as triangulated categories, because the derived category construction is functorial and preserves quasi-isomorphisms under exact functors. So Morita equivalence implies derived equivalence. The converse fails: two rings can be derived equivalent without being Morita equivalent — derived equivalence is strictly weaker."

- question: "Two algebras A and B are derived equivalent (but not Morita equivalent). A mathematician computes their Hochschild homology groups. What should she expect?"
  type: multiple-choice
  options:
    - "HH_n(A) ≇ HH_n(B) for most n, because Hochschild homology requires the ordinary categorical structure lost in the derived category"
    - "HH_n(A) ≅ HH_n(B) for all n, because Hochschild homology is an invariant of the derived category and is preserved by derived equivalence"
    - "HH_0(A) ≅ HH_0(B) but higher Hochschild homology groups may differ"
    - "The comparison is undefined unless A and B have the same number of simple modules"
  answer: 1
  explanation: "Hochschild homology is a derived invariant — it can be computed directly from the derived category and is therefore preserved by any derived equivalence. This is one of the key practical consequences of the theory: algebras with different presentations, different numbers of simple modules, and very different ordinary categorical structures can be 'homologically indistinguishable.' The preservation of Hochschild homology (and K-theory, Hochschild cohomology, etc.) makes derived equivalence a useful coarsening — it identifies a meaningful notion of 'same homological type.'"

- question: "If two categories A and B are equivalent as ordinary categories, they are automatically derived equivalent."
  type: true-false
  answer: true
  explanation: "Ordinary equivalence is stronger than derived equivalence — it implies derived equivalence but not vice versa. If F: A → B is an ordinary equivalence of abelian categories, the induced functor on derived categories D(A) → D(B) is a triangulated equivalence. This is because exact functors preserve quasi-isomorphisms, and an ordinary equivalence of abelian categories is exact. So the implication is: ordinary equivalence ⟹ derived equivalence; but derived equivalence ⇏ ordinary equivalence."

- question: "Two rings can be derived equivalent even if their module categories are not equivalent as ordinary categories."
  type: true-false
  answer: true
  explanation: "This is the key feature that makes derived equivalence genuinely useful beyond Morita theory. A tilting complex T in D^b(Mod-R) can induce an equivalence D^b(Mod-R) ≅ D^b(Mod-S) where S = End(T), even when Mod-R and Mod-S are not equivalent as ordinary categories. In representation theory, this means two algebras with different numbers of simple modules (and hence non-isomorphic module categories) can still be 'homologically the same.' Derived equivalence is strictly weaker than Morita equivalence, capturing a coarser notion of sameness at the homological level."

- question: "Explain why derived equivalence is described as 'coarser' than ordinary equivalence, and give an example of what is preserved and what may not be preserved when two categories are derived equivalent but not ordinarily equivalent."
  type: short-answer
  answer: "Derived equivalence identifies more pairs of categories as 'the same' than ordinary equivalence does — it imposes weaker requirements. Two categories are derived equivalent if their derived categories (which retain homological information but lose some fine-grained categorical structure) are equivalent as triangulated categories; they might differ significantly at the level of their ordinary categorical structure. What is preserved: Hochschild homology, Hochschild cohomology, K-theory, and other homological invariants that can be computed from the derived category. What may not be preserved: the number of simple modules (which can differ between derived equivalent algebras), and other structure visible only at the level of individual objects rather than homological complexes."
  explanation: "The coarseness is the whole point: working at the level of derived categories creates equivalences between algebras that look different superficially but share the same deep homological structure. This is useful in representation theory (transfer results between algebras) and algebraic geometry (derived equivalences between coherent sheaf categories on different varieties reveal surprising geometric relationships, as in mirror symmetry)."
```

## Explainer

From your study of triangulated categories and equivalence of categories, you have the conceptual building blocks for derived equivalence. Recall that the derived category D(A) of an abelian category A is constructed by formally inverting quasi-isomorphisms — maps of chain complexes that induce isomorphisms on all cohomology groups. This process loses some fine-grained information about A but retains its homological behavior. Two categories are **derived equivalent** when their derived categories are equivalent as triangulated categories — meaning there is a triangulated functor between them that is an equivalence.

The key calibration is where derived equivalence sits in a hierarchy of notions of sameness. Ordinary categorical equivalence is strongest: two categories that are equivalent in the usual sense certainly have equivalent derived categories. Derived equivalence is strictly weaker: two categories can be derived equivalent while being very different as ordinary categories. The classic example is **Morita equivalence** for rings: rings R and S are Morita equivalent when their module categories Mod-R and Mod-S are equivalent (as ordinary categories). Morita equivalence is an instance of derived equivalence, since an ordinary equivalence induces a derived equivalence. But derived equivalence allows more: a derived equivalence between module categories need not come from any ordinary equivalence between the categories themselves.

The mechanism for constructing derived equivalences is the **tilting complex**. A tilting complex T in the derived category D^b(Mod-R) is a complex satisfying certain orthogonality conditions (no self-Ext groups in nonzero degrees) and generating the derived category. The endomorphism ring S = End(T) is the derived equivalent partner: there is a derived equivalence D^b(Mod-R) ≅ D^b(Mod-S). This is the Rickard-Morita theorem, the derived analogue of classical Morita theory. Tilting theory is the primary tool for constructing and classifying derived equivalences in representation theory of algebras.

Derived equivalence preserves a substantial collection of invariants: **Hochschild homology** and **Hochschild cohomology**, **K-theory**, the **center** of the derived category, and many other homological and homotopical data. This makes derived equivalence a powerful coarsening that is still discriminating enough to be useful. Two algebras that are derived equivalent are "homologically indistinguishable" in a precise sense — all homological machinery applied to one gives the same answer as applied to the other. The study of which invariants are preserved and which are not is an active area, and derived equivalence is the standard notion of "same homological type" in modern representation theory and algebraic geometry.

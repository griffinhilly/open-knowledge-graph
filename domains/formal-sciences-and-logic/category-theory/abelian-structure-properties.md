---
id: abelian-structure-properties
title: Properties of Abelian Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: additive-categories
  type: soft
builds-toward:
- homological-dimension-intro
- derived-functors
tags:
- abelian-categories
- homological-algebra
- structure
stage: expert
status: draft
---

# Properties of Abelian Categories

## Core Idea
Abelian categories are additive categories satisfying two axioms: every morphism has a kernel and cokernel, and every monomorphism is a kernel and every epimorphism is a cokernel. This ensures rich homological properties: short exact sequences abound, kernels and cokernels coincide with 'categorical' subobjects, and the theory of extensions via Ext is well-defined.

## Questions

```yaml
- question: "A mathematician wants to prove the snake lemma for the category of sheaves of abelian groups on a topological space. She reasons: 'I'll do an element chase, but sheaves don't have elements in the usual sense — is this valid?' Which theorem directly licenses this approach?"
  type: multiple-choice
  options:
    - "The Yoneda lemma — every category embeds fully into its presheaf category, where morphisms become natural transformations that can be checked pointwise"
    - "The Freyd-Mitchell embedding theorem — every small abelian category embeds fully and faithfully into a category of R-modules for some ring R, so element-level diagram chases transfer back automatically"
    - "The adjoint functor theorem — because the forgetful functor from sheaves to sets has a left adjoint, element arguments can be transported across the adjunction"
    - "The universal coefficient theorem — which converts homological results from module categories to arbitrary abelian categories"
  answer: 1
  explanation: "The Freyd-Mitchell embedding theorem is precisely designed for this situation. It guarantees that any small abelian category can be embedded fully and faithfully (preserving exact sequences, kernels, cokernels, and all exact structure) into the category of modules over some ring R. This means any diagram lemma proven by element-chasing in R-Mod — where objects have elements — automatically transfers back to the abstract abelian category through the embedding. A mathematician can therefore treat sheaves 'as if' they had elements for diagram-chasing purposes, knowing the conclusion will be valid in the original category."

- question: "A short exact sequence 0 → A → B → C → 0 of abelian groups does not split (B is not isomorphic to A ⊕ C). Which algebraic object classifies all non-isomorphic extensions of C by A?"
  type: multiple-choice
  options:
    - "Hom(C, A) — the abelian group of all homomorphisms from C to A"
    - "Ext¹(C, A) — the first derived functor of Hom, which vanishes if and only if every extension of C by A splits"
    - "Tor₁(C, A) — which measures the failure of the tensor product to be exact"
    - "End(B) — the endomorphism ring of the middle object B in the sequence"
  answer: 1
  explanation: "Ext¹(C, A) is exactly the abelian group that classifies extensions of C by A up to equivalence. An element of Ext¹(C, A) corresponds to an equivalence class of short exact sequences 0 → A → B → C → 0. The zero element corresponds to the split extension B ≅ A ⊕ C. If Ext¹(C, A) = 0, every extension splits — there is only the direct sum. Non-trivial elements of Ext¹ parametrize the ways A can be 'twisted' inside B. This is the entry point to derived functor theory: Ext groups generalize this classification to higher degrees and measure the failure of Hom to be exact."

- question: "In an abelian category, the canonical map from the coimage of f (the cokernel of ker f) to the image of f (the kernel of coker f) is always an isomorphism — this is the categorical form of the first isomorphism theorem."
  type: true-false
  answer: true
  explanation: "This is one of the key structural properties of abelian categories, built into their definition. In the category of abelian groups, coimage(f) = A/ker(f) and image(f) = im(f) ⊂ B, and the first isomorphism theorem says A/ker(f) ≅ im(f). The abelian category axioms are precisely chosen to guarantee this isomorphism holds in full generality — in R-modules, sheaves of abelian groups, coherent sheaves, and every other abelian category. This universality is what makes homological algebra transferable across different mathematical contexts."

- question: "The Freyd-Mitchell embedding theorem implies that every abelian category is actually a full category of modules over some ring, making the abstract categorical language redundant for most homological algebra."
  type: true-false
  answer: false
  explanation: "The Freyd-Mitchell theorem applies to *small* abelian categories and produces a full and faithful embedding — not an equivalence of categories. The category of all sheaves on a topological space, or the category of all R-modules for a given ring, is large (not small) and may not embed into a module category in the required sense. Moreover, the ring R in the embedding depends on the specific small category and may be exotic. The abstract categorical language is essential for results that must apply uniformly across all abelian categories — including large ones — and for concepts like adjoint functors and limits that are naturally categorical. The theorem licenses element chasing in proofs; it does not make category theory redundant."

- question: "Why does the Freyd-Mitchell embedding theorem matter for mathematicians working in abelian categories like sheaves of abelian groups, which have no 'elements' in the usual sense?"
  type: short-answer
  answer: "The Freyd-Mitchell theorem guarantees that every small abelian category embeds fully and faithfully into the module category R-Mod for some ring R, preserving all the exact structure (kernels, cokernels, exact sequences). This means any diagram lemma — snake lemma, five lemma, nine lemma — proven by element-chasing in R-Mod automatically transfers back to the original abelian category. A mathematician can therefore reason with 'elements' even in categories like sheaves that have no elements in the naive set-theoretic sense, trusting that the abstract categorical version of the argument is valid. Without this theorem, every such lemma would need a separate element-free abstract proof."
  explanation: "The theorem is an existence result: the embedding exists, but may be non-constructive. In practice, mathematicians rarely find the specific ring R — they just invoke Freyd-Mitchell as justification for element arguments. The essential content is that the axioms of an abelian category exactly capture what is needed for homological algebra: kernels and cokernels exist, monomorphisms are kernels, epimorphisms are cokernels, and the first isomorphism theorem holds. Any category satisfying these axioms inherits the full toolkit of diagram-chasing, derived functors, and exact sequence theory developed in the concrete setting of module categories."
```

## Explainer

You know that an abelian category is an additive category where every morphism has a kernel and cokernel, and where monomorphisms and epimorphisms are the "right" kind of morphism — they are kernels and cokernels respectively. These axioms might seem technical, but they are chosen precisely to guarantee a cluster of structural properties that make homological algebra possible. Understanding which properties follow from which axioms, and why, reveals the architecture behind the definition.

The first major consequence is the **first isomorphism theorem** in categorical form. In any abelian category, for a morphism f: A → B, the coimage (cokernel of the kernel of f) is canonically isomorphic to the image (kernel of the cokernel of f). In the category of abelian groups, this recovers the classical theorem: A/ker(f) ≅ im(f). The fact that this holds in any abelian category means every result in homological algebra that rests only on the first isomorphism theorem is automatically valid in R-modules, sheaves of abelian groups, and every other abelian category — you prove it once, and it works everywhere.

**Short exact sequences** (SES) 0 → A → B → C → 0 are the fundamental building blocks of abelian category structure. The sequence is exact at B means the image of A → B equals the kernel of B → C. Exactness encodes "no gaps and no overlaps" at each position. In the category of modules, a SES says that A embeds into B with quotient C — so B is an "extension" of C by A. Not every such extension is trivial (a direct sum A ⊕ C); the **Ext groups** Ext¹(C, A) classify all extensions up to equivalence, and their vanishing characterizes when all sequences split. This is the entry point to derived functor theory.

The most celebrated structural result in abelian categories is the **snake lemma**: given a commutative diagram with exact rows, there is a natural connecting homomorphism ∂: ker(γ) → coker(α) making a longer exact sequence. The snake lemma cannot even be stated without the machinery of abelian categories, and its proof is a mechanical but illuminating diagram chase that works in any abelian category once you know that monomorphisms are kernels and epimorphisms are cokernels. The **Freyd-Mitchell embedding theorem** gives the ultimate license for such arguments: every small abelian category embeds fully and faithfully into a category of R-modules, meaning diagram chases performed in modules automatically transfer back to the abstract setting. This is why you are permitted to do element-level proofs even in abelian categories that have no elements, like sheaves.

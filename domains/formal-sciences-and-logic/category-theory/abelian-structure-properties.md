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
stage: advanced
status: draft
---

# Properties of Abelian Categories

## Core Idea
Abelian categories are additive categories satisfying two axioms: every morphism has a kernel and cokernel, and every monomorphism is a kernel and every epimorphism is a cokernel. This ensures rich homological properties: short exact sequences abound, kernels and cokernels coincide with 'categorical' subobjects, and the theory of extensions via Ext is well-defined.

## Explainer

You know that an abelian category is an additive category where every morphism has a kernel and cokernel, and where monomorphisms and epimorphisms are the "right" kind of morphism — they are kernels and cokernels respectively. These axioms might seem technical, but they are chosen precisely to guarantee a cluster of structural properties that make homological algebra possible. Understanding which properties follow from which axioms, and why, reveals the architecture behind the definition.

The first major consequence is the **first isomorphism theorem** in categorical form. In any abelian category, for a morphism f: A → B, the coimage (cokernel of the kernel of f) is canonically isomorphic to the image (kernel of the cokernel of f). In the category of abelian groups, this recovers the classical theorem: A/ker(f) ≅ im(f). The fact that this holds in any abelian category means every result in homological algebra that rests only on the first isomorphism theorem is automatically valid in R-modules, sheaves of abelian groups, and every other abelian category — you prove it once, and it works everywhere.

**Short exact sequences** (SES) 0 → A → B → C → 0 are the fundamental building blocks of abelian category structure. The sequence is exact at B means the image of A → B equals the kernel of B → C. Exactness encodes "no gaps and no overlaps" at each position. In the category of modules, a SES says that A embeds into B with quotient C — so B is an "extension" of C by A. Not every such extension is trivial (a direct sum A ⊕ C); the **Ext groups** Ext¹(C, A) classify all extensions up to equivalence, and their vanishing characterizes when all sequences split. This is the entry point to derived functor theory.

The most celebrated structural result in abelian categories is the **snake lemma**: given a commutative diagram with exact rows, there is a natural connecting homomorphism ∂: ker(γ) → coker(α) making a longer exact sequence. The snake lemma cannot even be stated without the machinery of abelian categories, and its proof is a mechanical but illuminating diagram chase that works in any abelian category once you know that monomorphisms are kernels and epimorphisms are cokernels. The **Freyd-Mitchell embedding theorem** gives the ultimate license for such arguments: every small abelian category embeds fully and faithfully into a category of R-modules, meaning diagram chases performed in modules automatically transfer back to the abstract setting. This is why you are permitted to do element-level proofs even in abelian categories that have no elements, like sheaves.

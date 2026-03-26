---
id: abelian-categories-homology
title: Abelian Categories and Homological Algebra
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: homology-and-cohomology
  type: hard
builds-toward:
- derived-functors
- triangulated-categories
tags:
- abelian
- homology
- exact-sequence
- kernel
- cokernel
stage: expert
status: validated
---

# Abelian Categories and Homological Algebra

## Core Idea
An abelian category is an additive category with kernels, cokernels, and images, in which every monomorphism is a kernel and every epimorphism is a cokernel. Abelian categories provide the natural setting for homological algebra: chain complexes, homology, cohomology, and derived functors. Examples include module categories, vector spaces, and abelian groups. The theory of abelian categories abstracts homological algebra to axiomatic foundations.

## How It's Best Learned
Study module categories and vector space categories as canonical abelian examples. Verify the five lemma and snake lemma for abelian categories. Compute derived functors (Ext, Tor) via projective and injective resolutions in abelian categories.

## Common Misconceptions
Abelian categories generalize module categories but are not just 'categorical algebra'—they require specific exactness properties. Not every additive category is abelian; the kernel-cokernel conditions are non-trivial. Abelian category axioms are sufficient for homological algebra but some conclusions require additional structure (e.g., enough projectives).

## Questions

```yaml
- question: "You want to prove the snake lemma holds for sheaves of abelian groups on a topological space, which is not a module category. You know the proof for abelian groups uses element-chasing. What theorem justifies applying the same element-chasing argument here?"
  type: multiple-choice
  options:
    - "The five lemma, which holds in any category with zero morphisms"
    - "The Freyd-Mitchell embedding theorem, which guarantees a full exact embedding of any small abelian category into a module category"
    - "The universal coefficient theorem, which reduces sheaf cohomology to module cohomology"
    - "The comparison theorem for resolutions, which shows any two resolutions compute the same homology"
  answer: 1
  explanation: "The Freyd-Mitchell embedding theorem states that every small abelian category embeds fully and exactly (preserving and reflecting exactness) into R-Mod for some ring R. This means any diagram-chasing proof valid in R-Mod — including the snake lemma, five lemma, and horseshoe lemma — is automatically valid in every abelian category. You do not need a separate proof for sheaves; you invoke Freyd-Mitchell and transfer the module proof. This is the key that unlocks homological algebra across all abelian categories simultaneously."

- question: "Which of the following properties is NOT automatically guaranteed by the abelian category axioms, requiring additional hypotheses for certain homological constructions?"
  type: multiple-choice
  options:
    - "Every morphism has a kernel and a cokernel"
    - "Every monomorphism is a kernel of some morphism"
    - "The category has enough injective objects for right derived functor computation"
    - "Short exact sequences 0 → A → B → C → 0 are well-defined"
  answer: 2
  explanation: "The abelian category axioms guarantee kernels, cokernels, the mono=kernel and epi=cokernel conditions, and thus well-defined exact sequences. However, 'enough injectives' — the condition that every object embeds into an injective — is an additional hypothesis required to construct injective resolutions and compute right derived functors. For example, sheaves on a topological space have enough injectives, but this is a theorem, not an axiom. The category of finitely generated modules over a Noetherian ring may lack enough injectives without further assumptions."

- question: "Most additive category — one where hom-sets are abelian groups and composition is bilinear — is automatically an abelian category."
  type: true-false
  answer: false
  explanation: "Being additive is necessary but far from sufficient for being abelian. An abelian category additionally requires: every morphism has a kernel AND a cokernel, every monomorphism is a kernel (of its cokernel), and every epimorphism is a cokernel (of its kernel). These conditions are non-trivial. The category of free abelian groups is additive but not abelian (cokernels may not be free). The category of Banach spaces with bounded linear maps is additive but not abelian. The kernel/cokernel exactness conditions are what give abelian categories their homological power."

- question: "In an abelian category, the homology object Hₙ = ker(dₙ)/im(dₙ₊₁) of a chain complex is well-defined because the axioms guarantee that images and kernels exist as subobjects in the required categorical sense."
  type: true-false
  answer: true
  explanation: "In a general category, 'image' and 'kernel' may not be defined or may not be comparable. In an abelian category, every morphism f: A → B has a kernel (an equalizer of f and 0) and an image (defined as the kernel of the cokernel of f). The condition that every monomorphism is a kernel ensures that im(dₙ₊₁) is a legitimate subobject of ker(dₙ) — their categorical quotient Hₙ = ker(dₙ)/im(dₙ₊₁) is then a well-defined object of the category. This is exactly what allows homology to be defined internally without reference to elements."

- question: "What does the Freyd-Mitchell embedding theorem mean practically for proving a diagram lemma (e.g., the five lemma or horseshoe lemma) in an arbitrary abelian category?"
  type: short-answer
  answer: "It means you can write the proof using element-chasing in R-Mod, as if objects were sets with elements, and the proof is automatically valid in any abelian category. You do not need to reprove the lemma for each new abelian category (sheaves, representations, coherent sheaves on a scheme). The embedding is full and exact, so it preserves and reflects all the categorical structure (kernels, cokernels, exact sequences) needed for the proof to transfer. Essentially: prove it once in R-Mod with elements; it holds everywhere abelian."
  explanation: "Before Freyd-Mitchell, results in abelian categories required abstract, element-free arguments that were significantly harder to write and check. The embedding theorem permits the concreteness of module-theoretic reasoning without losing generality. The price is that the embedding is not canonical and may require enlarging universes for large categories — the theorem applies to small abelian categories — but for any fixed diagram lemma, the relevant category is small, so the theorem applies."
```

## Explainer

From your study of abelian categories, you know the axioms: the hom-sets are abelian groups, composition is bilinear, there are finite products, every morphism has a **kernel** and **cokernel**, and every monomorphism is a kernel while every epimorphism is a cokernel. From homology and cohomology you know chain complexes and their homology groups in concrete settings like simplicial homology or singular cohomology. The present topic is the synthesis: abelian categories are precisely the setting in which homological algebra works, not just for one or two examples, but universally.

The core machinery that homological algebra requires is **exactness**: a sequence A → B → C is exact at B if the image of the first map equals the kernel of the second. Exactness captures "no information is lost or invented." In an abelian category, exactness is well-defined because kernels and images exist as objects (not just sets), and the condition that every mono is a kernel ensures that "image = kernel" is a categorical statement, not just a set-theoretic one. **Short exact sequences** 0 → A → B → C → 0 generalize the relationship between a subobject, an object, and its quotient, and they appear everywhere: the long exact sequence in homology, the snake lemma output, extension problems. All of this requires only the abelian category axioms — it applies simultaneously to modules, sheaves of abelian groups, representations of a quiver, and coherent sheaves on a scheme.

**Diagram-chasing** is the technique of chasing elements around commutative diagrams to prove exactness results. In the category of abelian groups or R-modules, this is literal: you pick an element in one group and track it through maps to reach a contradiction or a desired element elsewhere. The remarkable fact is that diagram-chasing proofs in any abelian category can be reduced to the same argument — by the **Freyd-Mitchell embedding theorem**, every small abelian category embeds fully and exactly into a module category. This means: whenever you want to prove a result about an abelian category (the **five lemma**, the **snake lemma**, the **horseshoe lemma**), you may assume without loss of generality that objects have elements. Write the element-chasing proof in R-Mod; it is valid in every abelian category.

**Chain complexes** in an abelian category A are sequences ⋯ → Aₙ₊₁ →^{dₙ₊₁} Aₙ →^{dₙ} Aₙ₋₁ → ⋯ with dₙ ∘ dₙ₊₁ = 0 for all n. The **homology** at position n is Hₙ = ker(dₙ)/im(dₙ₊₁), which is an object of A. In an abelian category this quotient is well-defined (coequalized images and kernels coexist as required). A **morphism of chain complexes** is a collection of morphisms fₙ: Aₙ → Bₙ commuting with differentials; it induces morphisms Hₙ(A) → Hₙ(B) on homology. This is exactly the functorial behavior from your homology prerequisite, now seen to hold in any abelian category, for any chain complexes — not just topological ones.

**Derived functors** are the deepest payoff. Left-exact functors (like Hom(−, N) or the global sections functor Γ on sheaves) fail to preserve short exact sequences exactly: they preserve the left portion but truncate at the right. The **right derived functors** Rⁱ F measure the failure: they detect "hidden" information lost by the inexact portion. To compute Rⁱ F(A), resolve A by an injective resolution 0 → A → I⁰ → I¹ → ⋯, apply F termwise, and take homology. The result is independent of the choice of resolution — a consequence of the comparison theorem for resolutions, which in turn requires that the ambient category be abelian with enough injectives. The canonical examples Ext^i_R(M, N) = Rⁱ Hom_R(M, −)(N) and Tor^R_i(M, N) = L_i(M ⊗_R −)(N) are specific instances; the language of abelian categories reveals them as two faces of the same general construction.

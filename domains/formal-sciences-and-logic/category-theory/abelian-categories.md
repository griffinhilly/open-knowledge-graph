---
id: abelian-categories
title: Abelian Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: equalizers-and-coequalizers
  type: hard
- id: products-and-coproducts
  type: soft
- id: initial-and-terminal-objects
  type: soft
- id: group-definition-examples
  type: soft
- id: ring-definition-examples
  type: soft
- id: group-definition-and-examples
  type: soft
- id: vector-spaces
  type: soft
builds-toward:
- chain-complexes-exact-sequences
tags:
- abelian category
- additive category
- kernel
- cokernel
- exact sequence
- Ab-enriched
stage: advanced
status: draft
---
# Abelian Categories

## Core Idea
An abelian category is an additive category (enriched over abelian groups, with biproducts) in which every morphism has a kernel and cokernel, every monomorphism is the kernel of its cokernel, and every epimorphism is the cokernel of its kernel. This axiom system, formalized by Grothendieck and Buchsbaum, captures the essential properties of categories like Ab (abelian groups), R-Mod (modules over a ring), and sheaves of abelian groups, enabling homological algebra to be developed in a purely categorical setting. The Freyd-Mitchell embedding theorem shows every small abelian category embeds exactly into some R-Mod, justifying diagram-chasing arguments.

## How It's Best Learned
Verify the abelian category axioms for R-Mod: check that hom-sets are abelian groups, biproducts exist (direct sums), every morphism has a kernel and cokernel, and the canonical factorization image(f) → coimage(f) is an isomorphism. Then try to find a non-example: the category of free abelian groups is additive but not abelian (cokernels may not be free).

## Common Misconceptions
- Not every additive category is abelian; the existence of kernels and cokernels plus the factorization axiom are essential additional conditions.
- The Freyd-Mitchell embedding theorem applies only to small abelian categories; it does not mean every abelian category literally is a module category.
- An abelian category is not the same as an Ab-enriched category; abelian requires additional exactness properties beyond mere enrichment.

## Questions

```yaml
- question: "Which of the following categories is additive but NOT abelian?"
  type: multiple-choice
  options: ["Ab (abelian groups)", "R-Mod (modules over a ring)", "Free abelian groups", "Sheaves of abelian groups on a topological space"]
  answer: 2
  explanation: "The category of free abelian groups is additive — hom-sets are abelian groups and biproducts (direct sums) exist — but it fails to be abelian because cokernels of maps between free abelian groups need not be free. For instance, the cokernel of Z →×2 Z is Z/2Z, which is not free. The other three are standard examples of abelian categories."

- question: "Every Ab-enriched category with biproducts is an abelian category."
  type: true-false
  answer: false
  explanation: "Ab-enrichment plus biproducts makes a category additive, which is only the first layer of abelian. An abelian category additionally requires that every morphism has a kernel and cokernel, and that the canonical map from the coimage to the image is an isomorphism. These exactness conditions are not implied by additivity alone."

- question: "State what the Freyd-Mitchell embedding theorem guarantees and identify its key restriction."
  type: short-answer
  answer: "The theorem guarantees that every small abelian category embeds fully, faithfully, and exactly (preserving exact sequences) into R-Mod for some ring R. The key restriction is smallness: the theorem does not apply to large abelian categories such as Ab or R-Mod itself. The practical payoff is that diagram-chasing arguments valid in R-Mod (e.g., the snake lemma proved by element-chasing) transfer to any small abelian category."
  explanation: "The embedding theorem is what licenses the common practice of 'chasing elements' in an abstract abelian category even though its objects may not literally have elements. Without the smallness hypothesis the result fails, so it cannot be invoked for the most common large examples."
```

## Explainer

If you have worked through categories and morphisms and understand equalizers, you already know what kernels are in familiar settings: the kernel of a group homomorphism f: G → H is the subgroup of elements mapped to the identity. Abelian categories take that idea and axiomatize it purely in terms of morphisms, with no reference to elements.

The starting point is an *additive* category: one where every hom-set carries an abelian group structure that is compatible with composition, and where finite products and coproducts coincide (these coinciding objects are called biproducts, or direct sums). In Ab or R-Mod, the biproduct of M and N is just M ⊕ N, and hom-sets inherit pointwise addition. Once you have additivity, you can define the kernel of f: A → B as the equalizer of f and the zero morphism — a construction you have already seen. The cokernel is the dual notion: it is the coequalizer of f and 0.

An abelian category adds two exactness axioms on top of additivity. First, every morphism must have both a kernel and a cokernel. Second, the canonical factorization of any morphism f as A ↠ coimage(f) → image(f) ↣ B must have the middle map be an isomorphism. In R-Mod this is automatic — the coimage is A/ker(f) and the image is the set-theoretic image, and the first isomorphism theorem says they are isomorphic. The axiom demands this holds *categorically* without assuming elements.

The Freyd-Mitchell embedding theorem tells you that this axiomatic framework is, in a precise sense, equivalent to working in some module category. Any small abelian category embeds exactly into R-Mod for some ring R. "Exactly" means exact sequences are preserved and reflected — so a sequence that is exact in the abstract category maps to an exact sequence of modules, and vice versa. This justifies the widespread practice of proving lemmas (snake lemma, five lemma, horseshoe lemma) by element-chasing: even in an abstract abelian category, there is always an underlying module category where the proof goes through, and the embedding carries it back.

The boundary of the abelian world is worth knowing. Free abelian groups form an additive category that is not abelian, because cokernels of maps between free modules can have torsion (like Z/2Z), which fails to be free. Topological abelian groups and Banach spaces form categories where some abelian axioms fail. Recognizing these non-examples sharpens the intuition for what the exactness axioms are actually buying you.

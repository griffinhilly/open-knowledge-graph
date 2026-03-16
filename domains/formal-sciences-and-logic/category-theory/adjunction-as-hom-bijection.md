---
id: adjunction-as-hom-bijection
title: Adjunctions as Natural Hom-set Bijections
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: left-adjoint-functors
  type: hard
- id: right-adjoint-functors
  type: hard
- id: adjoint-functors
  type: soft
builds-toward:
- monads-in-category-theory
- kan-extensions
tags:
- adjunction
- hom-sets
- natural-transformation
stage: advanced
status: draft
---

# Adjunctions as Natural Hom-set Bijections

## Core Idea
An adjunction L ⊣ R is a pair of functors with a natural isomorphism φ: Hom_D(Lc, d) ≅ Hom_C(c, Rd) for all objects c and d. The unit η: id_C ⇒ RL and counit ε: LR ⇒ id_D encapsulate the adjunction. This framework unifies diverse constructions—free groups, tensor products, completions—as universal solutions.

## Explainer

You already understand left and right adjoints separately — you know that a left adjoint L "freely generates" something and a right adjoint R "forgets" or "restricts." The hom-set formulation makes the relationship between them precise. The claim is that maps from Lc to d in category D are in **natural bijective correspondence** with maps from c to Rd in category C. The word "natural" carries real weight: this bijection must be compatible with pre- and post-composition by morphisms, meaning it commutes with all relevant functorial operations. This naturality is what elevates the bijection from a coincidence to a structural fact.

The canonical example is the free-forgetful adjunction between **Set** and **Grp**. The free functor L sends a set S to the free group F(S); the forgetful functor R sends a group G to its underlying set. The adjunction says: a group homomorphism from F(S) to G is the same thing as a function from S to the underlying set of G. Concretely, to define a homomorphism out of the free group, you only need to specify where the generators go — an element of Hom_Set(S, R(G)). This is the **universal property of free constructions** in hom-set language.

The **unit** η: id_C ⇒ RL is a natural transformation that sends each object c to a morphism ηc: c → R(Lc). It is the "canonical inclusion": every set embeds into the underlying set of its free group, every vector space basis embeds into the span it generates. The **counit** ε: LR ⇒ id_D goes the other way: εd: L(Rd) → d is the "evaluation map," the canonical map out of the free object built on the underlying structure of d back to d itself (e.g., the free group on the underlying set of G maps canonically onto G by sending each generator word to its product in G). The unit and counit together satisfy the **triangle identities**, which encode that round trips through the adjunction (first apply η, then ε, in the right order) are the identity natural transformation.

The power of the hom-set perspective is that it packages all of this into a single natural isomorphism φ: Hom_D(Lc, d) ≅ Hom_C(c, Rd), making explicit what the unit and counit only imply. Given any morphism f: Lc → d, its **transpose** φ(f): c → Rd is the corresponding map in C; given g: c → Rd, its transpose φ⁻¹(g): Lc → d is the corresponding map in D. The naturality of φ means these transpositions interact correctly with all morphisms in both categories — the bijection is not just object-by-object but globally coherent across the entire categorical structure. This is the sense in which adjunctions "unify diverse constructions": tensor-hom adjunctions, product-diagonal adjunctions, and suspension-loop adjunctions in topology all have exactly this hom-set structure.

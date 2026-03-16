---
id: presheaves-and-sheaves
title: Presheaves and Sheaves on Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: presheaves
  type: hard
- id: yoneda-embedding-full-faithful
  type: soft
builds-toward:
- topos-theory-intro
tags:
- presheaf
- sheaf
- grothendieck-topology
- topos
- gluing
stage: advanced
status: draft
---

# Presheaves and Sheaves on Categories

## Core Idea
A presheaf on a category C is a contravariant functor C^op → Set. The presheaf category [C^op, Set] is a Grothendieck topos: cartesian closed, complete, cocomplete, and satisfying the internal axiom of choice. Sheaves are presheaves satisfying a gluing condition with respect to a Grothendieck topology, forming a reflective subcategory. Presheaves and sheaves provide the fundamental examples of topoi and model intuitionistic logic.

## How It's Best Learned
Study simplicial sets [∆^op, Set] as the canonical presheaf example. Verify that [C^op, Set] is cartesian closed and complete. Define sheafification and verify that sheaves form a reflective subcategory. Compute limits and colimits of presheaves and sheaves explicitly.

## Common Misconceptions
Presheaves are not sheaves; sheafification requires imposing a Grothendieck topology. Not every presheaf is representable; non-representable presheaves are essential to the theory. Topos logic is intuitionistic; classical logic requires additional axioms (like axiom of choice), and not all topoi satisfy them.

## Explainer

A **presheaf** on a small category C is a contravariant functor F : C^op → **Set**: to each object c ∈ C it assigns a set F(c), and to each morphism f : c → d it assigns a function F(f) : F(d) → F(c) going the opposite way, with functoriality. You should think of C as a category of "open sets" (or patches of some space), and F(c) as the set of "local data" (sections) defined on c. The contravariancy captures restriction: if d is a smaller patch inside c, and f : d → c is the inclusion, then F(f) restricts data from c down to d.

From your study of the Yoneda embedding, you know that every representable presheaf yc = hom(–, c) is a presheaf, and the Yoneda lemma says natural transformations from yc to F correspond bijectively to elements of F(c). The presheaf category [C^op, **Set**] is vastly larger than C itself — it contains representables, but also all the non-representable presheaves that arise when you "freely complete" C. This category is a **Grothendieck topos**: it has all limits and colimits, it is cartesian closed (internal function objects exist), and it has a subobject classifier Ω. Limits and colimits in [C^op, **Set**] are computed pointwise — (lim F_i)(c) = lim(F_i(c)) — making it one of the most tractable categories to work with concretely.

A **sheaf** imposes an additional *gluing condition*. Given a **Grothendieck topology** J on C — a system specifying, for each object c, which families of morphisms "cover" c — a presheaf F is a *J-sheaf* if whenever you have local sections defined on a covering family that agree on all overlaps, there is a unique global section that restricts to each local one. This is exactly the classical condition from topology: a continuous function on a space is determined by its values on an open cover, and a sheaf formalizes this "local-to-global" principle categorically. The category of J-sheaves **Sh(C, J)** is a reflective subcategory of [C^op, **Set**]: the inclusion has a left adjoint called **sheafification**, which forces a presheaf to satisfy the gluing condition by "forcing" agreement on overlaps.

Sheaves and presheaves connect the abstract machinery of category theory to concrete mathematics in both directions. Going toward topology and geometry: sheaves on the site of open sets of a topological space model varying algebraic structures (the structure sheaf of a scheme, the sheaf of continuous functions). Going toward logic: the internal language of a Grothendieck topos is intuitionistic higher-order logic, and different Grothendieck topologies on the same category C give different logical universes — some satisfying classical logic, some not. This is why the theory of presheaves and sheaves is foundational to topos theory, algebraic geometry (the étale site, the flat site), and categorical logic: the gluing axiom is the precise mathematical expression of the idea that local truth implies global truth, and its failure or variation gives rise to rich structure.

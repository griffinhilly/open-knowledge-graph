---
id: adjunction-unit-and-counit
title: Adjunction Unit and Counit
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: natural-transformations
  type: hard
builds-toward:
- monads-in-category-theory
- equivalence-of-categories
tags:
- unit
- counit
- triangle identities
- adjunction
- monad
stage: advanced
status: validated
---

# Adjunction Unit and Counit

## Core Idea
An adjunction F ⊣ G can equivalently be given by two natural transformations: the unit η: Id_C ⇒ G∘F and the counit ε: F∘G ⇒ Id_D, satisfying the triangle identities (ε_F ∘ F(η) = id_F and G(ε) ∘ η_G = id_G). The unit η_A: A → GF(A) is the universal arrow from A to G—the 'most efficient' way to place A inside the G-structure. The triangle identities are the coherence conditions that ensure the hom-set bijection and the unit-counit formulation are equivalent.

## How It's Best Learned
For the free-forgetful adjunction between Set and Grp, identify the unit as the inclusion of a set S into the underlying set of its free group F(S), and the counit as the evaluation map F(U(G)) → G sending generators to their values. Verify both triangle identities by tracing elements.

## Common Misconceptions
- The triangle identities look like cancellation laws but are not trivially true; they encode the coherence between unit and counit.
- The unit need not be a monomorphism and the counit need not be an epimorphism in general, though they are in many familiar examples.
- Confusing the unit (going into GF) with the counit (coming out of FG) is a common source of errors.

## Explainer

You already understand adjoint functors through the hom-set bijection: F ⊣ G means there is a natural bijection Hom_D(FA, B) ≅ Hom_C(A, GB) for every A in C and B in D. The unit and counit offer an alternative formulation of the same adjunction — one that packages the adjunction into two natural transformations rather than a family of bijections, and that makes the "closest approximation" intuition explicit.

The **unit** η: Id_C ⇒ G∘F assigns to each object A a morphism η_A: A → G(FA) in C. Think of this as the "embedding" of A into the G-structure built by first applying F. In the free-forgetful adjunction (F = free group functor from Set to Grp, G = forgetful functor), η_A: A → G(FA) is the inclusion of the set A into the underlying set of the free group F(A): each element maps to the corresponding generator. This map is **universal**: any set map A → G(B) (for any group B) factors *uniquely* through η_A via the group homomorphism FA → B corresponding to it under the hom-set bijection. The unit is the "most efficient" or "least committed" way to map A into anything in the image of G.

The **counit** ε: F∘G ⇒ Id_D assigns to each object B a morphism ε_B: F(G(B)) → B in D. This goes in the opposite direction: take B, forget structure to get G(B), freely rebuild with F to get F(G(B)), then collapse back to B via ε_B. In the free-forgetful example, G(B) is the underlying set of group B, F(G(B)) is the free group on that set, and ε_B: F(G(B)) → B is the **evaluation homomorphism** — it sends each generator (= group element of B, viewed as a generator of the free group) back to itself in B. This is a group homomorphism that "quotients out" the free group by all relations that hold in B.

The **triangle identities** state that the unit and counit are self-consistent: (ε_F ∘ F(η)) = id_F and (G(ε) ∘ η_G) = id_G. Written as component equations: ε_{FA} ∘ F(η_A) = id_{FA} for each A, and G(ε_B) ∘ η_{G(B)} = id_{G(B)} for each B. These are not automatic — they are the conditions that guarantee the unit-counit formulation is *equivalent* to the hom-set bijection. To see one triangle concretely: take a set A, form F(A) (free group on A), apply G to get G(F(A)) (underlying set of free group = generators plus all words), form F(G(F(A))) (free group on all those words), then apply the counit ε_{F(A)} (evaluate back to F(A)). The triangle identity says the round trip via η and ε returns you to F(A) with the identity map — nothing is added or lost by the detour.

The unit-counit formulation becomes indispensable when you work with monads. The monad associated to an adjunction F ⊣ G is the endofunctor T = G∘F with unit η: Id ⇒ T and multiplication μ: T∘T ⇒ T defined as μ = G(ε_F): G(F(G(F(−)))) → G(F(−)). The triangle identities become the unit laws for the monad: η_T and T(η) are right and left units for μ. This shows that the triangle identities are not merely bookkeeping — they are the axioms that make the monad structure coherent, and they originate entirely from the unit and counit of the underlying adjunction.

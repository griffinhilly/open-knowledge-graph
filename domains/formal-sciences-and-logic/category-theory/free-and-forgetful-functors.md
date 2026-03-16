---
id: free-and-forgetful-functors
title: Free and Forgetful Functors
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: free-objects
  type: hard
- id: group-definition-and-examples
  type: soft
builds-toward:
- left-right-adjoints
tags:
- free
- forgetful
- adjoint
- universal-property
stage: advanced
status: draft
---

# Free and Forgetful Functors

## Core Idea
The forgetful functor U: D → C 'forgets' structure by mapping objects to their underlying sets or simpler structures. The free functor F: C → D is left adjoint to U, and sends generators to the 'freest' objects in D built from them. The adjunction F ⊣ U encodes the universal property of free objects: every function from a generating set extends uniquely to a D-morphism.

## How It's Best Learned
Study free-forgetful adjunctions for groups, rings, and modules. Compute free groups on generators and verify the universal property by constructing unique homomorphic extensions. Explore the relationship between free objects and presentable objects.

## Common Misconceptions
Free objects are not trivial or empty; they are the 'largest' objects with minimal structural constraints. Not every forgetful functor has a left adjoint; existence requires sufficient colimits or a generating set. The forgetful functor must be well-defined on both objects and morphisms, not just on objects.

## Explainer

You know what adjoint functors are: a pair F ⊣ U with a natural bijection Hom_D(F(X), Y) ≅ Hom_C(X, U(Y)). The **forgetful functor** and its **free functor** left adjoint are the most intuitive and concrete instance of this pattern, and working through them carefully builds the intuition you need for adjoints in more abstract settings.

The **forgetful functor** U: D → C simply discards structure. For example, U: Grp → Set sends a group (G, ·) to its underlying set G, and a group homomorphism to its underlying function. It "forgets" the group operation. The functor is called forgetful because it does less work than the morphisms of D require — a set function need not preserve the group operation, so U maps group homomorphisms to set functions but allows many more morphisms in Set than exist in Grp between the same underlying sets. The forgetful functor is faithful (injective on hom-sets) because distinct homomorphisms remain distinct as functions, but generally not full (surjective on hom-sets) because not every function is a homomorphism.

The **free functor** F: Set → Grp is the left adjoint to U. F(X) is the **free group** on the generating set X: the group of all finite words in the symbols of X and their formal inverses, with concatenation as the group operation and no relations imposed. The adjunction Hom_Grp(F(X), G) ≅ Hom_Set(X, U(G)) says: to specify a group homomorphism from the free group F(X) to any group G, you need only specify where each generator goes — that is, a function from X to the underlying set of G. The group homomorphism is then uniquely determined by extending that function to all words by applying the group law. This is the **universal property of free objects**: generators determine the morphism, and the free object imposes no constraints beyond those required by the structure itself.

This pattern appears everywhere. The free vector space F(X) on a set X of basis vectors is the left adjoint to the forgetful functor from Vect to Set; linear maps are determined by where basis vectors go. The free monoid on X is the set of all finite strings over X, with concatenation; monoid homomorphisms from it to any monoid M are determined by functions X → M. The free abelian group on X is ℤ^X — integer-valued formal sums of generators. In each case, the free object is "as unstructured as possible while still being an object of D," and the adjunction makes this precision. The adjunction counit ε: F(U(G)) → G is the canonical group homomorphism that sends each generator [g] ∈ F(U(G)) (one generator for each group element g) back to g ∈ G — it is the "evaluation" map collapsing the free object onto the structured one.

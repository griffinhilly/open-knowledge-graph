---
id: dagger-categories
title: Dagger Categories and Involutions
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
- id: functors
  type: soft
builds-toward:
- compact-closed-categories
tags:
- dagger
- involution
- adjoint
- unitary
- self-adjoint
stage: advanced
status: draft
---

# Dagger Categories and Involutions

## Core Idea
A dagger category (†-category) is a category with an involutive functor †: C → C^op such that objects are fixed and f† = (g∘f)† = f† ∘ g†, with (f†)† = f. This structure models categories where morphisms have 'adjoints' or conjugates, as in Hilbert spaces with adjoint operators. Dagger categories provide a categorical framework for self-adjoint and unitary morphisms, and are foundational in categorical quantum mechanics.

## How It's Best Learned
Study the category of finite-dimensional Hilbert spaces with dagger-structure given by adjoint operators. Examine finite sets with involution and verify dagger properties. Define and work with unitary, self-adjoint, and isometric morphisms using the dagger involution.

## Common Misconceptions
The dagger is not a contravariant endofunctor; it is an involution swapping morphism directions while fixing objects. Self-adjoint morphisms (f = f†) behave like Hermitian operators but require careful interpretation in general dagger categories. The dagger structure is additional data and cannot be recovered from the category alone.

## Explainer

From your study of categories and morphisms, you know that a morphism f: A → B is an arrow from one object to another, and composition is the core operation. In many mathematical settings, morphisms have a natural "reversal" operation — not an inverse (which may not exist), but a transpose or adjoint. In linear algebra, every matrix A has a **conjugate transpose** A†. This operation flips the direction (A†: ℂⁿ → ℂᵐ if A: ℂᵐ → ℂⁿ), preserves compositionality ((AB)† = B†A†), and is an involution ((A†)† = A). A **dagger category** takes precisely this structure and abstracts it categorically: it equips each morphism f: A → B with a chosen partner f†: B → A satisfying these same axioms.

The axiomatic content is: (1) f† reverses direction; (2) (g ∘ f)† = f† ∘ g† (contravariance); (3) (f†)† = f (involution); (4) id_A† = id_A. Notice the dagger fixes objects — it is an involution on morphisms only. In the category **FHilb** of finite-dimensional Hilbert spaces with linear maps, the dagger is exactly the adjoint operator (conjugate transpose). This is the motivating example. But the axioms are purely algebraic, so you can have dagger categories with no connection to Hilbert spaces at all — for instance, the category of sets with relations, where f†(b, a) iff f(a, b) (the relational converse).

With the dagger in hand, you can define morphism classes by how they interact with their dagger. A morphism is **self-adjoint** (or Hermitian) if f† = f. It is **unitary** if f† ∘ f = id_A and f ∘ f† = id_B — meaning the dagger serves as a two-sided inverse, but one that knows about the Hilbert space geometry rather than just the set-theoretic structure. These notions categorify the matrix concepts with the same names. In FHilb, self-adjoint linear maps correspond to Hermitian matrices (real eigenvalues, orthogonal eigenvectors), and unitaries correspond to unitary matrices (length-preserving isometries).

The deepest application of dagger categories comes from **categorical quantum mechanics**, introduced by Abramsky and Coecke. Quantum processes are naturally described by morphisms in FHilb. The dagger gives you the dual process (time reversal, measurement), unitarity gives you quantum gates (reversible processes), and self-adjointness gives you observables. By combining dagger structure with the tensor product (compact closed structure), you can derive quantum teleportation protocols, no-cloning theorems, and quantum key distribution graphically — drawing diagrams of morphisms instead of calculating with matrices. The dagger category framework thus turns quantum mechanical reasoning into categorical reasoning, with compositionality built in from the start.

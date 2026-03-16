---
id: compact-closed-categories
title: Compact Closed Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: monoidal-categories
  type: hard
- id: symmetric-monoidal-categories
  type: hard
builds-toward:
- dagger-categories
tags:
- compact-closed
- dual
- trace
- finite-dimensionality
- linear-logic
stage: advanced
status: draft
---

# Compact Closed Categories

## Core Idea
A compact closed category is a monoidal category where every object X has a dual object X* with evaluation and coevaluation morphisms satisfying triangle identities. This categorical structure captures finite-dimensionality and enables a notion of categorical trace. Compact closed categories are the setting for categorical quantum mechanics and linear logic, providing semantics where the internal logic mirrors the monoidal structure.

## How It's Best Learned
Study FinVect (finite-dimensional vector spaces) with the standard dual construction. Verify triangle identities explicitly and compute traces via the dimension. Explore tangle diagrams and see how string diagrams encode morphisms in compact closed categories.

## Common Misconceptions
Compactness here refers to algebraic finite-dimensionality, not topological compactness. Duals are not unique—different dual constructions can coexist on the same category. The condition requires very specific adjoint-like relationships; failure of triangle identities indicates absence of the compact closed structure.

## Explainer

You already know that a **monoidal category** equips a category with a tensor product ⊗ and a unit object I, and that a **symmetric monoidal category** adds a natural isomorphism that swaps the two factors: X ⊗ Y ≅ Y ⊗ X. Compact closed categories go one step further: they add the ability to "bend" morphisms by equipping every object with a **dual**. The intuition comes directly from finite-dimensional vector spaces. If V is a finite-dimensional vector space with basis {e₁, ..., eₙ}, then V* is the dual space with dual basis {e₁*, ..., eₙ*}. There is a canonical evaluation map ε: V* ⊗ V → k (the field) and a coevaluation map η: k → V ⊗ V*, both of which are well-defined and satisfy "snake" or **triangle identities**: going from V to V ⊗ V* ⊗ V back to V via η and ε gives the identity on V.

These triangle identities are the algebraic heart of the compact closed structure. They say that the unit η and counit ε of the dual pair compose correctly, analogously to the unit-counit conditions in an adjunction. In fact, a compact closed category can be understood as a symmetric monoidal category where every object has a two-sided adjoint under ⊗ — dual objects are simultaneously left and right adjoints of each other with respect to the tensor product. The existence of both evaluation and coevaluation (not just one direction) is what distinguishes compact closed categories from more general closed categories.

The payoff is a powerful graphical calculus. In a compact closed category, every morphism f: A → B can be represented as a diagram with input and output wires, and wires can be bent: by using the coevaluation η you can "curl" an input wire around to become an output wire of the dual type, and vice versa using ε. This **string diagram** notation lets you reason about complex compositions visually without tracking indices or elements. The triangle identities become the statement that a wire bent into a U and then straightened out is the same as an unbent wire. This diagrammatic language is used heavily in categorical quantum mechanics, where it encodes quantum teleportation, entanglement, and other quantum information protocols as topological manipulations of string diagrams.

The canonical example is **FinVect_k**, the category of finite-dimensional vector spaces over a field k. The tensor product is the usual tensor product of vector spaces, and the dual X* of each object X is the dual vector space Hom(X, k). The **categorical trace** defined by the compact closed structure maps an endomorphism f: X → X to an element Tr(f) ∈ k (the unit object): Tr(f) = ε ∘ (f ⊗ id_X*) ∘ η. In FinVect, this recovers the ordinary trace of a linear map. In other compact closed categories, the trace captures analogous "cyclic" information — it is defined in purely categorical terms but specializes to matrix trace, partial trace in quantum mechanics, and other domain-specific notions.

The restriction to finite-dimensional objects is essential. Infinite-dimensional vector spaces do not generally have well-behaved duals in this strong sense — the evaluation and coevaluation fail to satisfy the triangle identities for infinite-dimensional spaces in the way they do for finite-dimensional ones. This is why compact closed categories are specifically associated with finite-dimensionality, and why they appear as the categorical setting for linear logic (which restricts resource use) and quantum computing (which operates on finite-dimensional Hilbert spaces). The builds-toward topic of dagger categories adds an additional structure — a notion of adjoint for morphisms — that combines with compact closure to model quantum operations more completely.


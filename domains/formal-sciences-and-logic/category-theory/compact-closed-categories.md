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
stage: expert
status: draft
---

# Compact Closed Categories

## Core Idea
A compact closed category is a monoidal category where every object X has a dual object X* with evaluation and coevaluation morphisms satisfying triangle identities. This categorical structure captures finite-dimensionality and enables a notion of categorical trace. Compact closed categories are the setting for categorical quantum mechanics and linear logic, providing semantics where the internal logic mirrors the monoidal structure.

## Questions

```yaml
- question: "In the compact closed category FinVect_k, what is the dual X* of a vector space X, and what do the evaluation and coevaluation maps do?"
  type: multiple-choice
  options:
    - "X* is the orthogonal complement of X; evaluation and coevaluation define the inner product structure"
    - "X* = Hom(X, k) is the dual vector space; evaluation encodes the pairing X* ⊗ X → k, and coevaluation encodes k → X ⊗ X*, with both satisfying triangle identities"
    - "X* is X itself (every finite-dimensional space is self-dual); evaluation and coevaluation are both the identity morphism"
    - "X* is defined by topological compactness; evaluation maps open sets to closed sets under the duality"
  answer: 1
  explanation: "In FinVect_k, the dual of X is the linear dual Hom(X, k) — linear functionals on X. The evaluation map ε: X* ⊗ X → k sends (f, v) to f(v). The coevaluation map η: k → X ⊗ X* sends 1 to Σᵢ eᵢ ⊗ eᵢ* (the sum over a basis and dual basis). These satisfy the triangle (snake) identities: composing η with ε in the right order recovers the identity on X (and on X*). This structure is the concrete instantiation of compact closure, and the triangle identities are what the abstract definition demands."

- question: "The triangle (snake) identities in a compact closed category express that:"
  type: multiple-choice
  options:
    - "The tensor product is associative and the swap isomorphism is its own inverse"
    - "Composing the coevaluation and evaluation on the appropriate factors yields the identity morphism — a wire bent into a U and then straightened is the same as an unbent wire"
    - "Every object is canonically isomorphic to its double dual via a natural transformation"
    - "The categorical trace of any identity morphism equals the dimension of the tensor unit"
  answer: 1
  explanation: "The triangle identities state: (idX ⊗ ε) ∘ (η ⊗ idX) = idX and (ε ⊗ idX*) ∘ (idX* ⊗ η) = idX*. In string diagram notation, these become the 'snake equations': drawing a coevaluation curve followed by an evaluation curve on the same wire simplifies to a straight wire. This is the fundamental identity that allows wire-bending in the graphical calculus — you can redirect any input wire into an output wire (or vice versa) using the dual structure, and the snake equations guarantee the manipulation is consistent."

- question: "In a compact closed category, every object has a dual, and morphisms can be 'bent' in string diagrams — an input wire of type X can be redirected into an output wire of type X* using the coevaluation map."
  type: true-false
  answer: true
  explanation: "This is the defining feature of compact closed categories and the source of their power in the string diagram calculus. The coevaluation η: I → X ⊗ X* allows a new X-wire and X*-wire to be created from nothing (from the monoidal unit), effectively 'bending' an input into an output. The triangle identities ensure this bending is internally consistent — bending and then straightening leaves the morphism unchanged. This diagrammatic flexibility is what makes compact closed categories the natural setting for quantum information protocols like teleportation."

- question: "The term 'compact' in compact closed categories is related to topological compactness — objects correspond to compact topological spaces, which have finite open cover properties."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about compact closed categories. 'Compact' here is an algebraic notion capturing something like finite-dimensionality — specifically, the existence of well-behaved dual objects with evaluation and coevaluation satisfying triangle identities. It has no relationship to topological compactness (the Heine-Borel property). The connection is to finite-dimensional vector spaces, not to compact topological spaces. The Common Misconceptions section of this topic explicitly flags this confusion."

- question: "Why does the compact closed structure specifically capture finite-dimensionality, and why do infinite-dimensional vector spaces fail to form compact closed categories in the standard sense?"
  type: short-answer
  answer: "The compact closed structure requires evaluation and coevaluation maps satisfying triangle identities. For finite-dimensional vector spaces, the coevaluation η: k → V ⊗ V* can be defined as η(1) = Σᵢ eᵢ ⊗ eᵢ* using any finite basis — this is a well-defined element of V ⊗ V* because the sum is finite. For an infinite-dimensional space, the analogous sum would be an infinite series of simple tensors, which is not an element of V ⊗ V* (the algebraic tensor product). Even using topological tensor products, the resulting maps fail the triangle identities in the required categorical form. The finite basis is essential: without it, the coevaluation cannot be constructed, and the dual pair structure collapses."
  explanation: "This is why compact closed categories appear in finite-dimensional quantum mechanics (finite-dimensional Hilbert spaces) and linear logic (which restricts resource use to prevent infinite accumulation). The 'compact' condition is a categorical way of saying 'there exists a finite basis that lets you build the dual pairing.' Infinite-dimensional spaces require much more careful treatment — they can have duals in weaker senses (conjugate-linear duals, continuous duals), but these do not satisfy the strict compact closed conditions."
```

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


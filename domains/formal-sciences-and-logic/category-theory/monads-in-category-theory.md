---
id: monads-in-category-theory
title: Monads in Category Theory
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjunction-unit-and-counit
  type: hard
- id: functor-categories
  type: soft
- id: lambda-calculus
  type: soft
- id: composition-of-functions
  type: soft
- id: binary-operations-and-algebraic-structures
  type: soft
builds-toward:
- algebras-over-a-monad
tags:
- monad
- unit
- multiplication
- Kleisli category
- monad laws
stage: advanced
status: validated
---

# Monads in Category Theory

## Core Idea
A monad on a category C is a functor T: C → C together with two natural transformations: unit η: Id_C ⇒ T and multiplication μ: T∘T ⇒ T, satisfying associativity and unit laws analogous to those of a monoid (μ∘Tμ = μ∘μT and μ∘Tη = id_T = μ∘ηT). Every adjunction F ⊣ G gives a monad T = G∘F; conversely, every monad arises from an adjunction in (at least) two canonical ways via the Kleisli and Eilenberg-Moore categories. Monads appear throughout mathematics (algebras, closure operators) and computer science (sequencing effects in functional programming).

## How It's Best Learned
Derive the monad T = U∘F from the free-forgetful adjunction for groups: T(S) = underlying set of the free group on S. Identify the unit (inclusion of S into T(S)) and multiplication (the group homomorphism μ_S: T(T(S)) → T(S) given by the universal property). Verify the monad laws.

## Common Misconceptions
- Monads in category theory are not the same as Haskell monads, though Haskell's Monad typeclass is directly inspired by them.
- The monad laws are not trivially satisfied by any endofunctor with a unit and multiplication; they must be verified.
- Not every endofunctor is a monad; the additional structure and coherence conditions are essential.

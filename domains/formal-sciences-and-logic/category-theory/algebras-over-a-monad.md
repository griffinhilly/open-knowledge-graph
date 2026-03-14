---
id: algebras-over-a-monad
title: Algebras over a Monad
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: monads-in-category-theory
  type: hard
- id: adjoint-functors
  type: soft
tags:
- Eilenberg-Moore algebra
- T-algebra
- Kleisli category
- monad
- free algebra
stage: advanced
status: validated
---

# Algebras over a Monad

## Core Idea
Given a monad (T, η, μ) on C, a T-algebra (Eilenberg-Moore algebra) is an object A together with a morphism α: T(A) → A satisfying α∘η_A = id_A and α∘μ_A = α∘T(α). T-algebras and their homomorphisms form the Eilenberg-Moore category C^T, which is the 'semantic' category of structures defined by the monad. The Kleisli category C_T has the same objects as C but morphisms A → B are morphisms A → T(B) in C, capturing computational effects: a morphism in the Kleisli category is a computation returning a B-value with effects tracked by T.

## How It's Best Learned
Show that T-algebras for the list monad on Set are exactly monoids. Verify the T-algebra axioms correspond to associativity and unit laws for the monoid operation. Then identify the Kleisli category for the maybe monad as the category of partial functions.

## Common Misconceptions
- The Eilenberg-Moore and Kleisli categories for the same monad are generally not equivalent; they sit at opposite extremes of a factorization.
- Not every algebra over a monad is a free algebra; free algebras are T(A) with structure map μ_A, but there are many non-free T-algebras.
- The Kleisli composition (Kleisli triple) is not ordinary composition; the bind operation encodes how effects compose.

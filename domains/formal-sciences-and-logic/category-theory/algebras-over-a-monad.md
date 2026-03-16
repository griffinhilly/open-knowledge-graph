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
- Not every algebra over a free algebra; free algebras are T(A) with structure map μ_A, but there are many non-free T-algebras.
- The Kleisli composition (Kleisli triple) is not ordinary composition; the bind operation encodes how effects compose.

## Explainer

From your study of monads, you know that a monad (T, η, μ) on a category C packages a unit η: Id → T and a multiplication μ: T² → T satisfying coherence laws that look like a monoid in the category of endofunctors. A natural question is: what does it mean for an object to "be acted on" by T coherently? This is precisely what a **T-algebra** captures — it is the structure that says "T can deposit its contents into this object in a compatible way."

Concretely, a **T-algebra** (or Eilenberg-Moore algebra) is a pair (A, α) where A is an object of C and α: T(A) → A is a morphism — the **structure map** — satisfying two axioms. The **unit axiom** α ∘ η_A = id_A says that the unit inclusion η_A: A → T(A) is a section of α: if you inject A into T(A) via the unit and then apply the structure map, you get back where you started. The **associativity axiom** α ∘ μ_A = α ∘ T(α) says that folding a nested T(T(A)) down to A gives the same result whether you first flatten T² to T (using μ) and then apply α, or whether you first apply α inside T and then apply α again. These two axioms are the algebra laws dressed in categorical clothing.

The canonical example clarifies everything. Take the **list monad** on Set, where T(A) = the set of finite lists over A, η_A maps each element to its singleton list, and μ_A concatenates a list of lists. A T-algebra is then a set A with a map α: List(A) → A. The unit axiom requires α([a]) = a — the operation on a singleton list returns the element itself. The associativity axiom requires that flattening a nested list before applying α equals applying α twice — once inside, once outside. This is exactly the definition of a **monoid**: associativity and unit for a binary operation generalized to arbitrary arities. So list-monad algebras on Set are precisely monoids; the monad has "encoded" the equational theory of monoids, and T-algebras are the models of that theory.

The **Eilenberg-Moore category** C^T has T-algebras as objects and **algebra homomorphisms** as morphisms: a morphism from (A, α) to (B, β) is a morphism f: A → B in C such that f ∘ α = β ∘ T(f) — meaning f commutes with the T-action on both sides. This is the "semantic" category: it contains all models of the algebraic theory encoded by T. At the other extreme sits the **Kleisli category** C_T, whose objects are the same as C but whose morphisms A → B are morphisms A → T(B) in C — computations that produce a B-value wrapped in T-effects. Kleisli composition (the bind/flatMap operation) sequences these effectful computations by composing them through μ. These two categories sit at opposite ends of a canonical factorization of the monad's adjunction: the free-forgetful adjunction factoring through C_T gives the "minimal" factorization, while C^T gives the "maximal" one.

An important subtlety your misconceptions note points to: not every T-algebra is free. The **free T-algebra** on an object A is (T(A), μ_A) — the algebra you get by applying T once and then folding with the multiplication. Free algebras are the "syntactic" objects, containing formal expressions. A non-free algebra like a specific monoid (the integers under addition, say, as a list-monad algebra) is a "semantic" quotient — it imposes additional equations beyond what T itself requires. The relationship between free and non-free algebras mirrors the relationship between syntax and semantics in logic, and the adjunction between C and C^T encodes exactly this syntax-semantics duality: the left adjoint builds free algebras (syntax), the right adjoint forgets the T-structure (extracts the underlying set), and the unit η is the inclusion of generators into their free algebra.

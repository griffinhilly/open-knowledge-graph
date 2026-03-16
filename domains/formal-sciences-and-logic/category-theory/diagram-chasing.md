---
id: diagram-chasing
title: Diagram Chasing and Commutative Diagrams
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
builds-toward:
- exact-sequences
- snake-lemma
- natural-isomorphisms
tags:
- proof-technique
- reasoning
- homological-algebra
stage: advanced
status: draft
---

# Diagram Chasing and Commutative Diagrams

## Core Idea
Diagram chasing is a proof technique using commutative diagrams: proving statements by composing morphisms along paths and verifying they commute. In abelian categories, it allows element-like reasoning despite working purely with morphisms. Chasing along paths captures logical deductions about morphism composition.

## Explainer

You already know what categories and morphisms are — objects connected by arrows that compose associatively with identity arrows at every object. A **commutative diagram** is simply a picture of a category (or a functor's image) where the assertion is: any two paths between the same pair of objects, composed along their arrows, give the same morphism. For example, if there are arrows f: A → B, g: B → D, and h: A → C, k: C → D, then the square "commutes" if g ∘ f = k ∘ h. The diagram is a visual encoding of equational constraints on morphisms.

**Diagram chasing** is the proof technique that exploits commutativity to deduce new facts. The idea is simple: you want to show that some morphism has a certain property (is zero, is an isomorphism, is unique, etc.). You start at a known object and "chase" across the diagram by substituting one path for another using commutativity, applying hypotheses about specific morphisms as you go. In abelian categories (like the category of abelian groups, or R-modules), you can reason about elements explicitly — an element x in object A can be "chased" through a morphism f to land at f(x) in B, then through g to reach g(f(x)) = (g∘f)(x) in D. The commutativity constraint then says this is the same as k(h(x)). By following the element x along every available path, you uncover what constraints the diagram imposes.

The technique becomes powerful for proving structural theorems in homological algebra. The **five lemma** and the **snake lemma** (which you'll encounter soon) are proved entirely by diagram chasing: assume some maps are isomorphisms or have trivial kernel, then chase elements through the commutative squares to show other maps must also be isomorphisms or have some property. The argument always has the same shape: take an element with some property in one object, chase it along one path to land somewhere, chase it along another path to land somewhere else, use commutativity to equate the two, use injectivity or surjectivity of specific maps to conclude it must be zero or have a preimage.

What makes diagram chasing elegant is that it works purely from the categorical structure — the names of the objects don't matter, only the arrows and their commutativity relations. In an arbitrary abelian category, you cannot literally "pick an element" (there may be no underlying sets), but a theorem by Mitchell (the **Freyd-Mitchell embedding theorem**) guarantees that any small abelian category can be fully faithfully embedded into a category of modules, so element-style arguments remain valid. In practice, most chasing proofs in algebraic topology, homological algebra, and algebraic geometry are written informally in terms of elements, with the understanding that the argument is really a morphism-level statement in the underlying category.

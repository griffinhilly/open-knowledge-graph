---
id: pullbacks-and-pushouts
title: Pullbacks and Pushouts
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: limits-and-colimits
  type: hard
- id: products-and-coproducts
  type: soft
builds-toward:
- adjoint-functors
tags:
- pullback
- pushout
- fiber product
- amalgamation
- span
- cospan
stage: advanced
status: validated
---

# Pullbacks and Pushouts

## Core Idea
A pullback of morphisms f: A → C and g: B → C is a limit of the cospan diagram A → C ← B: an object P with morphisms to A and B making a commutative square, universal with this property. The pushout is the colimit of the span A ← C → B. In Set, the pullback is {(a,b) ∈ A×B | f(a) = g(b)} (fiber product), and the pushout is the coproduct A+B quotiented by the relation f(c) ~ g(c). Pullbacks model intersection, preimage, and change of base; pushouts model amalgamation, gluing, and quotients.

## How It's Best Learned
Compute pullbacks explicitly in Set for a concrete choice of f and g: take f: {1,2,3} → {a,b} and g: {x,y} → {a,b} and construct the pullback set. Then dualize to understand pushouts by gluing topological spaces along a common subspace.

## Common Misconceptions
- A pullback square is not just any commutative square; the universal property is essential.
- Pullbacks and intersections coincide in Set only when A and B are subsets of C with f and g being inclusions.
- Pushouts in Top are colimits in the category of topological spaces, which involves a specific topology on the pushout set.

## Explainer

From limits and colimits, you know the general pattern: a limit of a diagram is a universal object with maps into all parts of the diagram that commute with the diagram's morphisms, while a colimit is the dual — a universal object with maps out. Pullbacks and pushouts are the special cases for diagrams shaped like a cospan (two arrows into a common target) and a span (two arrows out of a common source), respectively. They are the most concrete and frequently encountered examples of limits and colimits in mathematics.

The **pullback** of f: A → C and g: B → C is a limit of the cospan A →^f C ←^g B. It is an object P together with morphisms p₁: P → A and p₂: P → B such that f∘p₁ = g∘p₂ (the square commutes), and any other object Q with maps to A and B satisfying this commutativity factors uniquely through P. In Set, the pullback is the **fiber product**: P = A ×_C B = {(a, b) ∈ A × B | f(a) = g(b)}. The maps p₁ and p₂ are the projections. Concretely: if f: Students → Courses maps each student to their enrolled course, and g: Grades → Courses maps each grade record to its course, then the pullback is the set of (student, grade) pairs in the same course — the natural join in database terms. The fiber product operation matches things up over a common target.

The **pushout** of f: C → A and g: C → B is a colimit of the span A ←^f C →^g B. It is an object Q with maps i₁: A → Q and i₂: B → Q such that i₁∘f = i₂∘g, universal with this property. In Set, the pushout is the **amalgamation**: Q = (A ⊔ B) / ~, where ~ identifies f(c) ~ g(c) for each c ∈ C. You glue A and B together by identifying each image of C in A with the corresponding image in C in B. In topology, this is exactly how you construct spaces by gluing: to attach a disk D² to a circle S¹ along the boundary ∂D² ≅ S¹, you take the pushout of ∂D² → D² and ∂D² → S¹ in Top. The pushout with its quotient topology is the new space with the disk attached.

The dual relationship between pullbacks and pushouts is the categorical mirror of the duality between intersection and union, or between preimage and image. Pullbacks pull structure back along maps (change of base in algebraic geometry, preimage of a sheaf); pushouts push structure forward and glue things together (quotients, amalgamated free products in group theory, adjunction spaces in topology). In any category with a zero object, every kernel is a pullback along the zero map and every cokernel is a pushout along the zero map — connecting these constructions to exact sequences and homological algebra. Recognizing which construction you are dealing with (pullback or pushout, limit or colimit) immediately tells you the universal property you can invoke and the verification strategy you need.

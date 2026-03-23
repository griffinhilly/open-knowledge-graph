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
stage: expert
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

## Questions

```yaml
- question: "In Set, you form the pullback of f: A → C and g: B → C. Which set is the pullback?"
  type: multiple-choice
  options:
    - "A × B — the Cartesian product of A and B"
    - "A ∩ B — the intersection of A and B as subsets of C"
    - "{(a, b) ∈ A × B | f(a) = g(b)} — pairs that agree over C"
    - "A ∪ B — all elements of A and B combined"
  answer: 2
  explanation: "The pullback is the FIBER PRODUCT: it consists of all pairs (a, b) from A × B for which f(a) = g(b) — elements that 'match' over C. This is smaller than A × B (which ignores f and g entirely). Option B (A ∩ B) only gives the fiber product in the special case where A and B are both subsets of C with f and g being inclusion maps. The fiber product naturally models database joins: pairs of records related through a common foreign key."

- question: "A commutative square P → A, P → B, A → C, B → C satisfies f∘p₁ = g∘p₂. Is P necessarily the pullback of f and g?"
  type: multiple-choice
  options:
    - "Yes — any commutative square over f and g is a pullback by definition"
    - "No — P is the pullback only if it also has the universal property: any other commutative cone Q factors uniquely through P"
    - "Yes — in Set, every commutative square is automatically a pullback"
    - "No — P is the pullback only if the square is also a pushout"
  answer: 1
  explanation: "Commutativity is necessary but NOT sufficient for a pullback. The pullback requires the UNIVERSAL PROPERTY: P must be the 'most efficient' solution — every other commutative cone over the cospan must factor uniquely through P. For example, any proper subset of the actual fiber product with restricted maps forms a commutative square but fails the universal property because some Q cannot factor through it. This is the most common misconception about pullbacks."

- question: "The pushout in topology allows you to build new spaces by gluing two spaces along a common subspace, and the resulting space carries the quotient topology."
  type: true-false
  answer: true
  explanation: "The pushout in Top of the cospan B ←^f C →^g A is exactly the gluing construction: take the disjoint union B ⊔ A and quotient by identifying f(c) ~ g(c) for each c ∈ C. The quotient topology on this set is precisely the topology that makes it the pushout in the category of topological spaces — continuous maps out of the pushout correspond bijectively to pairs of continuous maps out of A and B that agree on C. Attaching a disk to a circle along its boundary is the canonical example."

- question: "Pullbacks and pushouts are categorically dual, so reversing all arrows in any specific pullback square in a category always yields a valid pushout square in that same category."
  type: true-false
  answer: false
  explanation: "Pullbacks and pushouts are categorically dual — the definition of one is obtained by reversing all arrows in the other. But duality is a statement about the RELATIONSHIP BETWEEN DEFINITIONS across all categories, not a guarantee that reversing a specific diagram in a specific category produces the dual construction in that same category. In Set, the pullback and pushout of the same data are generally different sets. A diagram that is a pullback square will not in general be a pushout square in the same category."

- question: "Explain the universal property of a pullback and why a commutative square alone is not sufficient to define one."
  type: short-answer
  answer: "A pullback of f: A → C and g: B → C is an object P with morphisms p₁: P → A and p₂: P → B satisfying f∘p₁ = g∘p₂ (commutativity), PLUS the universal property: for any other object Q with morphisms q₁: Q → A and q₂: Q → B satisfying f∘q₁ = g∘q₂, there exists a UNIQUE morphism h: Q → P such that p₁∘h = q₁ and p₂∘h = q₂. Commutativity alone is insufficient because many objects can complete a commutative square — the pullback is the unique one through which all others factor uniquely. It is the 'tightest' completion of the cospan."
  explanation: "The universal property encodes the pullback as the categorical intersection — it captures exactly the information common to A and B over C, no more and no less. Any 'larger' commutative completion (like all of A × B) fails the universal property because the factoring map is not unique. Any 'smaller' subobject fails because some Q cannot factor through it."
```

## Explainer

From limits and colimits, you know the general pattern: a limit of a diagram is a universal object with maps into all parts of the diagram that commute with the diagram's morphisms, while a colimit is the dual — a universal object with maps out. Pullbacks and pushouts are the special cases for diagrams shaped like a cospan (two arrows into a common target) and a span (two arrows out of a common source), respectively. They are the most concrete and frequently encountered examples of limits and colimits in mathematics.

The **pullback** of f: A → C and g: B → C is a limit of the cospan A →^f C ←^g B. It is an object P together with morphisms p₁: P → A and p₂: P → B such that f∘p₁ = g∘p₂ (the square commutes), and any other object Q with maps to A and B satisfying this commutativity factors uniquely through P. In Set, the pullback is the **fiber product**: P = A ×_C B = {(a, b) ∈ A × B | f(a) = g(b)}. The maps p₁ and p₂ are the projections. Concretely: if f: Students → Courses maps each student to their enrolled course, and g: Grades → Courses maps each grade record to its course, then the pullback is the set of (student, grade) pairs in the same course — the natural join in database terms. The fiber product operation matches things up over a common target.

The **pushout** of f: C → A and g: C → B is a colimit of the span A ←^f C →^g B. It is an object Q with maps i₁: A → Q and i₂: B → Q such that i₁∘f = i₂∘g, universal with this property. In Set, the pushout is the **amalgamation**: Q = (A ⊔ B) / ~, where ~ identifies f(c) ~ g(c) for each c ∈ C. You glue A and B together by identifying each image of C in A with the corresponding image in C in B. In topology, this is exactly how you construct spaces by gluing: to attach a disk D² to a circle S¹ along the boundary ∂D² ≅ S¹, you take the pushout of ∂D² → D² and ∂D² → S¹ in Top. The pushout with its quotient topology is the new space with the disk attached.

The dual relationship between pullbacks and pushouts is the categorical mirror of the duality between intersection and union, or between preimage and image. Pullbacks pull structure back along maps (change of base in algebraic geometry, preimage of a sheaf); pushouts push structure forward and glue things together (quotients, amalgamated free products in group theory, adjunction spaces in topology). In any category with a zero object, every kernel is a pullback along the zero map and every cokernel is a pushout along the zero map — connecting these constructions to exact sequences and homological algebra. Recognizing which construction you are dealing with (pullback or pushout, limit or colimit) immediately tells you the universal property you can invoke and the verification strategy you need.

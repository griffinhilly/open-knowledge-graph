---
id: limits-and-colimits
title: Limits and Colimits
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: products-and-coproducts
  type: hard
- id: equalizers-and-coequalizers
  type: hard
- id: functor-categories
  type: soft
- id: natural-transformations
  type: soft
- id: comma-categories
  type: soft
- id: set-fundamentals
  type: soft
- id: functions-and-function-properties
  type: soft
- id: set-operations
  type: soft
- id: partial-orders
  type: soft
builds-toward:
- pullbacks-and-pushouts
- adjoint-functors
- yoneda-lemma
tags:
- limit
- colimit
- cone
- cocone
- diagram
- completeness
stage: advanced
status: validated
---
# Limits and Colimits

## Core Idea
A limit of a diagram (functor) D: J → C is a terminal cone over D: an object L with morphisms to each D(j) compatible with the diagram, such that any other cone factors uniquely through L. Colimits are dual: initial cocones. Limits generalize products, equalizers, and pullbacks; colimits generalize coproducts, coequalizers, and pushouts. A category is complete if it has all small limits, and cocomplete if it has all small colimits; most categories arising in practice (Set, Grp, Top, Ab) are both complete and cocomplete.

## How It's Best Learned
Unify previously studied constructions: verify that products are limits over a discrete two-object diagram, equalizers are limits over a diagram with two parallel arrows, and terminal objects are limits over the empty diagram. Dually identify coproducts, coequalizers, and initial objects as colimits.

## Common Misconceptions
- Limits are not the same as limits of sequences in analysis, though filtered colimits capture directed limits of sequences in suitable categories.
- A limit is not just 'the smallest' object fitting a diagram; the universal property (unique factorization) is essential.
- Limits and colimits may fail to exist in a given category, and completeness must be verified, not assumed.

## Questions

```yaml
- question: "The universal property of a limit L over a diagram D: J → C says that for any other cone (N, f) over D:"
  type: multiple-choice
  options:
    - "There exists at least one morphism from N to L compatible with the cone morphisms"
    - "L is the smallest object in C that receives morphisms from every object in the image of D"
    - "There exists a unique morphism from N to L that commutes with all the cone morphisms to D(j)"
    - "There exists a unique morphism from L to N that commutes with all the cone morphisms to D(j)"
  answer: 2
  explanation: "The limit is a terminal cone: any other cone N must factor through L via a *unique* morphism N → L making all the relevant triangles commute. Option A is too weak (merely 'at least one' omits the essential uniqueness). Option B is the 'smallest object' misconception — size has no direct role; uniqueness of factorization is what matters. Option D reverses the direction."

- question: "The limit of a diagram is the smallest object that maps to every node in the diagram."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about limits. The limit is not characterized by size but by the universal property: every other cone factors through it *uniquely*. There may be many objects that map to all nodes; what makes the limit special is the unique factorization, not minimality. Trying to think of limits as 'smallest' breaks down quickly — in Set, the product A×B is not 'small' in any obvious sense, but it is the limit of the two-object discrete diagram."

- question: "How does the Cartesian product A × B of two sets arise as a limit in the category Set?"
  type: short-answer
  answer: "Consider the discrete index category J with two objects and no non-identity morphisms, and the diagram D: J → Set sending the two objects to A and B respectively. A cone over D is a set C equipped with functions f: C → A and g: C → B. The limit is the terminal such cone: the set A × B with projections π₁: A×B → A and π₂: A×B → B, such that any C with maps to A and B factors uniquely through A×B via the pairing ⟨f, g⟩."
  explanation: "The key is recognizing that 'maps to both A and B consistently' is exactly what pairs (a, b) capture. The universal property says A×B is the most economical such object: every cone C → A, C → B compresses uniquely into a map C → A×B. This pattern generalizes to any diagram shape: the limit is always the 'most efficient' cone."
```

## Explainer

You have already studied products, equalizers, pullbacks, terminal objects, and their colimit duals. Limits and colimits are the unifying concept behind all of them: they are the right way to say "an object that fits a diagram in the most efficient possible way."

A diagram in a category C is just a functor D: J → C, where J is a small index category encoding the shape of the diagram. For products, J has two objects and no arrows other than identities. For equalizers, J has two objects and two parallel arrows. For pullbacks, J is a cospan shape. The limit of D is a terminal cone over D: an object L together with morphisms L → D(j) for each object j of J, satisfying all the commutativity conditions imposed by J's arrows, and such that any other such cone N → D(j) factors through L via a unique morphism N → L. This unique factorization is the whole content of the universal property — it is not a minimality condition but a *uniqueness* condition.

Colimits are the exact dual. A cocone under D is an object Q with morphisms D(j) → Q compatible with the diagram. The colimit is the initial cocone: every other cocone factors through it uniquely. Coproducts are colimits over discrete two-object diagrams; coequalizers are colimits of two-parallel-arrow diagrams; pushouts are colimits of span diagrams.

Be careful not to confuse categorical limits with analytic limits of sequences. They are conceptually related only in the sense that both describe "convergence to a universal object" — filtered colimits in suitable categories do recover directed limits of sequences, but this is a special case. In general, categorical limits exist in many categories that have no analytic content at all, such as categories of groups or partial orders.

A category is called complete if every small diagram has a limit, and cocomplete if every small diagram has a colimit. Most familiar categories — Set, Ab, Grp, Top, and R-Mod for any ring R — are both complete and cocomplete. This is not automatic, however: the category of finitely generated abelian groups, for instance, fails to have all small limits. Completeness is a genuine structural property, and verifying it is one of the first things you check when working with a new category.

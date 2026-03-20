---
id: commutative-diagrams-and-composition
title: Commutative Diagrams and Composition
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: categories-and-morphisms
  type: hard
builds-toward:
- diagram-chasing-lemmas
- natural-transformations
tags:
- diagrams
- composition
- fundamentals
stage: advanced
status: draft
---

# Commutative Diagrams and Composition

## Core Idea
Commutative diagrams are the primary visual language of category theory, where paths between objects represent compositions of morphisms. A diagram commutes when different paths between the same objects have equal compositions, a principle that underlies almost all categorical reasoning. Understanding how to read, construct, and verify commutativity is essential for any categorical argument.

## How It's Best Learned
Begin with simple two-object, two-path diagrams and verify commutativity by hand. Graduate to three- and four-object diagrams. Practice translating prose proofs into diagram form and vice versa.

## Common Misconceptions
Students often think commutativity means all paths are equal; it only means designated paths are equal. Another confusion: a diagram need not be 'rectangular'—any shape of commutative diagram is valid.

## Explainer

From your study of categories and morphisms, you know that a category consists of objects, morphisms, a composition rule, and identity morphisms. The composite of f: A → B and g: B → C is written g∘f: A → C. A **commutative diagram** is simply a drawing of this structure: nodes represent objects, directed edges represent morphisms, and the diagram encodes an equality claim. The diagram **commutes** when every pair of directed paths with the same source and target produces the same composite morphism.

The simplest example is a triangle: three objects A, B, C with morphisms f: A → B, g: B → C, and h: A → C. The triangle commutes if h = g∘f. You trace the two paths from A to C — either go directly via h, or go through B via f then g — and check they are equal. That equality is the entire content of commutativity. A square with objects A, B, C, D and morphisms f: A → B, g: B → D, h: A → C, k: C → D commutes if g∘f = k∘h: going right-then-down equals going down-then-right.

The power of commutative diagrams is that they turn equality statements into geometry. A prose proof might say "the composite of these five morphisms equals the composite of those four" — a diagram makes this immediately visible and checkable by eye. When you encounter the phrase "the following diagram commutes" in a theorem or definition, it is asserting a specific equality between compositions of the labeled morphisms. Reading the diagram correctly means identifying all the paths between each pair of objects and confirming the equality claimed.

Note carefully: commutativity is **not** a global property of a diagram saying all morphisms are somehow the same. Two morphisms f, g: A → B are generally distinct. A diagram specifies particular morphisms along particular edges, and commutativity is the assertion that certain pairs of paths are equal — only those paths, not all paths. Different diagrams in the same category assert different equalities. This is why diagrams can encode definitions (a diagram that commutes *by construction*, defining a universal property) and theorems (a diagram one proves commutes from other axioms). Diagram chasing — your next topic — builds on this by proving that if certain sub-diagrams commute, other diagrams in the same figure must also commute, enabling chain-of-equality arguments that would be cumbersome in pure notation.

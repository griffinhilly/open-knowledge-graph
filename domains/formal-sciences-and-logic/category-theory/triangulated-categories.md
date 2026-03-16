---
id: triangulated-categories
title: Triangulated Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: chain-complexes-exact-sequences
  type: hard
- id: homology-and-cohomology
  type: hard
builds-toward:
- derived-equivalences
tags:
- triangulated
- distinguished-triangle
- long-exact-sequence
- derived-category
stage: advanced
status: draft
---

# Triangulated Categories

## Core Idea
A triangulated category is an additive category with a suspension functor and a distinguished collection of triangles satisfying four axioms (octahedral axiom and shift closure). Distinguished triangles behave like short exact sequences: they give rise to long exact sequences in homology and encode the composition structure of derived categories. Triangulated categories abstract the essential homological properties common to derived categories, homology, and cohomology theories.

## How It's Best Learned
Study the derived category D(R) of an abelian category, verifying that distinguished triangles come from short exact sequences in the derived category. Compute long exact sequences from triangles. Verify the octahedral axiom in concrete examples.

## Common Misconceptions
Triangulated categories are subtle; the axioms are more complex than they initially appear. Not every category that looks homological is triangulated—the axioms are necessary and restrictive. The octahedral axiom is deep and its necessity is not obvious; failure to satisfy it indicates missing triangulated structure.

## Explainer

From your work with chain complexes and exact sequences, you know that a short exact sequence 0 → A → B → C → 0 encodes how B is built from A and C — A is a sub-object and C is its quotient. Short exact sequences generate long exact sequences in homology, one of the most computationally powerful tools in algebra. Triangulated categories are the setting where this structure is abstracted to contexts where "sub-object" and "quotient" may not even make sense.

The central object is the **distinguished triangle**: A → B → C → ΣA, where Σ is the **suspension functor** shifting a complex up by one degree. Think of this as a categorification of a short exact sequence: A maps into B, B maps to a "cofiber" C (the categorical quotient that replaces the cokernel), and then C maps to ΣA, closing the sequence into a triangle. The triangle is "distinguished" not because of any topological meaning, but because it belongs to the specified class of triangles satisfying the triangulated structure axioms. Applying a cohomological functor H^n to a distinguished triangle generates a long exact sequence — extending in both directions via the suspension — which is the same computational payoff as the long exact sequence from a short exact sequence in an abelian category.

The four axioms constrain how distinguished triangles behave. The first says every morphism f: A → B embeds into a distinguished triangle A → B → C → ΣA (the cofiber C always exists). The second says triangles can be **rotated**: if A → B → C → ΣA is distinguished, so is B → C → ΣA → ΣB. Rotation corresponds to shifting perspective between sub-object, object, and quotient. The third axiom says that morphisms between triangles can be completed (triangles are "functorial" in a suitable sense). These three axioms are relatively intuitive.

The **octahedral axiom** is the deep one. Given composable morphisms f: A → B and g: B → C, the axiom asserts that the cofibers of f, g, and g∘f are themselves related by a distinguished triangle. This says that the "extension" structure is coherent: how B is built from A, how C is built from B, and how C is built directly from A must all fit together compatibly. In the derived category D(𝒜) of an abelian category, this axiom holds because it reflects how filtrations interact. Short exact sequences in 𝒜 give distinguished triangles in D(𝒜), and the octahedral axiom in D(𝒜) follows from the Snake Lemma in 𝒜. The triangulated structure is precisely what allows you to work with Tor and Ext as Hom-sets in D(𝒜), and to define derived equivalences — equivalences of entire derived categories — as the natural notion of "sameness" for categories in homological algebra and algebraic geometry.

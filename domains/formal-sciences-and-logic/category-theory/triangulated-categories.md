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
stage: expert
status: validated
---

# Triangulated Categories

## Core Idea
A triangulated category is an additive category with a suspension functor and a distinguished collection of triangles satisfying four axioms (octahedral axiom and shift closure). Distinguished triangles behave like short exact sequences: they give rise to long exact sequences in homology and encode the composition structure of derived categories. Triangulated categories abstract the essential homological properties common to derived categories, homology, and cohomology theories.

## How It's Best Learned
Study the derived category D(R) of an abelian category, verifying that distinguished triangles come from short exact sequences in the derived category. Compute long exact sequences from triangles. Verify the octahedral axiom in concrete examples.

## Common Misconceptions
Triangulated categories are subtle; the axioms are more complex than they initially appear. Not every category that looks homological is triangulated—the axioms are necessary and restrictive. The octahedral axiom is deep and its necessity is not obvious; failure to satisfy it indicates missing triangulated structure.

## Questions

```yaml
- question: "What is the primary structural role of distinguished triangles in a triangulated category?"
  type: multiple-choice
  options:
    - "They provide a multiplication structure that makes the category into a ring"
    - "They generalize short exact sequences, generating long exact sequences when a cohomological functor is applied"
    - "They replace morphisms with higher-dimensional cells, extending the category to an ∞-category"
    - "They classify all objects up to isomorphism using three canonical invariants"
  answer: 1
  explanation: "In an abelian category, short exact sequences 0 → A → B → C → 0 generate long exact sequences in cohomology. Triangulated categories extend this to settings — like derived categories — where 'sub-object' and 'quotient' may not exist. The distinguished triangle A → B → C → ΣA plays the role of a short exact sequence: applying a cohomological functor H produces the long exact sequence ⋯ → H(A) → H(B) → H(C) → H(ΣA) → ⋯. This computational payoff is the main reason for working in triangulated categories."

- question: "In the derived category D(𝒜) of an abelian category, a short exact sequence 0 → A → B → C → 0 gives rise to which structure?"
  type: multiple-choice
  options:
    - "A direct sum decomposition B ≅ A ⊕ C in D(𝒜)"
    - "A distinguished triangle A → B → C → ΣA in D(𝒜)"
    - "A new abelian category whose objects are the exact sequences themselves"
    - "A chain homotopy equivalence between A⊕C and B"
  answer: 1
  explanation: "Short exact sequences in the abelian category 𝒜 pass to distinguished triangles in D(𝒜). This is the precise way in which the derived category extends abelian homological algebra: exact sequences become triangles, and the long exact sequence in cohomology is recovered from the triangle. If the sequence split (B ≅ A⊕C), the triangle would be split distinguished — but this is a special case, not the general one."

- question: "Rotating a distinguished triangle A → B → C → ΣA generally produces a triangle that is no longer distinguished."
  type: true-false
  answer: false
  explanation: "Rotation is an axiom of triangulated categories. If A → B → C → ΣA is distinguished, then B → C → ΣA → ΣB is also distinguished (and so on by further rotation). Rotation shifts perspective around the triangle — what was B becomes A, what was C becomes B, what was ΣA becomes C — reflecting the symmetry between the roles of sub-object, object, and quotient in the underlying homological structure."

- question: "The octahedral axiom ensures that given composable morphisms f: A → B and g: B → C, the cofibers of f, g, and g∘f fit into a coherent distinguished triangle."
  type: true-false
  answer: true
  explanation: "The octahedral axiom states that if you know how B is built from A (via f), how C is built from B (via g), and how C is built directly from A (via g∘f), the three cofibers — Cone(f), Cone(g), Cone(g∘f) — are themselves related by a distinguished triangle. This coherence condition ensures the triangulated structure is compatible with composition. In D(𝒜), the axiom follows from the Snake Lemma in 𝒜, making it geometrically natural even when it appears formally mysterious."

- question: "Explain how distinguished triangles in a triangulated category serve the same purpose as short exact sequences in an abelian category, and what the cohomological functor provides in this setting."
  type: short-answer
  answer: "In an abelian category, short exact sequences 0→A→B→C→0 encode extension data and generate long exact sequences in any cohomological functor H: ⋯→H^n(A)→H^n(B)→H^n(C)→H^{n+1}(A)→⋯. Triangulated categories generalize this: a distinguished triangle A→B→C→ΣA plays the role of the short exact sequence (C is the 'cofiber' or categorical cokernel of A→B; ΣA is the suspension shifting degree by 1). Applying a cohomological functor H to the triangle produces the same long exact sequence pattern, giving the same computational power even in contexts — like stable homotopy theory or derived categories of sheaves — where sub-objects and quotients do not exist as abelian category objects."
  explanation: "The distinguished triangle is the minimal structure needed to produce long exact sequences. The octahedral axiom then ensures these long exact sequences are compatible when you compose morphisms — the same coherence that the Snake Lemma provides in abelian categories. This is why triangulated categories are the natural setting for derived functors, Tor, Ext, and sheaf cohomology in algebraic geometry."
```

## Explainer

From your work with chain complexes and exact sequences, you know that a short exact sequence 0 → A → B → C → 0 encodes how B is built from A and C — A is a sub-object and C is its quotient. Short exact sequences generate long exact sequences in homology, one of the most computationally powerful tools in algebra. Triangulated categories are the setting where this structure is abstracted to contexts where "sub-object" and "quotient" may not even make sense.

The central object is the **distinguished triangle**: A → B → C → ΣA, where Σ is the **suspension functor** shifting a complex up by one degree. Think of this as a categorification of a short exact sequence: A maps into B, B maps to a "cofiber" C (the categorical quotient that replaces the cokernel), and then C maps to ΣA, closing the sequence into a triangle. The triangle is "distinguished" not because of any topological meaning, but because it belongs to the specified class of triangles satisfying the triangulated structure axioms. Applying a cohomological functor H^n to a distinguished triangle generates a long exact sequence — extending in both directions via the suspension — which is the same computational payoff as the long exact sequence from a short exact sequence in an abelian category.

The four axioms constrain how distinguished triangles behave. The first says every morphism f: A → B embeds into a distinguished triangle A → B → C → ΣA (the cofiber C always exists). The second says triangles can be **rotated**: if A → B → C → ΣA is distinguished, so is B → C → ΣA → ΣB. Rotation corresponds to shifting perspective between sub-object, object, and quotient. The third axiom says that morphisms between triangles can be completed (triangles are "functorial" in a suitable sense). These three axioms are relatively intuitive.

The **octahedral axiom** is the deep one. Given composable morphisms f: A → B and g: B → C, the axiom asserts that the cofibers of f, g, and g∘f are themselves related by a distinguished triangle. This says that the "extension" structure is coherent: how B is built from A, how C is built from B, and how C is built directly from A must all fit together compatibly. In the derived category D(𝒜) of an abelian category, this axiom holds because it reflects how filtrations interact. Short exact sequences in 𝒜 give distinguished triangles in D(𝒜), and the octahedral axiom in D(𝒜) follows from the Snake Lemma in 𝒜. The triangulated structure is precisely what allows you to work with Tor and Ext as Hom-sets in D(𝒜), and to define derived equivalences — equivalences of entire derived categories — as the natural notion of "sameness" for categories in homological algebra and algebraic geometry.

---
id: the-five-lemma
title: The Five Lemma and Related Results
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: exact-sequences-in-abelian-categories
  type: hard
builds-toward:
- diagram-chasing-lemmas
tags:
- homological-algebra
- isomorphism-criteria
- diagram-chasing
stage: abstract-reasoning
status: draft
---

# The Five Lemma and Related Results

## Core Idea
The five lemma states that if two rows of a commutative diagram are exact and four of the five vertical morphisms are isomorphisms, then so is the fifth—providing a powerful criterion for establishing isomorphisms without explicit computation. The short five lemma and related results like the four lemma are equally useful for showing injectivity and surjectivity.

## How It's Best Learned
Begin with the standard five lemma and verify its proof by diagram chasing. Apply it to prove that certain canonical morphisms are isomorphisms. Explore variants: the four lemma, the three lemma, and how they all follow from the same principles.

## Common Misconceptions
The five lemma requires exactness of both rows; without exactness, the conclusion fails. Also, the positioning of the morphisms matters—swapping the roles of exactness and commutativity breaks the result.

## Explainer

From your study of abelian categories and exact sequences, you know that exactness at an object M means im(f) = ker(g) for the morphisms arriving and departing. **Diagram chasing** is the technique of proving facts about morphisms by following elements through a commutative diagram, using exactness conditions to lift, map, and conclude. The **five lemma** is the central theorem of diagram chasing: it converts a local question ("is this morphism an isomorphism?") into a structural question answered by neighboring data.

The setup is a commutative diagram with two exact rows and five vertical morphisms:

A → B → C → D → E
↓α  ↓β  ↓γ  ↓δ  ↓ε
A'→ B'→ C'→ D'→ E'

If α, β, δ, ε are all isomorphisms and both rows are exact, then γ is also an isomorphism. The proof splits into two halves. **Injectivity of γ**: suppose γ(c) = 0. Use commutativity and exactness to push c rightward — δ(image of c in D) = 0, so since δ is injective, the image is 0, meaning c comes from B by exactness. Then push leftward — β's injectivity forces c = 0. **Surjectivity of γ**: given c' ∈ C', push it rightward to D'; since δ is surjective, lift to D; use exactness at D to track it back to C; check that the residual in C' is zero using β's surjectivity. Each half is a short chain of standard moves — map, use commutativity, use exactness, use isomorphism — all following from definitions.

The **short five lemma** is the most frequently applied variant: given 0 → A → B → C → 0 on both rows (short exact sequences), with isomorphisms at A and C, the middle morphism at B is also an isomorphism. This appears constantly whenever two extensions of C by A are compared — if there exists a map of short exact sequences with isomorphisms at both ends, the middle map is automatically an isomorphism, meaning the extensions are equivalent. The **four lemma** weakens the hypothesis further: with only two or three outer isomorphisms, you can still conclude injectivity or surjectivity (but not necessarily both) at the middle position.

The broader significance is methodological. In algebraic topology, algebraic geometry, and homological algebra, you frequently want to show that a natural map between two invariants — a map of homology groups, of cohomology sheaves, of Ext groups — is an isomorphism. Direct computation is rarely available. The five lemma provides a structural route: construct a morphism of long exact sequences, establish isomorphisms at enough positions by independent means, and conclude the remaining isomorphisms by diagram chasing. Long exact sequences in homology (from a pair of spaces), in sheaf cohomology (from a short exact sequence of sheaves), and in derived categories all produce five-lemma situations as a matter of routine. The lemma is the grammar rule; the long exact sequence is the sentence it appears in.

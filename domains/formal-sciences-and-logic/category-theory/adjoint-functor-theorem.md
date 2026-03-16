---
id: adjoint-functor-theorem
title: The General Adjoint Functor Theorem
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: adjoint-functors
  type: hard
- id: limits-and-colimits
  type: hard
builds-toward:
- kan-extensions
- topos-theory-intro
tags:
- adjoint
- theorem
- representability
- preservation
- completeness
stage: advanced
status: draft
---

# The General Adjoint Functor Theorem

## Core Idea
The General Adjoint Functor Theorem states that a functor G: D → C has a left adjoint if and only if G preserves limits and satisfies the solution set condition (roughly: the class of solutions to a lifting problem forms a set). This theorem transforms adjoint existence into verifiable structural properties. It provides a systematic approach to constructing adjoints and is central to existence proofs in algebra and topology.

## How It's Best Learned
Study the proof using the solution set condition and verify its application to familiar functors (forgetful functors, localization). Explore what happens when hypotheses fail and how the theorem guides explicit adjoint construction.

## Common Misconceptions
The solution set condition is subtle and may be difficult to verify directly; sufficient conditions are often used in practice. Adjoint existence is guaranteed but may not yield explicit descriptions of the adjoint. The theorem applies to left adjoints; right adjoints require dual conditions.

## Explainer

From your study of adjoint functors and limits, you know what an adjunction is and what it means for a functor to preserve limits. The General Adjoint Functor Theorem (GAFT) answers a natural question: given a functor G, when does it *have* a left adjoint? Instead of constructing an adjoint directly, the theorem gives checkable conditions on G that guarantee the adjoint exists. This is valuable because in many situations (algebra, topology, logic) you want to know an adjoint exists before you try to describe it explicitly.

The first condition — **G preserves limits** — is necessary by a fundamental theorem of adjunctions: right adjoints always preserve limits. If G fails to preserve some limit, it cannot be a right adjoint to anything, and you need look no further. The deeper reason is that the unit and counit of an adjunction impose constraints that force the right adjoint to commute with limits. When you know G preserves limits (often easy to verify directly — forgetful functors from algebraic categories typically do), you have cleared the necessary hurdle.

The second condition — the **solution set condition** — is subtler. For each object C in C, consider the comma category (C ↓ G): the collection of all morphisms C → G(D) for varying D in D. These represent "all the ways C can map into something in the image of G." For the left adjoint F to exist at C, there must be a **universal** such morphism C → G(F(C)) — the unit of the adjunction. The solution set condition says: there exists a *set* (not a proper class) of objects {D_i} such that every C → G(D) factors through some C → G(D_i). This set controls the "size" of the search for the universal morphism, preventing set-theoretic pathology. Once a solution set exists, a standard construction (taking a limit over the solution set) produces F(C).

In practice, the solution set condition is often satisfied automatically for "small enough" categories or under mild set-theoretic assumptions. For instance, if D is locally small and has all small limits, and if G is accessible (roughly: preserves sufficiently filtered colimits), then the solution set condition follows. The **Special Adjoint Functor Theorem** provides an even simpler criterion for complete well-powered categories with a cogenerating set. These stronger versions reduce "does a left adjoint exist?" to a quick structural check. Examples that illustrate the theorem's power include the free group functor (left adjoint to the forgetful functor from Groups to Sets), the sheafification functor (left adjoint to the inclusion of sheaves into presheaves), and localization in ring theory — in each case, the adjoint's existence follows from the GAFT, even when writing down the adjoint explicitly requires more work.

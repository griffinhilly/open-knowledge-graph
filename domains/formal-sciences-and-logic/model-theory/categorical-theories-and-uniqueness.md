---
id: categorical-theories-and-uniqueness
title: Categorical Theories and Uniqueness of Models
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: elementary-equivalence-indistinguishability
  type: hard
- id: infinite-cardinal-numbers
  type: soft
- id: cardinality-and-countability
  type: soft
builds-toward:
- morleys-uncountable-categoricity
tags:
- κ-categorical
- categoricity spectrum
- uniqueness
- rigid theory
stage: advanced
status: draft
---

# Categorical Theories and Uniqueness of Models

## Core Idea
A complete theory T is κ-categorical if it has exactly one model of cardinality κ up to isomorphism. Categoricity captures that T completely determines model structure at a specific size. The spectrum of cardinalities where a theory is categorical is highly constrained: Morley proved surprising rigidity—if T is categorical in some uncountable κ, it is categorical in all uncountable cardinalities.

## Explainer

From your study of elementary equivalence, you know that two structures can satisfy exactly the same first-order sentences without being isomorphic—think of (ℕ, <) and a non-standard model of arithmetic that agrees with ℕ on every first-order sentence yet contains infinite elements. **κ-categoricity** asks whether there is a cardinality κ at which the theory rules out any such structural variation: if T is κ-categorical, any two models of T with cardinality κ are isomorphic. The theory determines the model uniquely at that size.

The canonical example is **DLO**, the theory of dense linear orders without endpoints—the first-order theory of (ℚ, <). This theory is ℵ₀-categorical: every countable dense linear order without endpoints is isomorphic to ℚ. The proof uses a **back-and-forth argument**, building an isomorphism incrementally by alternately extending it to cover one new element from each structure. Density and the absence of endpoints ensure you can always find an appropriate match. However, DLO is not κ-categorical for any uncountable κ: uncountable dense linear orders can differ in cofinality and whether they are Dedekind complete, producing genuinely non-isomorphic models of the same size.

**Morley's theorem** (1965) reveals a striking rigidity for uncountable categoricity: if a complete theory T in a countable language is categorical in *any* uncountable cardinality, it is categorical in *all* uncountable cardinalities. This was unexpected because uncountable cardinals are wildly diverse in size. The explanation lies in structural properties the theory must possess: it must be **totally transcendental**, must have a well-behaved notion of algebraic independence (generalizing linear independence in vector spaces), and models must be characterized entirely by a single "dimension." The theory of algebraically closed fields of fixed characteristic illustrates this: it is categorical in every uncountable cardinality (and also ℵ₁-categorical, since the algebraic closure of ℚ is countable while uncountable algebraically closed fields of characteristic 0 all look alike at each uncountable size).

Categoricity is ultimately a measure of how tightly a theory pins down structure. A κ-categorical theory leaves no freedom at cardinality κ—it is, in a precise sense, complete about models of that size. Non-categorical theories have multiple non-isomorphic models of the same infinite size, meaning the theory is "weaker" and cannot distinguish between structurally different possibilities. The spectrum of theories ranging from categorical to maximally non-categorical is a central organizing theme of modern model theory, and Morley's theorem is the founding result of that classification program.

---
id: ultraproducts-of-structures
title: Ultraproducts of Structures
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: ultrafilters-in-logic
  type: hard
- id: structure-homomorphisms-embeddings
  type: soft
- id: set-operations
  type: soft
- id: equivalence-relations-and-equivalence-classes
  type: soft
- id: cardinality-and-countability
  type: soft
builds-toward:
- los-theorem-and-preservation
- saturated-models-and-realization
tags:
- ultraproduct
- quotient construction
- diagonal embedding
- direct product
stage: advanced
status: draft
---

# Ultraproducts of Structures

## Core Idea
The ultraproduct ∏ᵤ Mᵢ of a family of structures over an ultrafilter U is constructed as the quotient of the direct product by identifying sequences equal on a U-large set. Ultraproducts preserve first-order properties generically (by Łoś's Theorem). Every complete theory has arbitrarily large saturated models obtained as ultraproducts of finite or smaller models.

## Explainer

You already know what ultrafilters are: ultrafilters on an index set I are maximal consistent collections of "large" subsets, where every subset is either large or its complement is large. You also know what direct products of structures look like and how equivalence classes quotient a set. An **ultraproduct** combines these: start with a family of structures (Mᵢ)_{i ∈ I} all of the same signature, form their direct product (sequences (aᵢ)_{i∈I} with aᵢ ∈ Mᵢ), then identify two sequences if they agree on a U-large index set. The resulting equivalence classes form the domain of the ultraproduct ∏ᵤ Mᵢ.

The key intuition is that the **ultrafilter acts as a voting rule**. A property holds in the ultraproduct if and only if the set of indices where it holds is "large" — belongs to U. Because U is an ultrafilter, every index set is either large or its complement is, so the ultraproduct takes a definite stance on every property. **Łoś's Theorem** (the fundamental theorem of ultraproducts) makes this precise: a first-order sentence φ is true in ∏ᵤ Mᵢ if and only if {i ∈ I : Mᵢ ⊨ φ} ∈ U. First-order truth in the ultraproduct is exactly the "U-majority vote" of truth across the component structures.

The most elegant application is the **non-standard models** construction. Take all structures to be the standard naturals ℕ with a non-principal ultrafilter U on ℕ (one that contains no finite set). The ultrapower ℕ^ℕ/U is a non-standard model of arithmetic: it satisfies every first-order sentence true in ℕ (by Łoś), yet contains "infinitely large" elements — equivalence classes of sequences that grow without bound. The element represented by the sequence (0, 1, 2, 3, ...) is larger than every standard natural number, because for each fixed standard n, the set {i : i > n} is cofinite, hence in any non-principal ultrafilter. This is the ultraproduct proof of the existence of non-standard models of arithmetic, complementing the compactness argument.

Ultraproducts also provide the cleanest proof of the Compactness Theorem. If every finite subset of Σ is satisfiable, pick models Mₙ satisfying the first n sentences of Σ, then form an ultraproduct over a non-principal ultrafilter. By Łoś, each sentence of Σ is satisfied in the ultraproduct because it is satisfied in all but finitely many Mₙ — a cofinite (and therefore large) set. More broadly, ultraproducts let model theorists transfer properties between fields of different characteristic (the **transfer principle** in non-standard analysis), and they are the main technical tool for constructing **saturated models** — structures rich enough to realize every type. Understanding ultraproducts is thus the entry point to advanced model-theoretic methods in algebra, analysis, and combinatorics.

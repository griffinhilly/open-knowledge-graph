---
id: los-theorem-and-preservation
title: Łoś's Theorem and Preservation in Ultraproducts
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: ultraproducts-of-structures
  type: hard
builds-toward:
- categorical-theories-and-uniqueness
tags:
- Łoś's theorem
- preservation
- first-order preservation
- fundamental theorem
stage: advanced
status: draft
---

# Łoś's Theorem and Preservation in Ultraproducts

## Core Idea
Łoś's Theorem states: a formula φ is satisfied in the ultraproduct ∏ᵤ Mᵢ iff it is satisfied in the component structures on a U-large set. This profound statement implies first-order logic is preserved 'generically' under ultraproducts. Łoś's Theorem is the key tool justifying ultraproduct utility and underlies many deep results in model theory.

## Explainer

Recall that an **ultraproduct** ∏_U Mᵢ is built from a family of structures {Mᵢ : i ∈ I} and an ultrafilter U on the index set I. Its elements are equivalence classes of sequences (aᵢ), where two sequences are identified if they agree on a U-large set of indices (a set in the ultrafilter). The ultrafilter captures the notion of "almost all" indices: a property holds almost everywhere if the set of indices where it holds is in U. Łoś's theorem makes this precise for first-order logic.

**Łoś's Theorem** states that a first-order sentence φ is true in ∏_U Mᵢ if and only if {i ∈ I : Mᵢ ⊨ φ} ∈ U — that is, φ holds in the ultraproduct iff it holds in almost all component structures. The proof is by induction on the complexity of φ. The atomic and Boolean cases follow from how the ultraproduct is defined. The crucial step is the quantifier case: ∃x ψ holds in the ultraproduct iff there is an element (aᵢ) such that ψ holds of it almost everywhere, which holds iff almost all Mᵢ satisfy ∃x ψ. The ultrafilter's closure under supersets and intersections ensures that the logic of "almost all" meshes perfectly with the logic of ∧ and ∨.

The most immediate consequence is the **compactness theorem** of first-order logic via ultraproducts. Suppose every finite subset of a theory T has a model. Build a family of models Mᵢ for each finite subset Tᵢ, index by the finite subsets of T, and take an ultrafilter containing all co-finite sets (which exists by the ultrafilter lemma). Łoś's theorem then shows the ultraproduct satisfies every sentence in T, because each sentence φ belongs to almost all Tᵢ. This is a beautiful semantic proof of compactness that avoids the syntactic machinery of Henkin constructions.

Łoś's theorem also governs which properties are *preserved* under ultraproducts. Since ultraproducts preserve all first-order sentences (by the theorem), they are a tool for transferring properties between structures when you know the property is first-order. **Non-standard analysis** exploits this directly: take an ultrapower ∏_U ℝ of the real numbers; by Łoś's theorem, every first-order statement true of ℝ is true of ∗ℝ (the hyperreals), including all of real analysis. The extra elements in ∗ℝ (infinitesimals and infinite numbers) don't violate any first-order property of ℝ — they only differ in higher-order or set-theoretic respects. Łoś's theorem is thus the engine that makes non-standard analysis logically sound.

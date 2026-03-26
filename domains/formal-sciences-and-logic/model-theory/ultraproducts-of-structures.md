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
stage: expert
status: validated
---

# Ultraproducts of Structures

## Core Idea
The ultraproduct ∏ᵤ Mᵢ of a family of structures over an ultrafilter U is constructed as the quotient of the direct product by identifying sequences equal on a U-large set. Ultraproducts preserve first-order properties generically (by Łoś's Theorem). Every complete theory has arbitrarily large saturated models obtained as ultraproducts of finite or smaller models.

## Questions

```yaml
- question: "A non-principal ultrafilter U is fixed on the index set ℕ. For each n ∈ ℕ, let Mₙ be the cyclic group ℤ/nℤ. Which first-order sentence is true in the ultraproduct ∏ᵤ Mₙ?"
  type: multiple-choice
  options:
    - "Every element has finite order, since each Mₙ is finite"
    - "The ultraproduct is the zero ring, because most Mₙ are small"
    - "The sentence 'there exists an element of order > k' holds for every standard k, because for each k the set {n : Mₙ has an element of order > k} is cofinite, hence in U"
    - "No first-order sentence is decidable in the ultraproduct without knowing U explicitly"
  answer: 2
  explanation: "By Łoś's Theorem, φ holds in ∏ᵤ Mₙ iff {n : Mₙ ⊨ φ} ∈ U. For any fixed k, all groups ℤ/nℤ with n > k contain an element of order > k, so the set {n > k} is cofinite. Because U is non-principal, every cofinite set is in U, so the ultraproduct contains elements of order exceeding every standard integer. Option A applies finite reasoning to an infinite construction — Łoś shows the ultraproduct can satisfy properties no individual component satisfies."

- question: "You want to use ultraproducts to prove the Compactness Theorem: if every finite subset of a theory Σ is satisfiable, then Σ is satisfiable. You choose models Mₙ where Mₙ satisfies the first n sentences of Σ, then form ∏ᵤ Mₙ for a non-principal ultrafilter U. Why does each sentence φₖ of Σ hold in the ultraproduct?"
  type: multiple-choice
  options:
    - "Because every Mₙ satisfies φₖ, so the whole index set is in U"
    - "Because Mₙ ⊨ φₖ for all n ≥ k, making the set {n : Mₙ ⊨ φₖ} cofinite, hence in U"
    - "Because the ultraproduct takes a logical average of all models"
    - "Because φₖ is finitely satisfiable, and ultraproducts preserve finite properties"
  answer: 1
  explanation: "By construction, Mₙ ⊨ φₖ for every n ≥ k (since Mₙ satisfies the first n sentences). The set {n : n ≥ k} is cofinite. A non-principal ultrafilter contains every cofinite set, so {n : Mₙ ⊨ φₖ} ∈ U. By Łoś's Theorem, ∏ᵤ Mₙ ⊨ φₖ. Option A would be correct if every Mₙ satisfied φₖ, but Mₙ with n < k may not — only cofiniteness is needed, not universality."

- question: "The ultraproduct ∏ᵤ Mᵢ satisfies a first-order sentence φ if and mainly if more than half the component structures satisfy φ."
  type: true-false
  answer: false
  explanation: "The correct criterion is not majority vote but U-membership: φ holds in the ultraproduct iff {i : Mᵢ ⊨ φ} ∈ U. An ultrafilter is not a counting measure — it does not depend on proportions. A non-principal ultrafilter on ℕ can contain sets with density zero (if every cofinite superset of a set is in U) and can exclude sets with density one if those sets are not in the filter. The voting metaphor is useful but the rule is 'which sets the ultrafilter declares large,' not 'which option gets a numerical majority.'"

- question: "If Mᵢ ⊨ φ for every i ∈ I, then ∏ᵤ Mᵢ ⊨ φ for any ultrafilter U on I."
  type: true-false
  answer: true
  explanation: "If φ holds in every component, then {i : Mᵢ ⊨ φ} = I. Every ultrafilter must contain the whole index set I (it is closed upward and contains the empty set's complement). So by Łoś's Theorem, ∏ᵤ Mᵢ ⊨ φ. This is the simplest case of Łoś and explains why ultraproducts of models of a complete theory are again models of that theory."

- question: "Explain why the ultrafilter's maximality — the fact that for every set A ⊆ I, either A ∈ U or its complement Aᶜ ∈ U — is essential for Łoś's Theorem to work."
  type: short-answer
  answer: "Łoś's Theorem must assign a definite truth value to every first-order sentence in the ultraproduct. For an atomic formula, the ultraproduct satisfies it or it doesn't; there is no middle ground. Maximality ensures that for any index set S = {i : Mᵢ ⊨ φ}, exactly one of S or Sᶜ is in U. If U were merely a filter (not an ultrafilter), some sentences could have S ∉ U and Sᶜ ∉ U simultaneously, leaving the ultraproduct's truth value undefined. Maximality turns the ultrafilter into a complete decision procedure: it takes a definite stance on every subset, which translates into a definite truth value for every first-order sentence."
  explanation: "This is the deepest structural reason ultrafilters (not just filters) are needed. A filter guarantees certain sets are 'large' but may leave many sets undecided. Adding maximality collapses this to a total two-valued measure: every set is either large (in U) or small (complement in U). Łoś's proof uses this at each step of the induction on formula complexity, especially for negations: ¬φ holds in the ultraproduct iff φ does not, which requires the index set for φ and for ¬φ to be complementary with exactly one in U."
```

## Explainer

You already know what ultrafilters are: ultrafilters on an index set I are maximal consistent collections of "large" subsets, where every subset is either large or its complement is large. You also know what direct products of structures look like and how equivalence classes quotient a set. An **ultraproduct** combines these: start with a family of structures (Mᵢ)_{i ∈ I} all of the same signature, form their direct product (sequences (aᵢ)_{i∈I} with aᵢ ∈ Mᵢ), then identify two sequences if they agree on a U-large index set. The resulting equivalence classes form the domain of the ultraproduct ∏ᵤ Mᵢ.

The key intuition is that the **ultrafilter acts as a voting rule**. A property holds in the ultraproduct if and only if the set of indices where it holds is "large" — belongs to U. Because U is an ultrafilter, every index set is either large or its complement is, so the ultraproduct takes a definite stance on every property. **Łoś's Theorem** (the fundamental theorem of ultraproducts) makes this precise: a first-order sentence φ is true in ∏ᵤ Mᵢ if and only if {i ∈ I : Mᵢ ⊨ φ} ∈ U. First-order truth in the ultraproduct is exactly the "U-majority vote" of truth across the component structures.

The most elegant application is the **non-standard models** construction. Take all structures to be the standard naturals ℕ with a non-principal ultrafilter U on ℕ (one that contains no finite set). The ultrapower ℕ^ℕ/U is a non-standard model of arithmetic: it satisfies every first-order sentence true in ℕ (by Łoś), yet contains "infinitely large" elements — equivalence classes of sequences that grow without bound. The element represented by the sequence (0, 1, 2, 3, ...) is larger than every standard natural number, because for each fixed standard n, the set {i : i > n} is cofinite, hence in any non-principal ultrafilter. This is the ultraproduct proof of the existence of non-standard models of arithmetic, complementing the compactness argument.

Ultraproducts also provide the cleanest proof of the Compactness Theorem. If every finite subset of Σ is satisfiable, pick models Mₙ satisfying the first n sentences of Σ, then form an ultraproduct over a non-principal ultrafilter. By Łoś, each sentence of Σ is satisfied in the ultraproduct because it is satisfied in all but finitely many Mₙ — a cofinite (and therefore large) set. More broadly, ultraproducts let model theorists transfer properties between fields of different characteristic (the **transfer principle** in non-standard analysis), and they are the main technical tool for constructing **saturated models** — structures rich enough to realize every type. Understanding ultraproducts is thus the entry point to advanced model-theoretic methods in algebra, analysis, and combinatorics.

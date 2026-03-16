---
id: elementary-substructures-preservation
title: Elementary Substructures and Preservation of Formulas
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-interpretation-and-satisfaction
  type: hard
- id: elementary-equivalence-indistinguishability
  type: hard
builds-toward:
- lowenheim-skolem-theorems-overview
- extensions-back-and-forth-lemma
tags:
- elementary-substructures
- submodels
- preservation
stage: advanced
status: draft
---

# Elementary Substructures and Preservation of Formulas

## Core Idea
A substructure M of N is elementary (M ≺ N) if every first-order formula has the same truth value in M and N under the same variable assignments. Elementary substructures are the model-theoretic notion of submodel, characterized by the tautology method. The Löwenheim-Skolem theorems guarantee existence of elementary submodels of any desired cardinality.

## How It's Best Learned
Use the downward Löwenheim-Skolem theorem to construct elementary submodels. Practice the tautology method for recognizing when substructures are elementary.

## Explainer

You already know what it means for a structure to **satisfy** a first-order formula, and you know that two structures are **elementarily equivalent** if they satisfy exactly the same first-order sentences. Now imagine one structure M is contained inside a larger structure N as a substructure — the universe of M is a subset of N's universe, and the interpretations of all constant symbols, function symbols, and relation symbols agree on M's elements. The question is: can M and N disagree on first-order sentences? In general, yes. But when they cannot, M is called an **elementary substructure** of N, written M ≺ N.

The definition is stronger than just having the same theory. Elementary equivalence (M ≡ N) says the two structures satisfy the same *closed sentences*. Elementary substructure says more: for *every* formula φ(x₁, …, xₙ) and every tuple ā from M, the formula holds of ā in M if and only if it holds of ā in N. The extra content is about formulas with free variables — we need the truth values to match under *all* assignments from M's domain, not just for sentences. Intuitively, M is not just "looking like" N from the outside; M is genuinely an indistinguishable fragment of N from the perspective of first-order logic.

A key example: the integers ℤ with the ordering < are a substructure of the rationals ℚ with <. But ℤ is *not* an elementary substructure of ℚ, because ℚ satisfies "between any two elements there is another element" (a first-order property expressible with an existential quantifier) that ℤ fails — no rational exists strictly between 1 and 2 in ℤ's ordering. By contrast, ℚ *is* an elementary substructure of ℝ with ordering, because both are dense linear orders without endpoints, and the **Tarski-Vaught test** (also called the tautology method) confirms every existential witness in ℝ that touches ℚ-elements can be found in ℚ itself.

The **Tarski-Vaught test** gives a practical criterion: M ≺ N if and only if, for every formula ∃y φ(ā, y) with ā from M, whenever ∃y φ(ā, y) is true in N, there is already an element b ∈ M witnessing it. This is the key to constructing elementary substructures: you start with a set X ⊆ N and close it under "Skolem witnesses" — for every existential formula true in N with parameters from your growing set, add a witness to the set. The closure is elementary in N. This construction underpins the downward Löwenheim-Skolem theorem, which guarantees elementary submodels of any infinite structure of any smaller infinite cardinality.

Elementary substructures matter because they let you reason about large or complex structures by shrinking them to more manageable sizes *without changing the first-order truths*. Any sentence true in a large elementary extension N is already true in the smaller M ≺ N. This means model-theoretic proofs can often be reduced to countable or even finite structures, and that the first-order properties of a structure are shared by an entire family of elementarily equivalent models of varying cardinalities.

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
stage: expert
status: validated
---

# Elementary Substructures and Preservation of Formulas

## Core Idea
A substructure M of N is elementary (M ≺ N) if every first-order formula has the same truth value in M and N under the same variable assignments. Elementary substructures are the model-theoretic notion of submodel, characterized by the tautology method. The Löwenheim-Skolem theorems guarantee existence of elementary submodels of any desired cardinality.

## How It's Best Learned
Use the downward Löwenheim-Skolem theorem to construct elementary submodels. Practice the tautology method for recognizing when substructures are elementary.

## Questions

```yaml
- question: "The integers ℤ are a substructure of the rationals ℚ under the ordering <. Is ℤ an elementary substructure of ℚ?"
  type: multiple-choice
  options:
    - "Yes — ℤ and ℚ are both infinite ordered sets, so they satisfy the same sentences"
    - "No — ℚ satisfies ∃y(1 < y < 2) with witness y = 3/2, but no such element exists in ℤ"
    - "Yes — elementary equivalence between ℤ and ℚ implies ℤ is an elementary substructure"
    - "No — elementary substructures must have the same cardinality as their ambient structure"
  answer: 1
  explanation: "The Tarski-Vaught test requires that every existential formula true in ℚ with parameters from ℤ already has a witness in ℤ. The formula ∃y(1 < y < 2) is true in ℚ (witnessed by 3/2), but no such element exists in ℤ — so the test fails. Note that option C is a common confusion: two structures can be elementarily equivalent (same closed sentences) without either being an elementary substructure of the other, since elementary substructure additionally requires formula agreement for all assignments of free variables from M's domain."

- question: "The Tarski-Vaught test says M ≺ N if and only if, for every formula ∃y φ(ā, y) with ā from M that is true in N, there exists a witness in M. This condition is equivalent to requiring that M and N satisfy the same:"
  type: multiple-choice
  options:
    - "Closed first-order sentences only"
    - "First-order formulas under all variable assignments from M's domain, not just sentences"
    - "Quantifier-free formulas with parameters from M"
    - "Universal sentences — ∀x φ(x) formulas"
  answer: 1
  explanation: "Elementary substructure (M ≺ N) is strictly stronger than elementary equivalence (M ≡ N). Elementary equivalence means the same closed sentences hold; elementary substructure means that for every formula φ(x̄) — including formulas with free variables — and every tuple ā from M, φ(ā) holds in M iff it holds in N. The Tarski-Vaught test is equivalent to this because closing off existential witnesses in N within M is exactly what guarantees formula-agreement for all assignments."

- question: "If M ≺ N (M is an elementary substructure of N), then M and N satisfy exactly the same first-order sentences."
  type: true-false
  answer: true
  explanation: "Elementary substructure implies elementary equivalence. Since every sentence is a formula with no free variables, and M ≺ N requires truth-value agreement for all formulas under all assignments from M, it certainly requires agreement on all closed sentences. The converse fails: elementary equivalence does NOT imply elementary substructure, which requires the stronger condition of formula-agreement for all variable assignments."

- question: "If M ≡ N (M and N are elementarily equivalent) and M is a substructure of N, then M is an elementary substructure of N."
  type: true-false
  answer: false
  explanation: "This is a key misconception. Elementary equivalence (same closed sentences) plus substructure does NOT imply elementary substructure. Elementary substructure additionally requires that for every formula φ(x₁, …, xₙ) with free variables and every tuple ā from M, the formula holds of ā in M iff it holds of ā in N. A counterexample: the integers ℤ and rationals ℚ under ordering are elementarily equivalent (both are dense linear orders without endpoints... actually ℤ is not dense). Better: consider ℝ and a non-archimedean elementary extension — they are elementarily equivalent, but a substructure might fail the Tarski-Vaught test even when the theories agree."

- question: "State the Tarski-Vaught test for elementary substructures and explain why it is equivalent to the definition M ≺ N."
  type: short-answer
  answer: "The Tarski-Vaught test: M ≺ N if and only if for every formula ∃y φ(ā, y) with parameters ā from M, whenever this formula is true in N, there exists b ∈ M with N ⊨ φ(ā, b). This is equivalent to M ≺ N because the only way a formula can be true in N but false in M is if some existential witness needed in N is missing from M. By closing M under Skolem witnesses — adding elements of N that witness existential formulas over current M-parameters — you build an elementary substructure. The test makes the inductive step precise: truth of quantified formulas propagates correctly between M and N exactly when existential witnesses in N can always be found in M."
  explanation: "The Tarski-Vaught test is the practical engine behind the downward Löwenheim-Skolem theorem. Given any infinite structure N and a subset X ⊆ N, you iteratively close X under witnesses: whenever ∃y φ(ā, y) is true in N with ā from the current set, add a witness. The closure is countable if X and the language are countable, and the resulting set is the domain of an elementary substructure M ≺ N. This shows that any infinite structure has an elementary submodel of any infinite cardinality ≥ the language's size."
```

## Explainer

You already know what it means for a structure to **satisfy** a first-order formula, and you know that two structures are **elementarily equivalent** if they satisfy exactly the same first-order sentences. Now imagine one structure M is contained inside a larger structure N as a substructure — the universe of M is a subset of N's universe, and the interpretations of all constant symbols, function symbols, and relation symbols agree on M's elements. The question is: can M and N disagree on first-order sentences? In general, yes. But when they cannot, M is called an **elementary substructure** of N, written M ≺ N.

The definition is stronger than just having the same theory. Elementary equivalence (M ≡ N) says the two structures satisfy the same *closed sentences*. Elementary substructure says more: for *every* formula φ(x₁, …, xₙ) and every tuple ā from M, the formula holds of ā in M if and only if it holds of ā in N. The extra content is about formulas with free variables — we need the truth values to match under *all* assignments from M's domain, not just for sentences. Intuitively, M is not just "looking like" N from the outside; M is genuinely an indistinguishable fragment of N from the perspective of first-order logic.

A key example: the integers ℤ with the ordering < are a substructure of the rationals ℚ with <. But ℤ is *not* an elementary substructure of ℚ, because ℚ satisfies "between any two elements there is another element" (a first-order property expressible with an existential quantifier) that ℤ fails — no rational exists strictly between 1 and 2 in ℤ's ordering. By contrast, ℚ *is* an elementary substructure of ℝ with ordering, because both are dense linear orders without endpoints, and the **Tarski-Vaught test** (also called the tautology method) confirms every existential witness in ℝ that touches ℚ-elements can be found in ℚ itself.

The **Tarski-Vaught test** gives a practical criterion: M ≺ N if and only if, for every formula ∃y φ(ā, y) with ā from M, whenever ∃y φ(ā, y) is true in N, there is already an element b ∈ M witnessing it. This is the key to constructing elementary substructures: you start with a set X ⊆ N and close it under "Skolem witnesses" — for every existential formula true in N with parameters from your growing set, add a witness to the set. The closure is elementary in N. This construction underpins the downward Löwenheim-Skolem theorem, which guarantees elementary submodels of any infinite structure of any smaller infinite cardinality.

Elementary substructures matter because they let you reason about large or complex structures by shrinking them to more manageable sizes *without changing the first-order truths*. Any sentence true in a large elementary extension N is already true in the smaller M ≺ N. This means model-theoretic proofs can often be reduced to countable or even finite structures, and that the first-order properties of a structure are shared by an entire family of elementarily equivalent models of varying cardinalities.

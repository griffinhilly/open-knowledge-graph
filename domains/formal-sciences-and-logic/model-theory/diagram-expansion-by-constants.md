---
id: diagram-expansion-by-constants
title: Diagram and Expansion by Constants
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-instantiation-structures
  type: hard
- id: signature-and-vocabulary-model-theory
  type: hard
builds-toward:
- existential-closure-homomorphism
- extension-lemma-embeddings
tags:
- diagram
- expansion
- constants
- language-extension
stage: expert
status: draft
---

# Diagram and Expansion by Constants

## Core Idea
The diagram of a structure M is formed by expanding the signature with a constant symbol for each element of M, then taking all atomic sentences true in M. The expanded theory allows explicit reference to elements and is crucial for proving extension lemmas and building homomorphism extensions.

## How It's Best Learned
Write out the diagram of a small structure like Z_3 (integers mod 3) with constants for each element, then extend embeddings using the diagram.

## Questions

```yaml
- question: "A structure N, expanded to interpret the constant symbols {c_a : a ∈ M}, satisfies Diag(M). What must be true about the relationship between M and N?"
  type: multiple-choice
  options:
    - "N is isomorphic to M — they are the same structure up to relabeling of elements"
    - "N is an elementary extension of M — every first-order sentence true in M is also true in N"
    - "There exists an injective homomorphism (embedding) from M into N"
    - "N is a homomorphic image of M — there is a surjective structure-preserving map from M onto N"
  answer: 2
  explanation: "The diagram lemma states precisely this: N ⊨ Diag(M) (with constants interpreted as required) if and only if there is an embedding of M into N. An embedding is an injective homomorphism that preserves and reflects all atomic relations — it places an isomorphic copy of M inside N. This is weaker than isomorphism (N may be larger) and weaker than elementary extension (N need not satisfy the same first-order sentences). The diagram captures only the atomic facts about M, which is exactly the information needed to guarantee M embeds into any model of those atomic facts."

- question: "The elementary diagram ElDiag(M) differs from the diagram Diag(M) in that it contains:"
  type: multiple-choice
  options:
    - "Sentences about the cardinality of M that Diag(M) omits"
    - "All first-order sentences (including quantified formulas) that are true in M with the named constants, not just atomic and negated-atomic sentences"
    - "Second-order sentences that more precisely characterize M up to isomorphism"
    - "Only the positive atomic sentences, omitting the negations that Diag(M) includes"
  answer: 1
  explanation: "Diag(M) contains only atomic sentences (R(c_a, c_b), f(c_a) = c_b, c_a = c_b) and their negations — facts about specific named elements with no quantification. ElDiag(M) extends this to all first-order sentences with the named constants: it includes ∀x φ(x, c_a) and ∃x φ(x, c_a) for every formula φ and every element a ∈ M. The consequence is that N ⊨ ElDiag(M) if and only if N is an elementary extension of M (not merely an extension by embedding). A model of Diag(M) only needs to contain an isomorphic copy of M; a model of ElDiag(M) must satisfy all the same first-order truths about its copy of M."

- question: "If distinct elements a and b in M are given distinct constant symbols c_a and c_b in the diagram construction, then any model of Diag(M) must have at least as many elements as M."
  type: true-false
  answer: true
  explanation: "Diag(M) includes the sentence ¬(c_a = c_b) for every pair of distinct elements a ≠ b in M. Any model N satisfying Diag(M) must interpret c_a and c_b as distinct elements of its domain, so N must contain at least one element for each element of M. The constant symbols function as 'witnesses' that force N to be at least as large as M. This is the embedding part of the diagram lemma: Diag(M) encodes the requirement that N has room for all of M's elements, not just that it satisfies the same abstract laws."

- question: "The diagram Diag(M) consists of all first-order sentences — including quantified sentences — that are true in M when each element is given a constant name."
  type: true-false
  answer: false
  explanation: "This describes the elementary diagram ElDiag(M), not the ordinary diagram Diag(M). The diagram uses only atomic sentences (and their negations): direct facts about named elements like R(c_a, c_b) = true or c_a + c_b = c_c. Quantified sentences like ∀x∃y R(x,y) are excluded from Diag(M). The distinction is consequential: satisfying Diag(M) guarantees only an embedding (injective homomorphism), while satisfying ElDiag(M) guarantees an elementary extension (one satisfying all the same first-order truths). Using Diag(M) where ElDiag(M) is needed, or vice versa, produces the wrong structural relationship."

- question: "Explain why Diag(M) — rather than a set of axioms describing M's properties — is the right tool for finding structures that 'contain' M in the embedding sense."
  type: short-answer
  answer: "Axioms describing M's properties are general: they say what kind of structure M is (e.g., 'a group', 'a field'), but they are satisfied by many structures that have nothing to do with M specifically. A model of the axioms for groups need not contain M as a subgroup — it just needs to be some group. Diag(M) is specific to M: it names every element of M explicitly with constants and records every atomic fact about those named elements. Any structure satisfying Diag(M) must contain interpretations for all those constants satisfying all those atomic facts, which forces it to contain an isomorphic copy of M. The diagram technique turns 'M embeds into N' from a semantic relationship that must be verified by finding an embedding into a syntactic condition — N models a particular theory — that can be manipulated with compactness and other logical tools."
  explanation: "This syntactic handle on embeddings is what makes the diagram construction so useful in model theory. The upward Löwenheim-Skolem theorem, for example, is proved by adding Diag(M) to a theory with witnesses for new elements and applying compactness: any finite subset of the combined theory has a model, so the whole theory has a model, and that model is an extension of M. The diagram turns a construction problem (build a larger structure containing M) into a consistency problem (does this theory have a model?), which is solved by compactness."
```

## Explainer

You've studied structures and signatures — a signature σ specifies function, relation, and constant symbols, and a structure M interprets them over a domain. The diagram technique gives you a precise way to "name" every element of a structure in the language, turning facts about M into sentences of a theory that other structures must satisfy.

The construction: start with a structure M with domain A. Expand the signature σ by adding a fresh **constant symbol** c_a for each element a ∈ A, producing the expanded signature σ_A. Interpret each c_a as the element a itself in the expanded structure M_A = (M, a)_{a∈A}. The **diagram** of M, written Diag(M), is the set of all **atomic sentences** and **negations of atomic sentences** in the language σ_A that are true in M_A. For a small structure like ℤ₃ with elements {0, 1, 2} and signature {+, 0}, the diagram includes sentences like c₀ + c₁ = c₁, c₁ + c₁ = c₂, c₁ + c₂ = c₀, ¬(c₀ = c₁), and so on — every true atomic fact about the elements, each named explicitly.

The key theorem is the **diagram lemma**: a σ-structure N (expanded to interpret the constants c_a) is a model of Diag(M) if and only if there exists an **embedding** (an injective homomorphism) from M into N. In other words, satisfying Diag(M) forces N to contain an isomorphic copy of M. This is the bridge between syntactic manipulation of theories and the semantic question of which structures embed into which. Whenever you want to extend M to a larger structure or find a model containing M, you work with Diag(M) — any model of Diag(M) works.

The **elementary diagram** ElDiag(M) extends this further: it includes all first-order sentences (not just atomic ones) true in M_A. A structure N is an **elementary extension** of M — meaning it satisfies exactly the same first-order sentences — if and only if N models ElDiag(M). This is the syntactic characterization of elementary extensions, and it is how the upward Löwenheim-Skolem theorem is typically proved: you add Diag(M) plus witnesses for new elements, apply compactness, and the resulting model is an elementary extension of M. The diagram construction is the workhorse for building larger models that preserve exactly the properties you care about.

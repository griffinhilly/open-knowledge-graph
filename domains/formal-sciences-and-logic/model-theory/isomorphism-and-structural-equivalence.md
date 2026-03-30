---
id: isomorphism-and-structural-equivalence
title: Isomorphisms and Structural Equivalence
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: embedding-and-preservation-properties
  type: hard
- id: isomorphisms-in-categories
  type: soft
builds-toward:
- elementary-equivalence-indistinguishability
- ryll-nardzewski-categoricity-theorem
tags:
- isomorphism
- equivalence
- bijection
- structure-preserving
stage: advanced
status: validated
---

# Isomorphisms and Structural Equivalence

## Core Idea
Two structures M and N are isomorphic if there exists a bijection f: M → N that preserves all atomic formulas. Isomorphic structures are essentially identical from a first-order perspective—they satisfy exactly the same sentences. Isomorphism is the strongest notion of structural equivalence in model theory.

## Questions

```yaml
- question: "The structures (ℤ, <) and (ℚ, <) — the integers and rationals under their usual orderings — satisfy different first-order sentences (for example, ℚ satisfies 'between any two elements there is another,' while ℤ does not). What can we conclude?"
  type: multiple-choice
  options:
    - "They are isomorphic, because both are infinite linear orders"
    - "They are not isomorphic, and since they differ on a first-order sentence, they are not even elementarily equivalent"
    - "They are elementarily equivalent but not isomorphic, because they have the same cardinality"
    - "They cannot be compared because one has a different language than the other"
  answer: 1
  explanation: "If two structures disagree on any first-order sentence, they cannot be isomorphic (isomorphic structures satisfy exactly the same sentences) and they are not elementarily equivalent. The density property 'between any two elements there is a third' is a first-order sentence true of ℚ but false of ℤ (there is nothing between 1 and 2 in ℤ). So ℤ and ℚ are neither isomorphic nor elementarily equivalent as ordered structures."

- question: "An isomorphism f: M → N differs from a mere embedding g: M → N in which crucial respect?"
  type: multiple-choice
  options:
    - "An isomorphism preserves all first-order formulas; an embedding preserves only universal sentences"
    - "An isomorphism must be surjective — its image is all of N; an embedding's image may be a proper substructure"
    - "An isomorphism is always elementary; an embedding may fail to preserve existential formulas"
    - "An embedding requires a bijection; an isomorphism only requires injectivity"
  answer: 1
  explanation: "Both an embedding and an isomorphism are injective maps that preserve and reflect atomic formulas. The difference is surjectivity: an embedding's image may be a proper substructure of N (it identifies M with a copy of itself inside N), while an isomorphism is bijective — M is put in perfect one-to-one correspondence with all of N. Isomorphisms are 'perfect translations' of one structure into another; embeddings are 'inclusions into a larger structure.'"

- question: "If M and N are isomorphic, then every first-order sentence true in M is also true in N."
  type: true-false
  answer: true
  explanation: "This is the fundamental theorem of isomorphisms: an isomorphism f: M → N is a bijection that preserves all atomic formulas, and by induction on formula complexity, it preserves the truth of every first-order formula. Intuitively, renaming elements by f produces an indistinguishable copy — no formula can detect whether you're evaluating it on M or on its f-image in N. Isomorphism is the strongest notion of structural equivalence precisely because it preserves all logical properties, not just atomic ones."

- question: "Two structures that satisfy exactly the same first-order sentences is expected to be isomorphic."
  type: true-false
  answer: false
  explanation: "This is false, and it is one of model theory's most important lessons. Elementary equivalence (satisfying the same sentences) is strictly weaker than isomorphism. A classic example: (ℚ, <) and any countable dense linear order without endpoints are elementarily equivalent to each other, but a countable dense linear order and an uncountable one (like ℝ) also satisfy the same first-order sentences — yet they cannot be isomorphic since they have different cardinalities. Compactness and Löwenheim-Skolem theorems guarantee the existence of models of different sizes that are elementarily equivalent."

- question: "What is the difference between isomorphism and elementary equivalence, and why does model theory need both concepts?"
  type: short-answer
  answer: "Two structures are isomorphic if there exists a bijection between them that preserves all atomic formulas — they are literally the same structure with renamed elements, and they agree on every first-order sentence. Two structures are elementarily equivalent if they satisfy exactly the same first-order sentences, but there may be no bijection between them (they might have different cardinalities). Isomorphism implies elementary equivalence, but not conversely. Model theory needs both because isomorphism is too strong for classifying models of most theories: by Löwenheim-Skolem, a theory with an infinite model has models of every infinite cardinality, which cannot all be isomorphic. Elementary equivalence is the coarser tool for identifying models that are logically indistinguishable even when structurally different in size."
  explanation: "This distinction drives much of model theory. A theory is categorical in cardinality κ if all its models of size κ are isomorphic — this is a very strong condition. Most theories have non-isomorphic models of the same cardinality. Elementary equivalence classes partition models by logical indistinguishability, providing a finer analysis than 'same theory' but coarser than isomorphism. The interplay between these equivalence relations is studied through tools like back-and-forth systems, Ehrenfeucht-Fraïssé games, and Scott sentences."
```

## Explainer

You already know about embeddings and preservation properties: an embedding is an injective map between structures that preserves and reflects atomic formulas. An **isomorphism** is an embedding that is also surjective — a bijection in both directions. If f: M → N is an isomorphism, then f is a perfect dictionary that translates every element of M to a unique element of N, with every structural fact preserved exactly.

The fundamental theorem of isomorphisms says that isomorphic structures satisfy the same first-order sentences: M ⊨ φ if and only if N ⊨ φ for every sentence φ. This makes sense intuitively — if you relabel all the elements of M according to f, you get a structure that looks identical to N in every logical respect. No formula in the language can distinguish them, because any formula evaluated on M can be translated element-by-element to the same truth value on N.

It helps to compare isomorphism to related but weaker notions from your prerequisites. An **embedding** (from your prerequisite topic) preserves structure in one direction but the image might be a proper substructure of N. An **elementary embedding** preserves all first-order formulas, not just atomic ones, which is a stronger requirement. **Elementary equivalence** (which you'll study next) is weaker than isomorphism: M ≡ N means they satisfy the same sentences, but there might be no bijection between them — this can happen when the structures have different cardinalities but are otherwise logically indistinguishable.

This hierarchy of equivalences — isomorphism ⊃ elementary equivalence — is central to model theory. Isomorphism is the "gold standard" of sameness: two structures that are isomorphic are literally the same structure with different names for elements. But isomorphism is often too strong for classifying models of a theory, because a theory can have non-isomorphic models of different sizes. This is why model theory develops the coarser tool of elementary equivalence: two models that satisfy exactly the same sentences are equivalent for all logical purposes, even if no bijection exists between them. Understanding where isomorphism ends and elementary equivalence takes over is one of the first lessons in the subject's depth.

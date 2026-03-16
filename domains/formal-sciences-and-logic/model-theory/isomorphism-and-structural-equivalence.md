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
- elementary-equivalence-and-logical-indistinguishability
- ryll-nardzewski-categoricity-theorem
tags:
- isomorphism
- equivalence
- bijection
- structure-preserving
stage: abstract-reasoning
status: draft
---

# Isomorphisms and Structural Equivalence

## Core Idea
Two structures M and N are isomorphic if there exists a bijection f: M → N that preserves all atomic formulas. Isomorphic structures are essentially identical from a first-order perspective—they satisfy exactly the same sentences. Isomorphism is the strongest notion of structural equivalence in model theory.

## Explainer

You already know about embeddings and preservation properties: an embedding is an injective map between structures that preserves and reflects atomic formulas. An **isomorphism** is an embedding that is also surjective — a bijection in both directions. If f: M → N is an isomorphism, then f is a perfect dictionary that translates every element of M to a unique element of N, with every structural fact preserved exactly.

The fundamental theorem of isomorphisms says that isomorphic structures satisfy the same first-order sentences: M ⊨ φ if and only if N ⊨ φ for every sentence φ. This makes sense intuitively — if you relabel all the elements of M according to f, you get a structure that looks identical to N in every logical respect. No formula in the language can distinguish them, because any formula evaluated on M can be translated element-by-element to the same truth value on N.

It helps to compare isomorphism to related but weaker notions from your prerequisites. An **embedding** (from your prerequisite topic) preserves structure in one direction but the image might be a proper substructure of N. An **elementary embedding** preserves all first-order formulas, not just atomic ones, which is a stronger requirement. **Elementary equivalence** (which you'll study next) is weaker than isomorphism: M ≡ N means they satisfy the same sentences, but there might be no bijection between them — this can happen when the structures have different cardinalities but are otherwise logically indistinguishable.

This hierarchy of equivalences — isomorphism ⊃ elementary equivalence — is central to model theory. Isomorphism is the "gold standard" of sameness: two structures that are isomorphic are literally the same structure with different names for elements. But isomorphism is often too strong for classifying models of a theory, because a theory can have non-isomorphic models of different sizes. This is why model theory develops the coarser tool of elementary equivalence: two models that satisfy exactly the same sentences are equivalent for all logical purposes, even if no bijection exists between them. Understanding where isomorphism ends and elementary equivalence takes over is one of the first lessons in the subject's depth.

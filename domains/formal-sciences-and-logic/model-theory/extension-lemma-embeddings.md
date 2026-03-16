---
id: extension-lemma-embeddings
title: Extension Lemma for Embeddings
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: existential-closure-homomorphism
  type: hard
- id: diagram-expansion-by-constants
  type: hard
- id: compactness-theorem-model-theory
  type: soft
builds-toward:
- universal-homogeneous-models
- amalgamation-construction-extensions
tags:
- extension
- embedding
- homomorphism-extension
- partial-map
stage: abstract-reasoning
status: draft
---

# Extension Lemma for Embeddings

## Core Idea
The extension lemma states that a partial embedding f: A → M (where A ⊂ M) can be extended to an embedding of a larger set into a sufficiently large structure. This is proved using the compactness theorem applied to the diagram of M with constants for elements of A. Extension lemmas are foundational for all amalgamation constructions.

## How It's Best Learned
Prove the extension lemma from compactness for a specific example: extending an embedding of Q into itself to an embedding of an algebraic extension.

## Explainer

You already know the **diagram** of a structure M: the set of all atomic and negated-atomic sentences true in M when constants are introduced for each element. You also know that an **embedding** f: A → M is an injective map that preserves the truth of atomic formulas — it is a way of copying A faithfully into M. The extension lemma asks: given a partial embedding of a subset A of M into another structure N, can you extend it to embed a *larger* subset of M into some extension of N? The answer is yes, provided you choose N generously enough, and the proof uses compactness in a clean and instructive way.

Here is the argument. Suppose f: A → N is an embedding of A (a subset of M) into N. You want to extend f to include a new element m ∈ M \ A. Introduce a new constant symbol c for m. Consider the **diagram of M expanded by A-constants**: all atomic and negated-atomic sentences about M using names for elements of A. Now form the set T of sentences that includes the existential consequences of this diagram — specifically, the type of m over A, expressing all the atomic relationships between m and the named elements of A. Ask whether T ∪ Th(N) is satisfiable. By the assumption that f embeds A into N, N already satisfies all the conditions on the A-constants. The new type of m over A consists of finitely supported conditions (by compactness), each of which is individually satisfiable in some extension of N. Compactness then guarantees a model of the whole set, giving an extension N' of N that contains an element playing the role of m.

The lemma's power comes from iteration: you can extend one element at a time, and a back-and-forth argument (alternating extensions from each side) builds **isomorphisms** between models. This is the engine behind proving that two countable homogeneous structures satisfying the same theory are isomorphic — each partial isomorphism can be extended because the extension lemma applies at every step. The result is also the foundation for **amalgamation** constructions: given two structures that each extend a common base A, you can amalgamate them into a single structure containing both, by applying the extension lemma to the pushout diagram.

Think of the extension lemma as the "local-to-global" principle of model theory. Globally building a large embedding or isomorphism is hard to guarantee directly. But locally — one element at a time — compactness ensures you can always take one more step. The art of model-theoretic construction is arranging these local steps into a coherent transfinite or back-and-forth procedure that reaches the globally desired structure.


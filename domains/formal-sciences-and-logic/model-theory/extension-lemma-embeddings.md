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
stage: expert
status: draft
---

# Extension Lemma for Embeddings

## Core Idea
The extension lemma states that a partial embedding f: A → M (where A ⊂ M) can be extended to an embedding of a larger set into a sufficiently large structure. This is proved using the compactness theorem applied to the diagram of M with constants for elements of A. Extension lemmas are foundational for all amalgamation constructions.

## How It's Best Learned
Prove the extension lemma from compactness for a specific example: extending an embedding of Q into itself to an embedding of an algebraic extension.

## Questions

```yaml
- question: "You have a partial embedding f: A → N (where A ⊂ M) and want to extend it to include a new element m ∈ M \\ A. What does the extension lemma guarantee?"
  type: multiple-choice
  options:
    - "That m itself embeds into N directly, without any modification to N"
    - "That there exists an extension N' ⊇ N containing an element that plays the role of m"
    - "That f can always be extended to a full automorphism of M"
    - "That the extension is possible only if A is an algebraically closed substructure"
  answer: 1
  explanation: "The extension lemma does not promise that N already contains a copy of m — N may need to be extended. The conclusion is that some N' ⊇ N exists in which the extended embedding lands. This is the key: you get a larger target structure, not a free embedding into the original one. The compactness argument constructs N' by showing the type of m over A is finitely satisfiable in extensions of N, then invoking compactness to guarantee a model."

- question: "What role does compactness play in the proof of the extension lemma?"
  type: multiple-choice
  options:
    - "It guarantees that the diagram of any infinite structure is equivalent to a finite one"
    - "It allows inferring satisfiability of the full type of m over A from satisfiability of each finite subset"
    - "It ensures that every embedding extends to an automorphism of a sufficiently large structure"
    - "It eliminates the need for constants in the diagram expansion"
  answer: 1
  explanation: "The type of m over A is an infinite set of atomic and negated-atomic conditions. Compactness says: if every finite subset is satisfiable, the whole set is satisfiable. Since each finite fragment of the type can be satisfied in some extension of N (using that f already embeds A correctly), compactness delivers a model satisfying all conditions at once — that model is N'. Without compactness you could only extend finitely many conditions at a time."

- question: "The extension lemma provides a 'local-to-global' principle: small, one-element extensions guaranteed by compactness can be iterated to build a global isomorphism between countable structures."
  type: true-false
  answer: true
  explanation: "This is exactly the back-and-forth method. Each stage extends a partial isomorphism by one element from one side, then one element from the other. The extension lemma guarantees each single step is possible. Iterating countably many times — alternating between the two structures — builds a total isomorphism. The 'local' is each one-element extension; the 'global' is the finished isomorphism."

- question: "The extension lemma guarantees that a partial embedding f: A → N can always be extended within the same structure N, without passing to a larger structure."
  type: true-false
  answer: false
  explanation: "This is the key misreading to avoid. The lemma guarantees an extension into some N' that extends N — it does not promise the extension lands inside the original N. In general, N may not contain the necessary element. The construction produces a new structure N' ⊇ N. Requiring the extension to stay in N would be a much stronger (and often false) claim."

- question: "Why does building a global isomorphism via back-and-forth require the extension lemma to apply at every stage, not just once?"
  type: short-answer
  answer: "Each stage of back-and-forth produces a new partial isomorphism that is larger than the previous one, with new elements on both sides. The extension lemma is invoked fresh at each stage to extend the current partial map by one more element. If the lemma failed at any stage — if some element could not be matched — the construction would halt and no total isomorphism would result. The entire argument is a countable iteration, and its validity rests on the lemma holding unconditionally at each step."
  explanation: "This is why the extension lemma is 'foundational' for amalgamation and homogeneity results: those constructions are essentially back-and-forth arguments, and the lemma is the engine that makes every local extension work. A single failure would break the transfinite induction."
```

## Explainer

You already know the **diagram** of a structure M: the set of all atomic and negated-atomic sentences true in M when constants are introduced for each element. You also know that an **embedding** f: A → M is an injective map that preserves the truth of atomic formulas — it is a way of copying A faithfully into M. The extension lemma asks: given a partial embedding of a subset A of M into another structure N, can you extend it to embed a *larger* subset of M into some extension of N? The answer is yes, provided you choose N generously enough, and the proof uses compactness in a clean and instructive way.

Here is the argument. Suppose f: A → N is an embedding of A (a subset of M) into N. You want to extend f to include a new element m ∈ M \ A. Introduce a new constant symbol c for m. Consider the **diagram of M expanded by A-constants**: all atomic and negated-atomic sentences about M using names for elements of A. Now form the set T of sentences that includes the existential consequences of this diagram — specifically, the type of m over A, expressing all the atomic relationships between m and the named elements of A. Ask whether T ∪ Th(N) is satisfiable. By the assumption that f embeds A into N, N already satisfies all the conditions on the A-constants. The new type of m over A consists of finitely supported conditions (by compactness), each of which is individually satisfiable in some extension of N. Compactness then guarantees a model of the whole set, giving an extension N' of N that contains an element playing the role of m.

The lemma's power comes from iteration: you can extend one element at a time, and a back-and-forth argument (alternating extensions from each side) builds **isomorphisms** between models. This is the engine behind proving that two countable homogeneous structures satisfying the same theory are isomorphic — each partial isomorphism can be extended because the extension lemma applies at every step. The result is also the foundation for **amalgamation** constructions: given two structures that each extend a common base A, you can amalgamate them into a single structure containing both, by applying the extension lemma to the pushout diagram.

Think of the extension lemma as the "local-to-global" principle of model theory. Globally building a large embedding or isomorphism is hard to guarantee directly. But locally — one element at a time — compactness ensures you can always take one more step. The art of model-theoretic construction is arranging these local steps into a coherent transfinite or back-and-forth procedure that reaches the globally desired structure.


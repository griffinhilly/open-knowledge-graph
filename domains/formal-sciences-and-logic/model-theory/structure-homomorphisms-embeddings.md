---
id: structure-homomorphisms-embeddings
title: Structure Homomorphisms and Embeddings
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: structures-and-formal-languages
  type: hard
- id: functions-and-mappings-formal
  type: soft
- id: binary-relations-definition-and-properties
  type: soft
builds-toward:
- elementary-equivalence-indistinguishability
tags:
- homomorphism
- embedding
- morphism
- isomorphism
- preservation
stage: expert
status: draft
---

# Structure Homomorphisms and Embeddings

## Core Idea
A homomorphism between two structures is a map that respects the interpretation: constants map to constants, functions commute (f(φ(a)) = φ(f(a))), and positive relations are preserved. Embeddings are injective homomorphisms that also preserve all relations, not just positive ones. These maps generalize familiar group and ring homomorphisms to arbitrary relational structures.

## Questions

```yaml
- question: "Let φ: M → N be a homomorphism between two structures, and suppose relation R holds on tuple (a, b) in M. Which statement is guaranteed by the definition of homomorphism?"
  type: multiple-choice
  options:
    - "R^N holds on (φ(a), φ(b)), and if R^N holds on any (φ(c), φ(d)) then R^M holds on (c, d)"
    - "R^N holds on (φ(a), φ(b))"
    - "R^M holds on (a, b) if and only if R^N holds on (φ(a), φ(b))"
    - "R^N holds on every tuple of elements in the image of φ"
  answer: 1
  explanation: "A homomorphism only guarantees the FORWARD direction: if R holds in M on a tuple, its image satisfies R in N. It does NOT require the converse — R^N might hold on (φ(c), φ(d)) even when R^M does not hold on (c, d). Option C (biconditional preservation) is precisely the additional property that, combined with injectivity, makes a map an embedding rather than merely a homomorphism. Option A confuses this forward-only preservation with the stronger reflection property of embeddings."

- question: "Which type of map between structures M and N guarantees that the image φ(M) is an isomorphic copy of M sitting inside N as a substructure?"
  type: multiple-choice
  options:
    - "Any homomorphism φ: M → N"
    - "An injective homomorphism (embedding) φ: M → N"
    - "A surjective homomorphism φ: M → N"
    - "Any map φ: M → N between structures with the same cardinality"
  answer: 1
  explanation: "An embedding is an injective homomorphism that also reflects relations: R^M holds on a tuple if and only if R^N holds on the image tuple. The two-way preservation plus injectivity ensures the image φ(M) is an isomorphic copy of M — no relational facts are lost or gained, and no two elements of M collapse to the same image element. A mere homomorphism might be non-injective (collapsing elements) or fail to reflect relations, so its image need not mirror M's structure. Surjectivity (option C) produces an isomorphism of the whole of M to N, not a substructure relationship."

- question: "If φ: M → N is a homomorphism and R^N holds on (φ(a), φ(b)), then R^M must hold on (a, b) in M."
  type: true-false
  answer: false
  explanation: "False. This backward direction — reflection of relations — is NOT required by a mere homomorphism. It is the extra property (along with injectivity) that makes a map an embedding. Homomorphisms preserve relations only forward: R in M implies R in N on the image. But R holding in N on image elements does not guarantee R held in M on the preimages. A homomorphism can map elements into N in a way that satisfies additional relations not present in M. This is why embeddings are strictly stronger: they prevent the image from 'gaining' relational facts that didn't exist in the source."

- question: "An isomorphism between two structures M and N guarantees that any first-order sentence true in M is also true in N."
  type: true-false
  answer: true
  explanation: "True. An isomorphism is a bijective embedding — a perfect, structure-preserving bijection in both directions. It preserves all elements, functions, and relations completely. Any first-order sentence quantifies over elements and applies function and relation symbols; since the isomorphism mirrors every element, function value, and relational fact between M and N, any sentence true in one is true in the other. Structures satisfying exactly the same first-order sentences are called elementarily equivalent; isomorphic structures are a special case that are both elementarily equivalent and structurally identical (not just logically indistinguishable)."

- question: "What is the key difference between a homomorphism and an embedding, and why does it matter for which logical sentences are preserved?"
  type: short-answer
  answer: "A homomorphism preserves relations only in the forward direction: if R holds in M, it holds on the image in N, but R can hold in N on image elements without holding in M. An embedding is an injective homomorphism that also reflects relations: R holds in M if and only if R holds on the image in N. This matters because embeddings preserve all quantifier-free first-order sentences — both positive and negative relational facts — while homomorphisms preserve only positive existential sentences. Homomorphisms cannot preserve negations because they permit the image to satisfy relations absent in the source."
  explanation: "The logical characterization is central to model theory: each type of structure-preserving map corresponds to a class of first-order formulas it preserves. Homomorphisms preserve sentences of the form ∃x R(x) (positive existential), but not ¬R(x) or ∀x R(x) — because the image might satisfy R in ways the source does not. Embeddings preserve quantifier-free sentences, so both 'R(a, b) holds' and 'R(a, b) does not hold' are accurately reflected. For preservation of all first-order sentences, one needs elementary embeddings, a yet stronger condition. This layered picture — stronger maps preserve richer formula classes — organizes much of classical model theory."
```

## Explainer

From your study of structures and formal languages, you know that a structure M for a signature σ interprets each symbol: constants become elements, function symbols become functions on the domain, and relation symbols become subsets of Cartesian powers. A map between two σ-structures must respect all of these interpretations to be considered structure-preserving. The different strengths of preservation correspond to different types of map, each capturing a different notion of "sameness" between structures.

A **homomorphism** φ: M → N is the weakest condition: for each constant symbol c, φ(c^M) = c^N; for each n-ary function symbol f, φ(f^M(a_1,...,a_n)) = f^N(φ(a_1),...,φ(a_n)); and for each n-ary relation symbol R, if R^M(a_1,...,a_n) holds in M then R^N(φ(a_1),...,φ(a_n)) holds in N. Notice that relations are only required to be preserved in the *forward* direction: the map cannot "create" a relation that was absent in M, but it may "destroy" one — if R does not hold in M on some tuple, the image of that tuple might still satisfy R in N. This is exactly the analogue of group homomorphisms, where φ(ab) = φ(a)φ(b) but φ need not be injective.

An **embedding** is an injective homomorphism that also **reflects** relations: R^M(a_1,...,a_n) holds if and only if R^N(φ(a_1),...,φ(a_n)) holds. The two-way preservation means the image of M inside N is an isomorphic copy of M — no relation is lost or gained. An embedding lets you think of M as literally living inside N as a substructure. An **isomorphism** is a surjective embedding, so φ is a bijection that perfectly mirrors both structures. Note the hierarchy: isomorphism → embedding → homomorphism, each strictly weaker in requirements.

The distinction matters most when asking what first-order sentences a map preserves. Homomorphisms preserve all **positive existential** sentences (∃x P(x), ∃x∃y (P(x) ∧ Q(y)), etc.) but need not preserve negations or universal quantifiers. Embeddings preserve all **quantifier-free** sentences. For full preservation of all first-order sentences, you need **elementary embeddings** — a strictly stronger condition (the subject of elementary equivalence). This layered picture is central to model theory: the logical properties of a map are determined precisely by what syntactic class of formulas it preserves, and each class corresponds to a geometric notion of how faithfully one structure sits inside another.


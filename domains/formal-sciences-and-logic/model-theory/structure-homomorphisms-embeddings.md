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
stage: advanced
status: draft
---

# Structure Homomorphisms and Embeddings

## Core Idea
A homomorphism between two structures is a map that respects the interpretation: constants map to constants, functions commute (f(φ(a)) = φ(f(a))), and positive relations are preserved. Embeddings are injective homomorphisms that also preserve all relations, not just positive ones. These maps generalize familiar group and ring homomorphisms to arbitrary relational structures.

## Explainer

From your study of structures and formal languages, you know that a structure M for a signature σ interprets each symbol: constants become elements, function symbols become functions on the domain, and relation symbols become subsets of Cartesian powers. A map between two σ-structures must respect all of these interpretations to be considered structure-preserving. The different strengths of preservation correspond to different types of map, each capturing a different notion of "sameness" between structures.

A **homomorphism** φ: M → N is the weakest condition: for each constant symbol c, φ(c^M) = c^N; for each n-ary function symbol f, φ(f^M(a_1,...,a_n)) = f^N(φ(a_1),...,φ(a_n)); and for each n-ary relation symbol R, if R^M(a_1,...,a_n) holds in M then R^N(φ(a_1),...,φ(a_n)) holds in N. Notice that relations are only required to be preserved in the *forward* direction: the map cannot "create" a relation that was absent in M, but it may "destroy" one — if R does not hold in M on some tuple, the image of that tuple might still satisfy R in N. This is exactly the analogue of group homomorphisms, where φ(ab) = φ(a)φ(b) but φ need not be injective.

An **embedding** is an injective homomorphism that also **reflects** relations: R^M(a_1,...,a_n) holds if and only if R^N(φ(a_1),...,φ(a_n)) holds. The two-way preservation means the image of M inside N is an isomorphic copy of M — no relation is lost or gained. An embedding lets you think of M as literally living inside N as a substructure. An **isomorphism** is a surjective embedding, so φ is a bijection that perfectly mirrors both structures. Note the hierarchy: isomorphism → embedding → homomorphism, each strictly weaker in requirements.

The distinction matters most when asking what first-order sentences a map preserves. Homomorphisms preserve all **positive existential** sentences (∃x P(x), ∃x∃y (P(x) ∧ Q(y)), etc.) but need not preserve negations or universal quantifiers. Embeddings preserve all **quantifier-free** sentences. For full preservation of all first-order sentences, you need **elementary embeddings** — a strictly stronger condition (the subject of elementary equivalence). This layered picture is central to model theory: the logical properties of a map are determined precisely by what syntactic class of formulas it preserves, and each class corresponds to a geometric notion of how faithfully one structure sits inside another.


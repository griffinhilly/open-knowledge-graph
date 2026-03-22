---
id: exact-sequences
title: Exact Sequences in Categories
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: additive-categories
  type: hard
- id: vector-spaces
  type: soft
- id: linear-transformations-definition
  type: soft
builds-toward:
- snake-lemma
- abelian-structure-properties
- homology-and-cohomology
tags:
- sequences
- homological-algebra
- kernels-cokernels
stage: advanced
status: draft
---

# Exact Sequences in Categories

## Core Idea
An exact sequence is a sequence of morphisms f: A → B → C where the image of one equals the kernel of the next. Exactness encodes compatibility conditions between maps. Short exact sequences (0 → A → B → C → 0) characterize extensions and are central to homological algebra, capturing how one object fits inside another with a given quotient.

## Questions

```yaml
- question: "A sequence A →^f B →^g C satisfies g∘f = 0 (the composition is the zero map). Does this guarantee the sequence is exact at B?"
  type: multiple-choice
  options:
    - "Yes — g∘f = 0 is the definition of exactness at B"
    - "Yes — the zero composition is equivalent to im(f) = ker(g) in any abelian category"
    - "No — g∘f = 0 only implies im(f) ⊆ ker(g), not necessarily im(f) = ker(g)"
    - "No — exactness at B additionally requires that f is injective and g is surjective"
  answer: 2
  explanation: "g∘f = 0 means every element in the image of f is sent to 0 by g, which is exactly the statement im(f) ⊆ ker(g). But exactness requires the stronger condition im(f) = ker(g) — every element that g kills must have come from f. A sequence satisfying g∘f = 0 is called a chain complex; an exact sequence is a chain complex with the additional constraint that there is no 'extra' kernel. The difference matters: the homology of a chain complex measures exactly this gap, H = ker(g)/im(f), which is trivial precisely when the sequence is exact."

- question: "In the short exact sequence 0 → ℤ →^×2 ℤ →^mod2 ℤ/2ℤ → 0 (where ×2 is multiplication by 2 and mod2 is reduction mod 2), which statement best describes what exactness at ℤ (the middle term) tells us?"
  type: multiple-choice
  options:
    - "The map ×2 is an isomorphism from ℤ to ℤ"
    - "Every integer that maps to 0 under mod2 (i.e., every even integer) is in the image of ×2"
    - "The only integer sent to 0 by ×2 is 0 itself"
    - "ℤ is isomorphic to the direct sum ℤ ⊕ ℤ/2ℤ"
  answer: 1
  explanation: "Exactness at the middle ℤ requires im(×2) = ker(mod2). The image of ×2 is the even integers {…, -4, -2, 0, 2, 4, …}. The kernel of mod2 is also the even integers (those that map to 0 in ℤ/2ℤ). So im(×2) = ker(mod2) = 2ℤ — confirmed exact. Option B correctly identifies this equality. Note that option D is false: this short exact sequence does not split (there is no homomorphism ℤ/2ℤ → ℤ), so ℤ is not isomorphic to ℤ ⊕ ℤ/2ℤ — a key illustration that extension problems are non-trivial."

- question: "In a short exact sequence 0 → A →^f B →^g C → 0, exactness at A forces f to be injective, and exactness at C forces g to be surjective."
  type: true-false
  answer: true
  explanation: "Exactness at A means im(0 → A) = ker(f). The image of the zero map into A is {0}, so ker(f) = {0}, which means f is injective. Exactness at C means im(g) = ker(C → 0). The kernel of the zero map out of C is all of C, so im(g) = C, which means g is surjective. These are not extra assumptions — they are forced by exactness at the endpoints. This is why short exact sequences 0 → A → B → C → 0 are often described by saying 'f is a monomorphism and g is an epimorphism.'"

- question: "If 0 → A →^f B →^g C → 0 is a short exact sequence, then B must be isomorphic to the direct sum A ⊕ C."
  type: true-false
  answer: false
  explanation: "This is a classic misconception. Exactness tells you that A embeds into B and C is the quotient B/A, but it does not tell you how B is built from these pieces. B is an extension of C by A, and different short exact sequences with the same A and C (but different B) correspond to genuinely non-isomorphic middle objects. B ≅ A ⊕ C holds only when the sequence splits — meaning there exists a section s: C → B with g∘s = id_C. Whether a given exact sequence splits is a non-trivial question and is precisely what Ext¹(C, A) measures."

- question: "What does it mean for a sequence to be 'exact at B,' and why is this condition strictly stronger than merely requiring that the composition of consecutive maps is zero?"
  type: short-answer
  answer: "A sequence A →^f B →^g C is exact at B if im(f) = ker(g): everything that f maps into B is precisely the collection of elements that g sends to 0. The condition g∘f = 0 only requires im(f) ⊆ ker(g) — every image element is killed by g, but there may be elements in ker(g) that are not in im(f). Exactness demands there are no such 'extra' kernel elements. The gap ker(g)/im(f) — which vanishes exactly when the sequence is exact — is what homology groups measure."
  explanation: "The distinction between chain complexes (g∘f = 0) and exact sequences (im = ker) is foundational to homological algebra. A chain complex can fail to be exact, and that failure is measured by its homology groups. Exact sequences are chain complexes with trivial homology everywhere. This is why long exact sequences in algebraic topology are so powerful: they allow you to relate the homology of spaces in a controlled way, and any deviation from exactness would signal a non-trivial topological feature."
```

## Explainer

From your work on additive categories and linear transformations, you know that a morphism f: A → B in an abelian category has both a kernel (elements sent to 0) and an image (elements reached by f). Exactness is a condition on how consecutive morphisms in a sequence interact: in A →^f B →^g C, the sequence is **exact at B** if im(f) = ker(g). In words, everything that f sends into B is precisely the collection of things that g kills — no more, no less. Exactness is not about a single map, but about the compatibility of two consecutive maps.

A concrete linear algebra example grounds the abstraction. Let V be a vector space and T: V → W a linear transformation. The sequence 0 → ker(T) →^i V →^T im(T) → 0 is always exact, where i is the inclusion. Exactness at ker(T): the map from 0 is the zero map, and its image {0} equals the kernel of i (which is {0} since inclusions are injective). Exactness at V: the image of i is ker(T), and the kernel of T is — by definition — ker(T). Exactness at im(T): T is surjective onto im(T), so its image is all of im(T), and the kernel of the map to 0 is also all of im(T). This exact sequence encodes the rank-nullity theorem: it says that V is built from ker(T) and im(T) in a precise way.

The most important structure is the **short exact sequence** 0 → A →^f B →^g C → 0. Exactness at A says f is injective (kernel of f equals image of 0 → A, which is {0}). Exactness at C says g is surjective (image of g equals kernel of the map to 0, which is all of C). Exactness at B says im(f) = ker(g). This means A embeds into B as a subobject, and C is the quotient B/A. The short exact sequence is precisely the data of an **extension**: B is "between" A and C in the sense that A sits inside B and C is what's left over. Different short exact sequences with the same A and C correspond to different ways B can extend A by C — this is the subject of **Ext groups** in homological algebra.

The power of exact sequences is that they let you transfer information between objects. If you know two of the three objects and some maps in a short exact sequence, you can often deduce properties of the third. **Long exact sequences** — which arise naturally from derived functors — chain these short exact sequences together and allow you to compute cohomology groups by relating them across a sequence. The snake lemma (which this topic builds toward) is the key engine: it produces long exact sequences from diagrams of short exact sequences. Once you can manipulate exact sequences fluently, you have the core computational tool of homological algebra, algebraic topology, and much of modern algebra.

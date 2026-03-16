---
id: homology-and-cohomology
title: Homology and Cohomology
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: chain-complexes-exact-sequences
  type: hard
- id: functors
  type: soft
- id: vector-spaces
  type: soft
- id: linear-transformations
  type: hard
- id: kernel-and-image
  type: soft
- id: linear-transformations-definition
  type: soft
builds-toward:
- derived-functors
tags:
- homology
- cohomology
- long exact sequence
- snake lemma
- connecting homomorphism
- homological algebra
stage: advanced
status: draft
---
# Homology and Cohomology

## Core Idea
The homology of a chain complex C_* in an abelian category is the sequence of objects H_n(C) = ker(d_n) / im(d_{n+1}), measuring the failure of the complex to be exact at each degree. Cohomology arises dually from cochain complexes. The central structural result is the long exact sequence in homology: a short exact sequence of chain complexes 0 → A_* → B_* → C_* → 0 induces a long exact sequence ··· → H_n(A) → H_n(B) → H_n(C) → H_{n-1}(A) → ···, connected by boundary maps constructed via the snake lemma. This machinery transforms short exact sequences of complexes into computable algebraic invariants across algebra, topology, and geometry.

## How It's Best Learned
Compute homology of a simple chain complex of abelian groups by hand: find the kernel, find the image, and take the quotient. Then take a short exact sequence of chain complexes and construct the long exact sequence, tracing the connecting homomorphism through the snake lemma diagram. The snake lemma proof, while technical, is the engine of homological algebra and rewards careful study.

## Common Misconceptions
- Homology and cohomology are not the same thing, even though they often carry equivalent information; cohomology has a natural ring structure (cup product) that homology lacks.
- The connecting homomorphism in the long exact sequence is not arbitrary; it arises canonically from the snake lemma and is natural in the short exact sequence.
- Zero homology does not mean the complex is trivial; it means the complex is exact, which is a strong and useful condition.

## Explainer

You already know what a chain complex is: a sequence of abelian groups (or modules, or objects in an abelian category) connected by boundary maps d_n: C_n → C_{n-1} satisfying d_{n-1} ∘ d_n = 0. The condition d² = 0 guarantees that the image of each boundary map is a subgroup of the kernel of the next one. Homology measures by how much the complex fails to be exact at each degree — in other words, how many "cycles" (elements in the kernel of d_n) are not "boundaries" (elements in the image of d_{n+1}). Formally, **H_n(C) = ker(d_n) / im(d_{n+1})**.

The geometric intuition is cleanest in simplicial homology. A 1-cycle is a loop of edges with no boundary; a 1-boundary is a loop that bounds a 2-dimensional face. H_1 counts loops that are not boundaries — it detects holes in the space. H_0 counts connected components. H_2 counts enclosed voids. This is why homology is a topological invariant: a doughnut and a coffee cup have the same homology because they have the same "hole structure," while a sphere and a torus differ in H_1. But in the algebraic setting you are learning, all this geometric content is abstracted away: homology is just the quotient ker/im, computable in any abelian category without reference to space at all.

The central theorem is the **long exact sequence in homology**. Given a short exact sequence of chain complexes 0 → A_* → B_* → C_* → 0 (an exact sequence at every degree), there is a naturally induced long exact sequence: ··· → H_n(A) → H_n(B) → H_n(C) →^δ H_{n-1}(A) → H_{n-1}(B) → ··· The map δ, called the **connecting homomorphism**, is the new and non-obvious part. It is constructed by the **snake lemma**: given an element c ∈ H_n(C), lift it to an element b ∈ B_n (possible by surjectivity of B → C), apply the boundary map d to get d(b) ∈ B_{n-1} (which turns out to land in the image of A_{n-1} by exactness), then map it back to A_{n-1} (possible by injectivity of A → B), and observe that it is a cycle. The connecting homomorphism δ sends the homology class [c] to the homology class [a] constructed this way. The proof that δ is well-defined and the resulting sequence is exact is a classic diagram chase.

Why does this matter? The long exact sequence is the main computational engine of homological algebra. To compute the homology of a complex B, it often suffices to find a short exact sequence where A and C are simpler. The long exact sequence then constrains H(B) in terms of H(A) and H(C), and you can often determine H(B) exactly from the resulting constraints. This strategy — compute by fitting into a short exact sequence — underlies the Mayer-Vietoris sequence in topology, the long exact sequence of a pair, and countless spectral sequence arguments.

**Cohomology** arises by reversing all the arrows: take a cochain complex C^* with coboundary maps d^n: C^n → C^{n+1} satisfying d^{n+1} ∘ d^n = 0, and define H^n(C) = ker(d^n) / im(d^{n-1}). In many cases, cohomology carries strictly more structure than homology: the **cup product** makes H*(C; R) into a graded ring, capturing intersection information that homology groups alone cannot see. For spaces, the cup product in singular cohomology detects non-trivial product structures — for instance, the cohomology rings of CP² and S² ∨ S⁴ are not isomorphic even though their cohomology groups are, meaning ring structure distinguishes spaces that groups cannot.

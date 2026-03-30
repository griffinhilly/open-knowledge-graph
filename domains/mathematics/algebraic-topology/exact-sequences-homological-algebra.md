---
id: exact-sequences-homological-algebra
title: Exact Sequences in Homological Algebra
domain: mathematics
course: algebraic-topology
prerequisites:
- id: group-homomorphisms
  type: hard
- id: quotient-groups
  type: hard
- id: chain-complexes-boundary-operator
  type: soft
builds-toward:
- snake-lemma-algebraic-topology
- five-lemma
- relative-homology-long-exact-sequence
- mayer-vietoris-sequence
- universal-coefficient-theorem
tags: [algebraic-topology, exact-sequences, homological-algebra, short-exact-sequences]
stage: expert
status: validated
---
# Exact Sequences in Homological Algebra

## Core Idea
A sequence of abelian group homomorphisms ... -> A -> B -> C -> ... is exact at B if the image of the incoming map equals the kernel of the outgoing map: im(A -> B) = ker(B -> C). Exact sequences encode relationships between groups with perfect precision — no information is lost or created at any stage. Short exact sequences 0 -> A -> B -> C -> 0 express B as an "extension" of C by A, and long exact sequences are the workhorses of homological computation, connecting the homology of related spaces through an infinite chain of exactness conditions.

## Questions

```yaml
- question: "In the short exact sequence 0 → Z →^{×2} Z → Z/2Z → 0, what does exactness at the middle Z tell us?"
  type: multiple-choice
  options:
    - "The map Z → Z/2Z is injective"
    - "The image of the multiplication-by-2 map (the even integers) equals the kernel of the quotient map Z → Z/2Z (also the even integers)"
    - "Z is isomorphic to Z ⊕ Z/2Z"
    - "The sequence splits"
  answer: 1
  explanation: "Exactness at the middle term means im(×2) = ker(Z → Z/2Z). The image of ×2 is 2Z (the even integers). The kernel of the quotient Z → Z/2Z is also 2Z. So im = ker = 2Z, confirming exactness. This sequence does NOT split: Z is not isomorphic to Z ⊕ Z/2Z (the former is torsion-free, the latter has 2-torsion). The non-splitting shows that Z is a 'non-trivial extension' of Z/2Z by Z."

- question: "A short exact sequence 0 → A →^i B →^p C → 0 encodes three exactness conditions. Exactness at A means i is injective, and exactness at C means p is surjective."
  type: true-false
  answer: true
  explanation: "Exactness at A: im(0 → A) = ker(i), so ker(i) = {0}, meaning i is injective. Exactness at C: im(p) = ker(C → 0) = C, so p is surjective. Exactness at B: im(i) = ker(p), meaning the image of the injection equals the kernel of the surjection. Together: A injects into B, the image of A is exactly the 'part of B that maps to zero in C,' and every element of C is hit by p. The sequence encodes that C ≅ B/i(A)."

- question: "Every short exact sequence 0 → A → B → C → 0 of abelian groups with C free (e.g., C ≅ Z^n) splits: B ≅ A ⊕ C."
  type: true-false
  answer: true
  explanation: "When C is free abelian, we can choose a section s: C → B (a homomorphism with p ∘ s = id_C) by sending each generator of C to a preimage under p. Then B = i(A) ⊕ s(C) ≅ A ⊕ C. This is a fundamental fact: free abelian groups are projective modules over Z, meaning every surjection onto them has a section. When C is not free (e.g., C = Z/2Z), the sequence may or may not split — the extension is classified by Ext^1(C, A)."

- question: "Explain why the exactness condition 'im = ker' at each term is the correct algebraic formulation of 'no information is lost or gained.'"
  type: short-answer
  answer: "At each term B in the sequence A → B → C: the image of A → B is the information 'coming in,' and the kernel of B → C is the information 'filtered out' (sent to zero in C). Exactness im(A → B) = ker(B → C) means: everything coming in from A is exactly what gets killed going to C. There is no 'extra' kernel (information destroyed without being accounted for by the incoming map) and no 'missing' image (information from A that survives into C). The sequence is 'tight' — each group is determined up to extension by its neighbors."
  explanation: "Contrast with a chain complex where im ⊆ ker but equality may fail. The quotient ker/im is the homology, measuring the 'gap.' An exact sequence has homology zero at every term — the sequence is 'acyclic' as a chain complex. Exact sequences are the most structured chain complexes: they carry maximum algebraic information about the relationships between the groups."
```

## Explainer

An **exact sequence** is a sequence of abelian groups and homomorphisms ... -> A_{n+1} -f_{n+1}-> A_n -f_n-> A_{n-1} -> ... where the image of each map equals the kernel of the next: im(f_{n+1}) = ker(f_n) for all n. This is a stronger condition than being a chain complex (where im subset ker); exactness means the homology H_n = ker(f_n)/im(f_{n+1}) is zero at every term. Exact sequences encode the tightest possible algebraic relationships between groups.

The most important type is the **short exact sequence** (SES): 0 -> A -i-> B -p-> C -> 0. Exactness at A says i is injective (A embeds in B). Exactness at C says p is surjective (every element of C is in the image). Exactness at B says im(i) = ker(p) (the copy of A inside B is exactly what gets killed by p). Together: C = B/i(A), and B is an "extension" of C by A. The group B is assembled from A and C, but the SES does not uniquely determine B — there can be multiple non-isomorphic extensions (classified by the Ext functor). The SES **splits** if B = A direct sum C, which happens when there exists a section s : C -> B with p compose s = id, or equivalently a retraction r : B -> A with r compose i = id.

**Long exact sequences** (LES) arise naturally in algebraic topology whenever we have a short exact sequence of chain complexes. Given 0 -> A_* -> B_* -> C_* -> 0 (an SES of chain complexes), there is a long exact sequence in homology: ... -> H_n(A) -> H_n(B) -> H_n(C) -partial-> H_{n-1}(A) -> H_{n-1}(B) -> ... The maps H_n(A) -> H_n(B) -> H_n(C) are induced by the chain maps. The **connecting homomorphism** partial : H_n(C) -> H_{n-1}(A) is the key new ingredient — it does not come from a chain map but is constructed by diagram chasing (the snake lemma). This connecting homomorphism is what links the homology groups across dimensions.

In algebraic topology, long exact sequences appear everywhere. The **LES of a pair** (X, A) comes from the SES of chain complexes 0 -> C_*(A) -> C_*(X) -> C_*(X, A) -> 0. The **Mayer-Vietoris sequence** for X = A union B is a long exact sequence derived (via excision) from a similar SES. The **LES of a fibration** F -> E -> B in homotopy theory comes from the fiber sequence structure. In each case, the long exact sequence provides the computational framework: knowing two of the three families of groups determines the third, up to extension problems that the connecting homomorphisms resolve.

The language of exact sequences pervades all of homological algebra and algebraic topology. A map being injective is equivalent to 0 -> A -> B being exact. A map being surjective is equivalent to B -> C -> 0 being exact. An isomorphism is equivalent to 0 -> A -> B -> 0 being exact. The **five lemma** and **snake lemma** are tools for manipulating exact sequences, and the entire framework of derived functors (Ext, Tor, sheaf cohomology) is built on analyzing when functors fail to preserve exactness. Understanding exact sequences is understanding the grammar of homological algebra.

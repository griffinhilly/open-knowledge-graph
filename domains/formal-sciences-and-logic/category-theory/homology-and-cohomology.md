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
- id: linear-transformations
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
stage: expert
status: validated
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

## Questions

```yaml
- question: "A chain complex C_* satisfies H_n(C) = 0 for all n. What does this mean about the complex?"
  type: multiple-choice
  options:
    - "All chain groups C_n are zero — the complex is trivially empty"
    - "The complex is exact at every degree — every cycle is a boundary"
    - "All boundary maps d_n are zero maps, so nothing maps anywhere"
    - "The complex has only even-degree terms; odd-degree terms are absent"
  answer: 1
  explanation: "H_n(C) = ker(d_n)/im(d_{n+1}) = 0 means ker(d_n) = im(d_{n+1}) at each degree — every cycle is a boundary. This is exactness. The chain groups C_n themselves can be very large and non-trivial; zero homology says nothing about the size of the groups, only about the relationship between consecutive maps. This is a common misconception: zero homology does not mean the complex is empty or trivial, but that it has the 'right' map structure — a strong and often useful condition."

- question: "A topologist wants to distinguish CP² (complex projective plane) from S² ∨ S⁴ (the wedge sum). Both spaces have identical homology groups in every degree. Which algebraic structure detects the difference?"
  type: multiple-choice
  options:
    - "The kernel of the boundary map in degree 2"
    - "The cup product structure in cohomology"
    - "The connecting homomorphism in the long exact sequence"
    - "The torsion subgroups of the chain groups"
  answer: 1
  explanation: "H*(CP²; ℤ) and H*(S² ∨ S⁴; ℤ) are isomorphic as graded abelian groups — homology cannot distinguish them. But in cohomology, the generator α ∈ H²(CP²) satisfies α ∪ α ≠ 0 (the cup product generates H⁴), while on S² ∨ S⁴ any cup product of positive-degree classes is zero. The cup product is a ring structure on cohomology with no homology analogue, demonstrating that cohomology sometimes carries strictly more information."

- question: "If the homology group H_n(C) = 0, then the chain complex is expected to be trivial — most of the chain groups C_n are zero."
  type: true-false
  answer: false
  explanation: "H_n(C) = 0 means the complex is exact at degree n (ker d_n = im d_{n+1}), which is a condition on the relationship between maps, not on the sizes of the groups. A non-trivial example: the complex 0 → ℤ →×2 ℤ → ℤ/2 → 0 is exact (has zero homology) but involves non-trivial groups throughout. Exactness is a structural property; zero homology is a powerful condition that says cycles and boundaries coincide perfectly at each degree."

- question: "Cohomology can distinguish spaces that homology cannot, because the cup product in cohomology carries information about how cohomology classes intersect that homology groups alone do not capture."
  type: true-false
  answer: true
  explanation: "As illustrated by CP² versus S² ∨ S⁴, cohomology rings (equipped with the cup product) detect multiplicative structure invisible to homology groups. The cup product α ∪ β ∈ H^{p+q} encodes intersection data between p- and q-dimensional classes. This extra structure makes cohomology essential in algebraic topology, algebraic geometry (de Rham, sheaf, and étale cohomology), and physics (characteristic classes, anomaly cancellation). Cohomology is dual to homology but is not equivalent to it in general."

- question: "What does the homology group H_n(C) actually measure, and why is the definition H_n = ker(d_n) / im(d_{n+1}) geometrically meaningful?"
  type: short-answer
  answer: "H_n(C) measures the failure of the chain complex to be exact at degree n — it counts n-cycles (closed chains with no boundary, in ker d_n) that are not themselves boundaries of (n+1)-chains (not in im d_{n+1}). In topology, these are genuine 'holes': loops not bounding disks, voids not enclosing solid regions. H_0 counts connected components, H_1 counts 1-dimensional holes (loops), H_2 counts enclosed voids, and so on. The quotient is meaningful because d² = 0 guarantees im d_{n+1} ⊆ ker d_n — without this, the quotient wouldn't even be well-defined."
  explanation: "The condition d² = 0 is the algebraic foundation that makes homology possible. It means every boundary is a cycle, so cycles form a group containing boundaries as a subgroup, and we can take the quotient. The size of H_n reflects how many independent non-boundary cycles exist — the 'topological complexity' at dimension n."
```

## Explainer

You already know what a chain complex is: a sequence of abelian groups (or modules, or objects in an abelian category) connected by boundary maps d_n: C_n → C_{n-1} satisfying d_{n-1} ∘ d_n = 0. The condition d² = 0 guarantees that the image of each boundary map is a subgroup of the kernel of the next one. Homology measures by how much the complex fails to be exact at each degree — in other words, how many "cycles" (elements in the kernel of d_n) are not "boundaries" (elements in the image of d_{n+1}). Formally, **H_n(C) = ker(d_n) / im(d_{n+1})**.

The geometric intuition is cleanest in simplicial homology. A 1-cycle is a loop of edges with no boundary; a 1-boundary is a loop that bounds a 2-dimensional face. H_1 counts loops that are not boundaries — it detects holes in the space. H_0 counts connected components. H_2 counts enclosed voids. This is why homology is a topological invariant: a doughnut and a coffee cup have the same homology because they have the same "hole structure," while a sphere and a torus differ in H_1. But in the algebraic setting you are learning, all this geometric content is abstracted away: homology is just the quotient ker/im, computable in any abelian category without reference to space at all.

The central theorem is the **long exact sequence in homology**. Given a short exact sequence of chain complexes 0 → A_* → B_* → C_* → 0 (an exact sequence at every degree), there is a naturally induced long exact sequence: ··· → H_n(A) → H_n(B) → H_n(C) →^δ H_{n-1}(A) → H_{n-1}(B) → ··· The map δ, called the **connecting homomorphism**, is the new and non-obvious part. It is constructed by the **snake lemma**: given an element c ∈ H_n(C), lift it to an element b ∈ B_n (possible by surjectivity of B → C), apply the boundary map d to get d(b) ∈ B_{n-1} (which turns out to land in the image of A_{n-1} by exactness), then map it back to A_{n-1} (possible by injectivity of A → B), and observe that it is a cycle. The connecting homomorphism δ sends the homology class [c] to the homology class [a] constructed this way. The proof that δ is well-defined and the resulting sequence is exact is a classic diagram chase.

Why does this matter? The long exact sequence is the main computational engine of homological algebra. To compute the homology of a complex B, it often suffices to find a short exact sequence where A and C are simpler. The long exact sequence then constrains H(B) in terms of H(A) and H(C), and you can often determine H(B) exactly from the resulting constraints. This strategy — compute by fitting into a short exact sequence — underlies the Mayer-Vietoris sequence in topology, the long exact sequence of a pair, and countless spectral sequence arguments.

**Cohomology** arises by reversing all the arrows: take a cochain complex C^* with coboundary maps d^n: C^n → C^{n+1} satisfying d^{n+1} ∘ d^n = 0, and define H^n(C) = ker(d^n) / im(d^{n-1}). In many cases, cohomology carries strictly more structure than homology: the **cup product** makes H*(C; R) into a graded ring, capturing intersection information that homology groups alone cannot see. For spaces, the cup product in singular cohomology detects non-trivial product structures — for instance, the cohomology rings of CP² and S² ∨ S⁴ are not isomorphic even though their cohomology groups are, meaning ring structure distinguishes spaces that groups cannot.

---
id: snake-lemma-algebraic-topology
title: The Snake Lemma
domain: mathematics
course: algebraic-topology
prerequisites:
- id: exact-sequences-homological-algebra
  type: hard
- id: group-homomorphisms
  type: hard
builds-toward:
- relative-homology-long-exact-sequence
- five-lemma
tags: [algebraic-topology, snake-lemma, homological-algebra, connecting-homomorphism]
stage: expert
status: validated
---
# The Snake Lemma

## Core Idea
The snake lemma is the fundamental diagram-chasing result in homological algebra. Given a commutative diagram of abelian groups with exact rows, it produces a connecting homomorphism between the kernels and cokernels of the vertical maps, forming a long exact sequence. The snake lemma is the algebraic engine that produces every long exact sequence in homology and cohomology — the long exact sequence of a pair, Mayer-Vietoris, the long exact sequence of a fibration in homotopy — all are instances of the snake lemma applied to appropriate short exact sequences of chain complexes.

## Questions

```yaml
- question: "The snake lemma applies to a commutative diagram with exact rows. What are the 'kernel' and 'cokernel' objects in the resulting exact sequence?"
  type: multiple-choice
  options:
    - "ker(A → A') and coker(C → C')"
    - "ker(f), ker(g), ker(h) and coker(f), coker(g), coker(h), where f, g, h are the vertical maps in the diagram"
    - "The homology groups of the chain complexes"
    - "The image and kernel of the horizontal maps"
  answer: 1
  explanation: "Given a commutative diagram with exact rows 0 → A → B → C → 0 and 0 → A' → B' → C' → 0, and vertical maps f: A → A', g: B → B', h: C → C', the snake lemma produces: ker(f) → ker(g) → ker(h) →^δ coker(f) → coker(g) → coker(h). The connecting homomorphism δ: ker(h) → coker(f) is the 'snake' — it connects the kernel sequence to the cokernel sequence by weaving through the diagram."

- question: "The connecting homomorphism δ in the snake lemma is defined by a 'diagram chase.' This means it depends on choices of representatives."
  type: true-false
  answer: false
  explanation: "Although the CONSTRUCTION of δ involves choosing lifts (given c ∈ ker(h), choose b ∈ B mapping to c, then g(b) ∈ B' has image 0 in C', so g(b) comes from some a' ∈ A', and δ(c) = [a'] in coker(f)), the result is independent of the choices made. If we chose a different b' mapping to c, then b - b' is in the image of A → B, and tracking through the diagram shows the two choices give the same element of coker(f). This well-definedness is a key part of the snake lemma's proof."

- question: "How does the snake lemma produce the long exact sequence of a pair (X, A) in homology?"
  type: short-answer
  answer: "The short exact sequence of chain complexes 0 → C_*(A) → C_*(X) → C_*(X)/C_*(A) → 0 gives, for each n, a commutative diagram with the boundary maps as vertical arrows. Applying the snake lemma to this diagram (with appropriate identifications) produces the connecting homomorphism ∂: H_n(X, A) → H_{n-1}(A) and the exact sequence H_n(A) → H_n(X) → H_n(X, A) → H_{n-1}(A) → H_{n-1}(X) → .... Iterating across all dimensions and splicing together gives the full long exact sequence of the pair."
  explanation: "More precisely, the snake lemma is applied to the diagram where the rows are the short exact sequences of cycles and boundaries (derived from the chain complex SES), and the vertical maps come from the inclusion of boundaries into cycles. The connecting homomorphism emerges from chasing elements through the diagram, exactly as in the abstract snake lemma. This is the universal mechanism: every long exact sequence in homological algebra arises from the snake lemma applied to a short exact sequence of chain complexes."

- question: "In the movie 'It's My Turn' (1980), the snake lemma is proved on a blackboard. This reflects its status as a foundational result in homological algebra."
  type: true-false
  answer: true
  explanation: "The snake lemma is indeed proved in the opening scene of the 1980 film 'It's My Turn' starring Jill Clayburgh as a mathematics professor. This pop-culture appearance reflects the lemma's status as perhaps the single most important technical result in homological algebra — it is the lemma that makes long exact sequences possible. Every textbook on algebraic topology or homological algebra proves the snake lemma, and it is often the first 'diagram chase' students encounter."
```

## Explainer

The **snake lemma** starts with a commutative diagram of abelian groups with exact rows:

0 -> A -a-> B -b-> C -> 0
     |f      |g      |h
0 -> A' -a'-> B' -b'-> C' -> 0

The lemma asserts the existence of an exact sequence: ker(f) -> ker(g) -> ker(h) -delta-> coker(f) -> coker(g) -> coker(h). The maps between kernels and between cokernels are induced by the horizontal maps (restricted or projected). The **connecting homomorphism** delta : ker(h) -> coker(f) is the new and essential ingredient — it "snakes" from the right side of the kernel row to the left side of the cokernel row, connecting the two halves of the exact sequence.

The construction of delta by **diagram chasing** is the prototypical example of this technique. Given c in ker(h) (so c in C with h(c) = 0): since b : B -> C is surjective, choose b_0 in B with b(b_0) = c. Now g(b_0) in B' has the property that b'(g(b_0)) = h(b(b_0)) = h(c) = 0 (by commutativity and the assumption c in ker(h)). So g(b_0) is in ker(b') = im(a'). Choose a' in A' with a'(a') = g(b_0). Define delta(c) = [a'] in coker(f) = A'/im(f). The proof that this is well-defined (independent of the choices of b_0 and a') and that the resulting sequence is exact is a series of straightforward but careful diagram chases.

The snake lemma produces **long exact sequences** from short exact sequences of chain complexes. Given a short exact sequence of chain complexes 0 -> A_* -> B_* -> C_* -> 0 (exact at each level), the snake lemma applies to the diagram formed by the boundary maps. The connecting homomorphism delta : H_n(C) -> H_{n-1}(A) is exactly the snake lemma's delta applied to an appropriate diagram. Splicing these together across all dimensions gives the long exact sequence: ... -> H_n(A) -> H_n(B) -> H_n(C) -> H_{n-1}(A) -> H_{n-1}(B) -> ... This is a universal construction: every long exact sequence in algebraic topology (the LES of a pair, Mayer-Vietoris, the LES of a fibration, the Gysin sequence, the Wang sequence) is an instance of this pattern.

The snake lemma is the workhorse of **diagram chasing**, a proof technique that manipulates elements through commutative diagrams by following arrows and using exactness to deduce properties. While diagram chasing can feel mechanical, it is powerful: it converts topological questions (how do the homology groups of A, X, and X/A relate?) into routine algebraic verifications. The snake lemma, the five lemma, and the nine lemma form the basic toolkit of diagram chasing. In more advanced settings, these lemmas generalize to abelian categories (where elements may not exist), leading to the theory of derived categories and spectral sequences — but the snake lemma remains the conceptual prototype.

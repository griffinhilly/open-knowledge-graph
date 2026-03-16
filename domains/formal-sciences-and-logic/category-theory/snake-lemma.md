---
id: snake-lemma
title: The Snake Lemma
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: exact-sequences
  type: hard
- id: diagram-chasing
  type: soft
builds-toward:
- homology-and-cohomology
- derived-functors
tags:
- lemma
- homological-algebra
- connecting-map
stage: advanced
status: draft
---

# The Snake Lemma

## Core Idea
The snake lemma constructs a connecting homomorphism between kernels and cokernels from a commutative diagram with exact rows in an abelian category. It produces a long exact sequence of kernels and cokernels from a short exact sequence of complexes. Named for the 'snake-like' path through the diagram, it links local and global homology fundamentally.

## Explainer

From exact sequences, you know that exactness at B in A → B → C means the image of the first map equals the kernel of the second — nothing more and nothing less passes through. From diagram chasing, you're comfortable following elements through commutative squares using exactness to constrain where they can go. The snake lemma is the most powerful result produced by this technique: it constructs a long exact sequence that you could not see by looking at any single row or column of the diagram.

The setup is a **commutative diagram with two exact rows** in an abelian category:

```
0 → A → B → C → 0
    ↓f  ↓g  ↓h
0 → A'→ B'→ C'→ 0
```

The vertical maps f, g, h are arbitrary (not assumed injective or surjective). The snake lemma produces a six-term exact sequence:

`0 → ker(f) → ker(g) → ker(h) →^δ coker(f) → coker(g) → coker(h) → 0`

(with 0s at the ends when the original rows are short exact as shown). The maps ker(f) → ker(g) → ker(h) are induced by the top row, and coker(f) → coker(g) → coker(h) are induced by the bottom row. The remarkable part is the **connecting homomorphism** δ: ker(h) → coker(f), which crosses the diagram diagonally.

The connecting homomorphism δ is constructed by diagram chasing in four steps. Take c ∈ ker(h). (1) Since B → C is surjective (top row is exact and the right 0 implies surjectivity), lift c to some b ∈ B. (2) Apply g to get g(b) ∈ B'. (3) Since h(c) = 0 and the diagram commutes, the image of g(b) in C' is 0, so g(b) lies in the kernel of B' → C', which equals the image of A' → B' by exactness of the bottom row. Lift g(b) to a unique a' ∈ A'. (4) Define δ(c) = [a'] ∈ coker(f) = A' / im(f). The verification that this is well-defined — independent of the choice of lift b in step 1 — is the heart of the proof: two different lifts b and b₁ differ by an element of ker(B → C) = im(A → B), and tracing through shows their corresponding a' values differ by an element of im(f), hence define the same class in coker(f).

Why is it called the **snake lemma**? Draw the morphisms used to construct δ on the diagram: starting at ker(h) ⊂ C (top right), lift left across the top row to B, descend via g to B', move left through the bottom row to A', exit via coker(f) (bottom left). The path traces an S-curve through the diagram — the snake. This mnemonic is reliable, and it correctly describes the directional flow of every diagram chase needed.

The snake lemma is the engine that generates **long exact sequences in homology**. Given a short exact sequence of chain complexes 0 → A_• → B_• → C_• → 0, applying homology gives a commutative diagram at each degree n with the boundary maps ∂_n as vertical arrows. The connecting homomorphism of the snake lemma at each degree produces the connecting map ∂: H_n(C) → H_{n-1}(A), and splicing these together yields the long exact sequence ⋯ → H_n(A) → H_n(B) → H_n(C) → H_{n-1}(A) → ⋯. The entirety of algebraic topology — the Mayer-Vietoris sequence, the long exact sequence of a pair, the Künneth formula — relies on this construction. The snake lemma is where diagram chasing stops being a local technique and becomes a machine for global algebraic invariants.

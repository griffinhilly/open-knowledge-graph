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

## Questions

```yaml
- question: "In the snake lemma, the connecting homomorphism δ: ker(h) → coker(f) is the 'non-obvious' map in the long exact sequence. What makes it non-obvious compared to the other maps?"
  type: multiple-choice
  options:
    - "Because it requires inverting one of the vertical maps, which may not exist"
    - "Because it crosses the diagram diagonally by composing maps from different rows, and its well-definedness requires proof since it involves a non-unique lift"
    - "Because it only exists when f and h are isomorphisms"
    - "Because it goes from a cokernel to a kernel, reversing the usual direction of maps"
  answer: 1
  explanation: "The maps ker(f) → ker(g) → ker(h) are simply the top-row maps restricted to kernels — completely natural. Similarly coker(f) → coker(g) → coker(h) come from the bottom row. But δ travels diagonally: take c ∈ ker(h), lift to b in the top row (non-unique!), apply g vertically, then lift backwards through the bottom row to A', then project to coker(f). The proof that δ is well-defined — independent of which lift b you choose — is the substantive mathematical content of the lemma. No inverses are needed; exactness provides the necessary uniqueness."

- question: "In the snake lemma setup, suppose f: A → A' is surjective and h: C → C' is injective. What can you conclude from the long exact sequence?"
  type: multiple-choice
  options:
    - "g must be an isomorphism"
    - "ker(g) ≅ ker(f) and coker(g) ≅ coker(h), but g need not be an isomorphism"
    - "The connecting homomorphism δ vanishes, so ker(h) ≅ 0"
    - "g must be surjective but not necessarily injective"
  answer: 1
  explanation: "If f is surjective then coker(f) = 0; if h is injective then ker(h) = 0. The long exact sequence becomes 0 → ker(f) → ker(g) → 0 → 0 → coker(g) → coker(h) → 0. Exactness forces ker(g) ≅ ker(f) and coker(g) ≅ coker(h). But to conclude g is an isomorphism we would also need f injective (ker(f) = 0) and h surjective (coker(h) = 0). With only f surjective and h injective, g is not generally an isomorphism. The snake lemma's exact sequence precisely encodes what can and cannot be concluded."

- question: "The connecting homomorphism δ is well-defined because any two different choices of lift b for c ∈ ker(h) yield elements of A' that differ by an element of im(f), hence the same class in coker(f)."
  type: true-false
  answer: true
  explanation: "This is the heart of the well-definedness proof. Given c ∈ ker(h), any two lifts b and b₁ to B satisfy b − b₁ ∈ ker(B → C) = im(A → B) by exactness of the top row. Applying g to b − b₁ and tracing through shows the corresponding pre-images a', a'₁ in A' differ by an element in im(f). Therefore [a'] = [a'₁] in coker(f) = A'/im(f). Without this, δ would be a multi-valued relation rather than a function — the entire lemma would fail."

- question: "The snake lemma requires the vertical maps f, g, h to be injective or surjective for the connecting homomorphism to be constructible."
  type: true-false
  answer: false
  explanation: "The vertical maps f, g, h can be arbitrary homomorphisms — no injectivity or surjectivity is assumed. What IS required is that the two horizontal rows are exact (as given by the short exact sequences 0 → A → B → C → 0 and 0 → A'→ B'→ C'→ 0). The construction of δ uses the surjectivity of B → C and injectivity of A'→ B', which are properties of the horizontal maps, not the vertical ones. Arbitrary vertical maps still yield the connecting homomorphism and the full exact sequence of kernels and cokernels."

- question: "Why does the snake lemma's connecting homomorphism δ produce long exact sequences in homology when applied to short exact sequences of chain complexes?"
  type: short-answer
  answer: "A short exact sequence of chain complexes 0 → A_• → B_• → C_• → 0 gives a commutative diagram at each degree n with boundary maps ∂_n as vertical arrows. The snake lemma applied at degree n produces a six-term exact sequence involving H_n(A), H_n(B), H_n(C) and their shifted versions. The connecting homomorphism δ: H_n(C) → H_{n-1}(A) stitches the degree-n piece to the degree-(n-1) piece. Splicing these across all degrees yields the long exact sequence ⋯ → H_n(A) → H_n(B) → H_n(C) → H_{n-1}(A) → ⋯, the foundational tool underlying Mayer-Vietoris and the long exact sequence of a pair."
  explanation: "The snake lemma is not just an abstract algebraic curiosity — it is the machine that generates the computational tools of algebraic topology. Every time homology 'jumps' from one space to another via a connecting map, the snake lemma is operating behind the scenes."
```

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

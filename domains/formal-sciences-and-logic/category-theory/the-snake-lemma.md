---
id: the-snake-lemma
title: The Snake Lemma
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: exact-sequences-in-abelian-categories
  type: hard
- id: commutative-diagrams-and-composition
  type: hard
builds-toward:
  - the-five-lemma
tags:
- homological-algebra
- diagram-chasing
- connecting-morphism
stage: expert
status: validated
---
# The Snake Lemma

## Core Idea
The snake lemma is a fundamental result in homological algebra stating that given a commutative diagram of short exact sequences in an abelian category, there exists a natural connecting morphism (the 'snake') from the kernel of one morphism to the cokernel of another, and the resulting six-term sequence is exact. It is a premier tool for deriving long exact sequences from short ones.

## How It's Best Learned
Draw the full commutative diagram and carefully trace through the construction of the connecting morphism using diagram chasing. Apply it to derive long exact sequences in homology and cohomology. Work through its proof in a concrete category first (abelian groups or modules).

## Common Misconceptions
The connecting morphism is not arbitrary; its construction involves careful diagram chasing and depends on exactness. Students sometimes apply the snake lemma without verifying that the input diagram genuinely consists of short exact sequences.

## Questions

```yaml
- question: "In the snake lemma, the connecting morphism δ maps between which objects?"
  type: multiple-choice
  options:
    - "From coker α to ker γ, providing a bridge from the top row to the bottom row"
    - "From ker γ to coker α, crossing from the bottom-right kernel to the top-left cokernel"
    - "From ker β to coker β, staying within the middle column of the diagram"
    - "From H_n(C) to H_{n-1}(A), directly producing the long exact sequence in homology"
  answer: 1
  explanation: "The six-term exact sequence produced by the snake lemma is: ker α → ker β → ker γ →^δ coker α → coker β → coker γ. The connecting morphism δ maps from ker γ (bottom-right) to coker α (top-left) — it 'snakes' diagonally across the diagram, which is why the lemma has its name. Option D describes what δ becomes when applied to chain complexes, but in the raw snake lemma, δ connects ker γ to coker α, not homology groups."

- question: "The well-definedness of δ(x) — that different choices of preimage b ∈ B of x ∈ ker γ yield the same class in coker α — depends on which property of the diagram?"
  type: multiple-choice
  options:
    - "The commutativity of the right square (involving β and γ) only"
    - "The exactness of the top row: any two preimages differ by an element of ker(B → C) = im(A → B), which maps into im(A' → B') via commutativity, giving the same class in coker α"
    - "The injectivity (monomorphism) of the map B → C in the top row"
    - "The surjectivity (epimorphism) of the map B' → C' in the bottom row"
  answer: 1
  explanation: "If b and b' are both preimages of x ∈ ker γ under the surjection B → C, then b - b' ∈ ker(B → C) = im(A → B) by exactness of the top row at B. So b - b' = f(a) for some a ∈ A. Applying β: β(b) - β(b') = β(f(a)) = g(α(a)) by commutativity, where g: A' → B' is the bottom-row injection. So α(a) ∈ A' maps to the same element whether we started with b or b', and the cokernel class [α(a)] ∈ coker α is well-defined. Exactness at B is essential; without it, the preimage difference need not land in im(A → B), and the construction fails."

- question: "The six-term sequence ker α → ker β → ker γ →^δ coker α → coker β → coker γ produced by the snake lemma is exact at every term."
  type: true-false
  answer: true
  explanation: "This is the full content of the snake lemma: not only does the connecting morphism δ exist, but the resulting six-term sequence is exact throughout — at ker β, at ker γ, at coker α, and at coker β. Exactness at each term requires a separate argument: at ker γ, one shows im(ker β → ker γ) = ker δ; at coker α, one shows im δ = ker(coker α → coker β); and so on. Together, these exactness conditions are what make the lemma powerful: they guarantee that no information is lost or duplicated as you move through the sequence."

- question: "The snake lemma can be applied to any commutative diagram of abelian groups with morphisms between them, even if the rows of the diagram are not exact sequences."
  type: true-false
  answer: false
  explanation: "Exactness of both rows is essential, not optional. Every step of the connecting morphism's construction uses exactness: the existence of the preimage b ∈ B (uses surjectivity B → C, hence exactness of the top row at C), the fact that β(b) lies in ker(B' → C') (uses commutativity and ker γ ∋ x), the existence of a' ∈ A' mapping to β(b) (uses exactness of the bottom row at B'), and the well-definedness argument (uses exactness of the top row at B). Without exact rows, none of these existence or uniqueness claims hold, and the connecting morphism cannot be defined."

- question: "Why is the snake lemma described as the 'engine' that produces long exact sequences in homology from short exact sequences of chain complexes?"
  type: short-answer
  answer: "Given a short exact sequence of chain complexes 0 → A_• → B_• → C_• → 0, at each degree n there is a commutative diagram with exact rows: the top row involves the boundary maps of A_n and B_n, the bottom row involves B_n and C_n. Applying the snake lemma to this diagram produces a connecting morphism δ_n: ker(∂_C at C_n) → coker(∂_A at A_{n-1}). Interpreting these in terms of homology (ker ∂ / im ∂ = H_n), the connecting morphisms become δ_n: H_n(C) → H_{n-1}(A). The snake lemma's exactness then stitches together the fragments H_n(A) → H_n(B) → H_n(C) from each degree with the connecting morphisms into the long exact sequence ⋯ → H_n(A) → H_n(B) → H_n(C) →^δ H_{n-1}(A) → ⋯. Without the snake lemma's existence and exactness guarantee, there would be no systematic bridge between short exact sequences and long exact sequences of invariants."
  explanation: "This application — deriving long exact sequences in homology — is why the snake lemma appears at the very beginning of algebraic topology and homological algebra. It is not merely a technical result; it is the mechanism that makes the theory computationally useful."
```

## Explainer

From your study of exact sequences, you know that a sequence A → B → C is exact at B when im(A → B) = ker(B → C): every element arriving from A is exactly the set of elements that map to zero in C. A short exact sequence 0 → A → B → C → 0 is exact at every term, which means A injects into B and B surjects onto C with kernel exactly the image of A. From abelian categories, you have the machinery of kernels, cokernels, and the fact that every morphism factors as an epimorphism followed by a monomorphism. The snake lemma takes these tools and uses them to build a surprising bridge across two short exact sequences.

The setup is a commutative diagram with exact rows: one short exact sequence 0 → A → B → C → 0 across the top, another 0 → A' → B' → C' → 0 across the bottom, and vertical morphisms α: A → A', β: B → B', γ: C → C' connecting them. The snake lemma asserts that there is a natural exact sequence of six terms: **ker α → ker β → ker γ →^δ coker α → coker β → coker γ**, where the first two and last two arrows are induced by the original row maps, and **δ** is the connecting morphism that crosses from one row to the other.

The construction of δ is the heart of the lemma and an introduction to **diagram chasing**. To define δ(x) for x ∈ ker γ: since γ(x) = 0, start from some preimage b ∈ B of x under the top row's surjection (this uses exactness). Apply β to get β(b) ∈ B'. Since the square commutes and x maps to 0, β(b) is in the kernel of B' → C', which by exactness of the bottom row means β(b) is the image of some a' ∈ A'. Set δ(x) = [a'] ∈ coker α. The construction requires checking: (1) a' exists because of exactness, (2) the cokernel class [a'] is independent of the choice of preimage b because any two choices differ by an element in ker(B → C) = im(A → B), which maps to im(A' → B') under commutativity, (3) the resulting map δ is a morphism.

The snake lemma is the engine behind **long exact sequences in homology**. Given a short exact sequence of chain complexes 0 → A_• → B_• → C_• → 0, applying the snake lemma level by level produces connecting morphisms δ_n: H_n(C) → H_{n-1}(A) and assembles the fragments into a long exact sequence ⋯ → H_n(A) → H_n(B) → H_n(C) →^δ H_{n-1}(A) → ⋯. This is why the snake lemma appears at the very beginning of any serious treatment of algebraic topology or homological algebra: it is the machine that converts short exact sequences of spaces or modules into long exact sequences of their invariants.

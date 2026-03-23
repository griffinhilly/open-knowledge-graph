---
id: the-five-lemma
title: The Five Lemma and Related Results
domain: formal-sciences-and-logic
course: category-theory
prerequisites:
- id: abelian-categories
  type: hard
- id: exact-sequences-in-abelian-categories
  type: hard
builds-toward: []
tags:
- homological-algebra
- isomorphism-criteria
- diagram-chasing
stage: expert
status: validated
---
# The Five Lemma and Related Results

## Core Idea
The five lemma states that if two rows of a commutative diagram are exact and four of the five vertical morphisms are isomorphisms, then so is the fifth—providing a powerful criterion for establishing isomorphisms without explicit computation. The short five lemma and related results like the four lemma are equally useful for showing injectivity and surjectivity.

## How It's Best Learned
Begin with the standard five lemma and verify its proof by diagram chasing. Apply it to prove that certain canonical morphisms are isomorphisms. Explore variants: the four lemma, the three lemma, and how they all follow from the same principles.

## Common Misconceptions
The five lemma requires exactness of both rows; without exactness, the conclusion fails. Also, the positioning of the morphisms matters—swapping the roles of exactness and commutativity breaks the result.

## Questions

```yaml
- question: "You have a commutative diagram with two rows and five vertical morphisms α, β, γ, δ, ε. All four outer morphisms (α, β, δ, ε) are isomorphisms. A student concludes that γ must also be an isomorphism based on commutativity alone — without checking the rows. What is the flaw in this reasoning?"
  type: multiple-choice
  options:
    - "The student needs to check that α and ε are both surjective, not just isomorphisms"
    - "The five lemma requires both rows to be exact sequences; commutativity alone is not sufficient"
    - "The conclusion is only valid if the diagram has at least six columns"
    - "The student should apply the short five lemma instead, which does not require exactness"
  answer: 1
  explanation: "Commutativity alone is not enough — exactness of both rows is essential. The entire diagram-chasing proof of the five lemma uses exactness at every position: to lift an element into a kernel, to assert that something in a kernel comes from the previous term, or to conclude that a residual is zero. Without exactness, the chains of logical steps break down and the conclusion can fail. The common misconception is to think that commutativity plus four isomorphisms is sufficient; it is not."

- question: "In algebraic topology, a geometric map f: X → Y induces a map on long exact sequences of a pair. At every position except one, the induced maps on homology groups are known to be isomorphisms. What is the most efficient way to conclude that the remaining map is also an isomorphism?"
  type: multiple-choice
  options:
    - "Compute the remaining homology group directly using the definition"
    - "Apply the five lemma: the map of long exact sequences with four known isomorphisms forces the fifth by diagram chasing"
    - "Use the universal coefficient theorem to relate homology to cohomology at the unknown position"
    - "Apply Mayer-Vietoris to decompose the spaces and compute the missing group"
  answer: 1
  explanation: "This is the canonical application of the five lemma in topology. A map of long exact sequences is a commutative diagram with two exact rows. If four consecutive vertical maps are isomorphisms, the five lemma immediately gives the fifth. This avoids direct computation — which may be unavailable or extremely difficult — and replaces it with a structural argument. Direct computation, universal coefficients, and Mayer-Vietoris are all more expensive tools for what diagram chasing handles automatically."

- question: "The short five lemma states: given a commutative diagram with two short exact sequences 0 → A → B → C → 0 as rows, if the vertical maps at A and C are isomorphisms, then the vertical map at B is also an isomorphism."
  type: true-false
  answer: true
  explanation: "The short five lemma is the most frequently applied special case. It is the five lemma applied to a diagram of the form 0 → A → B → C → 0 on both rows (where the '0 → A' and 'C → 0' positions automatically provide isomorphisms at the trivial objects). Knowing isomorphisms at A and C forces an isomorphism at B. This appears constantly when comparing two extensions of C by A: a map of short exact sequences with isomorphisms at both ends implies the middle map is an isomorphism, meaning the extensions are equivalent."

- question: "The five lemma can be applied to any commutative diagram with five columns, even when the rows are not exact sequences, as long as the outer four morphisms are isomorphisms."
  type: true-false
  answer: false
  explanation: "Exactness of both rows is a non-negotiable hypothesis. The proof of the five lemma at every step uses exactness to conclude that an element in a kernel arose from a previous term — without this, the diagram chase cannot proceed. In a commutative diagram without exactness, four outer isomorphisms tell you very little about the middle morphism. The five lemma is not simply a 'four isomorphisms imply the fifth' result for arbitrary commutative diagrams."

- question: "Describe the diagram-chasing argument for why γ must be injective in the five lemma. What specific roles do exactness and commutativity each play in the proof?"
  type: short-answer
  answer: "Suppose γ(c) = 0. Commutativity says the map from C to D' via γ then the bottom row equals the map via the top row then δ: so δ(image of c in D) = 0. Since δ is injective (an isomorphism), the image of c in D is 0. Exactness at D says ker(D → E) = im(C → D), so c maps to 0 in D means c is in the kernel of C → D; by exactness at C in the top row, c comes from some b in B. Now apply β: commutativity gives the image of b in B' maps to the image of c = 0 in C'. Since β is injective, c in C' coming from 0... actually β(b) maps to 0 in C'. By exactness at B' in the bottom row, β(b) comes from some a' in A'. Since α is surjective, a' = α(a) for some a. By commutativity, α(a) maps to β(b), but also a maps to b via exactness at B in the top row would give b = 0 if the sequence is correct... Exactness provides the 'kernel = image' conditions that let you track the element back and forward; commutativity ensures the paths around the diagram give consistent results, allowing conclusions about one morphism from information about adjacent ones."
  explanation: "The proof splits into two halves (injectivity and surjectivity), each a chain of 4–5 standard moves: map an element forward or backward, apply commutativity to change paths, use exactness to lift into a kernel or conclude an element is zero, use an isomorphism hypothesis to conclude injectivity or surjectivity. The power of the argument is that it never requires knowing what the objects actually are — it works in any abelian category."
```

## Explainer

From your study of abelian categories and exact sequences, you know that exactness at an object M means im(f) = ker(g) for the morphisms arriving and departing. **Diagram chasing** is the technique of proving facts about morphisms by following elements through a commutative diagram, using exactness conditions to lift, map, and conclude. The **five lemma** is the central theorem of diagram chasing: it converts a local question ("is this morphism an isomorphism?") into a structural question answered by neighboring data.

The setup is a commutative diagram with two exact rows and five vertical morphisms:

A → B → C → D → E
↓α  ↓β  ↓γ  ↓δ  ↓ε
A'→ B'→ C'→ D'→ E'

If α, β, δ, ε are all isomorphisms and both rows are exact, then γ is also an isomorphism. The proof splits into two halves. **Injectivity of γ**: suppose γ(c) = 0. Use commutativity and exactness to push c rightward — δ(image of c in D) = 0, so since δ is injective, the image is 0, meaning c comes from B by exactness. Then push leftward — β's injectivity forces c = 0. **Surjectivity of γ**: given c' ∈ C', push it rightward to D'; since δ is surjective, lift to D; use exactness at D to track it back to C; check that the residual in C' is zero using β's surjectivity. Each half is a short chain of standard moves — map, use commutativity, use exactness, use isomorphism — all following from definitions.

The **short five lemma** is the most frequently applied variant: given 0 → A → B → C → 0 on both rows (short exact sequences), with isomorphisms at A and C, the middle morphism at B is also an isomorphism. This appears constantly whenever two extensions of C by A are compared — if there exists a map of short exact sequences with isomorphisms at both ends, the middle map is automatically an isomorphism, meaning the extensions are equivalent. The **four lemma** weakens the hypothesis further: with only two or three outer isomorphisms, you can still conclude injectivity or surjectivity (but not necessarily both) at the middle position.

The broader significance is methodological. In algebraic topology, algebraic geometry, and homological algebra, you frequently want to show that a natural map between two invariants — a map of homology groups, of cohomology sheaves, of Ext groups — is an isomorphism. Direct computation is rarely available. The five lemma provides a structural route: construct a morphism of long exact sequences, establish isomorphisms at enough positions by independent means, and conclude the remaining isomorphisms by diagram chasing. Long exact sequences in homology (from a pair of spaces), in sheaf cohomology (from a short exact sequence of sheaves), and in derived categories all produce five-lemma situations as a matter of routine. The lemma is the grammar rule; the long exact sequence is the sentence it appears in.

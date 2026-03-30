---
id: five-lemma
title: The Five Lemma
domain: mathematics
course: algebraic-topology
prerequisites:
- id: exact-sequences-homological-algebra
  type: hard
- id: snake-lemma-algebraic-topology
  type: soft
- id: group-homomorphisms
  type: hard
builds-toward:
- kunneth-formula
tags: [algebraic-topology, five-lemma, diagram-chasing, homological-algebra]
stage: expert
status: validated
---
# The Five Lemma

## Core Idea
The five lemma states: given a commutative diagram with two exact rows of five terms each, if four of the five vertical maps are isomorphisms, then the fifth is also an isomorphism. More precisely, if the first and third vertical maps are surjective and the second and fourth are injective, then the middle map is injective; the dual statement gives surjectivity. The five lemma is the standard tool for proving that a map between homology groups is an isomorphism, by embedding it in a map of long exact sequences where the surrounding terms are known.

## Questions

```yaml
- question: "In the five lemma diagram with exact rows and vertical maps α, β, γ, δ, ε, the conclusion that γ is an isomorphism requires which conditions?"
  type: multiple-choice
  options:
    - "α, β, δ, ε are all isomorphisms"
    - "β and δ are isomorphisms, α is surjective, and ε is injective"
    - "All vertical maps are surjective"
    - "The rows are split exact"
  answer: 1
  explanation: "The five lemma has two halves. Injectivity of γ requires: β injective and α surjective (these are used in the diagram chase to show γ(x) = 0 implies x = 0). Surjectivity of γ requires: δ surjective and ε injective. If all four outer maps are isomorphisms, both conditions hold and γ is an isomorphism. The weaker conditions (B) are sufficient and are sometimes needed in practice when the outer maps are not full isomorphisms."

- question: "The five lemma is often used as follows: two long exact sequences are connected by a map, and isomorphisms at four terms force an isomorphism at the fifth. Give an example from algebraic topology."
  type: short-answer
  answer: "Example: proving that a homotopy equivalence f: X → Y induces isomorphisms on relative homology H_n(X, A) → H_n(Y, B) when f maps A to B. The induced map of long exact sequences of pairs gives a commutative diagram where f_*: H_n(A) → H_n(B) and f_*: H_n(X) → H_n(Y) are isomorphisms (by homotopy invariance). The five lemma then forces f_*: H_n(X, A) → H_n(Y, B) to be an isomorphism at each term."
  explanation: "Another standard application: proving that simplicial homology equals singular homology. One constructs a map from the simplicial chain complex to the singular chain complex, shows it is a chain map, and uses the five lemma on the resulting maps of long exact sequences (after establishing the result for simplices and cones). The five lemma reduces the problem from all spaces to elementary building blocks."

- question: "The five lemma works only for abelian groups (or more generally, abelian categories)."
  type: true-false
  answer: true
  explanation: "The proof of the five lemma uses diagram chasing, which relies on the ability to add, subtract, and manipulate elements through homomorphisms — operations that require the abelian group structure. In non-abelian settings (e.g., groups that are not abelian), the five lemma can fail. There is a version for groups (using normal subgroups and quotients), but it requires additional hypotheses. For algebraic topology, where homology and cohomology are abelian groups, the standard abelian five lemma is sufficient."

- question: "State and prove the 'short five lemma': if 0 → A → B → C → 0 and 0 → A' → B' → C' → 0 are exact with α: A → A' and γ: C → C' isomorphisms, then β: B → B' is an isomorphism."
  type: short-answer
  answer: "This is the five lemma applied to the diagram 0 → A → B → C → 0 over 0 → A' → B' → C' → 0, where the maps from 0 to 0 on each end are trivially isomorphisms. Injectivity of β: suppose β(b) = 0. Then γ(p(b)) = p'(β(b)) = 0, and since γ is injective, p(b) = 0. By exactness, b = i(a) for some a. Then i'(α(a)) = β(i(a)) = β(b) = 0, so α(a) = 0 (since i' is injective). Since α is injective, a = 0, so b = 0. Surjectivity is similar, using surjectivity of α and γ."
  explanation: "The short five lemma is the most commonly used special case. It says that in a morphism of short exact sequences, if the 'ends' are isomorphisms, the 'middle' is too. This is used constantly: to show B ≅ B', it suffices to show A ≅ A' and C ≅ C' with compatible maps, plus exactness of both rows."
```

## Explainer

The **five lemma** is the most frequently used diagram lemma in homological algebra and algebraic topology. Consider a commutative diagram with two exact rows of five terms, connected by five vertical maps:

A_1 -> A_2 -> A_3 -> A_4 -> A_5
|alpha  |beta  |gamma  |delta  |epsilon
B_1 -> B_2 -> B_3 -> B_4 -> B_5

The five lemma states: if alpha, beta, delta, and epsilon are isomorphisms, then gamma is an isomorphism. The proof is a diagram chase in two parts (injectivity and surjectivity of gamma), each using only two of the four assumed isomorphisms.

**Injectivity of gamma**: Suppose gamma(a_3) = 0 in B_3. We want to show a_3 = 0. Map a_3 to A_4: the element d_3(a_3) in A_4 maps to d_3'(gamma(a_3)) = d_3'(0) = 0 in B_4 by commutativity. Since delta is injective, d_3(a_3) = 0. By exactness of the top row at A_3, a_3 = d_2(a_2) for some a_2 in A_2. Now beta(a_2) maps to gamma(d_2(a_2)) = gamma(a_3) = 0 in B_3, so d_2'(beta(a_2)) = 0 in B_3. By exactness of the bottom row at B_2, beta(a_2) = d_1'(b_1) for some b_1 in B_1. Since alpha is surjective, b_1 = alpha(a_1) for some a_1. Then beta(a_2) = d_1'(alpha(a_1)) = beta(d_1(a_1)) by commutativity. Since beta is injective, a_2 = d_1(a_1). Therefore a_3 = d_2(a_2) = d_2(d_1(a_1)) = 0 by exactness (im(d_1) subset ker(d_2)).

**Surjectivity of gamma** proceeds dually: start with b_3 in B_3, use surjectivity of delta to control d_3'(b_3), use exactness and surjectivity of alpha to adjust, and arrive at a preimage in A_3.

The five lemma is used in algebraic topology whenever a map between spaces induces a map of long exact sequences. For instance, to show that a map f : X -> Y inducing isomorphisms on the homology of subspaces A subset X and B subset Y also induces isomorphisms on relative homology H_*(X, A) -> H_*(Y, B): the long exact sequences of the pairs (X, A) and (Y, B) are connected by f_*, and the five lemma (applied term by term) upgrades the known isomorphisms on H_*(A) and H_*(X) to isomorphisms on H_*(X, A).

The **short five lemma** (the special case where A_1 = A_5 = B_1 = B_5 = 0) is the most common version in practice. It states: in a morphism of short exact sequences, if the "end" maps are isomorphisms, the "middle" map is too. This is used to show that homology is an invariant of the chain homotopy type, to prove the uniqueness of homology theories satisfying the Eilenberg-Steenrod axioms, and to compare different definitions of cohomology. The five lemma, together with the snake lemma, forms the core technical foundation of homological algebra.

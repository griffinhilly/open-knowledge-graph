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
The five lemma states: given a commutative diagram with two exact rows of five terms each, if the four outer vertical maps are isomorphisms, then the middle one is also an isomorphism. More precisely, if the first vertical map is surjective and the second and fourth are injective, then the middle map is injective; dually, if the second and fourth are surjective and the fifth is injective, then the middle map is surjective. The five lemma is the standard tool for proving that a map between homology groups is an isomorphism, by embedding it in a map of long exact sequences where the surrounding terms are known.

## How It's Best Learned
Prove the short five lemma yourself with the diagram drawn large, naming each element as you chase it. Then prove the full five lemma, with vertical maps α, β, γ, δ, ε, and write down which hypothesis each step of the injectivity chase for γ used: β and δ injective, α surjective. Do the same for surjectivity. Finally, apply it to the map of long exact sequences of pairs for a map (X, A) -> (Y, B) that is a homology isomorphism on X and on A.

## Common Misconceptions
- If A ≅ A' and C ≅ C', then any B and B' in short exact sequences with them are isomorphic. (The lemma needs a map β making the diagram commute. Z/4 and Z/2 ⊕ Z/2 both sit between Z/2 and Z/2.)
- All four outer maps must be isomorphisms. (Less is enough: β and δ isomorphisms, α surjective and ε injective.)
- Four isomorphisms in any positions force the fifth map to be an isomorphism. (The conclusion is about the middle map. With top row Z -> 0 -> 0 -> 0 -> 0 and bottom row all zeros, the last four maps are isomorphisms but Z -> 0 is not.)

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
  explanation: "The five lemma has two halves. Injectivity of γ requires: β and δ injective and α surjective (these are used in the diagram chase to show γ(x) = 0 implies x = 0). Surjectivity of γ requires: β and δ surjective and ε injective. If all four outer maps are isomorphisms, both conditions hold and γ is an isomorphism. The weaker conditions (B) are sufficient and are sometimes needed in practice when the outer maps are not full isomorphisms."

- question: "The five lemma is often used as follows: two long exact sequences are connected by a map, and isomorphisms at the four surrounding terms force an isomorphism at the middle term. Give an example from algebraic topology."
  type: short-answer
  answer: "Example: proving that a homotopy equivalence f: X → Y induces isomorphisms on relative homology H_n(X, A) → H_n(Y, B) when f maps A to B. The induced map of long exact sequences of pairs gives a commutative diagram where f_*: H_n(A) → H_n(B) and f_*: H_n(X) → H_n(Y) are isomorphisms (by homotopy invariance). The five lemma then forces f_*: H_n(X, A) → H_n(Y, B) to be an isomorphism at each term."
  explanation: "Another standard application: proving that simplicial homology equals singular homology. One constructs a map from the simplicial chain complex to the singular chain complex, shows it is a chain map, and uses the five lemma on the resulting maps of long exact sequences (after establishing the result for simplices and cones). The five lemma reduces the problem from all spaces to elementary building blocks."

- question: "The five lemma works only for abelian groups (or more generally, abelian categories)."
  type: true-false
  answer: false
  explanation: "The five lemma also holds for groups that are not abelian. The same diagram chase works in multiplicative notation, because it uses only kernels, images, exactness and the group operation. It also holds in any abelian category. It can fail for pointed sets, which matters at the low end of the long exact sequence of homotopy groups, where π_0 terms are only pointed sets. For homology and cohomology, which are abelian groups, the standard version is all that is needed."

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

---
id: bijections-establish-equinumerosity
title: Bijections and Cardinality Equivalence
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: naive-set-theory
  type: hard
builds-toward:
- cardinality-and-equinumerosity
- infinite-cardinal-numbers
tags:
- cardinality
- bijections
- functions
- equivalence
stage: formal-systems
status: validated
---

# Bijections and Cardinality Equivalence

## Core Idea
Two sets have the same cardinality if and only if there exists a bijection (one-to-one and onto function) between them. This formal definition replaces intuitive notions of 'same size' with a precise mathematical relation. Bijections establish an equivalence relation on sets, partitioning them into cardinality classes.

## How It's Best Learned
Start with finite examples: show bijections between sets of different sizes establish equality. Then apply to countably infinite sets, comparing ℕ with ℤ and ℚ via explicit bijections.

## Common Misconceptions
- Assuming infinite sets cannot be equinumerous with proper subsets (forgetting that Dedekind-infinite sets can be).
- Confusing bijections with other function types; bijections require both injection AND surjection.

## Questions

```yaml
- question: "Which function establishes that the set of even natural numbers E = {0, 2, 4, 6, ...} has the same cardinality as the natural numbers ℕ = {0, 1, 2, 3, ...}?"
  type: multiple-choice
  options:
    - "f(n) = n + 2, which shifts each natural number up by 2"
    - "f(n) = 2n, which maps every natural number to a distinct even number and covers all of E"
    - "No such function can exist because E is a proper subset of ℕ and must therefore be smaller"
    - "f(n) = n², because squares grow fast enough to reach all even numbers"
  answer: 1
  explanation: "f(n) = 2n is injective (if 2m = 2n then m = n, so no two inputs share an output) and surjective onto E (every even number 2k is the image of k). Together these make it a bijection from ℕ to E, proving |ℕ| = |E|. Option C is the central misconception: for infinite sets, a proper subset CAN have the same cardinality as the whole. This is Dedekind's definition of an infinite set. Option D — f(n) = n² — is injective but not surjective onto E (for example, 6 is not a perfect square)."

- question: "A student argues that the integers ℤ must have larger cardinality than the natural numbers ℕ, because ℤ contains all of ℕ plus all negative integers. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — ℤ does have strictly larger cardinality than ℕ by Cantor's theorem"
    - "The student is confusing subset containment with cardinality; a bijection from ℕ to ℤ can be constructed, showing they are equinumerous"
    - "The reasoning is correct for finite sets but the conclusion happens to be wrong for infinite sets for unrelated reasons"
    - "ℤ is actually smaller than ℕ because the negative integers cancel out the positive ones"
  answer: 1
  explanation: "The bijection from ℕ to ℤ interleaves positives and negatives: 0↦0, 1↦1, 2↦−1, 3↦2, 4↦−2, ... This mapping is injective and surjective, so |ℕ| = |ℤ|. The student's error is assuming that 'contains more elements' translates to 'has larger cardinality' for infinite sets — an intuition that holds for finite sets but breaks down for infinite ones. Cardinality is defined exclusively by bijection existence, not by subset relationships."

- question: "If set A is a proper subset of set B (meaning A ⊂ B and A ≠ B), then A always has strictly smaller cardinality than B."
  type: true-false
  answer: false
  explanation: "This is true for finite sets but false for infinite sets. The set of even natural numbers is a proper subset of ℕ, yet the bijection f(n) = 2n shows they have equal cardinality. More strikingly, this property — being equinumerous with a proper subset — is Dedekind's definition of an infinite set. The failure of the 'proper subset means smaller' intuition for infinite sets is not a flaw in the mathematics; it is precisely what distinguishes infinite cardinality from finite cardinality."

- question: "A bijection between two sets A and B is a function that is both injective (one-to-one) and surjective (onto)."
  type: true-false
  answer: true
  explanation: "Injectivity ensures no two elements of A map to the same element of B (nothing in B is 'hit twice'). Surjectivity ensures every element of B is mapped to by at least one element of A (nothing in B is 'left out'). Together they guarantee a perfect pairing: each element of A is paired with exactly one element of B and vice versa. Bijections are also exactly the functions that have a two-sided inverse. If either condition fails — an injection that misses some elements of B, or a surjection with collisions — you cannot form a perfect pairing and cardinality equality is not established."

- question: "Why is the existence of a bijection the right definition of 'same cardinality,' and what makes this definition more powerful than simply counting elements when dealing with infinite sets?"
  type: short-answer
  answer: "Counting works for finite sets by assigning consecutive natural numbers 1, 2, 3, ... to elements. But 'counting' an infinite set would never terminate — you can never finish and declare a final tally. The bijection definition sidesteps counting entirely: instead of counting each set separately and comparing totals, you directly exhibit a perfect correspondence between the two sets. If every element of A is paired with exactly one element of B, and every element of B is covered, the sets are 'the same size' by definition — regardless of whether they are finite or infinite. This definition also extends naturally to comparing different sizes of infinity: ℕ and ℝ cannot be put in bijection (Cantor's diagonal argument), so they have different cardinalities, which is a meaningful mathematical fact that the 'just count them' approach cannot express."
  explanation: "The power of this definition also comes from being an equivalence relation: reflexive (every set bijects with itself via the identity), symmetric (bijections are invertible), and transitive (compositions of bijections are bijections). This partitions all sets into cardinality classes and enables rigorous comparison of all sets, finite and infinite."
```

## Explainer

From naive set theory, you know how to describe sets and functions. Now a natural question arises: when do two sets have "the same number of elements"? For finite sets you can just count. But Cantor's insight, which launched the mathematical study of infinity, was that the right definition in all cases — finite or infinite — is to use **bijections**. Two sets A and B have the same **cardinality** if there exists a bijection f: A → B: a function that is both **injective** (one-to-one: distinct inputs map to distinct outputs, so nothing in B is hit twice) and **surjective** (onto: every element of B is mapped to by at least one element of A). Together these guarantee a perfect pairing with nothing left over on either side.

For finite sets, this matches intuition precisely. A bijection between two finite sets is exactly a perfect pairing — like matching dancers to partners one-to-one with none left unpartnered. If such a pairing exists, the two sets must be the same size. The bijection replaces the need to count: rather than counting each set separately and comparing the numbers, you directly exhibit the correspondence. The key shift is moving from "count then compare" to "pair directly" — a shift that pays off enormously when dealing with infinite sets where counting breaks down.

The payoff is immediate and counterintuitive. Consider the even natural numbers E = {0, 2, 4, 6,...}. Intuitively, E seems "smaller" than ℕ = {0, 1, 2, 3,...} — it misses all the odd numbers. But the function f(n) = 2n is a bijection from ℕ to E: it is injective (different n's give different 2n's) and surjective (every even number 2k is the image of k). By Cantor's definition, ℕ and E have the same cardinality. This is **Dedekind-infinity**: a set is Dedekind-infinite if it can be put in bijection with a proper subset. For infinite sets, cardinality-as-bijection diverges from finite intuition — and that divergence is mathematically meaningful, not a flaw.

Cardinality defined via bijections is an **equivalence relation** on sets. Reflexivity: every set A bijects with itself via the identity function. Symmetry: if f: A → B is a bijection, then f⁻¹: B → A is also a bijection (bijections are invertible). Transitivity: if f: A → B and g: B → C are bijections, then g ∘ f: A → C is a bijection. This partitions all sets into cardinality classes. The finite sets divide into classes of size 0, 1, 2, 3,... Then comes the class of **countably infinite** sets (those bijecting with ℕ), and beyond that the uncountable sets. Your next step will be Cantor's theorem: no set bijects with its own power set, which shows that no matter how large a set is, its collection of subsets is strictly larger. The cardinality hierarchy is infinite — there is no largest infinity.

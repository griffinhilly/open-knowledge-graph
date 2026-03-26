---
id: ordinal-numbers-definition-and-order
title: 'Ordinal Numbers: Definition and Order Structure'
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: set-membership-and-notation
  type: hard
- id: well-founded-relations
  type: soft
- id: binary-relations
  type: soft
- id: well-ordering-principle
  type: soft
- id: mathematical-induction
  type: soft
builds-toward:
- successor-limit-and-von-neumann-ordinals
tags:
- ordinal
- order-type
- transfinite
stage: formal-systems
status: validated
---

# Ordinal Numbers: Definition and Order Structure

## Core Idea
Ordinals generalize natural numbers to capture both size and order structure, extending the sequence 0, 1, 2, ..., ω, ω+1, ω+2, ... Ordinals are well-ordered sets providing the foundation for transfinite recursion and induction, allowing finite techniques to be applied to infinite structures.

## How It's Best Learned
Study small ordinals: 0 = ∅, 1 = {0}, 2 = {0,1}, 3 = {0,1,2}. Visualize ω as the 'first infinite ordinal' followed by ω+1, ω+2. Practice comparing ordinals using the membership-based ordering.

## Questions

```yaml
- question: "Why does the set {..., −2, −1, 0} (all non-positive integers in their usual order) have no associated ordinal number?"
  type: multiple-choice
  options:
    - "It is an infinite set, and ordinals only apply to finite sets"
    - "It is not well-ordered: there is no least element (no smallest non-positive integer), so the set lacks the structural property ordinals require"
    - "It uses negative numbers, which cannot be elements of ordinals"
    - "Its cardinality is uncountable, placing it beyond the ordinal hierarchy"
  answer: 1
  explanation: "Ordinals are canonical representatives of well-orderings — orderings in which every nonempty subset has a least element. The non-positive integers {..., −2, −1, 0} have no least element: for any n ≤ 0, there exists n−1 < n. Since the set is not well-ordered, it has no ordinal. This is not about finiteness or cardinality — it's about order structure. Well-orderedness is precisely the property that makes transfinite induction work."

- question: "Two sets are both countably infinite: ω (natural numbers 0, 1, 2, ... in usual order) and ω + 1 (natural numbers followed by one additional element at the end). Which statement is correct?"
  type: multiple-choice
  options:
    - "They are the same ordinal because both are countably infinite — ordinals measure size"
    - "ω + 1 ≠ ω: adding a last element changes the order type even though both sets have the same cardinality; ordinals capture order structure, not just size"
    - "ω + 1 = ω because infinity plus one is still infinity"
    - "ω + 1 must be uncountable since it is strictly larger than ω"
  answer: 1
  explanation: "This is the central insight about ordinals: they capture order type, not cardinality. ω has no last element; ω + 1 has a last element (ω itself). These are structurally different well-orderings, so they are different ordinals. Both are countably infinite — same cardinality — but distinct ordinal numbers. The intuition that 'infinity + 1 = infinity' confuses cardinal arithmetic (where ℵ₀ + 1 = ℵ₀) with ordinal arithmetic (where ω + 1 ≠ ω)."

- question: "In von Neumann's construction, ordinals are defined as sets where the ordering relation 'n < m' is equivalent to set membership 'n ∈ m', eliminating the need for a separate definition of 'less than.'"
  type: true-false
  answer: true
  explanation: "This is the elegant economy of von Neumann ordinals: 0 = ∅, 1 = {0}, 2 = {0, 1}, and n < m simply means n ∈ m. Every ordinal is the set of all smaller ordinals, so the 'less than' relation is built into the set structure itself. This is not a coincidence — it is a deliberate design choice that makes ordinals self-contained mathematical objects with their order encoded internally rather than added on separately."

- question: "Two sets with the same cardinality generally have the same ordinal number, because ordinals and cardinals both measure the 'size' of sets."
  type: true-false
  answer: false
  explanation: "Ordinals capture order type; cardinals capture size. The sets {0, 1, 2, ...} (order type ω) and {0, 1, 2, ..., ω} (order type ω + 1) have the same cardinality (both countably infinite) but different ordinals. Even for finite sets, every 3-element set has the same cardinality, but {a, b, c} ordered differently gives different order types — though for finite well-orderings, cardinality and ordinal happen to coincide. The distinction matters crucially in the transfinite setting."

- question: "Explain why ordinals capture 'order type' rather than just 'size,' and give a concrete example of two infinite sets that have the same cardinality but different ordinal structure."
  type: short-answer
  answer: "Order type describes the pattern of how elements are arranged — specifically, whether a well-ordering has a first element, a last element, limit points, etc. Cardinality only counts how many elements there are. Example: ω = {0, 1, 2, ...} and ω + 1 = {0, 1, 2, ..., ω} are both countably infinite (same cardinality) but ω has no last element while ω + 1 does — they are structurally different well-orderings with different ordinals."
  explanation: "Every well-ordered set is order-isomorphic to exactly one ordinal — this uniqueness makes ordinals the canonical yardstick for well-orderings. Two well-orderings that look the same structurally (you can match them element-by-element in an order-preserving way) get the same ordinal. Two that don't match structurally — even if they have the same number of elements — get different ordinals. This is why transfinite induction needs ordinals, not just cardinals: the induction step depends on having a well-defined 'previous' element, which is an order property, not a size property."
```

## Explainer

To understand ordinals, start from a question your work with set membership already makes natural: can we build *numbers* purely out of sets? Von Neumann's answer is a beautiful recursive construction. Define **zero** as the empty set: 0 = ∅. Then define each successive number as the set of all numbers that came before it: 1 = {0} = {∅}, 2 = {0, 1} = {∅, {∅}}, 3 = {0, 1, 2}, and so on. Every natural number is a finite set whose members are exactly its predecessors. Crucially, the **ordering** between ordinals is just set membership — n < m if and only if n ∈ m. You don't need a separate definition of "less than"; it falls out of the set structure itself.

What makes ordinals more than a clever encoding of the natural numbers is that this construction doesn't have to stop. After all the finite ordinals 0, 1, 2, 3, ..., there is nothing preventing us from forming their union: **ω** = {0, 1, 2, 3, ...}. This is the first **transfinite ordinal** — the smallest set that contains all natural numbers. Then ω + 1 = ω ∪ {ω} = {0, 1, 2, ..., ω}, and ω + 2 = {0, 1, 2, ..., ω, ω+1}, and so on. The sequence extends far beyond ω: ω·2, ω², ω^ω, and beyond. Each ordinal is the set of all ordinals before it, which means the collection of all ordinals is well-ordered by the membership relation.

The key structural property that makes ordinals so useful is **well-ordering**: every nonempty set of ordinals has a least element (its member that contains no other member of the set). You have already encountered the well-ordering principle and mathematical induction for the natural numbers — ordinals generalize exactly this. **Transfinite induction** works by the same logic: to prove a property holds for all ordinals, show it holds for 0, show that if it holds for all ordinals less than α then it holds for α, and handle the special case of **limit ordinals** (like ω) that have no immediate predecessor. This three-case structure — zero, successor, limit — is the heartbeat of virtually every transfinite proof.

Ordinals capture *order type*, not just size. Two sets can have the same cardinality but different ordinal structure. The set {0, 1, 2, ...} has order type ω (a first element, no last). The set {..., -2, -1, 0} has no first element — it is not well-ordered — and so has no ordinal. Even among well-orderings of the same size, {1, 2, 3, ..., 0} (natural numbers followed by zero at the end) has order type ω + 1, not ω, because there is now a last element. Ordinals are precisely the canonical representatives of well-ordering types: each well-ordered set is order-isomorphic to exactly one ordinal. This is why ordinals are foundational — they provide the standard yardstick against which any well-ordered structure is measured.

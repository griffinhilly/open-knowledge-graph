---
id: cartesian-product-and-ordered-pairs
title: Cartesian Product and Ordered Pairs
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: set-membership-and-notation
  type: hard
builds-toward:
- relations-as-set-subsets
- functions-and-mappings-formal
tags:
- cartesian-product
- ordered-pairs
- relations
stage: formal-systems
status: validated
---

# Cartesian Product and Ordered Pairs

## Core Idea
The Cartesian product A × B is the set of all ordered pairs (a,b) where a ∈ A and b ∈ B. Two ordered pairs are equal iff (a,b) = (c,d) means a = c and b = d. This construction provides the formal foundation for relations, functions, and multi-dimensional structures in set theory.

## Questions

```yaml
- question: "Why is (3, 5) ≠ (5, 3) in set theory, even though {3, 5} = {5, 3}?"
  type: multiple-choice
  options:
    - "Because in set theory, order is always preserved by default for numeric elements"
    - "Because the Kuratowski definition (a,b) = {{a},{a,b}} distinguishes positions: {{3},{3,5}} ≠ {{5},{5,3}}"
    - "Because 3 and 5 are different numbers, so any pairing must respect their natural ordering"
    - "Because sets preserve the order in which elements were inserted"
  answer: 1
  explanation: "Sets are inherently unordered — {3,5} and {5,3} are identical as sets. To encode order within set theory, Kuratowski defined (a,b) = {{a},{a,b}}. The first component a appears as a singleton {a}, unique to the pair encoding, which distinguishes it from b. You can verify: (3,5) = {{3},{3,5}} while (5,3) = {{5},{5,3}}, and these are different sets because their singletons differ. The equality rule (a,b) = (c,d) iff a=c and b=d follows directly."

- question: "If |A| = 4 and |B| = 3, how many elements does A × B contain?"
  type: multiple-choice
  options:
    - "7 — the sum of the sizes"
    - "12 — the product of the sizes"
    - "It depends on how many elements A and B share"
    - "24 — the number of ways to arrange all elements"
  answer: 1
  explanation: "|A × B| = |A| · |B| = 4 · 3 = 12. For each of the 4 elements of A, you form an ordered pair with each of the 3 elements of B independently — giving 4 × 3 = 12 distinct pairs. Shared elements between A and B are irrelevant because ordered pairs track both components: even if a ∈ A ∩ B, the pair (a,a) is a valid element of A × B, distinct from (a,x) for any x ≠ a. The product formula follows from the independent choice of first and second component."

- question: "For any two sets A and B, A × B = B × A."
  type: true-false
  answer: false
  explanation: "A × B contains pairs (a,b) with a ∈ A first and b ∈ B second. B × A contains pairs (b,a) with b ∈ B first and a ∈ A second. Unless A = B (or one is empty), these are different sets because (a,b) ≠ (b,a) when a ≠ b. For example, if A = {1} and B = {x}, then A × B = {(1,x)} while B × A = {(x,1)}, and (1,x) ≠ (x,1). The order of the sets in the product determines which element comes first in each pair."

- question: "A function f: A → B can be formally defined as a subset of the Cartesian product A × B."
  type: true-false
  answer: true
  explanation: "A function f: A → B is formally a relation (a subset R ⊆ A × B) with the additional constraint that every element of A appears as a first component exactly once: for each a ∈ A, there is exactly one pair (a,b) ∈ R. This 'exactly one' condition captures the requirement that a function assigns a unique output to every input. The Cartesian product provides the universe of all possible input-output pairs; the function selects the specific subset satisfying the uniqueness condition."

- question: "Why is it necessary to formally encode ordered pairs as sets (using the Kuratowski definition or similar), rather than simply treating them as a new primitive notion alongside sets?"
  type: short-answer
  answer: "Set theory aims to provide a single unified foundation in which all mathematical objects are sets. If ordered pairs were treated as a separate primitive, the foundation would require additional axioms and a new sort of entity. By encoding (a,b) as {{a},{a,b}}, ordered pairs become sets constructible from existing axioms, keeping the foundational theory minimal. The encoding works as long as it satisfies the key property: (a,b) = (c,d) if and only if a = c and b = d."
  explanation: "The choice of encoding is not unique — other encodings exist — but Kuratowski's is the standard. What matters is that some encoding exists, ensuring ordered pairs don't require a new axiom. Once ordered pairs are sets, Cartesian products are sets, and then relations and functions are sets, allowing all of mathematics to be developed within the single framework of ZFC set theory."
```

## Explainer

Start from something you already know: a set is an unordered collection of distinct elements. The set {1, 2} is exactly the same as {2, 1}. But many mathematical objects are inherently ordered — the point (3, 5) in a coordinate plane is not the same as the point (5, 3). To talk about ordered structure within set theory, we need a new construction, and that is what the **ordered pair** provides.

The formal definition of an ordered pair is (a, b) = {{a}, {a, b}}. This encoding (due to Kuratowski) looks strange at first, but it achieves precisely one thing: it forces the two components to be distinguishable. You can verify that (a, b) = (c, d) if and only if a = c and b = d, while unordered sets {a, b} = {c, d} whenever the elements match in any order. The set-theoretic encoding is mostly scaffolding — what matters is the equality rule. Once you have ordered pairs, everything else follows from your prerequisite concept of **set membership**: you already know how to test whether something belongs to a set, and that is all you need to build the Cartesian product.

The **Cartesian product** A × B is defined as the set of all ordered pairs (a, b) where a ∈ A and b ∈ B. If A = {1, 2} and B = {x, y}, then A × B = {(1,x), (1,y), (2,x), (2,y)} — every element of A paired with every element of B, in that order. The name honors René Descartes, whose coordinate geometry pairs real numbers exactly this way: ℝ × ℝ is the Cartesian plane, where every point is an ordered pair of real numbers. The size of A × B is |A| · |B|, since each of |A| choices from A independently combines with each of |B| choices from B.

The payoff of this construction is that it makes **relations** and **functions** set-theoretic objects. A binary relation between A and B is simply a subset of A × B — a collection of ordered pairs. The relation "less than" on ℕ is the set {(0,1), (0,2), (1,2), (0,3), ...}. A function f: A → B is a special kind of relation — a subset of A × B where every element of A appears as a first component exactly once. This means everything you want to say about functions and relations can be reduced to membership questions about sets of ordered pairs, giving set theory its remarkable expressive power.

The construction extends naturally: the **n-fold Cartesian product** A₁ × A₂ × ... × Aₙ is the set of ordered n-tuples, and A × A × A can be written A³. Sequences, vectors, databases rows — all of these are instances of Cartesian products. Once you understand that ordered pairs are just a device for encoding position into a set, the entire tower of relational mathematics becomes accessible: relations build on ordered pairs, functions build on relations, and virtually every mathematical structure you will study is, at bottom, a set with some distinguished relations and functions on it.


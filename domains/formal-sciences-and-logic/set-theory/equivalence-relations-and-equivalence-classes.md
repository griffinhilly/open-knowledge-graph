---
id: equivalence-relations-and-equivalence-classes
title: Equivalence Relations and Partitions
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: binary-relations-definition-and-properties
  type: hard
builds-toward:
- cardinality-comparison-and-schroeder-bernstein
- cardinal-numbers-basic-theory
tags:
- equivalence
- partitions
- quotients
stage: formal-systems
status: validated
---

# Equivalence Relations and Partitions

## Core Idea
An equivalence relation is reflexive, symmetric, and transitive. It partitions its underlying set into equivalence classes [a] = {x : xRa}. There is a bijection between equivalence relations on S and partitions of S, making equivalence relations the natural formalism for quotient structures.

## How It's Best Learned
Start with concrete examples (congruence mod n, similarity of triangles), verify all three properties, then observe how equivalence classes partition the set.

## Questions

```yaml
- question: "Which of the following relations on ℤ is NOT an equivalence relation?"
  type: multiple-choice
  options:
    - "a R b if and only if a − b is even"
    - "a R b if and only if a² = b²"
    - "a R b if and only if a ≤ b"
    - "a R b if and only if a and b have the same remainder when divided by 5"
  answer: 2
  explanation: "An equivalence relation must be reflexive, symmetric, and transitive. The relation a ≤ b fails symmetry: 2 ≤ 3 but it is not the case that 3 ≤ 2. It is reflexive (a ≤ a) and transitive, but symmetry is missing. The other three are genuine equivalence relations: even differences partition ℤ into two classes (even and odd integers), a² = b² partitions by absolute value, and congruence mod 5 produces five classes."

- question: "The rational numbers ℚ are constructed as equivalence classes of integer pairs (a,b) with b ≠ 0 under the relation (a,b) ~ (c,d) iff ad = bc. What is the equivalence class [(1,2)]?"
  type: multiple-choice
  options:
    - "The single ordered pair (1, 2)"
    - "The unique fraction 1/2, with no other representations"
    - "The set of all integer pairs equal to 1/2: {(1,2), (2,4), (3,6), (−1,−2), …}"
    - "All fractions with numerator 1"
  answer: 2
  explanation: "The equivalence class [(1,2)] is not just the pair (1,2) — it is the entire collection of all pairs (a,b) where a/b = 1/2, i.e., (1,2), (2,4), (3,6), (−1,−2), and so on. The rational number 1/2 *is* this equivalence class: all its representations simultaneously, treated as a single object. This is the quotient construction — we build ℚ from ℤ by declaring pairs equivalent when they represent the same ratio, then working with the classes as mathematical objects."

- question: "If a relation on a set S is both symmetric and transitive, it should also be reflexive — and is therefore automatically an equivalence relation."
  type: true-false
  answer: false
  explanation: "This seems logically compelling but is false. Consider the empty relation on any nonempty set: it is vacuously symmetric and transitive (no counterexamples exist to violate these properties), but not reflexive — no element is related to itself. Reflexivity must be verified independently. A relation satisfying only symmetry and transitivity may hold only for some elements, leaving others unrelated to anything. All three properties must be checked separately."

- question: "There is a bijection between equivalence relations on a set S and partitions of S — every equivalence relation produces a partition, and every partition determines an equivalence relation."
  type: true-false
  answer: true
  explanation: "This is the fundamental theorem connecting the two concepts. Given an equivalence relation R, the equivalence classes form a partition: they are nonempty, pairwise disjoint, and cover all of S. Conversely, any partition of S defines an equivalence relation: declare a R b iff a and b lie in the same block. These two constructions are inverses of each other, establishing a one-to-one correspondence. The relational language (for logic and algebra) and the partition language (for combinatorics) are interchangeable."

- question: "What does it mean to form a 'quotient set' S/R, and why is this construction useful in mathematics? Give an example."
  type: short-answer
  answer: "The quotient set S/R is the set of all equivalence classes under R — it collapses S by treating equivalent elements as a single object. For example, ℤ/3ℤ partitions ℤ into three classes: {…,−3,0,3,…}, {…,−2,1,4,…}, and {…,−1,2,5,…}. Arithmetic on these three classes is well-defined, giving a new algebraic structure with only 3 elements. Quotient construction is how mathematics builds ℤ/nℤ, ℚ (equivalence classes of integer pairs), and cardinal numbers (equivalence classes of sets under bijection)."
  explanation: "The power of quotient sets is that they let you build new mathematical objects by declaring 'these things count as the same.' This is the foundational technique of abstract algebra: group quotients, ring quotients, and module quotients all rely on this construction. Understanding equivalence relations and quotients is prerequisite to virtually all of modern algebra and to the set-theoretic foundations of mathematics."
```

## Explainer

From binary relations, you know that a relation R on a set S is just a set of ordered pairs — a way of saying which elements are "related." Most relations are unstructured: an arbitrary relation can pair elements in any way. An **equivalence relation** is a relation with three specific properties that together make it behave like equality. **Reflexivity** says every element is related to itself: a R a for all a. **Symmetry** says relatedness is mutual: if a R b then b R a. **Transitivity** says relatedness chains: if a R b and b R c then a R c. Together these axioms capture the idea of "being the same in some respect." Equality itself satisfies all three, and every equivalence relation can be thought of as a generalized equality — sameness with respect to some chosen criterion.

The canonical example is **congruence modulo n**: for integers a and b, say a ≡ b (mod n) if n divides a − b. Reflexivity holds because n divides 0. Symmetry holds because if n divides a − b then n divides b − a. Transitivity holds because if n divides a − b and b − c, then it divides (a − b) + (b − c) = a − c. The **equivalence class** of an element a is the set [a] = {x ∈ S : x R a} — all elements related to a. For congruence mod 3, the classes are {…, −3, 0, 3, 6, …}, {…, −2, 1, 4, 7, …}, and {…, −1, 2, 5, 8, …}. Every integer belongs to exactly one class, and the three classes together cover all the integers with no overlap.

This "cover with no overlap" observation is the partition theorem: an equivalence relation on S produces a **partition** of S — a collection of nonempty, pairwise-disjoint subsets whose union is all of S. The classes are the partition blocks. Conversely, any partition of S defines an equivalence relation: declare a R b iff a and b lie in the same block. These two constructions are inverses of each other, establishing a bijection between equivalence relations on S and partitions of S. The two perspectives are equivalent; which you use depends on whether you want the relational language (for logic and set theory) or the combinatorial language (for counting and algebra).

The power of equivalence relations lies in **quotient construction**. Given an equivalence relation R on S, the **quotient set** S/R = {[a] : a ∈ S} is the set of equivalence classes. This construction collapses S by treating equivalent elements as identical — it is how you build ℤ/nℤ (integers mod n), the rational numbers ℚ (as equivalence classes of pairs of integers under the relation (a,b) ~ (c,d) iff ad = bc), and many other fundamental objects in algebra. The quotient set is also the foundation for cardinal numbers in set theory: two sets have the same cardinality iff they are equivalent under the relation "there exists a bijection between us," and cardinals are the equivalence classes. Understanding equivalence relations and their quotients is thus prerequisite to almost all of abstract algebra and to the set-theoretic treatment of size.

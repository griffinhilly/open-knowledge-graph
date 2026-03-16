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
status: draft
---

# Equivalence Relations and Partitions

## Core Idea
An equivalence relation is reflexive, symmetric, and transitive. It partitions its underlying set into equivalence classes [a] = {x : xRa}. There is a bijection between equivalence relations on S and partitions of S, making equivalence relations the natural formalism for quotient structures.

## How It's Best Learned
Start with concrete examples (congruence mod n, similarity of triangles), verify all three properties, then observe how equivalence classes partition the set.

## Explainer

From binary relations, you know that a relation R on a set S is just a set of ordered pairs — a way of saying which elements are "related." Most relations are unstructured: an arbitrary relation can pair elements in any way. An **equivalence relation** is a relation with three specific properties that together make it behave like equality. **Reflexivity** says every element is related to itself: a R a for all a. **Symmetry** says relatedness is mutual: if a R b then b R a. **Transitivity** says relatedness chains: if a R b and b R c then a R c. Together these axioms capture the idea of "being the same in some respect." Equality itself satisfies all three, and every equivalence relation can be thought of as a generalized equality — sameness with respect to some chosen criterion.

The canonical example is **congruence modulo n**: for integers a and b, say a ≡ b (mod n) if n divides a − b. Reflexivity holds because n divides 0. Symmetry holds because if n divides a − b then n divides b − a. Transitivity holds because if n divides a − b and b − c, then it divides (a − b) + (b − c) = a − c. The **equivalence class** of an element a is the set [a] = {x ∈ S : x R a} — all elements related to a. For congruence mod 3, the classes are {…, −3, 0, 3, 6, …}, {…, −2, 1, 4, 7, …}, and {…, −1, 2, 5, 8, …}. Every integer belongs to exactly one class, and the three classes together cover all the integers with no overlap.

This "cover with no overlap" observation is the partition theorem: an equivalence relation on S produces a **partition** of S — a collection of nonempty, pairwise-disjoint subsets whose union is all of S. The classes are the partition blocks. Conversely, any partition of S defines an equivalence relation: declare a R b iff a and b lie in the same block. These two constructions are inverses of each other, establishing a bijection between equivalence relations on S and partitions of S. The two perspectives are equivalent; which you use depends on whether you want the relational language (for logic and set theory) or the combinatorial language (for counting and algebra).

The power of equivalence relations lies in **quotient construction**. Given an equivalence relation R on S, the **quotient set** S/R = {[a] : a ∈ S} is the set of equivalence classes. This construction collapses S by treating equivalent elements as identical — it is how you build ℤ/nℤ (integers mod n), the rational numbers ℚ (as equivalence classes of pairs of integers under the relation (a,b) ~ (c,d) iff ad = bc), and many other fundamental objects in algebra. The quotient set is also the foundation for cardinal numbers in set theory: two sets have the same cardinality iff they are equivalent under the relation "there exists a bijection between us," and cardinals are the equivalence classes. Understanding equivalence relations and their quotients is thus prerequisite to almost all of abstract algebra and to the set-theoretic treatment of size.

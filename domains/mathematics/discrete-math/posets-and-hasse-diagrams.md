---
id: posets-and-hasse-diagrams
title: Partially Ordered Sets and Hasse Diagrams
domain: mathematics
course: discrete-math
prerequisites:
- id: partial-orders
  type: hard
- id: equivalence-relations
  type: soft
builds-toward:
- lattices-and-boolean-lattices
tags:
- discrete-structures
- posets
- order-theory
stage: formal-systems
status: draft
---

# Partially Ordered Sets and Hasse Diagrams

## Core Idea
A partially ordered set (poset) is a set with a partial order relation that is reflexive, antisymmetric, and transitive. Hasse diagrams visually represent posets by showing covering relations, making it easy to see the structure of partial orders and identify maximal/minimal elements.

## Explainer

You know from partial orders that a relation ≤ on a set must be **reflexive** (a ≤ a), **antisymmetric** (if a ≤ b and b ≤ a, then a = b), and **transitive** (if a ≤ b and b ≤ c, then a ≤ c). A **partially ordered set** (or **poset**) is just a set paired with such a relation. The word "partial" is the key: unlike the familiar ≤ on real numbers, not every pair of elements needs to be comparable. Consider the power set of {1, 2, 3} ordered by ⊆. The subsets {1, 2} and {1, 3} are both comparable to {1} and to {1, 2, 3}, but {1, 2} and {1, 3} are not comparable to each other — neither contains the other. This incomparability is what "partial" means, and it appears everywhere: tasks ordered by dependency, propositions ordered by logical implication, integers ordered by divisibility.

A **Hasse diagram** is the standard tool for drawing posets. The key idea is to remove redundant information: since ≤ is transitive, we only draw the "direct" relationships — the **covering relations**. We say b **covers** a if a < b and there's nothing strictly between them (no c with a < c < b). In the diagram, b is drawn above a with a line connecting them whenever b covers a. The transitive closure of all these lines gives you the full order. Arrows are dropped (we read "higher = greater"); reflexivity is implicit (every element is ≥ itself). The result is a clean, readable picture of the order's skeleton without clutter.

To read a Hasse diagram: a **minimal element** has nothing below it; a **maximal element** has nothing above it. A **minimum** (or **least**) element is below everything else — it exists only if there's a unique minimal element. A **maximum** (or **greatest**) element sits above everything. In the divisibility poset on {1, 2, 3, 6}: 1 is the minimum, 6 is the maximum, and the diagram would show 1 at the bottom, 2 and 3 in the middle (both covering 1), and 6 at the top (covering both 2 and 3). The diagram instantly shows you the structure that would take paragraphs to describe in words.

The power of Hasse diagrams becomes clear when you need to find **upper bounds** and **lower bounds**. Given two elements a and b, their **least upper bound** (lub or join) is the smallest element above both — the "meet point" of their upward paths in the diagram. Their **greatest lower bound** (glb or meet) is the largest element below both. When every pair of elements has both a lub and glb, the poset becomes a **lattice** — the structure you'll study next. Equivalence relations from your prerequisites connect here too: the equivalence classes of any equivalence relation form a poset under refinement, where one partition is "finer" than another if it subdivides its blocks further. Order theory and equivalence theory are different lenses on the same underlying mathematical landscape.

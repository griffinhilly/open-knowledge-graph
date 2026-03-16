---
id: set-relations-functions-discrete
title: Sets, Relations, and Functions in Discrete Mathematics
domain: mathematics
course: discrete-math
prerequisites:
- id: set-fundamentals
  type: hard
- id: functions-domain-codomain-range
  type: hard
builds-toward:
- counting-fundamentals-discrete
- cardinality-and-countability
tags:
- sets
- relations
- functions
- equivalence
stage: formal-systems
status: draft
---

# Sets, Relations, and Functions in Discrete Mathematics

## Core Idea
Sets form the foundation of discrete mathematics. Relations generalize the concept of 'connection' between elements; equivalence relations partition sets into disjoint subsets. Functions map elements between sets; surjections, injections, and bijections characterize different mapping types.

## How It's Best Learned
Visualize relations as directed graphs or matrices. Understand that equivalence relations correspond to partitions. Practice proving properties: reflexivity, symmetry, transitivity.

## Common Misconceptions
Not all relations are functions. A function must map every domain element to exactly one codomain element. An injection is one-to-one; a surjection is onto—easy to confuse.

## Explainer

You already know sets as collections of objects and functions as mappings between sets. In discrete mathematics, these concepts are formalized more precisely because we use them as the foundation for proofs, counting, and structural reasoning. A **relation** on sets A and B is simply a subset of the Cartesian product A × B — a set of ordered pairs (a, b) where a ∈ A and b ∈ B. This is more general than a function: a relation can pair one element with many others, or with none at all. Think of "is a prerequisite of" as a relation on courses: it pairs course A with course B whenever A must come before B, and one course can be paired with many successors.

An **equivalence relation** on a set A is a relation that is reflexive (a relates to itself), symmetric (if a relates to b then b relates to a), and transitive (if a relates to b and b relates to c then a relates to c). The canonical example is equality, but there are many others: "has the same remainder when divided by n" (congruence mod n), "was born in the same country as," "has the same number of elements as." The deep theorem here is that every equivalence relation on A partitions A into disjoint **equivalence classes** — every element belongs to exactly one class, and two elements are in the same class if and only if they are related. You visualize this as splitting a set into non-overlapping blobs where everything in a blob is equivalent.

A **function** f: A → B is a special relation where every element of A is paired with exactly one element of B — each input has a unique output. The three important function types characterize how the mapping fills the codomain. An **injection** (one-to-one) means no two distinct inputs share an output: f(a₁) = f(a₂) implies a₁ = a₂. A **surjection** (onto) means every element of B is hit by at least one input — no element of B is left out. A **bijection** is both: a perfect pairing, a one-to-one correspondence. These distinctions are not just vocabulary — bijections are the tool for proving two sets have the same size (cardinality), which becomes central when you study countability.

Connecting everything: visualizing a relation as a directed graph (draw a node for each element, draw an arrow from a to b whenever (a,b) is in the relation) makes the properties concrete. Reflexivity means every node has a self-loop. Symmetry means every arrow has a reverse arrow. Transitivity means if there is a path of length 2 from a to b, there is also a direct arrow. A function is a directed graph where every node in A has exactly one outgoing arrow. An injection means no two arrows in A point to the same node in B. These visual tools will serve you throughout discrete math, especially in counting arguments where you need to establish bijections between sets to prove they have the same size.

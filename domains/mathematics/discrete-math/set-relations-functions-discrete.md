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

## Questions

```yaml
- question: "The relation R = {(1,a), (1,b), (2,c)} has domain {1, 2} and codomain {a, b, c}. Is R a function?"
  type: multiple-choice
  options:
    - "Yes — every domain element appears in at least one pair"
    - "No — element 1 is paired with two different codomain elements"
    - "No — element c is not paired with any domain element"
    - "Yes — if we take the first occurrence of each domain element"
  answer: 1
  explanation: "A function requires every domain element to map to exactly one codomain element. Element 1 maps to both a and b, which violates this rule — R is a relation but not a function. Option A describes a property of relations in general, not functions specifically. Option C confuses the domain with the codomain: the requirement that every domain element has an output doesn't say anything about which codomain elements get 'hit' — that is the surjection question."

- question: "A bijection exists from set A to set B. What does this guarantee?"
  type: multiple-choice
  options:
    - "Both A and B are finite sets"
    - "A and B have the same cardinality"
    - "Every element of A is numerically less than every element of B"
    - "A and B are subsets of a common larger set"
  answer: 1
  explanation: "A bijection is a function that is both injective (one-to-one: distinct inputs give distinct outputs) and surjective (onto: every codomain element is hit by at least one input). A bijection establishes a perfect one-to-one correspondence between elements, which is the definition of equal cardinality. This works for infinite sets too — the bijection f(n) = 2n from ℤ to the even integers proves they have the same cardinality even though the even integers seem 'smaller'."

- question: "Every equivalence relation on a set A partitions A into disjoint equivalence classes that together cover all of A."
  type: true-false
  answer: true
  explanation: "This is the fundamental equivalence-classes theorem. Reflexivity guarantees every element is in at least one class (it belongs to its own class). Symmetry and transitivity together guarantee that being in the same class is a consistent, well-defined grouping. The resulting classes are disjoint (no element can belong to two different classes) and exhaustive (every element belongs to exactly one). This partition interpretation is often the most useful way to think about equivalence relations."

- question: "A function that is injective (one-to-one) must also be surjective (onto)."
  type: true-false
  answer: false
  explanation: "Injection and surjection are independent properties. The function f: ℤ → ℤ defined by f(n) = 2n is injective (distinct inputs give distinct outputs) but not surjective (odd integers are never in the image). A function can be injective without being surjective, surjective without being injective, both (bijection), or neither. Only when domain and codomain are finite sets of equal size does injectivity force surjectivity — but that is a special case, not a general rule."

- question: "Why must a function map every domain element to exactly one codomain element — what fails if it maps to zero elements, or to two elements?"
  type: short-answer
  answer: "If an element maps to zero outputs, the function is undefined on part of its domain — it fails to be a total function, making expressions like f(x) meaningless for those inputs. If an element maps to two different outputs, the function becomes ambiguous — f(x) would simultaneously equal two different values, undermining the whole point of a function as a deterministic mapping. A well-defined function must be both total (defined everywhere on the domain) and single-valued (one output per input)."
  explanation: "Partial functions (undefined on some inputs) and multivalued relations (multiple outputs) are both legitimate mathematical objects, but they are not functions. The single-valuedness condition is what allows functions to be composed, inverted (when bijective), and reasoned about deterministically. Many of the key theorems about functions — and their algorithmic interpretations in computer science — depend on this uniqueness property."
```

## Explainer

You already know sets as collections of objects and functions as mappings between sets. In discrete mathematics, these concepts are formalized more precisely because we use them as the foundation for proofs, counting, and structural reasoning. A **relation** on sets A and B is simply a subset of the Cartesian product A × B — a set of ordered pairs (a, b) where a ∈ A and b ∈ B. This is more general than a function: a relation can pair one element with many others, or with none at all. Think of "is a prerequisite of" as a relation on courses: it pairs course A with course B whenever A must come before B, and one course can be paired with many successors.

An **equivalence relation** on a set A is a relation that is reflexive (a relates to itself), symmetric (if a relates to b then b relates to a), and transitive (if a relates to b and b relates to c then a relates to c). The canonical example is equality, but there are many others: "has the same remainder when divided by n" (congruence mod n), "was born in the same country as," "has the same number of elements as." The deep theorem here is that every equivalence relation on A partitions A into disjoint **equivalence classes** — every element belongs to exactly one class, and two elements are in the same class if and only if they are related. You visualize this as splitting a set into non-overlapping blobs where everything in a blob is equivalent.

A **function** f: A → B is a special relation where every element of A is paired with exactly one element of B — each input has a unique output. The three important function types characterize how the mapping fills the codomain. An **injection** (one-to-one) means no two distinct inputs share an output: f(a₁) = f(a₂) implies a₁ = a₂. A **surjection** (onto) means every element of B is hit by at least one input — no element of B is left out. A **bijection** is both: a perfect pairing, a one-to-one correspondence. These distinctions are not just vocabulary — bijections are the tool for proving two sets have the same size (cardinality), which becomes central when you study countability.

Connecting everything: visualizing a relation as a directed graph (draw a node for each element, draw an arrow from a to b whenever (a,b) is in the relation) makes the properties concrete. Reflexivity means every node has a self-loop. Symmetry means every arrow has a reverse arrow. Transitivity means if there is a path of length 2 from a to b, there is also a direct arrow. A function is a directed graph where every node in A has exactly one outgoing arrow. An injection means no two arrows in A point to the same node in B. These visual tools will serve you throughout discrete math, especially in counting arguments where you need to establish bijections between sets to prove they have the same size.

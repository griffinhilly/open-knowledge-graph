---
id: injections-surjections-and-inverse-functions
title: Injective, Surjective, and Bijective Functions
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: functions-and-function-properties
  type: hard
- id: equivalence-relations-and-equivalence-classes
  type: soft
builds-toward:
- composition-of-functions-sets
- finite-sets-and-finiteness-definition
tags:
- function-types
- invertibility
- bijections
stage: formal-systems
status: validated
---

# Injective, Surjective, and Bijective Functions

## Core Idea
A function f: A → B is injective if f(a₁) = f(a₂) ⟹ a₁ = a₂, surjective if every b ∈ B has a preimage, and bijective if both. A bijection has an inverse function f⁻¹: B → A, and two sets have the same cardinality if and only if there exists a bijection between them.

## How It's Best Learned
Test each property with functions between explicit sets (e.g., f: ℕ → ℚ), drawing diagrams to visualize injections, surjections, and bijections.

## Questions

```yaml
- question: "The function f: ℕ → ℤ defined by f(n) = n is injective but not surjective (negative integers have no preimage). What does this tell us about the cardinality of ℕ compared to ℤ?"
  type: multiple-choice
  options:
    - "|ℕ| < |ℤ|, because f doesn't cover all of ℤ, proving ℤ is strictly larger"
    - "|ℕ| ≤ |ℤ|, but this injection alone doesn't establish whether |ℕ| = |ℤ| or |ℕ| < |ℤ|"
    - "|ℕ| = |ℤ|, because both sets are countably infinite"
    - "No cardinality comparison is possible from a single function"
  answer: 1
  explanation: "An injection f: A → B witnesses |A| ≤ |B| — A fits inside B without collisions, but B may have leftover elements. To establish |ℕ| = |ℤ|, you need a bijection. In fact such a bijection does exist (e.g., map 0 ↦ 0, 1 ↦ 1, 2 ↦ −1, 3 ↦ 2, 4 ↦ −2, ...), and this is the standard proof that ℕ and ℤ are equinumerous. The injective f here tells you |ℕ| ≤ |ℤ|; you need additional structure to conclude equality."

- question: "A function f: A → B has a right inverse g: B → A, meaning f(g(b)) = b for all b ∈ B. What does this tell you about f?"
  type: multiple-choice
  options:
    - "f is injective"
    - "f is bijective"
    - "f is surjective"
    - "f is neither injective nor surjective in general"
  answer: 2
  explanation: "A right inverse g means every b ∈ B is the image of g(b) under f, so every element of B has at least one preimage — exactly the definition of surjectivity. A right inverse does not require f to be injective: g simply picks one preimage for each b, but f might send multiple elements to the same b. Injectivity corresponds to a left inverse (g such that g(f(a)) = a for all a ∈ A). A full two-sided inverse requires bijectivity."

- question: "If f: A → B is injective, then f has an inverse function f⁻¹: B → A."
  type: true-false
  answer: false
  explanation: "An injection guarantees a left inverse — a function g: B → A with g(f(a)) = a for all a ∈ A — but not a full inverse on all of B. The inverse f⁻¹ must be defined on every element of B, and for elements of B outside the image f(A), there is no preimage to assign. A full two-sided inverse requires bijectivity: injectivity ensures each b in f(A) has a unique preimage, and surjectivity ensures every b is in f(A). Without surjectivity, the inverse is only partial."

- question: "Two sets have the same cardinality if and only if there exists a bijection between them."
  type: true-false
  answer: true
  explanation: "This is the definition of cardinality equality for sets of any size — finite or infinite. For finite sets it coincides with equal counts. For infinite sets it becomes the only coherent definition: ℕ and ℤ have the same cardinality because a bijection between them exists, even though ℤ 'contains' ℕ as a proper subset. This bijection-based definition, due to Cantor, revealed that not all infinite sets are the same size — ℝ has strictly greater cardinality than ℕ, as Cantor's diagonal argument shows."

- question: "Why is the Schröder-Bernstein theorem remarkable, and how does it let you prove two sets have the same cardinality without constructing an explicit bijection?"
  type: short-answer
  answer: "Schröder-Bernstein states: if injections exist in both directions (f: A → B and g: B → A), then |A| = |B|. Its power is that constructing two injections is often much easier than constructing a bijection directly. For example, to show |(0,1)| = |ℝ|, you can exhibit an injection from (0,1) into ℝ (the inclusion map) and an injection from ℝ into (0,1) (any sigmoid function). The theorem then guarantees a bijection exists, even though writing one explicitly is cumbersome. You prove cardinality equality by finding two injections rather than one bijection."
  explanation: "The theorem is remarkable because it converts a hard problem (construct an explicit bijection) into an easier one (construct two injections, possibly in totally different ways). The proof of the theorem itself is non-trivial — it requires constructing a bijection from two injections — but once proved, it becomes a general tool. The Schröder-Bernstein theorem is the foundational result that makes cardinality comparison via injections rigorous and useful throughout set theory."
```

## Explainer

You have studied functions as set-theoretic objects: a function f: A → B is a relation (a set of ordered pairs) in which every element of A appears as a first coordinate exactly once. This definition says nothing about how f distributes elements of A across B — multiple elements of A might share an image, or some elements of B might receive no preimage at all. The three properties — **injectivity**, **surjectivity**, and **bijectivity** — characterize fundamentally different patterns of that distribution and become the foundation for comparing infinite sets by cardinality.

An **injection** (one-to-one function) satisfies: f(a₁) = f(a₂) ⟹ a₁ = a₂. Equivalently, no two elements of A are sent to the same element of B. Think of it as: B has "at least as many slots as A needs." The image f(A) fits inside B without collisions, but B may have elements left over — elements with no preimage. A **surjection** (onto function) satisfies: for every b ∈ B, there exists some a ∈ A with f(a) = b. No element of B is left uncovered. This says B has "at most as many elements as A" — every element of B is the target of something. A **bijection** is both: every element of B has exactly one preimage, no more and no less.

The inverse function characterizes bijectivity precisely. If f: A → B is a bijection, define f⁻¹: B → A by: f⁻¹(b) is the unique a ∈ A with f(a) = b. Uniqueness requires injectivity (no two a's map to b); existence requires surjectivity (at least one a maps to b). Together they guarantee f⁻¹ is well-defined and itself a bijection, satisfying f⁻¹ ∘ f = id_A and f ∘ f⁻¹ = id_B. If f is only injective, a left inverse g: B → A with g ∘ f = id_A exists (though it may not be unique, since g can send elements outside f(A) anywhere). If f is only surjective, a right inverse exists — but choosing one for each b ∈ B requires the axiom of choice when B is infinite.

For cardinality, bijections become the fundamental measuring tool. Two sets A and B have the same cardinality — written |A| = |B| — exactly when a bijection A → B exists. An injection f: A → B witnesses |A| ≤ |B|; a surjection from A to B witnesses |A| ≥ |B|. These witnessing functions combine in the **Schröder-Bernstein theorem**: if injections exist in both directions (|A| ≤ |B| and |B| ≤ |A|), then |A| = |B| — a bijection must exist. The theorem is remarkable because it lets you establish equal cardinality without constructing an explicit bijection. To show |ℝ| = |(0, 1)|, for instance, you can exhibit injections in both directions — one sending ℝ into (0, 1) via a sigmoid, one the inclusion map — and invoke Schröder-Bernstein to conclude they are equinumerous, even without ever writing down an explicit bijection between them.

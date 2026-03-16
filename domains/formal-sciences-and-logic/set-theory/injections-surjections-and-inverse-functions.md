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
- cardinality-comparison-and-schroeder-bernstein
tags:
- function-types
- invertibility
- bijections
stage: formal-systems
status: draft
---

# Injective, Surjective, and Bijective Functions

## Core Idea
A function f: A → B is injective if f(a₁) = f(a₂) ⟹ a₁ = a₂, surjective if every b ∈ B has a preimage, and bijective if both. A bijection has an inverse function f⁻¹: B → A, and two sets have the same cardinality if and only if there exists a bijection between them.

## How It's Best Learned
Test each property with functions between explicit sets (e.g., f: ℕ → ℚ), drawing diagrams to visualize injections, surjections, and bijections.

## Explainer

You have studied functions as set-theoretic objects: a function f: A → B is a relation (a set of ordered pairs) in which every element of A appears as a first coordinate exactly once. This definition says nothing about how f distributes elements of A across B — multiple elements of A might share an image, or some elements of B might receive no preimage at all. The three properties — **injectivity**, **surjectivity**, and **bijectivity** — characterize fundamentally different patterns of that distribution and become the foundation for comparing infinite sets by cardinality.

An **injection** (one-to-one function) satisfies: f(a₁) = f(a₂) ⟹ a₁ = a₂. Equivalently, no two elements of A are sent to the same element of B. Think of it as: B has "at least as many slots as A needs." The image f(A) fits inside B without collisions, but B may have elements left over — elements with no preimage. A **surjection** (onto function) satisfies: for every b ∈ B, there exists some a ∈ A with f(a) = b. No element of B is left uncovered. This says B has "at most as many elements as A" — every element of B is the target of something. A **bijection** is both: every element of B has exactly one preimage, no more and no less.

The inverse function characterizes bijectivity precisely. If f: A → B is a bijection, define f⁻¹: B → A by: f⁻¹(b) is the unique a ∈ A with f(a) = b. Uniqueness requires injectivity (no two a's map to b); existence requires surjectivity (at least one a maps to b). Together they guarantee f⁻¹ is well-defined and itself a bijection, satisfying f⁻¹ ∘ f = id_A and f ∘ f⁻¹ = id_B. If f is only injective, a left inverse g: B → A with g ∘ f = id_A exists (though it may not be unique, since g can send elements outside f(A) anywhere). If f is only surjective, a right inverse exists — but choosing one for each b ∈ B requires the axiom of choice when B is infinite.

For cardinality, bijections become the fundamental measuring tool. Two sets A and B have the same cardinality — written |A| = |B| — exactly when a bijection A → B exists. An injection f: A → B witnesses |A| ≤ |B|; a surjection from A to B witnesses |A| ≥ |B|. These witnessing functions combine in the **Schröder-Bernstein theorem**: if injections exist in both directions (|A| ≤ |B| and |B| ≤ |A|), then |A| = |B| — a bijection must exist. The theorem is remarkable because it lets you establish equal cardinality without constructing an explicit bijection. To show |ℝ| = |(0, 1)|, for instance, you can exhibit injections in both directions — one sending ℝ into (0, 1) via a sigmoid, one the inclusion map — and invoke Schröder-Bernstein to conclude they are equinumerous, even without ever writing down an explicit bijection between them.

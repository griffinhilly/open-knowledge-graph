---
id: axiom-of-replacement
title: Axiom Schema of Replacement
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: zfc-axioms-overview
  type: hard
- id: first-order-logic-syntax
  type: soft
- id: axiom-of-separation
  type: soft
builds-toward:
- transfinite-recursion
- von-neumann-ordinals
tags:
- ZFC
- replacement
- image
- class function
- schema
stage: formal-systems
status: validated
---

# Axiom Schema of Replacement

## Core Idea
The axiom schema of replacement asserts that if φ(x, y) defines a class function (for each x in a set A, there is exactly one y with φ(x, y)), then the image {y : ∃x ∈ A, φ(x, y)} is a set. Replacement strictly extends separation: it permits constructing sets like {ω, P(ω), P(P(ω)), ...} that lie beyond any single level of the hierarchy reachable by separation alone. It is indispensable for defining the ordinal hierarchy via transfinite recursion and for proving key results about cardinal arithmetic.

## How It's Best Learned
Compare what can be built using only separation versus using replacement. Key example: define the sequence ω, ω+1, ω+2, ... and show that separation alone cannot guarantee this image is a set. Work through the formal statement of the schema carefully and see why the 'exactly one y' (functionality) condition is necessary.

## Common Misconceptions
- Replacement requires φ to be functional — for each x there is a unique y. If φ is merely a relation, the image need not be a set.
- Replacement does not follow from separation and the other basic axioms; it is genuinely stronger and essential for transfinite mathematics.

## Explainer

You already know from the ZFC axioms that the **axiom of separation** (Aussonderung) lets you carve out a subset of an existing set using a property: given a set A and a first-order formula φ(x), separation guarantees that {x ∈ A : φ(x)} is a set. Separation is conservative — it never produces a set larger than A. The axiom schema of **replacement** does something fundamentally different: it lets you *replace* each element of a set with a (possibly new, possibly much larger) element, and the result is still a set.

More precisely, suppose φ(x, y) defines a **class function** — for each element x of a set A, there is exactly one y satisfying φ(x, y). Then replacement asserts that the image {y : ∃x ∈ A, φ(x, y)} is a set. The functional requirement is essential: if φ were merely a relation (one x mapping to multiple y's), the image could be a proper class and the axiom would be false. But as long as the correspondence is one-to-one from inputs to outputs, the output collection is guaranteed to be a set — even if the outputs live in a much "higher" part of the set-theoretic universe than A does.

The paradigmatic example shows why separation alone is insufficient. Consider the function that sends the natural number n to the n-fold iterated power set of ω: 0 ↦ ω, 1 ↦ P(ω), 2 ↦ P(P(ω)), and so on. Each of these sets exists individually by the axiom of power set. But separation cannot collect them into the set {ω, P(ω), P(P(ω)), ...}, because there is no single set large enough to contain all of them that we can separate from — each P(ω) is strictly larger than its predecessor, so no bounded level of the hierarchy contains them all. Replacement, applied to the domain ω with the function n ↦ Vω+n (levels of the cumulative hierarchy), produces this set directly. The collection is bounded in the sense that the function is definable, even though the range items are scattered across the hierarchy.

Replacement is indispensable for **transfinite recursion** and for constructing the **von Neumann ordinal hierarchy**. To define a sequence indexed by all ordinals — say, the cumulative hierarchy Vα for every ordinal α — you need replacement to guarantee that at each limit stage λ, the union ⋃{Vα : α < λ} is indeed a set (the collection {Vα : α < λ} must first be guaranteed to be a set by applying replacement to the function α ↦ Vα on the ordinal λ). Without replacement, transfinite recursion over the ordinals cannot be formalized in ZFC. The axiom thus provides the engine for constructing the entire set-theoretic universe beyond the finite levels — it is the formal license to "climb" the cumulative hierarchy without bound.

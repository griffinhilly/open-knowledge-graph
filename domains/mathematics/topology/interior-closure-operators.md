---
id: interior-closure-operators
title: Interior and Closure Operators
domain: mathematics
course: topology
prerequisites:
- id: closure-interior-and-boundary
  type: hard
builds-toward:
- separation-axioms-t3-regular
tags:
- operators
- interior
- closure
- kuratowski-axioms
stage: advanced
status: draft
---

# Interior and Closure Operators

## Core Idea
Interior and closure are operators satisfying Kuratowski's axioms: they are idempotent, expansive (or contractive), preserve unions (or intersections), and are compatible with the empty set and whole space. These axioms characterize how topologies are defined, and an alternative approach to topology is to axiomatically define a closure operator and derive the open sets from it.

## Explainer

You already know the concrete definitions: the **interior** of a set A is the largest open set contained in A; the **closure** of A is the smallest closed set containing A. The goal of this topic is to step back from those definitions and ask: what abstract rules govern these operations? The answer is **Kuratowski's axioms**, which state that the closure operator cl satisfies four properties: (1) cl(∅) = ∅, (2) A ⊆ cl(A) (extensivity), (3) cl(cl(A)) = cl(A) (idempotency), and (4) cl(A ∪ B) = cl(A) ∪ cl(B) (preservation of unions). Dual axioms characterize the interior operator int with containment and unions reversed.

Idempotency captures the key intuition: closing an already-closed set does nothing. Taking the interior of an open set does nothing. The operations are *stable* — applying them twice is the same as applying them once. This contrasts with how iterating many other operations changes the result; here, one application fully saturates the operation. The fixed points of cl are precisely the closed sets; the fixed points of int are precisely the open sets.

The deeper insight is that these axioms are not just properties of the closure operator — they *characterize* topologies. Given *any* function cl : 𝒫(X) → 𝒫(X) satisfying Kuratowski's four axioms, you can define the closed sets to be exactly the fixed points of cl, and the resulting collection determines a unique topology on X. This means you can define a topology without ever mentioning open sets explicitly — the closure operator encodes the entire topological structure.

This operator perspective makes the duality between interior and closure completely explicit. The two operators are related by complementation: int(A) = (cl(Aᶜ))ᶜ. Every axiom for closure has a dual axiom for interior with the direction of containment reversed and unions replaced by intersections. When you encounter a proof about one operator, its dual proof about the other follows by mechanically applying this duality. This algebraic perspective becomes especially powerful when you study more abstract spaces where the concrete definitions are harder to visualize.

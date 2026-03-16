---
id: elementary-equivalence-and-logical-indistinguishability
title: 'Elementary Equivalence: Logical Indistinguishability'
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: complete-theory-of-structures
  type: hard
- id: elementary-equivalence-indistinguishability
  type: hard
builds-toward:
- ehrenfeucht-fraisse-games-equivalence
- back-and-forth-method-variants
tags:
- elementary-equivalence
- ≡
- indistinguishability
- same-theory
stage: abstract-reasoning
status: draft
---

# Elementary Equivalence: Logical Indistinguishability

## Core Idea
Two structures M and N are elementarily equivalent (M ≡ N) if they satisfy the same complete first-order theory: Th(M) = Th(N). This is weaker than isomorphism—elementarily equivalent structures may differ in cardinality and non-first-order properties, but no first-order sentence can distinguish them.

## How It's Best Learned
Show that (Q, <) and (R, <) are not isomorphic but are elementarily equivalent by describing the back-and-forth method at a high level.

## Explainer

You already know that two structures can be **isomorphic** — that is, there is a bijection between their domains that perfectly preserves all relations, functions, and constants. Isomorphic structures are entirely interchangeable: every property of one holds for the other. **Elementary equivalence** is a strictly weaker notion. Two structures M and N are elementarily equivalent, written M ≡ N, if they satisfy exactly the same first-order sentences — the same complete theory. They might not be isomorphic, might have different cardinalities, might even "look different" in many ways, but no first-order formula can tell them apart.

The canonical example is the ordered set of rationals (ℚ, <) and the ordered set of reals (ℝ, <). These are clearly not isomorphic: ℚ is countable and ℝ is uncountable, so no bijection between them can preserve the ordering. Yet they are elementarily equivalent. Every first-order sentence true in (ℚ, <) is also true in (ℝ, <) and vice versa. To see why, consider what first-order sentences can express about a dense linear order without endpoints — sentences like "between any two elements there is another" or "there is no smallest element." Both ℚ and ℝ satisfy all such sentences. What first-order logic *cannot* express is "this order has cardinality ℵ₁" or "this order is complete" (in the real-analysis sense, where every bounded set has a supremum) — these require second-order or infinitary tools.

The conceptual point is that **first-order logic has limited expressive power**. There are many structural properties it simply cannot detect. Elementary equivalence captures exactly this limitation: two structures are elementarily equivalent when they agree on everything that first-order logic can express. From the perspective of your prior study of complete theories: M ≡ N if and only if Th(M) = Th(N), where Th(M) is the set of all first-order sentences true in M. This is the connection to complete theories — if T is a complete theory, then all models of T are elementarily equivalent to one another by definition, because they all satisfy exactly the sentences in T and no others.

**Elementary equivalence** is not just a curiosity; it is practically important for understanding when model-theoretic results are transferable. If you prove a property of one structure using first-order means, that same property holds in every elementarily equivalent structure. Conversely, if two structures differ in some property, and you cannot distinguish them by any first-order sentence, that property is provably beyond first-order expressibility. This is the starting point for Ehrenfeucht-Fraïssé games and the back-and-forth method, which give a combinatorial characterization of elementary equivalence that does not require comparing theories directly.

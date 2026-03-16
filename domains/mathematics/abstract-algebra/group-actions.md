---
id: group-actions
title: Group Actions
domain: mathematics
course: abstract-algebra
prerequisites:
- id: permutation-groups
  type: hard
builds-toward:
- orbit-stabilizer-theorem
- class-equation
tags:
- action
- group-acting
- orbit
- stabilizer
stage: advanced
status: draft
---

# Group Actions

## Core Idea
An action of a group G on a set X is a function G × X → X satisfying (gh)x = g(hx) and ex = x. Group actions formalize the notion of a group 'acting' on a set by transformations, unifying permutation groups, matrix groups, and abstract symmetries.

## Explainer

A **group action** takes the abstract machinery of group theory and puts it to concrete work. You've worked with permutation groups, where elements of S_n are bijections on {1, ..., n} and multiplication is composition. A group action generalizes this: instead of just the symmetric group, any abstract group G can "act" on any set X, provided the action respects G's multiplication structure. The formal definition captures exactly what "respects the group structure" means.

The two axioms do the essential work. The identity axiom, e·x = x, demands that the identity element act as a do-nothing transformation — every point stays fixed. The compatibility axiom, (gh)·x = g·(h·x), says that the combined element gh acts like applying h first, then g. Together, these make the map g ↦ (x ↦ g·x) a group homomorphism from G into Sym(X), the symmetric group on X. Even if you never write it this way, this connection is what justifies calling it a group action.

A concrete example helps. Let G = ℤ₄ = {0, 1, 2, 3} under addition, and let X = {v₁, v₂, v₃, v₄}, the four vertices of a square. Define k·vᵢ = v_{(i+k) mod 4}: element k rotates each vertex by 90k degrees. Check the axioms: 0·vᵢ = vᵢ (identity ✓); (j + k)·vᵢ = v_{i+j+k} = j·(k·vᵢ) (compatibility ✓). The **orbit** of v₁ under this action is {v₁, v₂, v₃, v₄} — every vertex is reachable from v₁ by some group element. The **stabilizer** of v₁ is {0} — only the identity fixes v₁.

A second example shows how G can act on itself by left multiplication: g·x = gx. Every element can reach every other element, so the orbit of any element is all of G, and the stabilizer of any element is {e}. This action is the basis of Cayley's theorem — every group is isomorphic to a subgroup of a symmetric group. The orbit-stabilizer theorem you'll study next says |Orb(x)| · |Stab(x)| = |G|. In the square example: |Orb(v₁)| · |Stab(v₁)| = 4 · 1 = 4 = |ℤ₄|. This counting identity turns group actions into a powerful tool for analyzing group structure, especially in the class equation and Sylow theorems.

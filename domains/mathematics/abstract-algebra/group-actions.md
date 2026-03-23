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
status: validated
---

# Group Actions

## Core Idea
An action of a group G on a set X is a function G × X → X satisfying (gh)x = g(hx) and ex = x. Group actions formalize the notion of a group 'acting' on a set by transformations, unifying permutation groups, matrix groups, and abstract symmetries.

## Questions

```yaml
- question: "G = ℤ₄ acts on the four vertices of a square by rotation. The orbit of vertex v₁ is {v₁, v₂, v₃, v₄} and the stabilizer of v₁ is {0}. What does the orbit-stabilizer theorem predict about |G|?"
  type: multiple-choice
  options:
    - "|G| = |Orb(v₁)| + |Stab(v₁)| = 4 + 1 = 5"
    - "|G| = |Orb(v₁)| × |Stab(v₁)| = 4 × 1 = 4"
    - "|G| = |Stab(v₁)|² = 1, since ℤ₄ acts freely on v₁"
    - "The theorem does not apply here because the action is transitive"
  answer: 1
  explanation: "The orbit-stabilizer theorem states |Orb(x)| · |Stab(x)| = |G| for any x in X. Here |Orb(v₁)| = 4 (all four vertices are reachable from v₁) and |Stab(v₁)| = 1 (only the identity fixes v₁), so 4 × 1 = 4 = |ℤ₄|. The formula multiplies, not adds. The theorem applies to all group actions — transitivity (a single orbit covering all of X) is not required; apply it element by element."

- question: "Which of the following correctly describes a group action of G on a set X?"
  type: multiple-choice
  options:
    - "A bijection σ: G → X assigning each group element a unique point in X"
    - "A function · : G × X → X satisfying e·x = x for all x, and (gh)·x = g·(h·x) for all g,h ∈ G and x ∈ X"
    - "Any function G × X → X, provided G is abelian and X is finite"
    - "A surjective group homomorphism from G onto the symmetric group Sym(X)"
  answer: 1
  explanation: "The definition requires two axioms: the identity axiom (e·x = x — the identity element acts trivially) and the compatibility axiom ((gh)·x = g·(h·x) — the group multiplication is compatible with the action). These axioms ensure that the map g ↦ (x ↦ g·x) is a group homomorphism G → Sym(X). Option A defines a function G → X, which is the wrong type. Option D describes an action only if the map is surjective, but actions need not induce surjections onto Sym(X)."

- question: "The axioms of a group action guarantee that each group element g induces a bijection on X — that is, the map x ↦ g·x is a permutation of X."
  type: true-false
  answer: true
  explanation: "The map φ_g: X → X defined by φ_g(x) = g·x has a two-sided inverse: φ_{g⁻¹}(x) = g⁻¹·x. The compatibility axiom gives φ_g(φ_{g⁻¹}(x)) = g·(g⁻¹·x) = (g g⁻¹)·x = e·x = x, and symmetrically in the other order. So every φ_g is a bijection, i.e., a permutation of X. This is precisely why the map G → Sym(X) sending g to φ_g is well-defined."

- question: "If a group G acts on a set X, there must be exactly one orbit — every element of X is reachable from every other by some group element."
  type: true-false
  answer: false
  explanation: "An action with a single orbit is called transitive, but this is a special case, not a requirement. In general, a group action partitions X into orbits, and there can be many. For example, G = ℤ₂ acting on X = {1, 2, 3, 4} by swapping 1↔2 and fixing 3 and 4 produces three orbits: {1,2}, {3}, and {4}. The orbit-stabilizer theorem applies to each orbit separately, and each orbit's size divides |G| by Lagrange's theorem."

- question: "State the two axioms of a group action and explain why they together imply that a group action defines a group homomorphism from G into Sym(X)."
  type: short-answer
  answer: "The two axioms are: (1) e·x = x for all x ∈ X (the identity acts trivially); (2) (gh)·x = g·(h·x) for all g,h ∈ G and x ∈ X (compatibility with group multiplication). To see why these define a homomorphism φ: G → Sym(X): define φ(g) to be the function x ↦ g·x. Axiom (1) ensures each φ(g) is invertible with inverse φ(g⁻¹), so φ(g) ∈ Sym(X). Axiom (2) ensures φ(gh)(x) = (gh)·x = g·(h·x) = φ(g)(φ(h)(x)), which means φ(gh) = φ(g)∘φ(h) — exactly the homomorphism condition."
  explanation: "This homomorphism perspective unifies all group actions: every action is secretly a way of representing G as a group of symmetries (permutations) of some set. Cayley's theorem is the special case where X = G and the action is left multiplication, showing every group embeds in its own symmetric group."
```

## Explainer

A **group action** takes the abstract machinery of group theory and puts it to concrete work. You've worked with permutation groups, where elements of S_n are bijections on {1, ..., n} and multiplication is composition. A group action generalizes this: instead of just the symmetric group, any abstract group G can "act" on any set X, provided the action respects G's multiplication structure. The formal definition captures exactly what "respects the group structure" means.

The two axioms do the essential work. The identity axiom, e·x = x, demands that the identity element act as a do-nothing transformation — every point stays fixed. The compatibility axiom, (gh)·x = g·(h·x), says that the combined element gh acts like applying h first, then g. Together, these make the map g ↦ (x ↦ g·x) a group homomorphism from G into Sym(X), the symmetric group on X. Even if you never write it this way, this connection is what justifies calling it a group action.

A concrete example helps. Let G = ℤ₄ = {0, 1, 2, 3} under addition, and let X = {v₁, v₂, v₃, v₄}, the four vertices of a square. Define k·vᵢ = v_{(i+k) mod 4}: element k rotates each vertex by 90k degrees. Check the axioms: 0·vᵢ = vᵢ (identity ✓); (j + k)·vᵢ = v_{i+j+k} = j·(k·vᵢ) (compatibility ✓). The **orbit** of v₁ under this action is {v₁, v₂, v₃, v₄} — every vertex is reachable from v₁ by some group element. The **stabilizer** of v₁ is {0} — only the identity fixes v₁.

A second example shows how G can act on itself by left multiplication: g·x = gx. Every element can reach every other element, so the orbit of any element is all of G, and the stabilizer of any element is {e}. This action is the basis of Cayley's theorem — every group is isomorphic to a subgroup of a symmetric group. The orbit-stabilizer theorem you'll study next says |Orb(x)| · |Stab(x)| = |G|. In the square example: |Orb(v₁)| · |Stab(v₁)| = 4 · 1 = 4 = |ℤ₄|. This counting identity turns group actions into a powerful tool for analyzing group structure, especially in the class equation and Sylow theorems.

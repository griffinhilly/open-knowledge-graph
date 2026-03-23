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
stage: expert
status: draft
---

# Elementary Equivalence: Logical Indistinguishability

## Core Idea
Two structures M and N are elementarily equivalent (M ≡ N) if they satisfy the same complete first-order theory: Th(M) = Th(N). This is weaker than isomorphism—elementarily equivalent structures may differ in cardinality and non-first-order properties, but no first-order sentence can distinguish them.

## How It's Best Learned
Show that (Q, <) and (R, <) are not isomorphic but are elementarily equivalent by describing the back-and-forth method at a high level.

## Questions

```yaml
- question: "The ordered set of rationals (ℚ, <) and the ordered set of reals (ℝ, <) have different cardinalities. Which of the following is correct?"
  type: multiple-choice
  options:
    - "They are not elementarily equivalent because they are not isomorphic"
    - "They are elementarily equivalent because every first-order sentence true in one is true in the other"
    - "They are elementarily equivalent only with respect to sentences involving the ordering relation"
    - "They cannot be compared by elementary equivalence because one is countable and the other is not"
  answer: 1
  explanation: "(ℚ, <) and (ℝ, <) are the canonical example of structures that are elementarily equivalent but not isomorphic. Both are dense linear orders without endpoints, and every first-order sentence expressible in the language of orders holds in both or neither. Cardinality is not a first-order expressible property — no single first-order sentence can say 'this structure has exactly ℵ₁ elements.' Option A is the classic misconception: elementary equivalence does not require isomorphism, only agreement on all first-order sentences."

- question: "Which of the following properties can NEVER be expressed by a single first-order sentence?"
  type: multiple-choice
  options:
    - "Between any two elements there exists another element"
    - "The structure has no smallest element"
    - "The structure has uncountably many elements"
    - "Every element has a successor"
  answer: 2
  explanation: "Cardinality above ℵ₀ is not first-order expressible. You can write first-order sentences saying 'there are at least n elements' for any fixed n, but there is no single first-order sentence that says 'there are uncountably many elements' — this would require quantification over sets or infinite conjunctions. Options A, B, and D are all first-order expressible: A is '∀x∀y(x < y → ∃z(x < z ∧ z < y))', B is '∀x∃y(y < x)', and D depends on the specific language but is expressible. This illustrates the limited expressive power of first-order logic that elementary equivalence captures."

- question: "If M and N are models of the same complete theory T, then M ≡ N."
  type: true-false
  answer: true
  explanation: "By definition, a complete theory T is a maximal consistent set of sentences — for every sentence φ, either φ ∈ T or ¬φ ∈ T. If both M and N are models of T, they satisfy exactly the sentences in T (and no sentences not in T, since T is complete). Therefore Th(M) = T = Th(N), which is exactly the definition of M ≡ N. This is the connection between elementary equivalence and complete theories: all models of a complete theory are elementarily equivalent."

- question: "Two structures that are elementarily equivalent must be isomorphic."
  type: true-false
  answer: false
  explanation: "Elementary equivalence is strictly weaker than isomorphism. Isomorphism requires a bijection preserving all structure; elementary equivalence only requires agreement on all first-order sentences. The counterexample is immediate: (ℚ, <) and (ℝ, <) are elementarily equivalent — no first-order sentence distinguishes them — but they cannot be isomorphic because ℚ is countable and ℝ is uncountable, and no bijection between them preserves the ordering. Isomorphic structures are always elementarily equivalent, but the converse fails."

- question: "Why can two structures be elementarily equivalent without being isomorphic? What does this reveal about first-order logic?"
  type: short-answer
  answer: "First-order logic has limited expressive power — it cannot express properties like cardinality, completeness (in the order-theoretic sense), or other 'global' structural features. Two structures can agree on every first-order sentence while differing in ways first-order logic cannot detect. This reveals that first-order logic is too weak to pin down a structure up to isomorphism unless additional constraints (like compactness and cardinality) are imposed. Elementary equivalence is the precise equivalence relation that captures exactly what first-order logic can and cannot distinguish."
  explanation: "This is the central lesson of elementary equivalence. The Löwenheim–Skolem theorem further confirms it: any first-order theory with an infinite model has models of every infinite cardinality. So no first-order theory can have exactly one infinite model up to isomorphism. Elementary equivalence is not a defect — it is the right tool for asking 'what does first-order logic see?' and for calibrating which results transfer between structures and which do not."
```

## Explainer

You already know that two structures can be **isomorphic** — that is, there is a bijection between their domains that perfectly preserves all relations, functions, and constants. Isomorphic structures are entirely interchangeable: every property of one holds for the other. **Elementary equivalence** is a strictly weaker notion. Two structures M and N are elementarily equivalent, written M ≡ N, if they satisfy exactly the same first-order sentences — the same complete theory. They might not be isomorphic, might have different cardinalities, might even "look different" in many ways, but no first-order formula can tell them apart.

The canonical example is the ordered set of rationals (ℚ, <) and the ordered set of reals (ℝ, <). These are clearly not isomorphic: ℚ is countable and ℝ is uncountable, so no bijection between them can preserve the ordering. Yet they are elementarily equivalent. Every first-order sentence true in (ℚ, <) is also true in (ℝ, <) and vice versa. To see why, consider what first-order sentences can express about a dense linear order without endpoints — sentences like "between any two elements there is another" or "there is no smallest element." Both ℚ and ℝ satisfy all such sentences. What first-order logic *cannot* express is "this order has cardinality ℵ₁" or "this order is complete" (in the real-analysis sense, where every bounded set has a supremum) — these require second-order or infinitary tools.

The conceptual point is that **first-order logic has limited expressive power**. There are many structural properties it simply cannot detect. Elementary equivalence captures exactly this limitation: two structures are elementarily equivalent when they agree on everything that first-order logic can express. From the perspective of your prior study of complete theories: M ≡ N if and only if Th(M) = Th(N), where Th(M) is the set of all first-order sentences true in M. This is the connection to complete theories — if T is a complete theory, then all models of T are elementarily equivalent to one another by definition, because they all satisfy exactly the sentences in T and no others.

**Elementary equivalence** is not just a curiosity; it is practically important for understanding when model-theoretic results are transferable. If you prove a property of one structure using first-order means, that same property holds in every elementarily equivalent structure. Conversely, if two structures differ in some property, and you cannot distinguish them by any first-order sentence, that property is provably beyond first-order expressibility. This is the starting point for Ehrenfeucht-Fraïssé games and the back-and-forth method, which give a combinatorial characterization of elementary equivalence that does not require comparing theories directly.

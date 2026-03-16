---
id: lowenheim-skolem-theorem
title: Löwenheim-Skolem Theorems
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: model-theory-basics
  type: hard
- id: fol-compactness
  type: soft
- id: cardinality-and-countability
  type: soft
builds-toward:
- godels-incompleteness-theorems
tags:
- Lowenheim-Skolem
- cardinality
- downward
- upward
- Skolem-paradox
stage: formal-systems
status: validated
---

# Löwenheim-Skolem Theorems

## Core Idea
The downward Löwenheim-Skolem theorem states that any first-order theory with an infinite model has a countable model. The upward version states that any theory with an infinite model of cardinality κ has models of every infinite cardinality λ ≥ κ. Together, these theorems show that first-order logic cannot pin down the cardinality of infinite structures: no first-order theory can uniquely characterize the real numbers or the natural numbers up to isomorphism. Skolem's paradox arises when set theory — which proves uncountable sets exist — itself has a countable model.

## How It's Best Learned
Prove the downward theorem using the Henkin construction and the fact that a countable language generates at most countably many terms. Then state the upward theorem via compactness and compare the philosophical implications.

## Common Misconceptions
- Skolem's paradox is not a contradiction: 'uncountable' is relative to a model — the countable model of set theory thinks some of its sets are uncountable because the bijection witnessing countability doesn't exist inside the model.
- The theorems do not apply to second-order logic, which can characterize the natural numbers categorically.

## Explainer

From your prerequisite work on **model theory basics** and **cardinality**, you know that a model of a first-order theory is a structure (a domain plus interpretations of the symbols) satisfying all the theory's axioms. A theory may have many non-isomorphic models. The Löwenheim-Skolem theorems describe how radically the *size* of these models can vary, and they reveal a fundamental limitation of first-order logic's expressive power.

The **downward Löwenheim-Skolem theorem** states: if a first-order theory T has an infinite model, it has a countably infinite model. The proof uses the Henkin construction. Given any model M of T, take a countable subset of M (possible because a countable language generates at most countably many terms and formulas) and close it under Skolem witnesses — for every existential formula ∃y φ(ā, y) true in M with parameters ā from the subset, add a witness element. The closure remains a model of T and is countable. The **upward Löwenheim-Skolem theorem** goes the other direction: if T has an infinite model of cardinality κ, it has a model of every infinite cardinality λ ≥ κ. This follows from the compactness theorem — add λ-many new constants and the type asserting all are distinct; every finite subset is satisfiable, so the whole theory is, giving a model of size λ.

Taken together, the theorems mean that first-order logic is **non-categorical** for any infinite structure: no first-order theory can uniquely pin down an infinite structure up to isomorphism. A theory intended to describe the real numbers has countable models. A theory intended to describe the natural numbers has uncountable models. This is deeply counterintuitive if you think of first-order theories as *defining* their subjects — they don't. They constrain models, but infinitely many non-isomorphic models always remain.

**Skolem's paradox** is the sharpest illustration. Zermelo-Fraenkel set theory (ZF) proves that uncountable sets exist — this is a theorem of ZF. Yet by the downward theorem, ZF has a countable model M. How can M contain "uncountable sets" while M itself is countable? The resolution: *uncountability is relative to a model*. The set S that M thinks is uncountable is uncountable *from M's perspective* because the bijection between S and ℕ does not exist *inside M*. That bijection exists in a larger model, but M cannot see it. "Uncountable" means "no bijection to ℕ *in this model*" — not an absolute fact about cardinality.

The philosophical lesson is precise: first-order logic's quantifiers range only over the domain of the current model. Statements like "there is a bijection" only look for bijections *inside the model*, not externally. This is why second-order logic, which can quantify over sets and functions directly, *can* characterize ℕ categorically (via Peano's second-order axioms) — but first-order logic cannot. The Löwenheim-Skolem theorems mark exactly where first-order expressivity runs out.

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

## Questions

```yaml
- question: "A logician claims to have written a first-order theory T that uniquely characterizes the real numbers — every model of T is isomorphic to ℝ. What do the Löwenheim-Skolem theorems say about this claim?"
  type: multiple-choice
  options:
    - "The claim is achievable if the axioms are sufficiently strong and the theory is complete"
    - "The claim is impossible — T must have countable models and models of every uncountable cardinality"
    - "The claim holds as long as T is consistent and has exactly one axiom about cardinality"
    - "The claim is possible only if T is a finite axiom system"
  answer: 1
  explanation: "The Löwenheim-Skolem theorems directly refute this claim. The downward theorem gives T a countable model (not isomorphic to ℝ, which is uncountable). The upward theorem gives T models of every infinite cardinality larger than |ℝ|. Since T has models of many different cardinalities, it cannot be categorical. First-order logic lacks the expressive power to pin down infinite cardinality — this is a theorem about the logic itself, independent of how clever or numerous T's axioms are."

- question: "ZFC set theory has a countable model M, yet M contains a set S that M considers uncountable. Which explanation correctly resolves this apparent contradiction?"
  type: multiple-choice
  options:
    - "M must be inconsistent — a consistent set theory cannot have a countable model"
    - "S is actually finite inside M; 'uncountable' is just M's word for large finite sets"
    - "S is uncountable relative to M because the bijection from S to ℕ does not exist inside M, even though it exists externally"
    - "ZFC's proof that uncountable sets exist is flawed and this is evidence of that"
  answer: 2
  explanation: "This is Skolem's paradox, resolved by recognizing that 'uncountable' is model-relative. M is externally countable (a bijection from M's domain to ℕ exists from outside), but the specific bijection witnessing that S is countable doesn't exist as a function inside M. Since M can only 'see' functions in its own domain, S appears uncountable from M's internal perspective. There is no contradiction — just a relativity of set-theoretic concepts to the model you're working in."

- question: "The upward Löwenheim-Skolem theorem implies that any consistent first-order theory with an infinite model has models of arbitrarily large infinite cardinality."
  type: true-false
  answer: true
  explanation: "The upward theorem states: if a theory has an infinite model of cardinality κ, it has models of every infinite cardinality λ ≥ κ. So having any infinite model at all guarantees models of every larger infinite size. Combined with the downward theorem (which provides countable models), the spectrum of model cardinalities is vast in both directions. No first-order theory can be categorical for any infinite structure."

- question: "The Löwenheim-Skolem theorems apply to second-order logic just as they do to first-order logic, showing that no formal logic can pin down the cardinality of infinite structures."
  type: true-false
  answer: false
  explanation: "The theorems apply specifically to first-order logic and do not hold for second-order logic. Second-order logic can quantify over sets and functions, not just individuals, which gives it dramatically greater expressive power. Peano's second-order axioms categorically characterize the natural numbers — every model is isomorphic to ℕ. The failure of categorical characterization is a feature of first-order expressivity specifically, not a universal fact about all logics."

- question: "Explain Skolem's paradox: how can ZFC, which proves uncountable sets exist, itself have a countable model? Is this a contradiction?"
  type: short-answer
  answer: "It is not a contradiction. ZFC proves '∃S such that no bijection from S to ℕ exists' — but the quantifier 'there exists a bijection' ranges only over functions inside the model. In a countable model M, a set S exists such that no bijection S → ℕ is an element of M. Externally, such a bijection exists (M itself is countable), but M cannot see it. So S is uncountable from M's internal perspective, and the theorem ZFC proves is true under that internal meaning of 'uncountable.' The resolution is that 'uncountable' is relative to a model, not an absolute fact."
  explanation: "The key insight is that logical quantifiers range only over the current model's domain. 'No bijection exists' means 'no bijection exists in this model.' This relativity of set-theoretic concepts to models is one of the deepest lessons in mathematical logic."
```

## Explainer

From your prerequisite work on **model theory basics** and **cardinality**, you know that a model of a first-order theory is a structure (a domain plus interpretations of the symbols) satisfying all the theory's axioms. A theory may have many non-isomorphic models. The Löwenheim-Skolem theorems describe how radically the *size* of these models can vary, and they reveal a fundamental limitation of first-order logic's expressive power.

The **downward Löwenheim-Skolem theorem** states: if a first-order theory T has an infinite model, it has a countably infinite model. The proof uses the Henkin construction. Given any model M of T, take a countable subset of M (possible because a countable language generates at most countably many terms and formulas) and close it under Skolem witnesses — for every existential formula ∃y φ(ā, y) true in M with parameters ā from the subset, add a witness element. The closure remains a model of T and is countable. The **upward Löwenheim-Skolem theorem** goes the other direction: if T has an infinite model of cardinality κ, it has a model of every infinite cardinality λ ≥ κ. This follows from the compactness theorem — add λ-many new constants and the type asserting all are distinct; every finite subset is satisfiable, so the whole theory is, giving a model of size λ.

Taken together, the theorems mean that first-order logic is **non-categorical** for any infinite structure: no first-order theory can uniquely pin down an infinite structure up to isomorphism. A theory intended to describe the real numbers has countable models. A theory intended to describe the natural numbers has uncountable models. This is deeply counterintuitive if you think of first-order theories as *defining* their subjects — they don't. They constrain models, but infinitely many non-isomorphic models always remain.

**Skolem's paradox** is the sharpest illustration. Zermelo-Fraenkel set theory (ZF) proves that uncountable sets exist — this is a theorem of ZF. Yet by the downward theorem, ZF has a countable model M. How can M contain "uncountable sets" while M itself is countable? The resolution: *uncountability is relative to a model*. The set S that M thinks is uncountable is uncountable *from M's perspective* because the bijection between S and ℕ does not exist *inside M*. That bijection exists in a larger model, but M cannot see it. "Uncountable" means "no bijection to ℕ *in this model*" — not an absolute fact about cardinality.

The philosophical lesson is precise: first-order logic's quantifiers range only over the domain of the current model. Statements like "there is a bijection" only look for bijections *inside the model*, not externally. This is why second-order logic, which can quantify over sets and functions directly, *can* characterize ℕ categorically (via Peano's second-order axioms) — but first-order logic cannot. The Löwenheim-Skolem theorems mark exactly where first-order expressivity runs out.

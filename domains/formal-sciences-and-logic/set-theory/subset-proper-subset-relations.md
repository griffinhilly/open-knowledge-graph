---
id: subset-proper-subset-relations
title: Subset and Proper Subset Relations
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: set-membership-and-notation
  type: hard
- id: set-equality-and-extensionality
  type: hard
- id: subsets-and-supersets-intro
  type: hard
builds-toward:
- power-set-and-boolean-operations
tags:
- subset
- ordering
- relations
stage: formal-systems
status: validated
---

# Subset and Proper Subset Relations

## Core Idea
Set A is a subset of B (A ⊆ B) if every element of A is in B; A is a proper subset (A ⊂ B) if A ⊆ B and A ≠ B. These relations form a partial order on sets and establish a hierarchy of containment. Note that ∅ ⊆ A for every set A.

## Questions

```yaml
- question: "Let A = {1, 2} and B = {1, 2, 3}. Which of the following correctly describes the relationship between A and B?"
  type: multiple-choice
  options:
    - "A ⊂ B and A ⊆ B are both true"
    - "A ⊆ B is true but A ⊂ B is false, because A and B share elements"
    - "A ⊂ B is true but A ⊆ B is false, because A is strictly smaller"
    - "Neither relation holds because A and B are different sets"
  answer: 0
  explanation: "Every element of A (1 and 2) is in B, so A ⊆ B is true. Additionally, B contains 3, which is not in A, so A ≠ B — making A ⊂ B (proper subset) also true. Proper subset (⊂) implies subset (⊆), just as strict less-than (<) implies less-than-or-equal (≤). Option B confuses 'sharing elements' with equality; option C misreads the implication direction — A ⊂ B guarantees A ⊆ B, not the other way around."

- question: "Is ∅ ⊆ ∅ true? Is ∅ ⊂ ∅ true?"
  type: multiple-choice
  options:
    - "Both are true — the empty set is a subset and proper subset of itself"
    - "∅ ⊆ ∅ is true, but ∅ ⊂ ∅ is false — the empty set is not a proper subset of itself"
    - "Both are false — the empty set has no elements, so no subset relations hold"
    - "∅ ⊂ ∅ is true, but ∅ ⊆ ∅ is false — only proper containment applies to equal sets"
  answer: 1
  explanation: "A ⊆ A is true for any set A (every element of A is trivially in A), so ∅ ⊆ ∅ is true. But A ⊂ A requires A ≠ A, which is never true — a set cannot be a proper subset of itself, just as no number satisfies n < n. So ∅ ⊂ ∅ is false. This mirrors the number analogy: 5 ≤ 5 is true, but 5 < 5 is false. The empty set is a proper subset of every NON-EMPTY set, but not of itself."

- question: "For any set A, the empty set ∅ is a subset of A."
  type: true-false
  answer: true
  explanation: "The definition of A ⊆ B is: for every x, if x ∈ A then x ∈ B. To show ∅ ⊄ A, you would need to exhibit an element of ∅ that is not in A — but ∅ has no elements, so no such counterexample exists. The subset condition is vacuously satisfied. This is not a technicality; it is the definition working as intended. The empty set belongs to the power set of every set precisely because of this vacuous inclusion."

- question: "The empty set is a proper subset of nearly every set."
  type: true-false
  answer: false
  explanation: "∅ is a proper subset of every NON-EMPTY set, but NOT of ∅ itself. The proper subset relation requires A ⊆ B AND A ≠ B. While ∅ ⊆ ∅ is true (vacuously), ∅ = ∅ is also true, so the second condition A ≠ B fails. Therefore ∅ ⊄ ∅ as a proper subset. The claim 'every set' is one element too many — ∅ itself is the exception. This subtle error trips up many students who correctly remember that ∅ is always a subset but incorrectly extend this to 'proper subset of every set.'"

- question: "Explain why the empty set is a subset of every set, using only the definition of subset."
  type: short-answer
  answer: "The definition of A ⊆ B is: for every element x, if x ∈ A then x ∈ B. To show ∅ ⊆ B for any set B, we must check: for every x in ∅, x ∈ B. Since ∅ contains no elements, there is nothing to check — the condition holds vacuously. There is no element of ∅ that could fail to be in B, so the definition is satisfied."
  explanation: "Vacuous truth is often counterintuitive but is consistent with classical logic: a universal statement 'for all x in A, P(x)' is true when A is empty, because there are no witnesses to falsify it. This is not a loophole or exception — it is the definition of subset working correctly. The practical consequence is that ∅ appears in the power set of every set, and any proof involving 'pick an arbitrary element of A' automatically handles the empty set case without extra work, since no element needs to be chosen."
```

## Explainer

You already know that set membership (∈) asks a yes-or-no question about a single element: is 3 ∈ {1, 2, 3}? The **subset relation** (⊆) lifts that question up one level and asks it about an entire set at once: is every member of A also a member of B? Think of it as a universal membership test applied collectively. If A = {2, 4} and B = {1, 2, 3, 4, 5}, then A ⊆ B because each element of A — namely 2 and 4 — passes the ∈ B test. Not one element is left out.

The distinction between **subset** (⊆) and **proper subset** (⊂) mirrors the distinction between ≤ and < for numbers. A ⊆ B allows A and B to be equal — if A = B, then A ⊆ B is still true, because every element of A is trivially in B. A proper subset (A ⊂ B) adds the extra requirement A ≠ B, meaning B contains at least one element A does not. This parallels the number analogy: just as 5 ≤ 5 is true but 5 < 5 is false, A ⊆ A is always true, but A ⊂ A is always false. Knowing which symbol you need — containment-or-equal versus strict containment — matters whenever you prove set-theoretic statements.

The **empty set** (∅) deserves special attention because it surprises most learners: ∅ ⊆ A for every set A, including ∅ ⊆ ∅. The reason flows directly from the definition. To show A is NOT a subset of B, you need to produce an element of A that fails to be in B. The empty set has no elements, so no such counterexample exists — the subset condition is vacuously satisfied. This isn't a technicality to memorize; it is the definition working exactly as intended, and you will rely on it repeatedly in proofs.

These relations form what mathematicians call a **partial order**: they are reflexive (A ⊆ A), antisymmetric (if A ⊆ B and B ⊆ A, then A = B — which you know from set equality and extensionality), and transitive (if A ⊆ B and B ⊆ C, then A ⊆ C). The partial order structure means you can draw a **Hasse diagram** of sets ordered by containment — a picture where lines go upward from smaller to larger sets. This diagram makes the containment hierarchy visual and will be essential when you study power sets, where every subset of A appears as a node in the diagram above ∅ and below A itself.

A practical reasoning pattern: to prove A ⊆ B, you pick an arbitrary element x, assume x ∈ A, and show x ∈ B. To prove A ⊄ B (A is not a subset), you exhibit a specific element in A that is not in B. This pattern — universal proof by element-chasing — is the workhorse of most set-theoretic arguments, and mastering it now will carry you through power sets, Boolean operations, and beyond.

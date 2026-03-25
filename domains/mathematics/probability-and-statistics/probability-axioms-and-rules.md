---
id: probability-axioms-and-rules
title: Probability Axioms and Rules
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: set-fundamentals
  type: hard
- id: weak-law-large-numbers
  type: soft
builds-toward:
- conditional-probability
- bayes-theorem
tags:
- probability
- foundations
stage: formal-systems
status: validated
---
# Probability Axioms and Rules

## Core Idea
Probability measures satisfy three axioms: P(S)=1 for sample space S, P(A)≥0 for any event A, and P(A∪B)=P(A)+P(B) for disjoint events. These axioms imply complement rule P(Aᶜ)=1−P(A) and general addition rule P(A∪B)=P(A)+P(B)−P(A∩B). All probability rules derive from these axioms.

## Questions

```yaml
- question: "Events A and B overlap, with P(A) = 0.5, P(B) = 0.4, and P(A ∩ B) = 0.2. What is P(A ∪ B)?"
  type: multiple-choice
  options:
    - "0.9"
    - "0.7"
    - "0.3"
    - "1.1"
  answer: 1
  explanation: "The general addition rule gives P(A ∪ B) = P(A) + P(B) − P(A ∩ B) = 0.5 + 0.4 − 0.2 = 0.7. The overlap is subtracted because P(A) and P(B) each already include the probability of the intersection, so adding them together counts P(A ∩ B) twice."

- question: "For any two events A and B, P(A ∪ B) = P(A) + P(B)."
  type: true-false
  answer: false
  explanation: "This formula only holds when A and B are disjoint (mutually exclusive) — i.e., P(A ∩ B) = 0. For overlapping events, the correct formula is P(A ∪ B) = P(A) + P(B) − P(A ∩ B). Applying the simpler formula to overlapping events overcounts the shared outcomes and can even produce probabilities greater than 1."

- question: "Using only the three Kolmogorov axioms, explain why P(∅) = 0."
  type: short-answer
  answer: "The sample space S and the empty set ∅ are disjoint (they share no outcomes), and their union is S. By axiom 3, P(S ∪ ∅) = P(S) + P(∅). Since S ∪ ∅ = S, we have P(S) = P(S) + P(∅), which forces P(∅) = 0."
  explanation: "This derivation shows that P(∅) = 0 is not a separate assumption — it follows from the three axioms. The key move is recognizing that S and ∅ satisfy the disjointness condition in axiom 3 (A ∩ B = ∅ is trivially true when one set is empty), allowing the additive rule to apply."
```

## Explainer

Before Kolmogorov's 1933 formalization, probability was intuitive but mathematically inconsistent — different approaches sometimes yielded contradictory results. The Kolmogorov axioms resolved this by providing a minimal foundation: three rules that every valid probability measure must satisfy, from which everything else can be derived. Your work with sets gives you exactly the language needed to state and understand them.

The three axioms are: (1) for any event A, P(A) ≥ 0 (probabilities are non-negative); (2) P(S) = 1, where S is the sample space (something must happen); (3) if A and B are disjoint — A ∩ B = ∅ — then P(A ∪ B) = P(A) + P(B) (disjoint events add). Notice that "event" is just a set of outcomes, "disjoint" is the set-theoretic term you already know, and "union" is the set union operator. The axioms are abstract enough to apply to any sample space, not just coin flips or dice.

From these three axioms you can derive every other rule. The complement rule follows directly: since A and Aᶜ are disjoint and A ∪ Aᶜ = S, axiom 3 gives P(A) + P(Aᶜ) = P(S) = 1, so P(Aᶜ) = 1 − P(A). The rule P(∅) = 0 follows because S and ∅ are disjoint and S ∪ ∅ = S, giving P(S) = P(S) + P(∅), which forces P(∅) = 0. These derivations are not just exercises — they illustrate how much structure emerges from very few assumptions.

The general addition rule — P(A ∪ B) = P(A) + P(B) − P(A ∩ B) — handles overlapping events. The subtraction corrects for double-counting: when you add P(A) and P(B), outcomes in the intersection are counted once in each term, so they appear twice in the sum. Subtracting P(A ∩ B) once restores the correct count. This is the probabilistic version of inclusion-exclusion from set counting, which you may have seen with Venn diagrams.

A persistent misconception is applying P(A ∪ B) = P(A) + P(B) to all events. This only works when A and B cannot both occur (they are mutually exclusive). For overlapping events it overcounts — and can even produce probabilities exceeding 1. The habit to build is: before adding probabilities, always ask whether the events are disjoint. If they are not, you must subtract the intersection.

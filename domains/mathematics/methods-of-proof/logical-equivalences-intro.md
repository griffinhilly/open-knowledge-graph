---
id: logical-equivalences-intro
title: Logical Equivalences and Laws
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-tables-intro
  type: hard
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- conditional-and-biconditional-statements
- proof-by-contrapositive
tags:
- logic
- equivalence
- simplification
stage: formal-systems
status: validated
---

# Logical Equivalences and Laws

## Core Idea
Two statements are logically equivalent if they have identical truth values in all possible conditions. Key laws like De Morgan's laws, commutativity, and associativity allow us to transform and simplify logical statements while preserving their logical content. These transformations are essential tools for proof techniques.

## Questions

```yaml
- question: "A student claims that 'P → Q' and 'Q → P' are logically equivalent because 'both statements relate P and Q.' Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — both statements link P and Q, so they share the same truth conditions"
    - "No — 'if P then Q' and 'if Q then P' have different truth tables and are not equivalent"
    - "Yes — they are equivalent whenever P and Q are both true or both false"
    - "No — but only because implication is not commutative by convention"
  answer: 1
  explanation: "P → Q and Q → P are not logically equivalent — they are in fact each other's converse, and converses can have different truth values. P → Q is false only when P is true and Q is false. Q → P is false only when Q is true and P is false. Consider P = 'it is raining' and Q = 'the ground is wet': 'if it rains, the ground is wet' (P → Q) can be true while 'if the ground is wet, it rained' (Q → P) is false (sprinklers). The contrapositive ¬Q → ¬P is equivalent to P → Q — not the converse Q → P."

- question: "Which transformation correctly applies De Morgan's law to simplify ¬(A ∧ B)?"
  type: multiple-choice
  options:
    - "¬A ∧ ¬B"
    - "¬A ∨ ¬B"
    - "A ∨ B"
    - "¬A ∧ B"
  answer: 1
  explanation: "De Morgan's first law states ¬(P ∧ Q) ≡ ¬P ∨ ¬Q: the negation of a conjunction is the disjunction of the negations. The negation distributes inward and the connective flips from AND to OR. Option A (¬A ∧ ¬B) is the wrong law — it would apply to ¬(A ∨ B), not ¬(A ∧ B). De Morgan's laws are the primary tool for pushing negations inward through compound statements, which is essential in both proof writing and circuit simplification."

- question: "Two statements that agree in truth value for some — but not all — assignments of truth values to their variables are NOT logically equivalent."
  type: true-false
  answer: true
  explanation: "True. Logical equivalence is an all-or-nothing standard: P ≡ Q requires that the truth tables of P and Q are identical in every row — every possible assignment of truth values to atomic variables. If there is even one row where they differ, they are not equivalent. This is stricter than 'often agreeing' or 'agreeing in typical cases.' The symbol ≡ means 'is the same logical object, expressed differently.'"

- question: "Proving 'if P then Q' is logically equivalent to proving 'if Q then P,' so either can substitute for the other in a mathematical proof."
  type: true-false
  answer: false
  explanation: "False — this confuses the contrapositive with the converse. P → Q is logically equivalent to its contrapositive ¬Q → ¬P (not Q implies not P). It is NOT equivalent to Q → P (the converse). Only the contrapositive can substitute for the original conditional in a proof. Confusing the two is a serious logical error: assuming the converse is true because the original is true is the fallacy of affirming the consequent."

- question: "A student wants to prove: 'If n² is even, then n is even.' They find the direct approach difficult and instead prove: 'If n is odd, then n² is odd.' Explain why this alternative proof is logically valid, using the concept of logical equivalence."
  type: short-answer
  answer: "The alternative proof proves the contrapositive of the original statement. The original is P → Q where P = 'n² is even' and Q = 'n is even.' The contrapositive is ¬Q → ¬P: 'If n is not even (i.e., n is odd), then n² is not even (i.e., n² is odd).' By the contrapositive equivalence, (P → Q) ≡ (¬Q → ¬P), so proving the contrapositive is logically identical to proving the original — they have the same truth table. This is proof by contrapositive: when the direct route is hard, switch to the equivalent contrapositive form."
  explanation: "The contrapositive equivalence is one of the most practically useful logical equivalences in mathematics. Direct proofs sometimes require constructing n from knowing n² is even, which is awkward. The contrapositive form — start by assuming n is odd, then show n² must also be odd — is straightforward by direct computation: if n = 2k+1, then n² = 4k²+4k+1 = 2(2k²+2k)+1, which is odd. Same logical content, much cleaner proof."
```

## Explainer

From your work with truth tables, you know how to evaluate a compound statement row by row. **Logical equivalence** goes one step further: two statements P and Q are logically equivalent (written P ≡ Q) if their truth tables are identical — every possible assignment of truth values to the atomic components produces the same result for both P and Q. This is not just "they usually agree" — they must agree in every case, with no exceptions. The symbol ≡ means "is the same logical object as," just expressed differently.

Think of logical equivalences as algebraic identities for logic. Just as the algebraic identity a(b + c) = ab + ac lets you rewrite expressions without changing their value, logical laws let you rewrite compound statements into equivalent but simpler or more useful forms. The most important laws are **De Morgan's laws**: ¬(P ∧ Q) ≡ ¬P ∨ ¬Q, and ¬(P ∨ Q) ≡ ¬P ∧ ¬Q. In words: "not (A and B)" means "not A or not B"; "not (A or B)" means "not A and not B." These let you push negations inward through conjunctions and disjunctions, a maneuver you will use constantly in proofs.

Other essential equivalences include: commutativity (P ∧ Q ≡ Q ∧ P), associativity, distributivity, double negation (¬¬P ≡ P), and the **contrapositive** equivalence (P → Q) ≡ (¬Q → ¬P). The contrapositive equivalence is particularly powerful: it says that proving "if P then Q" is logically identical to proving "if not Q then not P." When the direct route (assume P, prove Q) is difficult, you can flip to the contrapositive form without changing what you're proving. This is proof by contrapositive — one of the core techniques your next topics cover.

Logical equivalences also give you a mechanical way to simplify premises and conclusions. If you have a complex hypothesis like ¬(P ∧ ¬Q), De Morgan's law turns it into ¬P ∨ Q, which by another equivalence is just P → Q. That simplification can make the structure of a proof much clearer. Mastering these transformations means you can fluidly rewrite any logical statement into whatever form is most convenient — direct, contrapositive, or proof by contradiction — without losing logical content.

---
id: logical-equivalence-propositional
title: Logical Equivalence in Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: truth-assignments-and-valuations
  type: hard
- id: logical-equivalence-formulas
  type: soft
builds-toward:
- normal-forms-cnf-dnf
- logical-equivalences
tags:
- semantics
- equivalence
- propositional
stage: formal-systems
status: validated
---
# Logical Equivalence in Propositional Logic

## Core Idea
Two formulas are logically equivalent if they have the same truth value under every possible truth assignment. Equivalence allows formulas to be substituted for one another and enables simplification. Standard equivalences include De Morgan's laws, double negation, and distributivity.

## How It's Best Learned
Verify equivalences using truth tables. Learn standard equivalence laws and apply them to rewrite and simplify formulas.

## Common Misconceptions
Confusing logical equivalence with material implication. Assuming formulas that 'sound similar' in English are equivalent.

## Questions

```yaml
- question: "Is P → Q logically equivalent to Q → P?"
  type: multiple-choice
  options:
    - "Yes — implications are symmetric, just like equality"
    - "No — P → Q can be true while Q → P is false; consider P = 'it rained' and Q = 'the ground is wet'"
    - "Yes — if P implies Q, then Q must imply P by the definition of logical consequence"
    - "Only if both P and Q are tautologies"
  answer: 1
  explanation: "P → Q and Q → P are NOT equivalent — Q → P is the converse of P → Q, and converses are not logically equivalent to the original in general. Consider P = T, Q = F: P → Q is false, but Q → P is true. Or by truth table: when P is false and Q is true, P → Q is true but Q → P is false. The confusion between an implication and its converse is one of the most common logical errors. P → Q is equivalent instead to its contrapositive: ¬Q → ¬P."

- question: "You want to verify that ¬(P ∧ Q) ≡ (¬P ∨ ¬Q) (De Morgan's first law). What is the correct procedure?"
  type: multiple-choice
  options:
    - "Prove that both ¬(P ∧ Q) and (¬P ∨ ¬Q) are tautologies individually"
    - "Find at least one truth assignment that makes both formulas true simultaneously"
    - "Construct a joint truth table and verify that the two formula columns match in every row"
    - "Show that ¬(P ∧ Q) → (¬P ∨ ¬Q) holds under all assignments"
  answer: 2
  explanation: "Logical equivalence means identical truth values under EVERY truth assignment — the two formula columns in a joint truth table must match in all rows. Option A is wrong because individual tautologies are not needed (neither formula is a tautology). Option B is insufficient — one matching row doesn't establish equivalence across all assignments. Option D checks only one direction of implication; equivalence requires both φ → ψ AND ψ → φ. Only the full truth table comparison is decisive."

- question: "If two formulas are logically equivalent, you can substitute one for the other within any larger formula without changing the truth value of the whole."
  type: true-false
  answer: true
  explanation: "This substitution property is precisely what makes logical equivalence useful. Because φ ≡ ψ means they agree on every truth assignment, replacing one with the other in any context preserves truth values throughout. For example, since P → Q ≡ ¬P ∨ Q, you can always rewrite implications as disjunctions. This substitution principle underlies all formula simplification and the conversion to normal forms like CNF and DNF."

- question: "If φ → ψ holds for nearly every truth assignment (φ logically implies ψ), then φ and ψ are logically equivalent."
  type: true-false
  answer: false
  explanation: "Implication (φ → ψ) is one-directional: in every assignment where φ is true, ψ is also true — but ψ can be true even when φ is false. Equivalence (φ ≡ ψ) requires both φ → ψ AND ψ → φ. Example: P → (P ∨ Q) holds for all assignments (P logically implies P ∨ Q), but they are not equivalent — when P is false and Q is true, P ∨ Q is true while P is false. Equivalence is mutual implication; one-way implication is strictly weaker."

- question: "What is the difference between logical equivalence (φ ≡ ψ) and material implication (φ → ψ)? Give a concrete example showing that implication does not guarantee equivalence."
  type: short-answer
  answer: "Logical equivalence φ ≡ ψ means φ and ψ have identical truth values under every truth assignment — they always agree. Material implication φ → ψ means: whenever φ is true, ψ is also true — but ψ can be true when φ is false. Example: P → (P ∨ Q) holds for all assignments (it's a tautology), so P logically implies P ∨ Q. But they are not equivalent: when P = false and Q = true, P ∨ Q = true while P = false — different truth values, so no equivalence."
  explanation: "The distinction matters enormously in proofs and formal reasoning. Equivalence licenses bidirectional substitution; implication licenses only one-directional inference. In mathematics, proving A ↔ B (equivalence) requires two separate proofs: A → B and B → A. Proving just one direction gives you implication, not equivalence. Many student errors in logic proofs come from treating a one-way proof as establishing equivalence."
```

## Explainer

You already know how truth assignments work: a truth assignment maps each propositional variable to true or false, and the truth value of a compound formula is determined compositionally by the connectives. **Logical equivalence** builds directly on this. Two formulas φ and ψ are **logically equivalent**, written φ ≡ ψ, if for every possible truth assignment, φ and ψ receive the same truth value — they always agree, no matter what the variables are set to. The standard way to check this is a joint truth table: if φ and ψ have matching columns across all rows, they are equivalent.

The payoff of equivalence is **substitution**: wherever φ appears in a larger formula, you can replace it with ψ without changing the truth value of the whole. This is what makes equivalence useful for simplification. Consider De Morgan's first law: ¬(P ∧ Q) ≡ (¬P ∨ ¬Q). If you have a complex formula containing ¬(P ∧ Q), you can swap in (¬P ∨ ¬Q) freely. Standard equivalences — double negation (¬¬P ≡ P), commutativity, associativity, distribution, De Morgan's laws, implication as disjunction (P → Q ≡ ¬P ∨ Q) — are the rewrite rules you use to put formulas into simpler or canonical forms.

A key equivalence worth internalizing is the **implication** form: P → Q is not "P causes Q" or "P is similar to Q." It is equivalent to ¬P ∨ Q — the formula is false only when P is true and Q is false. This surprises many students because natural language "if-then" is not purely truth-functional. In logic, "if the moon is made of cheese, then 2+2=4" is true, because the antecedent is false. Recognizing P → Q ≡ ¬P ∨ Q lets you manipulate implications using the toolkit of disjunction.

The difference between **logical equivalence** and **material implication** is critical. φ → ψ says: in every assignment that makes φ true, ψ is also true — but ψ might be false when φ is false. φ ≡ ψ says: in every assignment, φ and ψ have the same truth value — they go up and down together. Equivalence is mutual implication: φ ≡ ψ holds if and only if both φ → ψ and ψ → φ hold. If you ever doubt whether two formulas are equivalent, the truth table test is decisive for propositional logic: equivalence fails if even one assignment produces different truth values for the two formulas.
